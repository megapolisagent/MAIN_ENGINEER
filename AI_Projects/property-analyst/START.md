---
Проект: property-analyst
Тип: Agent Bootstrap
Статус: Stage 1 — Working Prototype
Дата: 2026-05-30
Связанные файлы: [[PROJECT_DNA.md]] | [[CLAUDE.md]] | [[ROADMAP.md]]
---

# START.md — property-analyst
## Протокол саморазвёртывания агента

---

## Первое действие

Прочитай в этом порядке:
1. `PROJECT_DNA.md` — контекст бизнеса и репутационные запреты
2. `CLAUDE.md` — твои правила и границы
3. `ROADMAP.md` — план по фазам

Начинай с **Phase 0 — Manual Proof**.
Не пиши код пока не проверил все API вручную.

---

## Capabilities — твой инструментарий

### Skills
| Инструмент | Когда |
|---|---|
| Sequential Thinking | Анализ объекта, многошаговые задачи |
| Humanizer | Любой текст перед выдачей клиенту — обязательно |
| data-scraper-agent | Парсинг Циан |
| market-research | Анализ рынка и позиционирование |

### MCP
| Инструмент | Когда |
|---|---|
| Filesystem | Чтение/запись файлов — всегда |
| Context7 | Документация API при каждом внешнем вызове |
| Tavily | Актуальные рыночные данные, проверка района |
| Exa | Семантический поиск по объектам и локации |

### Integrations
| Инструмент | Когда |
|---|---|
| ChatGPT /codex:review | Обязательно перед сдачей кода Марии |
| Google Drive | Stage 2 — автодоставка PDF |

### Infra
- Локальный агент, Python
- JSON — промежуточное хранение между модулями
- PDF — финальный выход в `reports/`
- Filesystem как source of truth

### Browser
- Playwright → только Циан

### APIs
| API | Модуль | Назначение |
|---|---|---|
| Циан API | `cian_client.py` | Данные объекта + аналоги |
| 2GIS или Яндекс Карты API | `geo_client.py` | Данные локации |
| Claude API | `narrative_engine.py` | AI reasoning и нарратив |

### Orchestration
- Получаешь задачу от MAIN_ENGINEER (Уровень 1)
- Работаешь автономно
- Возвращаешь PDF → Мария отправляет клиенту руками

---

## Автономные триггеры

| Ситуация | Действие |
|---|---|
| Работа с любым внешним API | Сначала Context7 — актуальная документация |
| Любой текст идёт клиенту | Humanizer — без исключений |
| Код готов | ChatGPT /codex:review перед сдачей |
| Многошаговый анализ | Sequential Thinking |

---

## Working Loop Stage 1

```
CLI → URL объекта + контекст A/B/C + enrichment block
  ↓
cian_client.py    → данные объекта + аналоги (JSON)
geo_client.py     → данные локации (JSON)
  ↓
market_scorer.py  → цена/м², перцентиль, отклонение, сегмент (JSON)
  ↓
narrative_engine.py → нарратив строго на данных выше (текст)
  ↓
report_renderer.py  → PDF → reports/
  ↓
qa_card.py          → feedback card в консоль
```

---

## STOP CONDITIONS

Остановись и доложи Марии если:
- API вернул неожиданную структуру данных
- Аналогов не найдено по фильтрам
- `narrative_engine.py` вернул факты без источника
- Нужно отступить от зафиксированной архитектуры
- Ошибка повторяется 3 раза подряд

---

## Что НЕ делать

- Не создавать папки "на будущее"
- Не объединять `cian_client.py` и `geo_client.py` — разные instability sources
- Не давать `narrative_engine.py` доступ к формулам
- Не добавлять AI туда где работают формулы
- Не сдавать код без ChatGPT review

---

*property-analyst START.md v1.0 | 2026-05-30*
