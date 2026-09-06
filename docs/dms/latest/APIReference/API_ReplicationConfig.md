---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_ReplicationConfig.html
---

# ReplicationConfig
<a name="API_ReplicationConfig"></a>

This object provides configuration information about a serverless replication.

## Contents
<a name="API_ReplicationConfig_Contents"></a>

 ** ComputeConfig **   <a name="DMS-Type-ReplicationConfig-ComputeConfig"></a>
Configuration parameters for provisioning an AWS DMS serverless replication.
Type: [ComputeConfig](API_ComputeConfig.md) object
Required: No

 ** IsReadOnly **   <a name="DMS-Type-ReplicationConfig-IsReadOnly"></a>
Indicates whether the replication configuration is read-only. When set to `true`, this replication configuration is managed by AWS DMS as part of a zero-ETL integration and cannot be modified or deleted directly. You can only modify or delete read-only replication configurations through their associated zero-ETL integration.
Type: Boolean
Required: No

 ** ReplicationConfigArn **   <a name="DMS-Type-ReplicationConfig-ReplicationConfigArn"></a>
The Amazon Resource Name (ARN) of this AWS DMS Serverless replication configuration.
Type: String
Required: No

 ** ReplicationConfigCreateTime **   <a name="DMS-Type-ReplicationConfig-ReplicationConfigCreateTime"></a>
The time the serverless replication config was created.
Type: Timestamp
Required: No

 ** ReplicationConfigIdentifier **   <a name="DMS-Type-ReplicationConfig-ReplicationConfigIdentifier"></a>
The identifier for the `ReplicationConfig` associated with the replication.
Type: String
Required: No

 ** ReplicationConfigUpdateTime **   <a name="DMS-Type-ReplicationConfig-ReplicationConfigUpdateTime"></a>
The time the serverless replication config was updated.
Type: Timestamp
Required: No

 ** ReplicationSettings **   <a name="DMS-Type-ReplicationConfig-ReplicationSettings"></a>
Configuration parameters for an AWS DMS serverless replication.
Type: String
Required: No

 ** ReplicationType **   <a name="DMS-Type-ReplicationConfig-ReplicationType"></a>
The type of the replication.
Type: String
Valid Values: `full-load | cdc | full-load-and-cdc`
Required: No

 ** SourceEndpointArn **   <a name="DMS-Type-ReplicationConfig-SourceEndpointArn"></a>
The Amazon Resource Name (ARN) of the source endpoint for this AWS DMS serverless replication configuration.
Type: String
Required: No

 ** SupplementalSettings **   <a name="DMS-Type-ReplicationConfig-SupplementalSettings"></a>
Additional parameters for an AWS DMS serverless replication.
Type: String
Required: No

 ** TableMappings **   <a name="DMS-Type-ReplicationConfig-TableMappings"></a>
Table mappings specified in the replication.
Type: String
Required: No

 ** TargetEndpointArn **   <a name="DMS-Type-ReplicationConfig-TargetEndpointArn"></a>
The Amazon Resource Name (ARN) of the target endpoint for this AWS DMS serverless replication configuration.
Type: String
Required: No

## See Also
<a name="API_ReplicationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/ReplicationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/ReplicationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/ReplicationConfig)
