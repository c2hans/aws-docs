---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_ListQAppSessionData.html
---

# ListQAppSessionData
<a name="API_qapps_ListQAppSessionData"></a>

Lists the collected data of a Q App data collection session.

## Request Syntax
<a name="API_qapps_ListQAppSessionData_RequestSyntax"></a>

```
GET /runtime.listQAppSessionData?sessionId={{sessionId}} HTTP/1.1
instance-id: {{instanceId}}
```

## URI Request Parameters
<a name="API_qapps_ListQAppSessionData_RequestParameters"></a>

The request uses the following URI parameters.

 ** [instanceId](#API_qapps_ListQAppSessionData_RequestSyntax) **   <a name="qbusiness-qapps_ListQAppSessionData-request-instanceId"></a>
The unique identifier of the Amazon Q Business application environment instance.
Required: Yes

 ** [sessionId](#API_qapps_ListQAppSessionData_RequestSyntax) **   <a name="qbusiness-qapps_ListQAppSessionData-request-uri-sessionId"></a>
The unique identifier of the Q App data collection session.
Pattern: `[\da-f]{8}-[\da-f]{4}-[45][\da-f]{3}-[89ABab][\da-f]{3}-[\da-f]{12}`
Required: Yes

## Request Body
<a name="API_qapps_ListQAppSessionData_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_qapps_ListQAppSessionData_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "sessionArn": "string",
   "sessionData": [
      {
         "cardId": "string",
         "submissionId": "string",
         "timestamp": "string",
         "user": {
            "userId": "string"
         },
         "value": JSON value
      }
   ],
   "sessionId": "string"
}
```

## Response Elements
<a name="API_qapps_ListQAppSessionData_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_qapps_ListQAppSessionData_ResponseSyntax) **   <a name="qbusiness-qapps_ListQAppSessionData-response-nextToken"></a>
 The pagination token that indicates the next set of results to retrieve.
Type: String

 ** [sessionArn](#API_qapps_ListQAppSessionData_ResponseSyntax) **   <a name="qbusiness-qapps_ListQAppSessionData-response-sessionArn"></a>
The Amazon Resource Name (ARN) of the Q App data collection session.
Type: String

 ** [sessionData](#API_qapps_ListQAppSessionData_ResponseSyntax) **   <a name="qbusiness-qapps_ListQAppSessionData-response-sessionData"></a>
The collected responses of a Q App session.
Type: Array of [QAppSessionData](API_qapps_QAppSessionData.md) objects

 ** [sessionId](#API_qapps_ListQAppSessionData_ResponseSyntax) **   <a name="qbusiness-qapps_ListQAppSessionData-response-sessionId"></a>
The unique identifier of the Q App data collection session.
Type: String
Pattern: `[\da-f]{8}-[\da-f]{4}-[45][\da-f]{3}-[89ABab][\da-f]{3}-[\da-f]{12}`

## Errors
<a name="API_qapps_ListQAppSessionData_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The client is not authorized to perform the requested operation.
HTTP Status Code: 403

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
<a name="API_qapps_ListQAppSessionData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qapps-2023-11-27/ListQAppSessionData)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qapps-2023-11-27/ListQAppSessionData)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qapps-2023-11-27/ListQAppSessionData)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qapps-2023-11-27/ListQAppSessionData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qapps-2023-11-27/ListQAppSessionData)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qapps-2023-11-27/ListQAppSessionData)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qapps-2023-11-27/ListQAppSessionData)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qapps-2023-11-27/ListQAppSessionData)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/qapps-2023-11-27/ListQAppSessionData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qapps-2023-11-27/ListQAppSessionData)
