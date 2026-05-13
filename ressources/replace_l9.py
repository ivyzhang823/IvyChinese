"""Replace the incorrect L9 stub with real content from 不用手机的日子."""
import re
from pathlib import Path

HTML = Path('D:/Claude_CODE/IvyChinese/HSK/HSK6/hsk6_01-10.html')

# ============================================================
# NEW L9 HEADER (replaces 第九课 + wrong subtitle)
# ============================================================
NEW_HEADER = '''  <div class="lesson-header" id="lesson-header-9" data-lesson="9" data-watermark="九" style="display:none">
    <div class="lesson-meta">
      <button class="lesson-tag" onclick="showIndex()">
        <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"/></svg>
        HSK 6
      </button>
      <span class="lesson-tag-num">第九课 · Lesson 09</span>
    </div>
    <h1>不用手机的日子</h1>
    <p style="font-size:0.9rem;color:var(--gold);margin-bottom:0.3rem;letter-spacing:0.02em;">Bùyòng shǒujī de rìzi</p>
    <p class="lesson-subtitle">A day without a cell phone</p>
  </div>'''

# ============================================================
# NEW L9 LESSON CONTENT (replaces full lesson-content block)
# ============================================================

# Vocabulary (47 words from textbook pages 85-87)
VOCAB = [
    ("正经", "zhèngjing", "adj.", "serious, proper", "别假装<em>正经</em>。", "Stop pretending to be proper."),
    ("玩意儿", "wányìr", "n.", "toy, thing", "那<em>玩意儿</em>这么好玩儿？", "Is that thing really so fun?"),
    ("憋", "biē", "v.", "to suppress, to hold back", "我脸<em>憋</em>得通红。", "My face flushed red from holding it in."),
    ("报警", "bàojǐng", "v.", "to call the police", "撞坏了桥也没<em>报警</em>。", "Crashed the bridge and didn't even call the police."),
    ("绑架", "bǎngjià", "v.", "to kidnap", "都让手机给你<em>绑架</em>了。", "You've all been kidnapped by your phones."),
    ("受罚", "shòufá", "v.", "to be punished", "这么过日子，不<em>受罚</em>吗？", "Living like this, won't you be punished?"),
    ("吼", "hǒu", "v.", "to shout, to roar", "老板大<em>吼</em>：'有病就得治！'", "The boss roared: 'If it's a sickness, it must be cured!'"),
    ("智能", "zhìnéng", "adj.", "smart, intelligent", "有了<em>智能</em>手机就成了奴隶。", "With a smartphone you become a slave."),
    ("麻木", "mámù", "adj.", "numb, apathetic", "每根神经都<em>麻木</em>了。", "Every nerve has gone numb."),
    ("狼吞虎咽", "lángtūn-hǔyàn", "idiom", "to wolf down, to gobble up", "<em>狼吞虎咽</em>吃饭。", "Wolf down the food."),
    ("伺候", "cìhou", "v.", "to serve, to wait upon", "把手机当老人家<em>伺候</em>。", "I served my phone like an elder."),
    ("眨", "zhǎ", "v.", "to blink, to wink", "我冲他<em>眨</em>眨眼。", "I winked at him."),
    ("索性", "suǒxìng", "adv.", "might as well, simply", "<em>索性</em>这礼拜就开始。", "Might as well start this week."),
    ("作息", "zuòxī", "v.", "to work and rest", "按小学生的<em>作息</em>时间。", "Following a schoolkid's work-and-rest schedule."),
    ("着手", "zhuóshǒu", "v.", "to begin, to set about", "先<em>着手</em>安置我的手机。", "First I set about putting my phone away."),
    ("安置", "ānzhì", "v.", "to find a place for, to arrange", "<em>安置</em>我的手机。", "Find a place for my phone."),
    ("防止", "fángzhǐ", "v.", "to prevent", "为了<em>防止</em>意志薄弱。", "To prevent weak willpower."),
    ("薄弱", "bóruò", "adj.", "weak, frail", "意志<em>薄弱</em>。", "Weak willpower."),
    ("精致", "jīngzhì", "adj.", "fine, exquisite", "一个<em>精致</em>的盒子。", "An exquisite box."),
    ("庄重", "zhuāngzhòng", "adj.", "solemn, dignified", "<em>庄重</em>地放在盒子里。", "Solemnly place it in the box."),
    ("分散", "fēnsàn", "v.", "to divert, to distract", "<em>分散</em>注意力。", "Divert one's attention."),
    ("僵硬", "jiāngyìng", "adj.", "stiff, hardened", "锻炼我那<em>僵硬</em>的四肢。", "Exercise my stiff limbs."),
    ("四肢", "sìzhī", "n.", "four limbs", "我那僵硬的<em>四肢</em>。", "My stiff limbs."),
    ("特长", "tècháng", "n.", "strong suit, forte", "跳舞是我的<em>特长</em>。", "Dancing is my forte."),
    ("兴高采烈", "xìnggāo-cǎiliè", "idiom", "in high spirits, cheerful", "<em>兴高采烈</em>地跳起了摇滚。", "Cheerfully started dancing rock and roll."),
    ("摇滚", "yáogǔn", "n.", "rock and roll", "跳起了<em>摇滚</em>。", "Started dancing rock and roll."),
    ("一举两得", "yìjǔ-liǎngdé", "idiom", "to kill two birds with one stone", "修身又锻炼身体，<em>一举两得</em>。", "Calms the mind and exercises the body — two birds with one stone."),
    ("冷落", "lěngluò", "v.", "to treat coldly, to neglect", "被<em>冷落</em>了半天儿的手机。", "The phone that had been neglected for half a day."),
    ("踏实", "tāshi", "adj.", "at peace, free from anxiety", "我心里<em>踏实</em>了许多。", "I felt much more at peace."),
    ("空虚", "kōngxū", "adj.", "empty, hollow", "弥补心中的<em>空虚</em>。", "Make up for the emptiness in my heart."),
    ("要命", "yàomìng", "v.", "to an extreme degree", "心里虚得<em>要命</em>。", "I felt extremely empty inside."),
    ("粥", "zhōu", "n.", "porridge, congee", "熬<em>粥</em>这种最消耗时间的事。", "Cooking porridge — the most time-consuming thing."),
    ("消耗", "xiāohào", "v.", "to consume, to expend", "最<em>消耗</em>时间的事。", "The most time-consuming task."),
    ("弥补", "míbǔ", "v.", "to make up for, to remedy", "<em>弥补</em>心中的空虚。", "Make up for the emptiness inside."),
    ("沸腾", "fèiténg", "v.", "to boil, to bubble", "雪白的米在<em>沸腾</em>的水中翻滚。", "The snow-white rice tumbles in the boiling water."),
    ("弥漫", "mímàn", "v.", "to permeate, to fill the air", "屋子里渐渐<em>弥漫</em>着粥的香气。", "The room gradually filled with the scent of porridge."),
    ("往常", "wǎngcháng", "n.", "usually, habitually in the past", "要在<em>往常</em>，我一定坚持不住了。", "Usually, I wouldn't have lasted."),
    ("侦探", "zhēntàn", "n.", "detective", "我那<em>侦探</em>的案件。", "My detective cases."),
    ("案件", "ànjiàn", "n.", "legal case", "侦探的<em>案件</em>。", "Detective cases."),
    ("突破", "tūpò", "v.", "to break through, to make a breakthrough", "是不是有了<em>突破</em>。", "Whether there has been a breakthrough."),
    ("震惊", "zhènjīng", "v.", "to shock, to astonish", "科学家是否有了<em>震惊</em>世界的发现。", "Whether scientists had a shocking discovery."),
    ("彩票", "cǎipiào", "n.", "lottery ticket", "买<em>彩票</em>。", "Buy a lottery ticket."),
    ("恐怖", "kǒngbù", "adj.", "terrible, horrible", "<em>恐怖</em>袭击。", "Terror attack."),
    ("袭击", "xíjī", "v.", "to attack, to assault", "前两天的恐怖<em>袭击</em>。", "The terror attack of a few days ago."),
    ("干扰", "gānrǎo", "v.", "to disturb, to interfere", "没有手机的<em>干扰</em>。", "Without the disturbance of the phone."),
    ("安宁", "ānníng", "adj.", "peaceful, tranquil", "享受着一种回归生活的<em>安宁</em>。", "Enjoying a peaceful return to life."),
    ("通红", "tōnghóng", "adj.", "very red, flushed", "脸憋得<em>通红</em>。", "His face flushed deep red."),
]

