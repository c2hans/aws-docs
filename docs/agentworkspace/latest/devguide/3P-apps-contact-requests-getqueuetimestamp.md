---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-requests-getqueuetimestamp.html
---

# Get the timestamp of the contact in Connect Customer agent workspace
<a name="3P-apps-contact-requests-getqueuetimestamp"></a>

Returns a `Date` object with the timestamp associated with when the contact was placed in the queue in the Connect Customer agent workspace.

```
async getQueueTimestamp(contactId: string): Promise<Date | undefined>
```

 **Permissions required:**

```
Contact.Details.View
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
