---
source_url: https://docs.aws.amazon.com/grafana/latest/userguide/timestream-query-editor.html
---

# Using the Timestream data source
<a name="timestream-query-editor"></a>

## Query editor
<a name="timestream-query-editor"></a>

 The query editor accepts Timestream syntax in addition to the macros listed previously and any dashboard template variables.

 Press **Ctrl\+Space** to open the IntelliSense suggestions.

## Macros
<a name="timestream-macros"></a>

 To simplify syntax and to allow for dynamic parts, such as date range filters, the query can contain macros.

|  Macro example  |  Description  |
| --- | --- |
| *$\_\_database* |  Will specify the selected database. This uses the default from the data source configuration, or the explicit value from the query editor.  |
| *$\_\_table* |  Will specify the selected database. This uses the default from the datasource config, or the explicit value from the query editor.  |
| *$\_\_measure* |  Will specify the selected measure. This uses the default from the datasource config, or the explicit value from the query editor.  |
| *$\_\_timeFilter* |  Will be replaced by an expression that limits the time to the dashboard range  |
| *$\_\_interval\_ms* |  Will be replaced by a number that represents the amount of time a single pixel in the graph should cover.  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Grafana. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query grafana` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
