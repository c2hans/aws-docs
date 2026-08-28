---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-events-startingacw-sub.html
---

# Subscribe a callback function when an Connect Customer agent workspace contact starts ACW
<a name="3P-apps-contact-events-startingacw-sub"></a>

Subscribes a callback function to-be-invoked whenever a contact StartingAcw event occurs in the Connect Customer agent workspace. If no contact ID is provided, then it uses the context of the current contact that the 3P app was opened on.

 **Signature**

```
onStartingAcw(handler: ContactStartingAcwHandler, contactId?: string)
```

 **Usage**

```
const handler: ContactStartingAcwHandler = async (data: ContactStartingAcw) => {
    console.log("Contact StartingAcw occurred! " + data);
};

contactClient.onStartingAcw(handler);

// ContactStartingAcw Structure
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
