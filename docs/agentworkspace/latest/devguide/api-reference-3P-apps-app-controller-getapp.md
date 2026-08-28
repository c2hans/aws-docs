---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/api-reference-3P-apps-app-controller-getapp.html
---

# Get application information in Connect Customer agent workspace
<a name="api-reference-3P-apps-app-controller-getapp"></a>

Returns the application information for the given application instance ID in the Connect Customer agent workspace.

 **Signature**

```
getApp(instanceId: string): Promise<AppInfo>
```

 **Usage**

```
const applicationInfo: AppInfo = await appControllerClient.getApp(appInstanceId);
```

 **Input**

|  **Parameter**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| appInstanceId Required | string | The instance ID of the application |

 **Output - AppInfo**

|  **Parameter**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| instanceId | string | Unique ID of the application instance |
| config | Config | The configuration of the application |
| startTime | Date | Time when the application is launched |
| state | AppState | Current state of the application |
| appCreateOrder | number | Sequentially incremented counter upon new application launches |
| accessUrl | string | Access URL of the application |
| parameters | AppParameters \| undefined | Key value pair of parameters passed to the application |
| launchKey | string | A unique id to avoid duplicate application being launched with multiple invocation of launchApp API |
| scope | ContactScope \| IdleScope | Indicates if the application is launched with idle i.e when there are no contacts or launched during an active contact |

 **Permissions required:**

```
*
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
