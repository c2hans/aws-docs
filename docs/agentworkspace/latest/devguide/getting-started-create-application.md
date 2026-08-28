---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/getting-started-create-application.html
---

# Create your application for Connect Customer agent workspace
<a name="getting-started-create-application"></a>

An application is a website that can be loaded from an HTTPS URL into an iframe in the Connect Customer agent workspace. It can be built using any frontend framework and hosted anywhere as long as it can be loaded by the user’s browser and supports being embedded. In addition to being accessible by the user, the application must integrate the [Amazon Connect SDK](https://github.com/amazon-connect/AmazonConnectSDK) to establish secure communication between the application and the agent workspace allowing the application to receive events and data from the workspace.

**Topics**
+ [Install the Amazon Connect SDK](getting-started-install-sdk.md)
+ [Using Connect SDK without package manager](sdk-without-package-manager.md)
+ [Initialize the Amazon Connect SDK in your application](getting-started-initialize-sdk.md)
+ [Events and requests](getting-started-events-and-requests.md)
+ [Application authentication](getting-started-authentication.md)
+ [Integrate with agent data](integrate-with-agent-data.md)
+ [Integrate with contact data](integrate-with-contact-data.md)
+ [Lifecycle events](integrating-with-agent-workspace-lifecycle-events.md)
+ [Apply a theme](integrating-with-agent-workspace-theme.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
