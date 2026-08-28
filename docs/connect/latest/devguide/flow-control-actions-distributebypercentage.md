---
source_url: https://docs.aws.amazon.com/connect/latest/devguide/flow-control-actions-distributebypercentage.html
---

# DistributeByPercentage
<a name="flow-control-actions-distributebypercentage"></a>

Returns a random number between 1 and 100 (inclusive) as its result, allowing comparisons against it.

## Parameter object
<a name="distributebypercentage-parameter"></a>

```
{

}
```

## Results and conditions
<a name="distributebypercentage-results"></a>

A number between 1 and 100, inclusive, chosen randomly. Comparisons are supported, but they must be a chain of NumericLessThan comparisons, with each subsequent comparison checking the previous value, plus the percentage that is desired to go down this next action, and no Comparison comparing a value larger than 100.

## Errors
<a name="distributebypercentage-errors"></a>
+ NoMatchingCondition if no Condition matches. This is the default option in the flow editor.

## Restrictions
<a name="distributebypercentage-restrictions"></a>

This action is available in inbound flows, transfer flows, and customer queue flows. It is not available to hold flows or to whisper flows.

## Corresponding block in the UI
<a name="distributebypercentage-ui"></a>

[Distribute by percentage](https://docs.aws.amazon.com/connect/latest/adminguide/distribute-by-percentage.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
