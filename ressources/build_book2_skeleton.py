"""Build hsk6_11-20.html skeleton by cloning hsk6_01-10.html and stripping all lesson content."""
import re
from pathlib import Path

SRC = Path('D:/Claude_CODE/IvyChinese/HSK/HSK6/hsk6_01-10.html')
DST = Path('D:/Claude_CODE/IvyChinese/HSK/HSK6/hsk6_11-20.html')

CHINESE_NUMS_FULL = ['一','二','三','四','五','六','七','八','九','十',
                    '十一','十二','十三','十四','十五','十六','十七','十八','十九','二十']

src = SRC.read_text(encoding='utf-8')

# ============================================================
# 1. Strip lesson-content blocks and replace with empty stubs
#    Iterate in reverse so regex doesn't conflict across blocks
# ============================================================
for n in range(10, 0, -1):
    new_n = n + 10  # 1→11, ..., 10→20
    pattern = re.compile(
        rf'  <div class="lesson-content" data-lesson="{n}".*?</div><!-- end lesson-content data-lesson="{n}" -->',
        re.DOTALL
    )
    stub = (
        f'  <div class="lesson-content" data-lesson="{new_n}" style="display:none">\n'
        f'    <p style="text-align:center;padding:3rem 1rem;color:#888;font-size:1.1rem;">敬请期待 · Coming soon</p>\n'
        f'  </div><!-- end lesson-content data-lesson="{new_n}" -->'
    )
    matches = pattern.findall(src)
    assert len(matches) == 1, f'L{n} content: expected 1 match, got {len(matches)}'
    src = pattern.sub(stub, src, count=1)

# ============================================================
# 2. Replace lesson-header blocks with stubs (L11-L20)
# ============================================================
for n in range(10, 0, -1):
    new_n = n + 10
    cn_num = CHINESE_NUMS_FULL[new_n - 1]
    pattern = re.compile(
        rf'  <div class="lesson-header" id="lesson-header-{n}".*?<p class="lesson-subtitle">.*?</p>\s*</div>',
        re.DOTALL
    )
    stub = (
        f'  <div class="lesson-header" id="lesson-header-{new_n}" data-lesson="{new_n}" data-watermark="{cn_num}" style="display:none">\n'
        f'    <div class="lesson-meta">\n'
        f'      <button class="lesson-tag" onclick="showIndex()">\n'
        f'        <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"/></svg>\n'
        f'        HSK 6\n'
        f'      </button>\n'
        f'      <span class="lesson-tag-num">第{cn_num}课 · Lesson {new_n}</span>\n'
        f'    </div>\n'
        f'    <h1>第{cn_num}课</h1>\n'
        f'    <p style="font-size:0.9rem;color:var(--gold);margin-bottom:0.3rem;letter-spacing:0.02em;">Coming soon</p>\n'
        f'    <p class="lesson-subtitle">Coming soon</p>\n'
        f'  </div>'
    )
    matches = pattern.findall(src)
    assert len(matches) == 1, f'L{n} header: expected 1 match, got {len(matches)}'
    src = pattern.sub(stub, src, count=1)

# ============================================================
# 3. Update JS state
# ============================================================
# currentLesson starts at 11, TOTAL_LESSONS = 20, LIVE_LESSONS empty
src = src.replace(
    '  let currentLesson = 1;\n  const TOTAL_LESSONS = 10;\n  const LIVE_LESSONS = new Set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);  // lessons with real content; others show coming-soon',
    '  let currentLesson = 11;\n  const TOTAL_LESSONS = 20;\n  const LIVE_LESSONS = new Set([]);  // lessons with real content; others show coming-soon'
)

# Extend CHINESE_NUMS to 1-20
src = src.replace(
    "const CHINESE_NUMS = ['一','二','三','四','五','六','七','八','九','十'];",
    "const CHINESE_NUMS = ['一','二','三','四','五','六','七','八','九','十','十一','十二','十三','十四','十五','十六','十七','十八','十九','二十'];"
)

# Card grid loop range: 11 → 20
src = src.replace(
    '    for (let n = 1; n <= TOTAL_LESSONS; n++) {',
    '    for (let n = 11; n <= TOTAL_LESSONS; n++) {'
)

# prevLesson lower bound: <= 11 (so prev from L11 goes back to index)
src = src.replace(
    'function prevLesson() {\n    if (currentLesson <= 1) {',
    'function prevLesson() {\n    if (currentLesson <= 11) {'
)

