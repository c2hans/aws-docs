---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-events-connecting-sub.html
---

# Subscribe a callback function when an Connect Customer agent workspace contact turns to Connecting state
<a name="3P-apps-contact-events-connecting-sub"></a>

Subscribes a callback function to-be-invoked whenever a contact turns to Connecting state in the Connect Customer agent workspace. The Connecting state means the contact is being routed to the agent and has not yet been fully assigned. If no contact ID is provided, then it uses the context of the current contact that the 3P app was opened on.

 **Signature**

```
onConnecting(handler: ContactConnectingHandler, contactId?: string)
```

 **Usage**

```
const handler: ContactConnectingHandler = async (data: ContactConnecting) => {
    console.log("Contact Connecting occurred! " + data.contactId);
};

contactClient.onConnecting(handler);

// ContactConnecting Structure
{
    contactId: string;
    initialContactId: string | undefined;
    type: string;
    subtype: string;
}
```

 **Permissions required:**

```
*
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
