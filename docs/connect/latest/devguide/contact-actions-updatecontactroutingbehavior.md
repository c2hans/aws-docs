---
source_url: https://docs.aws.amazon.com/connect/latest/devguide/contact-actions-updatecontactroutingbehavior.html
---

# UpdateContactRoutingBehavior
<a name="contact-actions-updatecontactroutingbehavior"></a>

Updates the contact's routing details. This can move the contact forward or backward in queue, or specify a queue priority.

## Parameter object
<a name="updatecontactroutingbehavior-parameter"></a>

```
{
  "QueuePriority": An integer that represents the queue priority to be applied to the contact (lower priorities are routed preferentially). Cannot be specified if QueueTimeAdjustmentSeconds is specified. Must be statically defined, must be larger than zero, and a valid integer value.
  "QueueTimeAdjustmentSeconds": An integer that represents the queue time adjust to be applied to the contact, in seconds (longer / larger queue times are routed preferentially). Cannot be specified if QueuePriority is specified. Must be statically defined and a valid integer value.
}
```

## Results and conditions
<a name="updatecontactroutingbehavior-results"></a>

None.

## Errors
<a name="updatecontactroutingbehavior-errors"></a>

None.

## Restrictions
<a name="updatecontactroutingbehavior-restrictions"></a>

This is supported only in inbound contact flows. It is not supported in transfer flows, whisper flows, customer queue flows, or hold flows.

## Corresponding block in the UI
<a name="updatecontactroutingbehavior-ui"></a>

[Change routing priority / age](https://docs.aws.amazon.com/connect/latest/adminguide/change-routing-priority.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
