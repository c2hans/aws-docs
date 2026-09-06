---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListPluginTypeActions.html
---

# ListPluginTypeActions
<a name="API_ListPluginTypeActions"></a>

**Note**
Amazon Q Business will no longer be open to new customers starting on July 31, 2026. If you would like to use the service, please sign up prior to July 30. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

Lists configured Amazon Q Business actions for any plugin type—both built-in and custom.

## Request Syntax
<a name="API_ListPluginTypeActions_RequestSyntax"></a>

```
GET /pluginTypes/{{pluginType}}/actions?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListPluginTypeActions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListPluginTypeActions_RequestSyntax) **   <a name="qbusiness-ListPluginTypeActions-request-uri-maxResults"></a>
The maximum number of plugins to return.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [nextToken](#API_ListPluginTypeActions_RequestSyntax) **   <a name="qbusiness-ListPluginTypeActions-request-uri-nextToken"></a>
If the number of plugins returned exceeds `maxResults`, Amazon Q Business returns a next token as a pagination token to retrieve the next set of plugins.
Length Constraints: Minimum length of 1. Maximum length of 800.

 ** [pluginType](#API_ListPluginTypeActions_RequestSyntax) **   <a name="qbusiness-ListPluginTypeActions-request-uri-pluginType"></a>
The type of the plugin.
Valid Values: `SERVICE_NOW | SALESFORCE | JIRA | ZENDESK | CUSTOM | QUICKSIGHT | SERVICENOW_NOW_PLATFORM | JIRA_CLOUD | SALESFORCE_CRM | ZENDESK_SUITE | ATLASSIAN_CONFLUENCE | GOOGLE_CALENDAR | MICROSOFT_TEAMS | MICROSOFT_EXCHANGE | PAGERDUTY_ADVANCE | SMARTSHEET | ASANA`
Required: Yes

## Request Body
<a name="API_ListPluginTypeActions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListPluginTypeActions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "actionIdentifier": "string",
         "description": "string",
         "displayName": "string",
         "instructionExample": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListPluginTypeActions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListPluginTypeActions_ResponseSyntax) **   <a name="qbusiness-ListPluginTypeActions-response-items"></a>
An array of information on one or more plugins.
Type: Array of [ActionSummary](API_ActionSummary.md) objects

 ** [nextToken](#API_ListPluginTypeActions_ResponseSyntax) **   <a name="qbusiness-ListPluginTypeActions-response-nextToken"></a>
If the response is truncated, Amazon Q Business returns this token, which you can use in a later request to list the next set of plugins.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 800.

## Errors
<a name="API_ListPluginTypeActions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.
HTTP Status Code: 403

 ** InternalServerException **
An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact [Support](http://aws.amazon.com/contact-us/) for help.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to throttling. Reduce the number of requests and try again.
HTTP Status Code: 429

 ** ValidationException **
The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.
 ** fields **
The input field(s) that failed validation.
 ** message **
The message describing the `ValidationException`.
 ** reason **
The reason for the `ValidationException`.
HTTP Status Code: 400

## See Also
<a name="API_ListPluginTypeActions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qbusiness-2023-11-27/ListPluginTypeActions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qbusiness-2023-11-27/ListPluginTypeActions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/ListPluginTypeActions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qbusiness-2023-11-27/ListPluginTypeActions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/ListPluginTypeActions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qbusiness-2023-11-27/ListPluginTypeActions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qbusiness-2023-11-27/ListPluginTypeActions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qbusiness-2023-11-27/ListPluginTypeActions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qbusiness-2023-11-27/ListPluginTypeActions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/ListPluginTypeActions)
