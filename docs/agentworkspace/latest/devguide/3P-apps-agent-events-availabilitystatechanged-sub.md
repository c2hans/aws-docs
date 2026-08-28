---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-agent-events-availabilitystatechanged-sub.html
---

# Subscribe a callback function when an Connect Customer agent workspace agent's availability state changes
<a name="3P-apps-agent-events-availabilitystatechanged-sub"></a>

Subscribes a callback function to be invoked whenever the agent's availability state changes in the Connect Customer agent workspace.

This API supersedes [onStateChanged()](3P-apps-agent-events-statechanged-sub.md), which is now deprecated.

 **Signature**

```
onAvailabilityStateChanged(handler: AvailabilityStateChangedHandler)
```

 **Usage**

```
const handler: AvailabilityStateChangedHandler = async (data: AgentAvailabilityStateChanged) => {
    console.log("Agent availability state changed! " + data.state.name);
};

agentClient.onAvailabilityStateChanged(handler);

// AgentAvailabilityStateChanged Structure
{
  state: AgentState;
  previous?: {
    state: AgentState;
  };
}
```

 **Permissions required:**

```
*
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
