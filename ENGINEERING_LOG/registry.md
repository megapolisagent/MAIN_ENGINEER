---
Версия: 2.1
Дата: 2026-05-29
Тип: System Asset Registry
Связанные файлы: [[MAIN_ENGINEER.md]] | [[SYSTEM_BOOTSTRAP.md]] | [[PROJECT_SUMMARIES/]]
---

# ENGINEERING_LOG / registry.md
## Реестр активов системы

> Append-only. Записи не переписываются задним числом.
> Разрешено: добавлять записи, обновлять статус, добавлять follow-up блоки.
> Запрещено: менять исторические решения, редактировать прошлые выводы, чистить ошибки постфактум.

---

## ФОРМАТ ЗАПИСИ

```
### [ID] Название
- **Тип:** Project / Agent / Workflow / System / Infrastructure
- **Путь:** локальный путь
- **Задача:** что решает
- **Pattern:** фундаментальная инженерная идея
- **Stage:** S1-S5
- **Приоритет:** HIGH / MEDIUM / LOW / ARCHIVED
- **Статус:** В работе / Завершён / Заморожен
- **Dependencies:** ID зависимостей или —
- **Last Verified:** ГГГГ-ММ-ДД
- **Дата регистрации:** ГГГГ-ММ-ДД
```

---

## АКТИВНЫЕ АКТИВЫ

### PRJ-001 · MAIN_ENGINEER
- **Тип:** System
- **Путь:** `C:\Users\bogol\OneDrive\Рабочий стол\MAIN_ENGINEER\`
- **Задача:** Мета-агентное ядро Уровня 1 — архитектор над всеми проектами
- **Pattern:** Filesystem-first orchestration + externalized memory + capability routing by tool layer
- **Stage:** S1 — Working Prototype
- **Приоритет:** HIGH
- **Статус:** В работе
- **Dependencies:** —
- **Last Verified:** 2026-05-29
- **Дата регистрации:** 2026-05-29

---

### PRJ-002 · hh-parser
- **Тип:** Project
- **Путь:** `AI_Projects\hh-parser\`
- **Задача:** Career intelligence агент — scoring вакансий с explainability
- **Pattern:** Deterministic scoring first → AI only on top of calibrated rules → feedback loop для continuous calibration
- **Stage:** S2 — Stable Workflow (calibration phase)
- **Приоритет:** MEDIUM
- **Статус:** В работе
- **Dependencies:** —
- **Last Verified:** 2026-05-29
- **Дата регистрации:** 2026-05-29

---

### PRJ-003 · seo-machine
- **Тип:** Project
- **Путь:** `AI_Projects\seo-machine\`
- **Задача:** SEO-система для контента агентства
- **Pattern:** Modular SEO orchestration — agent specialization + deterministic content pipeline + Python-assisted analytics
- **Stage:** S3 — Automation
- **Приоритет:** HIGH
- **Статус:** Активен
- **Dependencies:** —
- **Last Verified:** 2026-05-29
- **Дата регистрации:** 2026-05-29

---

### PRJ-004 · vibe-test
- **Тип:** Project
- **Путь:** `AI_Projects\vibe-test\`
- **Задача:** AI-native media infrastructure для Мегаполиса
- **Pattern:** Multi-platform brand voice system — единый голос бренда через специализированных агентов на 7 платформах
- **Stage:** S2 — Stable Workflow
- **Приоритет:** HIGH
- **Статус:** Активен
- **Dependencies:** PRJ-003 (brand voice system из seo-machine)
- **Last Verified:** 2026-05-29
- **Дата регистрации:** 2026-05-29

---

### PRJ-005 · property-analyst
- **Тип:** Project
- **Путь:** `AI_Projects\property-analyst\`
- **Задача:** AI-система аналитики объектов недвижимости — профессиональный PDF-отчёт для продавца (позиция на рынке, оценка цены, район, рекомендация)
- **Pattern:** Layered architecture с жёсткой Deterministic/AI границей + Hybrid QA loop + Separation by instability source (cian_client / geo_client раздельно)
- **Stage:** S1 — Working Prototype
- **Приоритет:** HIGH
- **Статус:** Bootstrap завершён — передан Локальному Строителю
- **Dependencies:** —
- **Last Verified:** 2026-05-30
- **Дата регистрации:** 2026-05-30

---

### PRJ-006 · MAIN_ASSISTANT
- **Тип:** System
- **Путь:** `C:\Users\bogol\OneDrive\Рабочий стол\MAIN_ASSISTANT\`
- **Задача:** Strategic Chief of Staff — Level 1 сиблинг MAIN_ENGINEER. Capture/Organize/Connect/Distill/Retrieve для решений и фокуса Марии вне AI-инженерии
- **Pattern:** Distilled Inheritance от MAIN_ENGINEER_CORE + Read-only Source of Truth на registry.md (асимметричный Role Boundary)
- **Stage:** S0 — Just Created (working loop не проверен)
- **Приоритет:** HIGH
- **Статус:** В работе
- **Dependencies:** PRJ-001 (read-only)
- **Last Verified:** 2026-06-13
- **Дата регистрации:** 2026-06-13

---

## ПРЕФИКСЫ ID

| Тип актива | Префикс | Пример |
|---|---|---|
| Проект | PRJ | PRJ-005 |
| Агент | AGT | AGT-001 |
| Workflow | WRK | WRK-001 |
| Инфраструктура | INF | INF-001 |
| Memory layer | MEM | MEM-001 |

---

*registry.md v2.1 | System Asset Registry | Append-only*
