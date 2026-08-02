---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-app-integrations_CreateApplication.html
---

# CreateApplication
<a name="API_connect-app-integrations_CreateApplication"></a>

Creates and persists an Application resource.

## Request Syntax
<a name="API_connect-app-integrations_CreateApplication_RequestSyntax"></a>

```
POST /applications HTTP/1.1
Content-type: application/json

{
   "ApplicationConfig": {
      "ContactHandling": {
         "Scope": "{{string}}"
      }
   },
   "ApplicationSourceConfig": {
      "ExternalUrlConfig": {
         "AccessUrl": "{{string}}",
         "ApprovedOrigins": [ "{{string}}" ]
      }
   },
   "ApplicationType": "{{string}}",
   "ClientToken": "{{string}}",
   "Description": "{{string}}",
   "IframeConfig": {
      "Allow": [ "{{string}}" ],
      "Sandbox": [ "{{string}}" ]
   },
   "InitializationTimeout": {{number}},
   "IsService": {{boolean}},
   "Name": "{{string}}",
   "Namespace": "{{string}}",
   "Permissions": [ "{{string}}" ],
   "Publications": [
      {
         "Description": "{{string}}",
         "Event": "{{string}}",
         "Schema": "{{string}}"
      }
   ],
   "Subscriptions": [
      {
         "Description": "{{string}}",
         "Event": "{{string}}"
      }
   ],
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_connect-app-integrations_CreateApplication_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_connect-app-integrations_CreateApplication_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ApplicationConfig](#API_connect-app-integrations_CreateApplication_RequestSyntax) **   <a name="connect-connect-app-integrations_CreateApplication-request-ApplicationConfig"></a>
The configuration settings for the application.
Type: [ApplicationConfig](API_connect-app-integrations_ApplicationConfig.md) object
Required: No

 ** [ApplicationSourceConfig](#API_connect-app-integrations_CreateApplication_RequestSyntax) **   <a name="connect-connect-app-integrations_CreateApplication-request-ApplicationSourceConfig"></a>
The configuration for where the application should be loaded from.
Type: [ApplicationSourceConfig](API_connect-app-integrations_ApplicationSourceConfig.md) object
Required: Yes

 ** [ApplicationType](#API_connect-app-integrations_CreateApplication_RequestSyntax) **   <a name="connect-connect-app-integrations_CreateApplication-request-ApplicationType"></a>
The type of application.
Type: String
Valid Values: `STANDARD | SERVICE | MCP_SERVER`
Required: No

 ** [ClientToken](#API_connect-app-integrations_CreateApplication_RequestSyntax) **   <a name="connect-connect-app-integrations_CreateApplication-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `.*`
Required: No

 ** [Description](#API_connect-app-integrations_CreateApplication_RequestSyntax) **   <a name="connect-connect-app-integrations_CreateApplication-request-Description"></a>
The description of the application.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `.*`
Required: No

 ** [IframeConfig](#API_connect-app-integrations_CreateApplication_RequestSyntax) **   <a name="connect-connect-app-integrations_CreateApplication-request-IframeConfig"></a>
The iframe configuration for the application.
Type: [IframeConfig](API_connect-app-integrations_IframeConfig.md) object
Required: No

 ** [InitializationTimeout](#API_connect-app-integrations_CreateApplication_RequestSyntax) **   <a name="connect-connect-app-integrations_CreateApplication-request-InitializationTimeout"></a>
The maximum time in milliseconds allowed to establish a connection with the workspace.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 600000.
Required: No

 ** [IsService](#API_connect-app-integrations_CreateApplication_RequestSyntax) **   <a name="connect-connect-app-integrations_CreateApplication-request-IsService"></a>
 *This parameter has been deprecated.*
Indicates whether the application is a service.
Type: Boolean
Required: No

 ** [Name](#API_connect-app-integrations_CreateApplication_RequestSyntax) **   <a name="connect-connect-app-integrations_CreateApplication-request-Name"></a>
The name of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9\/\._ \-]+$`
Required: Yes

 ** [Namespace](#API_connect-app-integrations_CreateApplication_RequestSyntax) **   <a name="connect-connect-app-integrations_CreateApplication-request-Namespace"></a>
The namespace of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 211.
Pattern: `^[a-zA-Z0-9\/\._\-]+$`
Required: Yes

 ** [Permissions](#API_connect-app-integrations_CreateApplication_RequestSyntax) **   <a name="connect-connect-app-integrations_CreateApplication-request-Permissions"></a>
The configuration of events or requests that the application has access to.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 150 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9\/\._\-\*]+$`
Required: No

 ** [Publications](#API_connect-app-integrations_CreateApplication_RequestSyntax) **   <a name="connect-connect-app-integrations_CreateApplication-request-Publications"></a>
 *This parameter has been deprecated.*
The events that the application publishes.
Type: Array of [Publication](API_connect-app-integrations_Publication.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [Subscriptions](#API_connect-app-integrations_CreateApplication_RequestSyntax) **   <a name="connect-connect-app-integrations_CreateApplication-request-Subscriptions"></a>
 *This parameter has been deprecated.*
The events that the application subscribes.
Type: Array of [Subscription](API_connect-app-integrations_Subscription.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [Tags](#API_connect-app-integrations_CreateApplication_RequestSyntax) **   <a name="connect-connect-app-integrations_CreateApplication-request-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_connect-app-integrations_CreateApplication_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "Id": "string"
}
```

## Response Elements
<a name="API_connect-app-integrations_CreateApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_connect-app-integrations_CreateApplication_ResponseSyntax) **   <a name="connect-connect-app-integrations_CreateApplication-response-Arn"></a>
The Amazon Resource Name (ARN) of the Application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^arn:aws:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`

 ** [Id](#API_connect-app-integrations_CreateApplication_ResponseSyntax) **   <a name="connect-connect-app-integrations_CreateApplication-response-Id"></a>
A unique identifier for the Application.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

## Errors
<a name="API_connect-app-integrations_CreateApplication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** DuplicateResourceException **
A resource with the specified name already exists.
HTTP Status Code: 409

 ** InternalServiceError **
Request processing failed due to an error or failure with the service.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
HTTP Status Code: 400

 ** ResourceQuotaExceededException **
The allowed quota for the resource has been exceeded.
HTTP Status Code: 429

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

 ** UnsupportedOperationException **
The operation is not supported.
HTTP Status Code: 400

## See Also
<a name="API_connect-app-integrations_CreateApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appintegrations-2020-07-29/CreateApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appintegrations-2020-07-29/CreateApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appintegrations-2020-07-29/CreateApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appintegrations-2020-07-29/CreateApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appintegrations-2020-07-29/CreateApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appintegrations-2020-07-29/CreateApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appintegrations-2020-07-29/CreateApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appintegrations-2020-07-29/CreateApplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appintegrations-2020-07-29/CreateApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appintegrations-2020-07-29/CreateApplication)
