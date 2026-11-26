---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/omni-investigate-with-the-aws-devops-agent.html
---

# Investigate with the AWS DevOps Agent

CloudWatch Omni can investigate an issue with its own root cause analysis or with a connected investigation agent, such as AWS DevOps Agent. To investigate with DevOps Agent, connect CloudWatch Omni to a DevOps Agent space.

You can start an investigation yourself, or have CloudWatch Omni start one automatically when an alert fires. See [Start an investigation](#omni-investigate-with-the-aws-devops-agent-start-an-investigation).

AWS DevOps Agent is an AI-powered, always-available agent that spans code change risk analysis and production operations across AWS, multicloud, and on-premises environments. For more information, see the [AWS DevOps Agent User Guide](https://docs.aws.amazon.com/devopsagent/latest/userguide/).

**Important**
**Trust boundary and data access**
AWS DevOps Agent reads data with the IAM roles of its agent space. It does not use your CloudWatch Omni space operator role or your members' access grants.
It reads CloudWatch Logs, AWS X-Ray, and other sources directly. Only its roles' IAM policies and the [DevOps Agent permission guardrail](https://docs.aws.amazon.com/devopsagent/latest/userguide/aws-devops-agent-security-limiting-agent-access-in-an-aws-account.html) limit these reads.
By default, [AIDevOpsAgentAccessPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AIDevOpsAgentAccessPolicy.html) lets its executor role read all CloudWatch Omni data in your space. To limit this, see [Limit what DevOps Agent reads from CloudWatch Omni](#omni-investigate-with-the-aws-devops-agent-limit-reads).
Any member of your space can see investigations that other members started. A member's log data scope can hide some of them. Data scopes don't filter the agent's step-by-step journal.
Connect an agent space only if every member of your space can already see the data its roles can read.

## Roles
<a name="omni-investigate-with-the-aws-devops-agent-roles"></a>

CloudWatch Omni works with three roles.

| Role | Direction | What it's used for | Policy |
| --- | --- | --- | --- |
| Space operator role | CloudWatch Omni → DevOps Agent | The CloudWatch Omni console and the Omni assistant use it to list agent spaces when you connect, read an investigation's progress, and chat with DevOps Agent. | [AIDevOpsAgentFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AIDevOpsAgentFullAccess.html). If you didn't choose to use DevOps Agent during [Set up Omni](omni-set-up-omni.md), an IAM administrator must attach it to the space operator role. It grants full DevOps Agent access in the account, including creating and deleting agent spaces. |
| Invocation role | CloudWatch Omni → DevOps Agent | CloudWatch Omni uses it to start and track investigations for the auto-trigger configuration. | [CloudWatchOmniDevOpsAgentInvestigationServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchOmniDevOpsAgentInvestigationServiceRolePolicy.html) (DevOps Agent investigation actions only, on agent spaces in your account). |
| Executor role | DevOps Agent → CloudWatch Omni | DevOps Agent's primary account role, used to read CloudWatch Omni data. | [AIDevOpsAgentAccessPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AIDevOpsAgentAccessPolicy.html) (set in DevOps Agent). Optionally [CloudWatchOmniGrantEnforcementPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchOmniGrantEnforcementPolicy.html). See [Limit what DevOps Agent reads from CloudWatch Omni](#omni-investigate-with-the-aws-devops-agent-limit-reads). |

## Limit what DevOps Agent reads from CloudWatch Omni
<a name="omni-investigate-with-the-aws-devops-agent-limit-reads"></a>

By default, [AIDevOpsAgentAccessPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AIDevOpsAgentAccessPolicy.html) lets the executor role read CloudWatch Omni data without an access grant. DevOps Agent can then read all the data in your space for this account and Region, and no data scope applies.

To enforce grants, attach a policy that denies the role's CloudWatch Omni reads unless `cloudwatch:HasAccessGrant` is `true`. CloudWatch Omni sets this key to `true` only when one of the role's grants allows the action. The [CloudWatchOmniGrantEnforcementPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchOmniGrantEnforcementPolicy.html) AWS managed policy does this, or you can use your own IAM policy with the same `Deny`. For more information, see [Preventative controls](omni-security-best-practices-for-cloudwatch-omni.md#omni-security-best-practices-for-cloudwatch-omni-preventative-controls).

### Before you begin
<a name="omni-investigate-with-the-aws-devops-agent-limit-reads-before"></a>
+ You are a Space Admin in the space.
+ You have IAM permission to attach policies to the role.

### To limit what DevOps Agent reads
<a name="omni-investigate-with-the-aws-devops-agent-limit-reads-steps"></a>

1. In CloudWatch Omni, navigate to **Settings** → **Integrations** → **AWS DevOps Agent**.

1. Under **Executor role**, choose **Manage access grants**.

1. Add a grant for the role. Choose **Viewer**, or choose **Custom** and select only the actions DevOps Agent needs. To limit which log and trace rows its queries return, add a data scope.

1. In the IAM console, attach [CloudWatchOmniGrantEnforcementPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchOmniGrantEnforcementPolicy.html) to the role, or your own equivalent policy.

**Note**
Add the grant before you enforce it. Grants apply to a caller that uses IAM credentials only when `cloudwatch:HasAccessGrant` is `true`. If you enforce grants and the role has no grant, DevOps Agent can't read any CloudWatch Omni data in the space.
Data scopes filter log and trace rows only. They don't filter reads such as the context graph and alerts. A grant only allows or denies those. If another grant without a data scope also allows the query, rows aren't filtered.
A grant applies to the role in this account's space and Region. If you delete and re-create the role, add its grant again.

## Connect an agent space
<a name="omni-investigate-with-the-aws-devops-agent-connect-an-agent-space"></a>

### Prerequisites
<a name="omni-investigate-with-the-aws-devops-agent-connect-an-agent-space-prerequisites"></a>
+ An agent space in the same AWS account and Region as your CloudWatch Omni space. CloudWatch Omni can list, connect, and chat with an agent space only in your space's Region. The agent space can still investigate other accounts through its secondary account roles. To create one, see [Creating an agent space](https://docs.aws.amazon.com/devopsagent/latest/userguide/getting-started-with-aws-devops-agent-creating-an-agent-space.html) in the AWS DevOps Agent User Guide.
+ The space operator role has [AIDevOpsAgentFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AIDevOpsAgentFullAccess.html). See [Roles](#omni-investigate-with-the-aws-devops-agent-roles).
+ You are a Space Admin, or your custom grant includes `cloudwatch:CreateIntegration`, `cloudwatch:UpdateIntegration`, and `cloudwatch:DeleteIntegration`. For more information about permission levels, see [Control access to your space](omni-control-access-to-your-space.md).

### Connect
<a name="omni-investigate-with-the-aws-devops-agent-connect-an-agent-space-connect"></a>

1. In CloudWatch Omni, navigate to **Settings** → **Integrations**. Under **Sub agents**, find **AWS DevOps Agent** and choose **Agent space**.

1. Choose your space's Region, select your agent space, and then choose **Connect**. CloudWatch Omni creates the invocation role.

To connect a different agent space later, choose **Change space**.

## Start an investigation
<a name="omni-investigate-with-the-aws-devops-agent-start-an-investigation"></a>

To start an investigation, you need permission to use the integration (`cloudwatch:InvokeIntegration`). The Editor and Space Admin permission levels include it, but the Viewer level doesn't. A custom grant must include it.
+ **From the Omni assistant.** In a thread, describe the symptom and ask Omni to investigate. If more than one investigator is available, Omni asks which one to use and remembers your choice.
+ **With the `/investigation` command.** In a thread, enter `/investigation new <description of issue>`.
+ **From an alert.** A firing alert offers an **Investigate** action. To start investigations automatically, turn on **Auto-trigger an investigation with your agent** in the alert's create or edit form, then choose the agent and the severities. When the alert breaches at a chosen severity, CloudWatch Omni starts an investigation on the invocation role, with the alert as its trigger. Make sure the alert's access profile can invoke the integration. If it can't, the form offers the **Grant permission** action. For more information, see [Investigate a firing alert](omni-alerts.md#omni-alerts-investigate-a-firing-alert).
