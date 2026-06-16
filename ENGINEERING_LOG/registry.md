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
- **Pattern:** Distilled Inheritance от MAIN_ENGINEER_CORE + Read-симметрия с MAIN_ENGINEER (вся система знаний Марии read-only) / Write-асимметрия (write только в собственную папку после подтверждения)
- **Stage:** S0 — Just Created → S1 кандидат (working loop пройден на Мегаполисе; 2026-06-15: run 1 вскрыл Navigation Drift → CORE v1.3; run 2 подтвердил M2/M3 пробелы → CORE v1.4 Brand Voice Filter + Hand-off Protocol; gap analysis уточнил M3 как identity-defining → CORE v1.5 Mode 3 Active Questioning; run 3 sweep без anchor + run 4 успешный extraction-mode review с decision Марии «брокерский бизнес» → CORE v1.6 Strategic Cadence 2.6 Quarterly Goal & Anchor Decision; runs 5–6 выявили Self-Execution drift + Maria сформулировала Model B + добавила анти-Agentization Drift → CORE v1.7 раздел 2.7 Capability Routing с тремя режимами Mode A/B/C + AGENT_SPECS/ как зона памяти Mode B; v1.8 — две точечные калибровки от Марии: Mode B триггеры стали мягкими сигналами устойчивой потребности (не «3+ повторений»), Edge-Currency переписан без иерархии «выше/ниже» — три равных уровня ответственности в экосистеме; v1.9 — verification test выявил два gap в исполнении: Brand Voice Filter не распространялся явно на прямой диалог («вываливай» в Mode A) → 1.7 расширен симметрично + добавлена категория pseudo-intimacy; Mode 3 правило «один вопрос вместо трёх» не распространялось на Mode C (5 вопросов взамен диалога при сборе инженерных требований) → добавлен кросс-режимный принцип One Question Per Step в 1.5; v1.10 — третий gap из того же verification test: Mentor reflex в Mode C сработал в финале как «встречный на засыпку», не как входной gate (бизнес-ценность проверялась после сборки 5 implementation-вопросов) → 2.7 Правило 5 переписано из абстрактного «тот ли это маршрут» в конкретный per-mode gate с явными вопросами окупаемости; **v1.11 (2026-06-16)** — wheel-of-life session выявила два класса ошибок: (a) двукратный уход в стратегию вопреки формату колеса (Финансы Угол 4 + Мегаполис Угол 3) → external review package v1.7.1 от MAIN_ENGINEER (`ENGINEERING_LOG/external_review_MAIN_ASSISTANT_v1.7.1_2026-06-16.md`) → MAIN_ASSISTANT интегрировал самостоятельно: 1.5 кросс-режимный принцип «Уважение к формату текущей сессии» (Mode 3 не ломает обзорный формат, помечает узел для отдельной сессии, триггер выхода — только явная просьба Марии); (b) фиксация Mode B-кандидата без gate (Красная Поляна = разовая поездка) + жёлтый Agentization Drift (4 кандидата за сессию) → 2.7 #5 Mode B расширен из однострочного вопроса до 4-вопросного pre-flight gate в порядке отсева: нужен ли вообще новый агент → горизонт 30–90 дней постоянной работы → метрика обоснования / антирулики → допустимость «не агент» как валидного исхода; второе правило из external review (Evidence Before Capability Judgment) MAIN_ASSISTANT сознательно не добавил как новое — направил «выводы без улик» в существующее 1.5 Three Cognitive States через дисциплину применения (Anti-Framework Disease). MAIN_ENGINEER second-pass review закрыт; обнаружил собственную асимметрию (2.1.1 Capability Falsification частично дублировал 2.1) — свёрнут в поправку к 2.1 по тому же принципу. Symmetric Self-Correction — рабочая установка без формализации до второго подтверждённого случая)
- **Приоритет:** HIGH
- **Статус:** В работе
- **Dependencies:** PRJ-001 (read-only ко всей папке MAIN_ENGINEER)
- **Open Threads:** STATE.md redesign — карта активных доменов жизни Марии с указанием владельца домена (engineered agent через указатель в `AI_Projects/` · Project Agent через `AGENT_SPECS/` · MAIN_ASSISTANT в Mode A live thinking · MAIN_ENGINEER · сама Мария без системного указателя). Не калибровка ошибок, архитектурная эволюция в ответ на внешний совет (ChatGPT) после прогона v1.11. Передано MAIN_ASSISTANT для пересмотра STATE через Anti-Framework Disease (минимальные изменения). Источник: разбор беседы Марии с ChatGPT 2026-06-16, верифицирован против существующего CORE 8.1 Hybrid Voice/Technical Layer Contract.
- **Last Verified:** 2026-06-16
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
