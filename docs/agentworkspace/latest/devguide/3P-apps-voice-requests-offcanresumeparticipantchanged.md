---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-voice-requests-offcanresumeparticipantchanged.html
---

# Unsubscribe from participant resume capability change events in Connect Customer agent workspace
<a name="3P-apps-voice-requests-offcanresumeparticipantchanged"></a>

Unsubscribes from participant capability change events.

 **Signature**

```
offCanResumeParticipantChanged(
  handler: CanResumeParticipantChangedHandler,
  participantId?: string
): void
```

 **Usage**

```
voiceClient.offCanResumeParticipantChanged(handleCanResumeChanged);
```

 **Input**

|  **Parameter**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| handler Required | CanResumeParticipantChangedHandler | Event handler function to remove |
| participantId | string | Optional participant ID to unsubscribe from specific participant events |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
