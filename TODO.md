# IvyChinese — TODO

Suivi des tâches en cours et à venir pour le projet IvyChinese.

---

## HSK 6 — `HSK/HSK6/hsk6_01-10.html`

### Leçons 1–10 (上 · Volume 1) ✅ COMPLET

| # | Titre | Contenu | Vérifié livre | Audio |
|---|---|---|---|---|
| 01 | 孩子给我们的启示 | ✅ Complète | ✅ | ❌ |
| 02 | 父母之爱 | ✅ Complète | ✅ | ❌ |
| 03 | 一盒月饼 | ✅ Complète | ✅ | ❌ |
| 04 | 完美的胜利 | ✅ Complète | ✅ | ❌ |
| 05 | 学一门外语需要理由吗 | ✅ Complète | ✅ | ❌ |
| 06 | 当好职场插班生 | ✅ Complète | ✅ | ❌ |
| 07 | 我的人生我做主 | ✅ Complète | ✅ | ❌ |
| 08 | 遇见原来的我 | ✅ Complète | ✅ | ❌ |
| 09 | 不用手机的日子 | ✅ Complète | ✅ | ❌ |
| 10 | 全球化视野中的中国饮食 | ✅ Complète | ✅ | ❌ |

### À faire — HSK 6

- [ ] Créer `hsk6_11-20.html` pour les leçons 11–20 (PDFs disponibles dans `ressources/HSK6 书 上/`)
- [ ] Ajouter les pistes audio pour toutes les leçons 1–10

---

## Autres fichiers HSK

| Fichier | Statut |
|---|---|
| `HSK/HSK6/hsk6_01-10.html` | ✅ Complet (10/10 leçons) |
| `HSK/HSK6/hsk6_11-20.html` | ❌ À créer |

---

## Workflow

Pour chaque nouvelle leçon :
1. Fournir le fichier PDF dans `ressources/HSK6 书 上/HSK6 第X课 书.pdf`
2. Claude rend en PNG via `pdf_to_png.py`, lit le contenu et génère `ressources/replace_lX.py`
3. Le script remplace le bloc lesson-content et met à jour `LIVE_LESSONS`
4. Auto commit + push après chaque leçon complétée
