---
source_url: https://docs.aws.amazon.com/emr/latest/APIReference/API_SupportedProductConfig.html
---

# SupportedProductConfig
<a name="API_SupportedProductConfig"></a>

The list of supported product configurations that allow user-supplied arguments. Amazon EMR accepts these arguments and forwards them to the corresponding installation script as bootstrap action arguments.

## Contents
<a name="API_SupportedProductConfig_Contents"></a>

 ** Args **   <a name="EMR-Type-SupportedProductConfig-Args"></a>
The list of user-supplied arguments.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 10280.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** Name **   <a name="EMR-Type-SupportedProductConfig-Name"></a>
The name of the product configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

## See Also
<a name="API_SupportedProductConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/SupportedProductConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/SupportedProductConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/SupportedProductConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
