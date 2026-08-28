---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-agent-requests-on-enabledchannellistchanged.html
---

# Subscribe to agent enabled channel list changes in Connect Customer agent workspace
<a name="3P-apps-agent-requests-on-enabledchannellistchanged"></a>

Creates a subscription for EnabledChannelListChanged event. This gets triggered when an Agent's enabled channels get updated.

 **Signature**

```
const handler: EnabledChannelListChangedHandler = async (data: EnabledChannelListChanged) => {
    console.log("Agent channel list change occurred! " + data);
};

agentClient.onEnabledChannelListChanged(handler);

// EnabledChannelListChanged Structure
{
    enabledChannels: AgentRoutingProfileChannelTypes[];
    previous?: {
        enabledChannels: AgentRoutingProfileChannelTypes[];
    };
}

// AgentRoutingProfileChannelTypes
type AgentRoutingProfileChannelTypes = "VOICE" | "CHAT" | "TASK" | "EMAIL";
```

 **Permissions required:**

```
*
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
