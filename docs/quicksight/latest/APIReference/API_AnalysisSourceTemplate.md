---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AnalysisSourceTemplate.html
---

# AnalysisSourceTemplate
<a name="API_AnalysisSourceTemplate"></a>

The source template of an analysis.

## Contents
<a name="API_AnalysisSourceTemplate_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="QS-Type-AnalysisSourceTemplate-Arn"></a>
The Amazon Resource Name (ARN) of the source template of an analysis.
Type: String
Required: Yes

 ** DataSetReferences **   <a name="QS-Type-AnalysisSourceTemplate-DataSetReferences"></a>
The dataset references of the source template of an analysis.
Type: Array of [DataSetReference](API_DataSetReference.md) objects
Array Members: Minimum number of 0 items.
Required: Yes

 ** TopicReferences **   <a name="QS-Type-AnalysisSourceTemplate-TopicReferences"></a>
The topic references of the source template of an analysis.
Type: Array of [TopicReference](API_TopicReference.md) objects
Array Members: Minimum number of 1 item.
Required: No

## See Also
<a name="API_AnalysisSourceTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/AnalysisSourceTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/AnalysisSourceTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/AnalysisSourceTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
