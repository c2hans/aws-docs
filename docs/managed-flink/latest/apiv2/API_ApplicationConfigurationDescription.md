---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ApplicationConfigurationDescription.html
---

# ApplicationConfigurationDescription
<a name="API_ApplicationConfigurationDescription"></a>

Describes details about the application code and starting parameters for a Managed Service for Apache Flink application.

## Contents
<a name="API_ApplicationConfigurationDescription_Contents"></a>

 ** ApplicationCodeConfigurationDescription **   <a name="APIReference-Type-ApplicationConfigurationDescription-ApplicationCodeConfigurationDescription"></a>
The details about the application code for a Managed Service for Apache Flink application.
Type: [ApplicationCodeConfigurationDescription](API_ApplicationCodeConfigurationDescription.md) object
Required: No

 ** ApplicationEncryptionConfigurationDescription **   <a name="APIReference-Type-ApplicationConfigurationDescription-ApplicationEncryptionConfigurationDescription"></a>
Describes the encryption at rest configuration.
Type: [ApplicationEncryptionConfigurationDescription](API_ApplicationEncryptionConfigurationDescription.md) object
Required: No

 ** ApplicationSnapshotConfigurationDescription **   <a name="APIReference-Type-ApplicationConfigurationDescription-ApplicationSnapshotConfigurationDescription"></a>
Describes whether snapshots are enabled for a Managed Service for Apache Flink application.
Type: [ApplicationSnapshotConfigurationDescription](API_ApplicationSnapshotConfigurationDescription.md) object
Required: No

 ** ApplicationSystemRollbackConfigurationDescription **   <a name="APIReference-Type-ApplicationConfigurationDescription-ApplicationSystemRollbackConfigurationDescription"></a>
Describes whether system rollbacks are enabled for a Managed Service for Apache Flink application.
Type: [ApplicationSystemRollbackConfigurationDescription](API_ApplicationSystemRollbackConfigurationDescription.md) object
Required: No

 ** EnvironmentPropertyDescriptions **   <a name="APIReference-Type-ApplicationConfigurationDescription-EnvironmentPropertyDescriptions"></a>
Describes execution properties for a Managed Service for Apache Flink application.
Type: [EnvironmentPropertyDescriptions](API_EnvironmentPropertyDescriptions.md) object
Required: No

 ** FlinkApplicationConfigurationDescription **   <a name="APIReference-Type-ApplicationConfigurationDescription-FlinkApplicationConfigurationDescription"></a>
The details about a Managed Service for Apache Flink application.
Type: [FlinkApplicationConfigurationDescription](API_FlinkApplicationConfigurationDescription.md) object
Required: No

 ** RunConfigurationDescription **   <a name="APIReference-Type-ApplicationConfigurationDescription-RunConfigurationDescription"></a>
The details about the starting properties for a Managed Service for Apache Flink application.
Type: [RunConfigurationDescription](API_RunConfigurationDescription.md) object
Required: No

 ** SqlApplicationConfigurationDescription **   <a name="APIReference-Type-ApplicationConfigurationDescription-SqlApplicationConfigurationDescription"></a>
The details about inputs, outputs, and reference data sources for a SQL-based Kinesis Data Analytics application.
Type: [SqlApplicationConfigurationDescription](API_SqlApplicationConfigurationDescription.md) object
Required: No

 ** VpcConfigurationDescriptions **   <a name="APIReference-Type-ApplicationConfigurationDescription-VpcConfigurationDescriptions"></a>
The array of descriptions of VPC configurations available to the application.
Type: Array of [VpcConfigurationDescription](API_VpcConfigurationDescription.md) objects
Required: No

 ** ZeppelinApplicationConfigurationDescription **   <a name="APIReference-Type-ApplicationConfigurationDescription-ZeppelinApplicationConfigurationDescription"></a>
The configuration parameters for a Managed Service for Apache Flink Studio notebook.
Type: [ZeppelinApplicationConfigurationDescription](API_ZeppelinApplicationConfigurationDescription.md) object
Required: No

## See Also
<a name="API_ApplicationConfigurationDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/ApplicationConfigurationDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/ApplicationConfigurationDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/ApplicationConfigurationDescription)
