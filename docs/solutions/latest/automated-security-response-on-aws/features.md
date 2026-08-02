---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/features.html
---

# Features and benefits
<a name="features"></a>

The Automated Security Response on AWS provides the following features:

 **Automatically remediate findings for specific controls**

Configure the solution to automatically remediate findings for specific controls by modifying the Remediation Configuration DynamoDB table deployed to the admin account.

 **Manage remediations across multiple accounts and Regions from one location**

From an AWS Security Hub administrator account that is configured as the aggregation destination for your organization’s accounts and Regions, initiate a remediation for a finding in any account and Region in which the solution is deployed.

 **Get notified of remediation actions and results**

Subscribe to the Amazon SNS topic deployed by the solution to be notified when remediations are initiated and whether or not the remediation was successful.

 **Use the Web User Interface to start, view, and manage remediations**

You will have the option to enable the solution’s Web UI when deplying the Admin stack, which will provide a comprehensive user-friendly view to run remediations and view all past remediations performed by the solution.

 **Integrate with ticket systems like Jira or ServiceNow**

To help your organization react to remediations (for example, updating your infrastructure code), this solution can push tickets to your external ticketing system.

 **Use AWSConfigRemediations in the GovCloud and China partitions**

Some of the remediations included in the solution are repackages of AWS-owned AWSConfigRemediation documents that are available in the commercial partition but not in GovCloud or China. Deploy this solution to make use of these documents in those partitions.

 **Extend the solution with custom remediation and Playbook implementations**

The solution is designed to be extensible and customizable. To specify an alternative remediation implementation, deploy customized AWS Systems Manager automation documents and AWS IAM Roles. To support an entire new set of controls that is not implemented by the solution, deploy a custom Playbook.
