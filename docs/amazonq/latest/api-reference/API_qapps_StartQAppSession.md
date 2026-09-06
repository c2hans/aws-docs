---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_StartQAppSession.html
---

# StartQAppSession
<a name="API_qapps_StartQAppSession"></a>

Starts a new session for an Amazon Q App, allowing inputs to be provided and the app to be run.

**Note**
Each Q App session will be condensed into a single conversation in the web experience.

## Request Syntax
<a name="API_qapps_StartQAppSession_RequestSyntax"></a>

```
POST /runtime.startQAppSession HTTP/1.1
instance-id: {{instanceId}}
Content-type: application/json

{
   "appId": "{{string}}",
   "appVersion": {{number}},
   "initialValues": [
      {
         "cardId": "{{string}}",
         "submissionMutation": {
            "mutationType": "{{string}}",
            "submissionId": "{{string}}"
         },
         "value": "{{string}}"
      }
   ],
   "sessionId": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_qapps_StartQAppSession_RequestParameters"></a>

The request uses the following URI parameters.

 ** [instanceId](#API_qapps_StartQAppSession_RequestSyntax) **   <a name="qbusiness-qapps_StartQAppSession-request-instanceId"></a>
The unique identifier of the Amazon Q Business application environment instance.
Required: Yes

## Request Body
<a name="API_qapps_StartQAppSession_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [appId](#API_qapps_StartQAppSession_RequestSyntax) **   <a name="qbusiness-qapps_StartQAppSession-request-appId"></a>
The unique identifier of the Q App to start a session for.
Type: String
Pattern: `[\da-f]{8}-[\da-f]{4}-[45][\da-f]{3}-[89ABab][\da-f]{3}-[\da-f]{12}`
Required: Yes

 ** [appVersion](#API_qapps_StartQAppSession_RequestSyntax) **   <a name="qbusiness-qapps_StartQAppSession-request-appVersion"></a>
The version of the Q App to use for the session.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: Yes

 ** [initialValues](#API_qapps_StartQAppSession_RequestSyntax) **   <a name="qbusiness-qapps_StartQAppSession-request-initialValues"></a>
Optional initial input values to provide for the Q App session.
Type: Array of [CardValue](API_qapps_CardValue.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** [sessionId](#API_qapps_StartQAppSession_RequestSyntax) **   <a name="qbusiness-qapps_StartQAppSession-request-sessionId"></a>
The unique identifier of the a Q App session.
Type: String
Required: No

 ** [tags](#API_qapps_StartQAppSession_RequestSyntax) **   <a name="qbusiness-qapps_StartQAppSession-request-tags"></a>
Optional tags to associate with the new Q App session.
Type: String to string map
Required: No

## Response Syntax
<a name="API_qapps_StartQAppSession_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "sessionArn": "string",
   "sessionId": "string"
}
```

## Response Elements
<a name="API_qapps_StartQAppSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [sessionArn](#API_qapps_StartQAppSession_ResponseSyntax) **   <a name="qbusiness-qapps_StartQAppSession-response-sessionArn"></a>
The Amazon Resource Name (ARN) of the new Q App session.
Type: String

 ** [sessionId](#API_qapps_StartQAppSession_ResponseSyntax) **   <a name="qbusiness-qapps_StartQAppSession-response-sessionId"></a>
The unique identifier of the new or retrieved Q App session.
Type: String

## Errors
<a name="API_qapps_StartQAppSession_Errors"></a>

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
<a name="API_qapps_StartQAppSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qapps-2023-11-27/StartQAppSession)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qapps-2023-11-27/StartQAppSession)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qapps-2023-11-27/StartQAppSession)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qapps-2023-11-27/StartQAppSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qapps-2023-11-27/StartQAppSession)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qapps-2023-11-27/StartQAppSession)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qapps-2023-11-27/StartQAppSession)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qapps-2023-11-27/StartQAppSession)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qapps-2023-11-27/StartQAppSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qapps-2023-11-27/StartQAppSession)
