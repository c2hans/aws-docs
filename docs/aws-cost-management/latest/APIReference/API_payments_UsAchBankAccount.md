---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_payments_UsAchBankAccount.html
---

# UsAchBankAccount

The details of a bank account that is debited over Automated Clearing House (ACH).

## Contents
<a name="API_payments_UsAchBankAccount_Contents"></a>

 ** accountHolderName **   <a name="awscostmanagement-Type-payments_UsAchBankAccount-accountHolderName"></a>
The name on the account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** accountNumberTail **   <a name="awscostmanagement-Type-payments_UsAchBankAccount-accountNumberTail"></a>
The last one to four characters of the account number. This member is absent until your bank provides the account details, for example before you complete authentication with your bank.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4.
Pattern: `[A-Za-z0-9]{1,4}`
Required: No

 ** accountType **   <a name="awscostmanagement-Type-payments_UsAchBankAccount-accountType"></a>
Whether the account is a checking account or a savings account.
Type: String
Valid Values: `CHECKING | SAVINGS`
Required: No

 ** bankName **   <a name="awscostmanagement-Type-payments_UsAchBankAccount-bankName"></a>
The bank holding the account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_payments_UsAchBankAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payments-2026-09-23/UsAchBankAccount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payments-2026-09-23/UsAchBankAccount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payments-2026-09-23/UsAchBankAccount)
