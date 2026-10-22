import json, sys, base64, subprocess, urllib.request, re, os
KEY=open("/root/.podcast/gemini_key").read().strip()
TEMPO=os.environ.get("TEMPO","1.1")
MODEL=os.environ.get("TTS_MODEL","gemini-3.8-flash-tts")
VF=os.environ.get("VOICE_MIRA","Aoede"); VM=os.environ.get("VOICE_JAN","Charon")
STYLE=("Lies das folgende Gespräch als lockeren, deutschsprachigen Lern-Podcast vor. "
       "Mira und Jan sind zwei gut gelaunte Kollegen, die sich gegenseitig zuhören und natürlich aufeinander reagieren. "
       "Ruhiges, angenehmes Sprechtempo, gut verständlich beim Spazierengehen.")
def tts(dialog, out_wav):
    parts=[]
    for l in dialog.splitlines():
        sp,t=l.split(":",1); parts.append({"text":t.strip(),"speechMetadata":{"speaker":sp}})
    body={"contents":[{"role":"user","parts":parts}],
          "generationConfig":{"responseModalities":["AUDIO"],"speechConfig":{"multiSpeakerVoiceConfig":{"speakerVoiceConfigs":[
            {"speaker":"Mira","voiceConfig":{"prebuiltVoiceConfig":{"voiceName":VF}}},
            {"speaker":"Jan","voiceConfig":{"prebuiltVoiceConfig":{"voiceName":VM}}}]}}}}
    req=urllib.request.Request(f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent",
        data=json.dumps(body).encode(),headers={"Content-Type":"application/json","x-goog-api-key":KEY})
    for attempt in range(3):
        try:
            d=json.load(urllib.request.urlopen(req,timeout=600)); break
        except Exception as e:
            err=e.read().decode()[:500] if hasattr(e,"read") else str(e); print("retry",attempt,err,file=sys.stderr)
            if "400" in str(e): raise SystemExit("TTS bad request")
    else: raise SystemExit("TTS failed")
    pcm=b"".join(base64.b64decode(p["inlineData"]["data"]) for p in d["candidates"][0]["content"]["parts"] if "inlineData" in p)
    subprocess.run(["ffmpeg","-y","-loglevel","error","-f","s16le","-ar","24000","-ac","1","-i","-",out_wav],input=pcm,check=True)
    return d.get("usageMetadata",{})
def chunks(script, max_chars=4000):
    lines=[l for l in open(script,encoding="utf-8").read().splitlines() if re.match(r"^(MIRA|JAN):",l)]
    lines=[("Mira" if l.startswith("MIRA") else "Jan")+":"+l.split(":",1)[1] for l in lines]
    cur=[];n=0
    for l in lines:
        if n+len(l)>max_chars and cur: yield "\n".join(cur); cur=[];n=0
        cur.append(l); n+=len(l)
    if cur: yield "\n".join(cur)
if __name__=="__main__":
    script,out=sys.argv[1],sys.argv[2]; limit=int(sys.argv[3]) if len(sys.argv)>3 else 999
    tmp=os.path.splitext(out)[0]+"_parts"; os.makedirs(tmp,exist_ok=True); parts=[]
    for i,c in enumerate(chunks(script)):
        if i>=limit: break
        f=f"{tmp}/{i:02d}.wav"; u=tts(c,f); parts.append(f); print("chunk",i,len(c),"chars",u,file=sys.stderr)
    args=["ffmpeg","-y","-loglevel","error"]
    for f in parts: args+=["-i",f]
    filt="".join(f"[{i}:a]apad=pad_dur=0.4[a{i}];" for i in range(len(parts)))+"".join(f"[a{i}]" for i in range(len(parts)))+f"concat=n={len(parts)}:v=0:a=1,atempo={TEMPO},loudnorm=I=-16:TP=-1.5[o]"
    subprocess.run(args+["-filter_complex",filt,"-map","[o]","-ac","1","-b:a","96k",out],check=True)
    print("done",out)
