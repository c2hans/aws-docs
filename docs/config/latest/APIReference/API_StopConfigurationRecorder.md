---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_StopConfigurationRecorder.html
---

# StopConfigurationRecorder
<a name="API_StopConfigurationRecorder"></a>

Stops the customer managed configuration recorder. The customer managed configuration recorder will stop recording configuration changes for the resource types you have specified.

## Request Syntax
<a name="API_StopConfigurationRecorder_RequestSyntax"></a>

```
{
   "ConfigurationRecorderName": "{{string}}"
}
```

## Request Parameters
<a name="API_StopConfigurationRecorder_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConfigurationRecorderName](#API_StopConfigurationRecorder_RequestSyntax) **   <a name="config-StopConfigurationRecorder-request-ConfigurationRecorderName"></a>
The name of the customer managed configuration recorder that you want to stop.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Response Elements
<a name="API_StopConfigurationRecorder_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_StopConfigurationRecorder_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** NoSuchConfigurationRecorderException **
You have specified a configuration recorder that does not exist.
HTTP Status Code: 400

 ** UnmodifiableEntityException **
The requested operation is not valid.
For [PutConfigurationRecorder](https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigurationRecorder.html), you will see this exception because you cannot use this operation to create a service-linked configuration recorder. Use the [PutServiceLinkedConfigurationRecorder](https://docs.aws.amazon.com/config/latest/APIReference/API_PutServiceLinkedConfigurationRecorder.html) operation to create a service-linked configuration recorder.
For [DeleteConfigurationRecorder](https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteConfigurationRecorder.html), you will see this exception because you cannot use this operation to delete a service-linked configuration recorder. Use the [DeleteServiceLinkedConfigurationRecorder](https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html) operation to delete a service-linked configuration recorder.
For [StartConfigurationRecorder](https://docs.aws.amazon.com/config/latest/APIReference/API_StartConfigurationRecorder.html) and [StopConfigurationRecorder](https://docs.aws.amazon.com/config/latest/APIReference/API_StopConfigurationRecorder.html), you will see this exception because these operations do not affect service-linked configuration recorders. Service-linked configuration recorders are always recording. To stop recording, you must delete the service-linked configuration recorder. Use the [DeleteServiceLinkedConfigurationRecorder](https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html) operation to delete a service-linked configuration recorder.
HTTP Status Code: 400

## See Also
<a name="API_StopConfigurationRecorder_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/StopConfigurationRecorder)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/StopConfigurationRecorder)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/StopConfigurationRecorder)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/StopConfigurationRecorder)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/StopConfigurationRecorder)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/StopConfigurationRecorder)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/StopConfigurationRecorder)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/StopConfigurationRecorder)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/StopConfigurationRecorder)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/StopConfigurationRecorder)
