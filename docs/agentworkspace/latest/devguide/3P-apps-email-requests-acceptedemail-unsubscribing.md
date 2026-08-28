---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-email-requests-acceptedemail-unsubscribing.html
---

# Unsubscribe from accepted email notifications in Connect Customer agent workspace
<a name="3P-apps-email-requests-acceptedemail-unsubscribing"></a>

Unsubscribes a callback function from the event that is fired when an inbound email contact is accepted.

 **Signature**

```
offAcceptedEmail(handler: SubscriptionHandler<EmailContactId>, contactId?: string): void
```

 **Usage**

```
emailClient.offAcceptedEmail(handler);
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
