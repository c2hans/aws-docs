---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-agent-requests-getnetworkconnectionstatus.html
---

# Get the current network connection status of the agent in Connect Customer agent workspace
<a name="3P-apps-agent-requests-getnetworkconnectionstatus"></a>

Returns the current network connection health status of the agent's connection to Connect Customer backend services.

```
async getNetworkConnectionStatus(): Promise<NetworkConnectionStatusChanged>
```

 **Output - NetworkConnectionStatusChanged**

| **Parameter** | **Type** | **Description** |
| --- | --- | --- |
| status | NetworkConnectionStatus | The connection health status. One of "connected", "connecting", "disconnected", or "failed". |
| timestamp | number | Epoch milliseconds when the status was reported. |

 **Permissions required:**

```
*
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
