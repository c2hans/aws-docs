---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_AccessBudget.html
---

# AccessBudget
<a name="API_AccessBudget"></a>

An access budget that defines consumption limits for a specific resource within defined time periods.

## Contents
<a name="API_AccessBudget_Contents"></a>

 ** aggregateRemainingBudget **   <a name="API-Type-AccessBudget-aggregateRemainingBudget"></a>
The total remaining budget across all active budget periods for this resource.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** details **   <a name="API-Type-AccessBudget-details"></a>
A list of budget details for this resource. Contains active budget periods that apply to the resource.
Type: Array of [AccessBudgetDetails](API_AccessBudgetDetails.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: Yes

 ** resourceArn **   <a name="API-Type-AccessBudget-resourceArn"></a>
The Amazon Resource Name (ARN) of the resource that this access budget applies to.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership/[\d\w-]+/configuredtableassociation/[\d\w-]+`
Required: Yes

## See Also
<a name="API_AccessBudget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/AccessBudget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/AccessBudget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/AccessBudget)
