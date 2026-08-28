---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-events-missed-sub.html
---

# Subscribe a callback function when an Connect Customer agent workspace contact is missed
<a name="3P-apps-contact-events-missed-sub"></a>

Subscribes a callback function to-be-invoked whenever a contact missed event occurs in the Connect Customer agent workspace. If no contact ID is provided, then it uses the context of the current contact that the 3P app was opened on.

 **Signature**

```
onMissed(handler: ContactMissedHandler, contactId?: string)
```

 **Usage**

```
const handler: ContactMissedHandler = async (data: ContactMissed) => {
    console.log("Contact missed occurred! " + data);
};

contactClient.onMissed(handler);

// ContactMissed Structure
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
