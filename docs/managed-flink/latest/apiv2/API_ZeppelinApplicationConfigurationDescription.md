---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ZeppelinApplicationConfigurationDescription.html
---

# ZeppelinApplicationConfigurationDescription
<a name="API_ZeppelinApplicationConfigurationDescription"></a>

The configuration of a Managed Service for Apache Flink Studio notebook.

## Contents
<a name="API_ZeppelinApplicationConfigurationDescription_Contents"></a>

 ** MonitoringConfigurationDescription **   <a name="APIReference-Type-ZeppelinApplicationConfigurationDescription-MonitoringConfigurationDescription"></a>
The monitoring configuration of a Managed Service for Apache Flink Studio notebook.
Type: [ZeppelinMonitoringConfigurationDescription](API_ZeppelinMonitoringConfigurationDescription.md) object
Required: Yes

 ** CatalogConfigurationDescription **   <a name="APIReference-Type-ZeppelinApplicationConfigurationDescription-CatalogConfigurationDescription"></a>
The Amazon Glue Data Catalog that is associated with the Managed Service for Apache Flink Studio notebook.
Type: [CatalogConfigurationDescription](API_CatalogConfigurationDescription.md) object
Required: No

 ** CustomArtifactsConfigurationDescription **   <a name="APIReference-Type-ZeppelinApplicationConfigurationDescription-CustomArtifactsConfigurationDescription"></a>
Custom artifacts are dependency JARs and user-defined functions (UDF).
Type: Array of [CustomArtifactConfigurationDescription](API_CustomArtifactConfigurationDescription.md) objects
Array Members: Maximum number of 50 items.
Required: No

 ** DeployAsApplicationConfigurationDescription **   <a name="APIReference-Type-ZeppelinApplicationConfigurationDescription-DeployAsApplicationConfigurationDescription"></a>
The parameters required to deploy a Managed Service for Apache Flink Studio notebook as an application with durable state.
Type: [DeployAsApplicationConfigurationDescription](API_DeployAsApplicationConfigurationDescription.md) object
Required: No

## See Also
<a name="API_ZeppelinApplicationConfigurationDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/ZeppelinApplicationConfigurationDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/ZeppelinApplicationConfigurationDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/ZeppelinApplicationConfigurationDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Apache Flink (formerly Amazon Kinesis Data Analytics for Apache Flink). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
