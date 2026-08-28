---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ApplicationConfiguration.html
---

# ApplicationConfiguration
<a name="API_ApplicationConfiguration"></a>

Specifies the creation parameters for a Managed Service for Apache Flink application.

## Contents
<a name="API_ApplicationConfiguration_Contents"></a>

 ** ApplicationCodeConfiguration **   <a name="APIReference-Type-ApplicationConfiguration-ApplicationCodeConfiguration"></a>
The code location and type parameters for a Managed Service for Apache Flink application.
Type: [ApplicationCodeConfiguration](API_ApplicationCodeConfiguration.md) object
Required: No

 ** ApplicationEncryptionConfiguration **   <a name="APIReference-Type-ApplicationConfiguration-ApplicationEncryptionConfiguration"></a>
The configuration to manage encryption at rest.
Type: [ApplicationEncryptionConfiguration](API_ApplicationEncryptionConfiguration.md) object
Required: No

 ** ApplicationSnapshotConfiguration **   <a name="APIReference-Type-ApplicationConfiguration-ApplicationSnapshotConfiguration"></a>
Describes whether snapshots are enabled for a Managed Service for Apache Flink application.
Type: [ApplicationSnapshotConfiguration](API_ApplicationSnapshotConfiguration.md) object
Required: No

 ** ApplicationSystemRollbackConfiguration **   <a name="APIReference-Type-ApplicationConfiguration-ApplicationSystemRollbackConfiguration"></a>
Describes whether system rollbacks are enabled for a Managed Service for Apache Flink application.
Type: [ApplicationSystemRollbackConfiguration](API_ApplicationSystemRollbackConfiguration.md) object
Required: No

 ** EnvironmentProperties **   <a name="APIReference-Type-ApplicationConfiguration-EnvironmentProperties"></a>
Describes execution properties for a Managed Service for Apache Flink application.
Type: [EnvironmentProperties](API_EnvironmentProperties.md) object
Required: No

 ** FlinkApplicationConfiguration **   <a name="APIReference-Type-ApplicationConfiguration-FlinkApplicationConfiguration"></a>
The creation and update parameters for a Managed Service for Apache Flink application.
Type: [FlinkApplicationConfiguration](API_FlinkApplicationConfiguration.md) object
Required: No

 ** SqlApplicationConfiguration **   <a name="APIReference-Type-ApplicationConfiguration-SqlApplicationConfiguration"></a>
The creation and update parameters for a SQL-based Kinesis Data Analytics application.
Type: [SqlApplicationConfiguration](API_SqlApplicationConfiguration.md) object
Required: No

 ** VpcConfigurations **   <a name="APIReference-Type-ApplicationConfiguration-VpcConfigurations"></a>
The array of descriptions of VPC configurations available to the application.
Type: Array of [VpcConfiguration](API_VpcConfiguration.md) objects
Required: No

 ** ZeppelinApplicationConfiguration **   <a name="APIReference-Type-ApplicationConfiguration-ZeppelinApplicationConfiguration"></a>
The configuration parameters for a Managed Service for Apache Flink Studio notebook.
Type: [ZeppelinApplicationConfiguration](API_ZeppelinApplicationConfiguration.md) object
Required: No

## See Also
<a name="API_ApplicationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/ApplicationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/ApplicationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/ApplicationConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Apache Flink (formerly Amazon Kinesis Data Analytics for Apache Flink). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
