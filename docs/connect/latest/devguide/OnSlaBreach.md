---
source_url: https://docs.aws.amazon.com/connect/latest/devguide/OnSlaBreach.html
---

# OnSlaBreach
<a name="OnSlaBreach"></a>

## Cases SLA name condition
<a name="OnSlaBreach-csnc-condition"></a>

**Parameters**
+ Operator - “CONTAINS\_ANY”
+ Operands – A list of SLA names.
+ ComparisonValue – "$.RelatedItem.SlaConfiguration.Name"
+ Negate - false

```
{
"Operator": "CONTAINS_ANY",
"Operands": ["highPrioritySla"],
"ComparisonValue": "$.RelatedItem.SlaConfiguration.Name",
"Negate": false
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
