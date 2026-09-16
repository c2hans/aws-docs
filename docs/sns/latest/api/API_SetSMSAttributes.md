---
source_url: https://docs.aws.amazon.com/sns/latest/api/API_SetSMSAttributes.html
---

# SetSMSAttributes
<a name="API_SetSMSAttributes"></a>

Use this request to set the default settings for sending SMS messages and receiving daily SMS usage reports.

You can override some of these settings for a single message when you use the `Publish` action with the `MessageAttributes.entry.N` parameter. For more information, see [Publishing to a mobile phone](https://docs.aws.amazon.com/sns/latest/dg/sms_publish-to-phone.html) in the *Amazon SNS Developer Guide*.

**Note**
To use this operation, you must grant the Amazon SNS service principal (`sns.amazonaws.com`) permission to perform the `s3:ListBucket` action.

## Request Parameters
<a name="API_SetSMSAttributes_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **attributes** attributes.entry.N.key (key)attributes.entry.N.value (value)
The default settings for sending SMS messages from your AWS account. You can set values for the following attribute names:
 `MonthlySpendLimit` – The maximum amount in USD that you are willing to spend each month to send SMS messages. When Amazon SNS determines that sending an SMS message would incur a cost that exceeds this limit, it stops sending SMS messages within minutes.
Amazon SNS stops sending SMS messages within minutes of the limit being crossed. During that interval, if you continue to send SMS messages, you will incur costs that exceed your limit.
By default, the spend limit is set to the maximum allowed by Amazon SNS. If you want to raise the limit, submit an [SNS Limit Increase case](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-sns). For **New limit value**, enter your desired monthly spend limit. In the **Use Case Description** field, explain that you are requesting an SMS monthly spend limit increase.
 `DeliveryStatusIAMRole` – The ARN of the IAM role that allows Amazon SNS to write logs about SMS deliveries in CloudWatch Logs. For each SMS message that you send, Amazon SNS writes a log that includes the message price, the success or failure status, the reason for failure (if the message failed), the message dwell time, and other information.
 `DeliveryStatusSuccessSamplingRate` – The percentage of successful SMS deliveries for which Amazon SNS will write logs in CloudWatch Logs. The value can be an integer from 0 - 100. For example, to write logs only for failed deliveries, set this value to `0`. To write logs for 10% of your successful deliveries, set it to `10`.
 `DefaultSenderID` – A string, such as your business brand, that is displayed as the sender on the receiving device. Support for sender IDs varies by country. The sender ID can be 1 - 11 alphanumeric characters, and it must contain at least one letter.
 `DefaultSMSType` – The type of SMS message that you will send by default. You can assign the following values:
+  `Promotional` – (Default) Noncritical messages, such as marketing messages. Amazon SNS optimizes the message delivery to incur the lowest cost.
+  `Transactional` – Critical messages that support customer transactions, such as one-time passcodes for multi-factor authentication. Amazon SNS optimizes the message delivery to achieve the highest reliability.
 `UsageReportS3Bucket` – The name of the Amazon S3 bucket to receive daily SMS usage reports from Amazon SNS. Each day, Amazon SNS will deliver a usage report as a CSV file to the bucket. The report includes the following information for each SMS message that was successfully delivered by your AWS account:
+ Time that the message was published (in UTC)
+ Message ID
+ Destination phone number
+ Message type
+ Delivery status
+ Message price (in USD)
+ Part number (a message is split into multiple parts if it is too long for a single message)
+ Total number of parts
To receive the report, the bucket must have a policy that allows the Amazon SNS service principal to perform the `s3:PutObject` and `s3:GetBucketLocation` actions.
For an example bucket policy and usage report, see [Monitoring SMS Activity](https://docs.aws.amazon.com/sns/latest/dg/sms_stats.html) in the *Amazon SNS Developer Guide*.
Type: String to string map
Required: Yes

## Errors
<a name="API_SetSMSAttributes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AuthorizationError **
Indicates that the user has been denied access to the requested resource.
HTTP Status Code: 403

 ** InternalError **
Indicates an internal service error.
HTTP Status Code: 500

 ** InvalidParameter **
Indicates that a request parameter does not comply with the associated constraints.
HTTP Status Code: 400

 ** Throttled **
Indicates that the rate at which requests have been submitted for this action exceeds the limit for your Amazon Web Services account.
 ** message **
Throttled request.
HTTP Status Code: 429

## Examples
<a name="API_SetSMSAttributes_Examples"></a>

### Example policy
<a name="API_SetSMSAttributes_Example_1"></a>

You can use the following example policy to provide permission for the Amazon SNS service principal to run the `s3:ListBucket` action. Replace `amzn-s3-demo-bucket` with the S3 bucket you specified in the `UsageReportS3Bucket` parameter.

```
{
  "Version": "2008-10-17",
  "Statement": [{
            "Sid": "AllowListBucket",
            "Effect": "Allow",
            "Principal": {
                "Service": "sns.amazonaws.com"
            },
            "Action": "s3:ListBucket",
            "Resource": "arn:aws:s3:::amzn-s3-demo-bucket"
        }]
}
```

## See Also
<a name="API_SetSMSAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sns-2010-03-31/SetSMSAttributes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sns-2010-03-31/SetSMSAttributes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sns-2010-03-31/SetSMSAttributes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sns-2010-03-31/SetSMSAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sns-2010-03-31/SetSMSAttributes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sns-2010-03-31/SetSMSAttributes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sns-2010-03-31/SetSMSAttributes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sns-2010-03-31/SetSMSAttributes)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sns-2010-03-31/SetSMSAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sns-2010-03-31/SetSMSAttributes)
