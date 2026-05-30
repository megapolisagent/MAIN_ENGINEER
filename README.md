---
Версия: 1.0
Дата: 2026-05-29
Тип: System — Входная дверь системы
Статус: Активен
Связанные файлы: [[MAIN_ENGINEER_CORE.md]] | [[ENGINEERING_LOG/registry.md]] | [[SKILLS_REGISTRY.md]]
---

# MAIN_ENGINEER
## AI Operating Architecture — Агентство недвижимости Мегаполис

> Читай этот файл первым если потерял контекст или открываешь папку после перерыва.

---

## ЧТО ЭТО

MAIN_ENGINEER — центральное ядро AI-экосистемы агентства недвижимости Мегаполис.

Это не набор файлов. Это AI Operating Architecture:
- **Архитектор** (MAIN_ENGINEER) думает, исследует, создаёт агентов
- **Агенты** (AI_Projects/) выполняют конкретные задачи
- **Память** (filesystem) хранит всё постоянно
- **Obsidian** визуализирует связи
- **GitHub** версионирует историю

---

## С ЧЕГО НАЧИНАТЬ

### Если ты Claude Code в новой сессии:
1. Читай `MAIN_ENGINEER_CORE.md` — твоя личность и правила
2. Читай `MARIA_PROFILE.md` — как работать с Марией
3. Читай `ENGINEERING_LOG/registry.md` — что активно прямо сейчас
4. Читай `SKILLS_REGISTRY.md` — какие инструменты доступны

### Если нужен конкретный проект:
1. Открой `ENGINEERING_LOG/registry.md` — найди ID проекта
2. Зайди в `AI_Projects/название/`
3. Читай `START.md` — точка входа в проект

### Если нужно создать нового агента:
1. Читай `MAIN_ENGINEER_CORE.md` Раздел 8 — Bootstrap Sequence
2. Используй `AGENT_PROTOCOL.md` как базу наследования
3. Следуй `OBSIDIAN_PROTOCOL.md` при создании файлов

---

## КАРТА СИСТЕМЫ

```
MAIN_ENGINEER/
├── README.md                    ← ты здесь
│
├── MAIN_ENGINEER_CORE.md        ← ядро: правила, мышление, оркестрация
├── MARIA_PROFILE.md             ← когнитивный профиль Архитектора
├── SKILLS_REGISTRY.md           ← все инструменты с уровнями L1/L2/L3
├── AGENT_PROTOCOL.md            ← ДНК для новых агентов
├── OBSIDIAN_PROTOCOL.md         ← стандарты markdown и knowledge graph
├── SYSTEM_BOOTSTRAP.md          ← история сборки ядра (не обновляется)
├── CLAUDE_INFRASTRUCTURE.md     ← физическая инфраструктура
├── GITHUB_SYNC.md               ← версионирование и backup
├── ai_engineering_operating_system_master.md ← шаблон CLAUDE.md
│
├── .claude/                     ← конфигурация Claude Code
├── AI_Projects/                 ← все проекты
│   ├── hh-parser/               ← PRJ-002
│   ├── seo-machine/             ← PRJ-003
│   └── vibe-test/               ← PRJ-004
├── ENGINEERING_LOG/
│   └── registry.md              ← реестр всех активов
├── PROJECT_SUMMARIES/           ← выжимки по проектам
└── ARCHIVE/                     ← завершённые/замороженные проекты
```

---

## АКТИВНЫЕ ПРОЕКТЫ

Актуальный список → `ENGINEERING_LOG/registry.md`

| ID | Проект | Stage | Приоритет |
|---|---|---|---|
| PRJ-001 | MAIN_ENGINEER | S1 | HIGH |
| PRJ-002 | hh-parser | S2 | MEDIUM |
| PRJ-003 | seo-machine | S3 | HIGH |
| PRJ-004 | vibe-test | S2 | HIGH |

---

## ГЛАВНЫЕ ПРИНЦИПЫ (одной строкой каждый)

- **Working Loop First** — если нельзя проверить сегодня, упрощай
- **Filesystem is truth** — memory только для CRM
- **Distilled inheritance** — агенты получают ДНК, не копию системы
- **Human Override** — финальное слово всегда за Марией

---

*README v1.0 | Входная дверь системы | MAIN_ENGINEER AI Operating Architecture*
