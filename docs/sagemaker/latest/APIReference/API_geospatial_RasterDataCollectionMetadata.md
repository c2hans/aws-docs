---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_RasterDataCollectionMetadata.html
---

# RasterDataCollectionMetadata
<a name="API_geospatial_RasterDataCollectionMetadata"></a>

Response object containing details for a specific RasterDataCollection.

## Contents
<a name="API_geospatial_RasterDataCollectionMetadata_Contents"></a>

 ** Arn **   <a name="sagemaker-Type-geospatial_RasterDataCollectionMetadata-Arn"></a>
The Amazon Resource Name (ARN) of the raster data collection.
Type: String
Pattern: `arn:aws[a-z-]{0,12}:sagemaker-geospatial:[a-z0-9-]{1,25}:[0-9]{12}:raster-data-collection/(public|premium|user)/[a-z0-9]{12,}`
Required: Yes

 ** Description **   <a name="sagemaker-Type-geospatial_RasterDataCollectionMetadata-Description"></a>
A description of the raster data collection.
Type: String
Required: Yes

 ** Name **   <a name="sagemaker-Type-geospatial_RasterDataCollectionMetadata-Name"></a>
The name of the raster data collection.
Type: String
Required: Yes

 ** SupportedFilters **   <a name="sagemaker-Type-geospatial_RasterDataCollectionMetadata-SupportedFilters"></a>
The list of filters supported by the raster data collection.
Type: Array of [Filter](API_geospatial_Filter.md) objects
Required: Yes

 ** Type **   <a name="sagemaker-Type-geospatial_RasterDataCollectionMetadata-Type"></a>
The type of raster data collection.
Type: String
Valid Values: `PUBLIC | PREMIUM | USER`
Required: Yes

 ** DescriptionPageUrl **   <a name="sagemaker-Type-geospatial_RasterDataCollectionMetadata-DescriptionPageUrl"></a>
The description URL of the raster data collection.
Type: String
Required: No

 ** Tags **   <a name="sagemaker-Type-geospatial_RasterDataCollectionMetadata-Tags"></a>
Each tag consists of a key and a value.
Type: String to string map
Required: No

## See Also
<a name="API_geospatial_RasterDataCollectionMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-geospatial-2020-05-27/RasterDataCollectionMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-geospatial-2020-05-27/RasterDataCollectionMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-geospatial-2020-05-27/RasterDataCollectionMetadata)
