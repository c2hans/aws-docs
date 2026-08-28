---
source_url: https://docs.aws.amazon.com/connect/latest/devguide/flow-control-actions-compare.html
---

# Compare
<a name="flow-control-actions-compare"></a>

Allows comparisons against the specified value.

## Parameter object
<a name="compare-parameter"></a>

```
{
  "ComparisonValue": Any **single** JSONPath identifier that is valid for the flow data object
}
```

## Execution results and conditions
<a name="compare-results"></a>

The value specified for comparison. This can be used for conditions.

## Errors
<a name="compare-errors"></a>
+ NoMatchingCondition - if no other Condition matches.

## Restrictions
<a name="compare-restrictions"></a>

This action is available in every type of flow.

## Corresponding block in the UI
<a name="compare-ui"></a>

[Check contact attributes](https://docs.aws.amazon.com/connect/latest/adminguide/check-contact-attributes.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
