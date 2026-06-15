---
Версия: 1.1
Дата: 2026-06-15
Тип: Discovery Summary
Статус: Активен
Связанные файлы: [[MAIN_ENGINEER_CORE.md]] | [[MARIA_PROFILE.md]] | [[ENGINEERING_LOG/registry.md]] | [[OBSIDIAN_PROTOCOL.md]]
---

# MAIN_ASSISTANT_DISCOVERY
## История Architecture Discovery нового Level-1 сиблинга MAIN_ENGINEER

> Фиксация выводов Discovery-сессии перед созданием MAIN_ASSISTANT Stage S0. Не CORE, не постоянная память ассистента.

---

## 1. INITIAL PROBLEM

### Боль
Мария обозначила потребность в стратегическом AI-партнёре, сопровождающем её в жизни и бизнесе — параллельная MAIN_ENGINEER сущность на схеме: MARIA → MAIN_ASSISTANT / MAIN_ENGINEER, где MAIN_ASSISTANT покрывает Личную жизнь, Здоровье, Финансы, Бизнесы, Идеи, Цели, Решения, Память.

### Первоначальные предположения
- MAIN_ASSISTANT нужна собственная отдельная память/база знаний
- Telegram-бот нужен с самого начала как интерфейс захвата
- Марию нужно "научить Obsidian" как программу
- MAIN_ASSISTANT строится сопоставимо мощным MAIN_ENGINEER с первого дня

### Что оказалось ошибочным
- ❌ Отдельная память → заменена на Obsidian как Long-Term Memory без своей "вселенной заметок"
- ❌ Telegram сразу → вынесен в будущие этапы (отдельный Capture Gap, не блокирует Computer Mode)
- ❌ "Учить Obsidian" → заменено на "Ассистент пишет в Obsidian, Мария разговаривает"
- ❌ Полноразмерная архитектура с первого дня → заменена на Stage S0 + один working loop

---

## 2. KEY ARCHITECTURAL DISCOVERIES

| Открытие | Суть |
|---|---|
| Level 1 sibling, не Level 2 агент | "Куда смотреть / на чём фокус" (MAIN_ASSISTANT) ≠ "как строить" (MAIN_ENGINEER) — разные роды вопросов |
| Роль — Strategic Chief of Staff | Strategic Partner + Knowledge Manager: Capture → Organize → Connect → Distill → Retrieve |
| Follow Maria's Vision | ≈ Human Override Priority — финальное слово за Марией |
| Challenge with Evidence | ≈ Root Cause First + Intellectual Honesty + Routing Falsification, применённые к жизни/бизнесу |
| Role Boundary | Асимметричный доступ: MAIN_ASSISTANT читает registry.md MAIN_ENGINEER для контекста; обратного доступа нет |
| Distilled Inheritance | MAIN_ASSISTANT_CORE.md — производное от мета-слоёв MAIN_ENGINEER_CORE (1.2–1.6, 2, 11–13, Idea Calibration), retargeted |
| Obsidian = Long-Term Memory, не интерфейс | "Мария → Ассистент → Obsidian", не наоборот. Obsidian — библиотека за спиной ассистента |
| Computer Mode vs Mobile Mode | Два канала захвата: за компьютером (разговор) и в движении (телефон/бумага) |
| Distill/Persist Gap vs Capture Gap | Computer Mode: Capture уже работает, разрыв — в Distill/Persist. Mobile Mode: разрыв в самом Capture |
| Telegram — будущий этап | Решает Mobile Capture Gap, отделённый от Computer Mode Gap — не блокирует Stage S0 |
| Vault топология | Sibling-папка + свобода выбора vault root в Obsidian later → единый граф без переноса файлов сейчас |
| Executive Layer ≠ PROJECT_STATE.md | Executive Layer — карта внимания CEO (цель квартала, направления, решения, что НЕ делаю, следующий шаг), а не статус одного проекта |

---

## 3. FAILED PATHS AND WHY REJECTED

