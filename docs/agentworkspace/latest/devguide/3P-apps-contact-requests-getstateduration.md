---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-requests-getstateduration.html
---

# Get the duration of the contact state in Connect Customer agent workspace
<a name="3P-apps-contact-requests-getstateduration"></a>

Returns the duration of the contact state in milliseconds relative to local time, in the Connect Customer agent workspace. This takes into account time skew between the JS client and the Connect Customer backend servers.

```
async getStateDuration(contactId: string): Promise<number>
```

 **Permissions required:**

```
Contact.Details.View
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
