---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_SessionKeyEmvCommon.html
---

# SessionKeyEmvCommon
<a name="API_SessionKeyEmvCommon"></a>

Parameters to derive session key for an Emv common payment card for ARQC verification.

## Contents
<a name="API_SessionKeyEmvCommon_Contents"></a>

 ** ApplicationTransactionCounter **   <a name="paymentcryptographydata-Type-SessionKeyEmvCommon-ApplicationTransactionCounter"></a>
The transaction counter that is provided by the terminal during transaction processing.
Type: String
Length Constraints: Fixed length of 4.
Pattern: `[0-9a-fA-F]+`
Required: Yes

 ** PanSequenceNumber **   <a name="paymentcryptographydata-Type-SessionKeyEmvCommon-PanSequenceNumber"></a>
A number that identifies and differentiates payment cards with the same Primary Account Number (PAN).
Type: String
Length Constraints: Fixed length of 2.
Pattern: `[0-9]+`
Required: Yes

 ** PrimaryAccountNumber **   <a name="paymentcryptographydata-Type-SessionKeyEmvCommon-PrimaryAccountNumber"></a>
The Primary Account Number (PAN) of the cardholder. A PAN is a unique identifier for a payment credit or debit card and associates the card to a specific account holder.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 19.
Pattern: `[0-9]+`
Required: Yes

## See Also
<a name="API_SessionKeyEmvCommon_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/SessionKeyEmvCommon)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/SessionKeyEmvCommon)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/SessionKeyEmvCommon)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Payment Cryptography Data Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query payment-cryptography` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
