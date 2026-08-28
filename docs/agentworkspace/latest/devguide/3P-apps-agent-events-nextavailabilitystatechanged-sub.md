---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-agent-events-nextavailabilitystatechanged-sub.html
---

# Subscribe a callback function when an Connect Customer agent workspace agent's next queued availability state changes
<a name="3P-apps-agent-events-nextavailabilitystatechanged-sub"></a>

Subscribes a callback function to be invoked whenever the agent's next queued availability state changes in the Connect Customer agent workspace. The next state is the availability state that is queued to apply once all of the agent's active contacts are cleared. This event fires when a new next state is queued, when a queued next state is replaced, or when a queued next state is cleared.

 **Signature**

```
onNextAvailabilityStateChanged(handler: NextAvailabilityStateChangedHandler)
```

 **Usage**

```
const handler: NextAvailabilityStateChangedHandler = async (data: NextAgentAvailabilityStateChanged) => {
    console.log("Next availability state changed! " + data.nextState?.name);
};

agentClient.onNextAvailabilityStateChanged(handler);

// NextAgentAvailabilityStateChanged Structure
{
  nextState: AgentState | null;
  previous?: {
    nextState: AgentState;
  };
}
```

 **Permissions required:**

```
*
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
