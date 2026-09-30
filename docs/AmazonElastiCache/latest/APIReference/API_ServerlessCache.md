---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ServerlessCache.html
---

# ServerlessCache
<a name="API_ServerlessCache"></a>

The resource representing a serverless cache.

## Contents
<a name="API_ServerlessCache_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ARN **
The Amazon Resource Name (ARN) of the serverless cache.
Type: String
Required: No

 ** CacheUsageLimits **
The cache usage limit for the serverless cache.
Type: [CacheUsageLimits](API_CacheUsageLimits.md) object
Required: No

 ** ConnectionType **
The connection type for the serverless cache. Must be either `vpc` \| `public`. If not specified, defaults to `vpc`.
Type: String
Valid Values: `vpc | public`
Required: No

 ** CreateTime **
When the serverless cache was created.
Type: Timestamp
Required: No

 ** DailySnapshotTime **
The daily time that a cache snapshot will be created. Default is NULL, i.e. snapshots will not be created at a specific time on a daily basis. Available for Valkey, Redis OSS and Serverless Memcached only.
Type: String
Required: No

 ** Description **
A description of the serverless cache.
Type: String
Required: No

 ** Endpoint **
Represents the information required for client programs to connect to a cache node. This value is read-only.
Type: [Endpoint](API_Endpoint.md) object
Required: No

 ** Engine **
The engine the serverless cache is compatible with.
Type: String
Required: No

 ** FullEngineVersion **
The name and version number of the engine the serverless cache is compatible with.
Type: String
Required: No

 ** KmsKeyId **
The ID of the AWS Key Management Service (KMS) key that is used to encrypt data at rest in the serverless cache.
Type: String
Required: No

 ** MajorEngineVersion **
The version number of the engine the serverless cache is compatible with.
Type: String
Required: No

 ** NetworkType **
The type of IP address protocol used by the serverless cache. Must be either `ipv4` \| `ipv6` \| `dual_stack`. `ipv6` is only supported with IPv6-only subnets. If not specified, defaults to `ipv4`, unless all provided subnets are IPv6-only, in which case it defaults to `ipv6`.
Type: String
Valid Values: `ipv4 | ipv6 | dual_stack`
Required: No

 ** ReaderEndpoint **
Represents the information required for client programs to connect to a cache node. This value is read-only.
Type: [Endpoint](API_Endpoint.md) object
Required: No

 ** SecurityGroupIds.SecurityGroupId.N **
The IDs of the EC2 security groups associated with the serverless cache.
Type: Array of strings
Required: No

 ** ServerlessCacheName **
The unique identifier of the serverless cache.
Type: String
Required: No

 ** SnapshotRetentionLimit **
The number of days for which ElastiCache retains automatic snapshots before deleting them. Available for Valkey, Redis OSS and Serverless Memcached only. The maximum value allowed is 35 days.
Type: Integer
Required: No

 ** Status **
The current status of the serverless cache. The allowed values are CREATING, AVAILABLE, DELETING, CREATE-FAILED and MODIFYING.
Type: String
Required: No

 ** StorageEncryptionType **
Indicates the type of encryption for data stored at rest in the serverless cache. Serverless caches are always encrypted at rest. The value is `sse-elasticache` if an ElastiCache service-managed key is used, or `sse-kms` if a customer-managed KMS key is used.
Type: String
Valid Values: `none | sse-elasticache | sse-kms`
Required: No

 ** SubnetIds.SubnetId.N **
If no subnet IDs are given and your VPC is in us-west-1, then ElastiCache will select 2 default subnets across AZs in your VPC. For all other Regions, if no subnet IDs are given then ElastiCache will select 3 default subnets across AZs in your default VPC.
Type: Array of strings
Required: No

 ** UserGroupId **
The identifier of the user group associated with the serverless cache. Available for Valkey and Redis OSS only. Default is NULL.
Type: String
Required: No

## See Also
<a name="API_ServerlessCache_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/ServerlessCache)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/ServerlessCache)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/ServerlessCache)
