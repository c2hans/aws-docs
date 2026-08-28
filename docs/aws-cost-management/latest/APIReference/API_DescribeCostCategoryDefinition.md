---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DescribeCostCategoryDefinition.html
---

# DescribeCostCategoryDefinition
<a name="API_DescribeCostCategoryDefinition"></a>

Returns the name, Amazon Resource Name (ARN), rules, definition, and effective dates of a cost category that's defined in the account.

You have the option to use `EffectiveOn` to return a cost category that's active on a specific date. If there's no `EffectiveOn` specified, you see a Cost Category that's effective on the current date. If cost category is still effective, `EffectiveEnd` is omitted in the response.

## Request Syntax
<a name="API_DescribeCostCategoryDefinition_RequestSyntax"></a>

```
{
   "CostCategoryArn": "{{string}}",
   "EffectiveOn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeCostCategoryDefinition_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CostCategoryArn](#API_DescribeCostCategoryDefinition_RequestSyntax) **   <a name="awscostmanagement-DescribeCostCategoryDefinition-request-CostCategoryArn"></a>
The unique identifier for your cost category.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:[-a-zA-Z0-9/:_]+`
Required: Yes

 ** [EffectiveOn](#API_DescribeCostCategoryDefinition_RequestSyntax) **   <a name="awscostmanagement-DescribeCostCategoryDefinition-request-EffectiveOn"></a>
The date when the cost category was effective.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(([+-]\d\d:\d\d)|Z)$`
Required: No

## Response Syntax
<a name="API_DescribeCostCategoryDefinition_ResponseSyntax"></a>

```
{
   "CostCategory": {
      "CostCategoryArn": "string",
      "DefaultValue": "string",
      "EffectiveEnd": "string",
      "EffectiveStart": "string",
      "Name": "string",
      "ProcessingStatus": [
         {
            "Component": "string",
            "Status": "string"
         }
      ],
      "Rules": [
         {
            "InheritedValue": {
               "DimensionKey": "string",
               "DimensionName": "string"
            },
            "Rule": {
               "And": [
                  "Expression"
               ],
               "CostCategories": {
                  "Key": "string",
                  "MatchOptions": [ "string" ],
                  "Values": [ "string" ]
               },
               "Dimensions": {
                  "Key": "string",
                  "MatchOptions": [ "string" ],
                  "Values": [ "string" ]
               },
               "Not": "Expression",
               "Or": [
                  "Expression"
               ],
               "Tags": {
                  "Key": "string",
                  "MatchOptions": [ "string" ],
                  "Values": [ "string" ]
               }
            },
            "Type": "string",
            "Value": "string"
         }
      ],
      "RuleVersion": "string",
      "SplitChargeRules": [
         {
            "Method": "string",
            "Parameters": [
               {
                  "Type": "string",
                  "Values": [ "string" ]
               }
            ],
            "Source": "string",
            "Targets": [ "string" ]
         }
      ]
   }
}
```

## Response Elements
<a name="API_DescribeCostCategoryDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CostCategory](#API_DescribeCostCategoryDefinition_ResponseSyntax) **   <a name="awscostmanagement-DescribeCostCategoryDefinition-response-CostCategory"></a>
The structure of Cost Categories. This includes detailed metadata and the set of rules for the `CostCategory` object.
Type: [CostCategory](API_CostCategory.md) object

## Errors
<a name="API_DescribeCostCategoryDefinition_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** LimitExceededException **
You made too many calls in a short period of time. Try again later.
HTTP Status Code: 400

 ** ResourceNotFoundException **
 The specified ARN in the request doesn't exist.
HTTP Status Code: 400

## See Also
<a name="API_DescribeCostCategoryDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ce-2017-10-25/DescribeCostCategoryDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ce-2017-10-25/DescribeCostCategoryDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/DescribeCostCategoryDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ce-2017-10-25/DescribeCostCategoryDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/DescribeCostCategoryDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ce-2017-10-25/DescribeCostCategoryDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ce-2017-10-25/DescribeCostCategoryDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ce-2017-10-25/DescribeCostCategoryDefinition)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ce-2017-10-25/DescribeCostCategoryDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/DescribeCostCategoryDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
