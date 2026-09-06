---
source_url: https://docs.aws.amazon.com/appfabric/latest/api/API_CreateAppAuthorization.html
---

# CreateAppAuthorization
<a name="API_CreateAppAuthorization"></a>

Creates an app authorization within an app bundle, which allows AppFabric to connect to an application.

## Request Syntax
<a name="API_CreateAppAuthorization_RequestSyntax"></a>

```
POST /appbundles/{{appBundleIdentifier}}/appauthorizations HTTP/1.1
Content-type: application/json

{
   "app": "{{string}}",
   "authType": "{{string}}",
   "clientToken": "{{string}}",
   "credential": { ... },
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "tenant": {
      "tenantDisplayName": "{{string}}",
      "tenantIdentifier": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateAppAuthorization_RequestParameters"></a>

The request uses the following URI parameters.

 ** [appBundleIdentifier](#API_CreateAppAuthorization_RequestSyntax) **   <a name="appfabric-CreateAppAuthorization-request-uri-appBundleIdentifier"></a>
The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app bundle to use for the request.
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:.+$|^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

## Request Body
<a name="API_CreateAppAuthorization_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [app](#API_CreateAppAuthorization_RequestSyntax) **   <a name="appfabric-CreateAppAuthorization-request-app"></a>
The name of the application.
Valid values are:
+  `SLACK`
+  `ASANA`
+  `JIRA`
+  `M365`
+  `M365AUDITLOGS`
+  `ZOOM`
+  `ZENDESK`
+  `OKTA`
+  `GOOGLE`
+  `DROPBOX`
+  `SMARTSHEET`
+  `CISCO`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [authType](#API_CreateAppAuthorization_RequestSyntax) **   <a name="appfabric-CreateAppAuthorization-request-authType"></a>
The authorization type for the app authorization.
Type: String
Valid Values: `oauth2 | apiKey`
Required: Yes

 ** [clientToken](#API_CreateAppAuthorization_RequestSyntax) **   <a name="appfabric-CreateAppAuthorization-request-clientToken"></a>
Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a [UUID type of value](https://wikipedia.org/wiki/Universally_unique_identifier).
If you don't provide this value, then AWS generates a random one for you.
If you retry the operation with the same `ClientToken`, but with different parameters, the retry fails with an `IdempotentParameterMismatch` error.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** [credential](#API_CreateAppAuthorization_RequestSyntax) **   <a name="appfabric-CreateAppAuthorization-request-credential"></a>
Contains credentials for the application, such as an API key or OAuth2 client ID and secret.
Specify credentials that match the authorization type for your request. For example, if the authorization type for your request is OAuth2 (`oauth2`), then you should provide only the OAuth2 credentials.
Type: [Credential](API_Credential.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [tags](#API_CreateAppAuthorization_RequestSyntax) **   <a name="appfabric-CreateAppAuthorization-request-tags"></a>
A map of the key-value pairs of the tag or tags to assign to the resource.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [tenant](#API_CreateAppAuthorization_RequestSyntax) **   <a name="appfabric-CreateAppAuthorization-request-tenant"></a>
Contains information about an application tenant, such as the application display name and identifier.
Type: [Tenant](API_Tenant.md) object
Required: Yes

## Response Syntax
<a name="API_CreateAppAuthorization_ResponseSyntax"></a>

```
HTTP/1.1 201
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
<a name="API_CreateAppAuthorization_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [appAuthorization](#API_CreateAppAuthorization_ResponseSyntax) **   <a name="appfabric-CreateAppAuthorization-response-appAuthorization"></a>
Contains information about an app authorization.
Type: [AppAuthorization](API_AppAuthorization.md) object

## Errors
<a name="API_CreateAppAuthorization_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You are not authorized to perform this operation.
HTTP Status Code: 403

 ** ConflictException **
The request has created a conflict. Check the request parameters and try again.
 ** resourceId **
The resource ID.
 ** resourceType **
The resource type.
HTTP Status Code: 409

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

 ** ServiceQuotaExceededException **
The request exceeds a service quota.
 ** quotaCode **
The code for the quota exceeded.
 ** resourceId **
The resource ID.
 ** resourceType **
The resource type.
 ** serviceCode **
The code of the service.
HTTP Status Code: 402

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
<a name="API_CreateAppAuthorization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appfabric-2023-05-19/CreateAppAuthorization)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appfabric-2023-05-19/CreateAppAuthorization)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appfabric-2023-05-19/CreateAppAuthorization)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appfabric-2023-05-19/CreateAppAuthorization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appfabric-2023-05-19/CreateAppAuthorization)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appfabric-2023-05-19/CreateAppAuthorization)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appfabric-2023-05-19/CreateAppAuthorization)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appfabric-2023-05-19/CreateAppAuthorization)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appfabric-2023-05-19/CreateAppAuthorization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appfabric-2023-05-19/CreateAppAuthorization)
