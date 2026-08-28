---
source_url: https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentTargetFilter.html
---

# ExperimentTargetFilter
<a name="API_ExperimentTargetFilter"></a>

Describes a filter used for the target resources in an experiment.

## Contents
<a name="API_ExperimentTargetFilter_Contents"></a>

 ** path **   <a name="fis-Type-ExperimentTargetFilter-path"></a>
The attribute path for the filter.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `[\S]+`
Required: No

 ** values **   <a name="fis-Type-ExperimentTargetFilter-values"></a>
The attribute values for the filter.
Type: Array of strings
Length Constraints: Maximum length of 128.
Pattern: `[\S]+`
Required: No

## See Also
<a name="API_ExperimentTargetFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fis-2020-12-01/ExperimentTargetFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fis-2020-12-01/ExperimentTargetFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fis-2020-12-01/ExperimentTargetFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Fault Injection Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
