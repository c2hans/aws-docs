---
source_url: https://docs.aws.amazon.com/devopsagent/latest/userguide/connecting-to-ticketing-and-chat-connecting-slack.html
---

# Connecting Slack
<a name="connecting-to-ticketing-and-chat-connecting-slack"></a>

You can configure AWS DevOps Agent to update Slack channels you select with incident response investigation key findings, root cause analyses, and generated mitigation plans.

## Before you begin
<a name="before-you-begin"></a>

Slack needs to be registered with DevOps Agent before it can be added to an Agent Space. To integrate AWS DevOps Agent with Slack you must meet these requirements:
+ Have access to a Slack workspace with the ability to install and authorize third-party applications
+ Have identified the Slack channels where you want AWS DevOps Agent to send notifications

## Register Slack integration with AWS DevOps Agent
<a name="register-slack-integration-with-aws-devops-agent"></a>

Each registration connects to one Slack workspace. To connect multiple workspaces, repeat this process for each one.

![Register Slack with AWS DevOps Agent page showing installation steps and authorization section.](http://docs.aws.amazon.com/devopsagent/latest/userguide/images/4034f56fad96.png)

1. From the **Capability Providers** page in the AWS DevOps Agent console, find **Slack** in the **Available** providers section under **Communication** and choose **Register**.

1. Choose the **Register** button.

1. You will be redirected to Slack to authorize the AWS DevOps Agent application for your workspace.

1. On the Slack authorization page, install directly to workspaces, not at the organization level.

1. Choose a workspace from the dropdown. Do not select an Enterprise Grid.

1. Install per workspace as needed for your organization.

1. Review the requested scopes and choose **Allow** to authorize the integration.

1. After authorization, you'll return to the AWS DevOps Agent console.

## Sharing a Slack workspace across multiple AWS accounts
<a name="sharing-a-slack-workspace-across-multiple-aws-accounts"></a>

You can share a single Slack workspace across multiple AWS accounts. This works even when your Agent Space uses a customer managed key (CMK) for encryption. If you have multiple AWS accounts, you don't need a separate Slack workspace for each account.

## Overlapping and duplicate workspace installations
<a name="overlapping-and-duplicate-workspace-installations"></a>

Your organization might have overlapping or duplicate Slack workspaces across Agent Spaces or AWS accounts. You can register the same Slack workspace with more than one Agent Space. Each registration is independent. Registering the same workspace in another Agent Space doesn't collide with or overwrite your existing registration.

## Associate Slack with your DevOps Agent Space(s)
<a name="associate-slack-with-your-devops-agent-spaces"></a>

After registering Slack, you can associate one or more channels with your DevOps Agent Space(s). Repeat these steps for each channel you want to add:

1. From the **Capabilities** tab within your configured AgentSpace, navigate to **Communications** > **Slack**.

1. Select **Add Slack **

1. Enter the Channel ID

1. Choose **Create** to complete the Slack configuration.

**Note**
** The agent’s bot user must be added to private channels before it can post messages.

**Important**
** Uninstalling the Slack app may result in the Slack app not being able to be reinstalled. Please avoid uninstalling the Slack app.

## AI-generated content
<a name="ai-generated-content"></a>

We use large language models to generate investigation findings, root-cause analyses, mitigation recommendations, and conversational responses. These outputs might be inaccurate or incomplete. Verify AI-generated information before acting on it.

## Data handling and privacy
<a name="data-handling-and-privacy"></a>

We retain data associated with your Agent Space for as long as necessary to provide the service. This data includes investigation journals, chat messages, and operational data. You can delete your Agent Space at any time to remove all associated data.

To request access to or deletion of your data, delete the Agent Space through the AWS Management Console or contact [AWS Support](https://aws.amazon.com/contact-us/).

For information about how we protect your data, see [Security and data protection](aws-devops-agent-security.html). We handle information in accordance with the [AWS Privacy Notice](https://aws.amazon.com/privacy/).
