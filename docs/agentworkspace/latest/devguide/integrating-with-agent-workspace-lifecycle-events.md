---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/integrating-with-agent-workspace-lifecycle-events.html
---

# Application lifecycle events in Connect Customer agent workspace
<a name="integrating-with-agent-workspace-lifecycle-events"></a>

There are lifecycle states that an app can move between from when the app is initially opened to when it is closed in the Connect Customer agent workspace. This includes the initialization handshake that the app goes through with the agent workspace after it has loaded to establish the communication channel between the two. There is another handshake between the agent workspace and the application when the app will be shutdown. An application can hook into `onCreate` and ` onDestroy` when calling `AmazonConnectApp.init()`.

The following section describe the create and destroy events in the Connect Customer agent workspace.

**Topics**
+ [Create event](integrating-with-agent-workspace-lifecycle-events-create.md)
+ [Destroy event](integrating-with-agent-workspace-lifecycle-events-destroy.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
