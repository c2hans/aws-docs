---
source_url: https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_KeyUsageProperty.html
---

# KeyUsageProperty
<a name="API_KeyUsageProperty"></a>

The key usage property defines the purpose of the private key contained in the certificate. You can specify specific purposes using property flags or all by using property type ALL.

## Contents
<a name="API_KeyUsageProperty_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** PropertyFlags **   <a name="PcaConnectorAd-Type-KeyUsageProperty-PropertyFlags"></a>
You can specify key usage for encryption, key agreement, and signature. You can use property flags or property type but not both.
Type: [KeyUsagePropertyFlags](API_KeyUsagePropertyFlags.md) object
Required: No

 ** PropertyType **   <a name="PcaConnectorAd-Type-KeyUsageProperty-PropertyType"></a>
You can specify all key usages using property type ALL. You can use property type or property flags but not both.
Type: String
Valid Values: `ALL`
Required: No

## See Also
<a name="API_KeyUsageProperty_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pca-connector-ad-2018-05-10/KeyUsageProperty)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pca-connector-ad-2018-05-10/KeyUsageProperty)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pca-connector-ad-2018-05-10/KeyUsageProperty)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Private CA Connector for Active Directory. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pca-connector-ad` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
