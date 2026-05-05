# IvyChinese — TODO

Suivi des tâches en cours et à venir pour le projet IvyChinese.

---

## HSK 6 — `HSK/HSK6/hsk6_01-10.html`

### Leçons 1–10 (上 · Volume 1)

| # | Titre | Contenu | Vérifié livre | Audio |
|---|---|---|---|---|
| 01 | 孩子给我们的启示 | ✅ Complète | ✅ | ❌ |
| 02 | 父母之爱 | ✅ Complète | ✅ | ❌ |
| 03 | 一盒月饼 | ✅ Complète | ✅ | ❌ |
| 04 | 完美的胜利 | ✅ Complète | ✅ | ❌ |
| 05 | 学一门外语需要理由吗 | ✅ Complète | ✅ | ❌ |
| 06 | 当好职场插班生 | ✅ Complète | ✅ | ❌ |
| 07 | 第七课 | ❌ Stub vide | ❌ | ❌ |
| 08 | 第八课 | ❌ Stub vide | ❌ | ❌ |
| 09 | 第九课 | ❌ Stub vide | ❌ | ❌ |
| 10 | 第十课 | ❌ Stub vide | ❌ | ❌ |

### À faire — HSK 6

- [ ] Implémenter L7 (fournir `HSK6_第7课_书.md`)
- [ ] Implémenter L8 (fournir `HSK6_第8课_书.md`)
- [ ] Implémenter L9 (fournir `HSK6_第9课_书.md`)
- [ ] Implémenter L10 (fournir `HSK6_第10课_书.md`)
- [ ] Créer `hsk6_11-20.html` pour les leçons 11–20

---

## Autres fichiers HSK

| Fichier | Statut |
|---|---|
| `HSK/HSK6/hsk6_01-10.html` | 🟡 En cours (6/10 leçons) |
| `HSK/HSK6/hsk6_11-20.html` | ❌ À créer |

---

## Workflow

Pour chaque nouvelle leçon :
1. Fournir le fichier markdown `HSK6_第X课_书.md` dans `Downloads`
2. Claude génère et exécute `ressources/replace_lX.py`
3. Auto commit + push après chaque leçon complétée
