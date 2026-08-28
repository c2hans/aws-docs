---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-app-integrations_UpdateEventIntegration.html
---

# UpdateEventIntegration
<a name="API_connect-app-integrations_UpdateEventIntegration"></a>

Updates the description of an event integration.

## Request Syntax
<a name="API_connect-app-integrations_UpdateEventIntegration_RequestSyntax"></a>

```
PATCH /eventIntegrations/{{Name}} HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}"
}
```

## URI Request Parameters
<a name="API_connect-app-integrations_UpdateEventIntegration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Name](#API_connect-app-integrations_UpdateEventIntegration_RequestSyntax) **   <a name="connect-connect-app-integrations_UpdateEventIntegration-request-uri-Name"></a>
The name of the event integration.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9\/\._\-]+$`
Required: Yes

## Request Body
<a name="API_connect-app-integrations_UpdateEventIntegration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_connect-app-integrations_UpdateEventIntegration_RequestSyntax) **   <a name="connect-connect-app-integrations_UpdateEventIntegration-request-Description"></a>
The description of the event integration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `.*`
Required: No

## Response Syntax
<a name="API_connect-app-integrations_UpdateEventIntegration_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_connect-app-integrations_UpdateEventIntegration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_connect-app-integrations_UpdateEventIntegration_Errors"></a>

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
<a name="API_connect-app-integrations_UpdateEventIntegration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appintegrations-2020-07-29/UpdateEventIntegration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appintegrations-2020-07-29/UpdateEventIntegration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appintegrations-2020-07-29/UpdateEventIntegration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appintegrations-2020-07-29/UpdateEventIntegration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appintegrations-2020-07-29/UpdateEventIntegration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appintegrations-2020-07-29/UpdateEventIntegration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appintegrations-2020-07-29/UpdateEventIntegration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appintegrations-2020-07-29/UpdateEventIntegration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appintegrations-2020-07-29/UpdateEventIntegration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appintegrations-2020-07-29/UpdateEventIntegration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
