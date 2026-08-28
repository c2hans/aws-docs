---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_DeliverConfigSnapshot.html
---

# DeliverConfigSnapshot
<a name="API_DeliverConfigSnapshot"></a>

Schedules delivery of a configuration snapshot to the Amazon S3 bucket in the specified delivery channel. After the delivery has started, AWS Config sends the following notifications using an Amazon SNS topic that you have specified.
+ Notification of the start of the delivery.
+ Notification of the completion of the delivery, if the delivery was successfully completed.
+ Notification of delivery failure, if the delivery failed.

## Request Syntax
<a name="API_DeliverConfigSnapshot_RequestSyntax"></a>

```
{
   "deliveryChannelName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeliverConfigSnapshot_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [deliveryChannelName](#API_DeliverConfigSnapshot_RequestSyntax) **   <a name="config-DeliverConfigSnapshot-request-deliveryChannelName"></a>
The name of the delivery channel through which the snapshot is delivered.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Response Syntax
<a name="API_DeliverConfigSnapshot_ResponseSyntax"></a>

```
{
   "configSnapshotId": "string"
}
```

## Response Elements
<a name="API_DeliverConfigSnapshot_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [configSnapshotId](#API_DeliverConfigSnapshot_ResponseSyntax) **   <a name="config-DeliverConfigSnapshot-response-configSnapshotId"></a>
The ID of the snapshot that is being created.
Type: String

## Errors
<a name="API_DeliverConfigSnapshot_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** NoAvailableConfigurationRecorderException **
There are no customer managed configuration recorders available to record your resources. Use the [PutConfigurationRecorder](https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigurationRecorder.html) operation to create the customer managed configuration recorder.
HTTP Status Code: 400

 ** NoRunningConfigurationRecorderException **
There is no configuration recorder running.
HTTP Status Code: 400

 ** NoSuchDeliveryChannelException **
You have specified a delivery channel that does not exist.
HTTP Status Code: 400

## See Also
<a name="API_DeliverConfigSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/DeliverConfigSnapshot)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/DeliverConfigSnapshot)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/DeliverConfigSnapshot)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/DeliverConfigSnapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/DeliverConfigSnapshot)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/DeliverConfigSnapshot)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/DeliverConfigSnapshot)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/DeliverConfigSnapshot)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/DeliverConfigSnapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/DeliverConfigSnapshot)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
