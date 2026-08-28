---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-agent-requests-setavailabilitystatebyname.html
---

# Set the agent state with the given agent state name in Connect Customer agent workspace
<a name="3P-apps-agent-requests-setavailabilitystatebyname"></a>

Sets the agent state with the given agent state name. The promise resolves after the agent state is set in the backend. The response status is either `updated` or ` queued` based on the current agent state.

 **Signature**

```
setAvailabilityStateByName(
    agentStateName: string,
  ): Promise<SetAvailabilityStateResult>
```

 **Usage**

```
const availabilityStateResult: SetAvailabilityStateResult = await agentClient.setAvailabilityStateByName('Available');
```

 **Input**

|  **Parameter**  |  **Type**  |  **Description**  |
| --- | --- | --- |
|  agentStateName Required  |  string  |  The name of the agent state  |

 **Output - SetAvailabilityStateResult**

|  **Parameter**  |  **Type**  |  **Description**  |
| --- | --- | --- |
|  status  |  string  |  The status will be "updated" or "queued" depends on if the agent is currently handling an active contact. |
|  current  |  AgentState  |  Reperesents the current state of the agent.  |
|  next  |  AgentState  |  It'll be the target state if the agent is handling active contact. Applicable when the status is queued |

 **Permissions required:**

```
User.Configuration.Edit
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
