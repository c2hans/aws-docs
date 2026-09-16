---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteDeliveryChannel.html
---

# DeleteDeliveryChannel
<a name="API_DeleteDeliveryChannel"></a>

Deletes the delivery channel.

Before you can delete the delivery channel, you must stop the customer managed configuration recorder. You can use the [StopConfigurationRecorder](API_StopConfigurationRecorder.md) operation to stop the customer managed configuration recorder.

## Request Syntax
<a name="API_DeleteDeliveryChannel_RequestSyntax"></a>

```
{
   "DeliveryChannelName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteDeliveryChannel_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DeliveryChannelName](#API_DeleteDeliveryChannel_RequestSyntax) **   <a name="config-DeleteDeliveryChannel-request-DeliveryChannelName"></a>
The name of the delivery channel that you want to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Response Elements
<a name="API_DeleteDeliveryChannel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteDeliveryChannel_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** LastDeliveryChannelDeleteFailedException **
You cannot delete the delivery channel you specified because the customer managed configuration recorder is running.
HTTP Status Code: 400

 ** NoSuchDeliveryChannelException **
You have specified a delivery channel that does not exist.
HTTP Status Code: 400

## See Also
<a name="API_DeleteDeliveryChannel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/DeleteDeliveryChannel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/DeleteDeliveryChannel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/DeleteDeliveryChannel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/DeleteDeliveryChannel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/DeleteDeliveryChannel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/DeleteDeliveryChannel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/DeleteDeliveryChannel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/DeleteDeliveryChannel)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/DeleteDeliveryChannel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/DeleteDeliveryChannel)
