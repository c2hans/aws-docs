---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-requests-engagepreviewcontact.html
---

# Engage the preview contact for the given contactId in Connect Customer agent workspace
<a name="3P-apps-contact-requests-engagepreviewcontact"></a>

When an agent is previewing a preview contact, this API will actually initiate the outbound dial to the end customer, ending the preview experience.

 **Signature**

```
engagePreviewContact(contactId: string): Promise<AddParticipantResult>
```

 **Usage**

```
const addParticipantResult: AddParticipantResult = await contactClient.engagePreviewContact(contactId);
```

 **Input**

|  **Parameter**  |  **Type**  |  **Description**  |
| --- | --- | --- |
|  contactId Required  |  string  |  The id of the contact which is being previewed by the agent to which a participant needs to be added.  |

 **Output - AddParticipantResult**

|  **Parameter**  |  **Type**  |  **Description**  |
| --- | --- | --- |
|  participantId  |  string  |  The id of the newly added participant  |

 **Permissions required:**

```
*
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
