---
source_url: https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_CreateLogPattern.html
---

# CreateLogPattern
<a name="API_CreateLogPattern"></a>

Adds an log pattern to a `LogPatternSet`.

## Request Syntax
<a name="API_CreateLogPattern_RequestSyntax"></a>

```
{
   "Pattern": "{{string}}",
   "PatternName": "{{string}}",
   "PatternSetName": "{{string}}",
   "Rank": {{number}},
   "ResourceGroupName": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateLogPattern_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Pattern](#API_CreateLogPattern_RequestSyntax) **   <a name="appinsights-CreateLogPattern-request-Pattern"></a>
The log pattern. The pattern must be DFA compatible. Patterns that utilize forward lookahead or backreference constructions are not supported.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[\S\s]+`
Required: Yes

 ** [PatternName](#API_CreateLogPattern_RequestSyntax) **   <a name="appinsights-CreateLogPattern-request-PatternName"></a>
The name of the log pattern.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[a-zA-Z0-9\.\-_]*`
Required: Yes

 ** [PatternSetName](#API_CreateLogPattern_RequestSyntax) **   <a name="appinsights-CreateLogPattern-request-PatternSetName"></a>
The name of the log pattern set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 30.
Pattern: `[a-zA-Z0-9\.\-_]*`
Required: Yes

 ** [Rank](#API_CreateLogPattern_RequestSyntax) **   <a name="appinsights-CreateLogPattern-request-Rank"></a>
Rank of the log pattern. Must be a value between `1` and `1,000,000`. The patterns are sorted by rank, so we recommend that you set your highest priority patterns with the lowest rank. A pattern of rank `1` will be the first to get matched to a log line. A pattern of rank `1,000,000` will be last to get matched. When you configure custom log patterns from the console, a `Low` severity pattern translates to a `750,000` rank. A `Medium` severity pattern translates to a `500,000` rank. And a `High` severity pattern translates to a `250,000` rank. Rank values less than `1` or greater than `1,000,000` are reserved for AWS provided patterns.
Type: Integer
Required: Yes

 ** [ResourceGroupName](#API_CreateLogPattern_RequestSyntax) **   <a name="appinsights-CreateLogPattern-request-ResourceGroupName"></a>
The name of the resource group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9\.\-_]*`
Required: Yes

## Response Syntax
<a name="API_CreateLogPattern_ResponseSyntax"></a>

```
{
   "LogPattern": {
      "Pattern": "string",
      "PatternName": "string",
      "PatternSetName": "string",
      "Rank": number
   },
   "ResourceGroupName": "string"
}
```

## Response Elements
<a name="API_CreateLogPattern_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LogPattern](#API_CreateLogPattern_ResponseSyntax) **   <a name="appinsights-CreateLogPattern-response-LogPattern"></a>
The successfully created log pattern.
Type: [LogPattern](API_LogPattern.md) object

 ** [ResourceGroupName](#API_CreateLogPattern_ResponseSyntax) **   <a name="appinsights-CreateLogPattern-response-ResourceGroupName"></a>
The name of the resource group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9\.\-_]*`

## Errors
<a name="API_CreateLogPattern_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The server encountered an internal error and is unable to complete the request.
HTTP Status Code: 400

 ** ResourceInUseException **
The resource is already created or in use.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource does not exist in the customer account.
HTTP Status Code: 400

 ** ValidationException **
The parameter is not valid.
HTTP Status Code: 400

## See Also
<a name="API_CreateLogPattern_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/application-insights-2018-11-25/CreateLogPattern)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/application-insights-2018-11-25/CreateLogPattern)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-insights-2018-11-25/CreateLogPattern)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/application-insights-2018-11-25/CreateLogPattern)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-insights-2018-11-25/CreateLogPattern)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/application-insights-2018-11-25/CreateLogPattern)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/application-insights-2018-11-25/CreateLogPattern)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/application-insights-2018-11-25/CreateLogPattern)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/application-insights-2018-11-25/CreateLogPattern)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-insights-2018-11-25/CreateLogPattern)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Application Insights. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudwatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
