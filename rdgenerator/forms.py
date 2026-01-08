from django import forms
from PIL import Image

class GenerateForm(forms.Form):
    #Platform
    platform = forms.ChoiceField(choices=[('windows','Windows 64Bit'),('windows-x86','Windows 32Bit'),('linux','Linux'),('android','Android'),('macos','macOS')], initial='windows')
    version = forms.ChoiceField(choices=[('master','nightly'),('1.4.5','1.4.5'),('1.4.4','1.4.4'),('1.4.3','1.4.3'),('1.4.2','1.4.2'),('1.4.1','1.4.1'),('1.4.0','1.4.0'),('1.3.9','1.3.9'),('1.3.8','1.3.8'),('1.3.7','1.3.7'),('1.3.6','1.3.6'),('1.3.5','1.3.5'),('1.3.4','1.3.4'),('1.3.3','1.3.3')], initial='1.4.4')
    help_text="'master' is the development version (nightly build) with the latest features but may be less stable"
    delayFix = forms.BooleanField(initial=True, required=False)

    #General
    exename = forms.CharField(label="EXE 파일 이름", required=True)
    appname = forms.CharField(label="맞춤형 앱 이름", required=False)
    direction = forms.ChoiceField(widget=forms.RadioSelect, choices=[
        ('incoming', '수신 전용'),
        ('outgoing', '발신 전용'),
        ('both', '양방향')
    ], initial='both')
    installation = forms.ChoiceField(label="설치 비활성화", choices=[
        ('installationY', '아니요, 설치를 활성화합니다.'),
        ('installationN', '예, 설치를 비활성화합니다.')
    ], initial='installationY')
    settings = forms.ChoiceField(label="설정 비활성화", choices=[
        ('settingsY', '아니요, 설정을 활성화합니다.'),
        ('settingsN', '예, 설정을 비활성화합니다.')
    ], initial='settingsY')
    androidappid = forms.CharField(label="사용자 지정 안드로이드 앱 ID(기존 'com.carriez.flutter_hbb' 대체)", required=False)

    #Custom Server
    serverIP = forms.CharField(label="호스트", required=False)
    apiServer = forms.CharField(label="API 서버", required=False)
    key = forms.CharField(label="키", required=False)
    urlLink = forms.CharField(label="링크용 맞춤 URL", required=False)
    downloadLink = forms.CharField(label="새 버전 다운로드를 위한 사용자 지정 URL", required=False)
    compname = forms.CharField(label="회사명",required=False)

    #Visual
    iconfile = forms.FileField(label="맞춤형 앱 아이콘(.png 형식)", required=False, widget=forms.FileInput(attrs={'accept': 'image/png'}))
    logofile = forms.FileField(label="맞춤형 앱 로고(.png 형식)", required=False, widget=forms.FileInput(attrs={'accept': 'image/png'}))
    iconbase64 = forms.CharField(required=False)
    logobase64 = forms.CharField(required=False)
    theme = forms.ChoiceField(choices=[
        ('light', '밝게'),
        ('dark', '어둡게'),
        ('system', '시스템 기본값')
    ], initial='system')
    themeDorO = forms.ChoiceField(choices=[('default', '기본값'),('override', '재정의')], initial='default')

    #Security
    passApproveMode = forms.ChoiceField(choices=[('password','비밀번호를 통해 세션 수락'),('click','클릭을 통해 세션 수락'),('password-click','두 가지 모두를 통한 세션 허용')],initial='password-click')
    permanentPassword = forms.CharField(widget=forms.PasswordInput(), required=False)
    #runasadmin = forms.ChoiceField(choices=[('false','No'),('true','Yes')], initial='false')
    denyLan = forms.BooleanField(initial=False, required=False)
    enableDirectIP = forms.BooleanField(initial=False, required=False)
    #ipWhitelist = forms.BooleanField(initial=False, required=False)
    autoClose = forms.BooleanField(initial=False, required=False)

    #Permissions
    permissionsDorO = forms.ChoiceField(choices=[('default', '기본값'),('override', '재정의')], initial='default')
    permissionsType = forms.ChoiceField(choices=[('custom', '사용자 정의'),('full', '전체 액세스'),('view','화면 공유')], initial='custom')
    enableKeyboard =  forms.BooleanField(initial=True, required=False)
    enableClipboard = forms.BooleanField(initial=True, required=False)
    enableFileTransfer = forms.BooleanField(initial=True, required=False)
    enableAudio = forms.BooleanField(initial=True, required=False)
    enableTCP = forms.BooleanField(initial=True, required=False)
    enableRemoteRestart = forms.BooleanField(initial=True, required=False)
    enableRecording = forms.BooleanField(initial=True, required=False)
    enableBlockingInput = forms.BooleanField(initial=True, required=False)
    enableRemoteModi = forms.BooleanField(initial=False, required=False)
    hidecm = forms.BooleanField(initial=False, required=False)
    enablePrinter = forms.BooleanField(initial=True, required=False)
    enableCamera = forms.BooleanField(initial=True, required=False)
    enableTerminal = forms.BooleanField(initial=True, required=False)

    #Other
    removeWallpaper = forms.BooleanField(initial=True, required=False)

    defaultManual = forms.CharField(widget=forms.Textarea, required=False)
    overrideManual = forms.CharField(widget=forms.Textarea, required=False)

    #custom added features
    cycleMonitor = forms.BooleanField(initial=False, required=False)
    xOffline = forms.BooleanField(initial=False, required=False)
    removeNewVersionNotif = forms.BooleanField(initial=False, required=False)

    def clean_iconfile(self):
        print("checking icon")
        image = self.cleaned_data['iconfile']
        if image:
            try:
                # Open the image using Pillow
                img = Image.open(image)

                # Check if the image is a PNG (optional, but good practice)
                if img.format != 'PNG':
                    raise forms.ValidationError("PNG 이미지만 허용됩니다.")

                # Get image dimensions
                width, height = img.size

                # Check for square dimensions
                if width != height:
                    raise forms.ValidationError("사용자 지정 앱 아이콘의 크기는 정사각형이어야 합니다.")
                
                return image
            except OSError:  # Handle cases where the uploaded file is not a valid image
                raise forms.ValidationError("잘못된 아이콘 파일입니다.")
            except Exception as e: # Catch any other image processing errors
                raise forms.ValidationError(f"아이콘 오류 처리: {e}")