# ============================================================
# 4. Update navigation/UI: swap active button & links
# ============================================================
# Nav dropdown: swap active class from 01-10 → 11-20
src = src.replace(
    '<a class="sub-item active" href="hsk6_01-10.html">Lesson 01–10</a>\n            <a class="sub-item" href="hsk6_11-20.html">Lesson 11–20</a>',
    '<a class="sub-item" href="hsk6_01-10.html">Lesson 01–10</a>\n            <a class="sub-item active" href="hsk6_11-20.html">Lesson 11–20</a>'
)

# Index page chapters-title: Lesson 01–10 → Lesson 11–20
src = src.replace(
    '<h2 class="chapters-title">Lesson 01–10</h2>',
    '<h2 class="chapters-title">Lesson 11–20</h2>'
)

# Top section button strip: swap which button is "active" (vermillion, non-clickable)
# Currently: 01-10 is active (vermillion, onclick=preventDefault), 11-20/21-30/31-40 link out
# New:       11-20 is active, 01-10 links back, 21-30/31-40 stay as before

old_buttons_block = '''      <a href="#" onclick="event.preventDefault();"
         style="display:inline-flex;align-items:center;gap:7px;padding:8px 18px;border-radius:8px;background:var(--vermillion);color:#fff;font-family:'Outfit',sans-serif;font-size:0.82rem;font-weight:600;text-decoration:none;transition:background 0.2s,transform 0.2s;cursor:default;">
        Lesson 01–10
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"/></svg>
      </a>
      <a href="hsk6_11-20.html"
         style="display:inline-flex;align-items:center;gap:7px;padding:8px 18px;border-radius:8px;background:#fff;color:var(--ink);border:1.5px solid var(--mist);font-family:'Outfit',sans-serif;font-size:0.82rem;font-weight:600;text-decoration:none;transition:border-color 0.2s,transform 0.2s,box-shadow 0.2s;"
         onmouseover="this.style.borderColor='var(--gold)';this.style.transform='translateY(-1px)';this.style.boxShadow='0 4px 12px rgba(26,18,9,0.08)'"
         onmouseout="this.style.borderColor='var(--mist)';this.style.transform='translateY(0)';this.style.boxShadow=''">
        Lesson 11–20'''

new_buttons_block = '''      <a href="hsk6_01-10.html"
         style="display:inline-flex;align-items:center;gap:7px;padding:8px 18px;border-radius:8px;background:#fff;color:var(--ink);border:1.5px solid var(--mist);font-family:'Outfit',sans-serif;font-size:0.82rem;font-weight:600;text-decoration:none;transition:border-color 0.2s,transform 0.2s,box-shadow 0.2s;"
         onmouseover="this.style.borderColor='var(--gold)';this.style.transform='translateY(-1px)';this.style.boxShadow='0 4px 12px rgba(26,18,9,0.08)'"
         onmouseout="this.style.borderColor='var(--mist)';this.style.transform='translateY(0)';this.style.boxShadow=''">
        Lesson 01–10
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"/></svg>
      </a>
      <a href="#" onclick="event.preventDefault();"
         style="display:inline-flex;align-items:center;gap:7px;padding:8px 18px;border-radius:8px;background:var(--vermillion);color:#fff;font-family:'Outfit',sans-serif;font-size:0.82rem;font-weight:600;text-decoration:none;transition:background 0.2s,transform 0.2s;cursor:default;">
        Lesson 11–20'''

assert old_buttons_block in src, 'Top buttons block not found'
src = src.replace(old_buttons_block, new_buttons_block)

# ============================================================
# 5. Update LIVE_PAGES list — references to siblings
# ============================================================
# In hsk6_11-20.html, the current page is 11-20 (always live), siblings (01-10) are live
src = src.replace(
    """  const LIVE_PAGES = new Set([
    'hsk6_01-10.html',
    // 'hsk6_11-20.html',  // not built yet → falls through to coming-soon
    // 'hsk6_21-30.html',
    // 'hsk6_31-40.html',""",
    """  const LIVE_PAGES = new Set([
    'hsk6_01-10.html',
    'hsk6_11-20.html',
    // 'hsk6_21-30.html',
    // 'hsk6_31-40.html',"""
)

# ============================================================
# 6. Write output
# ============================================================
DST.write_text(src, encoding='utf-8')
print(f'Created {DST}')
print(f'Size: {len(src):,} bytes')
