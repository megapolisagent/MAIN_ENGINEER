---
Версия: 1.2
Дата: 2026-06-13
Источник: https://github.com/megapolisagent/my-claude-arsenal
Статус: АКТУАЛЬНЫЙ
Связанные файлы: [[MAIN_ENGINEER.md]] | [[MARIA_PROFILE.md]]
---

# SKILLS_REGISTRY.md
## Реестр всех инструментов — Агентство недвижимости Москва

> Живой документ. Обновляется при установке новых инструментов.
> Claude читает этот файл при срабатывании Capability Selection Trigger (Impact/Uncertainty/Complexity — см. [[MAIN_ENGINEER_CORE.md]] РАЗДЕЛ 1.5, Шаг 0), не только при создании нового агента.

---

## УРОВНИ ИНСТРУМЕНТОВ (Tool Priority Layer)

| Уровень | Название | Когда использовать |
|---|---|---|
| 🟢 LEVEL 1 | CORE — ядро | Постоянно. Включаются автономно. |
| 🟡 LEVEL 2 | SPECIALIZED — специнструменты | Только под конкретную задачу. |
| 🔴 LEVEL 3 | HEAVY MEMORY — осторожная зона | Только CRM. Source of truth — всегда файлы. |

**Правило:** сначала попробуй решить задачу Level 1. Если не хватает — подключи минимум из Level 2.

---

## АВТОНОМНЫЕ ТРИГГЕРЫ

| Ситуация | Инструмент | Уровень |
|---|---|---|
| Анализ рынка / конкурентов / новостей | Tavily | 🟢 L1 |
| Семантический поиск по компаниям/людям | Exa | 🟢 L1 |
| Документация SDK/API при написании кода | Context7 | 🟢 L1 |
| Сложная многошаговая задача | Sequential Thinking | 🟢 L1 |
| Любой текст для клиентов или публикации | Humanizer | 🟢 L1 |
| Папка 10+ файлов / архив / база данных | Gemini Plugin | 🟡 L2 |
| Код или чертёж перед сдачей Марии | ChatGPT /codex:review | 🟡 L2 |
| Документ длиннее 50 строк | Caveman | 🟡 L2 |
| Парсинг сайта / мониторинг конкурентов | Playwright | 🟡 L2 |
| Контент для соцсетей | marketing-skills | 🟡 L2 |
| Упоминание клиента / объекта / сделки | Memory + MemPalace | 🔴 L3 |
| Долгая сделка между сессиями | AgentMemory | 🔴 L3 |

---

## MCP СЕРВЕРЫ

