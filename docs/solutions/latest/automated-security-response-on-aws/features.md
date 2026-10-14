---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/features.html
---

# Features and benefits
<a name="features"></a>

The Automated Security Response on AWS provides the following features:

 **Automatically remediate findings for specific controls**

Configure the solution to automatically remediate findings for specific controls from the Web UI **Controls** page, the MCP server, or the Remediation Configuration Amazon DynamoDB table deployed to the admin account.

 **Remediate findings from multiple AWS security services**

Beyond AWS Security Hub CSPM control findings, the solution can remediate findings from Amazon Inspector, Amazon GuardDuty, and Amazon Macie. The pre-processor maps each finding to the appropriate remediation and processes both the AWS Security Finding Format (ASFF) and the Open Cybersecurity Schema Framework (OCSF).

 **Manage remediations across multiple accounts and Regions from one location**

From an AWS Security Hub administrator account that is configured as the aggregation destination for your organization’s accounts and Regions, initiate a remediation for a finding in any account and Region in which the solution is deployed.

 **Get notified of remediation actions and results**

The solution publishes to an Amazon SNS topic when remediations are initiated and when they succeed or fail. You can also create notification configurations from the Web UI to deliver findings and remediation results to email, Slack, JIRA, or ServiceNow. For more information, see the [Configure notifications](configure-notifications.md) section.

 **Use the Web User Interface to start, view, and manage remediations**

You have the option to enable the solution’s Web UI when deploying the Admin stack. The Web UI provides a comprehensive, user-friendly view to run remediations and view all past remediations performed by the solution.

 **Roll back a completed remediation**

For supported controls, enable remediation rollback to reverse a completed remediation and return the resource to its pre-remediation state. The solution captures a pre-remediation snapshot, checks for drift before restoring, and lets an authorized administrator trigger the rollback from the Web UI. For more information, see [Remediation rollback](remediation-rollback.md).

 **Integrate with ticket systems like Jira or ServiceNow**

To help your organization react to remediations (for example, updating your infrastructure code), this solution can push tickets to your external ticketing system.

 **Use AWSConfigRemediations in the GovCloud and China partitions**

Some of the remediations included in the solution are repackages of AWS-owned AWSConfigRemediation documents that are available in the commercial partition but not in GovCloud or China. Deploy this solution to make use of these documents in those partitions.

 **Extend the solution with custom remediation and Playbook implementations**

The solution is designed to be extensible and customizable. To fill a coverage gap for a control that the solution does not already remediate, deploy your own remediation runbook into your member accounts. Your runbook never overrides a built-in remediation. Register it through the optional MCP server. The solution then records the runbook, gates its release on a passing test, and runs it only on demand. You can also deploy one yourself with AWS Systems Manager and IAM, which applies none of those safeguards. For more information, see [Custom remediation runbooks](custom-remediation-runbooks.md). To support an entire new set of controls that the solution does not implement, deploy a custom Playbook.

To accelerate building these customizations, the solution provides the AI Toolkit for Custom Remediations. The toolkit includes a shared remediation-authoring skill plus adapters for Claude Code, Kiro, and the OpenAI Codex CLI. It delivers ASR best practices, guardrails, and bundled validation and test scripts. An AI assistant in your integrated development environment (IDE) can use them to help you author, validate, test, and deploy remediations. For more information, see [AI Toolkit for Custom Remediations](adding-new-remediations.md#ai-toolkit-for-custom-remediations).

 **Connect AI clients through the optional MCP server**

Optionally deploy a Model Context Protocol (MCP) server that exposes the solution’s operations as tools to AI clients. The MCP server is off by default and works with or without the Web UI. It verifies each client’s identity and limits each user to the tools an administrator grants. For more information, see [MCP server for AI clients](mcp-server.md).
