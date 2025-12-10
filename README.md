# Sistema Experto: Consultor de Hardware

## Indice / Содержание

- [Русский](#русский)

Proyecto académico de sistema experto para recomendar equipos de cómputo
(PC/portátil) según propósito de uso, presupuesto y movilidad.

## Estructura del proyecto

- `src/` código fuente
  - `main.py` punto de entrada (menú principal)
  - `interfaz_usuario.py` modo usuario (consultas)
  - `interfaz_experto.py` modo experto (editor de reglas)
  - `motor_inferencia.py` motor de inferencia basado en reglas
  - `base_conocimientos.py` lectura/escritura de la base de conocimientos
  - `modelos.py` modelos de datos (Regla, etc.)
- `data/reglas.json` base de conocimientos (reglas en formato JSON)

## Cómo ejecutar

1. Abrir el proyecto en PyCharm.
2. Ejecutar `main.py` (Run → Run 'main').
3. Elegir:
   - Modo usuario para obtener recomendaciones.
   - Modo experto para editar reglas.


    

## Русский
# Экспертная система: Консультант по выбору компьютерной техники


Учебный проект экспертной системы для рекомендаций по выбору компьютера
(настольный ПК или ноутбук) в зависимости от назначения, бюджета и требований
к мобильности.

## Структура проекта

- `src/` исходный код
  - `main.py` точка входа (главное меню)
  - `interfaz_usuario.py` режим пользователя (получение рекомендаций)
  - `interfaz_experto.py` режим эксперта (редактор правил)
  - `motor_inferencia.py` механизм логического вывода на основе правил
  - `base_conocimientos.py` загрузка и сохранение базы знаний
  - `modelos.py` модели данных (класс правила и др.)
- `data/reglas.json` база знаний (набор правил в формате JSON)
- `README.md` описание проекта на испанском / английском
- `README_ru.md` описание проекта на русском

## Назначение системы

Система задаёт пользователю несколько вопросов:

- Для каких задач нужен компьютер (игры, офис, учёба, видео и др.).
- Каков доступный бюджет (низкий, средний, высокий).
- Какой тип устройства предпочтителен (настольный ПК или ноутбук).

На основе ответов система подбирает подходящие конфигурации из базы правил и
выдаёт рекомендации по:

- типу устройства (игровой ПК, офисный ноутбук, рабочая станция и т.п.);
- примерной аппаратной конфигурации (процессор, объём ОЗУ, диск, видеокарта);
- возможным брендам.

## Запуск проекта

1. Установить Python (3.x) и открыть проект в PyCharm или другой IDE.
2. Убедиться, что структура каталогов следующая:

   - корень проекта
     - `src/`
     - `data/`
     - `README.md`
     - `README_ru.md`

3. В IDE создать конфигурацию запуска для файла `src/main.py`.
4. Запустить проект (Run → Run `main`).

## Режимы работы

После запуска `main.py` в консоли появится меню:

- **Режим пользователя**  
  Пошаговый опрос (выбор вариантов по номеру) и вывод рекомендаций по выбору
  компьютерной техники.

- **Режим эксперта**  
  Просмотр, добавление, изменение и удаление правил в базе знаний
  (`data/reglas.json`) через простое текстовое меню.

## База знаний

База знаний хранится в файле `data/reglas.json` в виде набора продукционных
правил вида «ЕСЛИ условия, ТО рекомендация». Каждое правило описывает:

- условия (назначение, бюджет, мобильность);
- текстовую рекомендацию по типу устройства;
- рекомендуемую конфигурацию и возможные марки устройств.

При необходимости список правил можно расширять в режиме эксперта без
изменения исходного кода.
