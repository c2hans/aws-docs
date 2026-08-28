---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DataSetDateComparisonFilterCondition.html
---

# DataSetDateComparisonFilterCondition
<a name="API_DataSetDateComparisonFilterCondition"></a>

A filter condition that compares date values using operators like `BEFORE`, `AFTER`, or their inclusive variants.

## Contents
<a name="API_DataSetDateComparisonFilterCondition_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Operator **   <a name="QS-Type-DataSetDateComparisonFilterCondition-Operator"></a>
The comparison operator to use, such as `BEFORE`, `BEFORE_OR_EQUALS_TO`, `AFTER`, or `AFTER_OR_EQUALS_TO`.
Type: String
Valid Values: `BEFORE | BEFORE_OR_EQUALS_TO | AFTER | AFTER_OR_EQUALS_TO`
Required: Yes

 ** Value **   <a name="QS-Type-DataSetDateComparisonFilterCondition-Value"></a>
The date value to compare against.
Type: [DataSetDateFilterValue](API_DataSetDateFilterValue.md) object
Required: No

## See Also
<a name="API_DataSetDateComparisonFilterCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DataSetDateComparisonFilterCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DataSetDateComparisonFilterCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DataSetDateComparisonFilterCondition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
