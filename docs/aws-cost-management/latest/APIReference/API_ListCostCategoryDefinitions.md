---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ListCostCategoryDefinitions.html
---

# ListCostCategoryDefinitions
<a name="API_ListCostCategoryDefinitions"></a>

Returns the name, Amazon Resource Name (ARN), `NumberOfRules` and effective dates of all cost categories defined in the account. You have the option to use `EffectiveOn` and `SupportedResourceTypes` to return a list of cost categories that were active on a specific date. If there is no `EffectiveOn` specified, you’ll see cost categories that are effective on the current date. If cost category is still effective, `EffectiveEnd` is omitted in the response. `ListCostCategoryDefinitions` supports pagination. The request can have a `MaxResults` range up to 100.

## Request Syntax
<a name="API_ListCostCategoryDefinitions_RequestSyntax"></a>

```
{
   "EffectiveOn": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SupportedResourceTypes": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_ListCostCategoryDefinitions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EffectiveOn](#API_ListCostCategoryDefinitions_RequestSyntax) **   <a name="awscostmanagement-ListCostCategoryDefinitions-request-EffectiveOn"></a>
The date when the cost category was effective.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(([+-]\d\d:\d\d)|Z)$`
Required: No

 ** [MaxResults](#API_ListCostCategoryDefinitions_RequestSyntax) **   <a name="awscostmanagement-ListCostCategoryDefinitions-request-MaxResults"></a>
The number of entries a paginated response contains.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListCostCategoryDefinitions_RequestSyntax) **   <a name="awscostmanagement-ListCostCategoryDefinitions-request-NextToken"></a>
The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[\S\s]*`
Required: No

 ** [SupportedResourceTypes](#API_ListCostCategoryDefinitions_RequestSyntax) **   <a name="awscostmanagement-ListCostCategoryDefinitions-request-SupportedResourceTypes"></a>
 Filter cost category definitions that are supported by given resource types based on the latest version. If the filter is present, the result only includes Cost Categories that supports input resource type. If the filter isn't provided, no filtering is applied. The valid values are `billing:rispgroupsharing` and `billing:billingview`.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Pattern: `^[-a-zA-Z0-9/_]+:[-a-zA-Z0-9/_]+`
Required: No

## Response Syntax
<a name="API_ListCostCategoryDefinitions_ResponseSyntax"></a>

```
{
   "CostCategoryReferences": [
      {
         "CostCategoryArn": "string",
         "DefaultValue": "string",
         "EffectiveEnd": "string",
         "EffectiveStart": "string",
         "Name": "string",
         "NumberOfRules": number,
         "ProcessingStatus": [
            {
               "Component": "string",
               "Status": "string"
            }
         ],
         "SupportedResourceTypes": [ "string" ],
         "Values": [ "string" ]
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListCostCategoryDefinitions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CostCategoryReferences](#API_ListCostCategoryDefinitions_ResponseSyntax) **   <a name="awscostmanagement-ListCostCategoryDefinitions-response-CostCategoryReferences"></a>
A reference to a cost category that contains enough information to identify the Cost Category.
Type: Array of [CostCategoryReference](API_CostCategoryReference.md) objects

 ** [NextToken](#API_ListCostCategoryDefinitions_ResponseSyntax) **   <a name="awscostmanagement-ListCostCategoryDefinitions-response-NextToken"></a>
The token to retrieve the next set of results. AWS provides the token when the response from a previous call has more results than the maximum page size.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[\S\s]*`

## Errors
<a name="API_ListCostCategoryDefinitions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** LimitExceededException **
You made too many calls in a short period of time. Try again later.
HTTP Status Code: 400

## See Also
<a name="API_ListCostCategoryDefinitions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ce-2017-10-25/ListCostCategoryDefinitions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ce-2017-10-25/ListCostCategoryDefinitions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/ListCostCategoryDefinitions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ce-2017-10-25/ListCostCategoryDefinitions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/ListCostCategoryDefinitions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ce-2017-10-25/ListCostCategoryDefinitions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ce-2017-10-25/ListCostCategoryDefinitions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ce-2017-10-25/ListCostCategoryDefinitions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ce-2017-10-25/ListCostCategoryDefinitions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/ListCostCategoryDefinitions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
