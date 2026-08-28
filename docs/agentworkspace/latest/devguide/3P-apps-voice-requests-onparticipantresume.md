---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-voice-requests-onparticipantresume.html
---

# Subscribe to participant resume events in Connect Customer agent workspace
<a name="3P-apps-voice-requests-onparticipantresume"></a>

Subscribes to events when any participant is taken off hold.

 **Signature**

```
onParticipantResume(
  handler: ParticipantResumeHandler,
  participantId?: string
): void
```

 **Usage**

```
const handleParticipantResume = (event) => {
  console.log(`Participant ${event.participantId} has been resumed`);
};
voiceClient.onParticipantResume(handleParticipantResume, "participant-456");
```

 **Input**

|  **Parameter**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| handler Required | ParticipantResumeHandler | Event handler function to call when participants are taken off hold |
| participantId | string | Optional participant ID to filter events for a specific participant |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
