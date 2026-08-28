---
source_url: https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_TemplateDefinition.html
---

# TemplateDefinition
<a name="API_TemplateDefinition"></a>

Template configuration to define the information included in certificates. Define certificate validity and renewal periods, certificate request handling and enrollment options, key usage extensions, application policies, and cryptography settings.

## Contents
<a name="API_TemplateDefinition_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** TemplateV2 **   <a name="PcaConnectorAd-Type-TemplateDefinition-TemplateV2"></a>
Template configuration to define the information included in certificates. Define certificate validity and renewal periods, certificate request handling and enrollment options, key usage extensions, application policies, and cryptography settings.
Type: [TemplateV2](API_TemplateV2.md) object
Required: No

 ** TemplateV3 **   <a name="PcaConnectorAd-Type-TemplateDefinition-TemplateV3"></a>
Template configuration to define the information included in certificates. Define certificate validity and renewal periods, certificate request handling and enrollment options, key usage extensions, application policies, and cryptography settings.
Type: [TemplateV3](API_TemplateV3.md) object
Required: No

 ** TemplateV4 **   <a name="PcaConnectorAd-Type-TemplateDefinition-TemplateV4"></a>
Template configuration to define the information included in certificates. Define certificate validity and renewal periods, certificate request handling and enrollment options, key usage extensions, application policies, and cryptography settings.
Type: [TemplateV4](API_TemplateV4.md) object
Required: No

## See Also
<a name="API_TemplateDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pca-connector-ad-2018-05-10/TemplateDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pca-connector-ad-2018-05-10/TemplateDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pca-connector-ad-2018-05-10/TemplateDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Private CA Connector for Active Directory. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pca-connector-ad` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
