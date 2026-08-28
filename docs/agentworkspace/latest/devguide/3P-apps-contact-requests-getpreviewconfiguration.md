---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-requests-getpreviewconfiguration.html
---

# Get preview configuration for the given contactId in Connect Customer agent workspace
<a name="3P-apps-contact-requests-getpreviewconfiguration"></a>

This gets configuration information related to the preview experience.

 **Signature**

```
getPreviewConfiguration(contactId: string): Promise<GetPreviewConfigurationResponse>
```

 **Usage**

```
const isPreview  = await contactClient.isPreviewMode(contactId);
if (isPreview) {
    const {autoDialTimeout, canDiscardPreview} = await contactClient.getPreviewConfiguration(contactId);
}
```

 **Input**

|  **Parameter**  |  **Type**  |  **Description**  |
| --- | --- | --- |
|  contactId Required  |  string  |  The id of the contact which is in preview.  |

 **Output - GetPreviewConfigurationResponse**

|  **Parameter**  |  **Type**  |  **Description**  |
| --- | --- | --- |
|  autoDialTimeout  |  number  |  The number of seconds the agent has to preview the contact before the auto-dial triggers.  |
|  canDiscardPreview  |  boolean  |  Whether the agent has permission to discard the contact during preview. Use this to control whether the agent should be presented the option to discard the contact without dialing the end customer.  |

 **Permissions required:**

```
*
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
