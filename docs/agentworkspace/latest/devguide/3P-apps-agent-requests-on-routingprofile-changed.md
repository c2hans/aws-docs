---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-agent-requests-on-routingprofile-changed.html
---

# Subscribe to agent routing profile changes in Connect Customer agent workspace
<a name="3P-apps-agent-requests-on-routingprofile-changed"></a>

Creates a subscription for RoutingProfileChanged event. This gets triggered when an Agent's routing profile gets updated.

 **Signature**

```
const handler: RoutingProfileChangedHandler = async (data: AgentRoutingProfileChanged) => {
    console.log("Agent routing profile change occurred! " + data);
};

agentClient.onRoutingProfileChanged(handler);

// AgentRoutingProfileChanged Structure
{
    routingProfile: AgentRoutingProfile;
    previous?: {
        routingProfile: AgentRoutingProfile;
    };
}
```

 **Permissions required:**

```
*
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
