---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-events-missed-unsub.html
---

# Unsubscribe a callback function when an Connect Customer agent workspace contact is missed
<a name="3P-apps-contact-events-missed-unsub"></a>

Unsubscribes the callback function from the contact missed event.

 **Signature**

```
offMissed(handler: ContactMissedHandler, contactId?: string)
```

 **Usage**

```
contactClient.offMissed(handler);
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
