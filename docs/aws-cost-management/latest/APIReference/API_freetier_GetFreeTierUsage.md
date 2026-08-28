---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_freetier_GetFreeTierUsage.html
---

# GetFreeTierUsage
<a name="API_freetier_GetFreeTierUsage"></a>

Returns a list of all Free Tier usage objects that match your filters.

## Request Syntax
<a name="API_freetier_GetFreeTierUsage_RequestSyntax"></a>

```
{
   "filter": {
      "And": [
         "Expression"
      ],
      "Dimensions": {
         "Key": "{{string}}",
         "MatchOptions": [ "{{string}}" ],
         "Values": [ "{{string}}" ]
      },
      "Not": "Expression",
      "Or": [
         "Expression"
      ]
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_freetier_GetFreeTierUsage_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [filter](#API_freetier_GetFreeTierUsage_RequestSyntax) **   <a name="awscostmanagement-freetier_GetFreeTierUsage-request-filter"></a>
An expression that specifies the conditions that you want each `FreeTierUsage` object to meet.
Type: [Expression](API_freetier_Expression.md) object
Required: No

 ** [maxResults](#API_freetier_GetFreeTierUsage_RequestSyntax) **   <a name="awscostmanagement-freetier_GetFreeTierUsage-request-maxResults"></a>
The maximum number of results to return in the response. `MaxResults` means that there can be up to the specified number of values, but there might be fewer results based on your filters.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_freetier_GetFreeTierUsage_RequestSyntax) **   <a name="awscostmanagement-freetier_GetFreeTierUsage-request-nextToken"></a>
The pagination token that indicates the next set of results to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `[\S\s]*`
Required: No

## Response Syntax
<a name="API_freetier_GetFreeTierUsage_ResponseSyntax"></a>

```
{
   "freeTierUsages": [
      {
         "actualUsageAmount": number,
         "description": "string",
         "forecastedUsageAmount": number,
         "freeTierType": "string",
         "limit": number,
         "operation": "string",
         "region": "string",
         "service": "string",
         "unit": "string",
         "usageType": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_freetier_GetFreeTierUsage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [freeTierUsages](#API_freetier_GetFreeTierUsage_ResponseSyntax) **   <a name="awscostmanagement-freetier_GetFreeTierUsage-response-freeTierUsages"></a>
The list of Free Tier usage objects that meet your filter expression.
Type: Array of [FreeTierUsage](API_freetier_FreeTierUsage.md) objects

 ** [nextToken](#API_freetier_GetFreeTierUsage_ResponseSyntax) **   <a name="awscostmanagement-freetier_GetFreeTierUsage-response-nextToken"></a>
The pagination token that indicates the next set of results to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `[\S\s]*`

## Errors
<a name="API_freetier_GetFreeTierUsage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An unexpected error occurred during the processing of your request.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_freetier_GetFreeTierUsage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/freetier-2023-09-07/GetFreeTierUsage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/freetier-2023-09-07/GetFreeTierUsage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/freetier-2023-09-07/GetFreeTierUsage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/freetier-2023-09-07/GetFreeTierUsage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/freetier-2023-09-07/GetFreeTierUsage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/freetier-2023-09-07/GetFreeTierUsage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/freetier-2023-09-07/GetFreeTierUsage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/freetier-2023-09-07/GetFreeTierUsage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/freetier-2023-09-07/GetFreeTierUsage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/freetier-2023-09-07/GetFreeTierUsage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
