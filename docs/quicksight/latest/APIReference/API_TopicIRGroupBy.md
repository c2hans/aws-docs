---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TopicIRGroupBy.html
---

# TopicIRGroupBy
<a name="API_TopicIRGroupBy"></a>

The definition for a `TopicIRGroupBy`.

## Contents
<a name="API_TopicIRGroupBy_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DisplayFormat **   <a name="QS-Type-TopicIRGroupBy-DisplayFormat"></a>
The display format for the `TopicIRGroupBy`.
Type: String
Valid Values: `AUTO | PERCENT | CURRENCY | NUMBER | DATE | STRING`
Required: No

 ** DisplayFormatOptions **   <a name="QS-Type-TopicIRGroupBy-DisplayFormatOptions"></a>
A structure that represents additional options for display formatting.
Type: [DisplayFormatOptions](API_DisplayFormatOptions.md) object
Required: No

 ** FieldName **   <a name="QS-Type-TopicIRGroupBy-FieldName"></a>
The field name for the `TopicIRGroupBy`.
Type: [Identifier](API_Identifier.md) object
Required: No

 ** NamedEntity **   <a name="QS-Type-TopicIRGroupBy-NamedEntity"></a>
The named entity for the `TopicIRGroupBy`.
Type: [NamedEntityRef](API_NamedEntityRef.md) object
Required: No

 ** Sort **   <a name="QS-Type-TopicIRGroupBy-Sort"></a>
The sort for the `TopicIRGroupBy`.
Type: [TopicSortClause](API_TopicSortClause.md) object
Required: No

 ** TimeGranularity **   <a name="QS-Type-TopicIRGroupBy-TimeGranularity"></a>
The time granularity for the `TopicIRGroupBy`.
Type: String
Valid Values: `SECOND | MINUTE | HOUR | DAY | WEEK | MONTH | QUARTER | YEAR`
Required: No

## See Also
<a name="API_TopicIRGroupBy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TopicIRGroupBy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TopicIRGroupBy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TopicIRGroupBy)
