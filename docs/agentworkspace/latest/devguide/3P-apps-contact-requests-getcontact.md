---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-requests-getcontact.html
---

# Get detailed contact information in Connect Customer agent workspace
<a name="3P-apps-contact-requests-getcontact"></a>

Retrieves detailed information for a specific contact by its ID.

 **Signature**

```
getContact(contactId: string): Promise<ContactData>
```

 **Usage**

```
const contactData = await contactClient.getContact("contact-123");
console.log(`Contact type: ${contactData.type}`);
console.log(`Queue: ${contactData.queue.name}`);
```

 **Input**

|  **Parameter**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| contactId Required | string | The unique identifier for the contact |

 **Output - ContactData**

The ContactData interface includes:
+ `contactId`: string - Unique identifier for the contact
+ `type`: ContactType - Type of contact (voice, chat, task)
+ `subtype`: string - Subtype providing additional classification
+ `initialContactId`?: string - Initial contact ID for transferred contacts
+ `queue`: Queue - Queue information

 **Permissions required:**

```
*
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
