---
source_url: https://docs.aws.amazon.com/whitepapers/latest/nhs-cloud-security-guidance-using-aws/principle-13-audit-information-for-users.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Principle 13: Audit information for users
<a name="principle-13-audit-information-for-users"></a>

****
 You should be provided with the audit records needed to monitor access to your service and the data held within it. The type of audit information available to you will have a direct impact on your ability to detect and respond to inappropriate or malicious activity within reasonable timescales.
 The Service User should use the audit data as part of an effective pro-active monitoring regime.

 **Applicable risk classes:** All

 AWS offers a service called CloudTrail that provides audit records for AWS customers, presenting audit information in the form of log files to a specified storage location (specifically, a nominated Amazon S3 bucket). The recorded information includes the identity of the API caller, the time of the API call, the source IP address of the API caller, the request parameters, and the response elements returned by the AWS service.

 CloudTrail provides a history of AWS API calls for customer accounts, including those made via the AWS Management Console, AWS SDKs, command line tools, and higher-level AWS services (such as AWS CloudFormation) that invoke those APIs on a customer’s behalf. The AWS API call history captured by CloudTrail enables security analysis, resource change tracking, and compliance auditing.

 The log file objects written to Amazon S3 are granted full control to the bucket owner. The bucket owner thus has full control over whether to share the logs with any other parties. This feature provides AWS customers with a mechanism for investigating service misuse or security incidents.

 For more details on AWS CloudTrail and further information on audit records, see [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html).

 The other service relevant to this purpose is [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html), which enables events occurring on EC2 instances (under customer management in the Shared Responsibility Model for Security) to be written to log files in AWS for analysis (and response, if required, through the companion [Amazon CloudWatch Events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html) feature). This service is also used for longer-term storage of CloudTrail records.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
