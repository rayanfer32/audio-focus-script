from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
import pyautogui
import time

sessions = AudioUtilities.GetAllSessions()
MIN_VOL = 0.1
MAX_VOL = 1
webexApps = ['atmgr.exe', 'ptoneclk.exe']
braveApps = ['brave.exe']

def setAudioFocus(appName):
    allApps = getProcessNames(sessions)

    # set focus to one app and set MIN_VOL to all other apps    
    for app in allApps:
        setAppVolume(app,MIN_VOL)
    setAppVolume(appName,MAX_VOL)
    


def setAppVolume(appName, volume_val):
    isAppRunning = False
    for session in sessions:
        if session.Process:
            processName = session.Process.name()
            if processName == appName:
                isAppRunning = True
                volume = session._ctl.QueryInterface(ISimpleAudioVolume)
                volume.SetMasterVolume(volume_val,None)
                print(processName,':',volume.GetMasterVolume())
    if(not isAppRunning):
        raise Exception(f'{appName} is not running / not found!')
    return isAppRunning

def getProcessNames(sessions):
    apps = []
    for session in sessions:
        if session.Process:
            apps.append( session.Process.name() )
    return apps

# for appl in webexApps:
#     setAppVolume(appl,1)

print(getProcessNames(sessions))


if __name__ == "__main__":
    while True:
        try:
            pos = pyautogui.position()
            print(pos.x)
            
            if(pos.x > 0):
                # focus brave audio
                setAudioFocus('brave.exe')
            else:
                # focus webex audio
                setAudioFocus('atmgr.exe')
            
            time.sleep(0.5)
        except Exception as e:
            print(e)