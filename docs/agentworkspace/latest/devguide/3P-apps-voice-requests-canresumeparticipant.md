---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-voice-requests-canresumeparticipant.html
---

# Check if a participant can be resumed from hold in Connect Customer agent workspace
<a name="3P-apps-voice-requests-canresumeparticipant"></a>

Checks whether a specific participant can be resumed from hold.

 **Signature**

```
canResumeParticipant(participantId: string): Promise<boolean>
```

 **Usage**

```
const canResume = await voiceClient.canResumeParticipant("participant-456");
if (canResume) {
  await voiceClient.resumeParticipant("participant-456");
}
```

 **Input**

|  **Parameter**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| participantId Required | string | The unique identifier for the participant |

 **Output**

Returns a Promise that resolves to a boolean: true if the participant can be resumed, false otherwise

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
