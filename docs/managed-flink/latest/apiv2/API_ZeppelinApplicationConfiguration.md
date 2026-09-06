---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ZeppelinApplicationConfiguration.html
---

# ZeppelinApplicationConfiguration
<a name="API_ZeppelinApplicationConfiguration"></a>

The configuration of a Managed Service for Apache Flink Studio notebook.

## Contents
<a name="API_ZeppelinApplicationConfiguration_Contents"></a>

 ** CatalogConfiguration **   <a name="APIReference-Type-ZeppelinApplicationConfiguration-CatalogConfiguration"></a>
The Amazon Glue Data Catalog that you use in queries in a Managed Service for Apache Flink Studio notebook.
Type: [CatalogConfiguration](API_CatalogConfiguration.md) object
Required: No

 ** CustomArtifactsConfiguration **   <a name="APIReference-Type-ZeppelinApplicationConfiguration-CustomArtifactsConfiguration"></a>
Custom artifacts are dependency JARs and user-defined functions (UDF).
Type: Array of [CustomArtifactConfiguration](API_CustomArtifactConfiguration.md) objects
Array Members: Maximum number of 50 items.
Required: No

 ** DeployAsApplicationConfiguration **   <a name="APIReference-Type-ZeppelinApplicationConfiguration-DeployAsApplicationConfiguration"></a>
The information required to deploy a Managed Service for Apache Flink Studio notebook as an application with durable state.
Type: [DeployAsApplicationConfiguration](API_DeployAsApplicationConfiguration.md) object
Required: No

 ** MonitoringConfiguration **   <a name="APIReference-Type-ZeppelinApplicationConfiguration-MonitoringConfiguration"></a>
The monitoring configuration of a Managed Service for Apache Flink Studio notebook.
Type: [ZeppelinMonitoringConfiguration](API_ZeppelinMonitoringConfiguration.md) object
Required: No

## See Also
<a name="API_ZeppelinApplicationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/ZeppelinApplicationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/ZeppelinApplicationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/ZeppelinApplicationConfiguration)
