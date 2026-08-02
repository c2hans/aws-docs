---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ZeppelinApplicationConfigurationUpdate.html
---

# ZeppelinApplicationConfigurationUpdate
<a name="API_ZeppelinApplicationConfigurationUpdate"></a>

Updates to the configuration of Managed Service for Apache Flink Studio notebook.

## Contents
<a name="API_ZeppelinApplicationConfigurationUpdate_Contents"></a>

 ** CatalogConfigurationUpdate **   <a name="APIReference-Type-ZeppelinApplicationConfigurationUpdate-CatalogConfigurationUpdate"></a>
Updates to the configuration of the Amazon Glue Data Catalog that is associated with the Managed Service for Apache Flink Studio notebook.
Type: [CatalogConfigurationUpdate](API_CatalogConfigurationUpdate.md) object
Required: No

 ** CustomArtifactsConfigurationUpdate **   <a name="APIReference-Type-ZeppelinApplicationConfigurationUpdate-CustomArtifactsConfigurationUpdate"></a>
Updates to the customer artifacts. Custom artifacts are dependency JAR files and user-defined functions (UDF).
Type: Array of [CustomArtifactConfiguration](API_CustomArtifactConfiguration.md) objects
Array Members: Maximum number of 50 items.
Required: No

 ** DeployAsApplicationConfigurationUpdate **   <a name="APIReference-Type-ZeppelinApplicationConfigurationUpdate-DeployAsApplicationConfigurationUpdate"></a>
Type: [DeployAsApplicationConfigurationUpdate](API_DeployAsApplicationConfigurationUpdate.md) object
Required: No

 ** MonitoringConfigurationUpdate **   <a name="APIReference-Type-ZeppelinApplicationConfigurationUpdate-MonitoringConfigurationUpdate"></a>
Updates to the monitoring configuration of a Managed Service for Apache Flink Studio notebook.
Type: [ZeppelinMonitoringConfigurationUpdate](API_ZeppelinMonitoringConfigurationUpdate.md) object
Required: No

## See Also
<a name="API_ZeppelinApplicationConfigurationUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/ZeppelinApplicationConfigurationUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/ZeppelinApplicationConfigurationUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/ZeppelinApplicationConfigurationUpdate)
