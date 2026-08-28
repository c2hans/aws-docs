---
source_url: https://docs.aws.amazon.com/emr/latest/APIReference/API_BootstrapActionConfig.html
---

# BootstrapActionConfig
<a name="API_BootstrapActionConfig"></a>

Configuration of a bootstrap action.

## Contents
<a name="API_BootstrapActionConfig_Contents"></a>

 ** Name **   <a name="EMR-Type-BootstrapActionConfig-Name"></a>
The name of the bootstrap action.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** ScriptBootstrapAction **   <a name="EMR-Type-BootstrapActionConfig-ScriptBootstrapAction"></a>
The script run by the bootstrap action.
Type: [ScriptBootstrapActionConfig](API_ScriptBootstrapActionConfig.md) object
Required: Yes

## See Also
<a name="API_BootstrapActionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/BootstrapActionConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/BootstrapActionConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/BootstrapActionConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
