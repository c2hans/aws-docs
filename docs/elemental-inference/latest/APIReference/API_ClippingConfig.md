---
source_url: https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_ClippingConfig.html
---

# ClippingConfig
<a name="API_ClippingConfig"></a>

A type of OutputConfig, used when the output in a feed is for the clip feature.

## Contents
<a name="API_ClippingConfig_Contents"></a>

 ** callbackMetadata **   <a name="elementalinference-Type-ClippingConfig-callbackMetadata"></a>
A string that you want Elemental Inference to always include in the event clipping metadata for this output. The string might identify the sports event in the source media, for example.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\w \-\.',@:;]*`
Required: No

## See Also
<a name="API_ClippingConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elementalinference-2018-11-14/ClippingConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elementalinference-2018-11-14/ClippingConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elementalinference-2018-11-14/ClippingConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Inference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-inference` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
