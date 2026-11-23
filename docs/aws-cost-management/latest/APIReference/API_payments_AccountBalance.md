---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_payments_AccountBalance.html
---

# AccountBalance

An amount of the balance that `GetAccountBalance` returns: the total for one merchant of record in one currency.

## Contents
<a name="API_payments_AccountBalance_Contents"></a>

 ** amount **   <a name="awscostmanagement-Type-payments_AccountBalance-amount"></a>
The amount, in the currency that the records making up this balance were issued in.
Type: [CurrencyAmount](API_payments_CurrencyAmount.md) object
Required: Yes

 ** merchantOfRecord **   <a name="awscostmanagement-Type-payments_AccountBalance-merchantOfRecord"></a>
The merchant of record that issued the invoices or credit memos that make up this amount.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## See Also
<a name="API_payments_AccountBalance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payments-2026-09-23/AccountBalance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payments-2026-09-23/AccountBalance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payments-2026-09-23/AccountBalance)
