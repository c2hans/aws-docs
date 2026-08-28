---
source_url: https://docs.aws.amazon.com/iot/latest/developerguide/iot-sql-case.html
---

# Case statements
<a name="iot-sql-case"></a>

Case statements can be used for branching execution, like a switch statement.

Syntax:

```
CASE {{v}} WHEN {{t[1]}} THEN {{r[1]}}
  WHEN {{t[2]}} THEN {{r[2]}} ...
  WHEN {{t[n]}} THEN {{r[n]}}
  ELSE {{r[e]}} END
```

The expression {{`v`}} is evaluated and matched for equality against the {{`t[i]`}} value of each `WHEN` clause. If a match is found, the corresponding {{`r[i]`}} expression becomes the result of the `CASE` statement. The `WHEN` clauses are evaluated in order so that if there's more than one matching clause, the result of the first matching clause becomes the result of the `CASE` statement. If there are no matches, {{`r[e]`}} of the `ELSE` clause is the result. If there's no match and no `ELSE` clause, the result is `Undefined`.

`CASE` statements require at least one `WHEN` clause. An `ELSE` clause is optional.

For example:

Incoming payload published on topic `topic/subtopic`:

```
{
    "color":"yellow"
}
```

SQL statement:

```
SELECT CASE color
        WHEN 'green' THEN 'go'
        WHEN 'yellow' THEN 'caution'
        WHEN 'red' THEN 'stop'
        ELSE 'you are not at a stop light' END as instructions
    FROM 'topic/subtopic'
```

The resulting output payload would be:

```
{
    "instructions":"caution"
}
```

**Note**
If {{`v`}} is `Undefined`, the result of the case statement is `Undefined`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Core. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
