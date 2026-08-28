---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CalculatedField.html
---

# CalculatedField
<a name="API_CalculatedField"></a>

The calculated field of an analysis.

## Contents
<a name="API_CalculatedField_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Expression **   <a name="QS-Type-CalculatedField-Expression"></a>
The expression of the calculated field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32000.
Required: Yes

 ** Name **   <a name="QS-Type-CalculatedField-Name"></a>
The name of the calculated field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** DataSetIdentifier **   <a name="QS-Type-CalculatedField-DataSetIdentifier"></a>
The data set that is used in this calculated field.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** TopicIdentifier **   <a name="QS-Type-CalculatedField-TopicIdentifier"></a>
The topic that is used in this calculated field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_CalculatedField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CalculatedField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CalculatedField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CalculatedField)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
