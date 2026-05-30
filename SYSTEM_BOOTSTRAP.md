---
Версия: 1.0
Дата сборки: 2026-05-29
Тип: Bootstrap Snapshot — история сборки ядра системы
Связанные файлы: [[MAIN_ENGINEER.md]] | [[ENGINEERING_LOG/registry.md]]
---

# SYSTEM_BOOTSTRAP.md
## История сборки центрального ядра MAIN_ENGINEER

> Этот файл — исторический документ. Не обновляется.
> При следующей пересборке ядра создаётся новый файл: SYSTEM_BOOTSTRAP_v2.md

---

## СОСТОЯНИЕ ЯДРА НА МОМЕНТ СБОРКИ

| Файл | Версия | Статус |
|---|---|---|
| MAIN_ENGINEER.md | v2.5, 15 разделов | ✅ |
| SKILLS_REGISTRY.md | v1.1, Tool Priority Layer | ✅ |
| MARIA_PROFILE.md | v2.0, 12 разделов | ✅ |
| ai_engineering_operating_system_master.md | — | ✅ |
| ENGINEERING_LOG/registry.md | v2.0 | ✅ |
| SYSTEM_BOOTSTRAP.md | v1.0 | ✅ |
| PROJECT_SUMMARIES/ | — | ✅ Пустая, заполняется по проектам |

---

## КЛЮЧЕВЫЕ АРХИТЕКТУРНЫЕ РЕШЕНИЯ

1. Роутинг между агентами — автономный. Claude сам определяет триггер без команды Марии.
2. Source of truth — filesystem. Никогда memory.
3. Memory-системы — только CRM. Не для архитектуры и инженерных решений.
4. Каждый скилл = три слоя: Description + Instructions + Tools (правило Anthropic).
5. autopilot — не использовать до Stage 3.
6. MARIA_PROFILE хранит cognitive-operational traits. Инженерные законы — только в MAIN_ENGINEER.md.
7. registry.md = System Asset Registry. Регистрирует проекты, агентов, workflows, инфраструктуру.

---

## ИСТОЧНИКИ И ВЛИЯНИЯ

| Источник | Вклад |
|---|---|
| Андрей Карпати | 4-слойная архитектура памяти, принципы простоты, Working Loop Obsession |
| Anthropic Engineering | 4 правила скиллов: промть скиллы не Claude, три слоя, композиционные, обновлять каждую сессию |
| ChatGPT | Tool Priority Layer, Stage Awareness, Anti-Complexity, Failure Escalation, Observed Variability |
| Claude Code | MARIA_PROFILE v1.0 на основе реальных данных hh-parser, seo-machine, vibe-test |
| Мария | Архитектурное направление, философия системы, принципы взаимодействия AI + среды |

---

## ЭТАПЫ СБОРКИ (architectural lineage)

| # | Что добавлено | Почему |
|---|---|---|
| 1 | MAIN_ENGINEER.md v1.0 | Базовый документ — нужна была точка запуска |
| 2 | Pragmatic Override + Intellectual Honesty + Handover Protocol | Жёсткий язык заклинивал LLM; нужна была гибкость и честность о незнании |
| 3 | Граница передачи управления | Агент лез куда не надо — нужна была чёткая зона ответственности |
| 4 | Stage Awareness + Anti-Complexity + Decision Freeze + Priority Hierarchy | AI прыгал через Stage и предлагал архитектуру будущего вместо рабочего цикла сегодня |
| 5 | Retrieval Priority | Агент реконструировал контекст из предположений вместо чтения файлов — источник галлюцинаций |
| 6 | 4-слойная архитектура памяти (Карпати) | Нужна была чёткая граница что куда хранить и какой инструмент за что отвечает |
| 7 | Capability Routing Layer (Claude / GPT / Gemini) | Три инструмента без разделения ролей создавали tool-chaos |
| 8 | Автономный роутинг | Ручные команды замедляли работу; агент должен сам знать когда и что вызывать |
| 9 | Skills Propagation + SKILLS_REGISTRY | Агенты Уровня 2 не знали какие инструменты им нужны — нужен был briefing |
| 10 | System Health Check + Anti-Framework Disease | AI-системы умирают от накопленной сложности, не от недостатка функций |
| 11 | Failure Escalation | Агент бесконечно чинил хаос вместо признания плохой архитектуры |
| 12 | Human Override Priority | Автономная система без явного права вето Марии — архитектурный риск |
| 13 | Context Budget Awareness | Длинные multi-agent сессии начали размывать focus и качество reasoning |
| 14 | Working Loop Obsession | Центральный принцип — без него любая архитектура остаётся планом на бумаге |
| 15 | Skill Engineering (4 правила Anthropic) | Скиллы строились как промты — умирали с сессией вместо того чтобы накапливаться |
| 16 | Tool Priority Layer (Level 1/2/3) | Арсенал вырос до AI-lab уровня — без приоритетов начался tool-chaos |

---

*SYSTEM_BOOTSTRAP v1.0 | Сборка завершена 2026-05-29 | Следующий шаг: первый bootstrap execution test*
