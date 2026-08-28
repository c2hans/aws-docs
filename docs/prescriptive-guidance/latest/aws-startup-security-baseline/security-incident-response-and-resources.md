---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-startup-security-baseline/security-incident-response-and-resources.html
---

# Security incident response and resources
<a name="security-incident-response-and-resources"></a>

If your startup experiences an active security event in your AWS environment, such as unauthorized access, data exfiltration, or ransomware, the [AWS Customer Incident Response Team](https://aws.amazon.com/blogs/security/welcoming-the-aws-customer-incident-response-team/) (AWS CIRT) can help at no additional charge, regardless of your AWS Support plan. The AWS CIRT is a specialized 24/7 global team of security engineers that provides hands-on support to customers during active security events on the customer side of the shared responsibility model.

During an engagement, the AWS CIRT assists with triage, analysis, and containment of security events as they appear in AWS service logs and the AWS control plane. The team draws on sources such as [AWS CloudTrail](https://aws.amazon.com/cloudtrail/), [Amazon VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html), and [Amazon GuardDuty](https://aws.amazon.com/guardduty/) findings. After containment, the team provides recommendations to help you avoid similar events in the future.

For investigations that extend into host-level or application-level analysis, such as operating system forensics, memory analysis, or application code review, complement AWS CIRT support with a specialized [AWS Partner](https://aws.amazon.com/security/partner-solutions/) for digital forensics and incident response (DFIR) capabilities.

## Request assistance during an active security event
<a name="request-assistance-during-an-active-security-event.baad5cdf-0b4b-5471-a391-be0160461a92"></a>

**To request assistance from the AWS CIRT**

1. Open a support case from the impacted AWS account through the [AWS Support Center Console](https://console.aws.amazon.com/support/home#/).

1. Select the service most closely related to the security event (for example, [Amazon EC2](https://aws.amazon.com/ec2/), [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/), or [Amazon S3](https://aws.amazon.com/s3/)).

1. In the case description, state that you have an urgent security incident.

Opening a support case from the affected account allows AWS to confirm account ownership and gives you a case number to track the engagement. If you have an account team (Technical Account Manager, Account Manager, or Solutions Architect), alert them immediately.

If you have lost access to the affected account, [submit a request for assistance](https://aws.amazon.com/#/contacts/aws-account-support) through the account recovery process.

## Incident response resources
<a name="incident-response-resources.de6cea8c-7b30-5ae8-90b6-2768c3e7cd89"></a>

The AWS CIRT publishes open-source tools and resources based on patterns observed across engagements. Use these to build your incident response readiness.
+ [Threat Technique Catalog for AWS (TTC)](https://aws-samples.github.io/threat-technique-catalog-for-aws/) - Documents threat actor tactics, techniques, and procedures specific to AWS environments, based on MITRE ATT&CK Cloud Matrix. You can filter by the AWS services in your account to focus on what is most relevant.
+ [AWS Customer Playbook Framework](https://github.com/aws-samples/aws-customer-playbook-framework) - Response procedures covering common security events such as unauthorized IAM credential use, ransomware on Amazon S3, and cryptocurrency mining.
+ [AWS Incident Response Playbook Samples](https://github.com/aws-samples/aws-incident-response-playbooks) - Customizable incident response playbooks aligned to NIST SP 800-61r3, covering scenarios such as credential compromise, ransomware, data exfiltration, cryptomining, and container compromise. Includes a triage guide, regulatory notification context, and GuardDuty finding quick-response guides.
+ [Assisted Log Enabler for AWS](https://github.com/awslabs/assisted-log-enabler-for-aws) - Assists with enabling VPC Flow Logs, [CloudTrail](https://aws.amazon.com/cloudtrail/), [Amazon EKS audit logs](https://aws.amazon.com/eks/), [Route 53](https://aws.amazon.com/route53/) Resolver query logs, Amazon S3 server access logs, and [Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/) logs.
+ [Athena Security Analytics Bootstrap](https://github.com/awslabs/aws-security-analytics-bootstrap) - Provides a quick method to set up [Amazon Athena](https://aws.amazon.com/athena/) for investigating AWS service logs archived in Amazon S3.
+ [AWS CloudSaga](https://github.com/awslabs/aws-cloudsaga) - Tests security controls and alerts using simulated events based on common security events observed by the AWS CIRT.

**Note**
 Startups with Enterprise Support or AWS Unified Operations can also onboard to [AWS Security Incident Response](https://aws.amazon.com/security-incident-response/), a managed service that provides automated triage and 24/7 response for security events. For a comprehensive framework for building your incident response program, see the [AWS Security Incident Response Guide](https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/welcome.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
