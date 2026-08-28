---
source_url: https://docs.aws.amazon.com/security-ir/latest/userguide/logging-using-cloudtrail.html
---

# Logging AWS Security Incident Response API calls using AWS CloudTrail
<a name="logging-using-cloudtrail"></a>

AWS Security Incident Response is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in Security Incident Response. CloudTrail captures all API calls for Security Incident Response as events. The calls captured include calls from the Security Incident Response console and code calls to the Security Incident Response API operations. If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for Security Incident Response. If you don't configure a trail, you can still view the most recent events in the CloudTrail console in **Event history**. Using the information collected by CloudTrail, you can determine the request that was made to Security Incident Response, the IP address from which the request was made, who made the request, when it was made, and additional details.

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Security Incident Response. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-ir` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
