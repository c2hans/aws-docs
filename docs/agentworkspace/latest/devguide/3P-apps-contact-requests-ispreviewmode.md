---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-requests-ispreviewmode.html
---

# Check if contact is in preview mode in Connect Customer agent workspace
<a name="3P-apps-contact-requests-ispreviewmode"></a>

Returns whether the contact is being previewed. During this time, calling engagePreviewContact will trigger the outbound dial to the end customer and end preview mode.

 **Signature**

```
isPreviewMode(contactId: string): Promise<boolean>
```

 **Usage**

```
const isPreviewMode = await contactClient.isPreviewMode(currentContactId);
```

 **Input**

|  **Parameter**  |  **Type**  |  **Description**  |
| --- | --- | --- |
|  contactId Required  |  string  |  The id of the contact.  |

 **Permissions required:**

```
*
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
