---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/userguide/sql-functions-math.html
---

# Math functions
<a name="sql-functions-math"></a>

 Math functions are pre-defined mathematical operations used within SQL queries to perform calculations on numerical data. They provide ways to manipulate and transform data without needing to extract it from the database and process it separately.

**Math functions**

|  **Function**  |  **Signature**  |  **Description**  |
| --- | --- | --- |
| `POWER` | POWER (int\|double, int\|double) | Returns the value of first argument raised to the power of the second argument. |
| `ROUND` |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/sql-functions-math.html)  | Rounds to the nearest integer. |
| `FLOOR` |  FLOOR (int\|double)  | Returns the largest integer not greater than the value given. |

Examples of all functions:

|  **Function**  |  **Example**  |
| --- | --- |
| POWER |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/sql-functions-math.html)  |
| ROUND |  `ROUND (32.12435, 3)`  |
| FLOOR |  `FLOOR (21.2)`  |
