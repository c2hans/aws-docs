---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_NestedFilter.html
---

# NestedFilter
<a name="API_NestedFilter"></a>

A `NestedFilter` filters data with a subset of data that is defined by the nested inner filter.

## Contents
<a name="API_NestedFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Column **   <a name="QS-Type-NestedFilter-Column"></a>
The column that the filter is applied to.
Type: [ColumnIdentifier](API_ColumnIdentifier.md) object
Required: Yes

 ** FilterId **   <a name="QS-Type-NestedFilter-FilterId"></a>
An identifier that uniquely identifies a filter within a dashboard, analysis, or template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** IncludeInnerSet **   <a name="QS-Type-NestedFilter-IncludeInnerSet"></a>
A boolean condition to include or exclude the subset that is defined by the values of the nested inner filter.
Type: Boolean
Required: Yes

 ** InnerFilter **   <a name="QS-Type-NestedFilter-InnerFilter"></a>
The `InnerFilter` defines the subset of data to be used with the `NestedFilter`.
Type: [InnerFilter](API_InnerFilter.md) object
Required: Yes

## See Also
<a name="API_NestedFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/NestedFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/NestedFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/NestedFilter)
