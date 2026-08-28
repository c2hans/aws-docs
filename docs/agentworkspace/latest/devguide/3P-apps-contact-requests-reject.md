---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-requests-reject.html
---

# Reject the incoming contact for the given contactId in Connect Customer agent workspace
<a name="3P-apps-contact-requests-reject"></a>

Reject the incoming contact for the given contactId. The contact will not be connected to the agent and will be routed back to the queue.

 **Signature**

```
reject(contactId: string): Promise<void>
```

 **Usage**

```
await contactClient.reject(contactId);
```

 **Input**

| **Parameter** | **Type** | **Description** |
| --- | --- | --- |
| contactId Required | string | The id of the incoming contact to reject. |

 **Permissions required:**

```
*
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
