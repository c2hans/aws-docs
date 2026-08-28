---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_EvaluationFormItem.html
---

# EvaluationFormItem
<a name="API_EvaluationFormItem"></a>

Information about an item from an evaluation form. The item must be either a section or a question.

## Contents
<a name="API_EvaluationFormItem_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** Question **   <a name="connect-Type-EvaluationFormItem-Question"></a>
The information of the question.
Type: [EvaluationFormQuestion](API_EvaluationFormQuestion.md) object
Required: No

 ** Section **   <a name="connect-Type-EvaluationFormItem-Section"></a>
The information of the section.
Type: [EvaluationFormSection](API_EvaluationFormSection.md) object
Required: No

## See Also
<a name="API_EvaluationFormItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/EvaluationFormItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/EvaluationFormItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/EvaluationFormItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
