---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_GeoSpatialColumnGroup.html
---

# GeoSpatialColumnGroup
<a name="API_GeoSpatialColumnGroup"></a>

Geospatial column group that denotes a hierarchy.

## Contents
<a name="API_GeoSpatialColumnGroup_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Columns **   <a name="QS-Type-GeoSpatialColumnGroup-Columns"></a>
Columns in this hierarchy.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 16 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** Name **   <a name="QS-Type-GeoSpatialColumnGroup-Name"></a>
A display name for the hierarchy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** CountryCode **   <a name="QS-Type-GeoSpatialColumnGroup-CountryCode"></a>
Country code.
Type: String
Valid Values: `US`
Required: No

## See Also
<a name="API_GeoSpatialColumnGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/GeoSpatialColumnGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/GeoSpatialColumnGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/GeoSpatialColumnGroup)
