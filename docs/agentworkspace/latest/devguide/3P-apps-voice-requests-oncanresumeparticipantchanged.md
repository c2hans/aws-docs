---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-voice-requests-oncanresumeparticipantchanged.html
---

# Subscribe to participant resume capability change events in Connect Customer agent workspace
<a name="3P-apps-voice-requests-oncanresumeparticipantchanged"></a>

Subscribes to events when a participant's capability to be resumed from hold changes.

 **Signature**

```
onCanResumeParticipantChanged(
  handler: CanResumeParticipantChangedHandler,
  participantId?: string
): void
```

 **Usage**

```
const handleCanResumeChanged = (event) => {
  console.log(`Participant ${event.participantId} resume capability: ${event.canResumeConnection}`);
  if (event.canResumeConnection) {
    // Enable resume button for this participant
  } else {
    // Disable resume button for this participant
  }
};
voiceClient.onCanResumeParticipantChanged(handleCanResumeChanged, "participant-456");
```

 **Input**

|  **Parameter**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| handler Required | CanResumeParticipantChangedHandler | Event handler function to call when the capability changes |
| participantId | string | Optional participant ID to filter events for a specific participant |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
