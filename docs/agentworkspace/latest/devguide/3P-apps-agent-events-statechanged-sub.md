---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-agent-events-statechanged-sub.html
---

# Subscribe a callback function when an Connect Customer agent workspace agent state changes - Deprecated
<a name="3P-apps-agent-events-statechanged-sub"></a>

**Note**
This API is deprecated, use [onAvailabilityStateChanged()](3P-apps-agent-events-availabilitystatechanged-sub.md) instead.

Subscribes a callback function to-be-invoked whenever an agent state changed event occurs in the Connect Customer agent workspace.

 **Signature**

```
onStateChanged(handler: AgentStateChangedHandler)
```

 **Usage**

```
const handler: AgentStateChangedHandler = async (data: AgentStateChangedEventData) => {
    console.log("Agent state change occurred! " + data);
};

agentClient.onStateChanged(handler);

// AgentStateChangedEventData Structure
{
  state: string;
  previous: {
    state: string;
  };
}
```

 **Permissions required:**

```
User.Status.View
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
