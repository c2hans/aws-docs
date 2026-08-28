---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-security-controls/responsive-controls.html
---

# Responsive controls
<a name="responsive-controls"></a>

*Responsive controls* are security controls that are designed to drive remediation of adverse events or deviations from your security baseline. Examples of technical responsive controls include patching a system, quarantining a virus, shutting down a process, or rebooting a system.

Review the following about this type of control:
+ [Objectives](#responsive-objectives)
+ [Process](#responsive-process)
+ [Use cases](#responsive-use-cases)
+ [Technology](#responsive-technology)
+ [Business outcomes](#responsive-business-outcomes)

## Objectives
<a name="responsive-objectives"></a>
+ Responsive controls can help you create runbooks for common types of attacks, such as phishing or brute force.
+ Responsive controls can implement automated responses to potential security issues.
+ Responsive controls can automatically remediate unintended or unapproved actions on AWS resources, such as deleting unencrypted Amazon S3 buckets.
+ Responsive controls can be orchestrated to work with preventative and detective controls to create a holistic and proactive approach for addressing potential security incidents.

## Process
<a name="responsive-process"></a>

Detective controls are a prerequisite for establishing responsive controls. You must be able to detect the security issue before you can remediate it. You can then establish a policy or response to the security issue. For example, in the event of a brute force attack, a remediation process would be implemented. After the remediation process exists, it can then be automated and run as a script by using a programming language, such as a shell script.

Consider whether the responsive control might break an existing production workload. For example, if the detective security control is *S3 buckets must not be publicly accessible* and the remediation is *turn off public access for Amazon S3*, this could have significant implications for your company and its customers. If the S3 bucket is serving a public website, turning off public access could create an outage. Databases are a similar example. If a database must not be publicly accessible through the internet, turning off public access could affect connectivity to the application.

## Use cases
<a name="responsive-use-cases"></a>
+ Automatic response to detected security events
+ Automatic remediation of detected security vulnerabilities
+ Automated recovery control to reduce operational downtime

## Technology
<a name="responsive-technology"></a>

### Security Hub CSPM
<a name="9999999999999999ash-.ff0e69b4-8066-55c4-912e-482f2ca3f205"></a>

[AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) automatically sends all new findings and all updates of existing findings to Amazon EventBridge as events. You can also create custom actions that send selected findings and insight results to EventBridge. You can configure EventBridgeto respond to each type of event. The event can initiate an AWS Lambda function that performs the remediation action.

### AWS Config
<a name="9999999999999999cc-.1afa59f2-bab5-5894-93c4-8b7eff21f595"></a>

[AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) uses rules to evaluate your AWS resources and helps you remediate noncompliant resources. AWS Config applies remediation using [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html). In Automation documents, you define the actions that you want to perform on resources that AWS Config determines to be noncompliant. After you create Automation documents, you can use them in Systems Manager through the AWS Management Console or by using APIs. You can choose to either manually or automatically remediate noncompliant resources.

## Business outcomes
<a name="responsive-business-outcomes"></a>

### Minimize data loss
<a name="minimize-data-loss.d6beba8d-0f0e-5270-b204-191366564474"></a>

After a cybersecurity incident, using responsive security controls can help minimize data loss and damage to the system or network. Responsive controls can also help restore critical business systems and processes as quickly as possible, adding to the resilience of your workloads.

### Reduce costs
<a name="reduce-costs.a92e111f-cf6c-5950-bd5a-09551bba7ba7"></a>

Automation reduces costs associated with human resources because team members don't have to manually respond to incidents or otherwise manage them on a case-by-case basis.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
