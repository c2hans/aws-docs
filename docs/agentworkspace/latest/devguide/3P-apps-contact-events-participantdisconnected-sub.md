---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-events-participantdisconnected-sub.html
---

# Subscribe to participant disconnected events in Connect Customer agent workspace
<a name="3P-apps-contact-events-participantdisconnected-sub"></a>

Subscribes to participant disconnected events. This event fires when a participant leaves or is removed from a contact.

 **Signature**

```
onParticipantDisconnected(handler: ParticipantDisconnectedHandler, contactId?: string): void
```

 **Usage**

```
const handleParticipantDisconnected = (event) => {
    console.log(`Participant disconnected: ${event.participant.participantId}`);
};

contactClient.onParticipantDisconnected(
    handleParticipantDisconnected,
    "contact-123"
);
```

 **Input**

|  **Parameter**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| handler Required | ParticipantDisconnectedHandler | Event handler function to call when participants disconnect |
| contactId | string | Optional contact ID to filter events for a specific contact |

 **Event Structure - ParticipantDisconnected**

The handler receives a ParticipantDisconnected event with:
+ `participant`: ParticipantData - The participant that was disconnected

 **Permissions required:**

```
Contact.Details.View
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
