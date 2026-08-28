---
source_url: https://docs.aws.amazon.com/iot/latest/developerguide/iot-sql-where.html
---

# WHERE clause
<a name="iot-sql-where"></a>

The WHERE clause determines if the actions specified by a rule are carried out. If the WHERE clause evaluates to true, the rule actions are performed. Otherwise, the rule actions are not performed.

The WHERE clause supports [Data types](iot-sql-data-types.md), [Operators](iot-sql-operators.md), [Functions](iot-sql-functions.md), [Literals](iot-sql-literals.md), [Case statements](iot-sql-case.md), [JSON extensions](iot-sql-json.md), [Variables](iot-sql-set.md#iot-sql-set-usage), and [Nested object queries](iot-sql-nested-queries.md).

**Example:**

Incoming payload published on `topic/subtopic`: `{"color":"red", "temperature":40}`.

SQL: `SELECT color AS my_color FROM 'topic/subtopic' WHERE temperature > 50 AND color <> 'red'`.

In this case, the rule will be triggered, but the actions specified by the rule will not be performed. There will be no outgoing payload.

You can use functions and operators in the WHERE clause. However, you cannot reference any aliases created with the AS keyword in the SELECT. The WHERE clause is evaluated first, to determine if SELECT is evaluated.

**Example with non-JSON payload:**

Incoming non-JSON payload published on `topic/subtopic`: `80`

SQL: ``SELECT decode(encode(*, 'base64'), 'base64') AS value FROM 'topic/subtopic' WHERE decode(encode(*, 'base64'), 'base64') > 50`

In this case, the rule will be triggered, and the actions specified by the rule will be performed. The outgoing payload will be transformed by the SELECT clause as a JSON payload `{"value":80}`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Core. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
