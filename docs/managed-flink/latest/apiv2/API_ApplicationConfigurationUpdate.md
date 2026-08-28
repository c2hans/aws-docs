---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ApplicationConfigurationUpdate.html
---

# ApplicationConfigurationUpdate
<a name="API_ApplicationConfigurationUpdate"></a>

Describes updates to an application's configuration.

## Contents
<a name="API_ApplicationConfigurationUpdate_Contents"></a>

 ** ApplicationCodeConfigurationUpdate **   <a name="APIReference-Type-ApplicationConfigurationUpdate-ApplicationCodeConfigurationUpdate"></a>
Describes updates to an application's code configuration.
Type: [ApplicationCodeConfigurationUpdate](API_ApplicationCodeConfigurationUpdate.md) object
Required: No

 ** ApplicationEncryptionConfigurationUpdate **   <a name="APIReference-Type-ApplicationConfigurationUpdate-ApplicationEncryptionConfigurationUpdate"></a>
Represents an update for encryption at rest configuration.
Type: [ApplicationEncryptionConfigurationUpdate](API_ApplicationEncryptionConfigurationUpdate.md) object
Required: No

 ** ApplicationSnapshotConfigurationUpdate **   <a name="APIReference-Type-ApplicationConfigurationUpdate-ApplicationSnapshotConfigurationUpdate"></a>
Describes whether snapshots are enabled for a Managed Service for Apache Flink application.
Type: [ApplicationSnapshotConfigurationUpdate](API_ApplicationSnapshotConfigurationUpdate.md) object
Required: No

 ** ApplicationSystemRollbackConfigurationUpdate **   <a name="APIReference-Type-ApplicationConfigurationUpdate-ApplicationSystemRollbackConfigurationUpdate"></a>
Describes whether system rollbacks are enabled for a Managed Service for Apache Flink application.
Type: [ApplicationSystemRollbackConfigurationUpdate](API_ApplicationSystemRollbackConfigurationUpdate.md) object
Required: No

 ** EnvironmentPropertyUpdates **   <a name="APIReference-Type-ApplicationConfigurationUpdate-EnvironmentPropertyUpdates"></a>
Describes updates to the environment properties for a Managed Service for Apache Flink application.
Type: [EnvironmentPropertyUpdates](API_EnvironmentPropertyUpdates.md) object
Required: No

 ** FlinkApplicationConfigurationUpdate **   <a name="APIReference-Type-ApplicationConfigurationUpdate-FlinkApplicationConfigurationUpdate"></a>
Describes updates to a Managed Service for Apache Flink application's configuration.
Type: [FlinkApplicationConfigurationUpdate](API_FlinkApplicationConfigurationUpdate.md) object
Required: No

 ** SqlApplicationConfigurationUpdate **   <a name="APIReference-Type-ApplicationConfigurationUpdate-SqlApplicationConfigurationUpdate"></a>
Describes updates to a SQL-based Kinesis Data Analytics application's configuration.
Type: [SqlApplicationConfigurationUpdate](API_SqlApplicationConfigurationUpdate.md) object
Required: No

 ** VpcConfigurationUpdates **   <a name="APIReference-Type-ApplicationConfigurationUpdate-VpcConfigurationUpdates"></a>
Updates to the array of descriptions of VPC configurations available to the application.
Type: Array of [VpcConfigurationUpdate](API_VpcConfigurationUpdate.md) objects
Required: No

 ** ZeppelinApplicationConfigurationUpdate **   <a name="APIReference-Type-ApplicationConfigurationUpdate-ZeppelinApplicationConfigurationUpdate"></a>
Updates to the configuration of a Managed Service for Apache Flink Studio notebook.
Type: [ZeppelinApplicationConfigurationUpdate](API_ZeppelinApplicationConfigurationUpdate.md) object
Required: No

## See Also
<a name="API_ApplicationConfigurationUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/ApplicationConfigurationUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/ApplicationConfigurationUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/ApplicationConfigurationUpdate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Apache Flink (formerly Amazon Kinesis Data Analytics for Apache Flink). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
