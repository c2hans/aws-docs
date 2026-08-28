---
source_url: https://docs.aws.amazon.com/connect/latest/devguide/participant-actions-showview.html
---

# ShowView
<a name="participant-actions-showview"></a>

Initiates a UI-based workflow that can be surfaced to users of front end applications. This action can be used to create [step-by-step guides ](https://docs.aws.amazon.com/connect/latest/adminguide/step-by-step-guided-experiences.html) for agents who are using the Connect Customer agent workspace.

## Parameter object
<a name="showview-parameter"></a>

```
{
    "ViewResource": {
        "Id": "{{Id of the View Resource that will be shown in the UI.}}",
        "Version": "{{Version of the View Resource that will be shown in the UI.}}"
    },
    "InvocationTimeLimitSeconds": 400,
    "ViewData": {
        "Description": "{{An optional map of data that will be passed to the View Resource. Keys and values may be set statically or dynamically.}}"
    },
    "SensitiveDataConfiguration": {
        "HideResponseOn": ["{{TRANSCRIPT}}"]
    }
}
```

## Results and conditions
<a name="showview-results"></a>

The result that the user selects when interacting with the View. The available conditions will be dependent on the View resource specified in action parameters.

## Errors
<a name="showview-errors"></a>
+ NoMatchingError - if no other Error matches.
+ NoMatchingCondition - if no other Condition matches.
+ TimeLimitExceeded - if there is no response before the configured `InvocationTimeLimitSeconds`.

## Restrictions
<a name="showview-restrictions"></a>

This action is only supported on the chat channel.

This action can be used in inbound flows and customer queue flows.

To ensure reliable show view rendering, limit combined inputs and contact attributes to 16KB or less.

## Corresponding block in the UI
<a name="showview-ui"></a>

 [Show View](https://docs.aws.amazon.com/connect/latest/adminguide/show-view-block.html)

This action routes step-by-step guides that are to be displayed to agents in the agent workspace. It routes the guides as chat contacts. This type of chat contact is different from the customer-based contact that the agent is handling.

This action can only be used in inbound contact flows.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
