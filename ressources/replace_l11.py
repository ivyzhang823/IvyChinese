"""Replace the L11 stub in hsk6_11-20.html with real content from 我不在时，猫在干什么."""
import re
from pathlib import Path

HTML = Path('D:/Claude_CODE/IvyChinese/HSK/HSK6/hsk6_11-20.html')

# ============================================================
# NEW L11 HEADER
# ============================================================
NEW_HEADER = '''  <div class="lesson-header" id="lesson-header-11" data-lesson="11" data-watermark="十一" style="display:none">
    <div class="lesson-meta">
      <button class="lesson-tag" onclick="showIndex()">
        <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"/></svg>
        HSK 6
      </button>
      <span class="lesson-tag-num">第十一课 · Lesson 11</span>
    </div>
    <h1>我不在时，猫在干什么</h1>
    <p style="font-size:0.9rem;color:var(--gold);margin-bottom:0.3rem;letter-spacing:0.02em;">Wǒ bú zài shí, māo zài gàn shénme</p>
    <p class="lesson-subtitle">What do the cats do when I'm not home</p>
  </div>'''

# ============================================================
# Vocabulary (46 words from textbook pages 105-107)
# ============================================================
VOCAB = [
    ("流浪", "liúlàng", "v.", "to roam about, to lead a vagrant life", "大黄原本是只<em>流浪</em>猫。", "Big Yellow was originally a stray."),
    ("淋", "lín", "v.", "to drench, to be drenched (by rain)", "<em>淋</em>着大雨来找小奇拜访。", "Drenched by the rain, it came to visit Xiaoqi."),
    ("拜访", "bàifǎng", "v.", "to pay a visit, to call on", "来找小奇<em>拜访</em>。", "Came to call on Xiaoqi."),
    ("见多识广", "jiànduō-shíguǎng", "idiom", "experienced and knowledgeable", "<em>见多识广</em>的大黄虽有流浪史。", "Big Yellow, experienced and worldly, despite its vagrant past."),
    ("教养", "jiàoyǎng", "n.", "breeding, education, manners", "很有<em>教养</em>。", "Very well-mannered."),
    ("懒惰", "lǎnduò", "adj.", "lazy, indolent", "它既不<em>懒惰</em>，也不嘴馋。", "It is neither lazy nor greedy."),
    ("馋", "chán", "adj.", "greedy, gluttonous", "它既不懒惰，也不<em>馋</em>。", "It is neither lazy nor greedy."),
    ("趴", "pā", "v.", "to lie prone, to lie on one's stomach", "天天<em>趴</em>在窗台上晒太阳。", "Every day it lies on the windowsill basking in the sun."),
    ("知足常乐", "zhīzú chánglè", "idiom", "happiness consists in contentment", "一副<em>知足常乐</em>的样子。", "Wearing an expression of contented ease."),
    ("恭敬", "gōngjìng", "adj.", "respectful, deferential", "<em>恭敬</em>地迎接小奇。", "Respectfully greets Xiaoqi."),
    ("君子", "jūnzǐ", "n.", "gentleman, virtuous person", "不失<em>君子</em>风度。", "Never losing its gentlemanly bearing."),
    ("嗅觉", "xiùjué", "n.", "sense of smell, olfaction", "<em>嗅觉</em>灵敏。", "A keen sense of smell."),
    ("灵敏", "língmǐn", "adj.", "sensitive, keen, acute", "嗅觉<em>灵敏</em>。", "Has a keen sense of smell."),
    ("敏捷", "mǐnjié", "adj.", "quick, agile, nimble", "动作<em>敏捷</em>。", "Nimble in its movements."),
    ("快活", "kuàihuó", "adj.", "happy, merry, cheerful", "<em>快活</em>而不耐寂寞。", "Cheerful but cannot stand loneliness."),
    ("扑", "pū", "v.", "to pounce on, to throw oneself on", "每件东西都<em>扑</em>一遍。", "Pounces on every single item."),
    ("亲热", "qīnrè", "adj.", "loving, affectionate, warm", "对小奇特别<em>亲热</em>。", "Especially affectionate toward Xiaoqi."),
    ("统统", "tǒngtǒng", "adv.", "all, completely, every single one", "每件东西都<em>统统</em>扑一遍。", "Pounces on every single item without exception."),
    ("迷人", "mírén", "adj.", "charming, enchanting, fascinating", "喜儿是个<em>迷人</em>的女孩儿。", "Xi'er is an enchanting little girl."),
    ("模范", "mófàn", "adj./n.", "model, exemplary", "钱小奇是个<em>模范</em>饲养员。", "Qian Xiaoqi is a model pet-keeper."),
    ("饲养", "sìyǎng", "v.", "to raise, to keep, to breed", "<em>饲养</em>员。", "A keeper / breeder."),
    ("清洁", "qīngjié", "v.", "to clean", "<em>清洁</em>猫窝。", "Clean the cats' nests."),
    ("喂", "wèi", "v.", "to feed", "<em>喂</em>水、<em>喂</em>饭。", "Feed water and food."),
    ("繁忙", "fánmáng", "adj.", "busy, bustling", "他虽然工作<em>繁忙</em>。", "Although his work is busy."),
    ("急切", "jíqiè", "adj.", "eager, impatient, anxious", "最<em>急切</em>的事情就是回家。", "The most eagerly anticipated thing is going home."),
    ("例外", "lìwài", "n.", "exception", "每天毫无<em>例外</em>。", "Every single day without exception."),
    ("凝视", "níngshì", "v.", "to gaze fixedly, to stare", "<em>凝视</em>着深沉的热情。", "Gazing with deep affection."),
    ("深沉", "shēnchén", "adj.", "deep, profound", "<em>深沉</em>的热情。", "Deep affection."),
    ("监视", "jiānshì", "v.", "to monitor, to keep watch on", "<em>监视</em>猫的一举一动。", "Monitor every move the cats make."),
    ("动态", "dòngtài", "n.", "movement, activity, behavior", "时刻保持其的<em>动态</em>。", "Constantly track their behavior."),
    ("缺陷", "quēxiàn", "n.", "defect, flaw, drawback", "摄像头有局限<em>缺陷</em>。", "The fixed cameras have a flaw."),
    ("镜头", "jìngtóu", "n.", "camera lens, scene, shot", "拍下的<em>镜头</em>都是空的。", "The shots captured were all empty."),
    ("自力更生", "zìlì-gēngshēng", "idiom", "to rely on one's own efforts", "决定<em>自力更生</em>。", "Decided to rely on his own efforts."),
    ("尖端", "jiānduān", "adj.", "most advanced, cutting-edge", "购买了一套<em>尖端</em>设备。", "Bought a set of cutting-edge equipment."),
    ("钻研", "zuānyán", "v.", "to study intensively, to dig deeply into", "<em>钻研</em>几个月。", "Studied intensively for several months."),
    ("动作", "dòngzuò", "n.", "action, movement", "猫的<em>动作</em>很有规律。", "The cats' movements are quite regular."),
    ("储存", "chúcún", "v.", "to store, to stockpile", "<em>储存</em>图像数据。", "Store the image data."),
    ("遥控", "yáokòng", "v.", "to remotely control", "远程实时<em>遥控</em>。", "Remote real-time control."),
    ("即时", "jíshí", "adv.", "immediately, on the spot", "<em>即时</em>发送给他的姐姐。", "Immediately send to his sister."),
    ("操纵", "cāozòng", "v.", "to operate, to control", "<em>操纵</em>设备。", "Operate the equipment."),
    ("跟踪", "gēnzōng", "v.", "to follow the tracks of, to track", "对猫进行<em>跟踪</em>。", "Track the cats."),
    ("角落", "jiǎoluò", "n.", "corner, nook", "到家里的任何一个<em>角落</em>。", "To any corner of the house."),
    ("误差", "wùchā", "n.", "error, deviation", "时间<em>误差</em>平均不到5分钟。", "Average time deviation under 5 minutes."),
    ("踪迹", "zōngjì", "n.", "trace, trail, track", "解答了所迷的<em>踪迹</em>。", "Solved the mystery of their tracks."),
    ("动静", "dòngjing", "n.", "sound of activity, movement", "看到家里的<em>动静</em>。", "See the activity going on at home."),
    ("操作", "cāozuò", "v.", "to operate, to manipulate", "<em>操作</em>这套系统。", "Operate this system."),
]

