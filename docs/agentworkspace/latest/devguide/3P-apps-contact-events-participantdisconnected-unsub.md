---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-events-participantdisconnected-unsub.html
---

# Unsubscribe from participant disconnected events in Connect Customer agent workspace
<a name="3P-apps-contact-events-participantdisconnected-unsub"></a>

Unsubscribes from participant disconnected events.

 **Signature**

```
offParticipantDisconnected(handler: ParticipantDisconnectedHandler, contactId?: string): void
```

 **Usage**

```
contactClient.offParticipantDisconnected(handleParticipantDisconnected);
```

 **Input**

|  **Parameter**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| handler Required | ParticipantDisconnectedHandler | Event handler function to remove |
| contactId | string | Optional contact ID to unsubscribe from specific contact events |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
