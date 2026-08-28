---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-requests-disconnectself.html
---

# Disconnect the agent from the given contact in Connect Customer agent workspace
<a name="3P-apps-contact-requests-disconnectself"></a>

Disconnects the currently logged-in agent from the given contact. Other participants on the contact (such as the customer) remain connected.

 **Signature**

```
disconnectSelf(contactId: string): Promise<void>
```

 **Usage**

```
await contactClient.disconnectSelf(contactId);
```

 **Input**

| **Parameter** | **Type** | **Description** |
| --- | --- | --- |
| contactId Required | string | The id of the contact to disconnect the agent from. |

 **Permissions required:**

```
*
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
