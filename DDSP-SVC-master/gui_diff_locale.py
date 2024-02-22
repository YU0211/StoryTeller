import locale
'''
本地化方式如下所示
'''

LANGUAGE_LIST = ['zh_CN', 'en_US', 'ja_JP']
LANGUAGE_ALL = {
    'zh_CN': {
        'SUPER': 'END',
        'LANGUAGE': 'zh_CN',
        '選擇模型文件': '選擇模型文件',
        'DDSP模型（4.0版本及以後可以不需要）:': 'DDSP 模型(4.0版本及以後可以不需要)',
        '選擇配置文件所在目錄': '選擇配置文件所在目錄',
        '打開文件夾': '打開文件夾',
        '讀取配置文件': '讀取配置文件',
        '保存配置文件': '保存配置文件',
        '快速配置文件': '快速配置文件',
        '輸入設備': '輸入設備',
        '輸出設備': '輸出設備',
        '音訊設備': '音訊設備',
        '說話人id': '說話人id',
        '響應閾值': '響應閾值',
        '變調': '變調',
        '採樣率': '採樣率',
        '啟用捏音色功能': '啟用捏音色功能',
        '設置混合音色': '設置混合音色',
        '普通設置': '普通設置',
        '音訊切分大小': '音訊切分大小',
        '交叉淡化時長': '交叉淡化時長',
        '使用歷史區塊數量': '使用歷史區塊數量',
        'f0預測模式': 'f0預測模式',
        '啟用增強器': '啟用增強器',
        '啟用相位聲碼器': '啟用相位聲碼器',
        '性能設置': '性能設置',
        '開始音訊轉換': '開始音訊轉換',
        '停止音訊轉換': '停止音訊轉換',
        '推理所用時間(ms):': '推理所用時間(ms):',
        '擴散設置': '擴散設置',
        '啟用擴散': '啟用擴散',
        '擴散加速': '擴散加速',
        '擴散深度': '擴散深度',
        '擴散模型文件：.pt格式(自動識別同目錄下config.yaml)': '擴散模型文件：.pt格式(自動識別同目錄下config.yaml)',
        '不擴散安全區(加速但損失效果)': '不擴散安全區(加速但損失效果)',
        '擴散算法': '擴散算法'
    },
    'en_US': {
        'SUPER': 'zh_CN',
        'LANGUAGE': 'en_US',
        '選擇模型文件': 'Select Model File',
        'DDSP模型（4.0版本及以後可以不需要）:': 'DDSP model (version 4.0 and later may not be required):',
        '選擇配置文件所在目錄': 'Select the configuration file directory',
        '打開文件夾': 'Open folder',
        '讀取配置文件': 'Read config file',
        '保存配置文件': 'Save config file',
        '快速配置文件': 'Fast config file',
        '輸入設備': 'Input device',
        '輸出設備': 'Output device',
        '音訊設備': 'Audio devices',
        '說話人id': 'Speaker ID',
        '響應閾值': 'Response threshold',
        '變調': 'Pitch',
        '採樣率': 'Sampling rate',
        '啟用捏音色功能': 'Enable Mix Speaker',
        '設置混合音色': 'Mix Speaker',
        '普通設置': 'Normal Settings',
        '音訊切分大小': 'Segmentation size',
        '交叉淡化時長': 'Cross fade duration',
        '使用歷史區塊數量': 'Historical blocks used',
        'f0預測模式': 'f0Extractor',
        '啟用增強器': 'Enable Enhancer',
        '啟用相位聲碼器': 'Enable Phase Vocoder',
        '性能設置': 'Performance settings',
        '開始音訊轉換': 'Start conversion',
        '停止音訊轉換': 'Stop conversion',
        '推理所用時間(ms):': 'Inference time(ms):',
        '擴散設置': '擴散設置',
        '啟用擴散': '啟用擴散',
        '擴散加速': '擴散加速',
        '擴散深度': '擴散深度',
        '擴散模型文件：.pt格式(自動識別同目錄下config.yaml)': '擴散模型文件：.pt格式(自動識別同目錄下config.yaml)',
        '不擴散安全區(加速但損失效果)': '不擴散安全區(加速但損失效果)',
        '擴散算法': '擴散算法'
    },
    'ja_JP': {
        'SUPER': 'zh_CN',
        'LANGUAGE': 'ja_JP',
        '選擇模型文件': 'モデルを選択',
        'DDSP模型（4.0版本及以後可以不需要）:': 'DDSP モデル (バージョン 4.0 以降は必要ない場合があります)：',
        '選擇配置文件所在目錄': '設定ファイルを選択',
        '打開文件夾': 'フォルダを開く',
        '讀取配置文件': '設定ファイルを読み込む',
        '保存配置文件': '設定ファイルを保存',
        '快速配置文件': '設定プロファイル',
        '輸入設備': '入力デバイス',
        '輸出設備': '出力デバイス',
        '音訊設備': '音声デバイス',
        '說話人id': '話者ID',
        '響應閾值': '応答時の閾値',
        '變調': '音程',
        '採樣率': 'サンプリングレート',
        '啟用捏音色功能': 'ミキシングを有効化',
        '設置混合音色': 'ミキシング',
        '普通設置': '通常設定',
        '音訊切分大小': 'セグメンテーションのサイズ',
        '交叉淡化時長': 'クロスフェードの間隔',
        '使用歷史區塊數量': '使用するヒストリカルブロック数',
        'f0預測模式': 'f0予測モデル',
        '啟用增強器': 'Enhancerを有効化',
        '啟用相位聲碼器': 'フェーズボコーダを有効化',
        '性能設置': 'パフォーマンスの設定',
        '開始音訊轉換': '変換開始',
        '停止音訊轉換': '変換停止',
        '推理所用時間(ms):': '推論時間(ms):',
        '擴散設置': '擴散設置',
        '啟用擴散': '啟用擴散',
        '擴散加速': '擴散加速',
        '擴散深度': '擴散深度',
        '擴散說話人id': '擴散說話人id',
        '擴散模型文件：.pt格式(自動識別同目錄下config.yaml)': '擴散模型文件：.pt格式(自動識別同目錄下config.yaml)',
        '不擴散安全區(加速但損失效果)': '不擴散安全區(加速但損失效果)',
        '擴散算法': '擴散算法'
    }
}


class I18nAuto:
    def __init__(self, language=None):
        self.language_list = LANGUAGE_LIST
        self.language_all = LANGUAGE_ALL
        self.language_map = {}
        if language is None:
            language = 'auto'
        if language == 'auto':
            language = locale.getdefaultlocale()[0]
            if language not in self.language_list:
                language = 'zh_CN'
        self.language = language
        super_language_list = []
        while self.language_all[language]['SUPER'] != 'END':
            super_language_list.append(language)
            language = self.language_all[language]['SUPER']
        super_language_list.append('zh_CN')
        super_language_list.reverse()
        for _lang in super_language_list:
            self.read_language(self.language_all[_lang])

    def read_language(self, lang_dict: dict):
        for _key in lang_dict.keys():
            self.language_map[_key] = lang_dict[_key]

    def __call__(self, key):
        return self.language_map[key]
