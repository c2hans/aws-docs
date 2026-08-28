---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_TranslationIsoFormats.html
---

# TranslationIsoFormats
<a name="API_TranslationIsoFormats"></a>

Parameters that are required for translation between ISO9564 PIN block formats 0,1,3,4.

## Contents
<a name="API_TranslationIsoFormats_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** As2805Format0 **   <a name="paymentcryptographydata-Type-TranslationIsoFormats-As2805Format0"></a>
Parameters that are required for AS2805 PIN format 0 translation.
Type: [TranslationPinDataAs2805Format0](API_TranslationPinDataAs2805Format0.md) object
Required: No

 ** IsoFormat0 **   <a name="paymentcryptographydata-Type-TranslationIsoFormats-IsoFormat0"></a>
Parameters that are required for ISO9564 PIN format 0 translation.
Type: [TranslationPinDataIsoFormat034](API_TranslationPinDataIsoFormat034.md) object
Required: No

 ** IsoFormat1 **   <a name="paymentcryptographydata-Type-TranslationIsoFormats-IsoFormat1"></a>
Parameters that are required for ISO9564 PIN format 1 translation.
Type: [TranslationPinDataIsoFormat1](API_TranslationPinDataIsoFormat1.md) object
Required: No

 ** IsoFormat3 **   <a name="paymentcryptographydata-Type-TranslationIsoFormats-IsoFormat3"></a>
Parameters that are required for ISO9564 PIN format 3 translation.
Type: [TranslationPinDataIsoFormat034](API_TranslationPinDataIsoFormat034.md) object
Required: No

 ** IsoFormat4 **   <a name="paymentcryptographydata-Type-TranslationIsoFormats-IsoFormat4"></a>
Parameters that are required for ISO9564 PIN format 4 translation.
Type: [TranslationPinDataIsoFormat034](API_TranslationPinDataIsoFormat034.md) object
Required: No

## See Also
<a name="API_TranslationIsoFormats_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/TranslationIsoFormats)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/TranslationIsoFormats)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/TranslationIsoFormats)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Payment Cryptography Data Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query payment-cryptography` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
