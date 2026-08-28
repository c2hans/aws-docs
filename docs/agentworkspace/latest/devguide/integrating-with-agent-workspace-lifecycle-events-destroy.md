---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/integrating-with-agent-workspace-lifecycle-events-destroy.html
---

# The destroy event in Connect Customer agent workspace
<a name="integrating-with-agent-workspace-lifecycle-events-destroy"></a>

The destroy event in the Connect Customer agent workspace will trigger the ` onDestroy` callback configured during `AmazonConnectApp.init()`. The application should use this event to clean up resources and persist data. The agent workspace will wait for the application to respond that it has completed clean up for a period of time.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