def fc_card(zh, py, pos, en):
    return f'<div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">{zh}</div><div class="fcs-pos">{pos}</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">{py}</div><div class="fcs-en">{en}</div></div></div></div>'

def vocab_card(zh, py, pos, en, ex_zh, ex_en):
    return f'<div class="vocab-card"><div class="vocab-zh">{zh}</div><div class="vocab-pinyin">{py}</div><div class="vocab-pos">{pos}</div><div class="vocab-en">{en}</div><div class="vocab-example">{ex_zh}<br><span style="color:#bbb">{ex_en}</span></div></div>'

fc_cards = []
for i, (zh, py, pos, en, _, _) in enumerate(VOCAB):
    card = fc_card(zh, py, pos, en)
    if i == 0:
        card = card.replace('class="fc-card"', 'class="fc-card active"', 1)
    fc_cards.append('            ' + card)
fc_cards_html = '\n'.join(fc_cards)

vocab_cards_html = '\n        '.join(vocab_card(*v) for v in VOCAB)

NEW_CONTENT = f'''  <div class="lesson-content" data-lesson="11" style="display:none">
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
      <div class="dialogue-block" id="l11-block1">
        <div class="dialogue-header">
          <div class="dialogue-title-wrap">
            <div class="dialogue-title-row">
              <span class="dialogue-title">课文 · 我不在时，猫在干什么</span>
              <button class="dh-play-btn" id="l11-dhBtn1" onclick="dhPlay('l11-audioEl1','l11-dhBtn1')">
                <svg id="l11-dhIcon1" viewBox="0 0 24 24"><polygon points="5 3 19 12 5 21 5 3"/></svg>
              </button>
              <span style="flex:1;"></span>
              <div class="toggle-btns">
                <button class="toggle-btn" onclick="toggleBlock(this,'pinyin','l11-block1')"><span class="dot"></span>拼音</button>
                <button class="toggle-btn" onclick="toggleBlock(this,'en','l11-block1')"><span class="dot"></span>En</button>
              </div>
            </div>
            <span class="dialogue-title-en">What do the cats do when I'm not home</span>
          </div>
          <audio id="l11-audioEl1" src="" onended="dhEnded('l11-audioEl1','l11-dhBtn1','l11-dhIcon1')" ontimeupdate="dhUpdate('l11-audioEl1')"></audio>
        </div>
        <div class="dialogue-line" style="display:block;">
          <div class="line-content" style="font-size:0.88em;">
            <div class="line-zh" style="line-height:1.9;">
              <p style="margin:0 0 0.15em 0;">钱小奇养了3只猫。大黄原本是只流浪猫，那天，淋着大雨来到钱小奇家拜访，见完小奇就不走了。见多识广的大黄虽有流浪史，却很有教养，它既不懒惰，也不嘴馋，天天趴在窗台上晒太阳，一副知足常乐的样子。每次钱小奇出门回来，它都恭敬地起立迎接小奇，不失君子风度。白白是个聪明的小猫，嗅觉灵敏，动作敏捷，快活而不耐寂寞。每次钱小奇和他带回来的东西它都统统扑一遍。喜儿是个人人皆爱的迷人女孩儿，每天大部分时间都在整理自己的毛发，把自己梳理得漂漂亮亮。</p>
              <p class="line-pinyin" style="margin:0 0 1.1em 0;display:none;">Qián Xiǎoqí yǎng le 3 zhī māo. Dàhuáng yuánběn shì zhī liúlàng māo, nà tiān, lín zhe dàyǔ lái dào Qián Xiǎoqí jiā bàifǎng, jiàn wán Xiǎoqí jiù bù zǒu le. Jiànduō-shíguǎng de Dàhuáng suī yǒu liúlàng shǐ, què hěn yǒu jiàoyǎng, tā jì bù lǎnduò, yě bù zuǐ chán, tiāntiān pā zài chuāngtái shàng shài tàiyáng, yī fù zhīzú-chánglè de yàngzi. Měi cì Qián Xiǎoqí chūmén huílái, tā dōu gōngjìng de qǐlì yíngjiē Xiǎoqí, bù shī jūnzǐ fēngdù. Báibái shì gè cōngmíng de xiǎo māo, xiùjué língmǐn, dòngzuò mǐnjié, kuàihuó ér bù nài jìmò. Měi cì Qián Xiǎoqí hé tā dài huílai de dōngxi tā dōu tǒngtǒng pū yī biàn. Xǐ'ér shì gè rénrén jiē ài de mírén nǚháir, měi tiān dàbùfèn shíjiān dōu zài zhěnglǐ zìjǐ de máofà, bǎ zìjǐ shūlǐ de piàopiào-liàngliàng.</p>
              <p style="margin:0 0 0.15em 0;">钱小奇是个模范饲养员，每天早起第一件事就是清洁猫窝，喂水、喂饭。他虽然工作繁忙，但每天最急切的事情就是回家了，他刚一到家——大黄和白白在门口等候，每天毫无例外地凝视着他深沉的热情。</p>
              <p class="line-pinyin" style="margin:0 0 1.1em 0;display:none;">Qián Xiǎoqí shì gè mófàn sìyǎng yuán, měi tiān zǎo qǐ dì yī jiàn shì jiùshì qīngjié māo wō, wèi shuǐ, wèi fàn. Tā suīrán gōngzuò fánmáng, dàn měi tiān zuì jíqiè de shìqíng jiùshì huí jiā le, tā gāng yī dào jiā — Dàhuáng hé Báibái zài ménkǒu děnghòu, měi tiān háo wú lìwài de níngshì zhe tā shēnchén de rèqíng.</p>
              <p style="margin:0 0 0.15em 0;">钱小奇很好奇，自己不在家时猫都在做什么？多无聊啊，会不会做坏事？为了弄清楚他在家里安了三个监视摄像头，监视猫的一举一动。很快，他发现这个不能移动的摄像头有局限缺陷，拍下的镜头都是空的，于是他增加了设备，并决定自力更生，购买了一套尖端设备。他这样钻研工业，挂上几个月的努力，安装的设备能够时刻保持其的动态进行下到图像，钱小奇在外可以远程实时遥控的监视摄像头。对家里的猫进行跟踪、移动摄像头，跟随到家里的任何一个角落。</p>
              <p class="line-pinyin" style="margin:0 0 1.1em 0;display:none;">Qián Xiǎoqí hěn hàoqí, zìjǐ bú zài jiā shí māo dōu zài zuò shénme? Duō wúliáo a, huì bú huì zuò huài shì? Wèi le nòng qīngchu tā zài jiā lǐ ān le sān gè jiānshì shèxiàngtóu, jiānshì māo de yī jǔ yī dòng. Hěn kuài, tā fāxiàn zhège bù néng yídòng de shèxiàngtóu yǒu júxiàn quēxiàn, pāi xià de jìngtóu dōu shì kōng de, yúshì tā zēngjiā le shèbèi, bìng juédìng zìlì-gēngshēng, gòumǎi le yī tào jiānduān shèbèi. Tā zhèyàng zuānyán gōngyè, guàshàng jǐ gè yuè de nǔlì, ānzhuāng de shèbèi nénggòu shíkè bǎochí qí de dòngtài jìnxíng xià dào túxiàng, Qián Xiǎoqí zài wài kěyǐ yuǎnchéng shíshí yáokòng de jiānshì shèxiàngtóu. Duì jiā lǐ de māo jìnxíng gēnzōng, yídòng shèxiàngtóu, gēnsuí dào jiā lǐ de rènhé yī gè jiǎoluò.</p>
              <p style="margin:0 0 0.15em 0;">通过对大量数据和图片进行分析，钱小奇发现，这三只猫大多数时间都在睡觉。除了睡觉，猫的行动很有规律，每天有一个小时左右就站在门口，时间误差是平均不到5分钟。更有趣的是，每天回家时，门口的大黄和白白并不是真的在门口等他，而是在屋里某下喵呼叫，听到主人的脚步声和钥匙的声音，才会跑出门口来。</p>
              <p class="line-pinyin" style="margin:0 0 1.1em 0;display:none;">Tōngguò duì dàliàng shùjù hé túpiàn jìnxíng fēnxī, Qián Xiǎoqí fāxiàn, zhè sān zhī māo dà duōshù shíjiān dōu zài shuìjiào. Chú le shuìjiào, māo de xíngdòng hěn yǒu guīlǜ, měi tiān yǒu yī gè xiǎoshí zuǒyòu jiù zhàn zài ménkǒu, shíjiān wùchā shì píngjūn bú dào 5 fēnzhōng. Gèng yǒuqù de shì, měi tiān huí jiā shí, ménkǒu de Dàhuáng hé Báibái bìng bú shì zhēn de zài ménkǒu děng tā, érshì zài wū lǐ mǒu xià miāo hūjiào, tīng dào zhǔrén de jiǎobù shēng hé yàoshi de shēngyīn, cái huì pǎo chū ménkǒu lái.</p>
              <p style="margin:0 0 0.15em 0;">这套系统终于解答了钱小奇所迷的踪迹，他从办公室里上网就能看到家里的动静，找到了在家午老菜的钱包。能根据图像记录下来，并把拍下的照片即时附给他的姐姐看"耀眼"。这是一套多么实用的远程跟踪安全机系统呵。</p>
              <p class="line-pinyin" style="margin:0 0 1.1em 0;display:none;">Zhè tào xìtǒng zhōngyú jiědá le Qián Xiǎoqí suǒ mí de zōngjì, tā cóng bàngōngshì lǐ shàng wǎng jiù néng kàn dào jiā lǐ de dòngjing, zhǎo dào le zài jiā wǔ lǎo cài de qiánbāo. Néng gēnjù túxiàng jìlù xiàlái, bìng bǎ pāi xià de zhàopiàn jíshí fù gěi tā de jiějiě kàn "yàoyǎn". Zhè shì yī tào duōme shíyòng de yuǎnchéng gēnzōng ānquán jī xìtǒng a.</p>
            </div>
            <div class="line-en" style="margin-top:1.5em;padding-top:1em;border-top:1px solid var(--mist);display:none;">Qian Xiaoqi keeps three cats. Big Yellow had originally been a stray; one day, drenched by a downpour, it showed up at Xiaoqi's door, paid him a visit, and never left. For all its time on the road, Big Yellow is worldly yet well-mannered — neither lazy nor greedy. It spends its days lying on the windowsill in the sun, wearing a contented look. Every time Xiaoqi comes home, it rises respectfully to greet him, never losing its gentlemanly bearing. Little White is a clever cat — keen-nosed, nimble, cheerful but unable to bear loneliness. Whenever Xiaoqi or anything he brings home appears, White pounces on every item without exception. Xi'er is a charming little girl loved by all, who spends most of her day grooming her own fur until she shines.<br><br>Xiaoqi is a model pet-keeper: the first thing every morning is to clean the cats' nests and put out food and water. Busy as his job is, the thing he looks forward to most each day is going home. The moment he steps in — Big Yellow and Little White are at the door waiting, gazing up at him with unfailing, deep affection.<br><br>Xiaoqi grew curious: what do the cats actually do while he's away? Aren't they bored? Do they get up to mischief? To find out, he installed three surveillance cameras at home to monitor every move they made. He soon discovered that fixed cameras had their limits — many of the recorded shots were empty. So he upgraded the gear and decided to do it himself, buying a set of cutting-edge equipment. After months of intensive study and installation, his setup could continuously track the cats' movements and feed back live images; from outside, Xiaoqi could now remotely steer the cameras to follow the cats into every corner of the house.<br><br>Through analyzing piles of data and images, Xiaoqi found that the three cats spent most of their time asleep. Beyond sleep, their routine was remarkably regular: every day, for about an hour, they would stand by the front door — with an average deviation of under five minutes from the same moment. More intriguing still: when Xiaoqi came home, Big Yellow and Little White weren't actually waiting at the door — they were meowing from somewhere deep inside the house, and only sprang out to the door when they heard his footsteps and the sound of his keys.<br><br>The system finally solved the mystery of his cats' daily lives. From the office, he can now go online and watch what's happening at home — and he has even tracked down a wallet left tucked away among the noon leftovers. The setup records images of everything, and he can immediately send the snapshots to his sister to admire. What a wonderfully practical remote tracking and security system it has turned out to be!</div>
          </div>
        </div>
      </div>
    </div><!-- end 课文 tab -->

    <!-- 生词表 -->
    <div data-tab="vocab" class="tab-panel">
      <div class="fc-slider-wrap">
        <div class="fc-row">
          <div class="fc-slider" id="l11-fcSlider">
{fc_cards_html}
          </div>
        </div>
        <div style="display:flex;align-items:center;gap:10px;margin-top:10px;">
          <button class="fc-arrow" onclick="fcNav(-1)"><svg viewBox="0 0 24 24"><polyline points="15 18 9 12 15 6"/></svg></button>
          <span class="fc-counter" id="l11-fcCounter" style="min-width:36px;text-align:center;line-height:1;">1 / {len(VOCAB)}</span>
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
        <div class="vocab-zh">见多识广</div><div class="vocab-pinyin">jiànduō-shíguǎng</div><div class="vocab-pos">idiom</div>
        <div class="vocab-en">experienced and knowledgeable; well-traveled and broadly informed (lit. "having seen much and known widely") — describes someone or something with rich life experience</div>
        <div class="vocab-example">
          <em>见多识广</em>的大黄虽有流浪史。<br>
          <span style="color:#bbb">Big Yellow, worldly and well-informed despite its vagrant past.</span><br>
          老人家<em>见多识广</em>，问问他准没错。<br>
          <span style="color:#bbb">The elder is worldly and well-informed — asking him is always a safe bet.</span>
        </div>
      </div>
      <div class="vocab-card">
        <div class="vocab-zh">知足常乐</div><div class="vocab-pinyin">zhīzú chánglè</div><div class="vocab-pos">idiom</div>
        <div class="vocab-en">happiness consists in contentment; the contented are always happy (lit. "knowing-enough, always-joyful") — Taoist-flavored proverb on inner contentment</div>
        <div class="vocab-example">
          一副<em>知足常乐</em>的样子。<br>
          <span style="color:#bbb">Wearing an air of contented ease.</span><br>
          他生活简单，<em>知足常乐</em>。<br>
          <span style="color:#bbb">He lives simply and finds joy in contentment.</span>
        </div>
      </div>
      <div class="vocab-card">
        <div class="vocab-zh">自力更生</div><div class="vocab-pinyin">zìlì-gēngshēng</div><div class="vocab-pos">idiom</div>
        <div class="vocab-en">to rely on one's own efforts; to be self-reliant (lit. "use your own strength to renew yourself") — emphasizes independence and self-sufficiency</div>
        <div class="vocab-example">
          决定<em>自力更生</em>，购买了一套尖端设备。<br>
          <span style="color:#bbb">He decided to rely on himself and bought cutting-edge equipment.</span><br>
          公司初创时期，员工们<em>自力更生</em>，克服了许多困难。<br>
          <span style="color:#bbb">In the startup phase, the staff relied on their own efforts to overcome many difficulties.</span>
        </div>
      </div>
      <div class="vocab-card">
        <div class="vocab-zh">统统</div><div class="vocab-pinyin">tǒngtǒng</div><div class="vocab-pos">adv.</div>
        <div class="vocab-en">all, completely, every single one without exception — adverb covering all elements of a set; stronger and more emphatic than 都</div>
        <div class="vocab-example">
          每件东西都<em>统统</em>扑一遍。<br>
          <span style="color:#bbb">Pounces on every single item without exception.</span><br>
          这些东西他<em>统统</em>不要了。<br>
          <span style="color:#bbb">He doesn't want any of these things — every single one.</span>
        </div>
      </div>
    </div><!-- end worddetail tab -->

    <!-- 语法 -->
    <div data-tab="grammar" class="tab-panel">
      <div class="grammar-switcher">
        <button class="grammar-switch-btn active" onclick="switchGrammar(0, this)">统统</button>
        <button class="grammar-switch-btn" onclick="switchGrammar(1, this)">以…为…</button>
        <button class="grammar-switch-btn" onclick="switchGrammar(2, this)">该不该VO</button>
        <button class="grammar-switch-btn" onclick="switchGrammar(3, this)">急切 vs 急忙</button>
      </div>
      <div class="grammar-panel active">
        <div class="grammar-block">
          <div class="grammar-title"><span class="grammar-num">1</span>统统 · "All, every single one without exception"</div>
          <p class="grammar-desc">"统统"，副词，表示行为涉及全部对象，意思是"毫无例外地、一个不剩地"。多用于口语。也可以说"通通"。<br><span style="color:#888;font-size:0.85em;">"统统" is an adverb meaning "all" or "every single one without exception". Stronger than 都, it emphasizes that no item in a set is left out. Mostly spoken.</span></p>
          <div class="grammar-pattern">[Subject/object set] + 统统 + [verb/action]</div>
          <div class="grammar-examples">
            <div class="grammar-ex"><div class="zh">每次小奇和他带回来的东西它都统统扑一遍。</div><div class="en">Every time Xiaoqi brings something home, the cat pounces on every single item.</div></div>
            <div class="grammar-ex"><div class="zh">钱小奇一回家，三只猫统统跑出来迎接他。</div><div class="en">The moment Xiaoqi gets home, all three cats come running to greet him.</div></div>
            <div class="grammar-ex"><div class="zh">这些旧书我统统不要了，你拿去吧。</div><div class="en">I don't want any of these old books — take them all.</div></div>
          </div>
          <div class="grammar-block" style="margin-top:1.2em;">
            <div class="grammar-title" style="font-size:0.9em;">练一练 · 用"统统"改写句子</div>
            <div class="grammar-examples">
              <div class="grammar-ex"><div class="zh">1. 这周末我把家里的衣服都洗了一遍。</div></div>
              <div class="grammar-ex"><div class="zh">2. 今天来开会的人，每个都要签到。</div></div>
              <div class="grammar-ex"><div class="zh">3. 他把昨天买的水果都吃了。</div></div>
            </div>
          </div>
        </div>
      </div>
      <div class="grammar-panel">
        <div class="grammar-block">
          <div class="grammar-title"><span class="grammar-num">2</span>以…为… · "Take X as Y" — formal substitution pattern</div>
          <p class="grammar-desc">"以…为…"是书面语表达，相当于口语的"把…作为…"或"用…当作…"。两个"以…为…"连用时，第二个"以"可省略。<br><span style="color:#888;font-size:0.85em;">"以…为…" is a written-register pattern equivalent to "把…当作…" or "把…作为…". When two such phrases are coordinated, the second 以 can be dropped.</span></p>
          <div class="grammar-pattern">以 + X + 为 + Y  =  把 X 当作/作为 Y</div>
          <div class="grammar-examples">
            <div class="grammar-ex"><div class="zh">钱小奇以猫为家庭成员，处处考虑它们的需要。</div><div class="en">Qian Xiaoqi treats his cats as family members, considering their needs in every way.</div></div>
            <div class="grammar-ex"><div class="zh">中国饮食文化以国产食材为基本原料，同时合理引进外来食材。</div><div class="en">Chinese cuisine takes local produce as its basic ingredients while reasonably introducing foreign ones.</div></div>
            <div class="grammar-ex"><div class="zh">他以学习为乐趣，从来不觉得辛苦。</div><div class="en">He takes learning as a joy and never finds it hard.</div></div>
          </div>
          <div class="grammar-block" style="margin-top:1.2em;">
            <div class="grammar-title" style="font-size:0.9em;">练一练 · 用"以…为…"改写句子</div>
            <div class="grammar-examples">
              <div class="grammar-ex"><div class="zh">1. 他把工作当作人生的一部分。</div></div>
              <div class="grammar-ex"><div class="zh">2. 这部小说把农村生活作为题材。</div></div>
              <div class="grammar-ex"><div class="zh">3. 教育学是一门科学，它把研究对象定为教育。</div></div>
            </div>
          </div>
        </div>
      </div>
      <div class="grammar-panel">
        <div class="grammar-block">
          <div class="grammar-title"><span class="grammar-num">3</span>该VO不该VO · "Whether to V or not" — alternative-question pattern</div>
          <p class="grammar-desc">"该VO不该VO"是由"该VO（还是）做VO"省略而来，用于口语，表示一切都按你的标准而进行，往往含有体谅、信任或听从对方的语气。整个口语格式之后可以加"啊"等表示语气的助词。<br><span style="color:#888;font-size:0.85em;">"该VO不该VO" is a spoken alternative-question structure expressing "whether to do V or not", often with a tone of deference or leaving the decision to the listener. Modal particles like 啊 can follow.</span></p>
          <div class="grammar-pattern">该 + V + O + 不该 + V + O  /  该 + V + O + 还是 + 做VO</div>
          <div class="grammar-examples">
            <div class="grammar-ex"><div class="zh">该不该养猫，你自己决定吧。</div><div class="en">Whether to keep a cat or not — you decide.</div></div>
            <div class="grammar-ex"><div class="zh">这件事该不该做，咱们先讨论一下。</div><div class="en">Whether to do this thing or not — let's discuss it first.</div></div>
            <div class="grammar-ex"><div class="zh">你说，这种话该不该说啊？</div><div class="en">Tell me — should this kind of thing be said or not?</div></div>
          </div>
          <div class="grammar-block" style="margin-top:1.2em;">
            <div class="grammar-title" style="font-size:0.9em;">练一练 · 用"该VOVO"或省略形式改写句子</div>
            <div class="grammar-examples">
              <div class="grammar-ex"><div class="zh">1. 到底是走还是留下来呢？</div></div>
              <div class="grammar-ex"><div class="zh">2. 不管是好年代还是坏年代，人们到了一定年龄就会成熟。</div></div>
              <div class="grammar-ex"><div class="zh">3. 这件事情让他难以决定，他整天都琢磨。</div></div>
            </div>
          </div>
        </div>
      </div>
      <div class="grammar-panel">
        <div class="grammar-block">
          <div class="grammar-title"><span class="grammar-num">4</span>急切 vs 急忙 · "Eager / impatient" vs "in a hurry"</div>
          <p class="grammar-desc">两者都表示着急，但词性、用法和侧重点不同。<br><span style="color:#888;font-size:0.85em;">Both express urgency, but differ in part of speech and nuance:</span></p>
          <div class="grammar-pattern">急切：形容词；表示内心情急、迫切，多用于书面；可作谓语或定语<br>急忙：副词；表示行动迅速急促；只能作状语，修饰动词</div>
          <div class="grammar-examples">
            <div class="grammar-ex"><div class="zh">他每天最急切的事情就是回家。 ✓ (急切作定语，修饰"事情")</div><div class="en">The most eagerly anticipated thing each day is going home.</div></div>
            <div class="grammar-ex"><div class="zh">他听到铃声，急忙跑出去开门。 ✓ (急忙作状语，修饰"跑")</div><div class="en">Hearing the bell, he hurriedly ran to open the door.</div></div>
            <div class="grammar-ex"><div class="zh">大家急切地等待结果。 ✓ / 大家急忙地等待结果。 ✗</div><div class="en">Everyone is eagerly awaiting the result. (only 急切 works here — 等待 is not a quick action)</div></div>
          </div>
          <div class="grammar-block" style="margin-top:1.2em;">
            <div class="grammar-title" style="font-size:0.9em;">做一做 · Fill in 急切 or 急忙</div>
            <div class="grammar-examples">
              <div class="grammar-ex"><div class="zh">1. 一听说儿子病了，大夫__________检查。（急忙）</div></div>
              <div class="grammar-ex"><div class="zh">2. 妈妈__________地望着医院手术室的灯。（急切）</div></div>
              <div class="grammar-ex"><div class="zh">3. 一接到电话他__________出门，连饭都没吃。（急忙）</div></div>
            </div>
          </div>
        </div>
      </div>
    </div><!-- end grammar tab -->

    <!-- 练习 -->
    <div data-tab="exercise" class="tab-panel">
      <div class="exercise-block">
        <div class="exercise-type">选择题 · Multiple Choice</div>
        <div class="exercise-q">1. 钱小奇为什么要在家里安装监视摄像头？</div>
        <div class="exercise-choices">
          <div class="choice" onclick="selectChoice(this, false)"><span class="choice-label">A</span>担心家里被盗</div>
          <div class="choice" onclick="selectChoice(this, true)"><span class="choice-label">B</span>想知道自己不在家时猫在做什么</div>
          <div class="choice" onclick="selectChoice(this, false)"><span class="choice-label">C</span>记录猫的可爱瞬间</div>
          <div class="choice" onclick="selectChoice(this, false)"><span class="choice-label">D</span>训练猫的行为</div>
        </div>
      </div>
      <div class="exercise-block">
        <div class="exercise-type">选择题 · Multiple Choice</div>
        <div class="exercise-q">2. 关于大黄，下列说法正确的是：</div>
        <div class="exercise-choices">
          <div class="choice" onclick="selectChoice(this, false)"><span class="choice-label">A</span>从小被钱小奇收养</div>
          <div class="choice" onclick="selectChoice(this, false)"><span class="choice-label">B</span>非常懒惰</div>
          <div class="choice" onclick="selectChoice(this, true)"><span class="choice-label">C</span>原本是流浪猫，见多识广却很有教养</div>
          <div class="choice" onclick="selectChoice(this, false)"><span class="choice-label">D</span>嗅觉最灵敏</div>
        </div>
      </div>
      <div class="exercise-block">
        <div class="exercise-type">填空题 · Fill in the Blank</div>
        <div class="exercise-q">3. 从下面的词中选择合适的词填空：流浪 · 拜访 · 教养 · 急切 · 监视</div>
        <div style="font-size:0.88em;line-height:2;margin:8px 0 12px 0;">
          那只猫原本是一只<input id="l11-fill1" type="text" placeholder="流浪" style="padding:4px 8px;border:1.5px solid var(--mist);border-radius:6px;font-family:'Outfit',sans-serif;font-size:0.9rem;width:70px;outline:none;">猫，一天到我家<input id="l11-fill2" type="text" placeholder="拜访" style="padding:4px 8px;border:1.5px solid var(--mist);border-radius:6px;font-family:'Outfit',sans-serif;font-size:0.9rem;width:70px;outline:none;">就再也不肯走了。它虽然出身贫寒，却很有<input id="l11-fill3" type="text" placeholder="教养" style="padding:4px 8px;border:1.5px solid var(--mist);border-radius:6px;font-family:'Outfit',sans-serif;font-size:0.9rem;width:70px;outline:none;">。每天我下班回家时它都<input id="l11-fill4" type="text" placeholder="急切" style="padding:4px 8px;border:1.5px solid var(--mist);border-radius:6px;font-family:'Outfit',sans-serif;font-size:0.9rem;width:70px;outline:none;">地等在门口。为了了解它的生活，我装了一个摄像头<input id="l11-fill5" type="text" placeholder="监视" style="padding:4px 8px;border:1.5px solid var(--mist);border-radius:6px;font-family:'Outfit',sans-serif;font-size:0.9rem;width:70px;outline:none;">它的一举一动。
        </div>
        <div style="display:flex;gap:10px;flex-wrap:wrap;margin-top:4px;">
          <button class="check-btn" onclick="checkFill('l11-fill1','流浪','l11-reveal1')">检查①</button>
          <button class="check-btn" onclick="checkFill('l11-fill2','拜访','l11-reveal2')">检查②</button>
          <button class="check-btn" onclick="checkFill('l11-fill3','教养','l11-reveal3')">检查③</button>
          <button class="check-btn" onclick="checkFill('l11-fill4','急切','l11-reveal4')">检查④</button>
          <button class="check-btn" onclick="checkFill('l11-fill5','监视','l11-reveal5')">检查⑤</button>
        </div>
        <div id="l11-reveal1" style="display:none;margin-top:8px;padding:8px 12px;border-radius:8px;border:1.5px solid #b2dac9;font-size:0.88rem;">①参考答案：<strong>流浪</strong></div>
        <div id="l11-reveal2" style="display:none;margin-top:4px;padding:8px 12px;border-radius:8px;border:1.5px solid #b2dac9;font-size:0.88rem;">②参考答案：<strong>拜访</strong></div>
        <div id="l11-reveal3" style="display:none;margin-top:4px;padding:8px 12px;border-radius:8px;border:1.5px solid #b2dac9;font-size:0.88rem;">③参考答案：<strong>教养</strong></div>
        <div id="l11-reveal4" style="display:none;margin-top:4px;padding:8px 12px;border-radius:8px;border:1.5px solid #b2dac9;font-size:0.88rem;">④参考答案：<strong>急切</strong></div>
        <div id="l11-reveal5" style="display:none;margin-top:4px;padding:8px 12px;border-radius:8px;border:1.5px solid #b2dac9;font-size:0.88rem;">⑤参考答案：<strong>监视</strong></div>
      </div>
      <div class="exercise-block">
        <div class="exercise-type">写作题 · Writing</div>
        <div class="exercise-q">4. 你养过宠物吗？你想过这只宠物在你不在家时都在做什么？这篇课文给我们介绍了钱小奇家几只可爱的猫咪，描述了主人与猫之间的感情。请参考练习5，把课文增写或缩写成300字左右的短文。</div>
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
        <div class="culture-title">熟悉下列名词：家居物品 + 工具<span class="pinyin">Household items and tools vocabulary</span></div>
        <div class="culture-zh">
          <table style="width:100%;border-collapse:collapse;font-size:0.88em;line-height:1.8;">
            <thead>
              <tr style="border-bottom:2px solid var(--mist);">
                <th style="text-align:left;padding:6px 10px;">词汇</th>
                <th style="text-align:left;padding:6px 10px;">拼音</th>
                <th style="text-align:left;padding:6px 10px;">说明 / 例句</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom:1px solid var(--mist);"><td style="padding:6px 10px;">床单</td><td style="padding:6px 10px;">chuángdān</td><td style="padding:6px 10px;">铺在床上的单子。她正在收拾床单。</td></tr>
              <tr style="border-bottom:1px solid var(--mist);"><td style="padding:6px 10px;">膜</td><td style="padding:6px 10px;">mó</td><td style="padding:6px 10px;">保鲜膜：家里的保鲜膜用完了。</td></tr>
              <tr style="border-bottom:1px solid var(--mist);"><td style="padding:6px 10px;">锤</td><td style="padding:6px 10px;">chuí</td><td style="padding:6px 10px;">一把锤子。帮我拿锤子过来。</td></tr>
              <tr style="border-bottom:1px solid var(--mist);"><td style="padding:6px 10px;">话筒</td><td style="padding:6px 10px;">huàtǒng</td><td style="padding:6px 10px;">一个话筒。歌手手里拿着一个话筒。</td></tr>
              <tr style="border-bottom:1px solid var(--mist);"><td style="padding:6px 10px;">轮胎</td><td style="padding:6px 10px;">lúntāi</td><td style="padding:6px 10px;">那辆车的轮胎被扎破了。</td></tr>
              <tr style="border-bottom:1px solid var(--mist);"><td style="padding:6px 10px;">钩子</td><td style="padding:6px 10px;">gōuzi</td><td style="padding:6px 10px;">一个钩子。钩子上挂着几个杯子。</td></tr>
              <tr style="border-bottom:1px solid var(--mist);"><td style="padding:6px 10px;">摄像头</td><td style="padding:6px 10px;">shèxiàngtóu</td><td style="padding:6px 10px;">家里安了三个摄像头。</td></tr>
              <tr style="border-bottom:1px solid var(--mist);"><td style="padding:6px 10px;">猫窝</td><td style="padding:6px 10px;">māowō</td><td style="padding:6px 10px;">每天早起第一件事就是清洁猫窝。</td></tr>
              <tr style="border-bottom:1px solid var(--mist);"><td style="padding:6px 10px;">窗台</td><td style="padding:6px 10px;">chuāngtái</td><td style="padding:6px 10px;">天天趴在窗台上晒太阳。</td></tr>
              <tr style="border-bottom:1px solid var(--mist);"><td style="padding:6px 10px;">钥匙</td><td style="padding:6px 10px;">yàoshi</td><td style="padding:6px 10px;">听到钥匙的声音，猫才会跑出来。</td></tr>
              <tr style="border-bottom:1px solid var(--mist);"><td style="padding:6px 10px;">脚步声</td><td style="padding:6px 10px;">jiǎobù shēng</td><td style="padding:6px 10px;">听到主人的脚步声。</td></tr>
              <tr><td style="padding:6px 10px;">数据</td><td style="padding:6px 10px;">shùjù</td><td style="padding:6px 10px;">通过对大量数据进行分析。</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div><!-- end culture tab -->

  </div><!-- end content-area L11 -->
  </div><!-- end lesson-content data-lesson="11" -->'''

