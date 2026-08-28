---
source_url: https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_GetApplication.html
---

# GetApplication
<a name="API_connect-app-integrations_GetApplication"></a>

Get an Application resource.

## Request Syntax
<a name="API_connect-app-integrations_GetApplication_RequestSyntax"></a>

```
GET /applications/{{ApplicationIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-app-integrations_GetApplication_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ApplicationIdentifier](#API_connect-app-integrations_GetApplication_RequestSyntax) **   <a name="connect-connect-app-integrations_GetApplication-request-uri-Arn"></a>
The Amazon Resource Name (ARN) of the Application.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^(arn:aws:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}|[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})(:[\w\$]+)?$`
Required: Yes

## Request Body
<a name="API_connect-app-integrations_GetApplication_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-app-integrations_GetApplication_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ApplicationConfig": {
      "ContactHandling": {
         "Scope": "string"
      }
   },
   "ApplicationSourceConfig": {
      "ExternalUrlConfig": {
         "AccessUrl": "string",
         "ApprovedOrigins": [ "string" ]
      }
   },
   "ApplicationType": "string",
   "Arn": "string",
   "CreatedTime": number,
   "Description": "string",
   "Id": "string",
   "IframeConfig": {
      "Allow": [ "string" ],
      "Sandbox": [ "string" ]
   },
   "InitializationTimeout": number,
   "IsService": boolean,
   "LastModifiedTime": number,
   "Name": "string",
   "Namespace": "string",
   "Permissions": [ "string" ],
   "Publications": [
      {
         "Description": "string",
         "Event": "string",
         "Schema": "string"
      }
   ],
   "Subscriptions": [
      {
         "Description": "string",
         "Event": "string"
      }
   ],
   "Tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_connect-app-integrations_GetApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationConfig](#API_connect-app-integrations_GetApplication_ResponseSyntax) **   <a name="connect-connect-app-integrations_GetApplication-response-ApplicationConfig"></a>
The configuration settings for the application.
Type: [ApplicationConfig](API_connect-app-integrations_ApplicationConfig.md) object

 ** [ApplicationSourceConfig](#API_connect-app-integrations_GetApplication_ResponseSyntax) **   <a name="connect-connect-app-integrations_GetApplication-response-ApplicationSourceConfig"></a>
The configuration for where the application should be loaded from.
Type: [ApplicationSourceConfig](API_connect-app-integrations_ApplicationSourceConfig.md) object

 ** [ApplicationType](#API_connect-app-integrations_GetApplication_ResponseSyntax) **   <a name="connect-connect-app-integrations_GetApplication-response-ApplicationType"></a>
The type of application.
Type: String
Valid Values: `STANDARD | SERVICE | MCP_SERVER`

 ** [Arn](#API_connect-app-integrations_GetApplication_ResponseSyntax) **   <a name="connect-connect-app-integrations_GetApplication-response-Arn"></a>
The Amazon Resource Name (ARN) of the Application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^arn:aws:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`

 ** [CreatedTime](#API_connect-app-integrations_GetApplication_ResponseSyntax) **   <a name="connect-connect-app-integrations_GetApplication-response-CreatedTime"></a>
The created time of the Application.
Type: Timestamp

 ** [Description](#API_connect-app-integrations_GetApplication_ResponseSyntax) **   <a name="connect-connect-app-integrations_GetApplication-response-Description"></a>
The description of the application.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `.*`

 ** [Id](#API_connect-app-integrations_GetApplication_ResponseSyntax) **   <a name="connect-connect-app-integrations_GetApplication-response-Id"></a>
A unique identifier for the Application.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [IframeConfig](#API_connect-app-integrations_GetApplication_ResponseSyntax) **   <a name="connect-connect-app-integrations_GetApplication-response-IframeConfig"></a>
The iframe configuration for the application.
Type: [IframeConfig](API_connect-app-integrations_IframeConfig.md) object

 ** [InitializationTimeout](#API_connect-app-integrations_GetApplication_ResponseSyntax) **   <a name="connect-connect-app-integrations_GetApplication-response-InitializationTimeout"></a>
The maximum time in milliseconds allowed to establish a connection with the workspace.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 600000.

 ** [IsService](#API_connect-app-integrations_GetApplication_ResponseSyntax) **   <a name="connect-connect-app-integrations_GetApplication-response-IsService"></a>
 *This parameter has been deprecated.*
Indicates whether the application is a service.
Type: Boolean

 ** [LastModifiedTime](#API_connect-app-integrations_GetApplication_ResponseSyntax) **   <a name="connect-connect-app-integrations_GetApplication-response-LastModifiedTime"></a>
The last modified time of the Application.
Type: Timestamp

 ** [Name](#API_connect-app-integrations_GetApplication_ResponseSyntax) **   <a name="connect-connect-app-integrations_GetApplication-response-Name"></a>
The name of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9\/\._ \-]+$`

 ** [Namespace](#API_connect-app-integrations_GetApplication_ResponseSyntax) **   <a name="connect-connect-app-integrations_GetApplication-response-Namespace"></a>
The namespace of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 211.
Pattern: `^[a-zA-Z0-9\/\._\-]+$`

 ** [Permissions](#API_connect-app-integrations_GetApplication_ResponseSyntax) **   <a name="connect-connect-app-integrations_GetApplication-response-Permissions"></a>
The configuration of events or requests that the application has access to.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 150 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9\/\._\-\*]+$`

 ** [Publications](#API_connect-app-integrations_GetApplication_ResponseSyntax) **   <a name="connect-connect-app-integrations_GetApplication-response-Publications"></a>
 *This parameter has been deprecated.*
The events that the application publishes.
Type: Array of [Publication](API_connect-app-integrations_Publication.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.

 ** [Subscriptions](#API_connect-app-integrations_GetApplication_ResponseSyntax) **   <a name="connect-connect-app-integrations_GetApplication-response-Subscriptions"></a>
 *This parameter has been deprecated.*
The events that the application subscribes.
Type: Array of [Subscription](API_connect-app-integrations_Subscription.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.

 ** [Tags](#API_connect-app-integrations_GetApplication_ResponseSyntax) **   <a name="connect-connect-app-integrations_GetApplication-response-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.

## Errors
<a name="API_connect-app-integrations_GetApplication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServiceError **
Request processing failed due to an error or failure with the service.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_connect-app-integrations_GetApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appintegrations-2020-07-29/GetApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appintegrations-2020-07-29/GetApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appintegrations-2020-07-29/GetApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appintegrations-2020-07-29/GetApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appintegrations-2020-07-29/GetApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appintegrations-2020-07-29/GetApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appintegrations-2020-07-29/GetApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appintegrations-2020-07-29/GetApplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appintegrations-2020-07-29/GetApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appintegrations-2020-07-29/GetApplication)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
