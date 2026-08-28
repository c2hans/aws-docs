---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-Fillmissing.html
---

# fillmissing
<a name="CWL_QuerySyntax-Fillmissing"></a>

Use the `fillmissing` command to insert rows for empty time bins after `stats ... by bin()`. You can optionally fill fields with a constant value.

**Syntax**

```
| fillmissing [with {{value}} for {{field}} [, {{value}} for {{field}} ...]]
```

The command uses the following arguments:
+ `with {{value}} for {{field}}` (Optional) – The constant value to assign to the specified field in the inserted rows.

**Example**
The following query fills empty 1-minute bins with 0 for the `avg_latency` field.

```
fields @timestamp, latency
| stats avg(latency) as avg_latency by bin(1m)
| fillmissing with 0 for avg_latency
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
