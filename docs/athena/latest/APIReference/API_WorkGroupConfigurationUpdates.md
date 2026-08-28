---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_WorkGroupConfigurationUpdates.html
---

# WorkGroupConfigurationUpdates
<a name="API_WorkGroupConfigurationUpdates"></a>

The configuration information that will be updated for this workgroup, which includes the location in Amazon S3 where query and calculation results are stored, the encryption option, if any, used for query results, whether the Amazon CloudWatch Metrics are enabled for the workgroup, whether the workgroup settings override the client-side settings, and the data usage limit for the amount of bytes scanned per query, if it is specified.

## Contents
<a name="API_WorkGroupConfigurationUpdates_Contents"></a>

 ** AdditionalConfiguration **   <a name="athena-Type-WorkGroupConfigurationUpdates-AdditionalConfiguration"></a>
Contains a user defined string in JSON format for a Spark-enabled workgroup.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** BytesScannedCutoffPerQuery **   <a name="athena-Type-WorkGroupConfigurationUpdates-BytesScannedCutoffPerQuery"></a>
The upper limit (cutoff) for the amount of bytes a single query in a workgroup is allowed to scan.
Type: Long
Valid Range: Minimum value of 10000000.
Required: No

 ** CustomerContentEncryptionConfiguration **   <a name="athena-Type-WorkGroupConfigurationUpdates-CustomerContentEncryptionConfiguration"></a>
Specifies the customer managed KMS key that is used to encrypt the user's data stores in Athena. When an AWS managed key is used, this value is null. This setting does not apply to Athena SQL workgroups.
Type: [CustomerContentEncryptionConfiguration](API_CustomerContentEncryptionConfiguration.md) object
Required: No

 ** EnableMinimumEncryptionConfiguration **   <a name="athena-Type-WorkGroupConfigurationUpdates-EnableMinimumEncryptionConfiguration"></a>
Enforces a minimal level of encryption for the workgroup for query and calculation results that are written to Amazon S3. When enabled, workgroup users can set encryption only to the minimum level set by the administrator or higher when they submit queries. This setting does not apply to Spark-enabled workgroups.
The `EnforceWorkGroupConfiguration` setting takes precedence over the `EnableMinimumEncryptionConfiguration` flag. This means that if `EnforceWorkGroupConfiguration` is true, the `EnableMinimumEncryptionConfiguration` flag is ignored, and the workgroup configuration for encryption is used.
Type: Boolean
Required: No

 ** EnforceWorkGroupConfiguration **   <a name="athena-Type-WorkGroupConfigurationUpdates-EnforceWorkGroupConfiguration"></a>
If set to "true", the settings for the workgroup override client-side settings. If set to "false" client-side settings are used. For more information, see [Workgroup Settings Override Client-Side Settings](https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html).
Type: Boolean
Required: No

 ** EngineConfiguration **   <a name="athena-Type-WorkGroupConfigurationUpdates-EngineConfiguration"></a>
The engine configuration for the workgroup, which includes the minimum/maximum number of Data Processing Units (DPU) that queries should use when running in provisioned capacity. If not specified, Athena uses default values (Default value for min is 4 and for max is Minimum of 124 and allocated DPUs).
To specify DPU values for PC queries the WG containing EngineConfiguration should have the following values: The name of the Classifications should be `athena-query-engine-properties`, with the only allowed properties as `max-dpu-count` and `min-dpu-count`.
Type: [EngineConfiguration](API_EngineConfiguration.md) object
Required: No

 ** EngineVersion **   <a name="athena-Type-WorkGroupConfigurationUpdates-EngineVersion"></a>
The engine version requested when a workgroup is updated. After the update, all queries on the workgroup run on the requested engine version. If no value was previously set, the default is Auto. Queries on the `AmazonAthenaPreviewFunctionality` workgroup run on the preview engine regardless of this setting.
Type: [EngineVersion](API_EngineVersion.md) object
Required: No

 ** ExecutionRole **   <a name="athena-Type-WorkGroupConfigurationUpdates-ExecutionRole"></a>
The ARN of the execution role used to access user resources for Spark sessions and Identity Center enabled workgroups. This property applies only to Spark enabled workgroups and Identity Center enabled workgroups.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+$`
Required: No

 ** ManagedQueryResultsConfigurationUpdates **   <a name="athena-Type-WorkGroupConfigurationUpdates-ManagedQueryResultsConfigurationUpdates"></a>
Updates configuration information for managed query results in the workgroup.
Type: [ManagedQueryResultsConfigurationUpdates](API_ManagedQueryResultsConfigurationUpdates.md) object
Required: No

 ** MonitoringConfiguration **   <a name="athena-Type-WorkGroupConfigurationUpdates-MonitoringConfiguration"></a>
Contains the configuration settings for managed log persistence, delivering logs to Amazon S3 buckets, Amazon CloudWatch log groups etc.
Type: [MonitoringConfiguration](API_MonitoringConfiguration.md) object
Required: No

 ** PublishCloudWatchMetricsEnabled **   <a name="athena-Type-WorkGroupConfigurationUpdates-PublishCloudWatchMetricsEnabled"></a>
Indicates whether this workgroup enables publishing metrics to Amazon CloudWatch.
Type: Boolean
Required: No

 ** QueryResultsS3AccessGrantsConfiguration **   <a name="athena-Type-WorkGroupConfigurationUpdates-QueryResultsS3AccessGrantsConfiguration"></a>
Specifies whether Amazon S3 access grants are enabled for query results.
Type: [QueryResultsS3AccessGrantsConfiguration](API_QueryResultsS3AccessGrantsConfiguration.md) object
Required: No

 ** RemoveBytesScannedCutoffPerQuery **   <a name="athena-Type-WorkGroupConfigurationUpdates-RemoveBytesScannedCutoffPerQuery"></a>
Indicates that the data usage control limit per query is removed. [WorkGroupConfiguration:BytesScannedCutoffPerQuery](API_WorkGroupConfiguration.md#athena-Type-WorkGroupConfiguration-BytesScannedCutoffPerQuery)
Type: Boolean
Required: No

 ** RemoveCustomerContentEncryptionConfiguration **   <a name="athena-Type-WorkGroupConfigurationUpdates-RemoveCustomerContentEncryptionConfiguration"></a>
Removes content encryption configuration from an Apache Spark-enabled Athena workgroup.
Type: Boolean
Required: No

 ** RequesterPaysEnabled **   <a name="athena-Type-WorkGroupConfigurationUpdates-RequesterPaysEnabled"></a>
If set to `true`, allows members assigned to a workgroup to specify Amazon S3 Requester Pays buckets in queries. If set to `false`, workgroup members cannot query data from Requester Pays buckets, and queries that retrieve data from Requester Pays buckets cause an error. The default is `false`. For more information about Requester Pays buckets, see [Requester Pays Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html) in the *Amazon Simple Storage Service Developer Guide*.
Type: Boolean
Required: No

 ** ResultConfigurationUpdates **   <a name="athena-Type-WorkGroupConfigurationUpdates-ResultConfigurationUpdates"></a>
The result configuration information about the queries in this workgroup that will be updated. Includes the updated results location and an updated option for encrypting query results.
Type: [ResultConfigurationUpdates](API_ResultConfigurationUpdates.md) object
Required: No

## See Also
<a name="API_WorkGroupConfigurationUpdates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/WorkGroupConfigurationUpdates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/WorkGroupConfigurationUpdates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/WorkGroupConfigurationUpdates)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
