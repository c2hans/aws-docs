---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-startup-security-baseline/wkld-07.html
---

# WKLD.07 Log data events for S3 buckets with sensitive data

By default, AWS CloudTrail captures *management events*, which are events that create, modify, or delete resources in your account. Management events don't include read or write operations on individual objects in Amazon S3 buckets. To support security investigations, detection, and auditing, log data events for Amazon S3 buckets that store sensitive or business-critical data.

**To log data events for trails**

1. Open the [CloudTrail console](https://console.aws.amazon.com/cloudtrail/).

1. In the navigation pane, choose **Trails**, and then choose a trail name.

1. In **General details**, choose **Edit **to change the following settings (you cannot change the name of a trail).

   1. In **Data events**, choose **Edit**.

   1. For **Data event source**, choose **S3**.

   1. For **All current and future S3 buckets**, clear the default selections for **Read** and **Write**.

   1. In **Individual bucket selection**, choose the bucket on which to log data events. To add more buckets, choose **Add bucket**.

   1. Choose to log **Read** events (such as `GetObject`), **Write** events (such as `PutObject`), or both.

   1. Choose **Update trail**.

**Note**
Additional charges apply for logging CloudTrail data events. For more information, see [AWS CloudTrail pricing](https://aws.amazon.com/cloudtrail/pricing/).
