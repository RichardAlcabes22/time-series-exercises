<style>
@import url('https://fonts.googleapis.com/css?family=Open+Sans&display=swap');
body, html { height: 100%; }
body {
    font-family: 'Open Sans', sans-serif;
    max-width: 960px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-around;
}
th, td { padding: .5em 1em; }
thead tr { border-bottom: 1px solid #AAA; }
th { font-weight: bold; }
table { width: 100%; table-layout: fixed; border-collapse: collapse; }
th:nth-child(1), td:nth-child(1) { width: 10%; }
th:nth-child(2), td:nth-child(2) { width: 10%; }
th:nth-child(3), td:nth-child(3) { width: 80%; }

tr:nth-child(odd) { background: rgba(0, 0, 0, .05); }
thead > tr { background: white !important; }

code { font-size: 1.3em; }

</style>
# `strftime` Format Specifiers

| Units       | Specifier | Description                                                    |
| ---         | --------- | -----------                                                    |
| **seconds** | `%S`      | Second of the minute (00..60)                                  |
| **minutes** | `%M`      | Minute of the hour (00..59)                                    |
| **hours**   | `%H`      | Hour of the day, 24-hour clock (00..23)                        |
|             | `%I`      | Hour of the day, 12-hour clock (01..12)                        |
| **days**    | `%d`      | Day of the month                                               |
|             | `%a`      | The abbreviated weekday name ("Sun")                           |
|             | `%A`      | The full weekday name ("Sunday")                               |
|             | `%j`      | Day of the year (001..366)                                     |
|             | `%w`      | Day of the week, Sunday is 0 (0..6)                            |
| **weeks**   | `%U`      | Week of the year, Sunday is the first day of the week (00..53) |
|             | `%W`      | Week of the year, Monday is the first day of the week (00..53) |
| **months**  | `%b`      | The abbreviated month name ("Jan")                             |
|             | `%B`      | The full month name ("January")                                |
|             | `%d`      | Day of the month (01..31)                                      |
|             | `%m`      | Month of the year (01..12)                                     |
| **years**   | `%y`      | Year without a century (00..99)                                |
|             | `%Y`      | Year with century (1999)                                       |
| **misc**    | `%z`      | Time zone offset (-0500)                                       |
|             | `%Z`      | Time zone name ("CDT")                                         |
|             | `%p`      | Meridian indicator ("AM" or "PM")                              |
|             | `%c`      | The preferred local date and time representation               |
|             | `%x`      | Preferred representation for the date alone, no time           |
|             | `%X`      | Preferred representation for the time alone, no date           |
