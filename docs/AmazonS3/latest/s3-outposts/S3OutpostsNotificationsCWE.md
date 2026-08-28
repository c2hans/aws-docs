---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsNotificationsCWE.html
---

# Receiving S3 on Outposts event notifications by using Amazon CloudWatch Events
<a name="S3OutpostsNotificationsCWE"></a>

You can use CloudWatch Events to create a rule for any Amazon S3 on Outposts API event. When you create a rule, you can choose to get notified through all supported CloudWatch targets, including Amazon Simple Queue Service (Amazon SQS), Amazon Simple Notification Service (Amazon SNS), and AWS Lambda. For more information, see the list of [AWS services that can be targets for CloudWatch Events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html) in the *Amazon CloudWatch Events User Guide*. To choose a target service to work with your S3 on Outposts, see [Creating a CloudWatch Events rule that triggers on an AWS API call using AWS CloudTrail](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/Create-CloudWatch-Events-CloudTrail-Rule.html) in the *Amazon CloudWatch Events User Guide*.

**Note**
For S3 on Outposts object operations, AWS API call events sent by CloudTrail will match your rules only if you have trails (optionally with event selectors) configured to receive those events. For more information, see [Working with CloudTrail log files](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/create-event-selectors-for-a-trail.html) in the *AWS CloudTrail User Guide*.

**Example**
The following is a sample rule for the `DeleteObject` operation. To use this sample rule, replace `{{amzn-s3-demo-bucket1}}` with the name of your S3 on Outposts bucket.

```
{
  "source": [
    "aws.s3-outposts"
  ],
  "detail-type": [
    "AWS API call through CloudTrail"
  ],
  "detail": {
    "eventSource": [
      "s3-outposts.amazonaws.com"
    ],
    "eventName": [
      "DeleteObject"
    ],
    "requestParameters": {
      "bucketName": [
        "{{amzn-s3-demo-bucket1}}"
      ]
    }
  }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
