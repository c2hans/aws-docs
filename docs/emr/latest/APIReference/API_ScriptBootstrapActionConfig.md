---
source_url: https://docs.aws.amazon.com/emr/latest/APIReference/API_ScriptBootstrapActionConfig.html
---

# ScriptBootstrapActionConfig
<a name="API_ScriptBootstrapActionConfig"></a>

Configuration of the script to run during a bootstrap action.

## Contents
<a name="API_ScriptBootstrapActionConfig_Contents"></a>

 ** Path **   <a name="EMR-Type-ScriptBootstrapActionConfig-Path"></a>
Location in Amazon S3 of the script to run during a bootstrap action.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10280.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** Args **   <a name="EMR-Type-ScriptBootstrapActionConfig-Args"></a>
A list of command line arguments to pass to the bootstrap action script.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 10280.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

## See Also
<a name="API_ScriptBootstrapActionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/ScriptBootstrapActionConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/ScriptBootstrapActionConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/ScriptBootstrapActionConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
