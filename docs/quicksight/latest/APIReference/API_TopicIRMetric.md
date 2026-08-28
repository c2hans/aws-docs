---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TopicIRMetric.html
---

# TopicIRMetric
<a name="API_TopicIRMetric"></a>

The definition for a `TopicIRMetric`.

## Contents
<a name="API_TopicIRMetric_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CalculatedFieldReferences **   <a name="QS-Type-TopicIRMetric-CalculatedFieldReferences"></a>
The calculated field references for the `TopicIRMetric`.
Type: Array of [Identifier](API_Identifier.md) objects
Array Members: Maximum number of 250 items.
Required: No

 ** ComparisonMethod **   <a name="QS-Type-TopicIRMetric-ComparisonMethod"></a>
The comparison method for the `TopicIRMetric`.
Type: [TopicIRComparisonMethod](API_TopicIRComparisonMethod.md) object
Required: No

 ** DisplayFormat **   <a name="QS-Type-TopicIRMetric-DisplayFormat"></a>
The display format for the `TopicIRMetric`.
Type: String
Valid Values: `AUTO | PERCENT | CURRENCY | NUMBER | DATE | STRING`
Required: No

 ** DisplayFormatOptions **   <a name="QS-Type-TopicIRMetric-DisplayFormatOptions"></a>
A structure that represents additional options for display formatting.
Type: [DisplayFormatOptions](API_DisplayFormatOptions.md) object
Required: No

 ** Expression **   <a name="QS-Type-TopicIRMetric-Expression"></a>
The expression for the `TopicIRMetric`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** Function **   <a name="QS-Type-TopicIRMetric-Function"></a>
The function for the `TopicIRMetric`.
Type: [AggFunction](API_AggFunction.md) object
Required: No

 ** MetricId **   <a name="QS-Type-TopicIRMetric-MetricId"></a>
The metric ID for the `TopicIRMetric`.
Type: [Identifier](API_Identifier.md) object
Required: No

 ** NamedEntity **   <a name="QS-Type-TopicIRMetric-NamedEntity"></a>
The named entity for the `TopicIRMetric`.
Type: [NamedEntityRef](API_NamedEntityRef.md) object
Required: No

 ** Operands **   <a name="QS-Type-TopicIRMetric-Operands"></a>
The operands for the `TopicIRMetric`.
Type: Array of [Identifier](API_Identifier.md) objects
Array Members: Maximum number of 25 items.
Required: No

## See Also
<a name="API_TopicIRMetric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TopicIRMetric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TopicIRMetric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TopicIRMetric)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
