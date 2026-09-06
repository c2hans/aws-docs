---
source_url: https://docs.aws.amazon.com/appfabric/latest/api/API_UpdateAppAuthorization.html
---

# UpdateAppAuthorization
<a name="API_UpdateAppAuthorization"></a>

Updates an app authorization within an app bundle, which allows AppFabric to connect to an application.

If the app authorization was in a `connected` state, updating the app authorization will set it back to a `PendingConnect` state.

## Request Syntax
<a name="API_UpdateAppAuthorization_RequestSyntax"></a>

```
PATCH /appbundles/{{appBundleIdentifier}}/appauthorizations/{{appAuthorizationIdentifier}} HTTP/1.1
Content-type: application/json

{
   "credential": { ... },
   "tenant": {
      "tenantDisplayName": "{{string}}",
      "tenantIdentifier": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateAppAuthorization_RequestParameters"></a>

The request uses the following URI parameters.

 ** [appAuthorizationIdentifier](#API_UpdateAppAuthorization_RequestSyntax) **   <a name="appfabric-UpdateAppAuthorization-request-uri-appAuthorizationIdentifier"></a>
The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app authorization to use for the request.
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:.+$|^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** [appBundleIdentifier](#API_UpdateAppAuthorization_RequestSyntax) **   <a name="appfabric-UpdateAppAuthorization-request-uri-appBundleIdentifier"></a>
The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app bundle to use for the request.
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:.+$|^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

## Request Body
<a name="API_UpdateAppAuthorization_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [credential](#API_UpdateAppAuthorization_RequestSyntax) **   <a name="appfabric-UpdateAppAuthorization-request-credential"></a>
Contains credentials for the application, such as an API key or OAuth2 client ID and secret.
Specify credentials that match the authorization type of the app authorization to update. For example, if the authorization type of the app authorization is OAuth2 (`oauth2`), then you should provide only the OAuth2 credentials.
Type: [Credential](API_Credential.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [tenant](#API_UpdateAppAuthorization_RequestSyntax) **   <a name="appfabric-UpdateAppAuthorization-request-tenant"></a>
Contains information about an application tenant, such as the application display name and identifier.
Type: [Tenant](API_Tenant.md) object
Required: No

## Response Syntax
<a name="API_UpdateAppAuthorization_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "appAuthorization": {
      "app": "string",
      "appAuthorizationArn": "string",
      "appBundleArn": "string",
      "authType": "string",
      "authUrl": "string",
      "createdAt": "string",
      "persona": "string",
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
<a name="API_UpdateAppAuthorization_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [appAuthorization](#API_UpdateAppAuthorization_ResponseSyntax) **   <a name="appfabric-UpdateAppAuthorization-response-appAuthorization"></a>
Contains information about an app authorization.
Type: [AppAuthorization](API_AppAuthorization.md) object

## Errors
<a name="API_UpdateAppAuthorization_Errors"></a>

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
<a name="API_UpdateAppAuthorization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appfabric-2023-05-19/UpdateAppAuthorization)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appfabric-2023-05-19/UpdateAppAuthorization)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appfabric-2023-05-19/UpdateAppAuthorization)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appfabric-2023-05-19/UpdateAppAuthorization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appfabric-2023-05-19/UpdateAppAuthorization)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appfabric-2023-05-19/UpdateAppAuthorization)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appfabric-2023-05-19/UpdateAppAuthorization)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appfabric-2023-05-19/UpdateAppAuthorization)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appfabric-2023-05-19/UpdateAppAuthorization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appfabric-2023-05-19/UpdateAppAuthorization)
