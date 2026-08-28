---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_WorkGroupConfiguration.html
---

# WorkGroupConfiguration
<a name="API_WorkGroupConfiguration"></a>

The configuration of the workgroup, which includes the location in Amazon S3 where query and calculation results are stored, the encryption option, if any, used for query and calculation results, whether the Amazon CloudWatch Metrics are enabled for the workgroup and whether workgroup settings override query settings, and the data usage limits for the amount of data scanned per query or per workgroup. The workgroup settings override is specified in `EnforceWorkGroupConfiguration` (true/false) in the `WorkGroupConfiguration`. See [WorkGroupConfiguration:EnforceWorkGroupConfiguration](#athena-Type-WorkGroupConfiguration-EnforceWorkGroupConfiguration).

## Contents
<a name="API_WorkGroupConfiguration_Contents"></a>

 ** AdditionalConfiguration **   <a name="athena-Type-WorkGroupConfiguration-AdditionalConfiguration"></a>
Specifies a user defined JSON string that is passed to the notebook engine.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** BytesScannedCutoffPerQuery **   <a name="athena-Type-WorkGroupConfiguration-BytesScannedCutoffPerQuery"></a>
The upper data usage limit (cutoff) for the amount of bytes a single query in a workgroup is allowed to scan.
Type: Long
Valid Range: Minimum value of 10000000.
Required: No

 ** CustomerContentEncryptionConfiguration **   <a name="athena-Type-WorkGroupConfiguration-CustomerContentEncryptionConfiguration"></a>
Specifies the KMS key that is used to encrypt the user's data stores in Athena. This setting does not apply to Athena SQL workgroups.
Type: [CustomerContentEncryptionConfiguration](API_CustomerContentEncryptionConfiguration.md) object
Required: No

 ** EnableMinimumEncryptionConfiguration **   <a name="athena-Type-WorkGroupConfiguration-EnableMinimumEncryptionConfiguration"></a>
Enforces a minimal level of encryption for the workgroup for query and calculation results that are written to Amazon S3. When enabled, workgroup users can set encryption only to the minimum level set by the administrator or higher when they submit queries.
The `EnforceWorkGroupConfiguration` setting takes precedence over the `EnableMinimumEncryptionConfiguration` flag. This means that if `EnforceWorkGroupConfiguration` is true, the `EnableMinimumEncryptionConfiguration` flag is ignored, and the workgroup configuration for encryption is used.
Type: Boolean
Required: No

 ** EnforceWorkGroupConfiguration **   <a name="athena-Type-WorkGroupConfiguration-EnforceWorkGroupConfiguration"></a>
If set to "true", the settings for the workgroup override client-side settings. If set to "false", client-side settings are used. This property is not required for Apache Spark enabled workgroups. For more information, see [Workgroup Settings Override Client-Side Settings](https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html).
Type: Boolean
Required: No

 ** EngineConfiguration **   <a name="athena-Type-WorkGroupConfiguration-EngineConfiguration"></a>
The engine configuration for the workgroup, which includes the minimum/maximum number of Data Processing Units (DPU) that queries should use when running in provisioned capacity. If not specified, Athena uses default values (Default value for min is 4 and for max is Minimum of 124 and allocated DPUs).
To specify DPU values for PC queries the WG containing EngineConfiguration should have the following values: The name of the Classifications should be `athena-query-engine-properties`, with the only allowed properties as `max-dpu-count` and `min-dpu-count`.
Type: [EngineConfiguration](API_EngineConfiguration.md) object
Required: No

 ** EngineVersion **   <a name="athena-Type-WorkGroupConfiguration-EngineVersion"></a>
The engine version that all queries running on the workgroup use. Queries on the `AmazonAthenaPreviewFunctionality` workgroup run on the preview engine regardless of this setting.
Type: [EngineVersion](API_EngineVersion.md) object
Required: No

 ** ExecutionRole **   <a name="athena-Type-WorkGroupConfiguration-ExecutionRole"></a>
The ARN of the execution role used to access user resources for Spark sessions and IAM Identity Center enabled workgroups. This property applies only to Spark enabled workgroups and IAM Identity Center enabled workgroups. The property is required for IAM Identity Center enabled workgroups.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+$`
Required: No

 ** IdentityCenterConfiguration **   <a name="athena-Type-WorkGroupConfiguration-IdentityCenterConfiguration"></a>
Specifies whether the workgroup is IAM Identity Center supported.
Type: [IdentityCenterConfiguration](API_IdentityCenterConfiguration.md) object
Required: No

 ** ManagedQueryResultsConfiguration **   <a name="athena-Type-WorkGroupConfiguration-ManagedQueryResultsConfiguration"></a>
 The configuration for storing results in Athena owned storage, which includes whether this feature is enabled; whether encryption configuration, if any, is used for encrypting query results.
Type: [ManagedQueryResultsConfiguration](API_ManagedQueryResultsConfiguration.md) object
Required: No

 ** MonitoringConfiguration **   <a name="athena-Type-WorkGroupConfiguration-MonitoringConfiguration"></a>
Contains the configuration settings for managed log persistence, delivering logs to Amazon S3 buckets, Amazon CloudWatch log groups etc.
Type: [MonitoringConfiguration](API_MonitoringConfiguration.md) object
Required: No

 ** PublishCloudWatchMetricsEnabled **   <a name="athena-Type-WorkGroupConfiguration-PublishCloudWatchMetricsEnabled"></a>
Indicates that the Amazon CloudWatch metrics are enabled for the workgroup.
Type: Boolean
Required: No

 ** QueryResultsS3AccessGrantsConfiguration **   <a name="athena-Type-WorkGroupConfiguration-QueryResultsS3AccessGrantsConfiguration"></a>
Specifies whether Amazon S3 access grants are enabled for query results.
Type: [QueryResultsS3AccessGrantsConfiguration](API_QueryResultsS3AccessGrantsConfiguration.md) object
Required: No

 ** RequesterPaysEnabled **   <a name="athena-Type-WorkGroupConfiguration-RequesterPaysEnabled"></a>
If set to `true`, allows members assigned to a workgroup to reference Amazon S3 Requester Pays buckets in queries. If set to `false`, workgroup members cannot query data from Requester Pays buckets, and queries that retrieve data from Requester Pays buckets cause an error. The default is `false`. For more information about Requester Pays buckets, see [Requester Pays Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html) in the *Amazon Simple Storage Service Developer Guide*.
Type: Boolean
Required: No

 ** ResultConfiguration **   <a name="athena-Type-WorkGroupConfiguration-ResultConfiguration"></a>
The configuration for the workgroup, which includes the location in Amazon S3 where query and calculation results are stored and the encryption option, if any, used for query and calculation results. To run the query, you must specify the query results location using one of the ways: either in the workgroup using this setting, or for individual queries (client-side), using [ResultConfiguration:OutputLocation](API_ResultConfiguration.md#athena-Type-ResultConfiguration-OutputLocation). If none of them is set, Athena issues an error that no output location is provided.
Type: [ResultConfiguration](API_ResultConfiguration.md) object
Required: No

## See Also
<a name="API_WorkGroupConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/WorkGroupConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/WorkGroupConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/WorkGroupConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
