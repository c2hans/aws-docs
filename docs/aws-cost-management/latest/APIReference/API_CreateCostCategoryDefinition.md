---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CreateCostCategoryDefinition.html
---

# CreateCostCategoryDefinition
<a name="API_CreateCostCategoryDefinition"></a>

Creates a new cost category with the requested name and rules.

## Request Syntax
<a name="API_CreateCostCategoryDefinition_RequestSyntax"></a>

```
{
   "DefaultValue": "{{string}}",
   "EffectiveStart": "{{string}}",
   "Name": "{{string}}",
   "ResourceTags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
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
<a name="API_CreateCostCategoryDefinition_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DefaultValue](#API_CreateCostCategoryDefinition_RequestSyntax) **   <a name="awscostmanagement-CreateCostCategoryDefinition-request-DefaultValue"></a>
The default value for the cost category.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `^(?! )[\p{L}\p{N}\p{Z}-_]*(?<! )$`
Required: No

 ** [EffectiveStart](#API_CreateCostCategoryDefinition_RequestSyntax) **   <a name="awscostmanagement-CreateCostCategoryDefinition-request-EffectiveStart"></a>
The cost category's effective start date. It can only be a billing start date (first day of the month). If the date isn't provided, it's the first day of the current month. Dates can't be before the previous twelve months, or in the future.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(([+-]\d\d:\d\d)|Z)$`
Required: No

 ** [Name](#API_CreateCostCategoryDefinition_RequestSyntax) **   <a name="awscostmanagement-CreateCostCategoryDefinition-request-Name"></a>
The unique name of the cost category.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `^(?! )[\p{L}\p{N}\p{Z}-_]*(?<! )$`
Required: Yes

 ** [ResourceTags](#API_CreateCostCategoryDefinition_RequestSyntax) **   <a name="awscostmanagement-CreateCostCategoryDefinition-request-ResourceTags"></a>
An optional list of tags to associate with the specified [`CostCategory`](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostCategory.html). You can use resource tags to control access to your `cost category` using IAM policies.
Each tag consists of a key and a value, and each key must be unique for the resource. The following restrictions apply to resource tags:
+ Although the maximum number of array members is 200, you can assign a maximum of 50 user-tags to one resource. The remaining are reserved for AWS use
+ The maximum length of a key is 128 characters
+ The maximum length of a value is 256 characters
+ Keys and values can only contain alphanumeric characters, spaces, and any of the following: `_.:/=+@-`
+ Keys and values are case sensitive
+ Keys and values are trimmed for any leading or trailing whitespaces
+ Don’t use `aws:` as a prefix for your keys. This prefix is reserved for AWS use
Type: Array of [ResourceTag](API_ResourceTag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** [Rules](#API_CreateCostCategoryDefinition_RequestSyntax) **   <a name="awscostmanagement-CreateCostCategoryDefinition-request-Rules"></a>
The cost category rules used to categorize costs. For more information, see [CostCategoryRule](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostCategoryRule.html).
Type: Array of [CostCategoryRule](API_CostCategoryRule.md) objects
Array Members: Minimum number of 1 item. Maximum number of 500 items.
Required: Yes

 ** [RuleVersion](#API_CreateCostCategoryDefinition_RequestSyntax) **   <a name="awscostmanagement-CreateCostCategoryDefinition-request-RuleVersion"></a>
The rule schema version in this particular cost category.
Type: String
Valid Values: `CostCategoryExpression.v1`
Required: Yes

 ** [SplitChargeRules](#API_CreateCostCategoryDefinition_RequestSyntax) **   <a name="awscostmanagement-CreateCostCategoryDefinition-request-SplitChargeRules"></a>
 The split charge rules used to allocate your charges between your cost category values.
Type: Array of [CostCategorySplitChargeRule](API_CostCategorySplitChargeRule.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

## Response Syntax
<a name="API_CreateCostCategoryDefinition_ResponseSyntax"></a>

```
{
   "CostCategoryArn": "string",
   "EffectiveStart": "string"
}
```

## Response Elements
<a name="API_CreateCostCategoryDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CostCategoryArn](#API_CreateCostCategoryDefinition_ResponseSyntax) **   <a name="awscostmanagement-CreateCostCategoryDefinition-response-CostCategoryArn"></a>
The unique identifier for your newly created cost category.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:[-a-zA-Z0-9/:_]+`

 ** [EffectiveStart](#API_CreateCostCategoryDefinition_ResponseSyntax) **   <a name="awscostmanagement-CreateCostCategoryDefinition-response-EffectiveStart"></a>
The cost category's effective start date. It can only be a billing start date (first day of the month).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(([+-]\d\d:\d\d)|Z)$`

## Errors
<a name="API_CreateCostCategoryDefinition_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** LimitExceededException **
You made too many calls in a short period of time. Try again later.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
 You've reached the limit on the number of resources you can create, or exceeded the size of an individual resource.
HTTP Status Code: 400

## See Also
<a name="API_CreateCostCategoryDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ce-2017-10-25/CreateCostCategoryDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ce-2017-10-25/CreateCostCategoryDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/CreateCostCategoryDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ce-2017-10-25/CreateCostCategoryDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/CreateCostCategoryDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ce-2017-10-25/CreateCostCategoryDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ce-2017-10-25/CreateCostCategoryDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ce-2017-10-25/CreateCostCategoryDefinition)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ce-2017-10-25/CreateCostCategoryDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/CreateCostCategoryDefinition)
