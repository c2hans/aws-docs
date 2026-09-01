---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/overview-agent-distribution.html
---

# Set up your agent's experience with Connect Customer Global Resiliency
<a name="overview-agent-distribution"></a>

With Connect Customer Global Resiliency, you can provide a global experience for agents with global sign-in, agent distribution API, and Agent Workspace enhancements. With this set of features, you can:
+ Enable your agents to sign in once at the beginning of their day and process contacts from their current active Region without needing to know which Region is active at any time.
+ Add agents to your traffic distribution group and distribute agents across AWS Regions.
+ Redirect new inbound voice contacts to the agent workspace for the current active Region with a simple page refresh.

**Topics**
+ [Integrate your IdP with a Connect Customer Global Resiliency SAML sign in endpoint](integrate-idp.md)
+ [Associate agents to instances across multiple AWS Regions](associate-agents-across-regions.md)
+ [Update agent distribution across Regions](update-agents-across-regions.md)
+ [Set up Agent Workspace](setup-agentworkspace-switchover.md)
+ [Tips for avoiding issues when shifting agents across Regions](possible-issues-shifting-regions.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
