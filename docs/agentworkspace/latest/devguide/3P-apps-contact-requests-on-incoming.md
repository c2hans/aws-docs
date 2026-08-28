---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-requests-on-incoming.html
---

# Subscribe to incoming contact events in Connect Customer agent workspace
<a name="3P-apps-contact-requests-on-incoming"></a>

Creates a subscription whenever a new incoming event occurs in the Connect Customer agent workspace.

 **Signature**

```
onIncoming(handler: ContactIncomingHandler, contactId?: string): void
```

 **Usage**

```
const handler: ContactIncomingHandler = async (data: ContactIncoming) => {
    console.log("Contact incoming occurred! " + data);
};

contactClient.onIncoming(handler);

// ContactIncoming Structure
{
    contactId: string;
    initialContactId: string | undefined;
    type: ContactChannelType["type"];
    subtype: ContactChannelType["subtype"];
}
```

 **Permissions required:**

```
*
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
