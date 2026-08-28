---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/api-reference-3P-apps-app-controller-closeapp.html
---

# Close an application in Connect Customer agent workspace
<a name="api-reference-3P-apps-app-controller-closeapp"></a>

Closes the application for the given application instance ID in the Connect Customer agent workspace.

 **Signature**

```
closeApp(instanceId: string): Promise<void>
```

 **Usage**

```
await appControllerClient.closeApp(appInstanceId);
```

 **Input**

|  **Parameter**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| appInstanceId Required | string | The instance ID of the application |

 **Permissions required:**

```
*
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
