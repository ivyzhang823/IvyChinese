"""Replace the incorrect L10 stub with real content from 全球化视野中的中国饮食."""
import re
from pathlib import Path

HTML = Path('D:/Claude_CODE/IvyChinese/HSK/HSK6/hsk6_01-10.html')

# ============================================================
# NEW L10 HEADER
# ============================================================
NEW_HEADER = '''  <div class="lesson-header" id="lesson-header-10" data-lesson="10" data-watermark="十" style="display:none">
    <div class="lesson-meta">
      <button class="lesson-tag" onclick="showIndex()">
        <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"/></svg>
        HSK 6
      </button>
      <span class="lesson-tag-num">第十课 · Lesson 10</span>
    </div>
    <h1>全球化视野中的中国饮食</h1>
    <p style="font-size:0.9rem;color:var(--gold);margin-bottom:0.3rem;letter-spacing:0.02em;">Quánqiúhuà shìyě zhōng de Zhōngguó yǐnshí</p>
    <p class="lesson-subtitle">Chinese food in the global context</p>
  </div>'''

# ============================================================
# Vocabulary list (50 words from textbook pages 96-98)
# ============================================================
VOCAB = [
    ("视野", "shìyě", "n.", "field of vision, view", "全球化<em>视野</em>中的中国饮食。", "Chinese food from a global perspective."),
    ("饮食", "yǐnshí", "n.", "food and drink, diet", "中国的<em>饮食</em>文化历经数千年。", "Chinese food culture spans thousands of years."),
    ("蕴藏", "yùncáng", "v.", "to contain, to hold in store", "<em>蕴藏</em>着民族的精神。", "Contains the spirit of the nation."),
    ("传达", "chuándá", "v.", "to convey, to deliver", "<em>传达</em>着这个民族的文化传统。", "Conveys this nation's cultural tradition."),
    ("鲜明", "xiānmíng", "adj.", "clear-cut, distinct", "民族特性<em>鲜明</em>。", "With distinct national character."),
    ("区域", "qūyù", "n.", "zone, area, region", "不同<em>区域</em>、不同民族。", "Different regions, different peoples."),
    ("优异", "yōuyì", "adj.", "outstanding, excellent", "吸收不同民族的<em>优异</em>之处。", "Absorbing the best of other peoples."),
    ("以至", "yǐzhì", "conj.", "to such an extent that", "影响极深，<em>以至</em>影响到全世界。", "So deep that it reached the whole world."),
    ("辉煌", "huīhuáng", "adj.", "glorious, splendid", "<em>辉煌</em>至今。", "Glorious to this day."),
    ("和谐", "héxié", "adj.", "harmonious", "中和的<em>和谐</em>之道。", "The harmonious way of 'mean and balance'."),
    ("调和", "tiáohé", "v.", "to blend, to harmonize", "<em>调和</em>各种味道。", "Blend various flavors."),
    ("辽阔", "liáokuò", "adj.", "vast, extensive", "中华土地<em>辽阔</em>。", "China's land is vast."),
    ("飞禽走兽", "fēiqín-zǒushòu", "idiom", "birds and beasts", "高山上的<em>飞禽走兽</em>。", "The birds and beasts of high mountains."),
    ("湖泊", "húpō", "n.", "lake", "<em>湖泊</em>、小溪。", "Lakes and streams."),
    ("溪", "xī", "n.", "small stream, brook", "湖泊、小<em>溪</em>中的一条鱼。", "A fish from a lake or stream."),
    ("丘陵", "qiūlíng", "n.", "hills", "<em>丘陵</em>上种植的一棵菜。", "A vegetable grown on the hills."),
    ("种植", "zhòngzhí", "v.", "to plant, to grow", "丘陵上<em>种植</em>的菜。", "Vegetables grown on the hills."),
    ("精心", "jīngxīn", "adj.", "meticulous, painstaking", "经过<em>精心</em>构思。", "After meticulous design."),
    ("构思", "gòusī", "v.", "to conceive, to design", "精心<em>构思</em>。", "Meticulously conceive."),
    ("烹饪", "pēngrèn", "v.", "to cook", "巧妙<em>烹饪</em>。", "Cook skillfully."),
    ("即便", "jíbiàn", "conj.", "even, even if", "<em>即便</em>仅为一餐素食。", "Even just a vegetarian meal."),
    ("素食", "sùshí", "n.", "vegetarian meal", "仅为一餐<em>素食</em>。", "Just one vegetarian meal."),
    ("人间", "rénjiān", "n.", "human world", "可以让你尝尽<em>人间</em>美味。", "Can let you taste all the world's delicacies."),
    ("体系", "tǐxì", "n.", "system", "形成中华饮食<em>体系</em>。", "Formed the Chinese culinary system."),
    ("品种", "pǐnzhǒng", "n.", "variety, kind", "中国食物的<em>品种</em>。", "The variety of Chinese food."),
    ("接纳", "jiēnà", "v.", "to accept, to admit", "<em>接纳</em>其具有现代特征的方式。", "Accept its modern features."),
    ("形态", "xíngtài", "n.", "form, shape, pattern", "现代特征的<em>形态</em>。", "The form of modern features."),
    ("栽培", "zāipéi", "v.", "to cultivate, to grow", "合理引进、<em>栽培</em>外来农作物。", "Reasonably introduce and cultivate foreign crops."),
    ("培育", "péiyù", "v.", "to cultivate, to breed", "<em>培育</em>外来食物。", "Breed introduced foods."),
    ("凡是", "fánshì", "adv.", "every, any, all that...", "<em>凡是</em>人们一般认可的食物名称。", "All commonly accepted food names."),
    ("清晰", "qīngxī", "adj.", "clear, distinct", "把握得很<em>清晰</em>。", "Grasped very clearly."),
    ("分辨", "fēnbiàn", "v.", "to distinguish, to differentiate", "正宗的中餐与西餐的不同，使它<em>分辨</em>清楚。", "Distinguish authentic Chinese cuisine from Western cuisine."),
    ("频率", "pínlǜ", "n.", "frequency", "使用<em>频率</em>最高。", "Most frequently used."),
    ("调料", "tiáoliào", "n.", "seasoning, condiment", "葱、姜、蒜等<em>调料</em>。", "Scallion, ginger, garlic and other seasonings."),
    ("正宗", "zhèngzōng", "adj.", "authentic, orthodox", "<em>正宗</em>的中华食物。", "Authentic Chinese food."),
    ("加工", "jiāgōng", "v.", "to process", "对所有食物的<em>加工</em>。", "The processing of all foods."),
    ("照样", "zhàoyàng", "adv.", "in the same way, all the same", "<em>照样</em>美味。", "Just as delicious."),
    ("得力", "délì", "v.", "to benefit from", "<em>得力</em>于中国人。", "Benefiting from the Chinese."),
    ("固有", "gùyǒu", "adj.", "inherent, intrinsic", "中华食物的内在价值，<em>固有</em>的本性。", "The inherent value of Chinese food."),
    ("灵感", "línggǎn", "n.", "inspiration", "客观地匹配未食物成分为中华饮食的<em>灵感</em>。", "Inspiration in matching ingredients."),
    ("创新", "chuàngxīn", "v.", "to innovate", "创新地<em>创新</em>。", "Innovate creatively."),
    ("就餐", "jiùcān", "v.", "to dine, to have a meal", "中华文化样显示者不排斥开放文化的态度，比如中餐<em>就餐</em>的合餐制。", "Chinese culture's open attitude — for example, the shared-plate dining style."),
    ("排斥", "páichì", "v.", "to reject, to repel", "不<em>排斥</em>开放文化。", "Does not reject openness."),
    ("折", "zhé", "v.", "to fold", "南北朝时，一种可随意折起来、称作斯式具的有一种较大的餐桌。", "In the Southern and Northern dynasties, a foldable type of large table."),
    ("跪", "guì", "v.", "to kneel", "称作<em>跪</em>式的几案的合餐型。", "Called kneeling-style table."),
    ("局限", "júxiàn", "v.", "to limit, to confine", "根本不为'和'文化所<em>局限</em>。", "Not at all confined by 'harmony' culture."),
    ("诞生", "dànshēng", "v.", "to come into being, to be born", "中华饮食文化的<em>诞生</em>之日。", "The day Chinese food culture was born."),
    ("几成", "jǐchéng", "v.", "to come into existence", "就是中华饮食文化的传统之日。", "Came to be Chinese food's tradition."),
    ("元气", "yuánqì", "n.", "vigor, vitality", "充满活力的奥秘所在。", "Full of vigor — the mystery of its vitality."),
    ("奥秘", "àomì", "n.", "secret, mystery", "这也是其充满活力的<em>奥秘</em>所在。", "This is the mystery of its vitality."),
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

NEW_CONTENT = f'''  <div class="lesson-content" data-lesson="10" style="display:none">
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
      <div class="dialogue-block" id="l10-block1">
        <div class="dialogue-header">
          <div class="dialogue-title-wrap">
            <div class="dialogue-title-row">
              <span class="dialogue-title">课文 · 全球化视野中的中国饮食</span>
              <button class="dh-play-btn" id="l10-dhBtn1" onclick="dhPlay('l10-audioEl1','l10-dhBtn1')">
                <svg id="l10-dhIcon1" viewBox="0 0 24 24"><polygon points="5 3 19 12 5 21 5 3"/></svg>
              </button>
              <span style="flex:1;"></span>
              <div class="toggle-btns">
                <button class="toggle-btn" onclick="toggleBlock(this,'pinyin','l10-block1')"><span class="dot"></span>拼音</button>
                <button class="toggle-btn" onclick="toggleBlock(this,'en','l10-block1')"><span class="dot"></span>En</button>
              </div>
            </div>
            <span class="dialogue-title-en">Chinese food in the global context</span>
          </div>
          <audio id="l10-audioEl1" src="" onended="dhEnded('l10-audioEl1','l10-dhBtn1','l10-dhIcon1')" ontimeupdate="dhUpdate('l10-audioEl1')"></audio>
        </div>
        <div class="dialogue-line" style="display:block;">
          <div class="line-content" style="font-size:0.88em;">
            <div class="line-zh" style="line-height:1.9;">
              <p style="margin:0 0 0.15em 0;">任何一个民族的饮食都不仅为饮食，它蕴藏着这个民族的精神与特征，传达着这个民族的文化传统。中国的饮食文化历经数千年，始终具有魅力，是因为它不仅民族特性鲜明，而且善于吸收不同国家、不同区域、不同民族的优异之处，以至辉煌至今。</p>
              <p class="line-pinyin" style="margin:0 0 1.1em 0;display:none;">Rènhé yī gè mínzú de yǐnshí dōu bù jǐn wéi yǐnshí, tā yùncáng zhe zhège mínzú de jīngshén yǔ tèzhēng, chuándá zhe zhège mínzú de wénhuà chuántǒng. Zhōngguó de yǐnshí wénhuà lìjīng shù qiān nián, shǐzhōng jùyǒu mèilì, shì yīnwèi tā bù jǐn mínzú tèxìng xiānmíng, érqiě shànyú xīshōu bù tóng guójiā, bù tóng qūyù, bù tóng mínzú de yōuyì zhī chù, yǐzhì huīhuáng zhì jīn.</p>
              <p style="margin:0 0 0.15em 0;">中国文化的核心是一个"和"字。"和"包含"中和"和"谐"之意。"中和"的意思就是折中、调和，性质不同的事物。</p>
              <p class="line-pinyin" style="margin:0 0 1.1em 0;display:none;">Zhōngguó wénhuà de héxīn shì yī gè "hé" zì. "Hé" bāohán "zhōnghé" hé "xié" zhī yì. "Zhōnghé" de yìsi jiùshì zhézhōng, tiáohé, xìngzhì bù tóng de shìwù.</p>
              <p style="margin:0 0 0.15em 0;">原本中华饮食中的大量食物来自辽阔的土地，高山上的飞禽走兽，湖泊、小溪中的一条鱼，丘陵上种植的一棵菜，经过精心构思，巧妙烹饪，即便仅为一餐素食，也可以让你尝尽人间美味。汉唐以后，中亚及东南亚的食物进入了中华饮食体系，极大地丰富了中国食物的品种；近代，西方饮食思想方式得到引入，其有现代特征的中华饮食也逐渐形成。</p>
              <p class="line-pinyin" style="margin:0 0 1.1em 0;display:none;">Yuánběn Zhōnghuá yǐnshí zhōng de dàliàng shíwù lái zì liáokuò de tǔdì, gāoshān shàng de fēiqín-zǒushòu, húpō, xiǎo xī zhōng de yī tiáo yú, qiūlíng shàng zhòngzhí de yī kē cài, jīngguò jīngxīn gòusī, qiǎomiào pēngrèn, jíbiàn jǐn wéi yī cān sùshí, yě kěyǐ ràng nǐ chángjìn rénjiān měiwèi. Hàn-Táng yǐhòu, Zhōngyà jí Dōngnányà de shíwù jìnrù le Zhōnghuá yǐnshí tǐxì, jí dà de fēngfù le Zhōngguó shíwù de pǐnzhǒng; jìndài, xīfāng yǐnshí sīxiǎng fāngshì dédào yǐnrù, qí yǒu xiàndài tèzhēng de Zhōnghuá yǐnshí yě zhújiàn xíngchéng.</p>
              <p style="margin:0 0 0.15em 0;">在食材培育方面，中华饮食坚持以本国物产为基本原料，同时合理引进、培育外来农产品，比如咖啡、芒果等。凡是历史悠久的外来食品，人们一般以食物名称上就能立即清晰地标明它的洋身份。至于中餐中使用频率最高的葱、姜、蒜等调料，因其进入中华饮食年代久远，许多中国人甚至把它们当作正宗的中华食物。</p>
              <p class="line-pinyin" style="margin:0 0 1.1em 0;display:none;">Zài shícái péiyù fāngmiàn, Zhōnghuá yǐnshí jiānchí yǐ běnguó wùchǎn wéi jīběn yuánliào, tóngshí hélǐ yǐnjìn, péiyù wàilái nóngchǎnpǐn, bǐrú kāfēi, mángguǒ děng. Fánshì lìshǐ yōujiǔ de wàilái shípǐn, rénmen yībān yǐ shíwù míngchēng shàng jiù néng lìjí qīngxī de biāomíng tā de yáng shēnfèn. Zhìyú zhōngcān zhōng shǐyòng pínlǜ zuì gāo de cōng, jiāng, suàn děng tiáoliào, yīn qí jìnrù Zhōnghuá yǐnshí niándài jiǔyuǎn, xǔduō Zhōngguórén shènzhì bǎ tāmen dàngzuò zhèngzōng de Zhōnghuá shíwù.</p>
              <p style="margin:0 0 0.15em 0;">在加工过程中，中国人照样可以用中国方式定性外来食材，使它呈现中国人的味觉感受。而这一切得力于中国人对认识所有食物的内在价值，以对放性的思维方式，创新人地处理一种食物成为完美的中华饮食。</p>
              <p class="line-pinyin" style="margin:0 0 1.1em 0;display:none;">Zài jiāgōng guòchéng zhōng, Zhōngguórén zhàoyàng kěyǐ yòng Zhōngguó fāngshì dìngxìng wàilái shícái, shǐ tā chéngxiàn Zhōngguórén de wèijué gǎnshòu. Ér zhè yīqiè délì yú Zhōngguórén duì rènshí suǒyǒu shíwù de nèizài jiàzhí, yǐ duì fàngxìng de sīwéi fāngshì, chuàngxīn rén de chǔlǐ yī zhǒng shíwù chéngwéi wánměi de Zhōnghuá yǐnshí.</p>
              <p style="margin:0 0 0.15em 0;">在饮食方式上，中华饮食样显示者不排斥开放文化的态度，比如中餐"合餐制"的形成。先秦至唐代，中国采用分餐方式就餐。南北朝时，一种可随意折起来、称作斯式具的有一种较大的餐桌，被传到中亚地区进入中国，至唐代，这些都引入到了餐厅，形成了围坐合餐的方式。当然，所谓"合餐制"的形成，根本不为"和"文化所局限，因为可以说，中华饮食文化诞生之日，就成与"和"文化生存的发展之日。</p>
              <p class="line-pinyin" style="margin:0 0 1.1em 0;display:none;">Zài yǐnshí fāngshì shàng, Zhōnghuá yǐnshí yàng xiǎnshì zhě bù páichì kāifàng wénhuà de tàidu, bǐrú zhōngcān "hécān zhì" de xíngchéng. Xiānqín zhì Tángdài, Zhōngguó cǎiyòng fēncān fāngshì jiùcān. Nánběicháo shí, yī zhǒng kě suíyì zhé qǐlái, chēng zuò sī shì jù de yǒu yī zhǒng jiào dà de cānzhuō, bèi chuán dào Zhōngyà dìqū jìnrù Zhōngguó, zhì Tángdài, zhèxiē dōu yǐnrù dào le cāntīng, xíngchéng le wéizuò hécān de fāngshì. Dāngrán, suǒwèi "hécān zhì" de xíngchéng, gēnběn bù wéi "hé" wénhuà suǒ júxiàn, yīnwèi kěyǐ shuō, Zhōnghuá yǐnshí wénhuà dànshēng zhī rì, jiù chéng yǔ "hé" wénhuà shēngcún de fāzhǎn zhī rì.</p>
              <p style="margin:0 0 0.15em 0;">可以说，中华饮食文化自诞生之日起，就向一个开放、包容的方向发展，这也是其充满活力的奥秘所在。</p>
              <p class="line-pinyin" style="margin:0 0 1.1em 0;display:none;">Kěyǐ shuō, Zhōnghuá yǐnshí wénhuà zì dànshēng zhī rì qǐ, jiù xiàng yī gè kāifàng, bāoróng de fāngxiàng fāzhǎn, zhè yě shì qí chōngmǎn huólì de àomì suǒzài.</p>
            </div>
            <div class="line-en" style="margin-top:1.5em;padding-top:1em;border-top:1px solid var(--mist);display:none;">The cuisine of any people is never merely cuisine — it shelters that people's spirit and traits, and conveys their cultural tradition. Chinese food culture has carried its charm for thousands of years precisely because its national identity is sharply defined, and because it is unusually skilled at absorbing what is best from other nations, regions, and peoples — a brilliance that endures to this day.<br><br>The core of Chinese culture is a single character: 和 (harmony). 和 contains two senses — 中和 ("mean and balance") and 谐 ("harmony"). 中和 means moderation: blending and balancing things of different natures.<br><br>Most of the foods in traditional Chinese cuisine came from China's vast lands — game from the high mountains, a fish from the lakes and streams, a vegetable grown on the hills. Through meticulous design and skilled cooking, even a single vegetarian meal can let you taste all the flavors of the human world. From the Han and Tang dynasties onward, foods from Central Asia and Southeast Asia entered the Chinese culinary system and vastly expanded its variety. In modern times, Western culinary ideas were introduced as well, and a Chinese cuisine with modern traits gradually took shape.<br><br>In ingredient cultivation, Chinese cuisine has always taken local produce as its base while sensibly introducing and growing foreign crops — coffee, mango, and so on. For long-standing imports, people can usually mark the "foreign" identity right in the name. As for the most-used seasonings — scallion, ginger, garlic — they entered Chinese cooking so long ago that many Chinese now regard them as native Chinese ingredients.<br><br>In processing, Chinese cooks can re-define foreign ingredients in a Chinese way, making them yield a Chinese palate. All of this owes to the Chinese understanding of the intrinsic value of every food, combined with an open-minded approach that creatively turns each ingredient into a complete Chinese dish.<br><br>In dining style, Chinese cuisine likewise shows its openness — take, for example, the rise of "shared-plate" dining. From the pre-Qin era through the Tang, China followed individual-plate dining. During the Northern and Southern Dynasties, a kind of larger, foldable table — originally a Central-Asian object — was introduced into China, and by the Tang it had moved into dining halls, giving rise to seated, shared-plate meals. The emergence of "shared-plate" dining was never confined by the culture of "和" — for it can be said that the very day Chinese food culture was born became the day "和" culture began to grow.<br><br>One could say that, from its birth, Chinese food culture has moved toward openness and inclusion — and there lies the secret of its enduring vitality.</div>
          </div>
        </div>
      </div>
    </div><!-- end 课文 tab -->

    <!-- 生词表 -->
    <div data-tab="vocab" class="tab-panel">
      <div class="fc-slider-wrap">
        <div class="fc-row">
          <div class="fc-slider" id="l10-fcSlider">
{fc_cards_html}
          </div>
        </div>
        <div style="display:flex;align-items:center;gap:10px;margin-top:10px;">
          <button class="fc-arrow" onclick="fcNav(-1)"><svg viewBox="0 0 24 24"><polyline points="15 18 9 12 15 6"/></svg></button>
          <span class="fc-counter" id="l10-fcCounter" style="min-width:36px;text-align:center;line-height:1;">1 / {len(VOCAB)}</span>
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
        <div class="vocab-zh">飞禽走兽</div><div class="vocab-pinyin">fēiqín-zǒushòu</div><div class="vocab-pos">idiom</div>
        <div class="vocab-en">birds and beasts; all kinds of wildlife (lit. "flying-birds, running-beasts") — fixed four-character phrase referring to wild animals as a whole</div>
        <div class="vocab-example">
          高山上的<em>飞禽走兽</em>。<br>
          <span style="color:#bbb">The wildlife of the high mountains.</span><br>
          这片森林里栖息着各种<em>飞禽走兽</em>。<br>
          <span style="color:#bbb">All sorts of birds and beasts live in this forest.</span>
        </div>
      </div>
      <div class="vocab-card">
        <div class="vocab-zh">蕴藏</div><div class="vocab-pinyin">yùncáng</div><div class="vocab-pos">v.</div>
        <div class="vocab-en">to contain (hidden within); to be stored up; to harbor — used for abstract or natural resources held within something</div>
        <div class="vocab-example">
          饮食<em>蕴藏</em>着这个民族的精神与特征。<br>
          <span style="color:#bbb">Cuisine harbors a people's spirit and traits.</span><br>
          这片土地<em>蕴藏</em>着丰富的矿产资源。<br>
          <span style="color:#bbb">This land contains rich mineral resources.</span>
        </div>
      </div>
      <div class="vocab-card">
        <div class="vocab-zh">以至</div><div class="vocab-pinyin">yǐzhì</div><div class="vocab-pos">conj.</div>
        <div class="vocab-en">to such an extent that; so... that — links a cause/situation to a noteworthy result; formal register</div>
        <div class="vocab-example">
          善于吸收不同民族的优异之处，<em>以至</em>辉煌至今。<br>
          <span style="color:#bbb">Skilled at absorbing the best of other peoples, so much so that it remains glorious today.</span><br>
          他工作太忙了，<em>以至</em>常常忘记吃饭。<br>
          <span style="color:#bbb">He's so busy that he often forgets to eat.</span>
        </div>
      </div>
      <div class="vocab-card">
        <div class="vocab-zh">凡是</div><div class="vocab-pinyin">fánshì</div><div class="vocab-pos">adv.</div>
        <div class="vocab-en">every; any; all that... — sets up a universal statement; always followed by a noun/noun phrase and a 都 / 全 in the predicate</div>
        <div class="vocab-example">
          <em>凡是</em>历史悠久的外来食品，人们都能立即清晰地标明它的洋身份。<br>
          <span style="color:#bbb">All foreign foods with a long history can be immediately marked by name as foreign.</span><br>
          <em>凡是</em>来开会的人，都要带笔记本电脑。<br>
          <span style="color:#bbb">Everyone who comes to the meeting must bring a laptop.</span>
        </div>
      </div>
    </div><!-- end worddetail tab -->

    <!-- 语法 -->
    <div data-tab="grammar" class="tab-panel">
      <div class="grammar-switcher">
        <button class="grammar-switch-btn active" onclick="switchGrammar(0, this)">以至</button>
        <button class="grammar-switch-btn" onclick="switchGrammar(1, this)">即便</button>
        <button class="grammar-switch-btn" onclick="switchGrammar(2, this)">所在</button>
        <button class="grammar-switch-btn" onclick="switchGrammar(3, this)">凡是 vs 所有</button>
      </div>
      <div class="grammar-panel active">
        <div class="grammar-block">
          <div class="grammar-title"><span class="grammar-num">1</span>以至 · "To such an extent that…" — result conjunction</div>
          <p class="grammar-desc">"以至"，连词，用在后一分句的开头，表示由前一分句的情况程度很深而产生某种结果。也可以说"以至于"。<br><span style="color:#888;font-size:0.85em;">"以至" introduces the result of a cause described in the preceding clause. The cause is so significant or extreme that it leads to the stated result. Formal register.</span></p>
          <div class="grammar-pattern">[cause / situation], 以至 + [result]</div>
          <div class="grammar-examples">
            <div class="grammar-ex"><div class="zh">中国饮食文化历经数千年，始终具有魅力，是因为它不仅民族特性鲜明，而且善于吸收不同国家、不同区域、不同民族的优异之处，以至辉煌至今。</div><div class="en">Chinese food culture has remained captivating for thousands of years — so much so that it is still glorious today.</div></div>
            <div class="grammar-ex"><div class="zh">他一干就是十几年，以至于忘记了自己已年过半百。</div><div class="en">He worked for over a decade, to the point of forgetting he was past fifty.</div></div>
            <div class="grammar-ex"><div class="zh">书著名作家纪伯仑(Kahlil Gibran)曾说："我们已经走得太远，以至于忘了为什么出发。"</div><div class="en">The famous writer Kahlil Gibran once said: "We've come too far, so far that we've forgotten why we set out."</div></div>
          </div>
          <div class="grammar-block" style="margin-top:1.2em;">
            <div class="grammar-title" style="font-size:0.9em;">练一练 · 用"以至"完成句子</div>
            <div class="grammar-examples">
              <div class="grammar-ex"><div class="zh">1. 朋友告诉我，这所商学院在北美有相当的知名度，____________________。</div></div>
              <div class="grammar-ex"><div class="zh">2. 科学技术的发展实在是太快了，____________________，如今变为了现实。</div></div>
              <div class="grammar-ex"><div class="zh">3. 走在路上，他脚下一直是想到的事，____________________。</div></div>
            </div>
          </div>
        </div>
      </div>
      <div class="grammar-panel">
        <div class="grammar-block">
          <div class="grammar-title"><span class="grammar-num">2</span>即便 · "Even if" — hypothetical concession</div>
          <p class="grammar-desc">"即便"，连词，表示假设兼让步，意思是"即使"。后一分句常带"也"。<br><span style="color:#888;font-size:0.85em;">"即便" introduces a hypothetical concession, equivalent to 即使 ("even if"). The main clause typically contains 也 ("still / nevertheless").</span></p>
          <div class="grammar-pattern">即便 + [hypothetical condition], 也 + [main clause]</div>
          <div class="grammar-examples">
            <div class="grammar-ex"><div class="zh">即便仅为一餐素食，也可以让你尝尽人间美味。</div><div class="en">Even just a vegetarian meal can let you taste all the world's delights.</div></div>
            <div class="grammar-ex"><div class="zh">她虽然这样不太合理，即便我不喜欢，你也无能为力。</div><div class="en">Even though it's not entirely reasonable — even if I don't like it, you can't help it.</div></div>
            <div class="grammar-ex"><div class="zh">即便我成功了，对方也不会接受。</div><div class="en">Even if I succeed, the other side will not accept.</div></div>
          </div>
          <div class="grammar-block" style="margin-top:1.2em;">
            <div class="grammar-title" style="font-size:0.9em;">练一练 · 用"即便"完成句子</div>
            <div class="grammar-examples">
              <div class="grammar-ex"><div class="zh">1. 我家附近就有冬泉冠军，____________________。</div></div>
              <div class="grammar-ex"><div class="zh">2. 大家____________________，即便他说了也没有用。</div></div>
              <div class="grammar-ex"><div class="zh">3. ____________________，你也应该考虑要不要去。</div></div>
            </div>
          </div>
        </div>
      </div>
      <div class="grammar-panel">
        <div class="grammar-block">
          <div class="grammar-title"><span class="grammar-num">3</span>所在 · "The place where..." — formal noun</div>
          <p class="grammar-desc">"所在"，名词，意思是处所、存在的地方。多用于书面语。常用于"…的所在""…的奥秘所在"。<br><span style="color:#888;font-size:0.85em;">"所在" is a written-register noun meaning "the place where..." or "the locus of...". Often used in phrases like X的所在 ("the place of X") and 奥秘所在 ("the secret/key of...").</span></p>
          <div class="grammar-pattern">[modifier] + 的 + 所在  /  ……的奥秘 + 所在</div>
          <div class="grammar-examples">
            <div class="grammar-ex"><div class="zh">这也是其充满活力的奥秘所在。</div><div class="en">This is precisely where the secret of its vitality lies.</div></div>
            <div class="grammar-ex"><div class="zh">他选择了我家乡的农场作为他写作的所在。</div><div class="en">He chose the farm in my hometown as the place for his writing.</div></div>
            <div class="grammar-ex"><div class="zh">中华饮食文化能历久弥新，这也是其充满活力的奥秘所在。</div><div class="en">Chinese food culture stays fresh through the ages — that's where its vitality lies.</div></div>
          </div>
          <div class="grammar-block" style="margin-top:1.2em;">
            <div class="grammar-title" style="font-size:0.9em;">练一练 · 为"所在"选择适当的位置</div>
            <div class="grammar-examples">
              <div class="grammar-ex"><div class="zh">1. 大家都坚信A我A找到的力量B，我们一定会齐心C完成这个项目D。</div></div>
              <div class="grammar-ex"><div class="zh">2. 我看到问题A并不大C，才让B提出问题D。</div></div>
              <div class="grammar-ex"><div class="zh">3. 给人难得B创造幸福C的生活，是父亲一生为之奋斗D的目标A。</div></div>
            </div>
          </div>
        </div>
      </div>
      <div class="grammar-panel">
        <div class="grammar-block">
          <div class="grammar-title"><span class="grammar-num">4</span>凡是 vs 所有 · Both express totality</div>
          <p class="grammar-desc">两者都表示"所有的", 都强调没有例外。<br><span style="color:#888;font-size:0.85em;">Both mean "all" / "every", but with different scope and syntax:</span></p>
          <div class="grammar-pattern">凡是：副词；强调"凡是符合特定条件、特征或类别的人或事物"，后接名词，再加"都/全/一律"。<br>所有：形容词；直接修饰名词，表示"全部"。<br>区别：凡是 ⊂ 所有；凡是必须设定条件，所有可不设定。</div>
          <div class="grammar-examples">
            <div class="grammar-ex"><div class="zh">凡是来开会的人，都要带笔记本电脑。 ✓ (强调"符合条件的所有人")</div><div class="en">Everyone who comes to the meeting must bring a laptop.</div></div>
            <div class="grammar-ex"><div class="zh">所有的人都到齐了。 ✓ (强调"全部的人")</div><div class="en">All the people have arrived.</div></div>
            <div class="grammar-ex"><div class="zh">凡是历史悠久的外来食品，都能立即标明它的洋身份。</div><div class="en">All long-established foreign foods can immediately be identified as foreign.</div></div>
          </div>
          <div class="grammar-block" style="margin-top:1.2em;">
            <div class="grammar-title" style="font-size:0.9em;">做一做 · Fill in 凡是 or 所有</div>
            <div class="grammar-examples">
              <div class="grammar-ex"><div class="zh">1. __________见过她的人，都不会忘记她漂亮的笑容。（凡是）</div></div>
              <div class="grammar-ex"><div class="zh">2. __________有效的方法，我都会尝试。（凡是 / 所有）</div></div>
              <div class="grammar-ex"><div class="zh">3. __________收到这种邮件的人，请不要打开，已经证实这是病毒。（凡是）</div></div>
            </div>
          </div>
        </div>
      </div>
    </div><!-- end grammar tab -->

    <!-- 练习 -->
    <div data-tab="exercise" class="tab-panel">
      <div class="exercise-block">
        <div class="exercise-type">选择题 · Multiple Choice</div>
        <div class="exercise-q">1. 课文中说中国饮食文化历经数千年始终具有魅力的原因是什么？</div>
        <div class="exercise-choices">
          <div class="choice" onclick="selectChoice(this, false)"><span class="choice-label">A</span>原料丰富</div>
          <div class="choice" onclick="selectChoice(this, true)"><span class="choice-label">B</span>民族特性鲜明，且善于吸收不同国家、区域、民族的优异之处</div>
          <div class="choice" onclick="selectChoice(this, false)"><span class="choice-label">C</span>烹饪技巧高超</div>
          <div class="choice" onclick="selectChoice(this, false)"><span class="choice-label">D</span>价格便宜</div>
        </div>
      </div>
      <div class="exercise-block">
        <div class="exercise-type">选择题 · Multiple Choice</div>
        <div class="exercise-q">2. 课文中提到中国文化的核心是哪一个字？</div>
        <div class="exercise-choices">
          <div class="choice" onclick="selectChoice(this, false)"><span class="choice-label">A</span>礼</div>
          <div class="choice" onclick="selectChoice(this, false)"><span class="choice-label">B</span>仁</div>
          <div class="choice" onclick="selectChoice(this, true)"><span class="choice-label">C</span>和</div>
          <div class="choice" onclick="selectChoice(this, false)"><span class="choice-label">D</span>义</div>
        </div>
      </div>
      <div class="exercise-block">
        <div class="exercise-type">填空题 · Fill in the Blank</div>
        <div class="exercise-q">3. 从下面的词中选择合适的词填空：辉煌 · 调料 · 鲜明 · 蕴藏 · 体系</div>
        <div style="font-size:0.88em;line-height:2;margin:8px 0 12px 0;">
          中国饮食文化中<input id="l10-fill1" type="text" placeholder="蕴藏" style="padding:4px 8px;border:1.5px solid var(--mist);border-radius:6px;font-family:'Outfit',sans-serif;font-size:0.9rem;width:70px;outline:none;">着深厚的民族精神，特性<input id="l10-fill2" type="text" placeholder="鲜明" style="padding:4px 8px;border:1.5px solid var(--mist);border-radius:6px;font-family:'Outfit',sans-serif;font-size:0.9rem;width:70px;outline:none;">。中华饮食的<input id="l10-fill3" type="text" placeholder="体系" style="padding:4px 8px;border:1.5px solid var(--mist);border-radius:6px;font-family:'Outfit',sans-serif;font-size:0.9rem;width:70px;outline:none;">历经数千年的发展，至今仍然<input id="l10-fill4" type="text" placeholder="辉煌" style="padding:4px 8px;border:1.5px solid var(--mist);border-radius:6px;font-family:'Outfit',sans-serif;font-size:0.9rem;width:70px;outline:none;">。葱、姜、蒜是使用频率最高的<input id="l10-fill5" type="text" placeholder="调料" style="padding:4px 8px;border:1.5px solid var(--mist);border-radius:6px;font-family:'Outfit',sans-serif;font-size:0.9rem;width:70px;outline:none;">。
        </div>
        <div style="display:flex;gap:10px;flex-wrap:wrap;margin-top:4px;">
          <button class="check-btn" onclick="checkFill('l10-fill1','蕴藏','l10-reveal1')">检查①</button>
          <button class="check-btn" onclick="checkFill('l10-fill2','鲜明','l10-reveal2')">检查②</button>
          <button class="check-btn" onclick="checkFill('l10-fill3','体系','l10-reveal3')">检查③</button>
          <button class="check-btn" onclick="checkFill('l10-fill4','辉煌','l10-reveal4')">检查④</button>
          <button class="check-btn" onclick="checkFill('l10-fill5','调料','l10-reveal5')">检查⑤</button>
        </div>
        <div id="l10-reveal1" style="display:none;margin-top:8px;padding:8px 12px;border-radius:8px;border:1.5px solid #b2dac9;font-size:0.88rem;">①参考答案：<strong>蕴藏</strong></div>
        <div id="l10-reveal2" style="display:none;margin-top:4px;padding:8px 12px;border-radius:8px;border:1.5px solid #b2dac9;font-size:0.88rem;">②参考答案：<strong>鲜明</strong></div>
        <div id="l10-reveal3" style="display:none;margin-top:4px;padding:8px 12px;border-radius:8px;border:1.5px solid #b2dac9;font-size:0.88rem;">③参考答案：<strong>体系</strong></div>
        <div id="l10-reveal4" style="display:none;margin-top:4px;padding:8px 12px;border-radius:8px;border:1.5px solid #b2dac9;font-size:0.88rem;">④参考答案：<strong>辉煌</strong></div>
        <div id="l10-reveal5" style="display:none;margin-top:4px;padding:8px 12px;border-radius:8px;border:1.5px solid #b2dac9;font-size:0.88rem;">⑤参考答案：<strong>调料</strong></div>
      </div>
      <div class="exercise-block">
        <div class="exercise-type">写作题 · Writing</div>
        <div class="exercise-q">4. 这篇课文介绍了富有魅力的中国饮食文化，分别从饮食文化的历史发展、食材培育方面、就餐方式等几个方面进行了介绍。请参考练习5，把课文增写或缩写成300字左右的短文。</div>
        <textarea style="width:100%;min-height:120px;padding:10px 14px;border:1.5px solid var(--mist);border-radius:8px;font-family:'Outfit',sans-serif;font-size:0.9rem;margin-top:10px;resize:vertical;" placeholder="在这里写你的短文…"></textarea>
      </div>
    </div><!-- end exercise tab -->

    <!-- 更多 -->
    <div data-tab="culture" class="tab-panel">
      <div class="culture-block">
        <div class="culture-head">
          <div class="culture-tag">🏮 地理词汇</div>
          <button class="en-toggle" onclick="toggleEn(this)">En</button>
        </div>
        <div class="culture-title">熟悉下列地理方面的词语<span class="pinyin">Geography-related vocabulary</span></div>
        <div class="culture-zh">
          <table style="width:100%;border-collapse:collapse;font-size:0.88em;line-height:1.8;">
            <thead>
              <tr style="border-bottom:2px solid var(--mist);">
                <th style="text-align:left;padding:6px 10px;">大类</th>
                <th style="text-align:left;padding:6px 10px;">词语</th>
                <th style="text-align:left;padding:6px 10px;">说明 / 例句</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom:1px solid var(--mist);"><td style="padding:6px 10px;">地理</td><td style="padding:6px 10px;">地貌、地势、地表、地形</td><td style="padding:6px 10px;">中国地貌多样，从青藏高原到东海平原都有。</td></tr>
              <tr style="border-bottom:1px solid var(--mist);"><td style="padding:6px 10px;">地区</td><td style="padding:6px 10px;">地区、地段、地带、分区</td><td style="padding:6px 10px;">这一地区盛产水果。</td></tr>
              <tr style="border-bottom:1px solid var(--mist);"><td style="padding:6px 10px;">水流</td><td style="padding:6px 10px;">溪、运河、湖泊、瀑布、沼泽</td><td style="padding:6px 10px;">山间小溪清澈见底。</td></tr>
              <tr style="border-bottom:1px solid var(--mist);"><td style="padding:6px 10px;">海洋</td><td style="padding:6px 10px;">海湾、海峡、海岸、海面</td><td style="padding:6px 10px;">台湾海峡连接东海与南海。</td></tr>
              <tr style="border-bottom:1px solid var(--mist);"><td style="padding:6px 10px;">高地</td><td style="padding:6px 10px;">山脉、高原、丘陵、山峰</td><td style="padding:6px 10px;">丘陵上种植茶树。</td></tr>
              <tr style="border-bottom:1px solid var(--mist);"><td style="padding:6px 10px;">低地</td><td style="padding:6px 10px;">平原、盆地、低地、洼地</td><td style="padding:6px 10px;">华北平原是重要的粮食产区。</td></tr>
              <tr style="border-bottom:1px solid var(--mist);"><td style="padding:6px 10px;">中和</td><td style="padding:6px 10px;">"中和"——核心哲学</td><td style="padding:6px 10px;">"中和"思想体现在饮食中：调和不同食材以达到味道的平衡。</td></tr>
              <tr style="border-bottom:1px solid var(--mist);"><td style="padding:6px 10px;">和谐</td><td style="padding:6px 10px;">"和"——饮食精神</td><td style="padding:6px 10px;">合餐制体现的"和"文化：聚餐分享，强化亲情友情。</td></tr>
              <tr style="border-bottom:1px solid var(--mist);"><td style="padding:6px 10px;">食材</td><td style="padding:6px 10px;">飞禽走兽、果蔬、水产</td><td style="padding:6px 10px;">中国食材丰富，山珍海味俱全。</td></tr>
              <tr style="border-bottom:1px solid var(--mist);"><td style="padding:6px 10px;">引进</td><td style="padding:6px 10px;">栽培、培育、引种</td><td style="padding:6px 10px;">咖啡、芒果等外来作物已在中国成功栽培。</td></tr>
              <tr style="border-bottom:1px solid var(--mist);"><td style="padding:6px 10px;">烹饪</td><td style="padding:6px 10px;">炒、煮、蒸、烤、炸、煎、炖</td><td style="padding:6px 10px;">中餐烹饪方式多种多样。</td></tr>
              <tr><td style="padding:6px 10px;">就餐</td><td style="padding:6px 10px;">合餐制、分餐制、宴席、家宴</td><td style="padding:6px 10px;">合餐制由唐代逐渐形成，至今仍是中式就餐的主流。</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div><!-- end culture tab -->

  </div><!-- end content-area L10 -->
  </div><!-- end lesson-content data-lesson="10" -->'''

# ============================================================
# Perform replacement
# ============================================================
content = HTML.read_text(encoding='utf-8')

old_header_pattern = re.compile(
    r'  <div class="lesson-header" id="lesson-header-10".*?<p class="lesson-subtitle">.*?</p>\s*</div>',
    re.DOTALL
)
matches = old_header_pattern.findall(content)
assert len(matches) == 1, f"Expected 1 header match, got {len(matches)}"
content = old_header_pattern.sub(NEW_HEADER, content, count=1)

old_content_pattern = re.compile(
    r'  <div class="lesson-content" data-lesson="10".*?</div><!-- end lesson-content data-lesson="10" -->',
    re.DOTALL
)
matches = old_content_pattern.findall(content)
assert len(matches) == 1, f"Expected 1 content match, got {len(matches)}"
content = old_content_pattern.sub(NEW_CONTENT, content, count=1)

HTML.write_text(content, encoding='utf-8')
print(f'L10 replaced. New file size: {len(content):,} bytes')
print(f'Vocab words: {len(VOCAB)}')
