---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/integrating-with-agent-workspace-error-handling.html
---

# Handle application errors in Connect Customer agent workspace
<a name="integrating-with-agent-workspace-error-handling"></a>

Applications can communicate errors back to the Connect Customer agent workspace by either calling ` sendError` or `sendFatalError` on the `AmazonConnectApp` object. The agent workspace will shutdown an app if it sends a fatal error meaning that the app has reached an unrecoverable state and isn’t functional. When an app sends a fatal error the agent workspace won’t attempt to go through the destroy lifecycle handshake and will immediately remove the iframe from the DOM. Apps should do any clean up required prior to sending fatal errors.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
