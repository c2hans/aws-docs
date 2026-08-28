---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/well-architected-best-practices-fsx-windows/security.html
---

# Security pillar
<a name="security"></a>

The security pillar of the AWS Well-Architected Framework focuses on protecting information and systems. The following recommendations can help you meet the** **security design principles and architectural best practices for Amazon FSx for Windows File Server.

**Key focus areas**
+ Data integrity and confidentiality
+ Managing user permissions
+ Establishing controls to detect security events

## Implement a strong identity foundation
<a name="implement-a-strong-identity-foundation"></a>
+ Grant the least AWS Identity and Access Management (IAM) privileges needed to AWS resources that must integrate with or access Amazon FSx for Windows File Server. For more information, see [Resource administration access control with IAM for Amazon FSx](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/access-control-overview.html) in the Amazon FSx documentation.
+ Use Windows access control lists (ACLs) to manage fine-grained file-level and folder-level access. For more information, see [File- and Folder-Level Access Control Using Windows ACLs](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/limit-access-file-folder.html) in the Amazon FSx documentation.

## Activate traceability
<a name="activate-traceability"></a>
+ Enable file access auditing for FSx for Windows File Server file systems. For more information, see [File access auditing](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/file-access-auditing.html) in the Amazon FSx documentation.
+ Set audit controls on your files and folders in the FSx for Windows File Server file system to track failed logins. For more information, see the blog post [File storage access patterns insights using Amazon FSx for Windows File Server](https://aws.amazon.com/blogs/storage/file-storage-access-patterns-insights-using-amazon-fsx-for-windows-file-server/).
+ Use the Shared Folders tool to monitor connected user sessions and open files on your FSx for Windows File Server file system. For more information, see [User sessions and open files](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/manage-sessions-and-files.html) in the Amazon FSx documentation.
+ Activate AWS CloudTrail to log FSx for Windows File Server API calls. For more information, see the [Set up central AWS CloudTrail](https://catalog.us-east-1.prod.workshops.aws/workshops/d3f60827-89f2-46a8-9be7-6e7185bd7665/en-US/2-service-guardrails/cloudtrail) section of the AWS Multi-Account Security Governance Workshop in AWS Workshop Studio.

## Apply security to all layers
<a name="apply-security-to-all-layers"></a>
+ Configure your service account with minimum privileges required if you're joining a self-managed Active Directory. For more information, see [Delegating privileges to your Amazon FSx service account](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/self-managed-AD-best-practices.html#connect_delegate_privileges) in the Amazon FSx documentation.
+ Use security groups and network ACLs to restrict access to your file systems. For more information, see [File System Access Control with Amazon VPC](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/limit-access-security-groups.html) in the Amazon FSx documentation.

## Automate security best practices and prepare for security events
<a name="automate-security-best-practices-and-prepare-for-security-events"></a>
+ Automate incident responses to specific security events, such as notifying security teams of unauthorized access attempts.

To automate event notifications and responses you can use one or more of the following AWS services:
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
+ [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
+ [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html)
+ [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html)
+ [Amazon Simple Notification System (Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html))

## Protect data in transit and at rest
<a name="protect-data-in-transit-and-at-rest"></a>
+ To enforce in-transit encryption, limit access to only those clients that support the Server Message Block (SMB) protocol version 3.0 and higher. For more information, see [Managing encryption in transit](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/manage-encrypt-in-transit.html) in the Amazon FSx documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
