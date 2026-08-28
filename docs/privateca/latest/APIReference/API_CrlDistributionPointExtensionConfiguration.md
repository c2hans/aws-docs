---
source_url: https://docs.aws.amazon.com/privateca/latest/APIReference/API_CrlDistributionPointExtensionConfiguration.html
---

# CrlDistributionPointExtensionConfiguration
<a name="API_CrlDistributionPointExtensionConfiguration"></a>

Contains configuration information for the default behavior of the CRL Distribution Point (CDP) extension in certificates issued by your CA. This extension contains a link to download the CRL, so you can check whether a certificate has been revoked. To choose whether you want this extension omitted or not in certificates issued by your CA, you can set the **OmitExtension** parameter.

## Contents
<a name="API_CrlDistributionPointExtensionConfiguration_Contents"></a>

 ** OmitExtension **   <a name="privateca-Type-CrlDistributionPointExtensionConfiguration-OmitExtension"></a>
Configures whether the CRL Distribution Point extension should be populated with the default URL to the CRL. If set to `true`, then the CDP extension will not be present in any certificates issued by that CA unless otherwise specified through CSR or API passthrough.
Only set this if you have another way to distribute the CRL Distribution Points for certificates issued by your CA, such as the Matter Distributed Compliance Ledger
This configuration cannot be enabled with a custom CNAME set.
Type: Boolean
Required: Yes

## See Also
<a name="API_CrlDistributionPointExtensionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-pca-2017-08-22/CrlDistributionPointExtensionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-pca-2017-08-22/CrlDistributionPointExtensionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-pca-2017-08-22/CrlDistributionPointExtensionConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Private CA. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query privateca` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
