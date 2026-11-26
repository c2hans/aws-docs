---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/sandbox-spaces-sandbox-access.html
---

# How the agent reaches the sandbox account

The agent has no standing credentials for the sandbox account. For each AWS CLI command, it gets new, short-lived credentials by assuming the Intermediate role in the Hub account and then `SandboxAgentRole-<namespace>` in the sandbox account of the lease.

The permissions of each command are the intersection of the following:
+ The permission set that is assigned to the user on the lease, which the agent applies as a session policy. The solution adds deny statements that protect its own roles and the AWS Organizations and IAM Identity Center APIs.
+ The service control policies on the sandbox OU, which apply to the agent in the same way as they apply to users.

When the agent assumes the role, it derives the source identity from the user’s email address. AWS CloudTrail in the sandbox account uses that source identity to attribute every action of the agent to the user who requested it.

The lease must be Active for each command, so a lease that freezes or terminates stops the agent at its next command. The agent’s Amazon Bedrock model calls also run in the sandbox account, so their charges accrue in that account and count toward the lease budget.

**Important**
Sandbox Spaces doesn’t work with every permission set. The agent doesn’t run commands for a user whose permission set has a permissions boundary or has no policies. The permission set must also have 10 or fewer managed policies, and an inline policy of 1,648 characters or fewer as compact JSON. For more information, see [What the agent can access](user-section.md#sandbox-spaces-boundaries).