def fc_card(zh, py, pos, en):
    return f'<div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">{zh}</div><div class="fcs-pos">{pos}</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">{py}</div><div class="fcs-en">{en}</div></div></div></div>'

def vocab_card(zh, py, pos, en, ex_zh, ex_en):
    return f'<div class="vocab-card"><div class="vocab-zh">{zh}</div><div class="vocab-pinyin">{py}</div><div class="vocab-pos">{pos}</div><div class="vocab-en">{en}</div><div class="vocab-example">{ex_zh}<br><span style="color:#bbb">{ex_en}</span></div></div>'

# Build flashcards
fc_cards = []
for i, (zh, py, pos, en, _, _) in enumerate(VOCAB):
    card = fc_card(zh, py, pos, en)
    if i == 0:
        card = card.replace('class="fc-card"', 'class="fc-card active"', 1)
    fc_cards.append('            ' + card)
fc_cards_html = '\n'.join(fc_cards)

# Build vocab cards
vocab_cards_html = '\n        '.join(vocab_card(*v) for v in VOCAB)

NEW_CONTENT = f'''  <div class="lesson-content" data-lesson="9" style="display:none">
  <div class="tab-nav">
    <button class="tab-btn active" onclick="switchTab('text', this)">📖 课文</button>
    <button class="tab-btn" onclick="switchTab('vocab', this)">📝 生词表</button>
    <button class="tab-btn" onclick="switchTab('worddetail', this)">🔍 词汇详解</button>
    <button class="tab-btn" onclick="switchTab('grammar', this)">🔤 语法</button>
    <button class="tab-btn" onclick="switchTab('exercise', this)">✏️ 练习</button>
    <button class="tab-btn" onclick="switchTab('culture', this)">🏮 更多</button>
  </div>
  <div class="content-area">

    <!-- 课文 -->
    <div data-tab="text" class="tab-panel active">
      <div class="dialogue-block" id="l9-block1">
        <div class="dialogue-header">
          <div class="dialogue-title-wrap">
            <div class="dialogue-title-row">
              <span class="dialogue-title">课文 · 不用手机的日子</span>
              <button class="dh-play-btn" id="l9-dhBtn1" onclick="dhPlay('l9-audioEl1','l9-dhBtn1')">
                <svg id="l9-dhIcon1" viewBox="0 0 24 24"><polygon points="5 3 19 12 5 21 5 3"/></svg>
              </button>
              <span style="flex:1;"></span>
              <div class="toggle-btns">
                <button class="toggle-btn" onclick="toggleBlock(this,'pinyin','l9-block1')"><span class="dot"></span>拼音</button>
                <button class="toggle-btn" onclick="toggleBlock(this,'en','l9-block1')"><span class="dot"></span>En</button>
              </div>
            </div>
            <span class="dialogue-title-en">A day without a cell phone</span>
          </div>
          <audio id="l9-audioEl1" src="" onended="dhEnded('l9-audioEl1','l9-dhBtn1','l9-dhIcon1')" ontimeupdate="dhUpdate('l9-audioEl1')"></audio>
        </div>
        <div class="dialogue-line" style="display:block;">
          <div class="line-content" style="font-size:0.88em;">
            <div class="line-zh" style="line-height:1.9;">
              <p style="margin:0 0 0.15em 0;">开会时老板火了："别假装正经，我知道你们都在玩儿手机，那玩意儿这么好玩儿？"</p>
              <p class="line-pinyin" style="margin:0 0 1.1em 0;display:none;">Kāihuì shí lǎobǎn huǒ le: "Bié jiǎzhuāng zhèngjing, wǒ zhīdào nǐmen dōu zài wánr shǒujī, nà wányìr zhème hǎowánr?"</p>
              <p style="margin:0 0 0.15em 0;">老板指着我："你说说，看了什么？比我说话还有意思？"<br>我脸憋得通红，说："一时年轻人这边在玩儿手机拍照，把桥撞坏了几次，没报警，先下车拍照发微信。要不要受罚呢？"</p>
              <p class="line-pinyin" style="margin:0 0 1.1em 0;display:none;">Lǎobǎn zhǐ zhe wǒ: "Nǐ shuōshuo, kàn le shénme? Bǐ wǒ shuōhuà hái yǒuyìsi?" Wǒ liǎn biē de tōnghóng, shuō: "Yīshí niánqīngrén zhè biān zài wánr shǒujī pāizhào, bǎ qiáo zhuàng huài le jǐ cì, méi bàojǐng, xiān xiàchē pāizhào fā wēixìn. Yào bú yào shòufá ne?"</p>
              <p style="margin:0 0 0.15em 0;">老板一摆手："你们听，都让手机给你绑架了，这么过日子，不受罚吗？"<br>一同事举手："老板，刚搜索了一下，离不开手机也是一种精神病。"<br>老板大吼："有病就得治！"<br>随后黑着脸撂下一句话："以后开会谁都不许带手机！"</p>
              <p class="line-pinyin" style="margin:0 0 1.1em 0;display:none;">Lǎobǎn yī bǎishǒu: "Nǐmen tīng, dōu ràng shǒujī gěi nǐ bǎngjià le, zhème guò rìzi, bú shòufá ma?" Yī tóngshì jǔshǒu: "Lǎobǎn, gāng sōusuǒ le yīxià, lí bù kāi shǒujī yě shì yī zhǒng jīngshén bìng." Lǎobǎn dà hǒu: "Yǒu bìng jiù děi zhì!" Suíhòu hēi zhe liǎn liào xià yī jù huà: "Yǐhòu kāihuì shéi dōu bù xǔ dài shǒujī!"</p>
              <p style="margin:0 0 0.15em 0;">老板说的没错，特别是有了智能手机，我就成了手机的奴隶，每根神经都麻木了。心里只有手机：三分钟看一次微信，饭馆儿先拍照，狼吞虎咽吃饭，吃罢回头看微信；睡觉之前先给手机充电……把手机当老人家伺候得倍儿好。一次刚毛对我说："我跟你说话呢，你干吗老看手机！"我冲他眨眨眼，说："那你也拿手机，咱们手机上谈吧，保证不分心！"</p>
              <p class="line-pinyin" style="margin:0 0 1.1em 0;display:none;">Lǎobǎn shuō de méi cuò, tèbié shì yǒu le zhìnéng shǒujī, wǒ jiù chéng le shǒujī de núlì, měi gēn shénjīng dōu mámù le. Xīnli zhǐ yǒu shǒujī: sān fēnzhōng kàn yī cì wēixìn, fànguǎnr xiān pāizhào, lángtūn-hǔyàn chīfàn, chī bà huítóu kàn wēixìn; shuìjiào zhīqián xiān gěi shǒujī chōngdiàn… bǎ shǒujī dāng lǎorénjiā cìhou de bèir hǎo. Yī cì Gāngmáo duì wǒ shuō: "Wǒ gēn nǐ shuōhuà ne, nǐ gànmá lǎo kàn shǒujī!" Wǒ chòng tā zhǎzha yǎn, shuō: "Nà nǐ yě ná shǒujī, zánmen shǒujī shàng tán ba, bǎozhèng bù fēnxīn!"</p>
              <p style="margin:0 0 0.15em 0;">离开了手机，难道会死吗？何不尝试一下一周关机一天？说干就干，索性这礼拜就开始。</p>
              <p class="line-pinyin" style="margin:0 0 1.1em 0;display:none;">Líkāi le shǒujī, nándào huì sǐ ma? Hébù chángshì yīxià yī zhōu guānjī yī tiān? Shuō gàn jiù gàn, suǒxìng zhè lǐbài jiù kāishǐ.</p>
              <p style="margin:0 0 0.15em 0;">周日，我按小学生的作息时间七点起来，之后，先着手安置我的手机。为了防止自己意志薄弱，我找来个精致的盒子，把手机层层包好，庄重地放在盒子里，收到衣柜最里面。为了分散注意力，我决定去公园锻炼我那僵硬的四肢，因为这几年迷上手机以后，我已经好久不锻炼了。</p>
              <p class="line-pinyin" style="margin:0 0 1.1em 0;display:none;">Zhōurì, wǒ àn xiǎoxuéshēng de zuòxī shíjiān qī diǎn qǐlái, zhīhòu, xiān zhuóshǒu ānzhì wǒ de shǒujī. Wèile fángzhǐ zìjǐ yìzhì bóruò, wǒ zhǎo lái gè jīngzhì de hézi, bǎ shǒujī céngcéng bāo hǎo, zhuāngzhòng de fàng zài hézi lǐ, shōu dào yīguì zuì lǐmiàn. Wèile fēnsàn zhùyìlì, wǒ juédìng qù gōngyuán duànliàn wǒ nà jiāngyìng de sìzhī, yīnwèi zhè jǐ nián mí shàng shǒujī yǐhòu, wǒ yǐjīng hǎojiǔ bù duànliàn le.</p>
              <p style="margin:0 0 0.15em 0;">公园里唱的跳的都有。跳舞是我的特长，我兴高采烈地跳起了摇滚，跳舞既能修身心，又能锻炼身体，一举两得。</p>
              <p class="line-pinyin" style="margin:0 0 1.1em 0;display:none;">Gōngyuán lǐ chàng de tiào de dōu yǒu. Tiàowǔ shì wǒ de tècháng, wǒ xìnggāo-cǎiliè de tiào qǐ le yáogǔn, tiàowǔ jì néng xiū shēn xīn, yòu néng duànliàn shēntǐ, yìjǔ-liǎngdé.</p>
              <p style="margin:0 0 0.15em 0;">跳完舞，我往家走，突然想起被冷落了半天儿的手机，急忙赶回家，打开衣柜，手机还在，我心里踏实了许多。五个小时没碰它，我心里虚得要命，我决定用熬粥这种最消耗时间的事来弥补心中的空虚。烧水，下米，看着雪白的米在沸腾的水中翻滚，屋子里渐渐弥漫着粥的香气，我竟然听来了鸟的叫声，我的心慢慢静下来。要在往常，我一定坚持不住了，惦记着我那侦探的案件，是不是有了突破，科学家是否有了震惊，前两天的恐怖袭击查到底是谁干的……</p>
              <p class="line-pinyin" style="margin:0 0 1.1em 0;display:none;">Tiào wán wǔ, wǒ wǎng jiā zǒu, túrán xiǎngqǐ bèi lěngluò le bàntiānr de shǒujī, jímáng gǎn huí jiā, dǎkāi yīguì, shǒujī hái zài, wǒ xīnli tāshi le xǔduō. Wǔ ge xiǎoshí méi pèng tā, wǒ xīnli xū de yàomìng, wǒ juédìng yòng áo zhōu zhè zhǒng zuì xiāohào shíjiān de shì lái míbǔ xīnzhōng de kōngxū. Shāo shuǐ, xià mǐ, kàn zhe xuěbái de mǐ zài fèiténg de shuǐ zhōng fāngǔn, wūzi lǐ jiànjiàn mímàn zhe zhōu de xiāngqì, wǒ jìngrán tīng lái le niǎo de jiào shēng, wǒ de xīn mànmàn jìng xiàlái. Yào zài wǎngcháng, wǒ yīdìng jiānchí bú zhù le, diànjì zhe wǒ nà zhēntàn de ànjiàn, shì bú shì yǒu le tūpò, kēxuéjiā shìfǒu yǒu le zhènjīng, qián liǎng tiān de kǒngbù xíjī chá dàodǐ shì shéi gàn de……</p>
              <p style="margin:0 0 0.15em 0;">没有手机的干扰，我享受到了一种回归生活的安宁。</p>
              <p class="line-pinyin" style="margin:0 0 1.1em 0;display:none;">Méi yǒu shǒujī de gānrǎo, wǒ xiǎngshòu dào le yī zhǒng huíguī shēnghuó de ānníng.</p>
            </div>
            <div class="line-en" style="margin-top:1.5em;padding-top:1em;border-top:1px solid var(--mist);display:none;">At a meeting, the boss got furious: "Stop pretending to be proper — I know you're all on your phones. Are those things really so much fun?"<br><br>He pointed at me: "Tell us, what were you looking at? More interesting than what I'm saying?" My face flushed deep red. I stammered: "I was reading that some young driver was so busy taking photos and posting them on WeChat that he crashed into a bridge several times — and didn't even call the police, he just got out to take a picture first. Doesn't that deserve punishment?"<br><br>The boss waved his hand: "Listen — you've all been kidnapped by your phones. Living like this, won't you all be punished?" A colleague raised his hand: "Boss, I just searched it — phone addiction is actually a mental illness." The boss roared: "If it's a sickness, it has to be cured!" Then with a dark face he dropped the order: "From now on, no phones in meetings!"<br><br>The boss wasn't wrong. Ever since smartphones came along, I had become a slave to mine — every nerve gone numb. My mind held only my phone: I checked WeChat every three minutes, photographed every dish at restaurants, wolfed down food only to immediately check WeChat again, charged the phone before going to bed… I served it like an old elder. Once, my friend Gangmao said, "I'm talking to you — why are you always staring at your phone?" I winked back and said: "Then grab yours too, we'll talk via WeChat — guaranteed no distractions!"<br><br>Could one really die without a phone? Why not try one phone-free day per week? Said and done — I'd start this very week.<br><br>Sunday, I got up at seven, on a primary-schooler's schedule. The first thing I did was put my phone away. To guard against weak willpower, I found a fancy box, wrapped the phone layer after layer, ceremoniously placed it inside, and tucked it deep into the back of the wardrobe. To distract myself, I went to the park to exercise my stiff limbs — I'd barely moved since smartphones took over.<br><br>The park had everything — singing, dancing. Dance is my forte, so I joyfully launched into rock and roll. Dancing soothes the mind and exercises the body — two birds with one stone.<br><br>After dancing, walking home, I suddenly remembered the phone I'd neglected all morning. I hurried back, opened the wardrobe — it was still there. My heart settled. Five hours without touching it had left me feeling oddly empty, so I decided to fill the void with the most time-consuming task: cooking porridge. I lit the fire, poured in the rice, watched the snow-white grains tumble in the bubbling water, smelled the porridge slowly filling the room — I even caught the song of birds outside. My mind grew calm. Normally I'd have caved by now, worrying whether my detective show's case had a breakthrough, whether the scientists had announced anything shocking, who was behind the terror attack a few days ago…<br><br>Without the disturbance of the phone, I tasted a kind of peace — the peace of returning to life.</div>
          </div>
        </div>
      </div>
    </div><!-- end 课文 tab -->

    <!-- 生词表 -->
    <div data-tab="vocab" class="tab-panel">
      <div class="fc-slider-wrap">
        <div class="fc-row">
          <div class="fc-slider" id="l9-fcSlider">
{fc_cards_html}
          </div>
        </div>
        <div style="display:flex;align-items:center;gap:10px;margin-top:10px;">
          <button class="fc-arrow" onclick="fcNav(-1)"><svg viewBox="0 0 24 24"><polyline points="15 18 9 12 15 6"/></svg></button>
          <span class="fc-counter" id="l9-fcCounter" style="min-width:36px;text-align:center;line-height:1;">1 / {len(VOCAB)}</span>
          <button class="fc-arrow" onclick="fcNav(1)"><svg viewBox="0 0 24 24"><polyline points="9 18 15 12 9 6"/></svg></button>
        </div>
      </div>
      <a href="https://quizlet.com" target="_blank" rel="noopener"
         style="display:inline-flex;align-items:center;gap:8px;text-decoration:none;margin-bottom:1.4rem;padding:7px 14px;border:1.5px solid #e0e0ff;border-radius:8px;background:#f5f5ff;"
         onmouseover="this.style.background='#eaecff';this.style.borderColor='#4255FF'"
         onmouseout="this.style.background='#f5f5ff';this.style.borderColor='#e0e0ff'">
        <svg width="24" height="24" viewBox="0 0 36 36" fill="none"><rect width="36" height="36" rx="8" fill="#4255FF"/><text x="18" y="25" text-anchor="middle" font-family="Arial,sans-serif" font-size="18" font-weight="700" fill="#fff">Q</text></svg>
        <span style="font-size:0.78rem;font-weight:600;color:#4255FF;font-family:'Outfit',sans-serif;">More HSK Vocabulary on Quizlet</span>
      </a>
      <div class="vocab-grid">
        {vocab_cards_html}
      </div>
    </div><!-- end vocab tab -->

    <!-- 词汇详解 -->
    <div data-tab="worddetail" class="tab-panel">
      <div class="vocab-card">
        <div class="vocab-zh">狼吞虎咽</div><div class="vocab-pinyin">lángtūn-hǔyàn</div><div class="vocab-pos">idiom</div>
        <div class="vocab-en">to wolf down food; to eat ravenously (lit. "wolf-swallow, tiger-gulp") — vivid four-character idiom describing voracious eating</div>
        <div class="vocab-example">
          <em>狼吞虎咽</em>吃饭。<br>
          <span style="color:#bbb">Wolf down one's food.</span><br>
          饿了一整天，他<em>狼吞虎咽</em>地把饭吃完了。<br>
          <span style="color:#bbb">Starving after a whole day, he wolfed down the meal.</span>
        </div>
      </div>
      <div class="vocab-card">
        <div class="vocab-zh">兴高采烈</div><div class="vocab-pinyin">xìnggāo-cǎiliè</div><div class="vocab-pos">idiom</div>
        <div class="vocab-en">in high spirits; jubilant; with great enthusiasm (lit. "spirits-high, glow-fierce") — describes cheerful excitement</div>
        <div class="vocab-example">
          我<em>兴高采烈</em>地跳起了摇滚。<br>
          <span style="color:#bbb">I joyfully launched into rock and roll.</span><br>
          孩子们<em>兴高采烈</em>地玩了一整天。<br>
          <span style="color:#bbb">The children played all day in high spirits.</span>
        </div>
      </div>
      <div class="vocab-card">
        <div class="vocab-zh">一举两得</div><div class="vocab-pinyin">yìjǔ-liǎngdé</div><div class="vocab-pos">idiom</div>
        <div class="vocab-en">to kill two birds with one stone (lit. "one action, two gains") — to achieve two objectives with a single act</div>
        <div class="vocab-example">
          跳舞既能修身心，又能锻炼身体，<em>一举两得</em>。<br>
          <span style="color:#bbb">Dancing soothes the mind and exercises the body — two birds with one stone.</span><br>
          骑车上班既能省钱又能健身，<em>一举两得</em>。<br>
          <span style="color:#bbb">Cycling to work saves money and keeps you fit — two birds, one stone.</span>
        </div>
      </div>
      <div class="vocab-card">
        <div class="vocab-zh">说A就A</div><div class="vocab-pinyin">shuō A jiù A</div><div class="vocab-pos">pattern</div>
        <div class="vocab-en">Says X and immediately X — pattern expressing that something happens suddenly or that an idea is acted on at once. A is repeated and is typically a verb/adjective</div>
        <div class="vocab-example">
          <em>说干就干</em>，索性这礼拜就开始。<br>
          <span style="color:#bbb">Said and done — I'd start this very week.</span><br>
          天气<em>说变就变</em>，刚才还出太阳，现在就下雨了。<br>
          <span style="color:#bbb">The weather changes on a dime — sun a moment ago, rain now.</span>
        </div>
      </div>
    </div><!-- end worddetail tab -->

    <!-- 语法 -->
    <div data-tab="grammar" class="tab-panel">
      <div class="grammar-switcher">
        <button class="grammar-switch-btn active" onclick="switchGrammar(0, this)">通红/雪白</button>
        <button class="grammar-switch-btn" onclick="switchGrammar(1, this)">说A就A</button>
        <button class="grammar-switch-btn" onclick="switchGrammar(2, this)">adj./v.+得+要命</button>
        <button class="grammar-switch-btn" onclick="switchGrammar(3, this)">索性 vs 干脆</button>
      </div>
      <div class="grammar-panel active">
        <div class="grammar-block">
          <div class="grammar-title"><span class="grammar-num">1</span>通红、雪白 · "Through-red", "Snow-white" — intensified state adjectives</div>
          <p class="grammar-desc">"通红"、"雪白"都是状态形容词。"通红"表示十分鲜艳的红，"雪白"表示像雪一样的白，词义重在第二个字。这类形容词一般已含程度义，因此不能再用"很"、"非常"、"特别"等程度词来修饰，后面也不能加"极了""得很"等表示程度的补语。<br><span style="color:#888;font-size:0.85em;">State adjectives like 通红 ("through-red") and 雪白 ("snow-white") already carry a degree meaning, so they cannot be modified by 很/非常/极了 etc. They tend to follow an AABB-like vivid pattern.</span></p>
          <div class="grammar-pattern">[noun] + 通红 / 雪白 / 漆黑 / 笔直 / 冰凉 …  ✗ 很通红</div>
          <div class="grammar-examples">
            <div class="grammar-ex"><div class="zh">我脸憋得通红。</div><div class="en">My face flushed deep red from holding it in.</div></div>
            <div class="grammar-ex"><div class="zh">雪白的米在沸腾的水中翻滚，屋子里渐渐弥漫着粥的香气。</div><div class="en">The snow-white rice tumbled in the boiling water; the room slowly filled with the scent of porridge.</div></div>
            <div class="grammar-ex"><div class="zh">那条小路笔直地通向远方。</div><div class="en">That little path runs perfectly straight into the distance.</div></div>
          </div>
          <div class="grammar-block" style="margin-top:1.2em;">
            <div class="grammar-title" style="font-size:0.9em;">练一练 · 选择合适的词语填空：雪白 · 冰凉 · 笔直</div>
            <div class="grammar-examples">
              <div class="grammar-ex"><div class="zh">1. 夏天，____________的雪糕最受欢迎。</div></div>
              <div class="grammar-ex"><div class="zh">2. 那条____________的公路，她的车被笔直地停在公路当中。</div></div>
              <div class="grammar-ex"><div class="zh">3. 人们有自己的亲身经历，跟随他说____________。</div></div>
            </div>
          </div>
        </div>
      </div>
      <div class="grammar-panel">
        <div class="grammar-block">
          <div class="grammar-title"><span class="grammar-num">2</span>说A就A · Said and done — act on the spot / change without warning</div>
          <p class="grammar-desc">"说A就A"是常用口语结构，表示事情发生或动作进行得非常快、毫不犹豫，A是单音节或双音节动词或形容词，前后A相同。<br><span style="color:#888;font-size:0.85em;">A common spoken pattern. 说X就X means "say X and immediately X" — used either to commit to an action without hesitation or to describe something that changes/happens suddenly.</span></p>
          <div class="grammar-pattern">说 + A + 就 + A (A = verb/adjective, repeated)</div>
          <div class="grammar-examples">
            <div class="grammar-ex"><div class="zh">说干就干，索性这礼拜就开始。</div><div class="en">Said and done — I'd start this very week.</div></div>
            <div class="grammar-ex"><div class="zh">他遇到加意了的工作，一点儿也不犹豫，说辞就辞了。</div><div class="en">When he got tired of a job, he didn't hesitate — said quit and quit.</div></div>
            <div class="grammar-ex"><div class="zh">六月的天气说变就变，刚才还晴朗朗，现在就下大雨了。</div><div class="en">June weather changes on a dime — clear a moment ago, pouring now.</div></div>
          </div>
          <div class="grammar-block" style="margin-top:1.2em;">
            <div class="grammar-title" style="font-size:0.9em;">练一练 · 用"说A就A"改写句子</div>
            <div class="grammar-examples">
              <div class="grammar-ex"><div class="zh">1. 你看天上的乌云，马上就会下雨，不争分秒哪行！</div></div>
              <div class="grammar-ex"><div class="zh">2. 小孩儿就是这样，一会儿哭，一会儿笑。</div></div>
              <div class="grammar-ex"><div class="zh">3. 你快把句子再读一下吧，好得朋友相伴，形影不离。</div></div>
            </div>
          </div>
        </div>
      </div>
      <div class="grammar-panel">
        <div class="grammar-block">
          <div class="grammar-title"><span class="grammar-num">3</span>adj./v. + 得 + 要命 · X to death / extremely X</div>
          <p class="grammar-desc">"X得要命"表示程度极高。"要命"作补语，强调"X"到了让人难以忍受的地步。多用于口语，常带主观情绪色彩。<br><span style="color:#888;font-size:0.85em;">"得要命" attaches to an adjective or verb to express an extreme degree — "X to death", "extremely X". Spoken language, often subjective/emotional.</span></p>
          <div class="grammar-pattern">[adj./v.] + 得 + 要命</div>
          <div class="grammar-examples">
            <div class="grammar-ex"><div class="zh">五个小时没碰它，我心里虚得要命。</div><div class="en">Five hours without it, I felt extremely empty.</div></div>
            <div class="grammar-ex"><div class="zh">这个小时候紧得要命，又怕，又紧张，又有些心慌。</div><div class="en">That little while I was tense to death — scared, jittery, panicked.</div></div>
            <div class="grammar-ex"><div class="zh">他兴趣盎然，自从那次让她吃了一口苦，他害怕得要命。</div><div class="en">He was utterly fascinated; ever since she made him eat that bitter mouthful, he was scared to death.</div></div>
          </div>
          <div class="grammar-block" style="margin-top:1.2em;">
            <div class="grammar-title" style="font-size:0.9em;">练一练 · 用"adj./v.+得+要命"完成句子</div>
            <div class="grammar-examples">
              <div class="grammar-ex"><div class="zh">1. 他爸爸的脾气特别古怪，一点儿不顺心的事，____________________。</div></div>
              <div class="grammar-ex"><div class="zh">2. 可是孩子第一次离家，妈妈____________________，整晚睡不着。</div></div>
              <div class="grammar-ex"><div class="zh">3. 不知道你是怎么了，因为这点儿小事就____________________。</div></div>
            </div>
          </div>
        </div>
      </div>
      <div class="grammar-panel">
        <div class="grammar-block">
          <div class="grammar-title"><span class="grammar-num">4</span>索性 vs 干脆 · Both mean "might as well / straightforwardly"</div>
          <p class="grammar-desc">两者作副词时，用法基本相同，都表示直接、爽快地做出决定。<br><span style="color:#888;font-size:0.85em;">As adverbs, both express decisive, no-hesitation action. Subtle differences in tone and grammatical flexibility:</span></p>
          <div class="grammar-pattern">索性：作副词，"既然如此，就直接…"；带果断、放弃犹豫的语气<br>干脆：作副词或形容词；副词义同索性，但更口语化；形容词义为"直率、爽快"，可作谓语（这人很干脆）</div>
          <div class="grammar-examples">
            <div class="grammar-ex"><div class="zh">说干就干，索性这礼拜就开始。 / 干脆这礼拜就开始。</div><div class="en">Said and done — might as well start this week. (both work)</div></div>
            <div class="grammar-ex"><div class="zh">这人说话很干脆。 ✓ (索性 ✗)</div><div class="en">He speaks very straightforwardly. (only 干脆 can be an adjective)</div></div>
            <div class="grammar-ex"><div class="zh">索性把这件事彻底了结。</div><div class="en">Might as well settle this matter for good.</div></div>
          </div>
          <div class="grammar-block" style="margin-top:1.2em;">
            <div class="grammar-title" style="font-size:0.9em;">做一做 · Fill in 索性 or 干脆</div>
            <div class="grammar-examples">
              <div class="grammar-ex"><div class="zh">1. 这人说话办事非常__________，从不拖泥带水。（干脆）</div></div>
              <div class="grammar-ex"><div class="zh">2. 既然睡不着，他__________起来读起书来。（索性 / 干脆）</div></div>
              <div class="grammar-ex"><div class="zh">3. 他的回答很__________："不行，我不去！"（干脆）</div></div>
            </div>
          </div>
        </div>
      </div>
    </div><!-- end grammar tab -->

    <!-- 练习 -->
    <div data-tab="exercise" class="tab-panel">
      <div class="exercise-block">
        <div class="exercise-type">选择题 · Multiple Choice</div>
        <div class="exercise-q">1. 老板为什么在开会时发火？</div>
        <div class="exercise-choices">
          <div class="choice" onclick="selectChoice(this, false)"><span class="choice-label">A</span>员工迟到了</div>
          <div class="choice" onclick="selectChoice(this, true)"><span class="choice-label">B</span>员工开会时都在玩手机</div>
          <div class="choice" onclick="selectChoice(this, false)"><span class="choice-label">C</span>员工没完成业绩指标</div>
          <div class="choice" onclick="selectChoice(this, false)"><span class="choice-label">D</span>员工没穿正装</div>
        </div>
      </div>
      <div class="exercise-block">
        <div class="exercise-type">选择题 · Multiple Choice</div>
        <div class="exercise-q">2. "我"为什么把手机层层包好放进衣柜最里面？</div>
        <div class="exercise-choices">
          <div class="choice" onclick="selectChoice(this, false)"><span class="choice-label">A</span>怕手机被偷</div>
          <div class="choice" onclick="selectChoice(this, true)"><span class="choice-label">B</span>为了防止自己意志薄弱、忍不住去看</div>
          <div class="choice" onclick="selectChoice(this, false)"><span class="choice-label">C</span>因为手机坏了</div>
          <div class="choice" onclick="selectChoice(this, false)"><span class="choice-label">D</span>因为家里太乱</div>
        </div>
      </div>
      <div class="exercise-block">
        <div class="exercise-type">填空题 · Fill in the Blank</div>
        <div class="exercise-q">3. 从下面的词中选择合适的词填空：索性 · 庄重 · 兴高采烈 · 安宁 · 一举两得</div>
        <div style="font-size:0.88em;line-height:2;margin:8px 0 12px 0;">
          周末没有手机的干扰，我决定<input id="l9-fill1" type="text" placeholder="索性" style="padding:4px 8px;border:1.5px solid var(--mist);border-radius:6px;font-family:'Outfit',sans-serif;font-size:0.9rem;width:70px;outline:none;">把它收起来。我<input id="l9-fill2" type="text" placeholder="庄重" style="padding:4px 8px;border:1.5px solid var(--mist);border-radius:6px;font-family:'Outfit',sans-serif;font-size:0.9rem;width:70px;outline:none;">地把手机放进盒子里，然后去公园锻炼。在公园里我<input id="l9-fill3" type="text" placeholder="兴高采烈" style="padding:4px 8px;border:1.5px solid var(--mist);border-radius:6px;font-family:'Outfit',sans-serif;font-size:0.9rem;width:90px;outline:none;">地跳起了舞，既放松又锻炼，<input id="l9-fill4" type="text" placeholder="一举两得" style="padding:4px 8px;border:1.5px solid var(--mist);border-radius:6px;font-family:'Outfit',sans-serif;font-size:0.9rem;width:90px;outline:none;">。回到家，我享受到了从未有过的<input id="l9-fill5" type="text" placeholder="安宁" style="padding:4px 8px;border:1.5px solid var(--mist);border-radius:6px;font-family:'Outfit',sans-serif;font-size:0.9rem;width:70px;outline:none;">。
        </div>
        <div style="display:flex;gap:10px;flex-wrap:wrap;margin-top:4px;">
          <button class="check-btn" onclick="checkFill('l9-fill1','索性','l9-reveal1')">检查①</button>
          <button class="check-btn" onclick="checkFill('l9-fill2','庄重','l9-reveal2')">检查②</button>
          <button class="check-btn" onclick="checkFill('l9-fill3','兴高采烈','l9-reveal3')">检查③</button>
          <button class="check-btn" onclick="checkFill('l9-fill4','一举两得','l9-reveal4')">检查④</button>
          <button class="check-btn" onclick="checkFill('l9-fill5','安宁','l9-reveal5')">检查⑤</button>
        </div>
        <div id="l9-reveal1" style="display:none;margin-top:8px;padding:8px 12px;border-radius:8px;border:1.5px solid #b2dac9;font-size:0.88rem;">①参考答案：<strong>索性</strong></div>
        <div id="l9-reveal2" style="display:none;margin-top:4px;padding:8px 12px;border-radius:8px;border:1.5px solid #b2dac9;font-size:0.88rem;">②参考答案：<strong>庄重</strong></div>
        <div id="l9-reveal3" style="display:none;margin-top:4px;padding:8px 12px;border-radius:8px;border:1.5px solid #b2dac9;font-size:0.88rem;">③参考答案：<strong>兴高采烈</strong></div>
        <div id="l9-reveal4" style="display:none;margin-top:4px;padding:8px 12px;border-radius:8px;border:1.5px solid #b2dac9;font-size:0.88rem;">④参考答案：<strong>一举两得</strong></div>
        <div id="l9-reveal5" style="display:none;margin-top:4px;padding:8px 12px;border-radius:8px;border:1.5px solid #b2dac9;font-size:0.88rem;">⑤参考答案：<strong>安宁</strong></div>
      </div>
      <div class="exercise-block">
        <div class="exercise-type">写作题 · Writing</div>
        <div class="exercise-q">4. 有人说，手机、电脑等高科技产品已经控制了人们的生活，你是否像这篇课文所描述的那样成了它们的奴隶？要想改变这种状况，你有什么好的建议吗？请以"如何离开手机"为题，结合自己的实际写一篇不少于300字的文章。</div>
        <textarea style="width:100%;min-height:120px;padding:10px 14px;border:1.5px solid var(--mist);border-radius:8px;font-family:'Outfit',sans-serif;font-size:0.9rem;margin-top:10px;resize:vertical;" placeholder="在这里写你的短文…"></textarea>
      </div>
    </div><!-- end exercise tab -->

    <!-- 更多 -->
    <div data-tab="culture" class="tab-panel">
      <div class="culture-block">
        <div class="culture-head">
          <div class="culture-tag">🏮 词汇扩展</div>
          <button class="en-toggle" onclick="toggleEn(this)">En</button>
        </div>
        <div class="culture-title">熟悉下列词语的语素义<span class="pinyin">Morpheme expansion of L9 words</span></div>
        <div class="culture-zh">
          <table style="width:100%;border-collapse:collapse;font-size:0.88em;line-height:1.8;">
            <thead>
              <tr style="border-bottom:2px solid var(--mist);">
                <th style="text-align:left;padding:6px 10px;">核心词</th>
                <th style="text-align:left;padding:6px 10px;">语素义</th>
                <th style="text-align:left;padding:6px 10px;">扩展词</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom:1px solid var(--mist);"><td style="padding:6px 10px;">无知</td><td style="padding:6px 10px;">无 (没有) + 知</td><td style="padding:6px 10px;">无聊、无效、无所谓、无意</td></tr>
              <tr style="border-bottom:1px solid var(--mist);"><td style="padding:6px 10px;">破例</td><td style="padding:6px 10px;">破 (突破、撕除) + 例</td><td style="padding:6px 10px;">破坏、破产、突破、打破</td></tr>
              <tr style="border-bottom:1px solid var(--mist);"><td style="padding:6px 10px;">盛产</td><td style="padding:6px 10px;">盛 (兴盛) + 产</td><td style="padding:6px 10px;">盛行、盛况、盛会、丰盛</td></tr>
              <tr style="border-bottom:1px solid var(--mist);"><td style="padding:6px 10px;">额外</td><td style="padding:6px 10px;">额 (规定的数目) + 外</td><td style="padding:6px 10px;">名额、定额、限额、超额</td></tr>
              <tr style="border-bottom:1px solid var(--mist);"><td style="padding:6px 10px;">隐没</td><td style="padding:6px 10px;">隐 (隐藏) + 没</td><td style="padding:6px 10px;">隐瞒、隐居、隐患、隐私</td></tr>
              <tr style="border-bottom:1px solid var(--mist);"><td style="padding:6px 10px;">扩散</td><td style="padding:6px 10px;">扩 (扩大) + 散 (分散到各处)</td><td style="padding:6px 10px;">扩大、扩展、扩张、扩充</td></tr>
              <tr style="border-bottom:1px solid var(--mist);"><td style="padding:6px 10px;">登高</td><td style="padding:6px 10px;">登 (由低处到高处) + 高</td><td style="padding:6px 10px;">登山、登记、登场、刊登</td></tr>
              <tr style="border-bottom:1px solid var(--mist);"><td style="padding:6px 10px;">头绪</td><td style="padding:6px 10px;">头 (找不着头) + 绪</td><td style="padding:6px 10px;">情绪、思绪、就绪、千头万绪</td></tr>
              <tr style="border-bottom:1px solid var(--mist);"><td style="padding:6px 10px;">散布</td><td style="padding:6px 10px;">散 + 布 (分开、分散)</td><td style="padding:6px 10px;">散开、散发、散步、解散</td></tr>
              <tr style="border-bottom:1px solid var(--mist);"><td style="padding:6px 10px;">密封</td><td style="padding:6px 10px;">密 (事物之间距离近) + 封</td><td style="padding:6px 10px;">密切、密集、紧密、亲密</td></tr>
              <tr style="border-bottom:1px solid var(--mist);"><td style="padding:6px 10px;">密度</td><td style="padding:6px 10px;">密 + 度 (程度)</td><td style="padding:6px 10px;">浓度、湿度、温度、力度</td></tr>
              <tr><td style="padding:6px 10px;">凹地</td><td style="padding:6px 10px;">凹 (低洼的地方) + 地</td><td style="padding:6px 10px;">凹陷、凹凸、凹面、凸凹不平</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div><!-- end culture tab -->

  </div><!-- end content-area L9 -->
  </div><!-- end lesson-content data-lesson="9" -->'''

