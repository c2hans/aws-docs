---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_UpdateCostCategoryDefinition.html
---

# UpdateCostCategoryDefinition
<a name="API_UpdateCostCategoryDefinition"></a>

Updates an existing cost category. Changes made to the cost category rules will be used to categorize the current month’s expenses and future expenses. This won’t change categorization for the previous months.

## Request Syntax
<a name="API_UpdateCostCategoryDefinition_RequestSyntax"></a>

```
{
   "CostCategoryArn": "{{string}}",
   "DefaultValue": "{{string}}",
   "EffectiveStart": "{{string}}",
   "Rules": [
      {
         "InheritedValue": {
            "DimensionKey": "{{string}}",
            "DimensionName": "{{string}}"
         },
         "Rule": {
            "And": [
               "Expression"
            ],
            "CostCategories": {
               "Key": "{{string}}",
               "MatchOptions": [ "{{string}}" ],
               "Values": [ "{{string}}" ]
            },
            "Dimensions": {
               "Key": "{{string}}",
               "MatchOptions": [ "{{string}}" ],
               "Values": [ "{{string}}" ]
            },
            "Not": "Expression",
            "Or": [
               "Expression"
            ],
            "ProductAttributes": {
               "Key": "{{string}}",
               "MatchOptions": [ "{{string}}" ],
               "Values": [ "{{string}}" ]
            },
            "Tags": {
               "Key": "{{string}}",
               "MatchOptions": [ "{{string}}" ],
               "Values": [ "{{string}}" ]
            }
         },
         "Type": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "RuleVersion": "{{string}}",
   "SplitChargeRules": [
      {
         "Method": "{{string}}",
         "Parameters": [
            {
               "Type": "{{string}}",
               "Values": [ "{{string}}" ]
            }
         ],
         "Source": "{{string}}",
         "Targets": [ "{{string}}" ]
      }
   ]
}
```

## Request Parameters
<a name="API_UpdateCostCategoryDefinition_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CostCategoryArn](#API_UpdateCostCategoryDefinition_RequestSyntax) **   <a name="awscostmanagement-UpdateCostCategoryDefinition-request-CostCategoryArn"></a>
The unique identifier for your cost category.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:[-a-zA-Z0-9/:_]+`
Required: Yes

 ** [DefaultValue](#API_UpdateCostCategoryDefinition_RequestSyntax) **   <a name="awscostmanagement-UpdateCostCategoryDefinition-request-DefaultValue"></a>
The default value for the cost category.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `^(?! )[\p{L}\p{N}\p{Z}-_]*(?<! )$`
Required: No

 ** [EffectiveStart](#API_UpdateCostCategoryDefinition_RequestSyntax) **   <a name="awscostmanagement-UpdateCostCategoryDefinition-request-EffectiveStart"></a>
The cost category's effective start date. It can only be a billing start date (first day of the month). If the date isn't provided, it's the first day of the current month. Dates can't be before the previous twelve months, or in the future.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(([+-]\d\d:\d\d)|Z)$`
Required: No

 ** [Rules](#API_UpdateCostCategoryDefinition_RequestSyntax) **   <a name="awscostmanagement-UpdateCostCategoryDefinition-request-Rules"></a>
The `Expression` object used to categorize costs. For more information, see [CostCategoryRule ](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostCategoryRule.html).
Type: Array of [CostCategoryRule](API_CostCategoryRule.md) objects
Array Members: Minimum number of 1 item. Maximum number of 500 items.
Required: Yes

 ** [RuleVersion](#API_UpdateCostCategoryDefinition_RequestSyntax) **   <a name="awscostmanagement-UpdateCostCategoryDefinition-request-RuleVersion"></a>
The rule schema version in this particular cost category.
Type: String
Valid Values: `CostCategoryExpression.v1`
Required: Yes

 ** [SplitChargeRules](#API_UpdateCostCategoryDefinition_RequestSyntax) **   <a name="awscostmanagement-UpdateCostCategoryDefinition-request-SplitChargeRules"></a>
 The split charge rules used to allocate your charges between your cost category values.
Type: Array of [CostCategorySplitChargeRule](API_CostCategorySplitChargeRule.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

## Response Syntax
<a name="API_UpdateCostCategoryDefinition_ResponseSyntax"></a>

```
{
   "CostCategoryArn": "string",
   "EffectiveStart": "string"
}
```

## Response Elements
<a name="API_UpdateCostCategoryDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CostCategoryArn](#API_UpdateCostCategoryDefinition_ResponseSyntax) **   <a name="awscostmanagement-UpdateCostCategoryDefinition-response-CostCategoryArn"></a>
The unique identifier for your cost category.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:[-a-zA-Z0-9/:_]+`

 ** [EffectiveStart](#API_UpdateCostCategoryDefinition_ResponseSyntax) **   <a name="awscostmanagement-UpdateCostCategoryDefinition-response-EffectiveStart"></a>
The cost category's effective start date. It can only be a billing start date (first day of the month).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(([+-]\d\d:\d\d)|Z)$`

## Errors
<a name="API_UpdateCostCategoryDefinition_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** LimitExceededException **
You made too many calls in a short period of time. Try again later.
HTTP Status Code: 400

 ** ResourceNotFoundException **
 The specified ARN in the request doesn't exist.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
 You've reached the limit on the number of resources you can create, or exceeded the size of an individual resource.
HTTP Status Code: 400

## See Also
<a name="API_UpdateCostCategoryDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ce-2017-10-25/UpdateCostCategoryDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ce-2017-10-25/UpdateCostCategoryDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/UpdateCostCategoryDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ce-2017-10-25/UpdateCostCategoryDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/UpdateCostCategoryDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ce-2017-10-25/UpdateCostCategoryDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ce-2017-10-25/UpdateCostCategoryDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ce-2017-10-25/UpdateCostCategoryDefinition)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ce-2017-10-25/UpdateCostCategoryDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/UpdateCostCategoryDefinition)
