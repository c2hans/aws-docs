---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/omni-investigate-with-partner-agents.html
---

# Investigate with AWS Partner agents

To find the root cause of an incident with a tool that your team already uses, connect an investigation agent from an AWS Partner to your CloudWatch Omni space. Members of the space can then start an investigation with the partner agent from an alert, a chart, or a thread. The agent posts its findings to the investigation in Omni, next to investigations from the AWS Ops Agent.

Every partner agent works with Omni in the same way:
+ **A Space Admin connects it** – You connect the agent once for the whole space, and sign in with your account at the partner.
+ **It has read-only access** – Omni creates an IAM role in your account for the agent, and gives the role a read-only access grant in the space.
+ **A person starts each investigation** – The agent investigates when a member of the space asks it to.
+ **You can revoke access at any time** – Revoking access removes the agent's access grant immediately.

**Important**
A partner agent is a third-party service. The partner processes the content that you share with it, under the partner's own terms. Review those terms before you connect.

The following partner agents are available:
+ [Investigate with ResolveAI](omni-investigate-with-resolve-ai.md)