| Путь | Почему отклонён |
|---|---|
| Полная 4-слойная memory-архитектура (Karpathy map) с первого дня | Simple Before Scalable — нечего организовывать без реального контента |
| DOMAINS/ создаются заранее (Мегаполис, Здоровье, Финансы...) | Single Responsibility + lazy creation — домены должны вырасти из реального INBOX, не быть угаданы |
| Перенос MAIN_ENGINEER в MARIA_OPERATING_SYSTEM сейчас | Stage-несоответствие: MAIN_ENGINEER — S1 working с 5 активами, MAIN_ASSISTANT — S0 без единого working loop. Высокий blast radius ради выгоды, доступной позже бесплатно через vault root |
| Telegram-бот на Stage S0 | Решает Mobile Capture Gap, который не является текущим узким местом. Иначе — "3 недели инфраструктуры под непроверенную привычку" |
| "Научить Марию Obsidian" как предусловие | Барьер адопции — система, которой не будут пользоваться. Заменено на роль ассистента-библиотекаря |

---

## 4. FINAL ARCHITECTURE DECISION

### Stage S0 структура
```
MAIN_ASSISTANT/
├── README.md
├── MAIN_ASSISTANT_CORE.md     ← хаб, Distilled Inheritance от MAIN_ENGINEER_CORE
├── MAIN_ASSISTANT_STATE.md    ← Executive Layer (новый шаблон)
└── DECISIONS/
    └── 2026-06-13_main_assistant_design.md   ← дистиллят этой Discovery-сессии
```

Регистрация: `ENGINEERING_LOG/registry.md` → PRJ-006 · MAIN_ASSISTANT, Тип System, Stage S0, сиблинг PRJ-001.

### Первый Working Loop
1. Мария ↔ MAIN_ASSISTANT — разговор (Computer Mode), как сейчас с MAIN_ENGINEER
2. По команде "зафиксируй" — Distill в заметку с паспортом (DECISIONS/, позже DOMAINS/)
3. По запросу "покажи, что мы думали про X" — Retrieve из заметок

### Модель взаимодействия
- **Primary Interface:** разговор Мария ↔ MAIN_ASSISTANT (Computer Mode)
- **Secondary Interface:** Mobile Capture (Telegram) — будущий этап
- **Long-Term Memory:** Obsidian Vault = markdown-файлы MAIN_ASSISTANT/ (filesystem-first, Obsidian — опциональный визуальный слой)

---

## 5. OPEN QUESTIONS AND FUTURE EVOLUTION

- **Mobile Capture / Telegram** — предварён 7-дневным экспериментом с Telegram "Избранное", решение об автоматизации только по данным
- **Domain Memory (DOMAINS/)** — создаётся лениво при первом реальном INBOX-материале
- **Расширение Obsidian / vault scope** — единый граф (vault root выше обоих сиблингов) vs раздельные vault — решается по факту трения, не сейчас
- **Автоматизация** — только после ручного подтверждения Capture Habit + Distill loop
- **Cold-start бизнес-домена** — Executive Layer изначально пуст по метрикам Мегаполиса/Соцсетей/Недвижимости как бизнесов (в отличие от AI-портфеля, видимого через registry.md)

---

## 6. SUCCESS CRITERIA

### Первый Working Loop (S0) — механика Capture → Distill → Retrieve
- ✅ Мария регулярно (без напоминаний) выгружает мысли в разговоре с MAIN_ASSISTANT
- ✅ Команда "зафиксируй" реально создаёт заметку, которую можно найти позже
- ✅ MAIN_ASSISTANT по запросу напоминает прошлые решения ("вот что мы уже проходили")
- ✅ Executive Briefing (STATE.md) даёт ценность при просмотре — карта внимания, а не пустой шаблон

### После 3–5 сессий (когда накопится база в DECISIONS/STATE)
- ✅ Происходит хотя бы один реальный Challenge with Evidence — не декларация, а применённая проверка

> Перенесено из критериев первого loop (T13): на S0 STATE/DECISIONS пусты, улик для Challenge нет по построению. Первый loop оценивается только по механике Capture → Distill → Retrieve.

---

*MAIN_ASSISTANT_DISCOVERY v1.1 | История Discovery до Stage S0 | Не CORE, не постоянная память*
