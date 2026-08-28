---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-requests-clearedsubscribing.html
---

# Creates a subscription whenever a contact cleared event occurs in Connect Customer agent workspace
<a name="3P-apps-contact-requests-clearedsubscribing"></a>

 It creates a subscription whenever a contact cleared event occurs in Connect Customer agent workspace. If no contact ID is provided, then it uses the context of the current contact that the 3P app was opened on.

 **Signature**

 onCleared(handler: ContactClearedHandler, contactId?: string)

 **Usage**

```
const handler: ContactClearedHandler = async (data: ContactCleared) => {
    console.log("Contact cleared occurred! " + data);
};

contactClient.onCleared(handler);

// ContactCleared Structure
{
    contactId: string;
}
```

 **Permissions required:**

```
Contact.Details.View
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
