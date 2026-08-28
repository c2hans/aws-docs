---
source_url: https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_UpdateApplication.html
---

# UpdateApplication
<a name="API_connect-app-integrations_UpdateApplication"></a>

Updates and persists an Application resource.

## Request Syntax
<a name="API_connect-app-integrations_UpdateApplication_RequestSyntax"></a>

```
PATCH /applications/{{ApplicationIdentifier}} HTTP/1.1
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
   "Description": "{{string}}",
   "IframeConfig": {
      "Allow": [ "{{string}}" ],
      "Sandbox": [ "{{string}}" ]
   },
   "InitializationTimeout": {{number}},
   "IsService": {{boolean}},
   "Name": "{{string}}",
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
   ]
}
```

## URI Request Parameters
<a name="API_connect-app-integrations_UpdateApplication_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ApplicationIdentifier](#API_connect-app-integrations_UpdateApplication_RequestSyntax) **   <a name="connect-connect-app-integrations_UpdateApplication-request-uri-Arn"></a>
The Amazon Resource Name (ARN) of the Application.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^(arn:aws:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}|[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})(:[\w\$]+)?$`
Required: Yes

## Request Body
<a name="API_connect-app-integrations_UpdateApplication_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ApplicationConfig](#API_connect-app-integrations_UpdateApplication_RequestSyntax) **   <a name="connect-connect-app-integrations_UpdateApplication-request-ApplicationConfig"></a>
The configuration settings for the application.
Type: [ApplicationConfig](API_connect-app-integrations_ApplicationConfig.md) object
Required: No

 ** [ApplicationSourceConfig](#API_connect-app-integrations_UpdateApplication_RequestSyntax) **   <a name="connect-connect-app-integrations_UpdateApplication-request-ApplicationSourceConfig"></a>
The configuration for where the application should be loaded from.
Type: [ApplicationSourceConfig](API_connect-app-integrations_ApplicationSourceConfig.md) object
Required: No

 ** [ApplicationType](#API_connect-app-integrations_UpdateApplication_RequestSyntax) **   <a name="connect-connect-app-integrations_UpdateApplication-request-ApplicationType"></a>
The type of application.
Type: String
Valid Values: `STANDARD | SERVICE | MCP_SERVER`
Required: No

 ** [Description](#API_connect-app-integrations_UpdateApplication_RequestSyntax) **   <a name="connect-connect-app-integrations_UpdateApplication-request-Description"></a>
The description of the application.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `.*`
Required: No

 ** [IframeConfig](#API_connect-app-integrations_UpdateApplication_RequestSyntax) **   <a name="connect-connect-app-integrations_UpdateApplication-request-IframeConfig"></a>
The iframe configuration for the application.
Type: [IframeConfig](API_connect-app-integrations_IframeConfig.md) object
Required: No

 ** [InitializationTimeout](#API_connect-app-integrations_UpdateApplication_RequestSyntax) **   <a name="connect-connect-app-integrations_UpdateApplication-request-InitializationTimeout"></a>
The maximum time in milliseconds allowed to establish a connection with the workspace.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 600000.
Required: No

 ** [IsService](#API_connect-app-integrations_UpdateApplication_RequestSyntax) **   <a name="connect-connect-app-integrations_UpdateApplication-request-IsService"></a>
 *This parameter has been deprecated.*
Indicates whether the application is a service.
Type: Boolean
Required: No

 ** [Name](#API_connect-app-integrations_UpdateApplication_RequestSyntax) **   <a name="connect-connect-app-integrations_UpdateApplication-request-Name"></a>
The name of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9\/\._ \-]+$`
Required: No

 ** [Permissions](#API_connect-app-integrations_UpdateApplication_RequestSyntax) **   <a name="connect-connect-app-integrations_UpdateApplication-request-Permissions"></a>
The configuration of events or requests that the application has access to.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 150 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9\/\._\-\*]+$`
Required: No

 ** [Publications](#API_connect-app-integrations_UpdateApplication_RequestSyntax) **   <a name="connect-connect-app-integrations_UpdateApplication-request-Publications"></a>
 *This parameter has been deprecated.*
The events that the application publishes.
Type: Array of [Publication](API_connect-app-integrations_Publication.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [Subscriptions](#API_connect-app-integrations_UpdateApplication_RequestSyntax) **   <a name="connect-connect-app-integrations_UpdateApplication-request-Subscriptions"></a>
 *This parameter has been deprecated.*
The events that the application subscribes.
Type: Array of [Subscription](API_connect-app-integrations_Subscription.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_connect-app-integrations_UpdateApplication_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_connect-app-integrations_UpdateApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_connect-app-integrations_UpdateApplication_Errors"></a>

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

 ** UnsupportedOperationException **
The operation is not supported.
HTTP Status Code: 400

## See Also
<a name="API_connect-app-integrations_UpdateApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appintegrations-2020-07-29/UpdateApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appintegrations-2020-07-29/UpdateApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appintegrations-2020-07-29/UpdateApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appintegrations-2020-07-29/UpdateApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appintegrations-2020-07-29/UpdateApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appintegrations-2020-07-29/UpdateApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appintegrations-2020-07-29/UpdateApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appintegrations-2020-07-29/UpdateApplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appintegrations-2020-07-29/UpdateApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appintegrations-2020-07-29/UpdateApplication)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
