---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-agent-requests-getroutingprofile.html
---

# Get the routing profile of the agent in Connect Customer agent workspace
<a name="3P-apps-agent-requests-getroutingprofile"></a>

Returns the routing profile of the agent currently logged in to the Connect Customer agent workspace. The routing profile contains the following fields:
+ `channelConcurrencyMap`: See agent.[Get the limit of contacts for the agent in Connect Customer agent workspace](3P-apps-agent-requests-getchannelconcurrency.md) for more info.
+ `defaultOutboundQueue`: The default queue which should be associated with outbound contacts. See queues for details on properties.
+ `name`: The name of the routing profile.
+ `queues`: The queues contained in the routing profile. Each queue object has the following properties:
  + `name`: The name of the queue.
  + `queueARN`: The ARN of the queue.
  + `queueId`: Alias for queueARN.
+ `routingProfileARN`: The routing profile ARN.
+ `routingProfileId`: Alias for `routingProfileARN`.

```
async getRoutingProfile(): Promise<AgentRoutingProfile>
```

 **Permissions required:**

```
User.Configuration.View
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
