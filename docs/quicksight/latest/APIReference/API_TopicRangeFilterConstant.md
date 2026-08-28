---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TopicRangeFilterConstant.html
---

# TopicRangeFilterConstant
<a name="API_TopicRangeFilterConstant"></a>

A constant value that is used in a range filter to specify the endpoints of the range.

## Contents
<a name="API_TopicRangeFilterConstant_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ConstantType **   <a name="QS-Type-TopicRangeFilterConstant-ConstantType"></a>
The data type of the constant value that is used in a range filter. Valid values for this structure are `RANGE`.
Type: String
Valid Values: `SINGULAR | RANGE | COLLECTIVE`
Required: No

 ** RangeConstant **   <a name="QS-Type-TopicRangeFilterConstant-RangeConstant"></a>
The value of the constant that is used to specify the endpoints of a range filter.
Type: [RangeConstant](API_RangeConstant.md) object
Required: No

## See Also
<a name="API_TopicRangeFilterConstant_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TopicRangeFilterConstant)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TopicRangeFilterConstant)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TopicRangeFilterConstant)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
