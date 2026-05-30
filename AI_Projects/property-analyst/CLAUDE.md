---
Проект: property-analyst
Тип: Local Builder Instructions
Статус: Stage 1 — Working Prototype
Дата: 2026-05-30
Связанные файлы: [[PROJECT_DNA.md]] | [[ROADMAP.md]] | [[START.md]]
---

# CLAUDE.md — property-analyst
## Инструкции для Локального Строителя (Уровень 2)

---

## Твоя роль

Ты — Локальный Строитель этого проекта. Уровень 2.
Ты получил задачу от MAIN_ENGINEER и работаешь автономно.
Твой результат — рабочий working loop, не красивая архитектура.

---

## Текущий Stage: 1 — Working Prototype

**Цель Stage 1:** получить первый PDF-отчёт по реальному объекту.

**Начинай с Phase 1 — Manual Proof.**
Проверь все API вручную прежде чем писать код.

---

## Архитектура

Полная архитектура зафиксирована в `PROJECT_DNA.md`.
Не отступать без явного решения Марии.

---

## Структура файлов — имена несут ответственность

```
property-analyst/
├── main.py              ← CLI точка входа, оркестрация
├── config.py            ← параметры, константы, env
├── cian_client.py       ← ТОЛЬКО Циан: объект + аналоги
├── geo_client.py        ← ТОЛЬКО 2GIS / Яндекс: локация
├── market_scorer.py     ← ТОЛЬКО формулы: цена/м², перцентиль, отклонение
├── narrative_engine.py  ← ТОЛЬКО AI нарратив на данных слоёв 1-4
├── report_renderer.py   ← ТОЛЬКО сборка и рендер PDF
├── qa_card.py           ← ТОЛЬКО генерация feedback card
├── prompts/             ← промпты для narrative_engine
├── logs/                ← лог каждого запуска
├── reports/             ← выходные PDF
├── .env
├── .env.example
└── requirements.txt
```

**Naming rule:** имя файла отвечает на вопрос "что здесь разрешено — а что уже нарушение архитектуры?"

`cian_client.py` не работает с 2GIS.
`narrative_engine.py` не считает формулы.
`market_scorer.py` не вызывает AI.

---

## Deterministic / AI граница — ЖЁСТКОЕ ПРАВИЛО

```
cian_client.py    →  формула, нет AI
geo_client.py     →  формула, нет AI
market_scorer.py  →  формула, нет AI
narrative_engine  →  AI только на данных трёх модулей выше
report_renderer   →  числа из market_scorer, текст из narrative_engine
```

AI не пересчитывает числа. AI не добавляет факты.

---

## Anti-Hallucination — КРИТИЧНО

Это client-facing система. Ошибка = репутационный риск.

**Три уровня защиты обязательны:**
1. `narrative_engine.py` получает только структурированный JSON из слоёв 1-4
2. AI заполняет шаблон с полями — не пишет свободный нарратив
3. `report_renderer.py` сверяет числа в тексте с числами из `market_scorer.py`

**При отсутствии данных:**
- Некритичный фактор → пропустить молча
- Критичный (аналоги, цена/м² рынка, координаты) → пометить явно в отчёте

---

## Quality Gates — не переходить без прохождения

**Gate 1 — API Reality (первое действие)**
- [ ] `cian_client.py` — response structure проверена вручную
- [ ] `geo_client.py` — API проверен вручную, rate limits известны
- [ ] Claude API — вызов работает
- [ ] Все ключи в .env, не в коде

**Gate 2 — Working Loop**
- [ ] `cian_client.py` возвращает данные объекта и аналоги
- [ ] `market_scorer.py` считает цену/м², перцентиль, отклонение
- [ ] `narrative_engine.py` генерирует нарратив без галлюцинаций
- [ ] `report_renderer.py` собирает корректный PDF
- [ ] `qa_card.py` выводит feedback card в консоль

**Gate 3 — Stability**
- [ ] Retries при ошибках API в `cian_client.py` и `geo_client.py`
- [ ] Каждый запуск пишет лог в `logs/`
- [ ] .env.example актуален

---

## Logging — с первого запуска

Каждый запуск логирует:
- Входные параметры
- Количество найденных аналогов
- Ключевые числа из `market_scorer.py`
- Статус AI вызова
- Путь к PDF

Без логов нельзя калибровать.

---

## STOP CONDITIONS — остановись и спроси Марию

- API вернул неожиданную структуру данных
- Аналогов не найдено по заданным фильтрам
- `narrative_engine.py` вернул факты без источника в данных
- Нужно отступить от зафиксированной архитектуры

---

## Автономные триггеры

| Ситуация | Действие |
|---|---|
| Работа с внешним API | Context7 для актуальной документации |
| Текст идёт клиенту | Humanizer обязателен |
| Код готов к сдаче | ChatGPT /codex:review перед сдачей Марии |
| Сложная многошаговая задача | Sequential Thinking |

---

*property-analyst CLAUDE.md v1.0 | 2026-05-30*
