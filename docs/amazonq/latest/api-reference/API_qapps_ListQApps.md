---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_ListQApps.html
---

# ListQApps
<a name="API_qapps_ListQApps"></a>

Lists the Amazon Q Apps owned by or associated with the user either because they created it or because they used it from the library in the past. The user identity is extracted from the credentials used to invoke this operation..

## Request Syntax
<a name="API_qapps_ListQApps_RequestSyntax"></a>

```
GET /apps.list?limit={{limit}}&nextToken={{nextToken}} HTTP/1.1
instance-id: {{instanceId}}
```

## URI Request Parameters
<a name="API_qapps_ListQApps_RequestParameters"></a>

The request uses the following URI parameters.

 ** [instanceId](#API_qapps_ListQApps_RequestSyntax) **   <a name="qbusiness-qapps_ListQApps-request-instanceId"></a>
The unique identifier of the Amazon Q Business application environment instance.
Required: Yes

 ** [limit](#API_qapps_ListQApps_RequestSyntax) **   <a name="qbusiness-qapps_ListQApps-request-uri-limit"></a>
The maximum number of Q Apps to return in the response.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_qapps_ListQApps_RequestSyntax) **   <a name="qbusiness-qapps_ListQApps-request-uri-nextToken"></a>
The token to request the next page of results.
Length Constraints: Minimum length of 0. Maximum length of 300.

## Request Body
<a name="API_qapps_ListQApps_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_qapps_ListQApps_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "apps": [
      {
         "appArn": "string",
         "appId": "string",
         "canEdit": boolean,
         "createdAt": "string",
         "description": "string",
         "isVerified": boolean,
         "status": "string",
         "title": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_qapps_ListQApps_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [apps](#API_qapps_ListQApps_ResponseSyntax) **   <a name="qbusiness-qapps_ListQApps-response-apps"></a>
The list of Amazon Q Apps meeting the request criteria.
Type: Array of [UserAppItem](API_qapps_UserAppItem.md) objects

 ** [nextToken](#API_qapps_ListQApps_ResponseSyntax) **   <a name="qbusiness-qapps_ListQApps-response-nextToken"></a>
The token to use to request the next page of results.
Type: String

## Errors
<a name="API_qapps_ListQApps_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The client is not authorized to perform the requested operation.
HTTP Status Code: 403

 ** InternalServerException **
An internal service error occurred while processing the request.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the operation
HTTP Status Code: 500

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
<a name="API_qapps_ListQApps_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qapps-2023-11-27/ListQApps)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qapps-2023-11-27/ListQApps)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qapps-2023-11-27/ListQApps)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qapps-2023-11-27/ListQApps)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qapps-2023-11-27/ListQApps)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qapps-2023-11-27/ListQApps)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qapps-2023-11-27/ListQApps)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qapps-2023-11-27/ListQApps)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qapps-2023-11-27/ListQApps)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qapps-2023-11-27/ListQApps)
