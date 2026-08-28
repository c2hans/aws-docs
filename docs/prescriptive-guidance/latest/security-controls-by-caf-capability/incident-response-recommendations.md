---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-controls-by-caf-capability/incident-response-recommendations.html
---

# Security recommendations for responding to incidents
<a name="incident-response-recommendations"></a>

When a security event occurs in your organization, your users must be prepared to respond to the issue. All users should have a basic understanding of your organization's security response processes. Planning, training, and experience are critical to a successful incident response program. Ideally, you prepare your organization before a potential security event occurs. The AWS Well-Architected Framework identifies three foundations that are required for a successful incident response program in the cloud: *preparation*, *operations*, and *post-incident activity*. For more information, see [Aspects of AWS incident response](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/aspects-of-aws-incident-response.html) in the AWS Well-Architected Framework.

With the exception of security controls that notify you about events or automatically respond to them, there are limited controls that you can establish for incident response. A strong incident response posture is primarily established through the plans, processes, runbooks, playbook, and training programs that you use in your organization. You can use the controls and recommendations in this section to implement best practices for your incident response program. For more information about best practices for incident response and implementation guidance, see [Incident response](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/incident-response.html) in the AWS Well-Architected Framework.

Recommendations in this section:
+ [Define an incident response plan](#incident-response-plan)
+ [Create and maintain incident response runbooks and playbooks](#runbooks-playbooks)
+ [Implement event-driven security automation](#automation)
+ [Document how operational teams should engage with AWS Support](#engage-support)
+ [Configure alerts for security events](#alert-events)

## Define an incident response plan
<a name="incident-response-plan"></a>

Establish a well-defined incident response plan (IRP). The incident response plan is designed to be the foundation for your incident response program. This plan must be customized to address the needs of each organization.

For more information, see the following resources:
+ [Develop and test an incident response plan](https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/develop-and-test-incident-response-plan.html) in the *AWS Security Incident Response Guide*
+ [Develop incident management plans](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_incident_response_develop_management_plans.html) in the AWS Well-Architected Framework
+ [Identify key personnel and external resources](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_incident_response_identify_personnel.html) in the AWS Well-Architected Framework

## Create and maintain incident response runbooks and playbooks
<a name="runbooks-playbooks"></a>

A key part of preparing for an incident response processes is developing playbooks. Incident response playbooks provide a series of recommended steps that users follow when a security event occurs. Having a clear structure and steps simplifies the response and reduces the likelihood for human error.

For more information, see the following resources:
+ [What to create playbooks for](https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/what-to-create-playbooks-for.html) in the *AWS Security Incident Response Guide*
+ [AWS incident response playbook samples](https://github.com/aws-samples/aws-incident-response-playbooks) on GitHub
+ [Develop and test security incident response playbooks](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_incident_response_playbooks.html) in the AWS Well-Architected Framework

## Implement event-driven security automation
<a name="automation"></a>

*Security response automation* is a predefined and programmed action that is designed to automatically respond to or remediate a security event. These automations serve as detective or responsive security controls that help you implement AWS security best practices. Examples of automated response actions include modifying a VPC security group, patching an Amazon EC2 instance, or rotating credentials.

Many AWS services support automated responses. For example, you can configure an Amazon CloudWatch alarm for specific metrics, and the alarm can initiate action when the alarm changes state. Through Amazon EventBridge, you can also configure automated response and remediation for findings in AWS Security Hub CSPM and Amazon Inspector.

For more information please see the below resources:
+ [Remediate Amazon Inspector security findings automatically](https://aws.amazon.com/blogs/security/how-to-remediate-amazon-inspector-security-findings-automatically/) in the AWS Security Blog
+ [Get started with security response automation on AWS](https://aws.amazon.com/blogs/security/how-get-started-security-response-automation-aws/) in the AWS Security Blog
+ [Automated security response on AWS](https://aws.amazon.com/solutions/implementations/automated-security-response-on-aws/) in the AWS Solutions Library
+ [Using Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) in the CloudWatch documentation
+ [Automated response and remediation](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-cloudwatch-events.html) in the Security Hub CSPM documentation
+ [Creating custom responses to Amazon Inspector findings with Amazon EventBridge](https://docs.aws.amazon.com/inspector/latest/user/findings-managing-automating-responses.html) in the Amazon Inspector documentation

## Document how operational teams should engage with AWS Support
<a name="engage-support"></a>

For your AWS account, you can define a primary contact and three alternate contacts. We recommend that you provide a security contact for each AWS account or for your organization.

AWS Support offers a range of plans that provide access to tools and expertise that can support the success and operational health of AWS solutions. Also, consider whether your organization would benefit from using AWS Managed Services instead of an Support plan. [AWS Managed Services (AMS)](https://docs.aws.amazon.com/managedservices/?id=docs_gateway) helps you operate more efficiently and securely by providing ongoing management of your AWS infrastructure, including monitoring, incident management, security guidance, patch support, and backup for AWS workloads. The AMS support model can be a better fit for organizations that have limited resources on their cloud operations teams. We recommend that you compare these models and plans to choose the best fit for your organization use case and cloud maturity level.

For more information, see the following resources:
+ [Understand AWS response teams and support](https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/understand-aws-response-teams-and-support.html) in the *AWS Security Incident Response Guide*
+ [Update the alternate contacts for your AWS account](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact-alternate.html) in the *AWS Account Management Guide*
+ [Compare Support Plans](https://aws.amazon.com/premiumsupport/plans/) on the AWS website
+ [Strategy for using AWS Managed Services to achieve target business outcomes](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-aws-managed-services-outcomes/introduction.html) in AWS Prescriptive Guidance

## Configure alerts for security events
<a name="alert-events"></a>

Detecting an abnormality is as important as the measures implemented to control that abnormality. An alert is the main component of the detection phase. It generates a notification to initiate the incident response process based on AWS account activity of interest. Make sure that alerts include relevant information for the team to take action.

For more information, see the following resources:
+ [Detection](https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/detection.html) in the *AWS Security Incident Response Guide*
+ [Prepare forensic capabilities](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_incident_response_prepare_forensic.html) in the AWS Well-Architected Framework
+ [Implement actionable security events](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_detect_investigate_events_actionable_events.html) in the AWS Well-Architected Framework

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
