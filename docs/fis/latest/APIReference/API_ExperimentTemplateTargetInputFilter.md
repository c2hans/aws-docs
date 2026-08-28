---
source_url: https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentTemplateTargetInputFilter.html
---

# ExperimentTemplateTargetInputFilter
<a name="API_ExperimentTemplateTargetInputFilter"></a>

Specifies a filter used for the target resource input in an experiment template.

For more information, see [Resource filters](https://docs.aws.amazon.com/fis/latest/userguide/targets.html#target-filters) in the * AWS Fault Injection Service User Guide*.

## Contents
<a name="API_ExperimentTemplateTargetInputFilter_Contents"></a>

 ** path **   <a name="fis-Type-ExperimentTemplateTargetInputFilter-path"></a>
The attribute path for the filter.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `[\S]+`
Required: Yes

 ** values **   <a name="fis-Type-ExperimentTemplateTargetInputFilter-values"></a>
The attribute values for the filter.
Type: Array of strings
Length Constraints: Maximum length of 128.
Pattern: `[\S]+`
Required: Yes

## See Also
<a name="API_ExperimentTemplateTargetInputFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fis-2020-12-01/ExperimentTemplateTargetInputFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fis-2020-12-01/ExperimentTemplateTargetInputFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fis-2020-12-01/ExperimentTemplateTargetInputFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Fault Injection Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
