---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-requests-getqueue.html
---

# Get the queue of the contact in Connect Customer agent workspace
<a name="3P-apps-contact-requests-getqueue"></a>

Returns the queue associated with the contact in the Connect Customer agent workspace. The `Queue` object has the following fields:
+ `name`: The name of the queue.
+ `queueARN`: The ARN of the queue.
+ `queueId`: Alias for `queueARN`.

```
async getQueue(contactId: string): Promise<Queue>
```

 **Permissions required:**

```
Contact.Details.View
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
