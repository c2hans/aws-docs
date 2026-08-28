---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-activity-onexpirationwarning.html
---

# Subscribe to session expiration warning event in Connect Customer agent workspace
<a name="3P-apps-activity-onexpirationwarning"></a>

Subscribes a callback function to be invoked whenever the agent's session is about to expire due to inactivity.

 **Signature**

```
onExpirationWarning(handler: ExpirationWarningHandler);
```

 **Usage**

```
const handler: ExpirationWarningHandler = (data: SessionExpirationInformation) => {
    console.log("Agent's session expiring at:", data);
}

sessionExpirationWarningClient.onExpirationWarning(handler);

// SessionExpirationInformation Structure
{
   expiration: number;
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
