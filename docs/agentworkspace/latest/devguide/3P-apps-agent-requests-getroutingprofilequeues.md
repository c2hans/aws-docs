---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-agent-requests-getroutingprofilequeues.html
---

# Get the queues on the agent's routing profile in Connect Customer agent workspace
<a name="3P-apps-agent-requests-getroutingprofilequeues"></a>

Returns the list of queues on the routing profile of the agent currently logged in to the Connect Customer agent workspace. Each `Queue` contains `name`, `queueARN`, and `queueId`.

```
async getRoutingProfileQueues(): Promise<Queue[]>
```

 **Permissions required:**

```
*
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
