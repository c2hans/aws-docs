---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-agent-events-networkconnectionstatuschanged-sub.html
---

# Subscribe a callback function when the Connect Customer agent workspace agent's network connection status changes
<a name="3P-apps-agent-events-networkconnectionstatuschanged-sub"></a>

Subscribes a callback function to be invoked whenever the agent's network connection status changes in the Connect Customer agent workspace.

 **Signature**

```
onNetworkConnectionStatusChanged(handler: NetworkConnectionStatusChangedHandler)
```

 **Usage**

```
const handler: NetworkConnectionStatusChangedHandler = async (data: NetworkConnectionStatusChanged) => {
    console.log("Network connection status changed! " + data.status);
};

agentClient.onNetworkConnectionStatusChanged(handler);

// NetworkConnectionStatusChanged Structure
{
  status: NetworkConnectionStatus;
  timestamp: number;
}
```

 **Permissions required:**

```
*
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