# ============================================================
# Perform replacement
# ============================================================
content = HTML.read_text(encoding='utf-8')

# Replace L11 header
old_header_pattern = re.compile(
    r'  <div class="lesson-header" id="lesson-header-11".*?<p class="lesson-subtitle">.*?</p>\s*</div>',
    re.DOTALL
)
matches = old_header_pattern.findall(content)
assert len(matches) == 1, f"Expected 1 header match, got {len(matches)}"
content = old_header_pattern.sub(NEW_HEADER, content, count=1)

# Replace L11 content
old_content_pattern = re.compile(
    r'  <div class="lesson-content" data-lesson="11".*?</div><!-- end lesson-content data-lesson="11" -->',
    re.DOTALL
)
matches = old_content_pattern.findall(content)
assert len(matches) == 1, f"Expected 1 content match, got {len(matches)}"
content = old_content_pattern.sub(NEW_CONTENT, content, count=1)

# Unlock L11 in LIVE_LESSONS
content = content.replace(
    '  const LIVE_LESSONS = new Set([]);  // lessons with real content; others show coming-soon',
    '  const LIVE_LESSONS = new Set([11]);  // lessons with real content; others show coming-soon'
)

HTML.write_text(content, encoding='utf-8')
print(f'L11 replaced. New file size: {len(content):,} bytes')
print(f'Vocab words: {len(VOCAB)}')
