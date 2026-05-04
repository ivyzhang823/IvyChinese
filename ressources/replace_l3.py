import re

HTML_PATH = r'D:\Claude_CODE\IvyChinese\HSK\HSK6\hsk6_01-10.html'

with open(HTML_PATH, encoding='utf-8') as f:
    content = f.read()

pattern_l3 = r'<div class="lesson-header" id="lesson-header-3"[^>]*>\s*</div>\s*\n\s*<div class="lesson-content" data-lesson="3"[^>]*>\s*</div>'

replacement_l3 = '''<div class="lesson-header" id="lesson-header-3" data-lesson="3" data-watermark="三" style="display:none">
    <div class="lesson-meta">
      <button class="lesson-tag" onclick="showIndex()">
        <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"/></svg>
        HSK 6
      </button>
      <span class="lesson-tag-num">第三课 · Lesson 03</span>
    </div>
    <h1>一盒月饼</h1>
    <p style="font-size:0.9rem;color:var(--gold);margin-bottom:0.3rem;letter-spacing:0.02em;">Yī hé yuèbing</p>
    <p class="lesson-subtitle">A box of moon cakes</p>
  </div>

  <div class="lesson-content" data-lesson="3" style="display:none">
  <div class="tab-nav">
    <button class="tab-btn active" onclick="switchTab(\'text\', this)">📖 课文</button>
    <button class="tab-btn" onclick="switchTab(\'vocab\', this)">📝 生词表</button>
    <button class="tab-btn" onclick="switchTab(\'worddetail\', this)">🔍 词汇详解</button>
    <button class="tab-btn" onclick="switchTab(\'grammar\', this)">🔤 语法</button>
    <button class="tab-btn" onclick="switchTab(\'exercise\', this)">✏️ 练习</button>
    <button class="tab-btn" onclick="switchTab(\'culture\', this)">🏮 更多</button>
  </div>
  <div class="content-area">

    <!-- 课文 -->
    <div data-tab="text" class="tab-panel active">
      <div class="dialogue-block" id="l3-block1">
        <div class="dialogue-header">
          <div class="dialogue-title-wrap">
            <div class="dialogue-title-row">
              <span class="dialogue-title">课文 · 一盒月饼</span>
              <button class="dh-play-btn" id="l3-dhBtn1" onclick="dhPlay(\'l3-audioEl1\',\'l3-dhBtn1\')">
                <svg id="l3-dhIcon1" viewBox="0 0 24 24"><polygon points="5 3 19 12 5 21 5 3"/></svg>
              </button>
              <span style="flex:1;"></span>
              <div class="toggle-btns">
                <button class="toggle-btn" onclick="toggleBlock(this,\'pinyin\',\'l3-block1\')"><span class="dot"></span>拼音</button>
                <button class="toggle-btn" onclick="toggleBlock(this,\'en\',\'l3-block1\')"><span class="dot"></span>En</button>
              </div>
            </div>
            <span class="dialogue-title-en">A box of moon cakes</span>
          </div>
          <audio id="l3-audioEl1" src="" onended="dhEnded(\'l3-audioEl1\',\'l3-dhBtn1\',\'l3-dhIcon1\')" ontimeupdate="dhUpdate(\'l3-audioEl1\')"></audio>
        </div>
        <div class="dialogue-line" style="display:block;">
          <div class="line-content" style="font-size:0.88em;">
            <div class="line-zh" style="line-height:1.9;">
              <p style="margin:0 0 0.15em 0;">清晨上班，走到公司楼下，迎面站着一位农民工模样的男人，他打量了我一番，到嘴边的话又不说了。我停住脚步，疑惑地问："您有事吗？"他搓着手，迟疑地说："有件事想拜托你。"</p>
              <p class="line-pinyin" style="margin:0 0 1.1em 0;display:none;">Qīngchén shàngbān, zǒu dào gōngsī lóuxià, yíngmiàn zhàn zhe yī wèi nóngmíngōng múyàng de nánrén, tā dǎliang le wǒ yī fān, dào zuǐ biān de huà yòu bù shuō le. Wǒ tíng zhù jiǎobù, yíhuò de wèn: "Nín yǒu shì ma?" Tā cuō zhe shǒu, chíyí de shuō: "Yǒu jiàn shì xiǎng bàituō nǐ."</p>
              <p style="margin:0 0 0.15em 0;">"您说吧，只要能帮的，我一定帮。"这回轮到我打量他了：饱经沧桑的脸上流露出朴实；一双过于操劳的大手；胡须起码一个星期没刮了；南方口音。</p>
              <p class="line-pinyin" style="margin:0 0 1.1em 0;display:none;">"Nín shuō ba, zhǐyào néng bāng de, wǒ yīdìng bāng." Zhè huí lún dào wǒ dǎliang tā le: bǎojīng-cāngsāng de liǎn shàng liúlù chū pǔshí; yī shuāng guòyú cāoláo de dà shǒu; húxū qǐmǎ yī ge xīngqī méi guā le; nánfāng kǒuyīn.</p>
              <p style="margin:0 0 0.15em 0;">果然，他来自南方的一个乡镇，原先是裁缝，现在在我们旁边的港口干活。他女儿在上海，中秋节快到了，要给他寄盒月饼，可他白天在工地，地址没法写，想请我帮他代收一下。</p>
              <p class="line-pinyin" style="margin:0 0 1.1em 0;display:none;">Guǒrán, tā lái zì nánfāng de yī ge xiāngzhèn, yuánxiān shì cáifeng, xiànzài zài wǒmen pángbiān de gǎngkǒu gàn huó. Tā nǚ\'ér zài Shànghǎi, Zhōngqiūjié kuài dào le, yào gěi tā jì hé yuèbing, kě tā báitiān zài gōngdì, dìzhǐ méi fǎ xiě, xiǎng qǐng wǒ bāng tā dài shōu yīxià.</p>
              <p style="margin:0 0 0.15em 0;">"这个忙好帮，您不怕我把收到的月饼给吃了？"我半开玩笑地说。他笑着说："不会，你和我女儿一样，斯斯文文的，一看就读过书，心眼儿好，守信誉，怎么会欺骗我呢？"他说女儿念了硕士，有学位，在一家一流的公司上班，是个主管，还有助手，怎么也算得上是公司的骨干。说起女儿，他满脸的骄傲。</p>
              <p class="line-pinyin" style="margin:0 0 1.1em 0;display:none;">"Zhège máng hǎo bāng, nín bù pà wǒ bǎ shōu dào de yuèbing gěi chī le?" Wǒ bàn kāi wánxiào de shuō. Tā xiào zhe shuō: "Bù huì, nǐ hé wǒ nǚ\'ér yīyàng, sīsī-wénwén de, yī kàn jiù dú guò shū, xīnyǎnr hǎo, shǒu xìnyù, zěnme huì qīpiàn wǒ ne?" Tā shuō nǚ\'ér niàn le shuòshì, yǒu xuéwèi, zài yī jiā yīliú de gōngsī shàngbān, shì ge zhǔguǎn, hái yǒu zhùshǒu, zěnme yě suàn de shàng shì gōngsī de gǔgàn. Shuō qǐ nǚ\'ér, tā mǎn liǎn de jiāo\'ào.</p>
              <p style="margin:0 0 0.15em 0;">我记下了他的电话，给了他一张我的名片。他小心翼翼地收起来，满怀喜悦地走了。</p>
              <p class="line-pinyin" style="margin:0 0 1.1em 0;display:none;">Wǒ jì xià le tā de diànhuà, gěi le tā yī zhāng wǒ de míngpiàn. Tā xiǎoxīn-yìyì de shōu qǐlái, mǎnhuái xǐyuè de zǒu le.</p>
              <p style="margin:0 0 0.15em 0;">第三天中午，我收到了一个重重的包裹，发件人叫"张心悦"。我马上拨打张师傅的电话，却无人接听，给他发短信，他也不回，直到下班，仍旧没有音信。</p>
              <p class="line-pinyin" style="margin:0 0 1.1em 0;display:none;">Dì sān tiān zhōngwǔ, wǒ shōu dào le yī gè zhòngzhòng de bāoguǒ, fā jiàn rén jiào "Zhāng Xīnyuè". Wǒ mǎshàng bō dǎ Zhāng shīfu de diànhuà, què wú rén jiē tīng, gěi tā fā duǎnxìn, tā yě bù huí, zhídào xiàbān, réngjiù méiyǒu yīnxìn.</p>
              <p style="margin:0 0 0.15em 0;">我心里隐约有些不安，抱着包裹就往工地跑，找了一位工人，请他帮忙找张师傅。一会儿，浑身汗水的张师傅来了。他见了我又是道歉又是感谢，说今天特别忙，手机没电了都不知道。说着就要拆包裹，非要请我吃月饼不可。我说家里什么馅儿的月饼都有，还是赶快给女儿打电话吧。</p>
              <p class="line-pinyin" style="margin:0 0 1.1em 0;display:none;">Wǒ xīnlǐ yǐnyuē yǒuxiē bù\'ān, bào zhe bāoguǒ jiù wǎng gōngdì pǎo, zhǎo le yī wèi gōngrén, qǐng tā bāngmáng zhǎo Zhāng shīfu. Yīhuìr, húnshēn hànshuǐ de Zhāng shīfu lái le. Tā jiàn le wǒ yòu shì dàoqiàn yòu shì gǎnxiè, shuō jīntiān tèbié máng, shǒujī méi diàn le dōu bù zhīdào. Shuō zhe jiù yào chāi bāoguǒ, fēi yào qǐng wǒ chī yuèbing bùkě. Wǒ shuō jiā lǐ shénme xiànr de yuèbing dōu yǒu, háishi gǎnkuài gěi nǚ\'ér dǎ diànhuà ba.</p>
              <p style="margin:0 0 0.15em 0;">电话通了，张师傅满脸慈爱，笑得别提多灿烂了："心心，月饼爸爸收到了，……我身体好着呢，别惦记，好好工作，别给爸爸丢人啊……"讲完电话，张师傅还没忘了向我炫耀他的女儿，"要面子着呢，从来没有辜负过我的期望。"</p>
              <p class="line-pinyin" style="margin:0 0 1.1em 0;display:none;">Diànhuà tōng le, Zhāng shīfu mǎn liǎn cí\'ài, xiào de bié tí duō càn làn le: "Xīnxīn, yuèbing bàba shōu dào le, …… wǒ shēntǐ hǎo zhe ne, bié diànjì, hǎohǎo gōngzuò, bié gěi bàba diū rén a……" Jiǎng wán diànhuà, Zhāng shīfu hái méi wàng le xiàng wǒ xuànyào tā de nǚ\'ér, "yào miànzi zhe ne, cóng lái méiyǒu gūfù guò wǒ de qīwàng."</p>
              <p style="margin:0 0 0.15em 0;">看得出，女儿是他的幸福。</p>
              <p class="line-pinyin" style="margin:0 0 1.1em 0;display:none;">Kàn de chū, nǚ\'ér shì tā de xìngfú.</p>
            </div>
            <div class="line-en" style="margin-top:1.5em;padding-top:1em;border-top:1px solid var(--mist);display:none;">Early one morning on my way to work, I reached the lobby of my office building to find a man who looked like a migrant worker standing facing me. He sized me up for a moment, then swallowed whatever words had come to the tip of his tongue. I stopped and asked in puzzlement: \'Can I help you?\' Rubbing his hands together, he said hesitantly: \'There\'s something I\'d like to ask you to help me with.\'<br><br>\'Go ahead — if it\'s something I can help with, I\'ll definitely help.\' This time it was my turn to size him up: his weathered face showed an honest sincerity; his large hands were worn from excessive labor; his beard hadn\'t been shaved for at least a week; a southern accent.<br><br>Sure enough, he was from a small town in the south. He used to be a tailor; now he worked at a nearby port. His daughter was in Shanghai. Mid-Autumn Festival was coming and she wanted to send him a box of moon cakes — but he spent his days at a construction site with no way to receive deliveries, so he was hoping I could accept the parcel on his behalf.<br><br>\'That\'s easy to help with — aren\'t you afraid I\'ll eat the moon cakes when they arrive?\' I said half-jokingly. He laughed and said: \'That won\'t happen. You\'re just like my daughter — refined and educated. Any glance at you and you can tell you\'re well-read, warm-hearted, trustworthy. How could you deceive me?\' He told me his daughter had studied for a master\'s degree, had an academic qualification, and worked at a first-class company as a manager with an assistant — well and truly a backbone of the company. When he talked about his daughter, his whole face lit up with pride.<br><br>I jotted down his phone number and gave him one of my business cards. He tucked it away with the utmost care and left in high spirits.<br><br>On the third day at noon, I received a heavy parcel — the sender\'s name was \'Zhang Xinyue.\' I immediately called Carpenter Zhang, but no one picked up. I sent him a text message — no reply. By the time I left work, there was still no word from him.<br><br>Growing vaguely uneasy, I grabbed the parcel and ran to the construction site. I found a worker and asked him to help locate Carpenter Zhang. A moment later, Carpenter Zhang appeared, drenched in sweat. When he saw me, he apologized and thanked me profusely, saying he had been especially busy that day and hadn\'t even noticed his phone had run out of battery. As he spoke he was already reaching to tear open the parcel, insisting I eat some moon cakes. I said we had moon cakes of every flavor at home — he should hurry and call his daughter first.<br><br>The call went through. Carpenter Zhang\'s face filled with paternal warmth, and his smile was brilliant: \'Xinxin, Dad got the moon cakes... I\'m doing great, don\'t worry about me. Work hard — don\'t let Dad down...\' After the call, Carpenter Zhang still didn\'t forget to boast to me about his daughter: \'She cares so much about her reputation — she has never once let down my expectations.\'<br><br>You could tell: his daughter was his happiness.</div>
          </div>
        </div>
      </div>
    </div><!-- end 课文 tab -->

    <!-- 生词表 -->
    <div data-tab="vocab" class="tab-panel">
      <div class="fc-slider-wrap">
        <div class="fc-row">
          <div class="fc-slider" id="l3-fcSlider">
            <div class="fc-card active" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">月饼</div><div class="fcs-pos">n.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">yuèbing</div><div class="fcs-en">moon cake</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">清晨</div><div class="fcs-pos">n.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">qīngchén</div><div class="fcs-en">early morning</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">迎面</div><div class="fcs-pos">adv.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">yíngmiàn</div><div class="fcs-en">head-on, face to face</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">模样</div><div class="fcs-pos">n.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">múyàng</div><div class="fcs-en">appearance, look</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">打量</div><div class="fcs-pos">v.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">dǎliang</div><div class="fcs-en">to look up and down, to size up</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">番</div><div class="fcs-pos">m.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">fān</div><div class="fcs-en">measure word for effort-intensive actions</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">搓</div><div class="fcs-pos">v.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">cuō</div><div class="fcs-en">to rub with hands</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">迟疑</div><div class="fcs-pos">adj.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">chíyí</div><div class="fcs-en">hesitant</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">拜托</div><div class="fcs-pos">v.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">bàituō</div><div class="fcs-en">to ask a favor of</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">饱经沧桑</div><div class="fcs-pos">idiom</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">bǎojīng-cāngsāng</div><div class="fcs-en">to have witnessed many changes in life</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">流露</div><div class="fcs-pos">v.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">liúlù</div><div class="fcs-en">to show unintentionally, to reveal involuntarily</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">朴实</div><div class="fcs-pos">adj.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">pǔshí</div><div class="fcs-en">sincere, honest</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">过于</div><div class="fcs-pos">adv.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">guòyú</div><div class="fcs-en">too, exceedingly</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">操劳</div><div class="fcs-pos">v.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">cāoláo</div><div class="fcs-en">to work hard</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">胡须</div><div class="fcs-pos">n.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">húxū</div><div class="fcs-en">moustache, beard</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">起码</div><div class="fcs-pos">adj.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">qǐmǎ</div><div class="fcs-en">minimum, at least</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">口音</div><div class="fcs-pos">n.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">kǒuyīn</div><div class="fcs-en">accent</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">乡镇</div><div class="fcs-pos">n.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">xiāngzhèn</div><div class="fcs-en">small town</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">原先</div><div class="fcs-pos">n.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">yuánxiān</div><div class="fcs-en">former, original</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">裁缝</div><div class="fcs-pos">n.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">cáifeng</div><div class="fcs-en">tailor</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">港口</div><div class="fcs-pos">n.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">gǎngkǒu</div><div class="fcs-en">port, harbor</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">斯文</div><div class="fcs-pos">adj.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">sīwen</div><div class="fcs-en">gentle, refined</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">心眼儿</div><div class="fcs-pos">n.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">xīnyǎnr</div><div class="fcs-en">intention, heart</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">信誉</div><div class="fcs-pos">n.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">xìnyù</div><div class="fcs-en">credit, reputation</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">欺骗</div><div class="fcs-pos">v.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">qīpiàn</div><div class="fcs-en">to deceive, to cheat</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">学位</div><div class="fcs-pos">n.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">xuéwèi</div><div class="fcs-en">academic degree</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">一流</div><div class="fcs-pos">adj.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">yīliú</div><div class="fcs-en">first-class</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">主管</div><div class="fcs-pos">n.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">zhǔguǎn</div><div class="fcs-en">person in charge, manager</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">助手</div><div class="fcs-pos">n.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">zhùshǒu</div><div class="fcs-en">assistant</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">骨干</div><div class="fcs-pos">n.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">gǔgàn</div><div class="fcs-en">backbone, mainstay</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">小心翼翼</div><div class="fcs-pos">idiom</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">xiǎoxīn-yìyì</div><div class="fcs-en">with utmost care, gingerly</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">喜悦</div><div class="fcs-pos">adj.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">xǐyuè</div><div class="fcs-en">delightful, joyous</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">拨</div><div class="fcs-pos">v.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">bō</div><div class="fcs-en">to dial</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">仍旧</div><div class="fcs-pos">adv.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">réngjiù</div><div class="fcs-en">still, as ever</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">隐约</div><div class="fcs-pos">adj.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">yǐnyuē</div><div class="fcs-en">indistinct, faint, vague</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">浑身</div><div class="fcs-pos">n.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">húnshēn</div><div class="fcs-en">all over the body</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">馅儿</div><div class="fcs-pos">n.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">xiànr</div><div class="fcs-en">filling, stuffing</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">灿烂</div><div class="fcs-pos">adj.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">càn làn</div><div class="fcs-en">magnificent, splendid, bright</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">惦记</div><div class="fcs-pos">v.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">diànjì</div><div class="fcs-en">to keep thinking about, to be concerned about</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">丢人</div><div class="fcs-pos">v.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">diū rén</div><div class="fcs-en">to be disgraced, to lose face</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">炫耀</div><div class="fcs-pos">v.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">xuànyào</div><div class="fcs-en">to flaunt, to show off</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">面子</div><div class="fcs-pos">n.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">miànzi</div><div class="fcs-en">face, reputation</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">辜负</div><div class="fcs-pos">v.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">gūfù</div><div class="fcs-en">to let down, to fail to live up to</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">期望</div><div class="fcs-pos">v.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">qīwàng</div><div class="fcs-en">to hope, to expect</div></div></div></div>
          </div>
        </div>
        <div style="display:flex;align-items:center;gap:10px;margin-top:10px;">
          <button class="fc-arrow" onclick="fcNav(-1)"><svg viewBox="0 0 24 24"><polyline points="15 18 9 12 15 6"/></svg></button>
          <span class="fc-counter" id="l3-fcCounter" style="min-width:36px;text-align:center;line-height:1;">1 / 44</span>
          <button class="fc-arrow" onclick="fcNav(1)"><svg viewBox="0 0 24 24"><polyline points="9 18 15 12 9 6"/></svg></button>
        </div>
      </div>
      <a href="https://quizlet.com" target="_blank" rel="noopener"
         style="display:inline-flex;align-items:center;gap:8px;text-decoration:none;margin-bottom:1.4rem;padding:7px 14px;border:1.5px solid #e0e0ff;border-radius:8px;background:#f5f5ff;"
         onmouseover="this.style.background=\'#eaecff\';this.style.borderColor=\'#4255FF\'"
         onmouseout="this.style.background=\'#f5f5ff\';this.style.borderColor=\'#e0e0ff\'">
        <svg width="24" height="24" viewBox="0 0 36 36" fill="none"><rect width="36" height="36" rx="8" fill="#4255FF"/><text x="18" y="25" text-anchor="middle" font-family="Arial,sans-serif" font-size="18" font-weight="700" fill="#fff">Q</text></svg>
        <span style="font-size:0.78rem;font-weight:600;color:#4255FF;font-family:\'Outfit\',sans-serif;">More HSK Vocabulary on Quizlet</span>
      </a>
      <div class="vocab-grid">
        <div class="vocab-card"><div class="vocab-zh">月饼</div><div class="vocab-pinyin">yuèbing</div><div class="vocab-pos">n.</div><div class="vocab-en">moon cake</div><div class="vocab-example">中秋节要吃<em>月饼</em>。<br><span style="color:#bbb">Moon cakes are eaten at Mid-Autumn Festival.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">清晨</div><div class="vocab-pinyin">qīngchén</div><div class="vocab-pos">n.</div><div class="vocab-en">early morning</div><div class="vocab-example"><em>清晨</em>上班的路上。<br><span style="color:#bbb">On the way to work in the early morning.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">迎面</div><div class="vocab-pinyin">yíngmiàn</div><div class="vocab-pos">adv.</div><div class="vocab-en">head-on, face to face</div><div class="vocab-example"><em>迎面</em>站着一位男人。<br><span style="color:#bbb">A man stood facing me head-on.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">模样</div><div class="vocab-pinyin">múyàng</div><div class="vocab-pos">n.</div><div class="vocab-en">appearance, look</div><div class="vocab-example">农民工<em>模样</em>的男人。<br><span style="color:#bbb">A man who looked like a migrant worker.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">打量</div><div class="vocab-pinyin">dǎliang</div><div class="vocab-pos">v.</div><div class="vocab-en">to look up and down, to size up</div><div class="vocab-example">他<em>打量</em>了我一番。<br><span style="color:#bbb">He sized me up.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">番</div><div class="vocab-pinyin">fān</div><div class="vocab-pos">m.</div><div class="vocab-en">measure word for effort-intensive actions</div><div class="vocab-example">打量了我一<em>番</em>。<br><span style="color:#bbb">Sized me up once over.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">搓</div><div class="vocab-pinyin">cuō</div><div class="vocab-pos">v.</div><div class="vocab-en">to rub with hands</div><div class="vocab-example">他<em>搓</em>着手，迟疑地说。<br><span style="color:#bbb">He rubbed his hands and said hesitantly.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">迟疑</div><div class="vocab-pinyin">chíyí</div><div class="vocab-pos">adj.</div><div class="vocab-en">hesitant</div><div class="vocab-example"><em>迟疑</em>地说了一句话。<br><span style="color:#bbb">Said something hesitantly.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">拜托</div><div class="vocab-pinyin">bàituō</div><div class="vocab-pos">v.</div><div class="vocab-en">to ask a favor of</div><div class="vocab-example">有件事想<em>拜托</em>你。<br><span style="color:#bbb">There\'s something I\'d like to ask you.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">饱经沧桑</div><div class="vocab-pinyin">bǎojīng-cāngsāng</div><div class="vocab-pos">idiom</div><div class="vocab-en">to have witnessed many changes in life</div><div class="vocab-example"><em>饱经沧桑</em>的脸。<br><span style="color:#bbb">A face that had weathered many storms.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">流露</div><div class="vocab-pinyin">liúlù</div><div class="vocab-pos">v.</div><div class="vocab-en">to show unintentionally, to reveal involuntarily</div><div class="vocab-example">脸上<em>流露</em>出朴实。<br><span style="color:#bbb">His face revealed an honest sincerity.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">朴实</div><div class="vocab-pinyin">pǔshí</div><div class="vocab-pos">adj.</div><div class="vocab-en">sincere, honest</div><div class="vocab-example">流露出<em>朴实</em>。<br><span style="color:#bbb">Showed sincere honesty.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">过于</div><div class="vocab-pinyin">guòyú</div><div class="vocab-pos">adv.</div><div class="vocab-en">too, exceedingly</div><div class="vocab-example"><em>过于</em>操劳的大手。<br><span style="color:#bbb">Hands worn from excessive labor.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">操劳</div><div class="vocab-pinyin">cāoláo</div><div class="vocab-pos">v.</div><div class="vocab-en">to work hard</div><div class="vocab-example">一双过于<em>操劳</em>的大手。<br><span style="color:#bbb">Hands worn from overwork.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">胡须</div><div class="vocab-pinyin">húxū</div><div class="vocab-pos">n.</div><div class="vocab-en">moustache, beard</div><div class="vocab-example"><em>胡须</em>一个星期没刮了。<br><span style="color:#bbb">Beard unshaved for a week.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">起码</div><div class="vocab-pinyin">qǐmǎ</div><div class="vocab-pos">adj.</div><div class="vocab-en">minimum, at least</div><div class="vocab-example"><em>起码</em>一个星期没刮了。<br><span style="color:#bbb">At least a week without shaving.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">口音</div><div class="vocab-pinyin">kǒuyīn</div><div class="vocab-pos">n.</div><div class="vocab-en">accent</div><div class="vocab-example">南方<em>口音</em>。<br><span style="color:#bbb">A southern accent.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">乡镇</div><div class="vocab-pinyin">xiāngzhèn</div><div class="vocab-pos">n.</div><div class="vocab-en">small town</div><div class="vocab-example">来自南方的一个<em>乡镇</em>。<br><span style="color:#bbb">From a small town in the south.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">原先</div><div class="vocab-pinyin">yuánxiān</div><div class="vocab-pos">n.</div><div class="vocab-en">former, original</div><div class="vocab-example"><em>原先</em>是裁缝。<br><span style="color:#bbb">Used to be a tailor.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">裁缝</div><div class="vocab-pinyin">cáifeng</div><div class="vocab-pos">n.</div><div class="vocab-en">tailor</div><div class="vocab-example">原先是<em>裁缝</em>。<br><span style="color:#bbb">Was originally a tailor.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">港口</div><div class="vocab-pinyin">gǎngkǒu</div><div class="vocab-pos">n.</div><div class="vocab-en">port, harbor</div><div class="vocab-example">在旁边的<em>港口</em>干活。<br><span style="color:#bbb">Working at the nearby port.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">斯文</div><div class="vocab-pinyin">sīwen</div><div class="vocab-pos">adj.</div><div class="vocab-en">gentle, refined</div><div class="vocab-example">斯斯文文的，一看就读过书。<br><span style="color:#bbb">Refined-looking, clearly well-read.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">心眼儿</div><div class="vocab-pinyin">xīnyǎnr</div><div class="vocab-pos">n.</div><div class="vocab-en">intention, heart</div><div class="vocab-example"><em>心眼儿</em>好，守信誉。<br><span style="color:#bbb">Kind-hearted and trustworthy.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">信誉</div><div class="vocab-pinyin">xìnyù</div><div class="vocab-pos">n.</div><div class="vocab-en">credit, reputation</div><div class="vocab-example">守<em>信誉</em>，怎么会欺骗我呢？<br><span style="color:#bbb">Trustworthy — how could you deceive me?</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">欺骗</div><div class="vocab-pinyin">qīpiàn</div><div class="vocab-pos">v.</div><div class="vocab-en">to deceive, to cheat</div><div class="vocab-example">怎么会<em>欺骗</em>我呢？<br><span style="color:#bbb">How could you deceive me?</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">学位</div><div class="vocab-pinyin">xuéwèi</div><div class="vocab-pos">n.</div><div class="vocab-en">academic degree</div><div class="vocab-example">女儿有<em>学位</em>。<br><span style="color:#bbb">His daughter has a degree.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">一流</div><div class="vocab-pinyin">yīliú</div><div class="vocab-pos">adj.</div><div class="vocab-en">first-class</div><div class="vocab-example">在一家<em>一流</em>的公司上班。<br><span style="color:#bbb">Working at a first-class company.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">主管</div><div class="vocab-pinyin">zhǔguǎn</div><div class="vocab-pos">n.</div><div class="vocab-en">person in charge, manager</div><div class="vocab-example">是个<em>主管</em>，还有助手。<br><span style="color:#bbb">She\'s a manager with an assistant.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">助手</div><div class="vocab-pinyin">zhùshǒu</div><div class="vocab-pos">n.</div><div class="vocab-en">assistant</div><div class="vocab-example">还有<em>助手</em>。<br><span style="color:#bbb">She even has an assistant.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">骨干</div><div class="vocab-pinyin">gǔgàn</div><div class="vocab-pos">n.</div><div class="vocab-en">backbone, mainstay</div><div class="vocab-example">算得上是公司的<em>骨干</em>。<br><span style="color:#bbb">A backbone of the company.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">小心翼翼</div><div class="vocab-pinyin">xiǎoxīn-yìyì</div><div class="vocab-pos">idiom</div><div class="vocab-en">with utmost care, gingerly</div><div class="vocab-example"><em>小心翼翼</em>地收起来。<br><span style="color:#bbb">Tucked it away with utmost care.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">喜悦</div><div class="vocab-pinyin">xǐyuè</div><div class="vocab-pos">adj.</div><div class="vocab-en">delightful, joyous</div><div class="vocab-example">满怀<em>喜悦</em>地走了。<br><span style="color:#bbb">Left in high spirits.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">拨</div><div class="vocab-pinyin">bō</div><div class="vocab-pos">v.</div><div class="vocab-en">to dial</div><div class="vocab-example">马上<em>拨</em>打张师傅的电话。<br><span style="color:#bbb">Immediately dialed Carpenter Zhang.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">仍旧</div><div class="vocab-pinyin">réngjiù</div><div class="vocab-pos">adv.</div><div class="vocab-en">still, as ever</div><div class="vocab-example"><em>仍旧</em>没有音信。<br><span style="color:#bbb">Still no word from him.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">隐约</div><div class="vocab-pinyin">yǐnyuē</div><div class="vocab-pos">adj.</div><div class="vocab-en">indistinct, faint, vague</div><div class="vocab-example">心里<em>隐约</em>有些不安。<br><span style="color:#bbb">A vague sense of unease.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">浑身</div><div class="vocab-pinyin">húnshēn</div><div class="vocab-pos">n.</div><div class="vocab-en">all over the body</div><div class="vocab-example"><em>浑身</em>汗水的张师傅。<br><span style="color:#bbb">Carpenter Zhang, drenched in sweat.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">馅儿</div><div class="vocab-pinyin">xiànr</div><div class="vocab-pos">n.</div><div class="vocab-en">filling, stuffing</div><div class="vocab-example">什么<em>馅儿</em>的月饼都有。<br><span style="color:#bbb">Moon cakes of every flavor.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">灿烂</div><div class="vocab-pinyin">càn làn</div><div class="vocab-pos">adj.</div><div class="vocab-en">magnificent, splendid, bright</div><div class="vocab-example">笑得别提多<em>灿烂</em>了。<br><span style="color:#bbb">His smile was brilliant.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">惦记</div><div class="vocab-pinyin">diànjì</div><div class="vocab-pos">v.</div><div class="vocab-en">to keep thinking about, to be concerned about</div><div class="vocab-example">别<em>惦记</em>，好好工作。<br><span style="color:#bbb">Don\'t worry about me, work hard.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">丢人</div><div class="vocab-pinyin">diū rén</div><div class="vocab-pos">v.</div><div class="vocab-en">to be disgraced, to lose face</div><div class="vocab-example">别给爸爸<em>丢人</em>啊。<br><span style="color:#bbb">Don\'t let Dad down.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">炫耀</div><div class="vocab-pinyin">xuànyào</div><div class="vocab-pos">v.</div><div class="vocab-en">to flaunt, to show off</div><div class="vocab-example">向我<em>炫耀</em>他的女儿。<br><span style="color:#bbb">Showing off his daughter to me.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">面子</div><div class="vocab-pinyin">miànzi</div><div class="vocab-pos">n.</div><div class="vocab-en">face, reputation</div><div class="vocab-example">要<em>面子</em>着呢。<br><span style="color:#bbb">She really cares about face.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">辜负</div><div class="vocab-pinyin">gūfù</div><div class="vocab-pos">v.</div><div class="vocab-en">to let down, to fail to live up to</div><div class="vocab-example">从来没有<em>辜负</em>过我的期望。<br><span style="color:#bbb">Never once let down my expectations.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">期望</div><div class="vocab-pinyin">qīwàng</div><div class="vocab-pos">v.</div><div class="vocab-en">to hope, to expect</div><div class="vocab-example">辜负过我的<em>期望</em>。<br><span style="color:#bbb">Let down my expectations.</span></div></div>
      </div>
    </div><!-- end vocab tab -->

    <!-- 词汇详解 -->
    <div data-tab="worddetail" class="tab-panel">
      <div class="vocab-card">
        <div class="vocab-zh">饱经沧桑</div><div class="vocab-pinyin">bǎojīng-cāngsāng</div><div class="vocab-pos">idiom</div>
        <div class="vocab-en">to have gone through many of life\'s vicissitudes; a face or person that has witnessed great change (lit. "fully experienced the changes of the blue sea turning into mulberry fields")</div>
        <div class="vocab-example">
          <em>饱经沧桑</em>的脸上流露出朴实。<br>
          <span style="color:#bbb">His weathered face showed an honest sincerity.</span><br>
          这位老人<em>饱经沧桑</em>，见过了人生的起起落落。<br>
          <span style="color:#bbb">This old man had lived through many changes and seen the ups and downs of life.</span>
        </div>
      </div>
      <div class="vocab-card">
        <div class="vocab-zh">小心翼翼</div><div class="vocab-pinyin">xiǎoxīn-yìyì</div><div class="vocab-pos">idiom</div>
        <div class="vocab-en">with the utmost care; gingerly; very cautiously (lit. "careful as a bird folding its wings")</div>
        <div class="vocab-example">
          他<em>小心翼翼</em>地收起来，满怀喜悦地走了。<br>
          <span style="color:#bbb">He tucked it away with the utmost care and left in high spirits.</span><br>
          她<em>小心翼翼</em>地把那个花瓶搬到了柜子上。<br>
          <span style="color:#bbb">She gingerly moved the vase onto the cabinet.</span>
        </div>
      </div>
      <div class="vocab-card">
        <div class="vocab-zh">流露</div><div class="vocab-pinyin">liúlù</div><div class="vocab-pos">v.</div>
        <div class="vocab-en">to reveal involuntarily; to show unintentionally — unlike 表现 (to display on purpose), 流露 implies natural, unguarded revelation of feelings or character</div>
        <div class="vocab-example">
          饱经沧桑的脸上<em>流露</em>出朴实。<br>
          <span style="color:#bbb">His weathered face involuntarily revealed an honest sincerity.</span><br>
          她虽然没有说什么，但眼神里<em>流露</em>出了失望。<br>
          <span style="color:#bbb">She said nothing, but disappointment showed in her eyes.</span>
        </div>
      </div>
      <div class="vocab-card">
        <div class="vocab-zh">骨干</div><div class="vocab-pinyin">gǔgàn</div><div class="vocab-pos">n.</div>
        <div class="vocab-en">backbone; mainstay — the key person(s) a team or organization relies on</div>
        <div class="vocab-example">
          怎么也算得上是公司的<em>骨干</em>。<br>
          <span style="color:#bbb">A genuine backbone of the company by any measure.</span><br>
          他是我们团队的<em>骨干</em>，少了他，很多工作都做不下去。<br>
          <span style="color:#bbb">He is the backbone of our team — without him many tasks couldn\'t go on.</span>
        </div>
      </div>
    </div><!-- end worddetail tab -->

    <!-- 语法 -->
    <div data-tab="grammar" class="tab-panel">
      <div class="grammar-switcher">
        <button class="grammar-switch-btn active" onclick="switchGrammar(0, this)">番</button>
        <button class="grammar-switch-btn" onclick="switchGrammar(1, this)">过于</button>
        <button class="grammar-switch-btn" onclick="switchGrammar(2, this)">着呢</button>
        <button class="grammar-switch-btn" onclick="switchGrammar(3, this)">起码——至少</button>
      </div>
      <div class="grammar-panel active">
        <div class="grammar-block">
          <div class="grammar-title"><span class="grammar-num">1</span>番 · Measure Word (for effort-intensive actions)</div>
          <p class="grammar-desc">"番"，量词，有三种用法。<br><span style="color:#888;font-size:0.85em;">The measure word 番 has three distinct uses.</span></p>
          <p class="grammar-desc" style="margin-top:0.6em;">① 用于费时较多、用力较大或过程较长的动作。意思是"遍、回"。<br><span style="color:#888;font-size:0.85em;">For actions that take time, effort, or have a long process. Means "once through."</span></p>
          <div class="grammar-examples">
            <div class="grammar-ex"><div class="zh">他打量了我一番，到嘴边的话又不说了。</div><div class="en">He looked me over, then swallowed his words.</div></div>
            <div class="grammar-ex"><div class="zh">那只小鸟做了一番最后的挣扎，慢慢地躺在那里不动了。</div><div class="en">The little bird made one final struggle, then slowly lay still.</div></div>
          </div>
          <p class="grammar-desc" style="margin-top:0.6em;">② 用于心思、言语、过程等，表示次数。数词只能是"一、几"。<br><span style="color:#888;font-size:0.85em;">For thoughts, words, processes — indicating times. Only 一 or 几.</span></p>
          <div class="grammar-examples">
            <div class="grammar-ex"><div class="zh">父母的话常常在他耳边回响，他总在提醒自己不要辜负了父母的一番期望。</div><div class="en">His parents\' words often echoed in his ears; he always reminded himself not to let down their expectations.</div></div>
            <div class="grammar-ex"><div class="zh">经过了几番风雨，他才懂得人生的价值。</div><div class="en">After going through several storms, he finally understood the value of life.</div></div>
          </div>
          <p class="grammar-desc" style="margin-top:0.6em;">③ 用在动词"翻"后面，意思是"倍"。<br><span style="color:#888;font-size:0.85em;">After the verb 翻, meaning "to double."</span></p>
          <div class="grammar-examples">
            <div class="grammar-ex"><div class="zh">和五年前比，多数人的工资已经翻番了。</div><div class="en">Compared to five years ago, most people\'s salaries have doubled.</div></div>
          </div>
          <div class="grammar-block" style="margin-top:1rem;background:var(--mist);border-radius:10px;padding:1rem;">
            <div class="grammar-title" style="font-size:0.85rem;">练一练 · Practice</div>
            <p style="font-size:0.85rem;margin-bottom:0.4rem;">用"番"改写下列句子：</p>
            <ol style="font-size:0.85rem;padding-left:1.2rem;line-height:2;">
              <li>经理说，如今确定下来的改革方向，是经过了长时间认真考虑的。</li>
              <li>他汉字写得好，也是经过了好长时间艰苦付出的。</li>
              <li>他把我从上到下好好打量了一阵子，还是有些疑惑。</li>
            </ol>
          </div>
        </div>
      </div>
      <div class="grammar-panel">
        <div class="grammar-block">
          <div class="grammar-title"><span class="grammar-num">2</span>过于 · Too; Exceedingly</div>
          <p class="grammar-desc">"过于"，副词，表示超过一定限度，过分。常用格式为"过于 + 形容词/动词"。<br><span style="color:#888;font-size:0.85em;">The adverb 过于 means "excessively" or "going too far." Format: 过于 + adj./v.</span></p>
          <div class="grammar-examples">
            <div class="grammar-ex"><div class="zh">他出来得过于匆忙，居然忘了带手机。</div><div class="en">He left in such excessive haste that he forgot his phone.</div></div>
            <div class="grammar-ex"><div class="zh">进了山才发现，这里人烟过于稀少了，车开上好一阵子都见不到一个人。</div><div class="en">Entering the mountains, one finds the population far too sparse — you can drive a long while without seeing a soul.</div></div>
            <div class="grammar-ex"><div class="zh">一双过于操劳的大手。</div><div class="en">A pair of hands worn from excessive labor.</div></div>
          </div>
          <div class="grammar-block" style="margin-top:1rem;background:var(--mist);border-radius:10px;padding:1rem;">
            <div class="grammar-title" style="font-size:0.85rem;">练一练 · Practice</div>
            <p style="font-size:0.85rem;margin-bottom:0.4rem;">用"过于"完成下列句子：</p>
            <ol style="font-size:0.85rem;padding-left:1.2rem;line-height:2;">
              <li>有的登山爱好者遇险，是因为________________。</li>
              <li>不要________________，世间有很多东西比金钱更宝贵。</li>
              <li>你把他看得________________，其实他是个又简单又纯朴的人。</li>
            </ol>
          </div>
        </div>
      </div>
      <div class="grammar-panel">
        <div class="grammar-block">
          <div class="grammar-title"><span class="grammar-num">3</span>着呢 · Intensifying Particle (spoken)</div>
          <p class="grammar-desc">"着呢"，助词，表示程度深，带有夸张的语气。用于口语。<br><span style="color:#888;font-size:0.85em;">The particle 着呢 intensifies degree with an exaggerated tone. Used in spoken language.</span></p>
          <div class="grammar-examples">
            <div class="grammar-ex"><div class="zh">别看我已经年过七旬，我身体好着呢。</div><div class="en">Don\'t be fooled — even though I\'m past seventy, I\'m doing great.</div></div>
            <div class="grammar-ex"><div class="zh">他肯定发烧了，身上烫着呢。</div><div class="en">He must have a fever — he\'s burning up.</div></div>
            <div class="grammar-ex"><div class="zh">（我女儿）要面子着呢，从来没有辜负过我的期望。</div><div class="en">My daughter really cares about her reputation — she\'s never once let me down.</div></div>
          </div>
          <div class="grammar-block" style="margin-top:1rem;background:var(--mist);border-radius:10px;padding:1rem;">
            <div class="grammar-title" style="font-size:0.85rem;">练一练 · Practice</div>
            <p style="font-size:0.85rem;margin-bottom:0.4rem;">用"着呢"改写下列句子：</p>
            <ol style="font-size:0.85rem;padding-left:1.2rem;line-height:2;">
              <li>不行，干不动了，今天不干了，我太累了。</li>
              <li>天天上下班的时候，公共汽车特别挤。</li>
              <li>注意点儿，最近感冒的人多，医院里都是人。</li>
            </ol>
          </div>
        </div>
      </div>
      <div class="grammar-panel">
        <div class="grammar-block">
          <div class="grammar-title"><span class="grammar-num">4</span>起码 vs 至少 · Both mean "at least"</div>
          <p class="grammar-desc">两者都可以表示最低限度。但用法有区别。<br><span style="color:#888;font-size:0.85em;">Both express "minimum degree." Key differences:</span></p>
          <div class="grammar-pattern">起码：adj. → 可以做定语（起码的要求）；可以加"最"（最起码）<br>至少：adv. only → 不能做定语（*至少的要求 ✗）；不能加"最"（*最至少 ✗）</div>
          <div class="grammar-examples">
            <div class="grammar-ex"><div class="zh">小孩子每天起码/至少要睡九个小时。</div><div class="en">Children need to sleep at least nine hours a day.</div></div>
            <div class="grammar-ex"><div class="zh">按时上课，这是对学生起码的要求。（起码 ✓，至少 ✗）</div><div class="en">Attending class on time — this is the minimum requirement for students.</div></div>
            <div class="grammar-ex"><div class="zh">我一个月的电话费最起码也要100块钱。（最起码 ✓，*最至少 ✗）</div><div class="en">My phone bill is at least 100 yuan a month.</div></div>
          </div>
          <div class="grammar-block" style="margin-top:1rem;background:var(--mist);border-radius:10px;padding:1rem;">
            <div class="grammar-title" style="font-size:0.85rem;">做一做 · T/F</div>
            <p style="font-size:0.85rem;margin-bottom:0.4rem;">判断正误（✓/✗）：</p>
            <ol style="font-size:0.85rem;padding-left:1.2rem;line-height:2;">
              <li>我们一个星期起码要上16个小时的课。（✓）</li>
              <li>记住每天学过的生词，这是对学生至少的要求。（✗）</li>
              <li>人家帮了这么多忙，你最起码要说声谢谢吧？（✓）</li>
              <li>我看那箱苹果最至少也有十公斤。（✗）</li>
            </ol>
          </div>
        </div>
      </div>
    </div><!-- end grammar tab -->

    <!-- 练习 -->
    <div data-tab="exercise" class="tab-panel">
      <div class="exercise-block">
        <div class="exercise-type">选择题 · Multiple Choice</div>
        <div class="exercise-q">1. "我"为什么愿意帮张师傅代收包裹？</div>
        <div class="exercise-choices">
          <div class="choice" onclick="selectChoice(this, false)"><span class="choice-label">A</span>因为张师傅是她的朋友</div>
          <div class="choice" onclick="selectChoice(this, true)"><span class="choice-label">B</span>因为"我"答应了只要能帮的就一定帮</div>
          <div class="choice" onclick="selectChoice(this, false)"><span class="choice-label">C</span>因为"我"想吃月饼</div>
          <div class="choice" onclick="selectChoice(this, false)"><span class="choice-label">D</span>因为张师傅是公司的老板</div>
        </div>
      </div>
      <div class="exercise-block">
        <div class="exercise-type">选择题 · Multiple Choice</div>
        <div class="exercise-q">2. 张师傅为什么选择"我"帮他代收月饼？</div>
        <div class="exercise-choices">
          <div class="choice" onclick="selectChoice(this, false)"><span class="choice-label">A</span>因为"我"住在工地旁边</div>
          <div class="choice" onclick="selectChoice(this, false)"><span class="choice-label">B</span>因为"我"和他女儿认识</div>
          <div class="choice" onclick="selectChoice(this, true)"><span class="choice-label">C</span>因为"我"斯文、心眼儿好、守信誉</div>
          <div class="choice" onclick="selectChoice(this, false)"><span class="choice-label">D</span>因为"我"的公司离港口很远</div>
        </div>
      </div>
      <div class="exercise-block">
        <div class="exercise-type">填空题 · Fill in the Blank</div>
        <div class="exercise-q">3. 用所给词语填空（操劳 骨干 辜负 月饼 期望）：<br>大学毕业后，我到了一家贸易公司，工作努力勤奋，现在也算得上是公司的[　]了。中秋节快到了，我打算给父母送盒[　]表达心意，因为父母为我们[　]了半辈子，现在也该享享福了。我努力工作就是为了不[　]父母对我的[　]。</div>
        <div style="display:flex;align-items:center;gap:10px;margin-top:8px;flex-wrap:wrap;">
          <input id="l3-fill1" type="text" placeholder="骨干 月饼 操劳 辜负 期望" style="padding:8px 12px;border:1.5px solid var(--mist);border-radius:8px;font-family:\'Outfit\',sans-serif;font-size:0.9rem;width:280px;outline:none;">
          <button class="check-btn" onclick="checkFill(\'l3-fill1\',\'骨干\',\'l3-reveal1\')">检查</button>
        </div>
        <div id="l3-reveal1" style="display:none;margin-top:8px;padding:8px 12px;border-radius:8px;border:1.5px solid #b2dac9;font-size:0.88rem;">参考答案：公司的<strong>骨干</strong>……送盒<strong>月饼</strong>……为我们<strong>操劳</strong>了半辈子……不<strong>辜负</strong>父母对我的<strong>期望</strong>。</div>
      </div>
      <div class="exercise-block">
        <div class="exercise-type">填空题 · Fill in the Blank</div>
        <div class="exercise-q">4. 用所给词语填空（拨 起码 隐约 仍旧 拜托）：<br>昨天我[　]打好朋友小王的电话，却一直无人接听，直到今天早上[　]没有他的音信。我心中[　]有种不安的感觉，便给小王单位打了个电话，想[　]他的同事查看一下小王的情况，同事告诉我，小王的手机坏了，[　]要一个星期才能修好，知道小王没事，我就放心了。</div>
        <div style="display:flex;align-items:center;gap:10px;margin-top:8px;flex-wrap:wrap;">
          <input id="l3-fill2" type="text" placeholder="拨 仍旧 隐约 拜托 起码" style="padding:8px 12px;border:1.5px solid var(--mist);border-radius:8px;font-family:\'Outfit\',sans-serif;font-size:0.9rem;width:280px;outline:none;">
          <button class="check-btn" onclick="checkFill(\'l3-fill2\',\'拨\',\'l3-reveal2\')">检查</button>
        </div>
        <div id="l3-reveal2" style="display:none;margin-top:8px;padding:8px 12px;border-radius:8px;border:1.5px solid #b2dac9;font-size:0.88rem;">参考答案：我<strong>拨</strong>打电话……<strong>仍旧</strong>没有……<strong>隐约</strong>有种不安……<strong>拜托</strong>他的同事……<strong>起码</strong>要一个星期。</div>
      </div>
      <div class="exercise-block">
        <div class="exercise-type">写作题 · Writing</div>
        <div class="exercise-q">5. 这篇课文讲述了发生在中秋节前的一个感人的故事。请参考以下提示，把课文缩写成300字左右的短文。</div>
        <ul style="font-size:0.88rem;padding-left:1.4rem;margin:8px 0 0 0;line-height:2;">
          <li>时间、地点、人物（"我"、张师傅、女儿）</li>
          <li>张师傅的外貌特征</li>
          <li>事情的起因：代收月饼</li>
          <li>事情的发展：包裹到了，联系不上张师傅</li>
          <li>结局：父女通话，张师傅的骄傲</li>
        </ul>
      </div>
      <div class="exercise-block">
        <div class="exercise-type">句型练习 · Pattern Practice</div>
        <div class="exercise-q">6. 仿照例句，用下列格式造句：<br><em>我马上拨打张师傅的电话，却无人接听，给他发短信，他也不回，直到下班，仍旧没有音信。</em></div>
        <div style="font-size:0.88rem;margin-top:8px;line-height:2.2;padding:10px 14px;background:var(--mist);border-radius:8px;">
          我________________________________，却________________________________，给他________________________________，他也________________________________，直到________________________________，仍旧________________________________。
        </div>
      </div>
    </div><!-- end exercise tab -->

    <!-- 更多 -->
    <div data-tab="culture" class="tab-panel">
      <div class="grammar-block">
        <div class="grammar-title">病句类型：词语误用（二）</div>
        <p class="grammar-desc">词语误用的情况还包括实词之间的误用、虚词的误用和滥用，以及感情色彩、语体色彩的误用。</p>
        <table style="width:100%;border-collapse:collapse;font-size:0.85rem;margin-top:0.8rem;">
          <thead>
            <tr style="background:var(--mist);">
              <th style="padding:8px 10px;text-align:left;border:1px solid #ddd;">病句</th>
              <th style="padding:8px 10px;text-align:left;border:1px solid #ddd;">错误分析</th>
            </tr>
          </thead>
          <tbody>
            <tr><td style="padding:8px 10px;border:1px solid #ddd;">*整整一夜，我几乎没睡，一直在回想他的话，可是不管他说什么，我也<em>想</em>自己没有错误。</td><td style="padding:8px 10px;border:1px solid #ddd;">实词误用。"想"应换用"认为"或"觉得"。</td></tr>
            <tr><td style="padding:8px 10px;border:1px solid #ddd;">*咱们毕业都25年了，一直没见你，你下次给我写信时，随信<em>奉上</em>你的照片。</td><td style="padding:8px 10px;border:1px solid #ddd;">语体词误用。"奉"是敬体词，只能用于下级对上级，应改为"寄上"。</td></tr>
            <tr><td style="padding:8px 10px;border:1px solid #ddd;">*我<em>大概</em>每天下班后都要去书店买书，然后再回家。</td><td style="padding:8px 10px;border:1px solid #ddd;">副词误用。"大概"应换为"几乎"。</td></tr>
            <tr><td style="padding:8px 10px;border:1px solid #ddd;">*大企业招聘主要看实力，没有实力的话，<em>无论</em>来自很有名的大学，人家也不要你。</td><td style="padding:8px 10px;border:1px solid #ddd;">带关联词的固定搭配误用。应改为"无论来自多么有名的大学"。</td></tr>
            <tr><td style="padding:8px 10px;border:1px solid #ddd;">*这个酒店服务质量之差<em>有口皆碑</em>，可是天晚了，我们只好住进去。</td><td style="padding:8px 10px;border:1px solid #ddd;">成语误用。"有口皆碑"是褒义词，应改为"尽人皆知"。</td></tr>
          </tbody>
        </table>
        <div class="grammar-block" style="margin-top:1rem;background:var(--mist);border-radius:10px;padding:1rem;">
          <div class="grammar-title" style="font-size:0.85rem;">练一练 · Practice</div>
          <p style="font-size:0.85rem;margin-bottom:0.5rem;">指出下列句子的错误并提出修改建议：</p>
          <ol style="font-size:0.85rem;padding-left:1.2rem;line-height:2.2;">
            <li>因为是冬天，没有什么人到山上来玩儿。我站在山顶上，空气很清凉。<br><input type="text" style="width:100%;max-width:420px;padding:5px 8px;border:1px solid #ccc;border-radius:6px;font-size:0.85rem;margin-top:2px;" placeholder="错误分析与修改…"></li>
            <li>我的腿受伤了，不能去滑雪，我很眼红我的朋友们。<br><input type="text" style="width:100%;max-width:420px;padding:5px 8px;border:1px solid #ccc;border-radius:6px;font-size:0.85rem;margin-top:2px;" placeholder="错误分析与修改…"></li>
            <li>到北京来的时候，我带来一个好玩儿的U盘，偶然，我的同屋也带来一个。<br><input type="text" style="width:100%;max-width:420px;padding:5px 8px;border:1px solid #ccc;border-radius:6px;font-size:0.85rem;margin-top:2px;" placeholder="错误分析与修改…"></li>
            <li>有一天在书店，我看了一个小偷，偷了本书。<br><input type="text" style="width:100%;max-width:420px;padding:5px 8px;border:1px solid #ccc;border-radius:6px;font-size:0.85rem;margin-top:2px;" placeholder="错误分析与修改…"></li>
            <li>如果不修建这些水利工程，遇到严重的水旱灾害，其后果不可思议。<br><input type="text" style="width:100%;max-width:420px;padding:5px 8px;border:1px solid #ccc;border-radius:6px;font-size:0.85rem;margin-top:2px;" placeholder="错误分析与修改…"></li>
          </ol>
        </div>
      </div>
      <div class="grammar-block" style="margin-top:1.2rem;">
        <div class="grammar-title">词汇（1）—— 表示动作的词语</div>
        <table style="width:100%;border-collapse:collapse;font-size:0.85rem;margin-top:0.8rem;">
          <thead>
            <tr style="background:var(--mist);">
              <th style="padding:8px 10px;text-align:left;border:1px solid #ddd;">词</th>
              <th style="padding:8px 10px;text-align:left;border:1px solid #ddd;">例句</th>
            </tr>
          </thead>
          <tbody>
            <tr><td style="padding:8px 10px;border:1px solid #ddd;font-weight:600;">搂</td><td style="padding:8px 10px;border:1px solid #ddd;">孩子亲热地搂着妈妈。</td></tr>
            <tr><td style="padding:8px 10px;border:1px solid #ddd;font-weight:600;">拾</td><td style="padding:8px 10px;border:1px solid #ddd;">把地上的纸拾起来。</td></tr>
            <tr><td style="padding:8px 10px;border:1px solid #ddd;font-weight:600;">拧</td><td style="padding:8px 10px;border:1px solid #ddd;">把毛巾拧干。</td></tr>
            <tr><td style="padding:8px 10px;border:1px solid #ddd;font-weight:600;">投掷</td><td style="padding:8px 10px;border:1px solid #ddd;">他正在准备投掷铅球。</td></tr>
            <tr><td style="padding:8px 10px;border:1px solid #ddd;font-weight:600;">飘扬</td><td style="padding:8px 10px;border:1px solid #ddd;">红旗迎风飘扬。</td></tr>
            <tr><td style="padding:8px 10px;border:1px solid #ddd;font-weight:600;">绣</td><td style="padding:8px 10px;border:1px solid #ddd;">她很喜欢绣花儿。</td></tr>
            <tr><td style="padding:8px 10px;border:1px solid #ddd;font-weight:600;">泼</td><td style="padding:8px 10px;border:1px solid #ddd;">泼水节时人们会互相泼水表示祝福。</td></tr>
            <tr><td style="padding:8px 10px;border:1px solid #ddd;font-weight:600;">牵</td><td style="padding:8px 10px;border:1px solid #ddd;">两个人手牵手。</td></tr>
            <tr><td style="padding:8px 10px;border:1px solid #ddd;font-weight:600;">掐</td><td style="padding:8px 10px;border:1px solid #ddd;">请不要掐花儿。</td></tr>
            <tr><td style="padding:8px 10px;border:1px solid #ddd;font-weight:600;">削</td><td style="padding:8px 10px;border:1px solid #ddd;">吃苹果时最好削皮。</td></tr>
          </tbody>
        </table>
      </div>
      <div class="grammar-block" style="margin-top:1.2rem;">
        <div class="grammar-title">词汇（2）—— 表亲属称谓的词语</div>
        <table style="width:100%;border-collapse:collapse;font-size:0.85rem;margin-top:0.8rem;">
          <thead>
            <tr style="background:var(--mist);">
              <th style="padding:8px 10px;text-align:left;border:1px solid #ddd;">问题</th>
              <th style="padding:8px 10px;text-align:left;border:1px solid #ddd;">答案</th>
            </tr>
          </thead>
          <tbody>
            <tr><td style="padding:8px 10px;border:1px solid #ddd;">父亲的哥哥称为伯父，伯父的妻子怎样称呼？</td><td style="padding:8px 10px;border:1px solid #ddd;font-weight:600;">伯母</td></tr>
            <tr><td style="padding:8px 10px;border:1px solid #ddd;">哥哥的妻子怎样称呼？</td><td style="padding:8px 10px;border:1px solid #ddd;font-weight:600;">嫂子</td></tr>
            <tr><td style="padding:8px 10px;border:1px solid #ddd;">妻子的母亲怎样称呼？</td><td style="padding:8px 10px;border:1px solid #ddd;font-weight:600;">岳母</td></tr>
            <tr><td style="padding:8px 10px;border:1px solid #ddd;">弟兄或其他同辈男性亲属的儿子怎样称呼？</td><td style="padding:8px 10px;border:1px solid #ddd;font-weight:600;">侄子</td></tr>
          </tbody>
        </table>
      </div>
    </div><!-- end culture tab -->

  </div><!-- end content-area L3 -->
  </div><!-- end lesson-content data-lesson="3" -->'''

content_new = re.sub(pattern_l3, replacement_l3, content, flags=re.DOTALL)

if content_new == content:
    print('ERROR: no replacement')
else:
    print('L3 replaced successfully')
    with open(HTML_PATH, 'w', encoding='utf-8') as f:
        f.write(content_new)
    print('Done writing file.')
