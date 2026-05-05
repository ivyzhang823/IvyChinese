#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
replace_l8.py
Replaces the stub Lesson 8 block in HSK6/hsk6_01-10.html
with the real Lesson 8 content: 遇见原来的我
"""

import re
import sys

SRC = r"D:\Claude_CODE\IvyChinese\HSK\HSK6\hsk6_01-10.html"

# ---------------------------------------------------------------------------
# Real Lesson 8 HTML
# ---------------------------------------------------------------------------
REAL_L8 = r"""<div class="lesson-header" id="lesson-header-8" data-lesson="8" data-watermark="八" style="display:none">
    <div class="lesson-meta">
      <button class="lesson-tag" onclick="showIndex()">
        <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"/></svg>
        HSK 6
      </button>
      <span class="lesson-tag-num">第八课 · Lesson 08</span>
    </div>
    <h1>遇见原来的我</h1>
    <p style="font-size:0.9rem;color:var(--gold);margin-bottom:0.3rem;letter-spacing:0.02em;">Yùjiàn yuánlái de wǒ</p>
    <p class="lesson-subtitle">Meeting the old me</p>
  </div>

  <div class="lesson-content" data-lesson="8" style="display:none">
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
      <div class="dialogue-block" id="l8-block1">
        <div class="dialogue-header">
          <div class="dialogue-title-wrap">
            <div class="dialogue-title-row">
              <span class="dialogue-title">课文 · 遇见原来的我</span>
              <button class="dh-play-btn" id="l8-dhBtn1" onclick="dhPlay('l8-audioEl1','l8-dhBtn1')">
                <svg id="l8-dhIcon1" viewBox="0 0 24 24"><polygon points="5 3 19 12 5 21 5 3"/></svg>
              </button>
              <span style="flex:1;"></span>
              <div class="toggle-btns">
                <button class="toggle-btn" onclick="toggleBlock(this,'pinyin','l8-block1')"><span class="dot"></span>拼音</button>
                <button class="toggle-btn" onclick="toggleBlock(this,'en','l8-block1')"><span class="dot"></span>En</button>
              </div>
            </div>
            <span class="dialogue-title-en">Meeting the old me</span>
          </div>
          <audio id="l8-audioEl1" src="" onended="dhEnded('l8-audioEl1','l8-dhBtn1','l8-dhIcon1')" ontimeupdate="dhUpdate('l8-audioEl1')"></audio>
        </div>
        <div class="dialogue-line" style="display:block;">
          <div class="line-content" style="font-size:0.88em;">
            <div class="line-zh" style="line-height:1.9;">
              <p style="margin:0 0 0.15em 0;">如果有一天，你看到自己婴儿时期的一张照片，你能认出自己吗？</p>
              <p class="line-pinyin" style="margin:0 0 1.1em 0;display:none;">Rúguǒ yǒu yītiān, nǐ kàndào zìjǐ yīng'ér shíqī de yī zhāng zhàopiàn, nǐ néng rènchū zìjǐ ma?</p>
              <p style="margin:0 0 0.15em 0;">也许你会一下子认出自己，因为你觉得你一直都是你。但实际上，从拍照片的那一刻起，你的身上已经发生了翻天覆地的变化。你的皮肤自那以来已经更新130多次了。你的酒窝不见了，5岁那年，你从高处往下蹦，跌倒了，脸上留下了一道疤，而现在这块疤已经被掩盖了。与照片相比，你现在增加了两三岁的重量。</p>
              <p class="line-pinyin" style="margin:0 0 1.1em 0;display:none;">Yěxǔ nǐ huì yīxiàzi rènchū zìjǐ, yīnwèi nǐ juéde nǐ yīzhí dōu shì nǐ. Dàn shíjì shàng, cóng pāi zhàopiàn de nà yīkè qǐ, nǐ de shēnshàng yǐjīng fāshēngle fāntiān-fùdì de biànhuà. Nǐ de pífū zì nà yǐlái yǐjīng gēngxīn 130 duō cì le. Nǐ de jiǔwō bùjiàn le, wǔ suì nà nián, nǐ cóng gāochù wǎng xià bèng, diēdǎo le, liǎnshàng liúxià le yī dào bā, ér xiànzài zhè kuài bā yǐjīng bèi yǎngài le. Yǔ zhàopiàn xiāngbǐ, nǐ xiànzài zēngjiāle liǎng sān suì de zhòngliàng.</p>
              <p style="margin:0 0 0.15em 0;">如果你确信你就是你，不管发生什么变化，那么，照片里的婴儿到底是不是过去的你？是现在的你，还是一个不同的过去的你？如果是过去的你，那么有多少个过去的你？是不是还会有更多的不同的你？你用电脑处理了一张你50岁时的照片，对你而言，就像看着一个陌生人。</p>
              <p class="line-pinyin" style="margin:0 0 1.1em 0;display:none;">Rúguǒ nǐ quèxìn nǐ jiùshì nǐ, bùguǎn fāshēng shénme biànhuà, nàme, zhàopiàn lǐ de yīng'ér dàodǐ shì bùshì guòqù de nǐ? Shì xiànzài de nǐ, háishì yīgè bùtóng de guòqù de nǐ? Rúguǒ shì guòqù de nǐ, nàme yǒu duōshao gè guòqù de nǐ? Shì bùshì hái huì yǒu gèng duō de bùtóng de nǐ? Nǐ yòng diànnǎo chǔlǐ le yī zhāng nǐ wǔshí suì shí de zhàopiàn, duì nǐ ér yán, jiù xiàng kànzhe yīgè mòshēngrén.</p>
              <p style="margin:0 0 0.15em 0;">有关本体的问题，困扰了哲学家2500多年。什么是本体？这里说的本体就是我们的思想及身体。</p>
              <p class="line-pinyin" style="margin:0 0 1.1em 0;display:none;">Yǒuguān běntǐ de wèntí, kùnrǎo le zhéxuéjiā 2500 duō nián. Shénme shì běntǐ? Zhèlǐ shuō de běntǐ jiùshì wǒmen de sīxiǎng jí shēntǐ.</p>
              <p style="margin:0 0 0.15em 0;">赫拉克利特把自我比喻为一条河，河流流动时会呈现出不同的状态，但它始终是固有的那条河。他将自己的观点阐述为：不管你变化了多少，始终只有一个你。</p>
              <p class="line-pinyin" style="margin:0 0 1.1em 0;display:none;">Hèlākèlìtè bǎ zìwǒ bǐyù wéi yī tiáo hé, héliú liúdòng shí huì chéngxiàn chū bùtóng de zhuàngtài, dàn tā shǐzhōng shì gùyǒu de nà tiáo hé. Tā jiāng zìjǐ de guāndiǎn chénshù wéi: bùguǎn nǐ biànhuà le duōshao, shǐzhōng zhǐyǒu yīgè nǐ.</p>
              <p style="margin:0 0 0.15em 0;">大卫·休谟不同意"连续的自我"的观点，他是这样描述自己的见解的："我们的思想，是连续不断的认知组成的演变过程。"而你可以推测，婴儿大卫与成年大卫的呈现并非完全相同。</p>
              <p class="line-pinyin" style="margin:0 0 1.1em 0;display:none;">Dàwèi·Xiūmò bù tóngyì "liánxù de zìwǒ" de guāndiǎn, tā shì zhèyàng miáoshù zìjǐ de jiànjiě de: "Wǒmen de sīxiǎng, shì liánxù bùduàn de rèzhī zǔchéng de yǎnbiàn guòchéng." Ér nǐ kěyǐ tuīcè, yīng'ér Dàwèi yǔ chéngnián Dàwèi de chéngxiàn bìngfēi wánquán xiāngtóng.</p>
              <p style="margin:0 0 0.15em 0;">哲学家们对本体的问题各抒己见，我们却在追问一些更实际的问题，假如谜题就是对的，那么从现在开始，10年后你就会成为另一个人，你还需要遵守现在的你做出的承诺吗？或者说，一个触犯了法律的人，还应该受到对这个行为的惩罚吗？</p>
              <p class="line-pinyin" style="margin:0 0 1.1em 0;display:none;">Zhéxuéjiāmen duì běntǐ de wèntí gèshū-jǐjiàn, wǒmen què zài zhuīwèn yīxiē gèng shíjì de wèntí, jiǎrú mítí jiùshì duì de, nàme cóng xiànzài kāishǐ, 10 nián hòu nǐ jiù huì chéngwéi lìng yīgè rén, nǐ hái xūyào zūnshǒu xiànzài de nǐ zuòchū de chéngnuò ma? Huòzhě shuō, yīgè chùfàn le fǎlǜ de rén, hái yīnggāi shòudào duì zhège xíngwéi de chéngfá ma?</p>
              <p style="margin:0 0 0.15em 0;">我们每个人都会发生变化，譬如，你整形，你因为过度忧郁而吃药，你做心、肺及其他器官移植手术，这些都会进而改变你的面貌、情绪和行为，还是你吗？</p>
              <p class="line-pinyin" style="margin:0 0 1.1em 0;display:none;">Wǒmen měi gèrén dōu huì fāshēng biànhuà, pìrú, nǐ zhěngxíng, nǐ yīnwèi guòdù yōuyù ér chīyào, nǐ zuò xīn, fèi jí qítā qìguān yízhí shǒushù, zhèxiē dōu huì jìn'ér gǎibiàn nǐ de miànmào, qíngxù hé xíngwéi, hái shì nǐ ma?</p>
              <p style="margin:0 0 0.15em 0;">德里克·帕菲特有一个极端空前绝后的假设，例如将他的大脑一分为二，移植进另外两个身体中，两个人分别从昏迷中清醒过来，都会认为："我是德里克！"但是，德里克也不可能只是其中的一个。由此，他得出结论："个人的本体并不是最重要的事情。"</p>
              <p class="line-pinyin" style="margin:0 0 1.1em 0;display:none;">Délǐkè·Pàfēitè yǒu yīgè jíduān kōngqián-juéhòu de jiǎshè, lìrú jiāng tā de dànǎo yī fēn wéi èr, yízhí jìn lìngwài liǎng gè shēntǐ zhōng, liǎng gè rén fēnbié cóng hūnmí zhōng qīngxǐng guòlái, dōu huì rènwéi: "Wǒ shì Délǐkè!" Dànshì, Délǐkè yě bù kěnéng zhǐshì qízhōng de yīgè. Yóucǐ, tā dé chū jiélùn: "Gèrén de běntǐ bìng bù shì zuì zhòngyào de shìqing."</p>
              <p style="margin:0 0 0.15em 0;">不确你说，对这个问题，这是哲学家的言论，学习后我十分迷惑，我们不会纠结于本体的思索，如果谜题就是对的，那么从现在开始，10年后你就会成为另一个人，那简直就是自己的性命已经更换了，我们只想无忧无虑地过日子，可是，有朝一天，你醒了，感觉今天的我不像原来的我，而后遇见的是一个崭新的我了呢？</p>
              <p class="line-pinyin" style="margin:0 0 1.1em 0;display:none;">Bù què nǐ shuō, duì zhège wèntí, zhè shì zhéxuéjiā de yánlùn, xuéxí hòu wǒ shífēn míhuò, wǒmen bù huì jiūjié yú běntǐ de sīsuǒ, rúguǒ mítí jiùshì duì de, nàme cóng xiànzài kāishǐ, 10 nián hòu nǐ jiù huì chéngwéi lìng yīgè rén, nà jiǎnzhí jiùshì zìjǐ de xìngmìng yǐjīng gēnghuàn le, wǒmen zhǐ xiǎng wúyōu-wúlǜ de guò rìzi, kěshì, yǒu zhāo yītiān, nǐ xǐng le, gǎnjué jīntiān de wǒ bù xiàng yuánlái de wǒ, ér hòu yùjiàn de shì yīgè zhǎnxīn de wǒ le ne?</p>
            </div>
            <div class="line-en" style="margin-top:1.5em;padding-top:1em;border-top:1px solid var(--mist);display:none;">If one day you were to look at a photograph of yourself as a baby, would you be able to recognise yourself?<br><br>Perhaps you would recognise yourself straight away, because you feel you have always been you. But in truth, from the moment that photograph was taken, your body has undergone earth-shaking changes. Your skin has renewed itself more than 130 times since then. Your dimples have disappeared. When you were five you jumped off something high, fell over, and left a scar on your face — yet now that scar is gone, covered over. Compared with the photograph, you now carry two or three extra years' worth of weight.<br><br>If you are certain that you are you, whatever changes may occur, then is the baby in the photograph really the you of the past? Is it the present you, or a different, past you? If it is a past you, how many past yous are there? Could there be even more different versions of you? You use a computer to process a photograph of yourself aged fifty, and to you it is like looking at a stranger.<br><br>Questions about personal identity have troubled philosophers for more than 2,500 years. What is personal identity? The "identity" spoken of here refers to our minds and bodies taken together.<br><br>Heraclitus compared the self to a river — a river in flow presents different states, yet it remains inherently the same river. He stated his view as: no matter how much you change, there is always only one you.<br><br>David Hume disagreed with the notion of a "continuous self." He described his own understanding this way: "Our thoughts are an evolving process made up of an unbroken stream of perceptions." And you can infer that the infant David and the adult David are by no means identical in their presentation.<br><br>Philosophers each express their own views on the question of personal identity, while we find ourselves asking rather more practical questions. If the puzzle is correct, then starting from now, in ten years you will have become a different person — do you still need to keep the promises your current self has made? Or again: should a person who has broken the law still be punished for that act?<br><br>Every one of us will change. For instance, you may have cosmetic surgery; you may take medication because of severe depression; you may undergo a heart, lung, or other organ transplant. All of these will in turn alter your appearance, emotions, and behaviour — are you still you?<br><br>Derek Parfit put forward a hypothesis that was extreme and utterly unprecedented: imagine splitting his brain in two and transplanting each half into a separate body. Both individuals would come out of their coma and each would think, "I am Derek!" Yet Derek could not possibly be just one of them. From this he drew his conclusion: "Personal identity is not what matters."<br><br>I'm not sure about you, but when it comes to this question — these are philosophers' theories, and after studying them I am thoroughly confused. We are not going to agonise over questions of personal identity. If the puzzle is right, then starting from now, in ten years you will have become another person — which amounts to saying that our very lives have already been replaced. All we want is to live our days carefree and at ease. But what if one day you wake up, and you feel that today's me is not the me I used to be, and the one you then meet is a brand-new me?</div>
          </div>
        </div>
      </div>
    </div><!-- end 课文 tab -->

    <!-- 生词表 -->
    <div data-tab="vocab" class="tab-panel">
      <div class="fc-slider-wrap">
        <div class="fc-row">
          <div class="fc-slider" id="l8-fcSlider">
            <div class="fc-card active" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">婴儿</div><div class="fcs-pos">n.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">yīng'ér</div><div class="fcs-en">baby, infant</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">翻天覆地</div><div class="fcs-pos">idiom</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">fāntiān-fùdì</div><div class="fcs-en">earth-shaking, tremendous</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">更新</div><div class="fcs-pos">v.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">gēngxīn</div><div class="fcs-en">to regenerate, to renew</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">酒窝</div><div class="fcs-pos">n.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">jiǔwō</div><div class="fcs-en">dimple</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">蹦</div><div class="fcs-pos">v.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">bèng</div><div class="fcs-en">to leap, to jump</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">跌</div><div class="fcs-pos">v.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">diē</div><div class="fcs-en">to fall, to tumble</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">疤</div><div class="fcs-pos">n.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">bā</div><div class="fcs-en">scar</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">掩盖</div><div class="fcs-pos">v.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">yǎngài</div><div class="fcs-en">to cover, to conceal</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">大脑</div><div class="fcs-pos">n.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">dànǎo</div><div class="fcs-en">brain</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">确信</div><div class="fcs-pos">v.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">quèxìn</div><div class="fcs-en">to be certain, to be sure</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">比喻</div><div class="fcs-pos">v.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">bǐyù</div><div class="fcs-en">to draw an analogy, to use a metaphor</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">呈现</div><div class="fcs-pos">v.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">chéngxiàn</div><div class="fcs-en">to present (a certain appearance), to appear</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">固有</div><div class="fcs-pos">adj.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">gùyǒu</div><div class="fcs-en">intrinsic, inherent</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">肺</div><div class="fcs-pos">n.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">fèi</div><div class="fcs-en">lung</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">陈述</div><div class="fcs-pos">v.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">chénshù</div><div class="fcs-en">to state, to explain</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">见解</div><div class="fcs-pos">n.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">jiànjiě</div><div class="fcs-en">opinion, understanding</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">演变</div><div class="fcs-pos">v.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">yǎnbiàn</div><div class="fcs-en">to change, to evolve</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">推测</div><div class="fcs-pos">v.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">tuīcè</div><div class="fcs-en">to infer, to conjecture, to guess</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">譬如</div><div class="fcs-pos">conj.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">pìrú</div><div class="fcs-en">for example, such as</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">各抒己见</div><div class="fcs-pos">idiom</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">gèshū-jǐjiàn</div><div class="fcs-en">each one expresses his/her own views</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">触犯</div><div class="fcs-pos">v.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">chùfàn</div><div class="fcs-en">to offend, to violate</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">惩罚</div><div class="fcs-pos">v.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">chéngfá</div><div class="fcs-en">to punish, to penalize</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">忧郁</div><div class="fcs-pos">adj.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">yōuyù</div><div class="fcs-en">melancholy, heavy-hearted</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">器官</div><div class="fcs-pos">n.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">qìguān</div><div class="fcs-en">organ, apparatus</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">移植</div><div class="fcs-pos">v.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">yízhí</div><div class="fcs-en">to transplant, to graft</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">面貌</div><div class="fcs-pos">n.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">miànmào</div><div class="fcs-en">face, features</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">极端</div><div class="fcs-pos">adj.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">jíduān</div><div class="fcs-en">extreme</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">空前绝后</div><div class="fcs-pos">idiom</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">kōngqián-juéhòu</div><div class="fcs-en">unprecedented and unrepeatable</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">昏迷</div><div class="fcs-pos">v.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">hūnmí</div><div class="fcs-en">to faint, to be in a coma</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">清醒</div><div class="fcs-pos">v.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">qīngxǐng</div><div class="fcs-en">to regain consciousness, to come to</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">言论</div><div class="fcs-pos">n.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">yánlùn</div><div class="fcs-en">opinion on public affairs, speech</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">学说</div><div class="fcs-pos">n.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">xuéshuō</div><div class="fcs-en">theory, doctrine</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">遥远</div><div class="fcs-pos">adj.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">yáoyuǎn</div><div class="fcs-en">far, distant, remote</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">陷入</div><div class="fcs-pos">v.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">xiànrù</div><div class="fcs-en">to be immersed in, to be lost in</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">思索</div><div class="fcs-pos">v.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">sīsuǒ</div><div class="fcs-en">to think deeply, to ponder</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">设想</div><div class="fcs-pos">v.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">shèxiǎng</div><div class="fcs-en">to imagine, to conceive of</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">性命</div><div class="fcs-pos">n.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">xìngmìng</div><div class="fcs-en">life</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">无忧无虑</div><div class="fcs-pos">idiom</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">wúyōu-wúlǜ</div><div class="fcs-en">carefree, free from anxieties</div></div></div></div>
            <div class="fc-card" onclick="flipCard(this)"><div class="fc-card-inner"><div class="fc-front"><div class="fcs-zh">崭新</div><div class="fcs-pos">adj.</div><div class="fcs-hint">tap to flip</div></div><div class="fc-back"><div class="fcs-pinyin">zhǎnxīn</div><div class="fcs-en">brand-new, wholly new</div></div></div></div>
          </div>
        </div>
        <div style="display:flex;align-items:center;gap:10px;margin-top:10px;">
          <button class="fc-arrow" onclick="fcNav(-1)"><svg viewBox="0 0 24 24"><polyline points="15 18 9 12 15 6"/></svg></button>
          <span class="fc-counter" id="l8-fcCounter" style="min-width:36px;text-align:center;line-height:1;">1 / 40</span>
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
        <div class="vocab-card"><div class="vocab-zh">婴儿</div><div class="vocab-pinyin">yīng'ér</div><div class="vocab-pos">n.</div><div class="vocab-en">baby, infant</div><div class="vocab-example">你看到自己<em>婴儿</em>时期的一张照片。<br><span style="color:#bbb">A photo of yourself as a baby.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">翻天覆地</div><div class="vocab-pinyin">fāntiān-fùdì</div><div class="vocab-pos">idiom</div><div class="vocab-en">earth-shaking, tremendous</div><div class="vocab-example">你的身上已经发生了<em>翻天覆地</em>的变化。<br><span style="color:#bbb">Earth-shaking changes have occurred in your body.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">更新</div><div class="vocab-pinyin">gēngxīn</div><div class="vocab-pos">v.</div><div class="vocab-en">to regenerate, to renew</div><div class="vocab-example">你的皮肤已经<em>更新</em>130多次了。<br><span style="color:#bbb">Your skin has renewed itself over 130 times.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">酒窝</div><div class="vocab-pinyin">jiǔwō</div><div class="vocab-pos">n.</div><div class="vocab-en">dimple</div><div class="vocab-example">你的<em>酒窝</em>不见了。<br><span style="color:#bbb">Your dimples have disappeared.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">蹦</div><div class="vocab-pinyin">bèng</div><div class="vocab-pos">v.</div><div class="vocab-en">to leap, to jump</div><div class="vocab-example">从高处往下<em>蹦</em>，跌倒了。<br><span style="color:#bbb">Jumped off something high and fell.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">跌</div><div class="vocab-pinyin">diē</div><div class="vocab-pos">v.</div><div class="vocab-en">to fall, to tumble</div><div class="vocab-example">往下蹦，<em>跌</em>倒了。<br><span style="color:#bbb">Jumped and tumbled down.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">疤</div><div class="vocab-pinyin">bā</div><div class="vocab-pos">n.</div><div class="vocab-en">scar</div><div class="vocab-example">脸上留下了一道<em>疤</em>。<br><span style="color:#bbb">A scar was left on the face.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">掩盖</div><div class="vocab-pinyin">yǎngài</div><div class="vocab-pos">v.</div><div class="vocab-en">to cover, to conceal</div><div class="vocab-example">这块疤已经被<em>掩盖</em>了。<br><span style="color:#bbb">The scar has been covered over.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">大脑</div><div class="vocab-pinyin">dànǎo</div><div class="vocab-pos">n.</div><div class="vocab-en">brain</div><div class="vocab-example">将他的<em>大脑</em>一分为二。<br><span style="color:#bbb">Split his brain in two.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">确信</div><div class="vocab-pinyin">quèxìn</div><div class="vocab-pos">v.</div><div class="vocab-en">to be certain, to be sure</div><div class="vocab-example">如果你<em>确信</em>你就是你。<br><span style="color:#bbb">If you are certain that you are you.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">比喻</div><div class="vocab-pinyin">bǐyù</div><div class="vocab-pos">v.</div><div class="vocab-en">to draw an analogy, to use a metaphor</div><div class="vocab-example">把自我<em>比喻</em>为一条河。<br><span style="color:#bbb">Compared the self to a river.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">呈现</div><div class="vocab-pinyin">chéngxiàn</div><div class="vocab-pos">v.</div><div class="vocab-en">to present, to appear</div><div class="vocab-example">河流流动时会<em>呈现</em>出不同的状态。<br><span style="color:#bbb">A river presents different states as it flows.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">固有</div><div class="vocab-pinyin">gùyǒu</div><div class="vocab-pos">adj.</div><div class="vocab-en">intrinsic, inherent</div><div class="vocab-example">始终是<em>固有</em>的那条河。<br><span style="color:#bbb">Always the same inherent river.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">肺</div><div class="vocab-pinyin">fèi</div><div class="vocab-pos">n.</div><div class="vocab-en">lung</div><div class="vocab-example">做心、<em>肺</em>及其他器官移植手术。<br><span style="color:#bbb">Heart, lung and other organ transplant surgery.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">陈述</div><div class="vocab-pinyin">chénshù</div><div class="vocab-pos">v.</div><div class="vocab-en">to state, to explain</div><div class="vocab-example">他将自己的观点<em>阐述</em>为。<br><span style="color:#bbb">He stated his view as.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">见解</div><div class="vocab-pinyin">jiànjiě</div><div class="vocab-pos">n.</div><div class="vocab-en">opinion, understanding</div><div class="vocab-example">描述自己的<em>见解</em>。<br><span style="color:#bbb">Describe his own understanding.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">演变</div><div class="vocab-pinyin">yǎnbiàn</div><div class="vocab-pos">v.</div><div class="vocab-en">to change, to evolve</div><div class="vocab-example">连续不断的认知组成的<em>演变</em>过程。<br><span style="color:#bbb">An evolving process of continuous perceptions.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">推测</div><div class="vocab-pinyin">tuīcè</div><div class="vocab-pos">v.</div><div class="vocab-en">to infer, to conjecture, to guess</div><div class="vocab-example">你可以<em>推测</em>，婴儿大卫与成年大卫并非完全相同。<br><span style="color:#bbb">You can infer that infant David and adult David are not identical.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">譬如</div><div class="vocab-pinyin">pìrú</div><div class="vocab-pos">conj.</div><div class="vocab-en">for example, such as</div><div class="vocab-example"><em>譬如</em>，你整形，你因为忧郁而吃药。<br><span style="color:#bbb">For example, you have surgery or take medication.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">各抒己见</div><div class="vocab-pinyin">gèshū-jǐjiàn</div><div class="vocab-pos">idiom</div><div class="vocab-en">each one expresses his/her own views</div><div class="vocab-example">哲学家们对本体的问题<em>各抒己见</em>。<br><span style="color:#bbb">Philosophers each express their own views on identity.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">触犯</div><div class="vocab-pinyin">chùfàn</div><div class="vocab-pos">v.</div><div class="vocab-en">to offend, to violate</div><div class="vocab-example">一个<em>触犯</em>了法律的人。<br><span style="color:#bbb">A person who has violated the law.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">惩罚</div><div class="vocab-pinyin">chéngfá</div><div class="vocab-pos">v.</div><div class="vocab-en">to punish, to penalize</div><div class="vocab-example">受到对这个行为的<em>惩罚</em>。<br><span style="color:#bbb">Punished for this act.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">忧郁</div><div class="vocab-pinyin">yōuyù</div><div class="vocab-pos">adj.</div><div class="vocab-en">melancholy, heavy-hearted</div><div class="vocab-example">因为过度<em>忧郁</em>而吃药。<br><span style="color:#bbb">Taking medication because of severe depression.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">器官</div><div class="vocab-pinyin">qìguān</div><div class="vocab-pos">n.</div><div class="vocab-en">organ, apparatus</div><div class="vocab-example">心、肺及其他<em>器官</em>移植手术。<br><span style="color:#bbb">Heart, lung, and other organ transplants.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">移植</div><div class="vocab-pinyin">yízhí</div><div class="vocab-pos">v.</div><div class="vocab-en">to transplant, to graft</div><div class="vocab-example">做器官<em>移植</em>手术。<br><span style="color:#bbb">Undergo an organ transplant operation.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">面貌</div><div class="vocab-pinyin">miànmào</div><div class="vocab-pos">n.</div><div class="vocab-en">face, features</div><div class="vocab-example">改变你的<em>面貌</em>、情绪和行为。<br><span style="color:#bbb">Alter your appearance, emotions, and behaviour.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">极端</div><div class="vocab-pinyin">jíduān</div><div class="vocab-pos">adj.</div><div class="vocab-en">extreme</div><div class="vocab-example">一个<em>极端</em>空前绝后的假设。<br><span style="color:#bbb">An extreme, unprecedented hypothesis.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">空前绝后</div><div class="vocab-pinyin">kōngqián-juéhòu</div><div class="vocab-pos">idiom</div><div class="vocab-en">unprecedented and unrepeatable</div><div class="vocab-example">极端<em>空前绝后</em>的假设。<br><span style="color:#bbb">Unprecedented and unrepeatable hypothesis.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">昏迷</div><div class="vocab-pinyin">hūnmí</div><div class="vocab-pos">v.</div><div class="vocab-en">to faint, to be in a coma</div><div class="vocab-example">从<em>昏迷</em>中清醒过来。<br><span style="color:#bbb">Coming out of a coma.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">清醒</div><div class="vocab-pinyin">qīngxǐng</div><div class="vocab-pos">v.</div><div class="vocab-en">to regain consciousness, to come to</div><div class="vocab-example">从昏迷中<em>清醒</em>过来。<br><span style="color:#bbb">Regaining consciousness from a coma.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">言论</div><div class="vocab-pinyin">yánlùn</div><div class="vocab-pos">n.</div><div class="vocab-en">opinion on public affairs, speech</div><div class="vocab-example">这是哲学家的<em>言论</em>。<br><span style="color:#bbb">These are the philosophers' words.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">学说</div><div class="vocab-pinyin">xuéshuō</div><div class="vocab-pos">n.</div><div class="vocab-en">theory, doctrine</div><div class="vocab-example">哲学家的<em>学说</em>令人迷惑。<br><span style="color:#bbb">The philosophers' theories are confusing.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">遥远</div><div class="vocab-pinyin">yáoyuǎn</div><div class="vocab-pos">adj.</div><div class="vocab-en">far, distant, remote</div><div class="vocab-example"><em>遥远</em>的将来。<br><span style="color:#bbb">The distant future.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">陷入</div><div class="vocab-pinyin">xiànrù</div><div class="vocab-pos">v.</div><div class="vocab-en">to be immersed in, to be lost in</div><div class="vocab-example"><em>陷入</em>沉思。<br><span style="color:#bbb">Lost in deep thought.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">思索</div><div class="vocab-pinyin">sīsuǒ</div><div class="vocab-pos">v.</div><div class="vocab-en">to think deeply, to ponder</div><div class="vocab-example">纠结于本体的<em>思索</em>。<br><span style="color:#bbb">Agonising over questions of identity.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">设想</div><div class="vocab-pinyin">shèxiǎng</div><div class="vocab-pos">v.</div><div class="vocab-en">to imagine, to conceive of</div><div class="vocab-example"><em>设想</em>一下10年后的你。<br><span style="color:#bbb">Imagine the you of ten years from now.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">性命</div><div class="vocab-pinyin">xìngmìng</div><div class="vocab-pos">n.</div><div class="vocab-en">life</div><div class="vocab-example">自己的<em>性命</em>已经更换了。<br><span style="color:#bbb">One's very life has been replaced.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">无忧无虑</div><div class="vocab-pinyin">wúyōu-wúlǜ</div><div class="vocab-pos">idiom</div><div class="vocab-en">carefree, free from anxieties</div><div class="vocab-example">我们只想<em>无忧无虑</em>地过日子。<br><span style="color:#bbb">All we want is to live carefree days.</span></div></div>
        <div class="vocab-card"><div class="vocab-zh">崭新</div><div class="vocab-pinyin">zhǎnxīn</div><div class="vocab-pos">adj.</div><div class="vocab-en">brand-new, wholly new</div><div class="vocab-example">遇见的是一个<em>崭新</em>的我。<br><span style="color:#bbb">What you meet is a brand-new me.</span></div></div>
      </div>
    </div><!-- end vocab tab -->

    <!-- 词汇详解 -->
    <div data-tab="worddetail" class="tab-panel">
      <div class="vocab-card">
        <div class="vocab-zh">各抒己见</div><div class="vocab-pinyin">gèshū-jǐjiàn</div><div class="vocab-pos">idiom</div>
        <div class="vocab-en">Each person freely expresses their own opinion. Literal breakdown: 各=each, 抒=to express, 己=oneself, 见=view. Used positively in formal discussions and debates.</div>
        <div class="vocab-example">
          哲学家们对本体的问题<em>各抒己见</em>，没有统一的结论。<br>
          <span style="color:#bbb">Philosophers each express their own views on identity, with no unified conclusion.</span><br>
          在讨论会上，同学们<em>各抒己见</em>，气氛十分活跃。<br>
          <span style="color:#bbb">At the discussion, students each voiced their opinions and the atmosphere was very lively.</span><br>
          他们三个人对这件事<em>各抒己见</em>，最终达成了共识。<br>
          <span style="color:#bbb">The three of them each expressed their views and eventually reached a consensus.</span>
        </div>
      </div>
      <div class="vocab-card">
        <div class="vocab-zh">空前绝后</div><div class="vocab-pinyin">kōngqián-juéhòu</div><div class="vocab-pos">idiom</div>
        <div class="vocab-en">Unique, unprecedented and unrepeatable; one of a kind. Literal: 空前=unprecedented, 绝后=no successor. Often used ironically or humorously in casual speech.</div>
        <div class="vocab-example">
          德里克·帕菲特有一个极端<em>空前绝后</em>的假设。<br>
          <span style="color:#bbb">Derek Parfit put forward a hypothesis that was extreme and utterly unprecedented.</span><br>
          这场演出可以说是<em>空前绝后</em>，令观众叹为观止。<br>
          <span style="color:#bbb">This performance was truly one of a kind, leaving the audience in awe.</span><br>
          这种奇特的设计，可谓<em>空前绝后</em>，无人能及。<br>
          <span style="color:#bbb">This unique design is unprecedented and unmatched by anyone.</span>
        </div>
      </div>
      <div class="vocab-card">
        <div class="vocab-zh">翻天覆地</div><div class="vocab-pinyin">fāntiān-fùdì</div><div class="vocab-pos">idiom</div>
        <div class="vocab-en">Earth-shaking, world-changing; describes enormous change. Literal: heaven and earth turned upside down.</div>
        <div class="vocab-example">
          你的身上已经发生了<em>翻天覆地</em>的变化。<br>
          <span style="color:#bbb">Earth-shaking changes have already occurred in your body.</span><br>
          改革开放以来，中国发生了<em>翻天覆地</em>的变化。<br>
          <span style="color:#bbb">Since the reform and opening-up, China has undergone earth-shaking changes.</span><br>
          这场科技革命带来了<em>翻天覆地</em>的社会变革。<br>
          <span style="color:#bbb">This technological revolution brought about earth-shaking social transformation.</span>
        </div>
      </div>
      <div class="vocab-card">
        <div class="vocab-zh">无忧无虑</div><div class="vocab-pinyin">wúyōu-wúlǜ</div><div class="vocab-pos">idiom</div>
        <div class="vocab-en">Carefree, free from all worries. Often used to describe an ideal state of mind or the happiness of childhood.</div>
        <div class="vocab-example">
          我们只想<em>无忧无虑</em>地过日子。<br>
          <span style="color:#bbb">All we want is to live our days carefree and at ease.</span><br>
          童年时代的我们<em>无忧无虑</em>，天真烂漫。<br>
          <span style="color:#bbb">In childhood we were carefree and innocent.</span><br>
          退休后，他终于过上了<em>无忧无虑</em>的生活。<br>
          <span style="color:#bbb">After retiring, he finally lived a carefree life.</span>
        </div>
      </div>

      <!-- 词语辨析 -->
      <div class="vocab-card" style="margin-top:1.5em;">
        <div class="vocab-zh" style="font-size:1rem;font-weight:700;margin-bottom:0.4em;">词语辨析 · 极端 vs 极度</div>
        <div class="vocab-pos">Both indicate a very high degree or extreme level</div>
        <div class="vocab-en">
          <strong>极端 (jíduān)</strong> — adj./n./adv.: more often modifies negative concepts; can be used as a noun (走向极端); can modify verbs (极端地认为).<br>
          <strong>极度 (jídù)</strong> — usually an adverb modifying adjectives or verbs; cannot be used as a noun.
        </div>
        <div class="vocab-example">
          他的做法太<em>极端</em>，让我们无法认同。<br>
          <span style="color:#bbb">His approach is too extreme for us to accept.</span><br>
          这种<em>极端</em>的想法不可取。<br>
          <span style="color:#bbb">This extreme way of thinking is unacceptable.</span><br>
          <em>极度</em>疲劳之后，他感到<em>极度</em>舒缓。<br>
          <span style="color:#bbb">After extreme exhaustion, he felt extremely relaxed.</span><br>
          她对这件事<em>极度</em>关心。<br>
          <span style="color:#bbb">She is extremely concerned about this matter.</span>
        </div>
      </div>
    </div><!-- end worddetail tab -->

    <!-- 语法 -->
    <div data-tab="grammar" class="tab-panel">
      <div class="grammar-switcher">
        <button class="grammar-switch-btn active" onclick="switchGrammar(0, this)">对……而言</button>
        <button class="grammar-switch-btn" onclick="switchGrammar(1, this)">有关</button>
        <button class="grammar-switch-btn" onclick="switchGrammar(2, this)">不确你说</button>
      </div>
      <div class="grammar-panel active">
        <div class="grammar-block">
          <div class="grammar-title"><span class="grammar-num">1</span>对……而言 · From the perspective of / Speaking of</div>
          <p class="grammar-desc">"对……而言"，正式书面表达，表示"从……的角度来说"。口语中常用"对……说"或"对……来说"替代。<br><span style="color:#888;font-size:0.85em;">A formal written expression meaning "from the perspective of / speaking of." Informal equivalents: 对……说 / 对……来说.</span></p>
          <div class="grammar-pattern">对 + [person/thing] + 而言, + [comment]</div>
          <div class="grammar-examples">
            <div class="grammar-ex"><div class="zh">对当今的中国而言，经济发展必须坚持走可持续发展的道路。</div><div class="en">For today's China, economic development must stay on the path of sustainable development.</div></div>
            <div class="grammar-ex"><div class="zh">对年轻的我们而言，面对困难更是件快乐的事情——那意味着我们在成长。</div><div class="en">For us young people, facing difficulties is even a joyful thing — it means we are growing.</div></div>
            <div class="grammar-ex"><div class="zh">你用电脑处理了一张你50岁时的照片，对你而言，就像看着一个陌生人。</div><div class="en">You used a computer to process a photo of yourself at 50 — to you, it was like looking at a stranger.</div></div>
          </div>
          <div class="grammar-block" style="margin-top:1.2em;">
            <div class="grammar-title" style="font-size:0.9em;">练一练 · 用"对……而言"完成句子</div>
            <div class="grammar-examples">
              <div class="grammar-ex"><div class="zh">1. 对这位老科学家而言，______________________。</div></div>
              <div class="grammar-ex"><div class="zh">2. ______________________，对她而言，最重要的还是家人。</div></div>
            </div>
          </div>
        </div>
      </div>
      <div class="grammar-panel">
        <div class="grammar-block">
          <div class="grammar-title"><span class="grammar-num">2</span>有关 · To have to do with / Related to</div>
          <p class="grammar-desc">"有关"可作动词，意思是"与……有关"；也可作形容词，意思是"相关的、有关的"。比"关于"更正式。<br><span style="color:#888;font-size:0.85em;">As a verb: "to have to do with / to be related to." As an adjective/adjunct: "related, relevant." More formal than 关于.</span></p>
          <div class="grammar-pattern">Usage ①: 有关 + [topic] + 的 + [noun]　→　relating to / about</div>
          <div class="grammar-examples">
            <div class="grammar-ex"><div class="zh">有关本体的问题，困扰了哲学家2500多年。</div><div class="en">Questions about personal identity have troubled philosophers for more than 2,500 years.</div></div>
            <div class="grammar-ex"><div class="zh">他们研究了手中有关组织的文字记载。</div><div class="en">They studied the written records about the organisation in their possession.</div></div>
          </div>
          <div class="grammar-pattern" style="margin-top:1em;">Usage ②: [topic] + 有关 + (的) → verb phrase meaning "involves/pertains to"</div>
          <div class="grammar-examples">
            <div class="grammar-ex"><div class="zh">这件事与你无关，你不必担心。</div><div class="en">This matter has nothing to do with you — don't worry about it.</div></div>
            <div class="grammar-ex"><div class="zh">这个问题有关我们每一个人的利益。</div><div class="en">This issue involves the interests of each and every one of us.</div></div>
          </div>
          <div class="grammar-block" style="margin-top:1.2em;">
            <div class="grammar-title" style="font-size:0.9em;">练一练 · 用"有关"或"关于"填空</div>
            <div class="grammar-examples">
              <div class="grammar-ex"><div class="zh">1. ______科学发展的话题，他总有说不完的话。</div></div>
              <div class="grammar-ex"><div class="zh">2. 这份报告______公司未来发展的方向。</div></div>
            </div>
          </div>
        </div>
      </div>
      <div class="grammar-panel">
        <div class="grammar-block">
          <div class="grammar-title"><span class="grammar-num">3</span>不确你说 · I'm not sure about you, but… (parenthetical)</div>
          <p class="grammar-desc">"不确你说"是插入语/评论短语，表示"我不知道你怎么想，但对我来说……"，用来表达说话人的主观看法。类似表达：依我看、我想、说实在的、说真的、依我说。<br><span style="color:#888;font-size:0.85em;">"不确你说" is a parenthetical expression meaning "I'm not sure about you, but..." used to introduce the speaker's subjective view. Similar: 依我看, 我想, 说实在的, 说真的.</span></p>
          <div class="grammar-pattern">不确你说，[+ speaker's personal view / reaction]</div>
          <div class="grammar-examples">
            <div class="grammar-ex"><div class="zh">不确你说，对待这个问题，我是这样想的。</div><div class="en">I'm not sure about you, but this is how I think about this question.</div></div>
            <div class="grammar-ex"><div class="zh">不确你说，书法方面，本人虽称不上"家"，但水平还是有一定的。</div><div class="en">I'm not sure about you, but in calligraphy, I may not call myself an expert, yet I do have some ability.</div></div>
            <div class="grammar-ex"><div class="zh">依我看，无论你怎么选择，都不太可能找到称心如意的答案。</div><div class="en">In my view, no matter what you choose, you're unlikely to find a perfectly satisfying answer.</div></div>
          </div>
          <div class="grammar-block" style="margin-top:1.2em;">
            <div class="grammar-title" style="font-size:0.9em;">练一练 · 用"不确你说"或"依我看"完成句子</div>
            <div class="grammar-examples">
              <div class="grammar-ex"><div class="zh">1. ______，这部电影拍得十分精彩，值得一看。</div></div>
              <div class="grammar-ex"><div class="zh">2. ______，想要成功，最重要的是坚持不懈。</div></div>
            </div>
          </div>
        </div>
      </div>
    </div><!-- end grammar tab -->

    <!-- 练习 -->
    <div data-tab="exercise" class="tab-panel">
      <div class="exercise-block">
        <div class="exercise-type">练习一 · Word Formation</div>
        <div class="exercise-q">模仿例子，写出更多相关词语。<br><span style="color:#888;font-size:0.88em;">Example: 更新 → 更改、更换、更替、更变</span></div>
        <div style="font-size:0.88em;line-height:2.2;margin:10px 0;">
          <div>比喻：<input type="text" placeholder="比较、比方…" style="padding:4px 8px;border:1.5px solid var(--mist);border-radius:6px;font-family:'Outfit',sans-serif;font-size:0.9rem;width:180px;outline:none;" /></div>
          <div>思索：<input type="text" placeholder="思考、思维…" style="padding:4px 8px;border:1.5px solid var(--mist);border-radius:6px;font-family:'Outfit',sans-serif;font-size:0.9rem;width:180px;outline:none;" /></div>
          <div>推：<input type="text" placeholder="推测、推断…" style="padding:4px 8px;border:1.5px solid var(--mist);border-radius:6px;font-family:'Outfit',sans-serif;font-size:0.9rem;width:180px;outline:none;" /></div>
          <div>崭：<input type="text" placeholder="崭新、崭露…" style="padding:4px 8px;border:1.5px solid var(--mist);border-radius:6px;font-family:'Outfit',sans-serif;font-size:0.9rem;width:180px;outline:none;" /></div>
        </div>
      </div>
      <div class="exercise-block">
        <div class="exercise-type">练习二 · Sentence Completion</div>
        <div class="exercise-q">用所给词语或结构完成句子。</div>
        <div style="font-size:0.88em;line-height:2.4;margin:10px 0;">
          <div>1. 如果明天天气不好，___________，（那么）</div>
          <div>2. 目睹同学觉得汉字没那么难，可___________，（对……而言）</div>
          <div>3. 同学们___________，（各抒己见）</div>
          <div>4. 经过一段时间的观察，专家们___________，（推测）</div>
          <div>5. 青藏高原海拔很高，氧气稀薄，环境___________，（极端）</div>
        </div>
      </div>
      <div class="exercise-block">
        <div class="exercise-type">练习三 · Fill in the Blank</div>
        <div class="exercise-q">选择合适的词语填空：各抒己见、见解、无忧无虑、思索、比喻、通缉</div>
        <div style="font-size:0.88em;line-height:2;margin:8px 0 12px 0;">
          今天讨论课的话题是"幸福是什么？"同学们经过一番
          <input id="l8-fill1" type="text" placeholder="思索" style="padding:4px 8px;border:1.5px solid var(--mist);border-radius:6px;font-family:'Outfit',sans-serif;font-size:0.9rem;width:70px;outline:none;">
          之后，有人把幸福
          <input id="l8-fill2" type="text" placeholder="比喻" style="padding:4px 8px;border:1.5px solid var(--mist);border-radius:6px;font-family:'Outfit',sans-serif;font-size:0.9rem;width:70px;outline:none;">
          为盛开的花朵，虽然美好，却短暂；也有人认为幸福是
          <input id="l8-fill3" type="text" placeholder="无忧无虑" style="padding:4px 8px;border:1.5px solid var(--mist);border-radius:6px;font-family:'Outfit',sans-serif;font-size:0.9rem;width:80px;outline:none;">
          地生活；同学们
          <input id="l8-fill4" type="text" placeholder="各抒己见" style="padding:4px 8px;border:1.5px solid var(--mist);border-radius:6px;font-family:'Outfit',sans-serif;font-size:0.9rem;width:80px;outline:none;">
          ，每个人对幸福有不同的
          <input id="l8-fill5" type="text" placeholder="见解" style="padding:4px 8px;border:1.5px solid var(--mist);border-radius:6px;font-family:'Outfit',sans-serif;font-size:0.9rem;width:70px;outline:none;">
          。
        </div>
        <div style="display:flex;gap:10px;flex-wrap:wrap;margin-top:4px;">
          <button class="check-btn" onclick="checkFill('l8-fill1','思索','l8-rev1')">检查①</button>
          <button class="check-btn" onclick="checkFill('l8-fill2','比喻','l8-rev2')">检查②</button>
          <button class="check-btn" onclick="checkFill('l8-fill3','无忧无虑','l8-rev3')">检查③</button>
          <button class="check-btn" onclick="checkFill('l8-fill4','各抒己见','l8-rev4')">检查④</button>
          <button class="check-btn" onclick="checkFill('l8-fill5','见解','l8-rev5')">检查⑤</button>
        </div>
        <div id="l8-rev1" style="display:none;margin-top:8px;padding:8px 12px;border-radius:8px;border:1.5px solid #b2dac9;font-size:0.88rem;">①参考答案：<strong>思索</strong></div>
        <div id="l8-rev2" style="display:none;margin-top:4px;padding:8px 12px;border-radius:8px;border:1.5px solid #b2dac9;font-size:0.88rem;">②参考答案：<strong>比喻</strong></div>
        <div id="l8-rev3" style="display:none;margin-top:4px;padding:8px 12px;border-radius:8px;border:1.5px solid #b2dac9;font-size:0.88rem;">③参考答案：<strong>无忧无虑</strong></div>
        <div id="l8-rev4" style="display:none;margin-top:4px;padding:8px 12px;border-radius:8px;border:1.5px solid #b2dac9;font-size:0.88rem;">④参考答案：<strong>各抒己见</strong></div>
        <div id="l8-rev5" style="display:none;margin-top:4px;padding:8px 12px;border-radius:8px;border:1.5px solid #b2dac9;font-size:0.88rem;">⑤参考答案：<strong>见解</strong></div>
      </div>
      <div class="exercise-block">
        <div class="exercise-type">练习四 · Sentence Ordering</div>
        <div class="exercise-q">把下面的句子按照正确顺序重新组合成段落。</div>
        <div style="font-size:0.88em;line-height:2;margin:10px 0;">
          A. 她一个人坐在这里<br>
          B. 她想起去年的现在，她是和男朋友两个人坐在这地方<br>
          C. 她当时心情是多么激动和欢快呀<br>
          D. 心里装着一块冰<br>
          E. 可是一年后的今天
        </div>
        <div style="font-size:0.88em;color:#888;margin-top:6px;">参考顺序：B → C → E → A → D</div>
      </div>
      <div class="exercise-block">
        <div class="exercise-type">练习五 · Summary Table</div>
        <div class="exercise-q">根据提示，简述课文主要内容。</div>
        <div style="font-size:0.88em;margin:10px 0;">
          <table style="width:100%;border-collapse:collapse;line-height:1.8;">
            <thead><tr style="border-bottom:2px solid var(--mist);"><th style="text-align:left;padding:6px 10px;">问题</th><th style="text-align:left;padding:6px 10px;">提示词</th><th style="text-align:left;padding:6px 10px;">你的回答</th></tr></thead>
            <tbody>
              <tr style="border-bottom:1px solid var(--mist);"><td style="padding:6px 10px;">从婴儿时期到现在，"你"发生了什么变化？</td><td style="padding:6px 10px;">皮肤、酒窝、疤、婴儿、现在、以后</td><td style="padding:6px 10px;"><textarea style="width:100%;min-height:60px;padding:6px;border:1.5px solid var(--mist);border-radius:6px;font-size:0.85rem;resize:vertical;" placeholder="请写出你的回答…"></textarea></td></tr>
              <tr><td style="padding:6px 10px;">到底有多少个"你"？哲学家怎么说？</td><td style="padding:6px 10px;">赫拉克利特、休谟、帕菲特、不同见解</td><td style="padding:6px 10px;"><textarea style="width:100%;min-height:60px;padding:6px;border:1.5px solid var(--mist);border-radius:6px;font-size:0.85rem;resize:vertical;" placeholder="请写出你的回答…"></textarea></td></tr>
            </tbody>
          </table>
        </div>
      </div>
      <div class="exercise-block">
        <div class="exercise-type">写作题 · Writing</div>
        <div class="exercise-q">"今天的你跟昨天的你是同一个人吗？"这是一个关于本体的哲学问题，哲学家们有不同的见解。请参考练习五，把课文编写成300字左右的短文。</div>
        <textarea style="width:100%;min-height:120px;padding:10px 14px;border:1.5px solid var(--mist);border-radius:8px;font-family:'Outfit',sans-serif;font-size:0.9rem;margin-top:10px;resize:vertical;" placeholder="在这里写你的短文…"></textarea>
      </div>
    </div><!-- end exercise tab -->

    <!-- 更多 -->
    <div data-tab="culture" class="tab-panel">
      <div class="culture-block">
        <div class="culture-head">
          <div class="culture-tag">🏮 反义词</div>
          <button class="en-toggle" onclick="toggleEn(this)">En</button>
        </div>
        <div class="culture-title">词汇：熟悉下列反义词<span class="pinyin">Antonym Pairs</span></div>
        <div class="culture-zh">
          <table style="width:100%;border-collapse:collapse;font-size:0.88em;line-height:1.8;">
            <thead>
              <tr style="border-bottom:2px solid var(--mist);">
                <th style="text-align:left;padding:6px 10px;">词 A</th>
                <th style="text-align:left;padding:6px 10px;">词 B</th>
                <th style="text-align:left;padding:6px 10px;">词 A</th>
                <th style="text-align:left;padding:6px 10px;">词 B</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom:1px solid var(--mist);"><td style="padding:6px 10px;">动荡</td><td style="padding:6px 10px;">稳定</td><td style="padding:6px 10px;">停滞</td><td style="padding:6px 10px;">发展</td></tr>
              <tr style="border-bottom:1px solid var(--mist);"><td style="padding:6px 10px;">服从</td><td style="padding:6px 10px;">违抗</td><td style="padding:6px 10px;">推翻</td><td style="padding:6px 10px;">建立</td></tr>
              <tr style="border-bottom:1px solid var(--mist);"><td style="padding:6px 10px;">复活</td><td style="padding:6px 10px;">灭亡</td><td style="padding:6px 10px;">延期</td><td style="padding:6px 10px;">提前</td></tr>
              <tr style="border-bottom:1px solid var(--mist);"><td style="padding:6px 10px;">高潮</td><td style="padding:6px 10px;">低潮</td><td style="padding:6px 10px;">制止</td><td style="padding:6px 10px;">允许</td></tr>
              <tr style="border-bottom:1px solid var(--mist);"><td style="padding:6px 10px;">高尚</td><td style="padding:6px 10px;">低俗</td><td style="padding:6px 10px;">混浊</td><td style="padding:6px 10px;">清澈</td></tr>
              <tr style="border-bottom:1px solid var(--mist);"><td style="padding:6px 10px;">合并</td><td style="padding:6px 10px;">解散</td><td style="padding:6px 10px;">简陋</td><td style="padding:6px 10px;">豪华</td></tr>
              <tr><td style="padding:6px 10px;">敏锐</td><td style="padding:6px 10px;">迟钝</td><td style="padding:6px 10px;"></td><td style="padding:6px 10px;"></td></tr>
            </tbody>
          </table>
        </div>
        <div class="culture-en">Antonym pairs from HSK 6 Level vocabulary — study these opposite-meaning words to strengthen your lexical range.</div>
      </div>
      <div class="culture-block" style="margin-top:1.5em;">
        <div class="culture-head">
          <div class="culture-tag">🏮 运用</div>
          <button class="en-toggle" onclick="toggleEn(this)">En</button>
        </div>
        <div class="culture-title">写一写 · Application Writing<span class="pinyin">Shū yī shū</span></div>
        <div class="culture-zh">
          <p style="font-size:0.88em;line-height:1.8;">"今天的你跟昨天的你是同一个人吗？"这是一个关于本体的哲学问题，哲学家们有不同的见解。这篇课文介绍了不同的哲学家对本体的认识和观点。请参考练习五，把课文编写成300字左右的短文。</p>
        </div>
        <div class="culture-en">
          "Are you today the same person as you were yesterday?" This is a philosophical question about personal identity, and philosophers have different views. This text introduces various philosophical perspectives on selfhood. Refer to Exercise 5 and write a short essay of about 300 characters summarising the main ideas.
        </div>
      </div>
    </div><!-- end culture tab -->

  </div><!-- end content-area L8 -->
  </div><!-- end lesson-content data-lesson="8" -->"""

# ---------------------------------------------------------------------------
# Do the replacement
# ---------------------------------------------------------------------------
def main():
    with open(SRC, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = (
        r'<div class="lesson-header" id="lesson-header-8".*?'
        r'</div><!-- end lesson-content data-lesson="8" -->'
    )

    new_content, count = re.subn(pattern, REAL_L8, content, flags=re.DOTALL)

    if count == 0:
        print("ERROR: Pattern not found — no replacement made.", file=sys.stderr)
        sys.exit(1)

    print(f"Replaced {count} block(s).")

    with open(SRC, "w", encoding="utf-8") as f:
        f.write(new_content)

    # Verify
    with open(SRC, "r", encoding="utf-8") as f:
        verify = f.read()

    if "遇见原来的我" in verify:
        print("SUCCESS: target string found in output file.")
    else:
        print("ERROR: verification string not found in output file!", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
