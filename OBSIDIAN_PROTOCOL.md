---
Версия: 1.1
Дата: 2026-05-29
Тип: Protocol — Machine-Readable Knowledge System
Статус: Активен
Связанные файлы: [[MAIN_ENGINEER_CORE.md]] | [[AGENT_PROTOCOL.md]] | [[ENGINEERING_LOG/registry.md]]
---

# OBSIDIAN_PROTOCOL.md
## Стандарты Markdown и Knowledge Architecture

> Цель: не "красивый markdown", а machine-readable knowledge system.
> Документы должны быть понятны человеку И предсказуемы для AI одновременно.
> Все агенты системы обязаны следовать этим правилам.

---

## ПРАВИЛО 1 — FILE NAMING

### Системные файлы (MAIN_ENGINEER/)
```
MAIN_ENGINEER_CORE.md
MARIA_PROFILE.md
SKILLS_REGISTRY.md
SYSTEM_BOOTSTRAP.md
OBSIDIAN_PROTOCOL.md
CLAUDE_INFRASTRUCTURE.md
GITHUB_SYNC.md
AGENT_PROTOCOL.md
```

### Проектные файлы (AI_Projects/название/)
```
PROJECT_DNA.md        # контекст бизнеса и философия
CLAUDE.md             # правила агента
ROADMAP.md            # план развития
START.md              # протокол запуска + Agent Briefing
AGENT_PROTOCOL.md     # наследуемые правила (копия из MAIN_ENGINEER/)
```

### Summaries (PROJECT_SUMMARIES/)
```
PRJ-001_MAIN_ENGINEER.md
PRJ-002_hh-parser.md
PRJ-003_seo-machine.md
```

### Правила именования
- System layer: `UPPER_SNAKE_CASE.md` — MAIN_ENGINEER_CORE, MARIA_PROFILE и т.д.
- Projects / folders: `lower-kebab-case/` — seo-machine, hh-parser
- Scripts: `lower-kebab-case.py`
- Только `lower-kebab-case` для скриптов: `parse-cian.py`
- Никаких пробелов в именах — никогда
- Никакого транслита: `MARIA_PROFILE`, не `PROFIL_MARII`
- Никаких `final_v2_REAL.md` — только версия в паспорте

**Запрещено:**
```
❌ my file.md
❌ profil marii.md
❌ CLAUDE_final_v2_REAL.md
❌ новый документ.md
```

---

## ПРАВИЛО 2 — REQUIRED HEADER (паспорт файла)

Каждый `.md` файл обязан начинаться с паспорта:

```markdown
---
Версия: X.X
Дата: ГГГГ-ММ-ДД
Тип: [System / Project / Protocol / Profile / Registry / Bootstrap / Agent]
Статус: [Активен / Заморожен / Архив]
Связанные файлы: [[ФАЙЛ_1.md]] | [[ФАЙЛ_2.md]]
---

# НАЗВАНИЕ ФАЙЛА
## Подзаголовок — что это и зачем

> Одна строка: главная суть документа для быстрого понимания.
```

### Обязательные поля
| Поле | Обязательно | Описание |
|---|---|---|
| Версия | ✅ | Числовая: 1.0, 1.1, 2.0 |
| Дата | ✅ | Дата последнего обновления |
| Тип | ✅ | Категория документа |
| Статус | ✅ | Текущее состояние |
| Связанные файлы | ✅ | Минимум 2 wiki-link |

**Почему это важно:** Obsidian строит граф, Claude понимает связи, навигация и retrieval работают предсказуемо.

---

## ПРАВИЛО 3 — WIKI-LINKS

### Синтаксис
```markdown
[[MAIN_ENGINEER_CORE.md]]              # ссылка на файл
[[MARIA_PROFILE.md|Профиль Марии]]     # с отображаемым текстом
[[PRJ-001]]                            # ссылка на проект по ID
```

### Обязательные связи
Каждый файл ссылается на:
- Родительский документ (откуда вырос)
- `MAIN_ENGINEER_CORE.md` или `ENGINEERING_LOG/registry.md`
- Связанные проекты или агенты если есть

