---
source_url: https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_KeyUsageFlags.html
---

# KeyUsageFlags
<a name="API_KeyUsageFlags"></a>

The key usage flags represent the purpose (e.g., encipherment, signature) of the key contained in the certificate.

## Contents
<a name="API_KeyUsageFlags_Contents"></a>

 ** DataEncipherment **   <a name="PcaConnectorAd-Type-KeyUsageFlags-DataEncipherment"></a>
DataEncipherment is asserted when the subject public key is used for directly enciphering raw user data without the use of an intermediate symmetric cipher.
Type: Boolean
Required: No

 ** DigitalSignature **   <a name="PcaConnectorAd-Type-KeyUsageFlags-DigitalSignature"></a>
The digitalSignature is asserted when the subject public key is used for verifying digital signatures.
Type: Boolean
Required: No

 ** KeyAgreement **   <a name="PcaConnectorAd-Type-KeyUsageFlags-KeyAgreement"></a>
KeyAgreement is asserted when the subject public key is used for key agreement.
Type: Boolean
Required: No

 ** KeyEncipherment **   <a name="PcaConnectorAd-Type-KeyUsageFlags-KeyEncipherment"></a>
KeyEncipherment is asserted when the subject public key is used for enciphering private or secret keys, i.e., for key transport.
Type: Boolean
Required: No

 ** NonRepudiation **   <a name="PcaConnectorAd-Type-KeyUsageFlags-NonRepudiation"></a>
NonRepudiation is asserted when the subject public key is used to verify digital signatures.
Type: Boolean
Required: No

## See Also
<a name="API_KeyUsageFlags_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pca-connector-ad-2018-05-10/KeyUsageFlags)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pca-connector-ad-2018-05-10/KeyUsageFlags)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pca-connector-ad-2018-05-10/KeyUsageFlags)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Private CA Connector for Active Directory. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pca-connector-ad` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
