---
source_url: https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_CreateEventIntegration.html
---

# CreateEventIntegration
<a name="API_connect-app-integrations_CreateEventIntegration"></a>

Creates an EventIntegration, given a specified name, description, and a reference to an Amazon EventBridge bus in your account and a partner event source that pushes events to that bus. No objects are created in the your account, only metadata that is persisted on the EventIntegration control plane.

## Request Syntax
<a name="API_connect-app-integrations_CreateEventIntegration_RequestSyntax"></a>

```
POST /eventIntegrations HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "Description": "{{string}}",
   "EventBridgeBus": "{{string}}",
   "EventFilter": {
      "Source": "{{string}}"
   },
   "Name": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_connect-app-integrations_CreateEventIntegration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_connect-app-integrations_CreateEventIntegration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_connect-app-integrations_CreateEventIntegration_RequestSyntax) **   <a name="connect-connect-app-integrations_CreateEventIntegration-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `.*`
Required: No

 ** [Description](#API_connect-app-integrations_CreateEventIntegration_RequestSyntax) **   <a name="connect-connect-app-integrations_CreateEventIntegration-request-Description"></a>
The description of the event integration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `.*`
Required: No

 ** [EventBridgeBus](#API_connect-app-integrations_CreateEventIntegration_RequestSyntax) **   <a name="connect-connect-app-integrations_CreateEventIntegration-request-EventBridgeBus"></a>
The EventBridge bus.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9\/\._\-]+$`
Required: Yes

 ** [EventFilter](#API_connect-app-integrations_CreateEventIntegration_RequestSyntax) **   <a name="connect-connect-app-integrations_CreateEventIntegration-request-EventFilter"></a>
The event filter.
Type: [EventFilter](API_connect-app-integrations_EventFilter.md) object
Required: Yes

 ** [Name](#API_connect-app-integrations_CreateEventIntegration_RequestSyntax) **   <a name="connect-connect-app-integrations_CreateEventIntegration-request-Name"></a>
The name of the event integration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9\/\._\-]+$`
Required: Yes

 ** [Tags](#API_connect-app-integrations_CreateEventIntegration_RequestSyntax) **   <a name="connect-connect-app-integrations_CreateEventIntegration-request-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_connect-app-integrations_CreateEventIntegration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "EventIntegrationArn": "string"
}
```

## Response Elements
<a name="API_connect-app-integrations_CreateEventIntegration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EventIntegrationArn](#API_connect-app-integrations_CreateEventIntegration_ResponseSyntax) **   <a name="connect-connect-app-integrations_CreateEventIntegration-response-EventIntegrationArn"></a>
The Amazon Resource Name (ARN) of the event integration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^arn:aws:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`

## Errors
<a name="API_connect-app-integrations_CreateEventIntegration_Errors"></a>

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

## See Also
<a name="API_connect-app-integrations_CreateEventIntegration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appintegrations-2020-07-29/CreateEventIntegration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appintegrations-2020-07-29/CreateEventIntegration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appintegrations-2020-07-29/CreateEventIntegration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appintegrations-2020-07-29/CreateEventIntegration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appintegrations-2020-07-29/CreateEventIntegration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appintegrations-2020-07-29/CreateEventIntegration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appintegrations-2020-07-29/CreateEventIntegration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appintegrations-2020-07-29/CreateEventIntegration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appintegrations-2020-07-29/CreateEventIntegration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appintegrations-2020-07-29/CreateEventIntegration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
