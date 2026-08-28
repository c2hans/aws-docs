---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/describe-applicationlication.html
---

# Add an application to AWS Resilience Hub
<a name="describe-applicationlication"></a>

AWS Resilience Hub offers resiliency assessment and validation that integrates into your software development lifecycle. AWS Resilience Hub helps you proactively prepare and protect your AWS applications from disruptions by:
+ Uncovering resiliency weaknesses.
+ Estimating whether your target recovery time objective (RTO) and recovery point objective (RPO) can be met.
+ Resolving issues before they are released into production.

This section guides you through adding an application. You gather resources from an existing myApplications application, AWS CloudFormation stacks, or AWS Resource Groups and create an appropriate resiliency policy. After describing an application, you can publish it in AWS Resilience Hub, and generate an assessment report on the resiliency of your application. You can then use recommendations from the assessment to improve resiliency. You can run another assessment, compare results, and then iterate until the estimated workload RTO and estimated workload RPO achieves your RTO and RPO targets.

**Topics**
+ [Get started by adding an application](describe-app-intro.md)
+ [Select how this application is managed](how-app-manage.md)
+ [Add resource collections](discover-structure.md)
+ [Set RTO and RPO](setup-resiliency-policy.md)
+ [Setup scheduled assessments and drift notification](scheduled-assessment.md)
+ [Setup permissions](setup-permissions.md)
+ [Configure the application configuration parameters](app-config-param.md)
+ [Add tags](add-tags.md)
+ [Review and publish your AWS Resilience Hub application](review-and-publish.md)
+ [Run an assessment of your AWS Resilience Hub application](run-assessment-start.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
