---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-user-events-visualmodechange-sub.html
---

# Subscribe a callback function when an Connect Customer agent workspace user's visual mode changes
<a name="3P-apps-user-events-visualmodechange-sub"></a>

Subscribes a callback function to-be-invoked whenever the user's visual mode changes in the Connect Customer agent workspace.

 **Signature**

```
onVisualModeChange(handler: VisualModeChangedHandler)
```

 **Usage**

```
const handler: VisualModeChangedHandler = async (data: VisualModeChanged) => {
    console.log("Visual mode changed! " + data.visualMode);
};

settingsClient.onVisualModeChange(handler);

// VisualModeChanged Structure
{
  visualMode: VisualMode;
  previous: {
    visualMode: VisualMode | null;
  };
}
```

 **Permissions required:**

```
*
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
