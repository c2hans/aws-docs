---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-events-participantadded-sub.html
---

# Subscribe to participant added events in Connect Customer agent workspace
<a name="3P-apps-contact-events-participantadded-sub"></a>

Subscribes to participant added events. This event fires when a new participant joins a contact.

 **Signature**

```
onParticipantAdded(handler: ParticipantAddedHandler, contactId?: string): void
```

 **Usage**

```
const handleParticipantAdded = (event) => {
    console.log(`New participant added: ${event.participant.participantId}`);
    console.log(`Type: ${event.participant.type.value}`);
};

// Subscribe to all contacts
contactClient.onParticipantAdded(handleParticipantAdded);

// Or subscribe to a specific contact
contactClient.onParticipantAdded(handleParticipantAdded, "contact-123");
```

 **Input**

|  **Parameter**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| handler Required | ParticipantAddedHandler | Event handler function to call when participants are added |
| contactId | string | Optional contact ID to filter events for a specific contact |

 **Event Structure - ParticipantAdded**

The handler receives a ParticipantAdded event with:
+ `participant`: ParticipantData - The participant that was added

 **Permissions required:**

```
*
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
