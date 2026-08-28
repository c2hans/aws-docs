---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_NamedEntityDefinition.html
---

# NamedEntityDefinition
<a name="API_NamedEntityDefinition"></a>

A structure that represents a named entity.

## Contents
<a name="API_NamedEntityDefinition_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** FieldName **   <a name="QS-Type-NamedEntityDefinition-FieldName"></a>
The name of the entity.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** IsHidden **   <a name="QS-Type-NamedEntityDefinition-IsHidden"></a>
A Boolean value that indicates whether the named entity definition is hidden.
Type: Boolean
Required: No

 ** Metric **   <a name="QS-Type-NamedEntityDefinition-Metric"></a>
The definition of a metric.
Type: [NamedEntityDefinitionMetric](API_NamedEntityDefinitionMetric.md) object
Required: No

 ** PresentationOrder **   <a name="QS-Type-NamedEntityDefinition-PresentationOrder"></a>
The presentation order of the named entity definition.
Type: Integer
Required: No

 ** PropertyName **   <a name="QS-Type-NamedEntityDefinition-PropertyName"></a>
The property name to be used for the named entity.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** PropertyRole **   <a name="QS-Type-NamedEntityDefinition-PropertyRole"></a>
The property role. Valid values for this structure are `PRIMARY` and `ID`.
Type: String
Valid Values: `PRIMARY | ID`
Required: No

 ** PropertyUsage **   <a name="QS-Type-NamedEntityDefinition-PropertyUsage"></a>
The property usage. Valid values for this structure are `INHERIT`, `DIMENSION`, and `MEASURE`.
Type: String
Valid Values: `INHERIT | DIMENSION | MEASURE`
Required: No

 ** RankOrder **   <a name="QS-Type-NamedEntityDefinition-RankOrder"></a>
The rank order of the named entity definition.
Type: Integer
Required: No

## See Also
<a name="API_NamedEntityDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/NamedEntityDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/NamedEntityDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/NamedEntityDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
