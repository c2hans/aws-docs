---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_VectorEnrichmentJobInputConfig.html
---

# VectorEnrichmentJobInputConfig
<a name="API_geospatial_VectorEnrichmentJobInputConfig"></a>

The input structure for the InputConfig in a VectorEnrichmentJob.

## Contents
<a name="API_geospatial_VectorEnrichmentJobInputConfig_Contents"></a>

 ** DataSourceConfig **   <a name="sagemaker-Type-geospatial_VectorEnrichmentJobInputConfig-DataSourceConfig"></a>
The input structure for the data source that represents the storage type of the input data objects.
Type: [VectorEnrichmentJobDataSourceConfigInput](API_geospatial_VectorEnrichmentJobDataSourceConfigInput.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** DocumentType **   <a name="sagemaker-Type-geospatial_VectorEnrichmentJobInputConfig-DocumentType"></a>
The input structure that defines the data source file type.
Type: String
Valid Values: `CSV`
Required: Yes

## See Also
<a name="API_geospatial_VectorEnrichmentJobInputConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-geospatial-2020-05-27/VectorEnrichmentJobInputConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-geospatial-2020-05-27/VectorEnrichmentJobInputConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-geospatial-2020-05-27/VectorEnrichmentJobInputConfig)
