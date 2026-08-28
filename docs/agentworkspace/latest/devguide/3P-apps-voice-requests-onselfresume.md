---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-voice-requests-onselfresume.html
---

# Subscribe to self resume events in Connect Customer agent workspace
<a name="3P-apps-voice-requests-onselfresume"></a>

Subscribes to events when the current user's participant is taken off hold.

 **Signature**

```
onSelfResume(
  handler: ParticipantResumeHandler,
  contactId?: string
): void
```

 **Usage**

```
const handleSelfResume = (event) => {
  console.log("You have been resumed from hold");
};
voiceClient.onSelfResume(handleSelfResume, "contact-123");
```

 **Input**

|  **Parameter**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| handler Required | ParticipantResumeHandler | Event handler function to call when the current user's participant is taken off hold |
| contactId | string | Optional contact ID to filter events for a specific contact |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
