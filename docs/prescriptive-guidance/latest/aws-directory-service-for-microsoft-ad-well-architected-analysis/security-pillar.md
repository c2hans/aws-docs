---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-directory-service-for-microsoft-ad-well-architected-analysis/security-pillar.html
---

# Security pillar
<a name="security-pillar"></a>

The security pillar focuses on protecting information and systems. The following recommendations can help you meet the** **security design principles and architectural best practices for AWS Managed Microsoft AD.

**Key focus areas**
+ Data integrity and confidentiality
+ Managing user permissions
+ Establishing controls to detect security events

## Implement a strong identity foundation
<a name="implement-a-strong-identity-foundation"></a>
+ Grant the least AWS Identity and Access Management (IAM) privileges needed to AWS resources that must integrate with AWS Managed Microsoft AD.
+ Grant the least Microsoft Active Directory security permissions needed for the users and groups that you create within Microsoft Active Directory.
+ Use group Managed Service Accounts (gMSAs) together with Kerberos constrained delegation to manage service accounts. Make sure that you specify and enforce application trust boundaries by limiting when application services can act on a user's behalf.

## Activate traceability
<a name="activate-traceability"></a>
+ Activate log forwarding on the directory level to forward domain controller security event logs to Amazon CloudWatch Logs. For more information, see [Enable log forwarding](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_enable_log_forwarding.html) in the AWS Directory Service documentation.
+ Activate AWS CloudTrail to log AWS Directory Service API calls. For more information, see the [Set up central AWS CloudTrail](https://catalog.us-east-1.prod.workshops.aws/workshops/d3f60827-89f2-46a8-9be7-6e7185bd7665/en-US/2-service-guardrails/cloudtrail) section of the AWS Multi-Account Security Governance Workshop.
+ Track failed logins. For more information, see [How to monitor and track failed logins for your AWS Managed Microsoft AD](https://aws.amazon.com/blogs/security/how-to-monitor-and-track-failed-logins-for-your-aws-managed-microsoft-ad/) on the AWS Blog.

## Apply security to all layers
<a name="apply-security-to-all-layers"></a>
+ Change the directory security group rules that accept traffic from **0.0.0.0/0** to a more restrictive list of IP addresses or security groups.
+ Use **SMB 2.x **clients when accessing the SYSVOL and NETLOGON shares.
+ Track **SMBv1 **remote connections and gradually deactivate it. For more information, see [Safely disabling SMB v1 from your production environment](https://mymeasi.wordpress.com/2018/12/17/step-by-step-safely-disabling-smb-v1-from-your-production-environment/) on the Microsoft Secure Infrastructure Blog.
+ Configure password policies that meet your security standards. For more information, see [Manage password policies for AWS Managed Microsoft AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_password_policies.html) in the AWS Directory Service documentation.
+ Activate multi-factor authentication (MFA). For more information, see [Enable multi-factor authentication for AWS Managed Microsoft AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_mfa.html) in the AWS Directory Service documentation.

## Automate security best practices and prepare for security events
<a name="automate-security-best-practices"></a>
+ Automate incident responses to specific security events, including the following:
  + Group policy changes
  + Sensitive privilege use
  + Security state changes

  To automate event notifications and responses you can use any of the following AWS services:
  + [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
  + [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
  + [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html)
  + [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html)
  + [Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html)

## Protect data in transit and at rest
<a name="protect-data-in-transit-and-at-rest"></a>
+ Activate server-side and client-side secure Lightweight Directory Access Protocol (LDAP). For more information, see [Enable secure LDAP (LDAPS)](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_ldap.html) in the AWS Directory Service documentation.
