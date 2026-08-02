---
source_url: https://docs.aws.amazon.com/panorama/latest/api/API_SignalApplicationInstanceNodeInstances.html
---

# SignalApplicationInstanceNodeInstances
<a name="API_SignalApplicationInstanceNodeInstances"></a>

**Important**
End of support notice: On May 31, 2026, AWS will end support for AWS Panorama. After May 31, 2026, you will no longer be able to access the AWS Panorama console or AWS Panorama resources. For more information, see [AWS Panorama end of support](https://docs.aws.amazon.com/panorama/latest/dev/panorama-end-of-support.html).

Signal camera nodes to stop or resume.

## Request Syntax
<a name="API_SignalApplicationInstanceNodeInstances_RequestSyntax"></a>

```
PUT /application-instances/{{ApplicationInstanceId}}/node-signals HTTP/1.1
Content-type: application/json

{
   "NodeSignals": [
      {
         "NodeInstanceId": "{{string}}",
         "Signal": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_SignalApplicationInstanceNodeInstances_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ApplicationInstanceId](#API_SignalApplicationInstanceNodeInstances_RequestSyntax) **   <a name="panorama-SignalApplicationInstanceNodeInstances-request-uri-ApplicationInstanceId"></a>
An application instance ID.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_]+`
Required: Yes

## Request Body
<a name="API_SignalApplicationInstanceNodeInstances_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [NodeSignals](#API_SignalApplicationInstanceNodeInstances_RequestSyntax) **   <a name="panorama-SignalApplicationInstanceNodeInstances-request-NodeSignals"></a>
A list of signals.
Type: Array of [NodeSignal](API_NodeSignal.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

## Response Syntax
<a name="API_SignalApplicationInstanceNodeInstances_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ApplicationInstanceId": "string"
}
```

## Response Elements
<a name="API_SignalApplicationInstanceNodeInstances_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationInstanceId](#API_SignalApplicationInstanceNodeInstances_ResponseSyntax) **   <a name="panorama-SignalApplicationInstanceNodeInstances-response-ApplicationInstanceId"></a>
An application instance ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_]+`

## Errors
<a name="API_SignalApplicationInstanceNodeInstances_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The requestor does not have permission to access the target action or resource.
HTTP Status Code: 403

 ** InternalServerException **
An internal error occurred.
 ** RetryAfterSeconds **
The number of seconds a client should wait before retrying the call.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
The request would cause a limit to be exceeded.
 ** QuotaCode **
The name of the limit.
 ** ResourceId **
The target resource's ID.
 ** ResourceType **
The target resource's type.
 ** ServiceCode **
The name of the service.
HTTP Status Code: 402

 ** ValidationException **
The request contains an invalid parameter value.
 ** ErrorArguments **
A list of attributes that led to the exception and their values.
 ** ErrorId **
A unique ID for the error.
 ** Fields **
A list of request parameters that failed validation.
 ** Reason **
The reason that validation failed.
HTTP Status Code: 400

## See Also
<a name="API_SignalApplicationInstanceNodeInstances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/panorama-2019-07-24/SignalApplicationInstanceNodeInstances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/panorama-2019-07-24/SignalApplicationInstanceNodeInstances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/panorama-2019-07-24/SignalApplicationInstanceNodeInstances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/panorama-2019-07-24/SignalApplicationInstanceNodeInstances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/panorama-2019-07-24/SignalApplicationInstanceNodeInstances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/panorama-2019-07-24/SignalApplicationInstanceNodeInstances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/panorama-2019-07-24/SignalApplicationInstanceNodeInstances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/panorama-2019-07-24/SignalApplicationInstanceNodeInstances)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/panorama-2019-07-24/SignalApplicationInstanceNodeInstances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/panorama-2019-07-24/SignalApplicationInstanceNodeInstances)
