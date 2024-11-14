from django import forms

class GenerateForm(forms.Form):
    #Platform
    platform = forms.ChoiceField(choices=[('windows','Windows'),('linux','Linux (currently unavailable)'),('android','Android (testing now available)')], initial='windows')
    version = forms.ChoiceField(choices=[('nightly','nightly'),('master','beta'),('1.3.2','1.3.2'),('1.3.1','1.3.1'),('1.3.0','1.3.0')], initial='1.3.2')
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

    #Custom Server
    serverIP = forms.CharField(label="호스트", required=False)
    apiServer = forms.CharField(label="API 서버", required=False)
    key = forms.CharField(label="키", required=False)
    urlLink = forms.CharField(label="링크용 맞춤 URL", required=False)

    #Visual
    iconfile = forms.FileField(label="맞춤형 앱 아이콘(.png 형식)", required=False, widget=forms.FileInput(attrs={'accept': 'image/png'}))
    logofile = forms.FileField(label="맞춤형 앱 로고(.png 형식)", required=False, widget=forms.FileInput(attrs={'accept': 'image/png'}))
    theme = forms.ChoiceField(choices=[
        ('light', '밝게'),
        ('dark', '어둡게'),
        ('system', '시스템 기본값')
    ], initial='system')
    themeDorO = forms.ChoiceField(choices=[('default', '기본값'),('override', '재정의')], initial='default')

    #Security
    passApproveMode = forms.ChoiceField(choices=[('password','비밀번호를 통해 세션 수락'),('click','클릭을 통해 세션 수락'),('password-click','두 가지 모두를 통한 세션 허용')],initial='password-click')
    permanentPassword = forms.CharField(widget=forms.PasswordInput(), required=False)
    runasadmin = forms.ChoiceField(choices=[('false','아니오'),('true','예')], initial='false')
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

    #Other
    removeWallpaper = forms.BooleanField(initial=True, required=False)

    defaultManual = forms.CharField(widget=forms.Textarea, required=False)
    overrideManual = forms.CharField(widget=forms.Textarea, required=False)
