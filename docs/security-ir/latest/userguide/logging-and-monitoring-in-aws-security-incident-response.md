---
source_url: https://docs.aws.amazon.com/security-ir/latest/userguide/logging-and-monitoring-in-aws-security-incident-response.html
---

# Logging and monitoring in AWS Security Incident Response
<a name="logging-and-monitoring-in-aws-security-incident-response"></a>

 Monitoring is an important part of maintaining the reliability, availability, and performance of AWS Security Incident Response and your other AWS solutions. AWS Security Incident Response currently supports the following AWS services to monitor your organization and the activity that happens within it.

 **AWS CloudTrail –** With CloudTrail you can capture API calls from the AWS Security Incident Response console. For example, when a user authenticates, CloudTrail can record details such as the IP address in the request, who made the request, and when it was made.

 **Amazon CloudWatch Metrics –** With CloudWatch metrics you can monitor, report, and take automatic actions in case of an event in near real time. For example, you can create CloudWatch dashboards on the provided metrics to monitor your AWS Security Incident Response usage, or you can create CloudWatch alarms on the provided metrics to notify you on breach of a set threshold.

 The namespace for the service is AWS/Usage/ServiceName. The metric names available are ActiveManagedCases and SelfManagedCases.

 In accordance with the [AWS Service Terms](https://aws.amazon.com/service-terms/), The AWS Security Incident Response responder team will have access to your history of CloudTrail, VPC, DNS and S3 log data. This data may be utilized during active security incidents when a case is open in the AWS Security Incident Response service portal.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Security Incident Response. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-ir` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
