---
source_url: https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_ListLogPatternSets.html
---

# ListLogPatternSets
<a name="API_ListLogPatternSets"></a>

Lists the log pattern sets in the specific application.

## Request Syntax
<a name="API_ListLogPatternSets_RequestSyntax"></a>

```
{
   "AccountId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ResourceGroupName": "{{string}}"
}
```

## Request Parameters
<a name="API_ListLogPatternSets_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccountId](#API_ListLogPatternSets_RequestSyntax) **   <a name="appinsights-ListLogPatternSets-request-AccountId"></a>
The AWS account ID for the resource group owner.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^\d{12}$`
Required: No

 ** [MaxResults](#API_ListLogPatternSets_RequestSyntax) **   <a name="appinsights-ListLogPatternSets-request-MaxResults"></a>
The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned `NextToken` value.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 40.
Required: No

 ** [NextToken](#API_ListLogPatternSets_RequestSyntax) **   <a name="appinsights-ListLogPatternSets-request-NextToken"></a>
The token to request the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`
Required: No

 ** [ResourceGroupName](#API_ListLogPatternSets_RequestSyntax) **   <a name="appinsights-ListLogPatternSets-request-ResourceGroupName"></a>
The name of the resource group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9\.\-_]*`
Required: Yes

## Response Syntax
<a name="API_ListLogPatternSets_ResponseSyntax"></a>

```
{
   "AccountId": "string",
   "LogPatternSets": [ "string" ],
   "NextToken": "string",
   "ResourceGroupName": "string"
}
```

## Response Elements
<a name="API_ListLogPatternSets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AccountId](#API_ListLogPatternSets_ResponseSyntax) **   <a name="appinsights-ListLogPatternSets-response-AccountId"></a>
The AWS account ID for the resource group owner.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^\d{12}$`

 ** [LogPatternSets](#API_ListLogPatternSets_ResponseSyntax) **   <a name="appinsights-ListLogPatternSets-response-LogPatternSets"></a>
The list of log pattern sets.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 30.
Pattern: `[a-zA-Z0-9\.\-_]*`

 ** [NextToken](#API_ListLogPatternSets_ResponseSyntax) **   <a name="appinsights-ListLogPatternSets-response-NextToken"></a>
The token used to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`

 ** [ResourceGroupName](#API_ListLogPatternSets_ResponseSyntax) **   <a name="appinsights-ListLogPatternSets-response-ResourceGroupName"></a>
The name of the resource group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9\.\-_]*`

## Errors
<a name="API_ListLogPatternSets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The server encountered an internal error and is unable to complete the request.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource does not exist in the customer account.
HTTP Status Code: 400

 ** ValidationException **
The parameter is not valid.
HTTP Status Code: 400

## See Also
<a name="API_ListLogPatternSets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/application-insights-2018-11-25/ListLogPatternSets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/application-insights-2018-11-25/ListLogPatternSets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-insights-2018-11-25/ListLogPatternSets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/application-insights-2018-11-25/ListLogPatternSets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-insights-2018-11-25/ListLogPatternSets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/application-insights-2018-11-25/ListLogPatternSets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/application-insights-2018-11-25/ListLogPatternSets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/application-insights-2018-11-25/ListLogPatternSets)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/application-insights-2018-11-25/ListLogPatternSets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-insights-2018-11-25/ListLogPatternSets)
