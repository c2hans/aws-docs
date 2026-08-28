---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-voice-requests-onselfhold.html
---

# Subscribe to self hold events in Connect Customer agent workspace
<a name="3P-apps-voice-requests-onselfhold"></a>

Subscribes to events when the current user's participant is put on hold.

 **Signature**

```
onSelfHold(
  handler: ParticipantHoldHandler,
  contactId?: string
): void
```

 **Usage**

```
const handleSelfHold = (event) => {
  console.log("You have been put on hold");
  console.log(`Contact: ${event.contactId}`);
};
// Subscribe to all contacts
voiceClient.onSelfHold(handleSelfHold);
// Or subscribe to a specific contact
voiceClient.onSelfHold(handleSelfHold, "contact-123");
```

 **Input**

|  **Parameter**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| handler Required | ParticipantHoldHandler | Event handler function to call when the current user's participant is put on hold |
| contactId | string | Optional contact ID to filter events for a specific contact |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
