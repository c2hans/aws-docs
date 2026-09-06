---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ColumnTag.html
---

# ColumnTag
<a name="API_ColumnTag"></a>

A tag for a column in a ` [TagColumnOperation](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TagColumnOperation.html) ` structure. This is a variant type structure. For this structure to be valid, only one of the attributes can be non-null.

## Contents
<a name="API_ColumnTag_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ColumnDescription **   <a name="QS-Type-ColumnTag-ColumnDescription"></a>
A description for a column.
Type: [ColumnDescription](API_ColumnDescription.md) object
Required: No

 ** ColumnGeographicRole **   <a name="QS-Type-ColumnTag-ColumnGeographicRole"></a>
A geospatial role for a column.
Type: String
Valid Values: `COUNTRY | STATE | COUNTY | CITY | POSTCODE | LONGITUDE | LATITUDE`
Required: No

## See Also
<a name="API_ColumnTag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ColumnTag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ColumnTag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ColumnTag)
