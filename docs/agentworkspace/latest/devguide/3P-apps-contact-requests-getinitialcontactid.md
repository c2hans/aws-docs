---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-requests-getinitialcontactid.html
---

# Get the initial ID of the contact in Connect Customer agent workspace
<a name="3P-apps-contact-requests-getinitialcontactid"></a>

Returns the original (initial) contact id from which this contact was transferred in the Connect Customer agent workspace, or none if this is not an internal Connect transfer. This is typically a contact owned by another agent, thus this agent will not be able to manipulate it. It is for reference and association purposes only, and can be used to share data between transferred contacts externally if it is linked by originalContactId.

```
async getInitialContactId(contactId: string): Promise<string | undefined>
```

 **Permissions required:**

```
Contact.Details.View
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
