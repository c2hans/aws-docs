---
source_url: https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-non-api-events.html
---

# Non-API events captured by CloudTrail
<a name="cloudtrail-non-api-events"></a>

In addition to logging AWS API calls, CloudTrail captures other related events that might have a security or compliance impact on your AWS account or that might help you troubleshoot operational problems.
+ [AWS service events](non-api-aws-service-events.md) – CloudTrail supports logging non-API service events. These events are created by AWS services but are not directly triggered by a request to a public AWS API. For these events, the `eventType` field is `AwsServiceEvent`.
+ [AWS Management Console sign-in events](cloudtrail-event-reference-aws-console-sign-in-events.md) – CloudTrail logs attempts to sign in to the AWS Management Console, the AWS Discussion Forums, and the AWS Support Center. All IAM user and root user sign-in events, as well as all federated user sign-in events, generate records in CloudTrail. For sign-in events, the `eventType` field is `AwsConsoleSignIn`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudTrail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awscloudtrail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