**Запрещено:** raw пути внутри md если можно использовать wiki-link:
```markdown
❌ C:\Users\bogol\OneDrive\MAIN_ENGINEER\SKILLS_REGISTRY.md
✅ [[SKILLS_REGISTRY.md]]
```

### Центральные узлы графа (Central Nodes)
На эти файлы должны ссылаться все остальные:

| Файл | Роль в графе |
|---|---|
| `MAIN_ENGINEER_CORE.md` | Главный хаб — ядро системы |
| `SKILLS_REGISTRY.md` | Хаб инструментов |
| `MARIA_PROFILE.md` | Хаб когнитивной модели |
| `ENGINEERING_LOG/registry.md` | Хаб активов |
| `OBSIDIAN_PROTOCOL.md` | Хаб стандартов |

**Правило:** каждый новый файл → минимум 2 wiki-link на центральные узлы.

---

## ПРАВИЛО 4 — SINGLE RESPONSIBILITY

Один markdown-файл = одна роль. Нельзя смешивать:

```
❌ registry + memory + bootstrap + architecture в одном документе

✅ registry.md        → только реестр активов
✅ SYSTEM_BOOTSTRAP   → только история сборки
✅ MARIA_PROFILE      → только когнитивный профиль
✅ SKILLS_REGISTRY    → только инструменты
```

**Признак нарушения:** файл становится длиннее 300 строк — пора делить.

---

## ПРАВИЛО 5 — HUMAN + MACHINE READABLE

Документы должны быть понятны человеку И предсказуемы для AI:

### Структура заголовков
```markdown
# H1 — только название файла, один раз вверху
## H2 — основные разделы
### H3 — подразделы
```
Не использовать H4 и глубже — признак overengineering.

### Таблицы
✅ Для сравнений, реестров, матриц
❌ Для простых списков из 2-3 элементов → используй bullet points

### Статусные маркеры
```markdown
✅ Готово / Активен
⏳ В процессе
❌ Не готово / Заблокировано
⚠️ Внимание / Риск
```

### Блоки кода
```markdown
`inline` — команды, пути, имена файлов в тексте
```блок``` — многострочный код, структуры папок, примеры
```

### Callout (цитата)
```markdown
> Используй только для ключевого тезиса документа — одна строка.
```
Не злоупотреблять. Один callout на файл.

---

## ПРАВИЛО 6 — KNOWLEDGE GRAPH STRUCTURE

```
        MAIN_ENGINEER_CORE
       /     |      |      \
MARIA_PROFILE SKILLS BOOTSTRAP INFRASTRUCTURE
                |
           REGISTRY
          /    |    \
       PRJ-001 PRJ-002 PRJ-003
          |
    PROJECT_SUMMARIES/PRJ-001
```

### Что связываем
- Каждый проект → ядро (`MAIN_ENGINEER_CORE`)
- Каждый проект → реестр (`registry.md`)
- Проекты с зависимостями → друг с другом
- Агенты → их проект + `SKILLS_REGISTRY`

### Что НЕ связываем
- Технические скрипты `.py`, `.json`
- Временные рабочие файлы
- Raw данные и логи

---

## ЧЕКЛИСТ ДЛЯ CLAUDE

При создании любого нового `.md` файла:

- [ ] Паспорт вверху (Версия, Дата, Тип, Статус, Связанные файлы)
- [ ] Минимум 2 wiki-link на центральные узлы
- [ ] UPPER_SNAKE_CASE имя файла
- [ ] Заголовки не глубже H3
- [ ] Один файл — одна роль
- [ ] Если это новый проект, агент или workflow → запись в `ENGINEERING_LOG/registry.md` (не для каждого файла)

**Все persistent system documents обязаны иметь паспорт.** Временные заметки, черновики и scratchpads — исключение.

---

*OBSIDIAN_PROTOCOL v1.1 | Machine-Readable Knowledge System | Обязателен для всех агентов*

---

## ПРАВИЛО 7 — TEMP / SANDBOX ZONE

Каждый проект может иметь папку `temp/` для черновиков и экспериментов:

