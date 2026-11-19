---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-startup-security-baseline/security-incident-response-and-resources.html
---

# Security incident response and resources

If your startup experiences an active security event in your AWS environment, such as unauthorized access, data exfiltration, or ransomware, the [AWS Customer Incident Response Team](https://aws.amazon.com/blogs/security/welcoming-the-aws-customer-incident-response-team/) (AWS CIRT) can help at no additional charge, regardless of your AWS Support plan. The AWS CIRT is a specialized 24/7 global team of security engineers that provides hands-on support to customers during active security events on the customer side of the shared responsibility model.

During an engagement, the AWS CIRT assists with triage, analysis, and containment of security events as they appear in AWS service logs and the AWS control plane. The team draws on sources such as [AWS CloudTrail](https://aws.amazon.com/cloudtrail/), [Amazon VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html), and [Amazon GuardDuty](https://aws.amazon.com/guardduty/) findings. After containment, the team provides recommendations to help you avoid similar events in the future.

For investigations that extend into host-level or application-level analysis, such as operating system forensics, memory analysis, or application code review, complement AWS CIRT support with a specialized [AWS Partner](https://aws.amazon.com/security/partner-solutions/) for digital forensics and incident response (DFIR) capabilities.

## Request assistance during an active security event
<a name="request-assistance-during-an-active-security-event.dd93d5fd-1672-5ed4-ae21-264676a045c1"></a>

**To request assistance from the AWS CIRT**

1. Open a support case from the impacted AWS account through the [AWS Support Center Console](https://console.aws.amazon.com/support/home#/).

1. Select the service most closely related to the security event (for example, [Amazon Elastic Compute Cloud (Amazon EC2)](https://aws.amazon.com/ec2/), [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/), or [Amazon S3](https://aws.amazon.com/s3/)).

1. In the case description, state that you have an urgent security incident.

Opening a support case from the affected account allows AWS to confirm account ownership and gives you a case number to track the engagement. If you have an account team (Technical Account Manager, Account Manager, or Solutions Architect), alert them immediately.

If you have lost access to the affected account, [submit a request for assistance](https://aws.amazon.com/#/contacts/aws-account-support) through the account recovery process.

## Incident response resources
<a name="incident-response-resources.18ae0c7f-040b-52a7-83f5-2460952214cc"></a>

The AWS CIRT publishes open-source tools and resources based on patterns observed across engagements. Use these to build your incident response readiness.
+ Threat Technique Catalog for AWS (TTC) - Documents threat actor tactics, techniques, and procedures specific to AWS environments, based on MITRE ATT&CK Cloud Matrix. You can filter by the AWS services in your account to focus on what is most relevant.
+ AWS Customer Playbook Framework - Response procedures covering common security events such as unauthorized IAM credential use, ransomware on Amazon S3, and cryptocurrency mining.
+ AWS Incident Response Playbook Samples - Customizable incident response playbooks aligned to NIST SP 800-61r3, covering scenarios such as credential compromise, ransomware, data exfiltration, cryptomining, and container compromise. Includes a triage guide, regulatory notification context, and GuardDuty finding quick-response guides.
+ Assisted Log Enabler for AWS - Enables Amazon VPC Flow Logs, [CloudTrail](https://aws.amazon.com/cloudtrail/), [Amazon Elastic Kubernetes Service (Amazon EKS) audit logs](https://aws.amazon.com/eks/), [Amazon Route 53](https://aws.amazon.com/route53/) Resolver query logs, Amazon S3 server access logs, and [Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/) logs.
+ Athena Security Analytics Bootstrap - Helps you set up [Amazon Athena](https://aws.amazon.com/athena/) to investigate AWS service logs archived in Amazon S3.
+ AWS CloudSaga - Tests security controls and alerts using simulated events based on common security events observed by the AWS CIRT.

**Note**
 Startups with AWS Enterprise Support or AWS Unified Operations can also onboard to [AWS Security Incident Response](https://aws.amazon.com/security-incident-response/), a managed service that provides automated triage and 24/7 response for security events. For a framework for building your incident response program, see the [AWS Security Incident Response Guide](https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/welcome.html).
