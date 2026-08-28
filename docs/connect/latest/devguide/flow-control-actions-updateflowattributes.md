---
source_url: https://docs.aws.amazon.com/connect/latest/devguide/flow-control-actions-updateflowattributes.html
---

# UpdateFlowAttributes
<a name="flow-control-actions-updateflowattributes"></a>

Sets a collection of attributes on the current flow. These attributes are not carried over to the subsequent flows. With this type of operation, either all attributes are set or none are set.

## Parameter object
<a name="updateflowattributes-parameter"></a>

```
{
    ""FlowAttributes": { An Object that holds the attributes to be set. Keys are of type String, Values are of type FlowAttribute
        "Type": {
            FlowAttribute" : "Value"
        }
    }
}
```

## Results and conditions
<a name="updateflowattributes-results"></a>

None. No conditions are supported.

## Errors
<a name="updateflowattributes-errors"></a>

None.

## Restrictions
<a name="updateflowloggingbehavior-restrictions"></a>

This action is supported on all channels and in all flow types.

## Corresponding block in the UI
<a name="updateflowloggingbehavior-ui"></a>

[Set contact attributes](https://docs.aws.amazon.com/connect/latest/adminguide/set-contact-attributes.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
