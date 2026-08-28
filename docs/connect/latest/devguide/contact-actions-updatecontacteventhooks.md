---
source_url: https://docs.aws.amazon.com/connect/latest/devguide/contact-actions-updatecontacteventhooks.html
---

# UpdateContactEventHooks
<a name="contact-actions-updatecontacteventhooks"></a>

Sets one or more contact event hooks, which are flows associated with contact events, such as customer whisper or agent hold. For more information, see [Contact records data model](https://docs.aws.amazon.com/connect/latest/adminguide/ctr-data-model.html). The following event hooks are valid:
+ AgentHold
+ AgentWhisper
+ CustomerHold
+ CustomerQueue
+ CustomerRemaining
+ CustomerWhisper
+ DefaultAgentUI
+ DisconnectAgentUI
+ PauseContact
+ ResumeContact

## Parameter object
<a name="updatecontacteventhooks-parameter"></a>

```
{
    "EventHooks": { an Object that holds the event hooks to be set. Only one entry may be present in this map.
        "Key": "Value" - the event hook to be set where the key is the event type and the value is the flow ID or ARN to run when that event occurs. Keys must be defined statically.
    }
}
```

## Results and conditions
<a name="updatecontacteventhooks-results"></a>

None.

## Errors
<a name="updatecontacteventhooks-errors"></a>
+ NoMatchingError - if no other Error matches.

## Restrictions
<a name="updatecontacteventhooks-restrictions"></a>

This is supported in all types of flows.

## Corresponding blocks in the UI
<a name="updatecontacteventhooks-ui"></a>
+  [Set customer queue flow](https://docs.aws.amazon.com/connect/latest/adminguide/set-customer-queue-flow.html)
+ [Set event flow](https://docs.aws.amazon.com/connect/latest/adminguide/set-event-flow.html)
+ [Set hold flow](https://docs.aws.amazon.com/connect/latest/adminguide/set-hold-flow.html)
+ [Set whisper flow](https://docs.aws.amazon.com/connect/latest/adminguide/set-whisper-flow.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
