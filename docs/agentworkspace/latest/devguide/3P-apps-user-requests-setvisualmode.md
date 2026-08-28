---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-user-requests-setvisualmode.html
---

# Set the visual mode of a user in Connect Customer agent workspace
<a name="3P-apps-user-requests-setvisualmode"></a>

Sets the visual mode (light, dark, or auto) for the user that's currently logged in to the Connect Customer agent workspace. The promise resolves once the visual mode change has been persisted.

 **Signature**

```
setVisualMode(visualMode: VisualMode): Promise<void>
```

 **Usage**

```
await settingsClient.setVisualMode("dark");
```

 **Input**

| **Parameter** | **Type** | **Description** |
| --- | --- | --- |
| visualMode Required | VisualMode | The visual mode to set. One of "light", "dark", or "auto". |

 **Permissions required:**

```
*
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
