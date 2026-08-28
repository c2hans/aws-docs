---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_CreditData.html
---

# CreditData
<a name="API_billing_CreditData"></a>

Detailed information about an AWS credit, including its identifier, type, monetary amounts, applicable products, sharing configuration, and current enabled status.

## Contents
<a name="API_billing_CreditData_Contents"></a>

 ** accountId **   <a name="awscostmanagement-Type-billing_CreditData-accountId"></a>
The AWS account ID that owns the credit.
Type: String
Pattern: `[0-9]{12}`
Required: Yes

 ** creditId **   <a name="awscostmanagement-Type-billing_CreditData-creditId"></a>
The unique identifier for the credit.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[0-9]+`
Required: Yes

 ** creditType **   <a name="awscostmanagement-Type-billing_CreditData-creditType"></a>
The type of credit. Examples: `Promotion`, `Refund`, `TrueUp`.
Type: String
Required: Yes

 ** description **   <a name="awscostmanagement-Type-billing_CreditData-description"></a>
A human-readable description of the credit.
Type: String
Required: Yes

 ** initialAmount **   <a name="awscostmanagement-Type-billing_CreditData-initialAmount"></a>
The initial amount of the credit when it was issued.
Type: [Amount](API_billing_Amount.md) object
Required: Yes

 ** remainingAmount **   <a name="awscostmanagement-Type-billing_CreditData-remainingAmount"></a>
The unused balance of the credit.
Type: [Amount](API_billing_Amount.md) object
Required: Yes

 ** startDate **   <a name="awscostmanagement-Type-billing_CreditData-startDate"></a>
The date the credit becomes valid, as Unix epoch seconds.
Type: Timestamp
Required: Yes

 ** accountHasCreditSharingEnabled **   <a name="awscostmanagement-Type-billing_CreditData-accountHasCreditSharingEnabled"></a>
Whether the owning account has account-level credit sharing turned on.
Type: Boolean
Required: No

 ** applicableProductNames **   <a name="awscostmanagement-Type-billing_CreditData-applicableProductNames"></a>
The names of AWS services this credit applies to.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1000 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** applicationType **   <a name="awscostmanagement-Type-billing_CreditData-applicationType"></a>
When the credit is applied during bill computation. Valid values: `BEFORE_CROSS_SERVICE_DISCOUNTS`, `AFTER_DISCOUNTS`.
Type: String
Valid Values: `BEFORE_CROSS_SERVICE_DISCOUNTS | AFTER_DISCOUNTS`
Required: No

 ** costCategoryArn **   <a name="awscostmanagement-Type-billing_CreditData-costCategoryArn"></a>
The Amazon Resource Name (ARN) of the Cost Category controlling the credit's sharing scope. Present only when `creditSharingType` is `COST_CATEGORY_RULE`.
Type: String
Required: No

 ** creditConsoleVisibility **   <a name="awscostmanagement-Type-billing_CreditData-creditConsoleVisibility"></a>
The display configuration for the credit in the AWS Billing console.
Type: String
Required: No

 ** creditSharingType **   <a name="awscostmanagement-Type-billing_CreditData-creditSharingType"></a>
The sharing configuration for the credit. Valid values: `DEFAULT`, `DISABLED`, `CUSTOM`, `COST_CATEGORY_RULE`.
Type: String
Valid Values: `DEFAULT | DISABLED | CUSTOM | COST_CATEGORY_RULE`
Required: No

 ** creditStatus **   <a name="awscostmanagement-Type-billing_CreditData-creditStatus"></a>
Whether the credit participates in billing runs. Valid values: `ENABLED`, `DISABLED`.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** endDate **   <a name="awscostmanagement-Type-billing_CreditData-endDate"></a>
The date the credit expires, as Unix epoch seconds.
Type: Timestamp
Required: No

 ** estimatedAmount **   <a name="awscostmanagement-Type-billing_CreditData-estimatedAmount"></a>
The estimated remaining balance, including in-flight (open) bills that have not yet been finalized.
Type: [Amount](API_billing_Amount.md) object
Required: No

 ** exhaustDate **   <a name="awscostmanagement-Type-billing_CreditData-exhaustDate"></a>
The date the credit balance reached zero, as Unix epoch seconds.
Type: Timestamp
Required: No

 ** purchaseTypeApplications **   <a name="awscostmanagement-Type-billing_CreditData-purchaseTypeApplications"></a>
Restricts which purchase types this credit applies to. When `null` or omitted, the credit applies to all purchase types.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** ruleName **   <a name="awscostmanagement-Type-billing_CreditData-ruleName"></a>
The rule name within the Cost Category. Present only when `creditSharingType` is `COST_CATEGORY_RULE`.
Type: String
Required: No

 ** shareableAccounts **   <a name="awscostmanagement-Type-billing_CreditData-shareableAccounts"></a>
The AWS account IDs entitled to apply this credit.
Type: Array of strings
Pattern: `[0-9]{12}`
Required: No

## See Also
<a name="API_billing_CreditData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/CreditData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/CreditData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/CreditData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
