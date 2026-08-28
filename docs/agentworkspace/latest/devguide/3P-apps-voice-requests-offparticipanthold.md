---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-voice-requests-offparticipanthold.html
---

# Unsubscribe from participant hold events in Connect Customer agent workspace
<a name="3P-apps-voice-requests-offparticipanthold"></a>

Unsubscribes from participant hold events.

 **Signature**

```
offParticipantHold(
  handler: ParticipantHoldHandler,
  participantId?: string
): void
```

 **Usage**

```
voiceClient.offParticipantHold(handleParticipantHold);
```

 **Input**

|  **Parameter**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| handler Required | ParticipantHoldHandler | Event handler function to remove |
| participantId | string | Optional participant ID to unsubscribe from specific participant events |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
