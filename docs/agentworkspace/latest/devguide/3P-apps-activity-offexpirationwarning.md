---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-activity-offexpirationwarning.html
---

# Unsubscribe a callback function from the expiration warning event
<a name="3P-apps-activity-offexpirationwarning"></a>

Unsubscribes a callback function from the expiration warning event that is triggered when the agent is nearing expiration due to inactivity.

 **Signature**

```
offExpirationWarning(handler: ExpirationWarningHandler);
```

 **Usage**

```
sessionExpirationWarningClient.offExpirationWarning(handler);
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
