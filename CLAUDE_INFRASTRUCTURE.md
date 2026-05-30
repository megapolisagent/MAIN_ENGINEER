---
Версия: 1.0
Дата: 2026-05-29
Тип: Infrastructure — физическая инфраструктура Claude Code
Статус: Активен
Связанные файлы: [[MAIN_ENGINEER_CORE.md]] | [[SKILLS_REGISTRY.md]] | [[ENGINEERING_LOG/registry.md]]
---

# CLAUDE_INFRASTRUCTURE.md
## Физическая инфраструктура Claude Code

> Этот файл документирует WHERE, не HOW.
> Поведение системы описано в MAIN_ENGINEER_CORE.md.
> Здесь только: где физически лежат технические части системы.

---

## ФИЗИЧЕСКАЯ КАРТА

```
C:\Users\bogol\
├── .claude\                          ← конфигурация Claude Code
│   ├── settings.json                 ← глобальные настройки
│   ├── credentials.json              ← авторизация
│   ├── history.jsonl                 ← история сессий
│   ├── mcp-needs-auth-cache.json     ← кэш MCP авторизаций
│   ├── backups\                      ← автобэкапы
│   ├── projects\                     ← проекты Claude Code
│   ├── sessions\                     ← активные сессии
│   └── tasks\                        ← задачи агентов
│
└── OneDrive\Рабочий стол\MAIN_ENGINEER\
    ├── .claude\                      ← локальные настройки проекта
    │   └── skills\                   ← пользовательские скиллы
    └── AI_Projects\
        ├── seo-machine\.claude\skills\ ← скиллы seo-machine (25 штук)
        └── vibe-test\.claude\          ← конфиг vibe-test
```

---

## MCP СЕРВЕРЫ (подключённые)

Актуальный список — в `SKILLS_REGISTRY.md`.
Физическая конфигурация — в `~/.claude/settings.json`.

| MCP | Тип подключения | Статус |
|---|---|---|
| Gmail | claude.ai OAuth | Активен |
| Google Drive | claude.ai OAuth | Активен |
| Google Calendar | claude.ai OAuth | Активен |
| GitHub | plugin:everything-claude-code | Активен |
| Context7 | plugin:everything-claude-code | Активен |
| Exa | plugin:everything-claude-code | Активен |
| Memory | plugin:everything-claude-code | Активен |
| Playwright | plugin:everything-claude-code | Активен |
| Sequential Thinking | plugin:everything-claude-code | Активен |
| MemPalace | plugin:mempalace | Активен |
| Filesystem | filesystem | Активен |
| Tavily | tavily | Активен |
| AgentMemory | plugin:agentmemory | Активен |

---

## ПЛАГИНЫ (установленные)

| Плагин | Команды | Где конфиг |
|---|---|---|
| Caveman | /caveman, /caveman:* | ~/.claude/ |
| Everything Claude Code | /everything-claude-code:* | ~/.claude/ |
| Marketing Skills | /marketing-skills:* | ~/.claude/ |
| Claude SEO | /claude-seo:* | ~/.claude/ |
| Oh My Claude Code | /oh-my-claudecode:* | ~/.claude/ |
| Book-to-Skill | /book-to-skill | ~/.claude/ |
| Colleague | /colleague | ~/.claude/ |
| Creative Director | /creative-director | ~/.claude/ |
| Humanizer | /humanizer | ~/.claude/ |

---

## ПОЛЬЗОВАТЕЛЬСКИЕ СКИЛЛЫ

Физически лежат в:
```
~/.claude/skills/                     ← глобальные скиллы
AI_Projects/seo-machine/.claude/skills/  ← 25 скиллов seo-machine
AI_Projects/vibe-test/.claude/        ← скиллы vibe-test
```

Структура каждого скилла (правило Anthropic):
```
skill-name/
├── SKILL.md      ← description + instructions
├── tools/        ← скрипты и шаблоны
└── examples/     ← few-shot примеры
```

---

## ПРАВИЛА ОБНОВЛЕНИЯ

Любое изменение инфраструктуры фиксируется:
- Новый MCP → обновить этот файл + `SKILLS_REGISTRY.md`
- Новый скилл → обновить этот файл + `SKILLS_REGISTRY.md`
- Изменение config → обновить этот файл
- Всё → коммит в GitHub через `sync-to-github.ps1`

---

*CLAUDE_INFRASTRUCTURE v1.0 | Physical layer only | 2026-05-29*
