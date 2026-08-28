---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-email-requests-draftemailcreated-unsubscribing.html
---

# Unsubscribe from draft email creation notifications in Connect Customer agent workspace
<a name="3P-apps-email-requests-draftemailcreated-unsubscribing"></a>

Unsubscribes a callback function from the event that is fired when a draft email contact is created.

 **Signature**

```
offDraftEmailCreated(handler: SubscriptionHandler<EmailContactId>, contactId?: string): void
```

 **Usage**

```
emailClient.offDraftEmailCreated(handler);
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
