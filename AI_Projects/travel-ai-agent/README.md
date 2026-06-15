# travel-ai-agent

Прототип Travel-agent (MVP) — CLI, использующий мок-данные или OpenStreetMap для генерации рекомендаций по поездке.

Запуск (в корне репозитория):

```bash
python AI_Projects\travel-ai-agent\cli.py --city "Barcelona" --days 3 --profile family
```

С использованием OpenStreetMap:

```bash
python AI_Projects\travel-ai-agent\cli.py --city "Barcelona" --days 3 --profile family --source osm
```

Агент возвращает JSON со списком мест и базовой нормализацией категорий/адресов. Дальше: интеграция дополнительных источников и HTTP API.
