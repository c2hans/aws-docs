---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-activity-onexpirationwarningcleared.html
---

# Subscribe to expiration warning cleared event in Connect Customer agent workspace
<a name="3P-apps-activity-onexpirationwarningcleared"></a>

Subscribes a callback function to be invoked when the agent has acknowledged the expiration warning and chooses to update their session.

 **Signature**

```
onExpirationWarningCleared(handler: ExpirationWarningClearedHandler);
```

 **Usage**

```
const handler: ExpirationWarningClearedHandler = () => {
    console.log("My session was extended after I was warned!");
}

sessionExpirationWarningClient.onExpirationWarningCleared(handler);
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
