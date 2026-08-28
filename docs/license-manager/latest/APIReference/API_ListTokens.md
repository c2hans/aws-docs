---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_ListTokens.html
---

# ListTokens
<a name="API_ListTokens"></a>

Lists your tokens.

## Request Syntax
<a name="API_ListTokens_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "TokenIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_ListTokens_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_ListTokens_RequestSyntax) **   <a name="licensemanager-ListTokens-request-Filters"></a>
Filters to scope the results. The following filter is supported:
+  `LicenseArns`
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** [MaxResults](#API_ListTokens_RequestSyntax) **   <a name="licensemanager-ListTokens-request-MaxResults"></a>
Maximum number of results to return in a single call.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListTokens_RequestSyntax) **   <a name="licensemanager-ListTokens-request-NextToken"></a>
Token for the next set of results.
Type: String
Required: No

 ** [TokenIds](#API_ListTokens_RequestSyntax) **   <a name="licensemanager-ListTokens-request-TokenIds"></a>
Token IDs.
Type: Array of strings
Required: No

## Response Syntax
<a name="API_ListTokens_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Tokens": [
      {
         "ExpirationTime": "string",
         "LicenseArn": "string",
         "RoleArns": [ "string" ],
         "Status": "string",
         "TokenId": "string",
         "TokenProperties": [ "string" ],
         "TokenType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListTokens_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListTokens_ResponseSyntax) **   <a name="licensemanager-ListTokens-response-NextToken"></a>
Token for the next set of results.
Type: String

 ** [Tokens](#API_ListTokens_ResponseSyntax) **   <a name="licensemanager-ListTokens-response-Tokens"></a>
Received token details.
Type: Array of [TokenData](API_TokenData.md) objects

## Errors
<a name="API_ListTokens_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to resource denied.
HTTP Status Code: 400

 ** AuthorizationException **
The AWS user account does not have permission to perform the action. Check the IAM policy associated with this account.
HTTP Status Code: 400

 ** RateLimitExceededException **
Too many requests have been submitted. Try again after a brief wait.
HTTP Status Code: 400

 ** ServerInternalException **
The server experienced an internal error. Try again.
HTTP Status Code: 500

 ** ValidationException **
The provided input is not valid. Try your request again.
HTTP Status Code: 400

## See Also
<a name="API_ListTokens_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/license-manager-2018-08-01/ListTokens)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/license-manager-2018-08-01/ListTokens)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/ListTokens)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/license-manager-2018-08-01/ListTokens)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/ListTokens)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/license-manager-2018-08-01/ListTokens)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/license-manager-2018-08-01/ListTokens)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/license-manager-2018-08-01/ListTokens)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/license-manager-2018-08-01/ListTokens)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/ListTokens)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS License Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
