---
source_url: https://docs.aws.amazon.com/connect/latest/devguide/flow-control-actions-transfertoflow.html
---

# TransferToFlow
<a name="flow-control-actions-transfertoflow"></a>

Execution jumps to a different flow, and continues running at that flow's beginning.

## Parameter object
<a name="transfertoflow-parameter"></a>

```
{
    "ContactFlowId": A flow ID or flow ARN. *Must be either fully static or a single valid JSONPath identifier*
}
```

## Execution results and conditions
<a name="transfertoflow-results"></a>

None.

## Errors
<a name="transfertoflow-errors"></a>
+ NoMatchingError - if no other Error matches.

## Restrictions
<a name="transfertoflow-restrictions"></a>

This action is available in inbound flows and transfer flows. It is not available to hold flows, customer queue flows, or whisper flows.

## Corresponding block in the UI
<a name="transfertoflow-ui"></a>

[Transfer to flow](https://docs.aws.amazon.com/connect/latest/adminguide/transfer-to-flow.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
