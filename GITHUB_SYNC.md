---
Версия: 1.0
Дата: 2026-05-29
Тип: Protocol — GitHub синхронизация и версионирование
Статус: Активен
Связанные файлы: [[MAIN_ENGINEER_CORE.md]] | [[OBSIDIAN_PROTOCOL.md]] | [[ENGINEERING_LOG/registry.md]]
---

# GITHUB_SYNC.md
## Версионирование и backup системы MAIN_ENGINEER

> GitHub = страховка + история изменений.
> Obsidian = интерфейс мышления.
> Filesystem = единственный source of truth.

---

## АРХИТЕКТУРА СИНХРОНИЗАЦИИ

```
MAIN_ENGINEER/ (локально на Windows)
       ↕ git sync
GitHub репозиторий (backup + version history)
       ↕ читает папку
Obsidian Vault (визуальный интерфейс)
```

---

## ШАГ 1 — Подключить папку к GitHub

Открой PowerShell в папке MAIN_ENGINEER:

```powershell
cd "C:\Users\bogol\OneDrive\Рабочий стол\MAIN_ENGINEER"
git init
git remote add origin https://github.com/megapolisagent/MAIN_ENGINEER.git
```

Если репозиторий ещё не создан — создай на github.com/new с именем `MAIN_ENGINEER`.

---

## ШАГ 2 — Создать .gitignore

Создай файл `.gitignore` в корне папки MAIN_ENGINEER:

```
# Claude Code служебные папки
.claude/cache/
.claude/sessions/
.claude/telemetry/
.claude/paste-cache/

# Временные файлы
*.tmp
*.log
~$*

# Obsidian служебные файлы
.obsidian/workspace.json
.obsidian/workspace-mobile.json
```

---

## ШАГ 3 — Первый коммит

```powershell
git add .
git commit -m "init: AI Operating Layer v1.0 — первый запуск системы"
git push -u origin main
```

---

## ШАГ 4 — Автосинхронизация (PowerShell скрипт)

Создай файл `sync-to-github.ps1` в папке MAIN_ENGINEER:

```powershell
# sync-to-github.ps1
# Запускай вручную после важных изменений

cd "C:\Users\bogol\OneDrive\Рабочий стол\MAIN_ENGINEER"

$date = Get-Date -Format "yyyy-MM-dd HH:mm"
$message = "update: $date"

git add .
git status

Write-Host "Коммитим изменения: $message"
git commit -m $message
git push origin main

Write-Host "✅ Синхронизировано с GitHub"
```

Запуск: правой кнопкой на файле → "Запустить с PowerShell"

---

## ШАГ 5 — Подключить Obsidian

1. Открой Obsidian
2. Нажми "Open folder as vault"
3. Выбери папку `MAIN_ENGINEER`
4. Trust author → OK
5. Зайди в Settings → Files & Links → Default location for new notes → выбери корень vault

---

## ПРАВИЛА КОММИТОВ

| Тип изменения | Формат сообщения |
|---|---|
| Новый файл | `add: НАЗВАНИЕ_ФАЙЛА — краткое описание` |
| Обновление файла | `update: НАЗВАНИЕ_ФАЙЛА — что изменилось` |
| Новый проект | `project: PRJ-XXX — название` |
| Исправление | `fix: что исправлено` |
| Запуск теста | `test: что тестировалось — результат` |

---

## ЧТО СИНХРОНИЗИРУЕТСЯ

✅ Все `.md` файлы
✅ Python скрипты в AI_Projects/
✅ Конфиги проектов
✅ SKILLS_REGISTRY и другие реестры

❌ `.claude/cache/` и сессии — исключены через .gitignore
❌ Временные файлы

---

*GITHUB_SYNC v1.0 | Backup + Version History | 2026-05-29*
