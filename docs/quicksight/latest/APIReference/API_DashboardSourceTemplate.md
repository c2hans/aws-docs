---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DashboardSourceTemplate.html
---

# DashboardSourceTemplate
<a name="API_DashboardSourceTemplate"></a>

Dashboard source template.

## Contents
<a name="API_DashboardSourceTemplate_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="QS-Type-DashboardSourceTemplate-Arn"></a>
The Amazon Resource Name (ARN) of the resource.
Type: String
Required: Yes

 ** DataSetReferences **   <a name="QS-Type-DashboardSourceTemplate-DataSetReferences"></a>
Dataset references.
Type: Array of [DataSetReference](API_DataSetReference.md) objects
Array Members: Minimum number of 0 items.
Required: Yes

 ** TopicReferences **   <a name="QS-Type-DashboardSourceTemplate-TopicReferences"></a>
The topic references for the source template of a dashboard.
Type: Array of [TopicReference](API_TopicReference.md) objects
Array Members: Minimum number of 1 item.
Required: No

## See Also
<a name="API_DashboardSourceTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DashboardSourceTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DashboardSourceTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DashboardSourceTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
