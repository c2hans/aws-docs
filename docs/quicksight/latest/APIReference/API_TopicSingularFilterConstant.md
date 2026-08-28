---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TopicSingularFilterConstant.html
---

# TopicSingularFilterConstant
<a name="API_TopicSingularFilterConstant"></a>

A structure that represents a singular filter constant, used in filters to specify a single value to match against.

## Contents
<a name="API_TopicSingularFilterConstant_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ConstantType **   <a name="QS-Type-TopicSingularFilterConstant-ConstantType"></a>
The type of the singular filter constant. Valid values for this structure are `SINGULAR`.
Type: String
Valid Values: `SINGULAR | RANGE | COLLECTIVE`
Required: No

 ** SingularConstant **   <a name="QS-Type-TopicSingularFilterConstant-SingularConstant"></a>
The value of the singular filter constant.
Type: String
Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_TopicSingularFilterConstant_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TopicSingularFilterConstant)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TopicSingularFilterConstant)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TopicSingularFilterConstant)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
