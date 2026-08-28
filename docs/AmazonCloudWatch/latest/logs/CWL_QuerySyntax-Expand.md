---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-Expand.html
---

# expand
<a name="CWL_QuerySyntax-Expand"></a>

Use `expand` to take a field containing a JSON array and create a separate log event for each element in the array. All other fields from the original log event are duplicated in each new event.

**Syntax**

```
expand {{fieldName}}
```

**Example**

If a log event contains `items = ["apple","banana","cherry"]` and `host = "web-01"`, then `expand items` produces three log events: `{items: "apple", host: "web-01"}`, `{items: "banana", host: "web-01"}`, and `{items: "cherry", host: "web-01"}`.

```
expand items
| stats count(*) by items, host
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
