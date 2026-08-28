---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/logging-using-cloudtrail.html
---

# Logging Amazon WorkSpaces Applications API Calls with AWS CloudTrail
<a name="logging-using-cloudtrail"></a>

Amazon WorkSpaces Applications is integrated with AWS CloudTrail. CloudTrail is a service that provides a record of actions taken by a user, role, or an AWS service in WorkSpaces Applications. CloudTrail captures API calls for WorkSpaces Applications as events. The calls captured include calls from the WorkSpaces Applications console and code calls to the WorkSpaces Applications API operations. If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for WorkSpaces Applications. If you don't configure a trail, you can still view the most recent events in the CloudTrail console in **Event history**. You can use the information collected by CloudTrail to determine details such as request information. For example, CloudTrail collects the following information: What request was made to WorkSpaces Applications, the IP address from which the request was made, who made the request, and when it was made.

To learn more about CloudTrail, including how to configure and enable it, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/).

**Topics**
+ [WorkSpaces Applications Information in CloudTrail](service-name-info-in-cloudtrail.md)
+ [Example: WorkSpaces Applications Log File Entries](understanding-service-name-entries.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
