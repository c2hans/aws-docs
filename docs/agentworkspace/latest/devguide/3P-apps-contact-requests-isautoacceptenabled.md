---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-requests-isautoacceptenabled.html
---

# Check whether auto-accept is enabled for the given contact in Connect Customer agent workspace
<a name="3P-apps-contact-requests-isautoacceptenabled"></a>

Returns whether auto-accept is enabled for the given contact. When auto-accept is enabled, an incoming contact is automatically accepted on the agent's behalf without requiring an explicit [accept()](3P-apps-contact-requests-accept.md) call.

 **Signature**

```
isAutoAcceptEnabled(contactId: string): Promise<boolean>
```

 **Usage**

```
const enabled: boolean = await contactClient.isAutoAcceptEnabled(contactId);
```

 **Input**

| **Parameter** | **Type** | **Description** |
| --- | --- | --- |
| contactId Required | string | The id of the contact to check. |

 **Permissions required:**

```
*
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
