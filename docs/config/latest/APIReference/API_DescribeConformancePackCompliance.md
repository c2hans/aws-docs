---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConformancePackCompliance.html
---

# DescribeConformancePackCompliance
<a name="API_DescribeConformancePackCompliance"></a>

Returns compliance details for each rule in that conformance pack.

**Note**
You must provide exact rule names.

## Request Syntax
<a name="API_DescribeConformancePackCompliance_RequestSyntax"></a>

```
{
   "ConformancePackName": "{{string}}",
   "Filters": {
      "ComplianceType": "{{string}}",
      "ConfigRuleNames": [ "{{string}}" ]
   },
   "Limit": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeConformancePackCompliance_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConformancePackName](#API_DescribeConformancePackCompliance_RequestSyntax) **   <a name="config-DescribeConformancePackCompliance-request-ConformancePackName"></a>
Name of the conformance pack.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z][-a-zA-Z0-9]*`
Required: Yes

 ** [Filters](#API_DescribeConformancePackCompliance_RequestSyntax) **   <a name="config-DescribeConformancePackCompliance-request-Filters"></a>
A `ConformancePackComplianceFilters` object.
Type: [ConformancePackComplianceFilters](API_ConformancePackComplianceFilters.md) object
Required: No

 ** [Limit](#API_DescribeConformancePackCompliance_RequestSyntax) **   <a name="config-DescribeConformancePackCompliance-request-Limit"></a>
The maximum number of AWS Config rules within a conformance pack are returned on each page.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000.
Required: No

 ** [NextToken](#API_DescribeConformancePackCompliance_RequestSyntax) **   <a name="config-DescribeConformancePackCompliance-request-NextToken"></a>
The `nextToken` string returned in a previous request that you use to request the next page of results in a paginated response.
Type: String
Required: No

## Response Syntax
<a name="API_DescribeConformancePackCompliance_ResponseSyntax"></a>

```
{
   "ConformancePackName": "string",
   "ConformancePackRuleComplianceList": [
      {
         "ComplianceType": "string",
         "ConfigRuleName": "string",
         "Controls": [ "string" ]
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeConformancePackCompliance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConformancePackName](#API_DescribeConformancePackCompliance_ResponseSyntax) **   <a name="config-DescribeConformancePackCompliance-response-ConformancePackName"></a>
Name of the conformance pack.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z][-a-zA-Z0-9]*`

 ** [ConformancePackRuleComplianceList](#API_DescribeConformancePackCompliance_ResponseSyntax) **   <a name="config-DescribeConformancePackCompliance-response-ConformancePackRuleComplianceList"></a>
Returns a list of `ConformancePackRuleCompliance` objects.
Type: Array of [ConformancePackRuleCompliance](API_ConformancePackRuleCompliance.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1000 items.

 ** [NextToken](#API_DescribeConformancePackCompliance_ResponseSyntax) **   <a name="config-DescribeConformancePackCompliance-response-NextToken"></a>
The `nextToken` string returned in a previous request that you use to request the next page of results in a paginated response.
Type: String

## Errors
<a name="API_DescribeConformancePackCompliance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidLimitException **
The specified limit is outside the allowable range.
HTTP Status Code: 400

 ** InvalidNextTokenException **
The specified next token is not valid. Specify the `nextToken` string that was returned in the previous response to get the next page of results.
HTTP Status Code: 400

 ** InvalidParameterValueException **
One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.
HTTP Status Code: 400

 ** NoSuchConfigRuleInConformancePackException **
 AWS Config rule that you passed in the filter does not exist.
HTTP Status Code: 400

 ** NoSuchConformancePackException **
You specified one or more conformance packs that do not exist.
HTTP Status Code: 400

## See Also
<a name="API_DescribeConformancePackCompliance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/DescribeConformancePackCompliance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/DescribeConformancePackCompliance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/DescribeConformancePackCompliance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/DescribeConformancePackCompliance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/DescribeConformancePackCompliance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/DescribeConformancePackCompliance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/DescribeConformancePackCompliance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/DescribeConformancePackCompliance)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/DescribeConformancePackCompliance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/DescribeConformancePackCompliance)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
