---
source_url: https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_GetEventIntegration.html
---

# GetEventIntegration
<a name="API_connect-app-integrations_GetEventIntegration"></a>

Returns information about the event integration.

## Request Syntax
<a name="API_connect-app-integrations_GetEventIntegration_RequestSyntax"></a>

```
GET /eventIntegrations/{{Name}} HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-app-integrations_GetEventIntegration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Name](#API_connect-app-integrations_GetEventIntegration_RequestSyntax) **   <a name="connect-connect-app-integrations_GetEventIntegration-request-uri-Name"></a>
The name of the event integration.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9\/\._\-]+$`
Required: Yes

## Request Body
<a name="API_connect-app-integrations_GetEventIntegration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-app-integrations_GetEventIntegration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Description": "string",
   "EventBridgeBus": "string",
   "EventFilter": {
      "Source": "string"
   },
   "EventIntegrationArn": "string",
   "Name": "string",
   "Tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_connect-app-integrations_GetEventIntegration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Description](#API_connect-app-integrations_GetEventIntegration_ResponseSyntax) **   <a name="connect-connect-app-integrations_GetEventIntegration-response-Description"></a>
The description of the event integration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `.*`

 ** [EventBridgeBus](#API_connect-app-integrations_GetEventIntegration_ResponseSyntax) **   <a name="connect-connect-app-integrations_GetEventIntegration-response-EventBridgeBus"></a>
The EventBridge bus.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9\/\._\-]+$`

 ** [EventFilter](#API_connect-app-integrations_GetEventIntegration_ResponseSyntax) **   <a name="connect-connect-app-integrations_GetEventIntegration-response-EventFilter"></a>
The event filter.
Type: [EventFilter](API_connect-app-integrations_EventFilter.md) object

 ** [EventIntegrationArn](#API_connect-app-integrations_GetEventIntegration_ResponseSyntax) **   <a name="connect-connect-app-integrations_GetEventIntegration-response-EventIntegrationArn"></a>
The Amazon Resource Name (ARN) for the event integration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^arn:aws:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`

 ** [Name](#API_connect-app-integrations_GetEventIntegration_ResponseSyntax) **   <a name="connect-connect-app-integrations_GetEventIntegration-response-Name"></a>
The name of the event integration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9\/\._\-]+$`

 ** [Tags](#API_connect-app-integrations_GetEventIntegration_ResponseSyntax) **   <a name="connect-connect-app-integrations_GetEventIntegration-response-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.

## Errors
<a name="API_connect-app-integrations_GetEventIntegration_Errors"></a>

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
<a name="API_connect-app-integrations_GetEventIntegration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appintegrations-2020-07-29/GetEventIntegration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appintegrations-2020-07-29/GetEventIntegration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appintegrations-2020-07-29/GetEventIntegration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appintegrations-2020-07-29/GetEventIntegration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appintegrations-2020-07-29/GetEventIntegration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appintegrations-2020-07-29/GetEventIntegration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appintegrations-2020-07-29/GetEventIntegration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appintegrations-2020-07-29/GetEventIntegration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/appintegrations-2020-07-29/GetEventIntegration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appintegrations-2020-07-29/GetEventIntegration)
