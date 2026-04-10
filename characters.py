# 200 most common Mandarin Chinese characters
# Organized into 33 themed weekly groups (6 new chars/week + 1 review/week)
# Tone numbers: 1=flat, 2=rising, 3=dip, 4=falling, 5=neutral

CHARACTERS = [
    # ── WEEK 1: Core Grammar Particles (most frequent characters in Chinese) ──
    {
        "char": "的", "pinyin": "de", "tone": 5,
        "meaning": "possessive/descriptive particle (like 's or -ly)",
        "example_cn": "我的书", "example_pinyin": "wǒ de shū", "example_en": "my book",
        "group": "Core Grammar", "week": 1,
    },
    {
        "char": "是", "pinyin": "shì", "tone": 4,
        "meaning": "to be (am / is / are)",
        "example_cn": "我是学生", "example_pinyin": "wǒ shì xuésheng", "example_en": "I am a student",
        "group": "Core Grammar", "week": 1,
    },
    {
        "char": "不", "pinyin": "bù", "tone": 4,
        "meaning": "not; no (general negation)",
        "example_cn": "我不累", "example_pinyin": "wǒ bù lèi", "example_en": "I am not tired",
        "group": "Core Grammar", "week": 1,
    },
    {
        "char": "了", "pinyin": "le", "tone": 5,
        "meaning": "completed-action particle; change of state",
        "example_cn": "他来了", "example_pinyin": "tā lái le", "example_en": "He came / He has arrived",
        "group": "Core Grammar", "week": 1,
    },
    {
        "char": "在", "pinyin": "zài", "tone": 4,
        "meaning": "at; in; on; to be present somewhere",
        "example_cn": "她在家", "example_pinyin": "tā zài jiā", "example_en": "She is at home",
        "group": "Core Grammar", "week": 1,
    },
    {
        "char": "有", "pinyin": "yǒu", "tone": 3,
        "meaning": "to have; there is / there are",
        "example_cn": "我有朋友", "example_pinyin": "wǒ yǒu péngyou", "example_en": "I have friends",
        "group": "Core Grammar", "week": 1,
    },

    # ── WEEK 2: Numbers 1–6 ──
    {
        "char": "一", "pinyin": "yī", "tone": 1,
        "meaning": "one; a / an",
        "example_cn": "一个人", "example_pinyin": "yī gè rén", "example_en": "one person",
        "group": "Numbers", "week": 2,
    },
    {
        "char": "二", "pinyin": "èr", "tone": 4,
        "meaning": "two",
        "example_cn": "二月", "example_pinyin": "èr yuè", "example_en": "February (month 2)",
        "group": "Numbers", "week": 2,
    },
    {
        "char": "三", "pinyin": "sān", "tone": 1,
        "meaning": "three",
        "example_cn": "三天", "example_pinyin": "sān tiān", "example_en": "three days",
        "group": "Numbers", "week": 2,
    },
    {
        "char": "四", "pinyin": "sì", "tone": 4,
        "meaning": "four",
        "example_cn": "四点钟", "example_pinyin": "sì diǎn zhōng", "example_en": "four o'clock",
        "group": "Numbers", "week": 2,
    },
    {
        "char": "五", "pinyin": "wǔ", "tone": 3,
        "meaning": "five",
        "example_cn": "五个苹果", "example_pinyin": "wǔ gè píngguǒ", "example_en": "five apples",
        "group": "Numbers", "week": 2,
    },
    {
        "char": "六", "pinyin": "liù", "tone": 4,
        "meaning": "six",
        "example_cn": "六月", "example_pinyin": "liù yuè", "example_en": "June (month 6)",
        "group": "Numbers", "week": 2,
    },

    # ── WEEK 3: Numbers 7–10 + Larger Numbers ──
    {
        "char": "七", "pinyin": "qī", "tone": 1,
        "meaning": "seven",
        "example_cn": "一周七天", "example_pinyin": "yī zhōu qī tiān", "example_en": "seven days in a week",
        "group": "Numbers", "week": 3,
    },
    {
        "char": "八", "pinyin": "bā", "tone": 1,
        "meaning": "eight",
        "example_cn": "八月", "example_pinyin": "bā yuè", "example_en": "August (month 8)",
        "group": "Numbers", "week": 3,
    },
    {
        "char": "九", "pinyin": "jiǔ", "tone": 3,
        "meaning": "nine",
        "example_cn": "九点", "example_pinyin": "jiǔ diǎn", "example_en": "nine o'clock",
        "group": "Numbers", "week": 3,
    },
    {
        "char": "十", "pinyin": "shí", "tone": 2,
        "meaning": "ten",
        "example_cn": "十分钟", "example_pinyin": "shí fēnzhōng", "example_en": "ten minutes",
        "group": "Numbers", "week": 3,
    },
    {
        "char": "百", "pinyin": "bǎi", "tone": 3,
        "meaning": "hundred",
        "example_cn": "一百块", "example_pinyin": "yī bǎi kuài", "example_en": "one hundred yuan",
        "group": "Numbers", "week": 3,
    },
    {
        "char": "千", "pinyin": "qiān", "tone": 1,
        "meaning": "thousand",
        "example_cn": "一千人", "example_pinyin": "yī qiān rén", "example_en": "one thousand people",
        "group": "Numbers", "week": 3,
    },
    {
        "char": "万", "pinyin": "wàn", "tone": 4,
        "meaning": "ten thousand; myriad",
        "example_cn": "一万元", "example_pinyin": "yī wàn yuán", "example_en": "ten thousand yuan",
        "group": "Numbers", "week": 3,
    },
    {
        "char": "零", "pinyin": "líng", "tone": 2,
        "meaning": "zero; remainder; spare",
        "example_cn": "零下五度", "example_pinyin": "líng xià wǔ dù", "example_en": "five degrees below zero",
        "group": "Numbers", "week": 3,
    },

    # ── WEEK 4: Pronouns ──
    {
        "char": "我", "pinyin": "wǒ", "tone": 3,
        "meaning": "I; me; my",
        "example_cn": "我叫小明", "example_pinyin": "wǒ jiào xiǎo míng", "example_en": "My name is Xiao Ming",
        "group": "Pronouns", "week": 4,
    },
    {
        "char": "你", "pinyin": "nǐ", "tone": 3,
        "meaning": "you (singular)",
        "example_cn": "你好吗", "example_pinyin": "nǐ hǎo ma", "example_en": "How are you?",
        "group": "Pronouns", "week": 4,
    },
    {
        "char": "他", "pinyin": "tā", "tone": 1,
        "meaning": "he; him",
        "example_cn": "他是老师", "example_pinyin": "tā shì lǎoshī", "example_en": "He is a teacher",
        "group": "Pronouns", "week": 4,
    },
    {
        "char": "她", "pinyin": "tā", "tone": 1,
        "meaning": "she; her",
        "example_cn": "她很漂亮", "example_pinyin": "tā hěn piàoliang", "example_en": "She is very pretty",
        "group": "Pronouns", "week": 4,
    },
    {
        "char": "们", "pinyin": "men", "tone": 5,
        "meaning": "plural suffix: 我们=we, 你们=y'all, 他们=they",
        "example_cn": "我们是朋友", "example_pinyin": "wǒmen shì péngyou", "example_en": "We are friends",
        "group": "Pronouns", "week": 4,
    },
    {
        "char": "这", "pinyin": "zhè", "tone": 4,
        "meaning": "this; these",
        "example_cn": "这是什么", "example_pinyin": "zhè shì shénme", "example_en": "What is this?",
        "group": "Pronouns", "week": 4,
    },

    # ── WEEK 5: Connectors & Adverbs ──
    {
        "char": "那", "pinyin": "nà", "tone": 4,
        "meaning": "that; those; then / in that case",
        "example_cn": "那个人是谁", "example_pinyin": "nà gè rén shì shuí", "example_en": "Who is that person?",
        "group": "Connectors", "week": 5,
    },
    {
        "char": "和", "pinyin": "hé", "tone": 2,
        "meaning": "and; with; harmonious",
        "example_cn": "我和你", "example_pinyin": "wǒ hé nǐ", "example_en": "you and me",
        "group": "Connectors", "week": 5,
    },
    {
        "char": "也", "pinyin": "yě", "tone": 3,
        "meaning": "also; too; as well",
        "example_cn": "我也喜欢", "example_pinyin": "wǒ yě xǐhuān", "example_en": "I also like it",
        "group": "Connectors", "week": 5,
    },
    {
        "char": "都", "pinyin": "dōu", "tone": 1,
        "meaning": "all; both; already (placed before verb)",
        "example_cn": "我们都去", "example_pinyin": "wǒmen dōu qù", "example_en": "We are all going",
        "group": "Connectors", "week": 5,
    },
    {
        "char": "很", "pinyin": "hěn", "tone": 3,
        "meaning": "very; quite",
        "example_cn": "她很高兴", "example_pinyin": "tā hěn gāoxìng", "example_en": "She is very happy",
        "group": "Connectors", "week": 5,
    },
    {
        "char": "就", "pinyin": "jiù", "tone": 4,
        "meaning": "then; right away; just; only",
        "example_cn": "我就来", "example_pinyin": "wǒ jiù lái", "example_en": "I'll be right there",
        "group": "Connectors", "week": 5,
    },

    # ── WEEK 6: Basic Action Verbs ──
    {
        "char": "来", "pinyin": "lái", "tone": 2,
        "meaning": "to come",
        "example_cn": "请进来", "example_pinyin": "qǐng jìnlái", "example_en": "Please come in",
        "group": "Action Verbs", "week": 6,
    },
    {
        "char": "去", "pinyin": "qù", "tone": 4,
        "meaning": "to go",
        "example_cn": "我去上学", "example_pinyin": "wǒ qù shàngxué", "example_en": "I go to school",
        "group": "Action Verbs", "week": 6,
    },
    {
        "char": "说", "pinyin": "shuō", "tone": 1,
        "meaning": "to say; to speak; to tell",
        "example_cn": "他说中文", "example_pinyin": "tā shuō zhōngwén", "example_en": "He speaks Chinese",
        "group": "Action Verbs", "week": 6,
    },
    {
        "char": "看", "pinyin": "kàn", "tone": 4,
        "meaning": "to look; to watch; to read",
        "example_cn": "我看书", "example_pinyin": "wǒ kàn shū", "example_en": "I read books",
        "group": "Action Verbs", "week": 6,
    },
    {
        "char": "吃", "pinyin": "chī", "tone": 1,
        "meaning": "to eat",
        "example_cn": "你吃饭了吗", "example_pinyin": "nǐ chīfàn le ma", "example_en": "Have you eaten?",
        "group": "Action Verbs", "week": 6,
    },
    {
        "char": "喝", "pinyin": "hē", "tone": 1,
        "meaning": "to drink",
        "example_cn": "我喝水", "example_pinyin": "wǒ hē shuǐ", "example_en": "I drink water",
        "group": "Action Verbs", "week": 6,
    },

    # ── WEEK 7: Movement Verbs ──
    {
        "char": "到", "pinyin": "dào", "tone": 4,
        "meaning": "to arrive; to reach; until",
        "example_cn": "我到了", "example_pinyin": "wǒ dào le", "example_en": "I have arrived",
        "group": "Movement Verbs", "week": 7,
    },
    {
        "char": "出", "pinyin": "chū", "tone": 1,
        "meaning": "to go out; to exit; to produce",
        "example_cn": "他出去了", "example_pinyin": "tā chūqù le", "example_en": "He went out",
        "group": "Movement Verbs", "week": 7,
    },
    {
        "char": "走", "pinyin": "zǒu", "tone": 3,
        "meaning": "to walk; to leave; to go",
        "example_cn": "我们走吧", "example_pinyin": "wǒmen zǒu ba", "example_en": "Let's go!",
        "group": "Movement Verbs", "week": 7,
    },
    {
        "char": "开", "pinyin": "kāi", "tone": 1,
        "meaning": "to open; to drive; to start; to turn on",
        "example_cn": "开门", "example_pinyin": "kāi mén", "example_en": "open the door",
        "group": "Movement Verbs", "week": 7,
    },
    {
        "char": "回", "pinyin": "huí", "tone": 2,
        "meaning": "to return; to go back; to reply",
        "example_cn": "我回家了", "example_pinyin": "wǒ huí jiā le", "example_en": "I went home",
        "group": "Movement Verbs", "week": 7,
    },
    {
        "char": "进", "pinyin": "jìn", "tone": 4,
        "meaning": "to enter; to come/go in; to advance",
        "example_cn": "请进", "example_pinyin": "qǐng jìn", "example_en": "Please come in",
        "group": "Movement Verbs", "week": 7,
    },

    # ── WEEK 8: Family ──
    {
        "char": "人", "pinyin": "rén", "tone": 2,
        "meaning": "person; people; human being",
        "example_cn": "那个人是谁", "example_pinyin": "nà gè rén shì shuí", "example_en": "Who is that person?",
        "group": "Family & People", "week": 8,
    },
    {
        "char": "家", "pinyin": "jiā", "tone": 1,
        "meaning": "home; family; house; (expert)",
        "example_cn": "我家有四口人", "example_pinyin": "wǒ jiā yǒu sì kǒu rén", "example_en": "My family has four people",
        "group": "Family & People", "week": 8,
    },
    {
        "char": "父", "pinyin": "fù", "tone": 4,
        "meaning": "father (formal/written)",
        "example_cn": "父母", "example_pinyin": "fùmǔ", "example_en": "parents (father and mother)",
        "group": "Family & People", "week": 8,
    },
    {
        "char": "母", "pinyin": "mǔ", "tone": 3,
        "meaning": "mother (formal/written)",
        "example_cn": "母亲", "example_pinyin": "mǔqīn", "example_en": "mother (formal)",
        "group": "Family & People", "week": 8,
    },
    {
        "char": "子", "pinyin": "zǐ", "tone": 3,
        "meaning": "son; child; offspring; seed",
        "example_cn": "孩子", "example_pinyin": "háizi", "example_en": "child / children",
        "group": "Family & People", "week": 8,
    },
    {
        "char": "女", "pinyin": "nǚ", "tone": 3,
        "meaning": "woman; female; daughter",
        "example_cn": "女儿", "example_pinyin": "nǚér", "example_en": "daughter",
        "group": "Family & People", "week": 8,
    },

    # ── WEEK 9: More Family & Social ──
    {
        "char": "男", "pinyin": "nán", "tone": 2,
        "meaning": "male; man; boy",
        "example_cn": "男生", "example_pinyin": "nánshēng", "example_en": "male student; boy",
        "group": "Family & People", "week": 9,
    },
    {
        "char": "兄", "pinyin": "xiōng", "tone": 1,
        "meaning": "older brother (formal/literary)",
        "example_cn": "兄弟", "example_pinyin": "xiōngdì", "example_en": "brothers; male siblings",
        "group": "Family & People", "week": 9,
    },
    {
        "char": "弟", "pinyin": "dì", "tone": 4,
        "meaning": "younger brother",
        "example_cn": "弟弟", "example_pinyin": "dìdi", "example_en": "younger brother",
        "group": "Family & People", "week": 9,
    },
    {
        "char": "姐", "pinyin": "jiě", "tone": 3,
        "meaning": "older sister",
        "example_cn": "姐姐", "example_pinyin": "jiějie", "example_en": "older sister",
        "group": "Family & People", "week": 9,
    },
    {
        "char": "妹", "pinyin": "mèi", "tone": 4,
        "meaning": "younger sister",
        "example_cn": "妹妹", "example_pinyin": "mèimei", "example_en": "younger sister",
        "group": "Family & People", "week": 9,
    },
    {
        "char": "友", "pinyin": "yǒu", "tone": 3,
        "meaning": "friend; friendly",
        "example_cn": "朋友", "example_pinyin": "péngyou", "example_en": "friend",
        "group": "Family & People", "week": 9,
    },

    # ── WEEK 10: Time I ──
    {
        "char": "年", "pinyin": "nián", "tone": 2,
        "meaning": "year",
        "example_cn": "今年", "example_pinyin": "jīnnián", "example_en": "this year",
        "group": "Time", "week": 10,
    },
    {
        "char": "月", "pinyin": "yuè", "tone": 4,
        "meaning": "month; moon",
        "example_cn": "这个月", "example_pinyin": "zhège yuè", "example_en": "this month",
        "group": "Time", "week": 10,
    },
    {
        "char": "日", "pinyin": "rì", "tone": 4,
        "meaning": "day; sun; date",
        "example_cn": "生日", "example_pinyin": "shēngrì", "example_en": "birthday",
        "group": "Time", "week": 10,
    },
    {
        "char": "天", "pinyin": "tiān", "tone": 1,
        "meaning": "day; sky; heaven; weather",
        "example_cn": "今天", "example_pinyin": "jīntiān", "example_en": "today",
        "group": "Time", "week": 10,
    },
    {
        "char": "时", "pinyin": "shí", "tone": 2,
        "meaning": "time; hour; when",
        "example_cn": "几时了", "example_pinyin": "jǐ shí le", "example_en": "What time is it?",
        "group": "Time", "week": 10,
    },
    {
        "char": "今", "pinyin": "jīn", "tone": 1,
        "meaning": "today; now; current",
        "example_cn": "今天天气好", "example_pinyin": "jīntiān tiānqì hǎo", "example_en": "Today's weather is nice",
        "group": "Time", "week": 10,
    },

    # ── WEEK 11: Time II ──
    {
        "char": "明", "pinyin": "míng", "tone": 2,
        "meaning": "tomorrow; bright; clear; understand",
        "example_cn": "明天见", "example_pinyin": "míngtiān jiàn", "example_en": "See you tomorrow",
        "group": "Time", "week": 11,
    },
    {
        "char": "昨", "pinyin": "zuó", "tone": 2,
        "meaning": "yesterday",
        "example_cn": "昨天", "example_pinyin": "zuótiān", "example_en": "yesterday",
        "group": "Time", "week": 11,
    },
    {
        "char": "早", "pinyin": "zǎo", "tone": 3,
        "meaning": "early; morning; Good morning!",
        "example_cn": "早上好", "example_pinyin": "zǎoshang hǎo", "example_en": "Good morning!",
        "group": "Time", "week": 11,
    },
    {
        "char": "晚", "pinyin": "wǎn", "tone": 3,
        "meaning": "evening; late; night",
        "example_cn": "晚上好", "example_pinyin": "wǎnshang hǎo", "example_en": "Good evening!",
        "group": "Time", "week": 11,
    },
    {
        "char": "前", "pinyin": "qián", "tone": 2,
        "meaning": "front; before; ago; previous",
        "example_cn": "三天前", "example_pinyin": "sān tiān qián", "example_en": "three days ago",
        "group": "Time", "week": 11,
    },
    {
        "char": "后", "pinyin": "hòu", "tone": 4,
        "meaning": "after; behind; later; back",
        "example_cn": "以后", "example_pinyin": "yǐhòu", "example_en": "after; from now on; in the future",
        "group": "Time", "week": 11,
    },

    # ── WEEK 12: Spatial Directions I ──
    {
        "char": "上", "pinyin": "shàng", "tone": 4,
        "meaning": "up; above; on top; to go up; last (week)",
        "example_cn": "桌子上", "example_pinyin": "zhuōzi shàng", "example_en": "on the table",
        "group": "Directions", "week": 12,
    },
    {
        "char": "下", "pinyin": "xià", "tone": 4,
        "meaning": "down; below; under; next (week); to fall",
        "example_cn": "下午", "example_pinyin": "xiàwǔ", "example_en": "afternoon",
        "group": "Directions", "week": 12,
    },
    {
        "char": "左", "pinyin": "zuǒ", "tone": 3,
        "meaning": "left (direction)",
        "example_cn": "左边", "example_pinyin": "zuǒbiān", "example_en": "left side",
        "group": "Directions", "week": 12,
    },
    {
        "char": "右", "pinyin": "yòu", "tone": 4,
        "meaning": "right (direction)",
        "example_cn": "右边", "example_pinyin": "yòubiān", "example_en": "right side",
        "group": "Directions", "week": 12,
    },
    {
        "char": "中", "pinyin": "zhōng", "tone": 1,
        "meaning": "middle; center; China; during",
        "example_cn": "中间", "example_pinyin": "zhōngjiān", "example_en": "in the middle",
        "group": "Directions", "week": 12,
    },
    {
        "char": "里", "pinyin": "lǐ", "tone": 3,
        "meaning": "inside; in; within",
        "example_cn": "房间里", "example_pinyin": "fángjiān lǐ", "example_en": "inside the room",
        "group": "Directions", "week": 12,
    },

    # ── WEEK 13: Spatial Directions II & Country ──
    {
        "char": "外", "pinyin": "wài", "tone": 4,
        "meaning": "outside; foreign; other",
        "example_cn": "外面", "example_pinyin": "wàimiàn", "example_en": "outside",
        "group": "Directions", "week": 13,
    },
    {
        "char": "东", "pinyin": "dōng", "tone": 1,
        "meaning": "east",
        "example_cn": "东方", "example_pinyin": "dōngfāng", "example_en": "the East; Eastern",
        "group": "Directions", "week": 13,
    },
    {
        "char": "西", "pinyin": "xī", "tone": 1,
        "meaning": "west; (东西 together = 'thing')",
        "example_cn": "东西", "example_pinyin": "dōngxi", "example_en": "thing(s) — lit. 'east-west'",
        "group": "Directions", "week": 13,
    },
    {
        "char": "南", "pinyin": "nán", "tone": 2,
        "meaning": "south",
        "example_cn": "南方", "example_pinyin": "nánfāng", "example_en": "the South; Southern China",
        "group": "Directions", "week": 13,
    },
    {
        "char": "北", "pinyin": "běi", "tone": 3,
        "meaning": "north",
        "example_cn": "北京", "example_pinyin": "Běijīng", "example_en": "Beijing — lit. 'Northern Capital'",
        "group": "Directions", "week": 13,
    },
    {
        "char": "国", "pinyin": "guó", "tone": 2,
        "meaning": "country; nation; national",
        "example_cn": "中国", "example_pinyin": "Zhōngguó", "example_en": "China — lit. 'Middle Kingdom'",
        "group": "Places", "week": 13,
    },

    # ── WEEK 14: Size & Quantity ──
    {
        "char": "大", "pinyin": "dà", "tone": 4,
        "meaning": "big; large; great; loud",
        "example_cn": "大学", "example_pinyin": "dàxué", "example_en": "university — lit. 'big study'",
        "group": "Adjectives", "week": 14,
    },
    {
        "char": "小", "pinyin": "xiǎo", "tone": 3,
        "meaning": "small; little; young",
        "example_cn": "小心", "example_pinyin": "xiǎoxīn", "example_en": "be careful — lit. 'small heart'",
        "group": "Adjectives", "week": 14,
    },
    {
        "char": "多", "pinyin": "duō", "tone": 1,
        "meaning": "many; much; more; a lot",
        "example_cn": "多少钱", "example_pinyin": "duōshǎo qián", "example_en": "How much does it cost?",
        "group": "Adjectives", "week": 14,
    },
    {
        "char": "少", "pinyin": "shǎo", "tone": 3,
        "meaning": "few; little; scarce",
        "example_cn": "多少", "example_pinyin": "duōshǎo", "example_en": "how many / how much",
        "group": "Adjectives", "week": 14,
    },
    {
        "char": "长", "pinyin": "cháng", "tone": 2,
        "meaning": "long (length/time)",
        "example_cn": "很长时间", "example_pinyin": "hěn cháng shíjiān", "example_en": "a very long time",
        "group": "Adjectives", "week": 14,
    },
    {
        "char": "高", "pinyin": "gāo", "tone": 1,
        "meaning": "tall; high; loud; elevated",
        "example_cn": "他很高", "example_pinyin": "tā hěn gāo", "example_en": "He is very tall",
        "group": "Adjectives", "week": 14,
    },

    # ── WEEK 15: Evaluative Adjectives ──
    {
        "char": "好", "pinyin": "hǎo", "tone": 3,
        "meaning": "good; well; OK; very (informal intensifier)",
        "example_cn": "你好", "example_pinyin": "nǐ hǎo", "example_en": "Hello! — lit. 'you good'",
        "group": "Adjectives", "week": 15,
    },
    {
        "char": "坏", "pinyin": "huài", "tone": 4,
        "meaning": "bad; broken; spoiled; evil",
        "example_cn": "手机坏了", "example_pinyin": "shǒujī huài le", "example_en": "My phone is broken",
        "group": "Adjectives", "week": 15,
    },
    {
        "char": "新", "pinyin": "xīn", "tone": 1,
        "meaning": "new; fresh; recently",
        "example_cn": "新年快乐", "example_pinyin": "xīnnián kuàilè", "example_en": "Happy New Year!",
        "group": "Adjectives", "week": 15,
    },
    {
        "char": "旧", "pinyin": "jiù", "tone": 4,
        "meaning": "old; used; worn; former",
        "example_cn": "旧书", "example_pinyin": "jiù shū", "example_en": "old / used book",
        "group": "Adjectives", "week": 15,
    },
    {
        "char": "热", "pinyin": "rè", "tone": 4,
        "meaning": "hot; warm; popular; fever",
        "example_cn": "今天很热", "example_pinyin": "jīntiān hěn rè", "example_en": "It's very hot today",
        "group": "Adjectives", "week": 15,
    },
    {
        "char": "冷", "pinyin": "lěng", "tone": 3,
        "meaning": "cold; cool; indifferent",
        "example_cn": "冬天很冷", "example_pinyin": "dōngtiān hěn lěng", "example_en": "Winter is very cold",
        "group": "Adjectives", "week": 15,
    },

    # ── WEEK 16: Cognitive & Modal Verbs ──
    {
        "char": "想", "pinyin": "xiǎng", "tone": 3,
        "meaning": "to think; to want to; to miss someone",
        "example_cn": "我想你", "example_pinyin": "wǒ xiǎng nǐ", "example_en": "I miss you",
        "group": "Cognitive Verbs", "week": 16,
    },
    {
        "char": "知", "pinyin": "zhī", "tone": 1,
        "meaning": "to know (a fact); knowledge",
        "example_cn": "我不知道", "example_pinyin": "wǒ bù zhīdào", "example_en": "I don't know",
        "group": "Cognitive Verbs", "week": 16,
    },
    {
        "char": "能", "pinyin": "néng", "tone": 2,
        "meaning": "can; able to; capable; energy",
        "example_cn": "你能帮我吗", "example_pinyin": "nǐ néng bāng wǒ ma", "example_en": "Can you help me?",
        "group": "Cognitive Verbs", "week": 16,
    },
    {
        "char": "会", "pinyin": "huì", "tone": 4,
        "meaning": "can; know how to; will (future); meeting",
        "example_cn": "你会游泳吗", "example_pinyin": "nǐ huì yóuyǒng ma", "example_en": "Can you swim?",
        "group": "Cognitive Verbs", "week": 16,
    },
    {
        "char": "要", "pinyin": "yào", "tone": 4,
        "meaning": "to want; need; will; should; important",
        "example_cn": "我要喝水", "example_pinyin": "wǒ yào hē shuǐ", "example_en": "I want to drink water",
        "group": "Cognitive Verbs", "week": 16,
    },
    {
        "char": "可", "pinyin": "kě", "tone": 3,
        "meaning": "can; may; approve; but",
        "example_cn": "可以", "example_pinyin": "kěyǐ", "example_en": "can; may; it's OK",
        "group": "Cognitive Verbs", "week": 16,
    },

    # ── WEEK 17: Communication & Language ──
    {
        "char": "问", "pinyin": "wèn", "tone": 4,
        "meaning": "to ask; to inquire",
        "example_cn": "我问你", "example_pinyin": "wǒ wèn nǐ", "example_en": "I ask you / let me ask you",
        "group": "Communication", "week": 17,
    },
    {
        "char": "答", "pinyin": "dá", "tone": 2,
        "meaning": "to answer; to reply; answer",
        "example_cn": "回答", "example_pinyin": "huídá", "example_en": "to answer; a reply",
        "group": "Communication", "week": 17,
    },
    {
        "char": "写", "pinyin": "xiě", "tone": 3,
        "meaning": "to write",
        "example_cn": "写字", "example_pinyin": "xiě zì", "example_en": "to write characters",
        "group": "Communication", "week": 17,
    },
    {
        "char": "读", "pinyin": "dú", "tone": 2,
        "meaning": "to read aloud; to study; reading",
        "example_cn": "读书", "example_pinyin": "dú shū", "example_en": "to read (books); to study",
        "group": "Communication", "week": 17,
    },
    {
        "char": "文", "pinyin": "wén", "tone": 2,
        "meaning": "language; culture; writing; literature",
        "example_cn": "中文", "example_pinyin": "Zhōngwén", "example_en": "Chinese language",
        "group": "Communication", "week": 17,
    },
    {
        "char": "字", "pinyin": "zì", "tone": 4,
        "meaning": "character; word; letter; written symbol",
        "example_cn": "汉字", "example_pinyin": "Hànzì", "example_en": "Chinese characters (hanzi)",
        "group": "Communication", "week": 17,
    },

    # ── WEEK 18: Nature I (Classic Elements) ──
    {
        "char": "水", "pinyin": "shuǐ", "tone": 3,
        "meaning": "water",
        "example_cn": "喝水", "example_pinyin": "hē shuǐ", "example_en": "drink water",
        "group": "Nature", "week": 18,
    },
    {
        "char": "火", "pinyin": "huǒ", "tone": 3,
        "meaning": "fire; flame; hot; anger",
        "example_cn": "火车", "example_pinyin": "huǒchē", "example_en": "train — lit. 'fire vehicle'",
        "group": "Nature", "week": 18,
    },
    {
        "char": "山", "pinyin": "shān", "tone": 1,
        "meaning": "mountain; hill",
        "example_cn": "上山", "example_pinyin": "shàng shān", "example_en": "to go up the mountain",
        "group": "Nature", "week": 18,
    },
    {
        "char": "木", "pinyin": "mù", "tone": 4,
        "meaning": "wood; tree; wooden; numb",
        "example_cn": "木头", "example_pinyin": "mùtou", "example_en": "wood; log",
        "group": "Nature", "week": 18,
    },
    {
        "char": "土", "pinyin": "tǔ", "tone": 3,
        "meaning": "earth; soil; land; local",
        "example_cn": "土地", "example_pinyin": "tǔdì", "example_en": "land; soil; territory",
        "group": "Nature", "week": 18,
    },
    {
        "char": "花", "pinyin": "huā", "tone": 1,
        "meaning": "flower; to spend (money/time)",
        "example_cn": "买花", "example_pinyin": "mǎi huā", "example_en": "buy flowers",
        "group": "Nature", "week": 18,
    },

    # ── WEEK 19: Nature II (Weather & Plants) ──
    {
        "char": "草", "pinyin": "cǎo", "tone": 3,
        "meaning": "grass; plant; rough draft",
        "example_cn": "草地", "example_pinyin": "cǎodì", "example_en": "lawn; grassland",
        "group": "Nature", "week": 19,
    },
    {
        "char": "树", "pinyin": "shù", "tone": 4,
        "meaning": "tree",
        "example_cn": "树上有鸟", "example_pinyin": "shù shàng yǒu niǎo", "example_en": "There are birds in the tree",
        "group": "Nature", "week": 19,
    },
    {
        "char": "雨", "pinyin": "yǔ", "tone": 3,
        "meaning": "rain",
        "example_cn": "下雨了", "example_pinyin": "xià yǔ le", "example_en": "It's raining",
        "group": "Nature", "week": 19,
    },
    {
        "char": "风", "pinyin": "fēng", "tone": 1,
        "meaning": "wind; style; custom; trend",
        "example_cn": "风很大", "example_pinyin": "fēng hěn dà", "example_en": "The wind is very strong",
        "group": "Nature", "week": 19,
    },
    {
        "char": "雪", "pinyin": "xuě", "tone": 3,
        "meaning": "snow",
        "example_cn": "下雪了", "example_pinyin": "xià xuě le", "example_en": "It's snowing",
        "group": "Nature", "week": 19,
    },
    {
        "char": "云", "pinyin": "yún", "tone": 2,
        "meaning": "cloud",
        "example_cn": "白云", "example_pinyin": "báiyún", "example_en": "white cloud",
        "group": "Nature", "week": 19,
    },

    # ── WEEK 20: Body Parts I ──
    {
        "char": "手", "pinyin": "shǒu", "tone": 3,
        "meaning": "hand; expert at something",
        "example_cn": "洗手", "example_pinyin": "xǐ shǒu", "example_en": "wash hands",
        "group": "Body", "week": 20,
    },
    {
        "char": "口", "pinyin": "kǒu", "tone": 3,
        "meaning": "mouth; opening; entrance; (measure for family members)",
        "example_cn": "入口", "example_pinyin": "rùkǒu", "example_en": "entrance — lit. 'enter mouth'",
        "group": "Body", "week": 20,
    },
    {
        "char": "眼", "pinyin": "yǎn", "tone": 3,
        "meaning": "eye",
        "example_cn": "眼睛", "example_pinyin": "yǎnjing", "example_en": "eye(s)",
        "group": "Body", "week": 20,
    },
    {
        "char": "耳", "pinyin": "ěr", "tone": 3,
        "meaning": "ear",
        "example_cn": "耳朵", "example_pinyin": "ěrduo", "example_en": "ear(s)",
        "group": "Body", "week": 20,
    },
    {
        "char": "心", "pinyin": "xīn", "tone": 1,
        "meaning": "heart; mind; center",
        "example_cn": "小心", "example_pinyin": "xiǎoxīn", "example_en": "be careful — lit. 'small heart'",
        "group": "Body", "week": 20,
    },
    {
        "char": "头", "pinyin": "tóu", "tone": 2,
        "meaning": "head; top; first; end",
        "example_cn": "头疼", "example_pinyin": "tóuténg", "example_en": "headache",
        "group": "Body", "week": 20,
    },

    # ── WEEK 21: Body Parts II ──
    {
        "char": "脚", "pinyin": "jiǎo", "tone": 3,
        "meaning": "foot; leg (of a table or animal)",
        "example_cn": "脚疼", "example_pinyin": "jiǎo téng", "example_en": "my foot hurts",
        "group": "Body", "week": 21,
    },
    {
        "char": "面", "pinyin": "miàn", "tone": 4,
        "meaning": "face; surface; noodles; side",
        "example_cn": "面条", "example_pinyin": "miàntiáo", "example_en": "noodles",
        "group": "Body", "week": 21,
    },
    {
        "char": "身", "pinyin": "shēn", "tone": 1,
        "meaning": "body; oneself",
        "example_cn": "身体好", "example_pinyin": "shēntǐ hǎo", "example_en": "in good health",
        "group": "Body", "week": 21,
    },
    {
        "char": "发", "pinyin": "fà", "tone": 4,
        "meaning": "hair (on head); (fā) to send; to happen",
        "example_cn": "头发", "example_pinyin": "tóufa", "example_en": "hair (on the head)",
        "group": "Body", "week": 21,
    },
    {
        "char": "背", "pinyin": "bèi", "tone": 4,
        "meaning": "back (of body); to carry on back; to memorize",
        "example_cn": "背包", "example_pinyin": "bēibāo", "example_en": "backpack",
        "group": "Body", "week": 21,
    },
    {
        "char": "腿", "pinyin": "tuǐ", "tone": 3,
        "meaning": "leg",
        "example_cn": "腿很长", "example_pinyin": "tuǐ hěn cháng", "example_en": "long legs",
        "group": "Body", "week": 21,
    },

    # ── WEEK 22: Colors ──
    {
        "char": "红", "pinyin": "hóng", "tone": 2,
        "meaning": "red; popular; lucky",
        "example_cn": "红色", "example_pinyin": "hóngsè", "example_en": "red (color)",
        "group": "Colors", "week": 22,
    },
    {
        "char": "白", "pinyin": "bái", "tone": 2,
        "meaning": "white; plain; blank; in vain",
        "example_cn": "白色", "example_pinyin": "báisè", "example_en": "white (color)",
        "group": "Colors", "week": 22,
    },
    {
        "char": "黑", "pinyin": "hēi", "tone": 1,
        "meaning": "black; dark; sinister",
        "example_cn": "黑色", "example_pinyin": "hēisè", "example_en": "black (color)",
        "group": "Colors", "week": 22,
    },
    {
        "char": "蓝", "pinyin": "lán", "tone": 2,
        "meaning": "blue",
        "example_cn": "蓝天", "example_pinyin": "lán tiān", "example_en": "blue sky",
        "group": "Colors", "week": 22,
    },
    {
        "char": "绿", "pinyin": "lǜ", "tone": 4,
        "meaning": "green",
        "example_cn": "绿色", "example_pinyin": "lǜsè", "example_en": "green (color)",
        "group": "Colors", "week": 22,
    },
    {
        "char": "黄", "pinyin": "huáng", "tone": 2,
        "meaning": "yellow",
        "example_cn": "黄色", "example_pinyin": "huángsè", "example_en": "yellow (color)",
        "group": "Colors", "week": 22,
    },

    # ── WEEK 23: Food I ──
    {
        "char": "饭", "pinyin": "fàn", "tone": 4,
        "meaning": "cooked rice; meal; food",
        "example_cn": "吃饭", "example_pinyin": "chīfàn", "example_en": "to eat (a meal)",
        "group": "Food & Drink", "week": 23,
    },
    {
        "char": "茶", "pinyin": "chá", "tone": 2,
        "meaning": "tea",
        "example_cn": "喝茶", "example_pinyin": "hē chá", "example_en": "drink tea",
        "group": "Food & Drink", "week": 23,
    },
    {
        "char": "酒", "pinyin": "jiǔ", "tone": 3,
        "meaning": "alcohol; wine; liquor; beer",
        "example_cn": "喝酒", "example_pinyin": "hē jiǔ", "example_en": "drink alcohol",
        "group": "Food & Drink", "week": 23,
    },
    {
        "char": "米", "pinyin": "mǐ", "tone": 3,
        "meaning": "rice (uncooked); meter",
        "example_cn": "白米饭", "example_pinyin": "báimǐfàn", "example_en": "white rice",
        "group": "Food & Drink", "week": 23,
    },
    {
        "char": "肉", "pinyin": "ròu", "tone": 4,
        "meaning": "meat; flesh",
        "example_cn": "猪肉", "example_pinyin": "zhūròu", "example_en": "pork — lit. 'pig meat'",
        "group": "Food & Drink", "week": 23,
    },
    {
        "char": "菜", "pinyin": "cài", "tone": 4,
        "meaning": "vegetable; dish; food",
        "example_cn": "中国菜", "example_pinyin": "Zhōngguó cài", "example_en": "Chinese food / Chinese dishes",
        "group": "Food & Drink", "week": 23,
    },

    # ── WEEK 24: Food II ──
    {
        "char": "鱼", "pinyin": "yú", "tone": 2,
        "meaning": "fish",
        "example_cn": "吃鱼", "example_pinyin": "chī yú", "example_en": "eat fish",
        "group": "Food & Drink", "week": 24,
    },
    {
        "char": "鸡", "pinyin": "jī", "tone": 1,
        "meaning": "chicken; fowl",
        "example_cn": "鸡肉", "example_pinyin": "jīròu", "example_en": "chicken (meat)",
        "group": "Food & Drink", "week": 24,
    },
    {
        "char": "蛋", "pinyin": "dàn", "tone": 4,
        "meaning": "egg",
        "example_cn": "鸡蛋", "example_pinyin": "jīdàn", "example_en": "chicken egg",
        "group": "Food & Drink", "week": 24,
    },
    {
        "char": "豆", "pinyin": "dòu", "tone": 4,
        "meaning": "bean; pea; legume",
        "example_cn": "豆腐", "example_pinyin": "dòufu", "example_en": "tofu — lit. 'bean curd'",
        "group": "Food & Drink", "week": 24,
    },
    {
        "char": "果", "pinyin": "guǒ", "tone": 3,
        "meaning": "fruit; result; indeed; resolute",
        "example_cn": "水果", "example_pinyin": "shuǐguǒ", "example_en": "fruit — lit. 'water fruit'",
        "group": "Food & Drink", "week": 24,
    },
    {
        "char": "糖", "pinyin": "táng", "tone": 2,
        "meaning": "sugar; candy; sweet",
        "example_cn": "糖果", "example_pinyin": "tángguǒ", "example_en": "candy — lit. 'sugar fruit'",
        "group": "Food & Drink", "week": 24,
    },

    # ── WEEK 25: Transport & Places ──
    {
        "char": "车", "pinyin": "chē", "tone": 1,
        "meaning": "vehicle; car; train",
        "example_cn": "坐车", "example_pinyin": "zuò chē", "example_en": "to ride (take a vehicle)",
        "group": "Transport & Places", "week": 25,
    },
    {
        "char": "路", "pinyin": "lù", "tone": 4,
        "meaning": "road; path; route; journey",
        "example_cn": "一路平安", "example_pinyin": "yī lù píng'ān", "example_en": "have a safe journey",
        "group": "Transport & Places", "week": 25,
    },
    {
        "char": "门", "pinyin": "mén", "tone": 2,
        "meaning": "door; gate; entrance; (measure for courses)",
        "example_cn": "开门", "example_pinyin": "kāi mén", "example_en": "open the door",
        "group": "Transport & Places", "week": 25,
    },
    {
        "char": "城", "pinyin": "chéng", "tone": 2,
        "meaning": "city; town; city wall",
        "example_cn": "城市", "example_pinyin": "chéngshì", "example_en": "city",
        "group": "Transport & Places", "week": 25,
    },
    {
        "char": "店", "pinyin": "diàn", "tone": 4,
        "meaning": "shop; store; inn",
        "example_cn": "书店", "example_pinyin": "shūdiàn", "example_en": "bookstore",
        "group": "Transport & Places", "week": 25,
    },
    {
        "char": "站", "pinyin": "zhàn", "tone": 4,
        "meaning": "station; stop; to stand",
        "example_cn": "火车站", "example_pinyin": "huǒchēzhàn", "example_en": "train station",
        "group": "Transport & Places", "week": 25,
    },

    # ── WEEK 26: Modern Life ──
    {
        "char": "电", "pinyin": "diàn", "tone": 4,
        "meaning": "electricity; electric; lightning",
        "example_cn": "电脑", "example_pinyin": "diànnǎo", "example_en": "computer — lit. 'electric brain'",
        "group": "Modern Life", "week": 26,
    },
    {
        "char": "话", "pinyin": "huà", "tone": 4,
        "meaning": "speech; words; conversation; language",
        "example_cn": "说话", "example_pinyin": "shuōhuà", "example_en": "to talk; to speak",
        "group": "Modern Life", "week": 26,
    },
    {
        "char": "机", "pinyin": "jī", "tone": 1,
        "meaning": "machine; opportunity; airplane; crucial",
        "example_cn": "手机", "example_pinyin": "shǒujī", "example_en": "mobile phone — lit. 'hand machine'",
        "group": "Modern Life", "week": 26,
    },
    {
        "char": "网", "pinyin": "wǎng", "tone": 3,
        "meaning": "net; internet; network",
        "example_cn": "上网", "example_pinyin": "shàng wǎng", "example_en": "go online / surf the internet",
        "group": "Modern Life", "week": 26,
    },
    {
        "char": "书", "pinyin": "shū", "tone": 1,
        "meaning": "book; letter; document; to write",
        "example_cn": "看书", "example_pinyin": "kàn shū", "example_en": "read a book",
        "group": "Modern Life", "week": 26,
    },
    {
        "char": "钱", "pinyin": "qián", "tone": 2,
        "meaning": "money; coin; currency",
        "example_cn": "多少钱", "example_pinyin": "duōshǎo qián", "example_en": "How much does it cost?",
        "group": "Modern Life", "week": 26,
    },

    # ── WEEK 27: Commerce & Work ──
    {
        "char": "买", "pinyin": "mǎi", "tone": 3,
        "meaning": "to buy; to purchase",
        "example_cn": "我去买菜", "example_pinyin": "wǒ qù mǎi cài", "example_en": "I'm going to buy groceries",
        "group": "Commerce", "week": 27,
    },
    {
        "char": "卖", "pinyin": "mài", "tone": 4,
        "meaning": "to sell",
        "example_cn": "这里卖书", "example_pinyin": "zhèlǐ mài shū", "example_en": "Books are sold here",
        "group": "Commerce", "week": 27,
    },
    {
        "char": "工", "pinyin": "gōng", "tone": 1,
        "meaning": "work; labor; craft; industry",
        "example_cn": "工作", "example_pinyin": "gōngzuò", "example_en": "work; job",
        "group": "Commerce", "week": 27,
    },
    {
        "char": "作", "pinyin": "zuò", "tone": 4,
        "meaning": "to do; to make; to work; work/composition",
        "example_cn": "工作", "example_pinyin": "gōngzuò", "example_en": "work; job (same compound as 工)",
        "group": "Commerce", "week": 27,
    },
    {
        "char": "业", "pinyin": "yè", "tone": 4,
        "meaning": "industry; business; profession; studies",
        "example_cn": "毕业", "example_pinyin": "bìyè", "example_en": "to graduate",
        "group": "Commerce", "week": 27,
    },
    {
        "char": "市", "pinyin": "shì", "tone": 4,
        "meaning": "city; market; urban; trade",
        "example_cn": "超市", "example_pinyin": "chāoshì", "example_en": "supermarket",
        "group": "Commerce", "week": 27,
    },

    # ── WEEK 28: Education ──
    {
        "char": "学", "pinyin": "xué", "tone": 2,
        "meaning": "to study; to learn; school; -ology",
        "example_cn": "学中文", "example_pinyin": "xué zhōngwén", "example_en": "study Chinese",
        "group": "Education", "week": 28,
    },
    {
        "char": "校", "pinyin": "xiào", "tone": 4,
        "meaning": "school",
        "example_cn": "学校", "example_pinyin": "xuéxiào", "example_en": "school (institution)",
        "group": "Education", "week": 28,
    },
    {
        "char": "生", "pinyin": "shēng", "tone": 1,
        "meaning": "to be born; life; student; raw; unfamiliar",
        "example_cn": "学生", "example_pinyin": "xuésheng", "example_en": "student",
        "group": "Education", "week": 28,
    },
    {
        "char": "老", "pinyin": "lǎo", "tone": 3,
        "meaning": "old; elderly; very; always; experienced",
        "example_cn": "老师", "example_pinyin": "lǎoshī", "example_en": "teacher — lit. 'old master'",
        "group": "Education", "week": 28,
    },
    {
        "char": "师", "pinyin": "shī", "tone": 1,
        "meaning": "teacher; master; expert; division (military)",
        "example_cn": "老师", "example_pinyin": "lǎoshī", "example_en": "teacher",
        "group": "Education", "week": 28,
    },
    {
        "char": "语", "pinyin": "yǔ", "tone": 3,
        "meaning": "language; words; speech",
        "example_cn": "普通话", "example_pinyin": "pǔtōnghuà", "example_en": "Mandarin Chinese — lit. 'common speech'",
        "group": "Education", "week": 28,
    },

    # ── WEEK 29: Comparison & Degree ──
    {
        "char": "最", "pinyin": "zuì", "tone": 4,
        "meaning": "most; -est (superlative)",
        "example_cn": "最好", "example_pinyin": "zuì hǎo", "example_en": "best; the best",
        "group": "Comparison", "week": 29,
    },
    {
        "char": "更", "pinyin": "gèng", "tone": 4,
        "meaning": "more; even more; further; even",
        "example_cn": "更好", "example_pinyin": "gèng hǎo", "example_en": "even better",
        "group": "Comparison", "week": 29,
    },
    {
        "char": "比", "pinyin": "bǐ", "tone": 3,
        "meaning": "to compare; than (comparison); ratio",
        "example_cn": "他比我高", "example_pinyin": "tā bǐ wǒ gāo", "example_en": "He is taller than me",
        "group": "Comparison", "week": 29,
    },
    {
        "char": "些", "pinyin": "xiē", "tone": 1,
        "meaning": "some; a few; a little (plural-ish marker)",
        "example_cn": "这些书", "example_pinyin": "zhèxiē shū", "example_en": "these books",
        "group": "Comparison", "week": 29,
    },
    {
        "char": "又", "pinyin": "yòu", "tone": 4,
        "meaning": "again; also; both...and...",
        "example_cn": "又大又好", "example_pinyin": "yòu dà yòu hǎo", "example_en": "both big and good",
        "group": "Comparison", "week": 29,
    },
    {
        "char": "还", "pinyin": "hái", "tone": 2,
        "meaning": "still; yet; also; even more; as well",
        "example_cn": "还有问题吗", "example_pinyin": "hái yǒu wèntí ma", "example_en": "Are there still questions?",
        "group": "Comparison", "week": 29,
    },

    # ── WEEK 30: Function Words I ──
    {
        "char": "以", "pinyin": "yǐ", "tone": 3,
        "meaning": "by means of; with; so as to; according to",
        "example_cn": "以后", "example_pinyin": "yǐhòu", "example_en": "after; in the future",
        "group": "Function Words", "week": 30,
    },
    {
        "char": "从", "pinyin": "cóng", "tone": 2,
        "meaning": "from; since; follow; through",
        "example_cn": "你从哪里来", "example_pinyin": "nǐ cóng nǎlǐ lái", "example_en": "Where are you from?",
        "group": "Function Words", "week": 30,
    },
    {
        "char": "于", "pinyin": "yú", "tone": 2,
        "meaning": "at; in; to; than; from (literary/formal)",
        "example_cn": "关于", "example_pinyin": "guānyú", "example_en": "about; regarding; concerning",
        "group": "Function Words", "week": 30,
    },
    {
        "char": "为", "pinyin": "wèi", "tone": 4,
        "meaning": "for; because of; on behalf of; to be (literary)",
        "example_cn": "为什么", "example_pinyin": "wèishénme", "example_en": "why? — lit. 'for what reason'",
        "group": "Function Words", "week": 30,
    },
    {
        "char": "被", "pinyin": "bèi", "tone": 4,
        "meaning": "passive marker (by); quilt",
        "example_cn": "被老师批评", "example_pinyin": "bèi lǎoshī pīpíng", "example_en": "was criticized by the teacher",
        "group": "Function Words", "week": 30,
    },
    {
        "char": "让", "pinyin": "ràng", "tone": 4,
        "meaning": "to let; to allow; to ask someone to; to yield",
        "example_cn": "让我来", "example_pinyin": "ràng wǒ lái", "example_en": "Let me do it",
        "group": "Function Words", "week": 30,
    },

    # ── WEEK 31: Function Words II ──
    {
        "char": "把", "pinyin": "bǎ", "tone": 3,
        "meaning": "to take/hold; disposal marker (把-construction); handle",
        "example_cn": "把书放下", "example_pinyin": "bǎ shū fàng xià", "example_en": "put the book down",
        "group": "Function Words", "week": 31,
    },
    {
        "char": "给", "pinyin": "gěi", "tone": 3,
        "meaning": "to give; for; to (indirect object marker)",
        "example_cn": "给我看", "example_pinyin": "gěi wǒ kàn", "example_en": "show me / let me see",
        "group": "Function Words", "week": 31,
    },
    {
        "char": "向", "pinyin": "xiàng", "tone": 4,
        "meaning": "toward; facing; direction; always",
        "example_cn": "向前走", "example_pinyin": "xiàng qián zǒu", "example_en": "walk forward",
        "group": "Function Words", "week": 31,
    },
    {
        "char": "对", "pinyin": "duì", "tone": 4,
        "meaning": "correct; toward; to face; pair; regarding",
        "example_cn": "对不起", "example_pinyin": "duìbuqǐ", "example_en": "sorry; I'm sorry",
        "group": "Function Words", "week": 31,
    },
    {
        "char": "才", "pinyin": "cái", "tone": 2,
        "meaning": "only then; just now; only; talent; ability",
        "example_cn": "现在才来", "example_pinyin": "xiànzài cái lái", "example_en": "only just arriving now (implies late)",
        "group": "Function Words", "week": 31,
    },
    {
        "char": "没", "pinyin": "méi", "tone": 2,
        "meaning": "not; haven't; to lack; (méi yǒu = don't have / didn't)",
        "example_cn": "没有问题", "example_pinyin": "méiyǒu wèntí", "example_en": "no problem; there is no problem",
        "group": "Function Words", "week": 31,
    },

    # ── WEEK 32: Emotions ──
    {
        "char": "爱", "pinyin": "ài", "tone": 4,
        "meaning": "to love; love; affection; to like to",
        "example_cn": "我爱你", "example_pinyin": "wǒ ài nǐ", "example_en": "I love you",
        "group": "Emotions", "week": 32,
    },
    {
        "char": "恨", "pinyin": "hèn", "tone": 4,
        "meaning": "to hate; hatred; to regret",
        "example_cn": "我恨你", "example_pinyin": "wǒ hèn nǐ", "example_en": "I hate you",
        "group": "Emotions", "week": 32,
    },
    {
        "char": "笑", "pinyin": "xiào", "tone": 4,
        "meaning": "to laugh; to smile; to laugh at",
        "example_cn": "开心地笑", "example_pinyin": "kāixīn de xiào", "example_en": "laugh happily",
        "group": "Emotions", "week": 32,
    },
    {
        "char": "哭", "pinyin": "kū", "tone": 1,
        "meaning": "to cry; to weep",
        "example_cn": "别哭了", "example_pinyin": "bié kū le", "example_en": "stop crying",
        "group": "Emotions", "week": 32,
    },
    {
        "char": "怕", "pinyin": "pà", "tone": 4,
        "meaning": "to fear; afraid; perhaps",
        "example_cn": "我怕蛇", "example_pinyin": "wǒ pà shé", "example_en": "I'm afraid of snakes",
        "group": "Emotions", "week": 32,
    },
    {
        "char": "急", "pinyin": "jí", "tone": 2,
        "meaning": "urgent; anxious; impatient; hasty",
        "example_cn": "不急", "example_pinyin": "bù jí", "example_en": "no rush; don't worry",
        "group": "Emotions", "week": 32,
    },

    # ── WEEK 33: Abstract Concepts ──
    {
        "char": "死", "pinyin": "sǐ", "tone": 3,
        "meaning": "to die; death; extremely (informal intensifier)",
        "example_cn": "累死了", "example_pinyin": "lèi sǐ le", "example_en": "dead tired — lit. 'tired to death'",
        "group": "Abstract", "week": 33,
    },
    {
        "char": "梦", "pinyin": "mèng", "tone": 4,
        "meaning": "dream; to dream",
        "example_cn": "做梦", "example_pinyin": "zuò mèng", "example_en": "to dream / to have a dream",
        "group": "Abstract", "week": 33,
    },
    {
        "char": "意", "pinyin": "yì", "tone": 4,
        "meaning": "meaning; intention; thought; wish",
        "example_cn": "意思", "example_pinyin": "yìsi", "example_en": "meaning; interesting",
        "group": "Abstract", "week": 33,
    },
    {
        "char": "情", "pinyin": "qíng", "tone": 2,
        "meaning": "feeling; emotion; situation; love; passion",
        "example_cn": "感情", "example_pinyin": "gǎnqíng", "example_en": "feelings; emotions; relationship",
        "group": "Abstract", "week": 33,
    },
    {
        "char": "感", "pinyin": "gǎn", "tone": 3,
        "meaning": "to feel; to sense; emotion; gratitude",
        "example_cn": "感谢", "example_pinyin": "gǎnxiè", "example_en": "to thank; to feel grateful",
        "group": "Abstract", "week": 33,
    },
    {
        "char": "思", "pinyin": "sī", "tone": 1,
        "meaning": "to think; to miss; thought; idea",
        "example_cn": "思念", "example_pinyin": "sīniàn", "example_en": "to miss someone; longing",
        "group": "Abstract", "week": 33,
    },
]

# Total: 200 characters across 33 themed weekly groups
assert len(CHARACTERS) == 200, f"Expected 200 characters, got {len(CHARACTERS)}"
