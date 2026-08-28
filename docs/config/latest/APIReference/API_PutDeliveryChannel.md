---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_PutDeliveryChannel.html
---

# PutDeliveryChannel
<a name="API_PutDeliveryChannel"></a>

Creates or updates a delivery channel to deliver configuration information and other compliance information.

You can use this operation to create a new delivery channel or to update the Amazon S3 bucket and the Amazon SNS topic of an existing delivery channel.

For more information, see [**Working with the Delivery Channel**](https://docs.aws.amazon.com/config/latest/developerguide/manage-delivery-channel.html) in the * AWS Config Developer Guide.*

**Note**
 **One delivery channel per account per Region**
You can have only one delivery channel for each account for each AWS Region.

## Request Syntax
<a name="API_PutDeliveryChannel_RequestSyntax"></a>

```
{
   "DeliveryChannel": {
      "configSnapshotDeliveryProperties": {
         "deliveryFrequency": "{{string}}"
      },
      "name": "{{string}}",
      "s3BucketName": "{{string}}",
      "s3KeyPrefix": "{{string}}",
      "s3KmsKeyArn": "{{string}}",
      "snsTopicARN": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_PutDeliveryChannel_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DeliveryChannel](#API_PutDeliveryChannel_RequestSyntax) **   <a name="config-PutDeliveryChannel-request-DeliveryChannel"></a>
An object for the delivery channel. A delivery channel sends notifications and updated configuration states.
Type: [DeliveryChannel](API_DeliveryChannel.md) object
Required: Yes

## Response Elements
<a name="API_PutDeliveryChannel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutDeliveryChannel_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InsufficientDeliveryPolicyException **
Your Amazon S3 bucket policy does not allow AWS Config to write to it.
HTTP Status Code: 400

 ** InvalidDeliveryChannelNameException **
The specified delivery channel name is not valid.
HTTP Status Code: 400

 ** InvalidS3KeyPrefixException **
The specified Amazon S3 key prefix is not valid.
HTTP Status Code: 400

 ** InvalidS3KmsKeyArnException **
The specified Amazon KMS Key ARN is not valid.
HTTP Status Code: 400

 ** InvalidSNSTopicARNException **
The specified Amazon SNS topic does not exist.
HTTP Status Code: 400

 ** MaxNumberOfDeliveryChannelsExceededException **
You have reached the limit of the number of delivery channels you can create.
HTTP Status Code: 400

 ** NoAvailableConfigurationRecorderException **
There are no customer managed configuration recorders available to record your resources. Use the [PutConfigurationRecorder](https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigurationRecorder.html) operation to create the customer managed configuration recorder.
HTTP Status Code: 400

 ** NoSuchBucketException **
The specified Amazon S3 bucket does not exist.
HTTP Status Code: 400

## See Also
<a name="API_PutDeliveryChannel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/PutDeliveryChannel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/PutDeliveryChannel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/PutDeliveryChannel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/PutDeliveryChannel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/PutDeliveryChannel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/PutDeliveryChannel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/PutDeliveryChannel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/PutDeliveryChannel)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/PutDeliveryChannel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/PutDeliveryChannel)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
