---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DeleteCostCategoryDefinition.html
---

# DeleteCostCategoryDefinition
<a name="API_DeleteCostCategoryDefinition"></a>

Deletes a cost category. Expenses from this month going forward will no longer be categorized with this cost category.

## Request Syntax
<a name="API_DeleteCostCategoryDefinition_RequestSyntax"></a>

```
{
   "CostCategoryArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteCostCategoryDefinition_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CostCategoryArn](#API_DeleteCostCategoryDefinition_RequestSyntax) **   <a name="awscostmanagement-DeleteCostCategoryDefinition-request-CostCategoryArn"></a>
The unique identifier for your cost category.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:[-a-zA-Z0-9/:_]+`
Required: Yes

## Response Syntax
<a name="API_DeleteCostCategoryDefinition_ResponseSyntax"></a>

```
{
   "CostCategoryArn": "string",
   "EffectiveEnd": "string"
}
```

## Response Elements
<a name="API_DeleteCostCategoryDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CostCategoryArn](#API_DeleteCostCategoryDefinition_ResponseSyntax) **   <a name="awscostmanagement-DeleteCostCategoryDefinition-response-CostCategoryArn"></a>
The unique identifier for your cost category.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:[-a-zA-Z0-9/:_]+`

 ** [EffectiveEnd](#API_DeleteCostCategoryDefinition_ResponseSyntax) **   <a name="awscostmanagement-DeleteCostCategoryDefinition-response-EffectiveEnd"></a>
The effective end date of the cost category as a result of deleting it. No costs after this date is categorized by the deleted cost category.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(([+-]\d\d:\d\d)|Z)$`

## Errors
<a name="API_DeleteCostCategoryDefinition_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** LimitExceededException **
You made too many calls in a short period of time. Try again later.
HTTP Status Code: 400

 ** ResourceNotFoundException **
 The specified ARN in the request doesn't exist.
HTTP Status Code: 400

## See Also
<a name="API_DeleteCostCategoryDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ce-2017-10-25/DeleteCostCategoryDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ce-2017-10-25/DeleteCostCategoryDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/DeleteCostCategoryDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ce-2017-10-25/DeleteCostCategoryDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/DeleteCostCategoryDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ce-2017-10-25/DeleteCostCategoryDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ce-2017-10-25/DeleteCostCategoryDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ce-2017-10-25/DeleteCostCategoryDefinition)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ce-2017-10-25/DeleteCostCategoryDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/DeleteCostCategoryDefinition)
