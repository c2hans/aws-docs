---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-requests-getparticipantstate.html
---

# Get participant state in Connect Customer agent workspace
<a name="3P-apps-contact-requests-getparticipantstate"></a>

Retrieves the current state of a specific participant.

 **Signature**

```
getParticipantState(participantId: string): Promise<ParticipantState>
```

 **Usage**

```
const state = await contactClient.getParticipantState("participant-456");
if (state.value === "connected") {
    console.log("Participant is connected");
} else if (state.value === "hold") {
    console.log("Participant is on hold");
}
```

 **Input**

|  **Parameter**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| participantId Required | string | The unique identifier for the participant |

 **Output - ParticipantState**

The ParticipantState type can be:
+ { value: ParticipantStateType } where ParticipantStateType includes: connecting, connected, hold, disconnected, rejected, silent\_monitor, barge
+ { value: "other"; actual: string } for unknown states

 **Permissions required:**

```
*
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
