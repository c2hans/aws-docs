---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_GetPreferences.html
---

# GetPreferences
<a name="API_CostOptimizationHub_GetPreferences"></a>

Returns a set of preferences for an account in order to add account-specific preferences into the service. These preferences impact how the savings associated with recommendations are presented—estimated savings after discounts or estimated savings before discounts, for example.

## Response Syntax
<a name="API_CostOptimizationHub_GetPreferences_ResponseSyntax"></a>

```
{
   "memberAccountDiscountVisibility": "string",
   "preferredCommitment": {
      "paymentOption": "string",
      "term": "string"
   },
   "savingsEstimationMode": "string"
}
```

## Response Elements
<a name="API_CostOptimizationHub_GetPreferences_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [memberAccountDiscountVisibility](#API_CostOptimizationHub_GetPreferences_ResponseSyntax) **   <a name="awscostmanagement-CostOptimizationHub_GetPreferences-response-memberAccountDiscountVisibility"></a>
Retrieves the status of the "member account discount visibility" preference.
Type: String
Valid Values: `All | None`

 ** [preferredCommitment](#API_CostOptimizationHub_GetPreferences_ResponseSyntax) **   <a name="awscostmanagement-CostOptimizationHub_GetPreferences-response-preferredCommitment"></a>
Retrieves the current preferences for how Reserved Instances and Savings Plans cost-saving opportunities are prioritized in terms of payment option and term length.
Type: [PreferredCommitment](API_CostOptimizationHub_PreferredCommitment.md) object

 ** [savingsEstimationMode](#API_CostOptimizationHub_GetPreferences_ResponseSyntax) **   <a name="awscostmanagement-CostOptimizationHub_GetPreferences-response-savingsEstimationMode"></a>
Retrieves the status of the "savings estimation mode" preference.
Type: String
Valid Values: `BeforeDiscounts | AfterDiscounts`

## Errors
<a name="API_CostOptimizationHub_GetPreferences_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You are not authorized to use this operation with the given parameters.
HTTP Status Code: 400

 ** InternalServerException **
An error on the server occurred during the processing of your request. Try again later.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** fields **
The list of fields that are invalid.
 ** reason **
The reason for the validation exception.
HTTP Status Code: 400

## See Also
<a name="API_CostOptimizationHub_GetPreferences_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cost-optimization-hub-2022-07-26/GetPreferences)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cost-optimization-hub-2022-07-26/GetPreferences)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cost-optimization-hub-2022-07-26/GetPreferences)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cost-optimization-hub-2022-07-26/GetPreferences)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cost-optimization-hub-2022-07-26/GetPreferences)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cost-optimization-hub-2022-07-26/GetPreferences)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cost-optimization-hub-2022-07-26/GetPreferences)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cost-optimization-hub-2022-07-26/GetPreferences)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cost-optimization-hub-2022-07-26/GetPreferences)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cost-optimization-hub-2022-07-26/GetPreferences)
