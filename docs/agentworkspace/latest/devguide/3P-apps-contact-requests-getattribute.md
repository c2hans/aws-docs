---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-requests-getattribute.html
---

# Get specific attributes for a contact in Connect Customer agent workspace
<a name="3P-apps-contact-requests-getattribute"></a>

Returns the requested attribute associated with the contact in the Connect Customer agent workspace.

```
async getAttribute(
  contactId: string,
  attribute: string,
): Promise<string | undefined>
```

 **Permissions required:**

```
Contact.Attributes.View
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
