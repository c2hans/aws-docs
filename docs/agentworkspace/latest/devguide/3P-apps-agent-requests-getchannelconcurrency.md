---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-agent-requests-getchannelconcurrency.html
---

# Get the limit of contacts for the agent in Connect Customer agent workspace
<a name="3P-apps-agent-requests-getchannelconcurrency"></a>

Returns a map of `ChannelType`-to-number indicating how many concurrent contacts can an Connect Customer agent workspace agent have on a given channel. 0 represents a disabled channel.

```
async getChannelConcurrency(): Promise<AgentChannelConcurrencyMap>
```

 **Permissions required:**

```
User.Configuration.View
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
