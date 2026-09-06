---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_Notification.html
---

# Notification
<a name="API_Notification"></a>

**Note**
 AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

The Amazon Simple Notification Service (Amazon SNS) notification settings associated with a specific job. The `Notification` object is returned as a part of the response syntax of the `DescribeJob` action in the `JobMetadata` data type.

When the notification settings are defined during job creation, you can choose to notify based on a specific set of job states using the `JobStatesToNotify` array of strings, or you can specify that you want to have Amazon SNS notifications sent out for all job states with `NotifyAll` set to true.

## Contents
<a name="API_Notification_Contents"></a>

 ** DevicePickupSnsTopicARN **   <a name="Snowball-Type-Notification-DevicePickupSnsTopicARN"></a>
Used to send SNS notifications for the person picking up the device (identified during job creation).
Type: String
Length Constraints: Maximum length of 255.
Pattern: `arn:aws.*:sns:.*:[0-9]{12}:.*`
Required: No

 ** JobStatesToNotify **   <a name="Snowball-Type-Notification-JobStatesToNotify"></a>
The list of job states that will trigger a notification for this job.
Type: Array of strings
Valid Values: `New | PreparingAppliance | PreparingShipment | InTransitToCustomer | WithCustomer | InTransitToAWS | WithAWSSortingFacility | WithAWS | InProgress | Complete | Cancelled | Listing | Pending`
Required: No

 ** NotifyAll **   <a name="Snowball-Type-Notification-NotifyAll"></a>
Any change in job state will trigger a notification for this job.
Type: Boolean
Required: No

 ** SnsTopicARN **   <a name="Snowball-Type-Notification-SnsTopicARN"></a>
The new SNS `TopicArn` that you want to associate with this job. You can create Amazon Resource Names (ARNs) for topics by using the [CreateTopic](https://docs.aws.amazon.com/sns/latest/api/API_CreateTopic.html) Amazon SNS API action.
You can subscribe email addresses to an Amazon SNS topic through the AWS Management Console, or by using the [Subscribe](https://docs.aws.amazon.com/sns/latest/api/API_Subscribe.html) Amazon Simple Notification Service (Amazon SNS) API action.
Type: String
Length Constraints: Maximum length of 255.
Pattern: `arn:aws.*:sns:.*:[0-9]{12}:.*`
Required: No

## See Also
<a name="API_Notification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snowball-2016-06-30/Notification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snowball-2016-06-30/Notification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snowball-2016-06-30/Notification)
