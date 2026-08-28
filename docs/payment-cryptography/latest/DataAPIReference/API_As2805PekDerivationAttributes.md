---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_As2805PekDerivationAttributes.html
---

# As2805PekDerivationAttributes
<a name="API_As2805PekDerivationAttributes"></a>

Parameter information to use a PEK derived using AS2805.

## Contents
<a name="API_As2805PekDerivationAttributes_Contents"></a>

 ** SystemTraceAuditNumber **   <a name="paymentcryptographydata-Type-As2805PekDerivationAttributes-SystemTraceAuditNumber"></a>
The system trace audit number for the transaction.
Type: String
Length Constraints: Fixed length of 6.
Pattern: `[0-9]+`
Required: Yes

 ** TransactionAmount **   <a name="paymentcryptographydata-Type-As2805PekDerivationAttributes-TransactionAmount"></a>
The transaction amount for the transaction.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]+`
Required: Yes

## See Also
<a name="API_As2805PekDerivationAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/As2805PekDerivationAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/As2805PekDerivationAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/As2805PekDerivationAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Payment Cryptography Data Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query payment-cryptography` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
