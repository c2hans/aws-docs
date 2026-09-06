---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_ItemSource.html
---

# ItemSource
<a name="API_geospatial_ItemSource"></a>

The structure representing the items in the response for SearchRasterDataCollection.

## Contents
<a name="API_geospatial_ItemSource_Contents"></a>

 ** DateTime **   <a name="sagemaker-Type-geospatial_ItemSource-DateTime"></a>
The searchable date and time of the item, in UTC.
Type: Timestamp
Required: Yes

 ** Geometry **   <a name="sagemaker-Type-geospatial_ItemSource-Geometry"></a>
The item Geometry in GeoJson format.
Type: [Geometry](API_geospatial_Geometry.md) object
Required: Yes

 ** Id **   <a name="sagemaker-Type-geospatial_ItemSource-Id"></a>
A unique Id for the source item.
Type: String
Required: Yes

 ** Assets **   <a name="sagemaker-Type-geospatial_ItemSource-Assets"></a>
This is a dictionary of Asset Objects data associated with the Item that can be downloaded or streamed, each with a unique key.
Type: String to [AssetValue](API_geospatial_AssetValue.md) object map
Required: No

 ** Properties **   <a name="sagemaker-Type-geospatial_ItemSource-Properties"></a>
This field contains additional properties of the item.
Type: [Properties](API_geospatial_Properties.md) object
Required: No

## See Also
<a name="API_geospatial_ItemSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-geospatial-2020-05-27/ItemSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-geospatial-2020-05-27/ItemSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-geospatial-2020-05-27/ItemSource)