# ============================================================
# Perform replacement
# ============================================================
content = HTML.read_text(encoding='utf-8')

# Replace the L9 header
header_pattern = re.compile(
    r'<div class="lesson-header" id="lesson-header-9".*?</div>\s*<!--.*?-->\s*\n\s*<div class="lesson-content" data-lesson="9"',
    re.DOTALL
)

# More robust: replace header and content separately
# 1. Replace header block (from "lesson-header" id="lesson-header-9" up to closing div before lesson-content)
old_header_pattern = re.compile(
    r'  <div class="lesson-header" id="lesson-header-9".*?<p class="lesson-subtitle">.*?</p>\s*</div>',
    re.DOTALL
)
matches = old_header_pattern.findall(content)
assert len(matches) == 1, f"Expected 1 header match, got {len(matches)}"
content = old_header_pattern.sub(NEW_HEADER, content, count=1)

# 2. Replace lesson-content block (from `<div class="lesson-content" data-lesson="9"` to its closing comment)
old_content_pattern = re.compile(
    r'  <div class="lesson-content" data-lesson="9".*?</div><!-- end lesson-content data-lesson="9" -->',
    re.DOTALL
)
matches = old_content_pattern.findall(content)
assert len(matches) == 1, f"Expected 1 content match, got {len(matches)}"
content = old_content_pattern.sub(NEW_CONTENT, content, count=1)

HTML.write_text(content, encoding='utf-8')
print(f'L9 replaced. New file size: {len(content):,} bytes')
print(f'Vocab words: {len(VOCAB)}')
