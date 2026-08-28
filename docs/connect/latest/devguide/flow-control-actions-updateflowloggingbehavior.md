---
source_url: https://docs.aws.amazon.com/connect/latest/devguide/flow-control-actions-updateflowloggingbehavior.html
---

# UpdateFlowLoggingBehavior
<a name="flow-control-actions-updateflowloggingbehavior"></a>

Enables or disables flow logging. If this is a flow, this same behavior remains unless it is overridden for the rest of the contact segment. It is also automatically inherited by new segments in the chain.

## Parameter object
<a name="updateflowloggingbehavior-parameter"></a>

```
{
  "FlowLoggingBehavior": One of [Enabled,Disabled]. *Dynamic values are not supported*
}
```

## Results and conditions
<a name="updateflowloggingbehavior-results"></a>

None. No conditions are supported.

## Errors
<a name="updateflowloggingbehavior-errors"></a>

None.

## Restrictions
<a name="updateflowloggingbehavior-restrictions"></a>

This action is available in every type of flow.

## Corresponding block in the UI
<a name="updateflowloggingbehavior-ui"></a>

[Set logging behavior](https://docs.aws.amazon.com/connect/latest/adminguide/set-logging-behavior.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
