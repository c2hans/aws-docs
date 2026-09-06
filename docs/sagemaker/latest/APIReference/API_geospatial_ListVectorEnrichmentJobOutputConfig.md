---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_ListVectorEnrichmentJobOutputConfig.html
---

# ListVectorEnrichmentJobOutputConfig
<a name="API_geospatial_ListVectorEnrichmentJobOutputConfig"></a>

An object containing information about the output file.

## Contents
<a name="API_geospatial_ListVectorEnrichmentJobOutputConfig_Contents"></a>

 ** Arn **   <a name="sagemaker-Type-geospatial_ListVectorEnrichmentJobOutputConfig-Arn"></a>
The Amazon Resource Name (ARN) of the list of the Vector Enrichment jobs.
Type: String
Pattern: `arn:aws[a-z-]{0,12}:sagemaker-geospatial:[a-z0-9-]{1,25}:[0-9]{12}:vector-enrichment-job/[a-z0-9]{12,}`
Required: Yes

 ** CreationTime **   <a name="sagemaker-Type-geospatial_ListVectorEnrichmentJobOutputConfig-CreationTime"></a>
The creation time.
Type: Timestamp
Required: Yes

 ** DurationInSeconds **   <a name="sagemaker-Type-geospatial_ListVectorEnrichmentJobOutputConfig-DurationInSeconds"></a>
The duration of the session, in seconds.
Type: Integer
Required: Yes

 ** Name **   <a name="sagemaker-Type-geospatial_ListVectorEnrichmentJobOutputConfig-Name"></a>
The names of the Vector Enrichment jobs in the list.
Type: String
Required: Yes

 ** Status **   <a name="sagemaker-Type-geospatial_ListVectorEnrichmentJobOutputConfig-Status"></a>
The status of the Vector Enrichment jobs list.
Type: String
Valid Values: `INITIALIZING | IN_PROGRESS | STOPPING | STOPPED | COMPLETED | FAILED | DELETING | DELETED`
Required: Yes

 ** Type **   <a name="sagemaker-Type-geospatial_ListVectorEnrichmentJobOutputConfig-Type"></a>
The type of the list of Vector Enrichment jobs.
Type: String
Valid Values: `REVERSE_GEOCODING | MAP_MATCHING`
Required: Yes

 ** Tags **   <a name="sagemaker-Type-geospatial_ListVectorEnrichmentJobOutputConfig-Tags"></a>
Each tag consists of a key and a value.
Type: String to string map
Required: No

## See Also
<a name="API_geospatial_ListVectorEnrichmentJobOutputConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-geospatial-2020-05-27/ListVectorEnrichmentJobOutputConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-geospatial-2020-05-27/ListVectorEnrichmentJobOutputConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-geospatial-2020-05-27/ListVectorEnrichmentJobOutputConfig)
