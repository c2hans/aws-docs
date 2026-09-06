---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_GetQAppSession.html
---

# GetQAppSession
<a name="API_qapps_GetQAppSession"></a>

Retrieves the current state and results for an active session of an Amazon Q App.

## Request Syntax
<a name="API_qapps_GetQAppSession_RequestSyntax"></a>

```
GET /runtime.getQAppSession?sessionId={{sessionId}} HTTP/1.1
instance-id: {{instanceId}}
```

## URI Request Parameters
<a name="API_qapps_GetQAppSession_RequestParameters"></a>

The request uses the following URI parameters.

 ** [instanceId](#API_qapps_GetQAppSession_RequestSyntax) **   <a name="qbusiness-qapps_GetQAppSession-request-instanceId"></a>
The unique identifier of the Amazon Q Business application environment instance.
Required: Yes

 ** [sessionId](#API_qapps_GetQAppSession_RequestSyntax) **   <a name="qbusiness-qapps_GetQAppSession-request-uri-sessionId"></a>
The unique identifier of the Q App session to retrieve.
Pattern: `[\da-f]{8}-[\da-f]{4}-[45][\da-f]{3}-[89ABab][\da-f]{3}-[\da-f]{12}`
Required: Yes

## Request Body
<a name="API_qapps_GetQAppSession_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_qapps_GetQAppSession_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "appVersion": number,
   "cardStatus": {
      "string" : {
         "currentState": "string",
         "currentValue": "string",
         "submissions": [
            {
               "submissionId": "string",
               "timestamp": "string",
               "value": JSON value
            }
         ]
      }
   },
   "latestPublishedAppVersion": number,
   "sessionArn": "string",
   "sessionId": "string",
   "sessionName": "string",
   "status": "string",
   "userIsHost": boolean
}
```

## Response Elements
<a name="API_qapps_GetQAppSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [appVersion](#API_qapps_GetQAppSession_ResponseSyntax) **   <a name="qbusiness-qapps_GetQAppSession-response-appVersion"></a>
The version of the Q App used for the session.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.

 ** [cardStatus](#API_qapps_GetQAppSession_ResponseSyntax) **   <a name="qbusiness-qapps_GetQAppSession-response-cardStatus"></a>
The current status for each card in the Q App session.
Type: String to [CardStatus](API_qapps_CardStatus.md) object map
Key Pattern: `[\da-f]{8}-[\da-f]{4}-[45][\da-f]{3}-[89ABab][\da-f]{3}-[\da-f]{12}`

 ** [latestPublishedAppVersion](#API_qapps_GetQAppSession_ResponseSyntax) **   <a name="qbusiness-qapps_GetQAppSession-response-latestPublishedAppVersion"></a>
The latest published version of the Q App used for the session.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.

 ** [sessionArn](#API_qapps_GetQAppSession_ResponseSyntax) **   <a name="qbusiness-qapps_GetQAppSession-response-sessionArn"></a>
The Amazon Resource Name (ARN) of the Q App session.
Type: String

 ** [sessionId](#API_qapps_GetQAppSession_ResponseSyntax) **   <a name="qbusiness-qapps_GetQAppSession-response-sessionId"></a>
The unique identifier of the Q App session.
Type: String

 ** [sessionName](#API_qapps_GetQAppSession_ResponseSyntax) **   <a name="qbusiness-qapps_GetQAppSession-response-sessionName"></a>
The name of the Q App session.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.

 ** [status](#API_qapps_GetQAppSession_ResponseSyntax) **   <a name="qbusiness-qapps_GetQAppSession-response-status"></a>
The current status of the Q App session.
Type: String
Valid Values: `IN_PROGRESS | WAITING | COMPLETED | ERROR`

 ** [userIsHost](#API_qapps_GetQAppSession_ResponseSyntax) **   <a name="qbusiness-qapps_GetQAppSession-response-userIsHost"></a>
Indicates whether the current user is the owner of the Q App data collection session.
Type: Boolean

## Errors
<a name="API_qapps_GetQAppSession_Errors"></a>

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
<a name="API_qapps_GetQAppSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qapps-2023-11-27/GetQAppSession)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qapps-2023-11-27/GetQAppSession)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qapps-2023-11-27/GetQAppSession)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qapps-2023-11-27/GetQAppSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qapps-2023-11-27/GetQAppSession)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qapps-2023-11-27/GetQAppSession)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qapps-2023-11-27/GetQAppSession)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qapps-2023-11-27/GetQAppSession)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qapps-2023-11-27/GetQAppSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qapps-2023-11-27/GetQAppSession)
