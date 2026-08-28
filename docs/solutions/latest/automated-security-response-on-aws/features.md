---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/features.html
---

# Features and benefits
<a name="features"></a>

The Automated Security Response on AWS provides the following features:

 **Automatically remediate findings for specific controls**

Configure the solution to automatically remediate findings for specific controls by modifying the Remediation Configuration DynamoDB table deployed to the admin account.

 **Remediate findings from multiple AWS security services**

Beyond AWS Security Hub CSPM control findings, the solution can remediate findings from Amazon Inspector, Amazon GuardDuty, and Amazon Macie. The pre-processor maps each finding to the appropriate remediation and processes both the AWS Security Finding Format (ASFF) and the Open Cybersecurity Schema Framework (OCSF).

 **Manage remediations across multiple accounts and Regions from one location**

From an AWS Security Hub administrator account that is configured as the aggregation destination for your organization’s accounts and Regions, initiate a remediation for a finding in any account and Region in which the solution is deployed.

 **Get notified of remediation actions and results**

The solution publishes to an Amazon SNS topic when remediations are initiated and when they succeed or fail. You can also create notification configurations from the Web UI to deliver findings and remediation results to email, Slack, JIRA, or ServiceNow. For more information, see the [Configure notifications](configure-notifications.md) section.

 **Use the Web User Interface to start, view, and manage remediations**

You have the option to enable the solution’s Web UI when deploying the Admin stack. The Web UI provides a comprehensive, user-friendly view to run remediations and view all past remediations performed by the solution.

 **Integrate with ticket systems like Jira or ServiceNow**

To help your organization react to remediations (for example, updating your infrastructure code), this solution can push tickets to your external ticketing system.

 **Use AWSConfigRemediations in the GovCloud and China partitions**

Some of the remediations included in the solution are repackages of AWS-owned AWSConfigRemediation documents that are available in the commercial partition but not in GovCloud or China. Deploy this solution to make use of these documents in those partitions.

 **Extend the solution with custom remediation and Playbook implementations**

The solution is designed to be extensible and customizable. To specify an alternative remediation implementation, deploy customized AWS Systems Manager automation documents and AWS IAM Roles. To support an entire new set of controls that is not implemented by the solution, deploy a custom Playbook.

To accelerate building these customizations, the solution provides the AI Toolkit for Custom Remediations. The toolkit delivers ASR best practices, guardrails, and development patterns as an instruction prompt that you provide to an AI assistant in your integrated development environment (IDE), giving the assistant the context it needs to help you author production-ready custom remediations more efficiently and safely.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Automated Security Response on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
