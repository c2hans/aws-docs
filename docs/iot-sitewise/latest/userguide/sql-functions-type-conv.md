---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/userguide/sql-functions-type-conv.html
---

# Type conversion functions
<a name="sql-functions-type-conv"></a>

 Type conversion functions are used to change the data type of a value from one to another. They are essential for ensuring data compatibility and performing operations that require data in a specific format.

|  **Function**  |  **Signature**  |  **Description**  |
| --- | --- | --- |
| `TO_DATE` |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/sql-functions-type-conv.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/sql-functions-type-conv.html)  |
| `TO_TIMESTAMP` |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/sql-functions-type-conv.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/sql-functions-type-conv.html)  |
| `TO_TIME` |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/sql-functions-type-conv.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/sql-functions-type-conv.html)  |
| `CAST` | CAST (<expression> AS <data type>) | Converts an entity, or expression that evaluates to a single value, from one type to another.<br />Supported data types are:[See the AWS documentation website for more details](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/sql-functions-type-conv.html) |

**Example of a SQL query using the listed functions:**

```
SELECT TO_TIMESTAMP (100) AS timestamp_value,
  TO_DATE(r.event_timestamp) AS date_value,
  TO_TIME(r.event_timestamp) AS time_value
FROM raw_time_series AS r
```
