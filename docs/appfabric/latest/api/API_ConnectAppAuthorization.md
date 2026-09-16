---
source_url: https://docs.aws.amazon.com/appfabric/latest/api/API_ConnectAppAuthorization.html
---

# ConnectAppAuthorization
<a name="API_ConnectAppAuthorization"></a>

Establishes a connection between AWS AppFabric and an application, which allows AppFabric to call the APIs of the application.

## Request Syntax
<a name="API_ConnectAppAuthorization_RequestSyntax"></a>

```
POST /appbundles/{{appBundleIdentifier}}/appauthorizations/{{appAuthorizationIdentifier}}/connect HTTP/1.1
Content-type: application/json

{
   "authRequest": {
      "code": "{{string}}",
      "redirectUri": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_ConnectAppAuthorization_RequestParameters"></a>

The request uses the following URI parameters.

 ** [appAuthorizationIdentifier](#API_ConnectAppAuthorization_RequestSyntax) **   <a name="appfabric-ConnectAppAuthorization-request-uri-appAuthorizationIdentifier"></a>
The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app authorization to use for the request.
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:.+$|^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** [appBundleIdentifier](#API_ConnectAppAuthorization_RequestSyntax) **   <a name="appfabric-ConnectAppAuthorization-request-uri-appBundleIdentifier"></a>
The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app bundle that contains the app authorization to use for the request.
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:.+$|^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

## Request Body
<a name="API_ConnectAppAuthorization_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [authRequest](#API_ConnectAppAuthorization_RequestSyntax) **   <a name="appfabric-ConnectAppAuthorization-request-authRequest"></a>
Contains OAuth2 authorization information.
This is required if the app authorization for the request is configured with an OAuth2 (`oauth2`) authorization type.
Type: [AuthRequest](API_AuthRequest.md) object
Required: No

## Response Syntax
<a name="API_ConnectAppAuthorization_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "appAuthorizationSummary": {
      "app": "string",
      "appAuthorizationArn": "string",
      "appBundleArn": "string",
      "status": "string",
      "tenant": {
         "tenantDisplayName": "string",
         "tenantIdentifier": "string"
      },
      "updatedAt": "string"
   }
}
```

## Response Elements
<a name="API_ConnectAppAuthorization_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [appAuthorizationSummary](#API_ConnectAppAuthorization_ResponseSyntax) **   <a name="appfabric-ConnectAppAuthorization-response-appAuthorizationSummary"></a>
Contains a summary of the app authorization.
Type: [AppAuthorizationSummary](API_AppAuthorizationSummary.md) object

## Errors
<a name="API_ConnectAppAuthorization_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You are not authorized to perform this operation.
HTTP Status Code: 403

 ** InternalServerException **
The request processing has failed because of an unknown error, exception, or failure with an internal server.
 ** retryAfterSeconds **
The period of time after which you should retry your request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** resourceId **
The resource ID.
 ** resourceType **
The resource type.
HTTP Status Code: 404

 ** ThrottlingException **
The request rate exceeds the limit.
 ** quotaCode **
The code for the quota exceeded.
 ** retryAfterSeconds **
The period of time after which you should retry your request.
 ** serviceCode **
The code of the service.
HTTP Status Code: 429

 ** ValidationException **
The request has invalid or missing parameters.
 ** fieldList **
The field list.
 ** reason **
The reason for the exception.
HTTP Status Code: 400

## See Also
<a name="API_ConnectAppAuthorization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appfabric-2023-05-19/ConnectAppAuthorization)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appfabric-2023-05-19/ConnectAppAuthorization)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appfabric-2023-05-19/ConnectAppAuthorization)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appfabric-2023-05-19/ConnectAppAuthorization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appfabric-2023-05-19/ConnectAppAuthorization)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appfabric-2023-05-19/ConnectAppAuthorization)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appfabric-2023-05-19/ConnectAppAuthorization)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appfabric-2023-05-19/ConnectAppAuthorization)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/appfabric-2023-05-19/ConnectAppAuthorization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appfabric-2023-05-19/ConnectAppAuthorization)
