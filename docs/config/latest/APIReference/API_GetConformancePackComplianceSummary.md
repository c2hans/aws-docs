---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_GetConformancePackComplianceSummary.html
---

# GetConformancePackComplianceSummary
<a name="API_GetConformancePackComplianceSummary"></a>

Returns compliance details for the conformance pack based on the cumulative compliance results of all the rules in that conformance pack.

## Request Syntax
<a name="API_GetConformancePackComplianceSummary_RequestSyntax"></a>

```
{
   "ConformancePackNames": [ "{{string}}" ],
   "Limit": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_GetConformancePackComplianceSummary_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConformancePackNames](#API_GetConformancePackComplianceSummary_RequestSyntax) **   <a name="config-GetConformancePackComplianceSummary-request-ConformancePackNames"></a>
Names of conformance packs.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z][-a-zA-Z0-9]*`
Required: Yes

 ** [Limit](#API_GetConformancePackComplianceSummary_RequestSyntax) **   <a name="config-GetConformancePackComplianceSummary-request-Limit"></a>
The maximum number of conformance packs returned on each page.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 20.
Required: No

 ** [NextToken](#API_GetConformancePackComplianceSummary_RequestSyntax) **   <a name="config-GetConformancePackComplianceSummary-request-NextToken"></a>
The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.
Type: String
Required: No

## Response Syntax
<a name="API_GetConformancePackComplianceSummary_ResponseSyntax"></a>

```
{
   "ConformancePackComplianceSummaryList": [
      {
         "ConformancePackComplianceStatus": "string",
         "ConformancePackName": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_GetConformancePackComplianceSummary_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConformancePackComplianceSummaryList](#API_GetConformancePackComplianceSummary_ResponseSyntax) **   <a name="config-GetConformancePackComplianceSummary-response-ConformancePackComplianceSummaryList"></a>
A list of `ConformancePackComplianceSummary` objects.
Type: Array of [ConformancePackComplianceSummary](API_ConformancePackComplianceSummary.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.

 ** [NextToken](#API_GetConformancePackComplianceSummary_ResponseSyntax) **   <a name="config-GetConformancePackComplianceSummary-response-NextToken"></a>
The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.
Type: String

## Errors
<a name="API_GetConformancePackComplianceSummary_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidLimitException **
The specified limit is outside the allowable range.
HTTP Status Code: 400

 ** InvalidNextTokenException **
The specified next token is not valid. Specify the `nextToken` string that was returned in the previous response to get the next page of results.
HTTP Status Code: 400

 ** NoSuchConformancePackException **
You specified one or more conformance packs that do not exist.
HTTP Status Code: 400

## See Also
<a name="API_GetConformancePackComplianceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/GetConformancePackComplianceSummary)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/GetConformancePackComplianceSummary)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/GetConformancePackComplianceSummary)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/GetConformancePackComplianceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/GetConformancePackComplianceSummary)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/GetConformancePackComplianceSummary)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/GetConformancePackComplianceSummary)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/GetConformancePackComplianceSummary)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/GetConformancePackComplianceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/GetConformancePackComplianceSummary)
