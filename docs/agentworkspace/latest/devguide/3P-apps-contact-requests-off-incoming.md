---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-requests-off-incoming.html
---

# Unsubscribe from incoming contact events in Connect Customer agent workspace
<a name="3P-apps-contact-requests-off-incoming"></a>

Unsubscribes the callback function from the contact incoming event in Connect Customer agent workspace.

 **Signature**

```
offIncoming(handler: ContactIncomingHandler, contactId?: string): void
```

 **Usage**

```
contactClient.offIncoming(handler);
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
