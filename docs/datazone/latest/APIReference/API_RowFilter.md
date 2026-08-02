---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_RowFilter.html
---

# RowFilter
<a name="API_RowFilter"></a>

The row filter.

## Contents
<a name="API_RowFilter_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** and **   <a name="datazone-Type-RowFilter-and"></a>
The 'and' clause of the row filter.
Type: Array of [RowFilter](#API_RowFilter) objects
Required: No

 ** expression **   <a name="datazone-Type-RowFilter-expression"></a>
The expression of the row filter.
Type: [RowFilterExpression](API_RowFilterExpression.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** or **   <a name="datazone-Type-RowFilter-or"></a>
The 'or' clause of the row filter.
Type: Array of [RowFilter](#API_RowFilter) objects
Required: No

## See Also
<a name="API_RowFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/RowFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/RowFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/RowFilter)
