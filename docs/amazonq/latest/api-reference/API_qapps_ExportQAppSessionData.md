---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_ExportQAppSessionData.html
---

# ExportQAppSessionData
<a name="API_qapps_ExportQAppSessionData"></a>

Exports the collected data of a Q App data collection session.

## Request Syntax
<a name="API_qapps_ExportQAppSessionData_RequestSyntax"></a>

```
POST /runtime.exportQAppSessionData HTTP/1.1
instance-id: {{instanceId}}
Content-type: application/json

{
   "sessionId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_qapps_ExportQAppSessionData_RequestParameters"></a>

The request uses the following URI parameters.

 ** [instanceId](#API_qapps_ExportQAppSessionData_RequestSyntax) **   <a name="qbusiness-qapps_ExportQAppSessionData-request-instanceId"></a>
The unique identifier of the Amazon Q Business application environment instance.
Required: Yes

## Request Body
<a name="API_qapps_ExportQAppSessionData_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [sessionId](#API_qapps_ExportQAppSessionData_RequestSyntax) **   <a name="qbusiness-qapps_ExportQAppSessionData-request-sessionId"></a>
The unique identifier of the Q App data collection session.
Type: String
Pattern: `[\da-f]{8}-[\da-f]{4}-[45][\da-f]{3}-[89ABab][\da-f]{3}-[\da-f]{12}`
Required: Yes

## Response Syntax
<a name="API_qapps_ExportQAppSessionData_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "csvFileLink": "string",
   "expiresAt": "string",
   "sessionArn": "string"
}
```

## Response Elements
<a name="API_qapps_ExportQAppSessionData_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [csvFileLink](#API_qapps_ExportQAppSessionData_ResponseSyntax) **   <a name="qbusiness-qapps_ExportQAppSessionData-response-csvFileLink"></a>
The link where the exported Q App session data can be downloaded from.
Type: String

 ** [expiresAt](#API_qapps_ExportQAppSessionData_ResponseSyntax) **   <a name="qbusiness-qapps_ExportQAppSessionData-response-expiresAt"></a>
The date and time when the link for the exported Q App session data expires.
Type: Timestamp

 ** [sessionArn](#API_qapps_ExportQAppSessionData_ResponseSyntax) **   <a name="qbusiness-qapps_ExportQAppSessionData-response-sessionArn"></a>
The Amazon Resource Name (ARN) of the Q App data collection session.
Type: String

## Errors
<a name="API_qapps_ExportQAppSessionData_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The client is not authorized to perform the requested operation.
HTTP Status Code: 403

 ** ConflictException **
The requested operation could not be completed due to a conflict with the current state of the resource.
 ** resourceId **
The unique identifier of the resource
 ** resourceType **
The type of the resource
HTTP Status Code: 409

 ** InternalServerException **
An internal service error occurred while processing the request.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the operation
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource could not be found.
 ** resourceId **
The unique identifier of the resource
 ** resourceType **
The type of the resource
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The requested operation could not be completed because it would exceed the service's quota or limit.
 ** quotaCode **
The code of the quota that was exceeded
 ** resourceId **
The unique identifier of the resource
 ** resourceType **
The type of the resource
 ** serviceCode **
The code for the service where the quota was exceeded
HTTP Status Code: 402

 ** ThrottlingException **
The requested operation could not be completed because too many requests were sent at once. Wait a bit and try again later.
 ** quotaCode **
The code of the quota that was exceeded
 ** retryAfterSeconds **
The number of seconds to wait before retrying the operation
 ** serviceCode **
The code for the service where the quota was exceeded
HTTP Status Code: 429

 ** UnauthorizedException **
The client is not authenticated or authorized to perform the requested operation.
HTTP Status Code: 401

 ** ValidationException **
The input failed to satisfy the constraints specified by the service.
HTTP Status Code: 400

## See Also
<a name="API_qapps_ExportQAppSessionData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qapps-2023-11-27/ExportQAppSessionData)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qapps-2023-11-27/ExportQAppSessionData)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qapps-2023-11-27/ExportQAppSessionData)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qapps-2023-11-27/ExportQAppSessionData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qapps-2023-11-27/ExportQAppSessionData)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qapps-2023-11-27/ExportQAppSessionData)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qapps-2023-11-27/ExportQAppSessionData)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qapps-2023-11-27/ExportQAppSessionData)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/qapps-2023-11-27/ExportQAppSessionData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qapps-2023-11-27/ExportQAppSessionData)
