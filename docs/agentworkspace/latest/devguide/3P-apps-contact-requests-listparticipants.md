---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-requests-listparticipants.html
---

# List all participants for a contact in Connect Customer agent workspace
<a name="3P-apps-contact-requests-listparticipants"></a>

Retrieves all participants associated with a specific contact.

 **Signature**

```
listParticipants(contactId: string): Promise<ParticipantData[]>
```

 **Usage**

```
const participants = await contactClient.listParticipants("contact-123");
participants.forEach((p) => {
    console.log(`Participant ${p.participantId}: ${p.type.value}`);
    if (p.isSelf) {
        console.log("This is the current user");
    }
});
```

 **Input**

|  **Parameter**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| contactId Required | string | The unique identifier for the contact |

 **Output - ParticipantData[]**

The ParticipantData interface includes:
+ `participantId`: string - Unique identifier for the participant
+ `contactId`: string - Contact this participant belongs to
+ `type`: ParticipantType - Type of participant (agent, outbound, inbound, monitoring, other)
+ `isInitial`: boolean - Whether this is the initial participant
+ `isSelf`: boolean - Whether this participant is associated with the current user

 **Permissions required:**

```
*
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
