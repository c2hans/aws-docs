---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-requests-disconnectparticipant.html
---

# Disconnect a participant from a contact in Connect Customer agent workspace
<a name="3P-apps-contact-requests-disconnectparticipant"></a>

Disconnects a specific participant from the contact.

 **Signature**

```
disconnectParticipant(participantId: string): Promise<void>
```

 **Usage**

```
await contactClient.disconnectParticipant("participant-456");
console.log("Participant disconnected");
```

 **Input**

|  **Parameter**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| participantId Required | string | The unique identifier for the participant to disconnect |

 **Permissions required:**

```
*
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
