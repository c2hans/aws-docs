---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-requests-getparticipant.html
---

# Get specific participant information in Connect Customer agent workspace
<a name="3P-apps-contact-requests-getparticipant"></a>

Retrieves information for a specific participant.

 **Signature**

```
getParticipant(participantId: string): Promise<ParticipantData>
```

 **Usage**

```
const participant = await contactClient.getParticipant("participant-456");
console.log(`Participant type: ${participant.type.value}`);
console.log(`Is initial: ${participant.isInitial}`);
```

 **Input**

|  **Parameter**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| participantId Required | string | The unique identifier for the participant |

 **Output - ParticipantData**

Returns a ParticipantData object with participant details.

 **Permissions required:**

```
*
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