```
AI_Projects/project-name/
└── temp/          ← черновики, sырой thinking, эксперименты
```

Файлы в `temp/` **не обязаны** следовать OBSIDIAN_PROTOCOL.
После стабилизации: либо удалить, либо превратить в persistent document с паспортом.

**Правило:** `temp/` не индексируется, не попадает в граф Obsidian, не грузится в контекст по умолчанию.

---

## ПРАВИЛО 8 — VERSIONING RULES

Когда повышать версию:

| Изменение | Версия | Пример |
|---|---|---|
| Изменение архитектуры или структуры | Major: X.0 | 1.0 → 2.0 |
| Локальные улучшения и уточнения | Minor: X.X | 1.0 → 1.1 |
| Исправление ошибок и опечаток | Patch: X.X.X | 1.1 → 1.1.1 |

Запрещено: `FINAL_v2_REAL`, `final_FINAL`. Только числовые версии в паспорте.

---

## ПРАВИЛО 9 — ARCHIVED FLOW

Архивные проекты и документы:
- Переводятся в статус `Архив` в паспорте
- Перемещаются в папку `ARCHIVE/` внутри проекта или системы
- Исключаются из active orchestration
- **Не загружаются в контекст по умолчанию**
- В registry.md статус меняется на `ARCHIVED`, приоритет на `ARCHIVED`

```
MAIN_ENGINEER/
└── ARCHIVE/
    └── устаревшие документы
```

**Правило для MAIN_ENGINEER:** при загрузке контекста игнорировать всё из `ARCHIVE/`.

---

## ПРАВИЛО 10 — PROJECT ENTRYPOINT

Каждый проект обязан иметь `START.md` — единственную точку входа.

`START.md` содержит:
- Текущий статус проекта (одна строка)
- Что сделано / что в работе / что заблокировано
- Bootstrap sequence — с чего начать агенту
- Ссылки на ключевые файлы проекта

**Правило при потере контекста:** читать `START.md` первым. Всегда.

```
AI_Projects/project-name/
├── START.md          ← читать первым
├── PROJECT_DNA.md
├── CLAUDE.md
├── ROADMAP.md
└── AGENT_PROTOCOL.md
```

---

*OBSIDIAN_PROTOCOL v1.2 | 10 правил | Machine-Readable Knowledge System*

---

## ПРАВИЛО 11 — PROJECT_STATE.md

Каждый активный проект должен иметь `PROJECT_STATE.md` — оперативную панель:

```markdown
---
Версия: X.X
Дата: ГГГГ-ММ-ДД
Тип: Project State
Статус: Активен
Связанные файлы: [[START.md]] | [[ROADMAP.md]]
---

# PROJECT_STATE — Название проекта

## Текущий Stage: S1 / S2 / S3 / S4 / S5

## Что работает сейчас
- ...

## Что сломано / заблокировано
- ...

## Следующий шаг
- ...

## Последняя проверка working loop
Дата: ГГГГ-ММ-ДД | Результат: ...
```

`PROJECT_STATE.md` обновляется после каждой рабочей сессии.
`ROADMAP.md` остаётся историческим планом — не трогать при каждом обновлении.

---

## ПРАВИЛО 12 — PROJECT CLOSE PROTOCOL

Проект переводится в архив если выполняется любое из условий:
- Не запускался 30+ дней
- Нет активного roadmap
- Working loop не существует или сломан

**Действия при закрытии:**
1. Обновить статус в `ENGINEERING_LOG/registry.md` → `ARCHIVED`
2. Обновить паспорт проекта → `Статус: Архив`
3. Переместить папку в `ARCHIVE/`
4. Удалить из active context loading
5. Сохранить summary в `PROJECT_SUMMARIES/PRJ-XXX_название.md`

**Статусы проекта:**
- `Активен` — работает, есть working loop
- `Заморожен` — пауза, планируется возобновить
- `Архив` — завершён или заброшен, не грузится в контекст
- `Abandoned` — удалён, summary сохранён

---

*OBSIDIAN_PROTOCOL v1.3 | 12 правил | Финальная версия*
