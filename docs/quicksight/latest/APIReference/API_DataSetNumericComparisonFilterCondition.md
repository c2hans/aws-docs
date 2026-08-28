---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DataSetNumericComparisonFilterCondition.html
---

# DataSetNumericComparisonFilterCondition
<a name="API_DataSetNumericComparisonFilterCondition"></a>

A filter condition that compares numeric values using operators like `EQUALS`, `GREATER_THAN`, or `LESS_THAN`.

## Contents
<a name="API_DataSetNumericComparisonFilterCondition_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Operator **   <a name="QS-Type-DataSetNumericComparisonFilterCondition-Operator"></a>
The comparison operator to use, such as `EQUALS`, `GREATER_THAN`, `LESS_THAN`, or their variants.
Type: String
Valid Values: `EQUALS | DOES_NOT_EQUAL | GREATER_THAN | GREATER_THAN_OR_EQUALS_TO | LESS_THAN | LESS_THAN_OR_EQUALS_TO`
Required: Yes

 ** Value **   <a name="QS-Type-DataSetNumericComparisonFilterCondition-Value"></a>
The numeric value to compare against.
Type: [DataSetNumericFilterValue](API_DataSetNumericFilterValue.md) object
Required: No

## See Also
<a name="API_DataSetNumericComparisonFilterCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DataSetNumericComparisonFilterCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DataSetNumericComparisonFilterCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DataSetNumericComparisonFilterCondition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
