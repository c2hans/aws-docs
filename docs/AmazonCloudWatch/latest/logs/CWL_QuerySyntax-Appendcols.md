---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-Appendcols.html
---

# appendcols
<a name="CWL_QuerySyntax-Appendcols"></a>

Use the `appendcols` command to append a sub-query's columns to the current results by positional row matching.

**Syntax**

```
| appendcols [override=true|false] [max={{n}}] ( {{subquery}} )
```

The command uses the following arguments:
+ `override` (Optional) – Whether to overwrite existing fields. Default: `false`.
+ `max` (Optional) – Maximum rows to process (1–100000, default 10000).
+ `{{subquery}}` – A complete CloudWatch Logs Insights query enclosed in parentheses.

**Example**
The following query appends average latency per service from another log group.

```
fields svc
| stats count(*) as cnt by svc
| appendcols override=true ( SOURCE lg | stats avg(latency) as avgLat by svc )
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
