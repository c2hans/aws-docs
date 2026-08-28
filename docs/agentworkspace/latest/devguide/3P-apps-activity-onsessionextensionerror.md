---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-activity-onsessionextensionerror.html
---

# Subscribe to session extension errors in Connect Customer agent workspace
<a name="3P-apps-activity-onsessionextensionerror"></a>

Subscribes a callback function to be invoked when an attempt to extend the agent's session fails.

 **Signature**

```
onSessionExtensionError(handler: SessionExtensionErrorHandler);
```

 **Usage**

```
const handler: SessionExtensionErrorHandler = (details: SessionExtensionErrorData) => {
    console.log("Failed to extend my session!", details);
}

sessionExpirationWarningClient.onSessionExtensionError(handler);

// SessionExtensionErrorData Structure
{
    isWarningActive: boolean;
    errorDetails: Record<string, unknown>;
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
