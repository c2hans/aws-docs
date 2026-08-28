---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-Where.html
---

# where
<a name="CWL_QuerySyntax-Where"></a>

Use the `where` command as an alias for the `filter` command. It accepts identical syntax and behavior.

**Syntax**

```
| where {{condition}}
```

The command uses the following arguments:
+ `{{condition}}` – A boolean expression identical to what the `filter` command accepts.

**Example**
The following query filters for log events containing "error".

```
fields @timestamp, @message
| where @message like /error/
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