### 📁 Filesystem — 🟢 LEVEL 1
- **Когда:** Чтение/запись локальных файлов — нужен всегда
- **Путь:** `C:\Users\bogol\OneDrive\Рабочий стол\AI_Projects\`
- **Агенты:** Все агенты Уровня 2

### 🔎 Tavily — 🟢 LEVEL 1
- **Когда:** Любой запрос на актуальную рыночную информацию, проверка застройщиков
- **Автономный триггер:** Включается автоматически при запросе текущих данных
- **Агенты:** Все агенты

### 🔍 Exa Search — 🟢 LEVEL 1
- **Команда:** plugin:everything-claude-code:exa
- **Когда:** Семантический поиск, анализ конкурентов, поиск инвесторов
- **Агенты:** Исследователь, Аналитик рынка

### 📚 Context7 — 🟢 LEVEL 1
- **Команда:** plugin:everything-claude-code:context7
- **Когда:** Актуальная документация SDK/API при написании кода
- **Автономный триггер:** Включается автоматически при работе с внешними API
- **Агенты:** Разработчик, Интеграционный агент

### 🤔 Sequential Thinking — 🟢 LEVEL 1
- **Команда:** plugin:everything-claude-code:sequential-thinking
- **Когда:** Анализ сделки, оценка рисков, сложные задачи с несколькими переменными
- **Автономный триггер:** Задача требует пошагового анализа
- **Агенты:** Аналитик, Советник

### ✍️ Humanizer — 🟢 LEVEL 1
- **Команда:** /humanizer
- **Когда:** Любой текст перед публикацией или отправкой клиенту
- **Автономный триггер:** Всегда после генерации текста для клиентов
- **Агенты:** Копирайтер, Контент-агент

---

### 📧 Gmail — 🟡 LEVEL 2
- **Когда:** Переписка с клиентами, отправка КП, напоминания о просмотрах
- **Статус:** Требует авторизацию Google
- **Агенты:** Клиентский менеджер, Email-оператор

### 📁 Google Drive — 🟡 LEVEL 2
- **Когда:** Договоры, шаблоны, аналитические отчёты
- **Статус:** Требует авторизацию Google
- **Агенты:** Аналитик, Документовед

### 📅 Google Calendar — 🟡 LEVEL 2
- **Когда:** Показы, встречи с клиентами, напоминания о задатках
- **Статус:** Требует авторизацию Google
- **Агенты:** Клиентский менеджер

### 🐙 GitHub — 🟡 LEVEL 2
- **Команда:** plugin:everything-claude-code:github
- **Когда:** Хранение скриптов, версионирование кода
- **Агенты:** Разработчик

### 🎭 Playwright — 🟡 LEVEL 2
- **Команда:** plugin:everything-claude-code:playwright
- **Когда:** Парсинг ЦИАН/Авито/Яндекс.Недвижимость, мониторинг конкурентов
- **Агенты:** Парсер, Мониторинг-агент

---

### 🧠 Memory / Knowledge Graph — 🔴 LEVEL 3
- **Команда:** plugin:everything-claude-code:memory + memory
- **Зона:** ТОЛЬКО CRM — клиенты, объекты, сделки
- **Запрещено хранить:** архитектурные решения, правила системы
- **Агенты:** CRM-агент

### 🏛️ MemPalace — 🔴 LEVEL 3
- **Команда:** plugin:mempalace
- **Зона:** ТОЛЬКО семантическая CRM-база — история переговоров, профили клиентов
- **Команды:** /mempalace:mine, /mempalace:search, /mempalace:status
- **Агенты:** CRM-агент

### 💾 AgentMemory — 🔴 LEVEL 3
- **Команда:** plugin:agentmemory
- **Зона:** ТОЛЬКО долгие сделки — сохранять контекст между сессиями
- **Команды:** /agentmemory:remember, /agentmemory:recall
- **Агенты:** Клиентский менеджер для долгих сделок

---

## ПЛАГИНЫ

### 🦴 Caveman — 🟡 LEVEL 2
- **Команда:** /caveman
- **Автономный триггер:** Документ длиннее 50 строк
- **Режимы:** lite / full / ultra

### ⚡ Everything Claude Code — 🟡 LEVEL 2
Ключевые скиллы (структура: SKILL.md + tools/ + examples/):

| Скилл | Применение | Уровень |
|---|---|---|
| deep-research | Глубокий ресёрч рынка | 🟡 L2 |
| data-scraper-agent | Парсинг ЦИАН/Авито | 🟡 L2 |
| dashboard-builder | Дашборд аналитики | 🟡 L2 |
| content-engine | Контент-машина | 🟡 L2 |
| market-research | Анализ рынка | 🟡 L2 |
| lead-intelligence | Профилирование лидов | 🟡 L2 |
| brand-voice | Tone of voice | 🟢 L1 для контент-агента |

### 📊 Marketing Skills — 🟡 LEVEL 2

| Скилл | Применение |
|---|---|
| cold-email | Письма собственникам |
| copywriting | Тексты объявлений |
| email-sequence | Цепочки нагрева |
| social-content | Посты Telegram/Instagram |
| competitor-profiling | Анализ конкурентов |

### 🔍 Claude SEO — 🟡 LEVEL 2

| Скилл | Применение |
|---|---|
| seo-audit | Аудит сайта |
| seo-local | Локальный SEO Москва |
| seo-content | SEO тексты объектов |
| seo-geo | Видимость в AI-поиске |

### 🎛️ Oh My Claude Code — 🟡 LEVEL 2

| Инструмент | Применение |
|---|---|
| wiki | База знаний агентства |
| python_repl | Аналитика Python |
| deep-dive | Глубокий анализ |
| autopilot | ⚠️ НЕ ИСПОЛЬЗОВАТЬ пока нет стабильного working loop |

---

## ПОЛЬЗОВАТЕЛЬСКИЕ СКИЛЛЫ

### 📖 Book-to-Skill — 🟡 LEVEL 2
- **Команда:** /book-to-skill
- **Структура:** SKILL.md + tools/ + examples/ (по правилу Anthropic)

### 👤 Colleague — 🟡 LEVEL 2
- **Команда:** /colleague
- **Структура:** SKILL.md + примеры переписок в examples/

### 🎨 Creative Director — 🟡 LEVEL 2
- **Команда:** /creative-director

### ✍️ Humanizer — 🟢 LEVEL 1
- **Команда:** /humanizer
- **Автономный триггер:** После любого текста для публикации

---

## СТРУКТУРА СКИЛЛА (правило Anthropic)

Каждый скилл = три слоя. Без tools/ — это просто промт.

```
~/.claude/skills/название-скилла/
├── SKILL.md       # Description (когда брать) + Instructions (как делать)
├── tools/         # Скрипты, шаблоны, API-обёртки
└── examples/      # Few-shot примеры для памяти
```

## РИТУАЛ КОНЦА СЕССИИ

После каждой решённой повторяющейся задачи Claude автономно спрашивает:
> "Что из этой сессии забрать в скилл навсегда?"

---

## УСТАНОВКА НЕДОСТАЮЩИХ ИНСТРУМЕНТОВ

| Инструмент | Как установить |
|---|---|
| Gemini Plugin | claude.ai → Settings → Extensions → Gemini |
| NotebookLM | notebooklm.google.com — отдельный инструмент |
| Obsidian Web Clipper | Chrome Web Store → "Obsidian Web Clipper" |
| Новые MCP | claude.ai → Settings → Integrations |

---

*SKILLS_REGISTRY v1.2 | Tool Priority Layer | 3 уровня | Читается по CS Trigger (MAIN_ENGINEER_CORE Шаг 0) | Anthropic Skill Rules | Синхронизирован с arsenal.md*
