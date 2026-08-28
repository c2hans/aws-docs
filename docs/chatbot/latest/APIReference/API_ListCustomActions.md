---
source_url: https://docs.aws.amazon.com/chatbot/latest/APIReference/API_ListCustomActions.html
---

# ListCustomActions
<a name="API_ListCustomActions"></a>

Lists custom actions defined in this account.

## Request Syntax
<a name="API_ListCustomActions_RequestSyntax"></a>

```
POST /list-custom-actions HTTP/1.1
Content-type: application/json

{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListCustomActions_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListCustomActions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListCustomActions_RequestSyntax) **   <a name="qdevinchatapps-ListCustomActions-request-MaxResults"></a>
The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListCustomActions_RequestSyntax) **   <a name="qdevinchatapps-ListCustomActions-request-NextToken"></a>
An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\x20-\x7F]+`
Required: No

## Response Syntax
<a name="API_ListCustomActions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CustomActions": [ "string" ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListCustomActions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CustomActions](#API_ListCustomActions_ResponseSyntax) **   <a name="qdevinchatapps-ListCustomActions-response-CustomActions"></a>
A list of custom actions.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws:chatbot::[0-9]{12}:custom-action/[a-zA-Z0-9_-]{1,64}`

 ** [NextToken](#API_ListCustomActions_ResponseSyntax) **   <a name="qdevinchatapps-ListCustomActions-response-NextToken"></a>
An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\x20-\x7F]+`

## Errors
<a name="API_ListCustomActions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceError **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** InvalidRequestException **
Your request input doesn't meet the constraints required by Amazon Q Developer.
HTTP Status Code: 400

 ** UnauthorizedException **
The request was rejected because it doesn't have valid credentials for the target resource.
HTTP Status Code: 403

## See Also
<a name="API_ListCustomActions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chatbot-2017-10-11/ListCustomActions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chatbot-2017-10-11/ListCustomActions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chatbot-2017-10-11/ListCustomActions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chatbot-2017-10-11/ListCustomActions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chatbot-2017-10-11/ListCustomActions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chatbot-2017-10-11/ListCustomActions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chatbot-2017-10-11/ListCustomActions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chatbot-2017-10-11/ListCustomActions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chatbot-2017-10-11/ListCustomActions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chatbot-2017-10-11/ListCustomActions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Developer in chat applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chatbot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
