---
source_url: https://docs.aws.amazon.com/serverlessrepo/latest/devguide/security-logging-monitoring.html
---

# Logging and Monitoring in the AWS Serverless Application Repository
<a name="security-logging-monitoring"></a>

Monitoring is an important part of maintaining the reliability, availability, and performance of your AWS solutions. You should collect monitoring data from all of the parts of your AWS solution so that you can more easily debug a multipoint failure if one occurs. AWS provides several tools for monitoring your AWS Serverless Application Repository resources and responding to potential incidents, such as the following:

**AWS CloudTrail Logs**
The AWS Serverless Application Repository is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in the AWS Serverless Application Repository. CloudTrail captures all API calls for the AWS Serverless Application Repository as events.

**Topics**
+ [Logging AWS Serverless Application Repository API Calls with AWS CloudTrail](logging-using-cloudtrail.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Serverless Application Repository. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query serverlessrepo` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
