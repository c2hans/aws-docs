---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_ChargeAccount.html
---

# ChargeAccount
<a name="API_billing_ChargeAccount"></a>

An account that is charged all or a portion of the total Support charge and the percentage of the charge allocated to it.

## Contents
<a name="API_billing_ChargeAccount_Contents"></a>

 ** accountId **   <a name="awscostmanagement-Type-billing_ChargeAccount-accountId"></a>
The account ID.
Type: String
Pattern: `[0-9]{12}`
Required: Yes

 ** chargePercentage **   <a name="awscostmanagement-Type-billing_ChargeAccount-chargePercentage"></a>
The percentage of the total Support charge allocated to this account. This is 0.0 when supportAllocationMethod = Proportional.
Type: String
Required: Yes

## See Also
<a name="API_billing_ChargeAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/ChargeAccount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/ChargeAccount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/ChargeAccount)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
