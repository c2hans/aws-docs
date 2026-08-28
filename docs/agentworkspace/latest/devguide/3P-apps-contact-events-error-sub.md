---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-events-error-sub.html
---

# Subscribe a callback function when an Connect Customer agent workspace contact turns to Error state
<a name="3P-apps-contact-events-error-sub"></a>

Subscribes a callback function to-be-invoked whenever a contact turns to Error state in the Connect Customer agent workspace. If no contact ID is provided, then it uses the context of the current contact that the 3P app was opened on.

 **Signature**

```
onError(handler: ContactErrorHandler, contactId?: string)
```

 **Usage**

```
const handler: ContactErrorHandler = async (data: ContactError) => {
    console.log("Contact Error occurred! " + data.contactId);
};

contactClient.onError(handler);

// ContactError Structure
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
