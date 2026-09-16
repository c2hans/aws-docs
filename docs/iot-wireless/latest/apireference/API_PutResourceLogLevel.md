---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_PutResourceLogLevel.html
---

# PutResourceLogLevel
<a name="API_PutResourceLogLevel"></a>

Sets the log-level override for a resource ID and resource type. A limit of 200 log level override can be set per account.

## Request Syntax
<a name="API_PutResourceLogLevel_RequestSyntax"></a>

```
PUT /log-levels/{{ResourceIdentifier}}?resourceType={{ResourceType}} HTTP/1.1
Content-type: application/json

{
   "LogLevel": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutResourceLogLevel_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ResourceIdentifier](#API_PutResourceLogLevel_RequestSyntax) **   <a name="iotwireless-PutResourceLogLevel-request-uri-ResourceIdentifier"></a>
The unique identifier of the resource, which can be the wireless gateway ID, the wireless device ID, or the FUOTA task ID.
Length Constraints: Maximum length of 256.
Required: Yes

 ** [ResourceType](#API_PutResourceLogLevel_RequestSyntax) **   <a name="iotwireless-PutResourceLogLevel-request-uri-ResourceType"></a>
The type of resource, which can be `WirelessDevice`, `WirelessGateway`, or `FuotaTask`.
Required: Yes

## Request Body
<a name="API_PutResourceLogLevel_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [LogLevel](#API_PutResourceLogLevel_RequestSyntax) **   <a name="iotwireless-PutResourceLogLevel-request-LogLevel"></a>
The log level for a log message. The log levels can be disabled, or set to `ERROR` to display less verbose logs containing only error information, or to `INFO` for more detailed logs.
Type: String
Valid Values: `INFO | ERROR | DISABLED`
Required: Yes

## Response Syntax
<a name="API_PutResourceLogLevel_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutResourceLogLevel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutResourceLogLevel_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have permission to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred while processing a request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Resource does not exist.
 ** ResourceId **
Id of the not found resource.
 ** ResourceType **
Type of the font found resource.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied because it exceeded the allowed API request rate.
HTTP Status Code: 429

 ** ValidationException **
The input did not meet the specified constraints.
HTTP Status Code: 400

## See Also
<a name="API_PutResourceLogLevel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/PutResourceLogLevel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/PutResourceLogLevel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/PutResourceLogLevel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/PutResourceLogLevel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/PutResourceLogLevel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/PutResourceLogLevel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/PutResourceLogLevel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/PutResourceLogLevel)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/PutResourceLogLevel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/PutResourceLogLevel)
