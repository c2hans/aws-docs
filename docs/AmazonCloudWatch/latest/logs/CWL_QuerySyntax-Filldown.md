---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-Filldown.html
---

# filldown
<a name="CWL_QuerySyntax-Filldown"></a>

Use the `filldown` command to carry the last non-null value forward to fill gaps. You can specify field names or use wildcards. If you do not specify fields, all fields are filled.

**Syntax**

```
| filldown [{{field1}} [{{field2}} ...]]
```

The command uses the following arguments:
+ `{{field}}` (Optional) – One or more field names or wildcard patterns. If omitted, all fields are filled.

**Example**
The following query carries forward non-null values in the `host` field and all fields matching `cpu*`.

```
fields @timestamp, host, cpu_user, cpu_system
| filldown host cpu*
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
