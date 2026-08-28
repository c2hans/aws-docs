---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-voice-requests-resumeparticipant.html
---

# Resume a participant from hold in Connect Customer agent workspace
<a name="3P-apps-voice-requests-resumeparticipant"></a>

Resumes a specific participant from hold.

 **Signature**

```
resumeParticipant(participantId: string): Promise<void>
```

 **Usage**

```
await voiceClient.resumeParticipant("participant-456");
console.log("Participant has been resumed");
```

 **Input**

|  **Parameter**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| participantId Required | string | The unique identifier for the participant to resume |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
