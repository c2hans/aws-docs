---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/userguide/sql-functions-null.html
---

# Null data functions
<a name="sql-functions-null"></a>

 Null data functions handle or manipulate NULL values, which represent the absence of a value. The functions allow you to replace NULLs with other values, check if a value is NULL, or perform operations that handle NULLs in a specific way.

|  **Function**  |  **Signature**  |  **Description**  |
| --- | --- | --- |
| `COALESCE` |  COALESCE (expression1, expression2, ..., expressionN)  | If all expressions evaluate to null, COALESCE returns null. Expressions must be of same type. |

**Example of a COALESCE function**

```
SELECT COALESCE (l.double_value, 100) AS non_double_value FROM latest_value_time_series AS l LIMIT 1
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
