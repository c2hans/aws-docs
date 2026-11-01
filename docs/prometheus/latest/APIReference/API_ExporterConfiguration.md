---
source_url: https://docs.aws.amazon.com/prometheus/latest/APIReference/API_ExporterConfiguration.html
---

# ExporterConfiguration
<a name="API_ExporterConfiguration"></a>

Contains the configuration for an exporter managed by the scraper.

## Contents
<a name="API_ExporterConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** kafkaConfiguration **   <a name="prometheus-Type-ExporterConfiguration-kafkaConfiguration"></a>
The configuration that the scraper uses to collect metrics from an Amazon MSK cluster through a managed Kafka exporter.
Type: [KafkaExporterConfiguration](API_KafkaExporterConfiguration.md) object
Required: No

 ** openSearchConfiguration **   <a name="prometheus-Type-ExporterConfiguration-openSearchConfiguration"></a>
The configuration that the scraper uses to export metrics to an Amazon OpenSearch Service domain.
Type: [OpenSearchExporterConfiguration](API_OpenSearchExporterConfiguration.md) object
Required: No

## See Also
<a name="API_ExporterConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/ExporterConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/ExporterConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/ExporterConfiguration)
