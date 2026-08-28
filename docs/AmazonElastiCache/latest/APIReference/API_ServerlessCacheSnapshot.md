---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ServerlessCacheSnapshot.html
---

# ServerlessCacheSnapshot
<a name="API_ServerlessCacheSnapshot"></a>

The resource representing a serverless cache snapshot. Available for Valkey, Redis OSS and Serverless Memcached only.

## Contents
<a name="API_ServerlessCacheSnapshot_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ARN **
The Amazon Resource Name (ARN) of a serverless cache snapshot. Available for Valkey, Redis OSS and Serverless Memcached only.
Type: String
Required: No

 ** BytesUsedForCache **
The total size of a serverless cache snapshot, in bytes. Available for Valkey, Redis OSS and Serverless Memcached only.
Type: String
Required: No

 ** CreateTime **
The date and time that the source serverless cache's metadata and cache data set was obtained for the snapshot. Available for Valkey, Redis OSS and Serverless Memcached only.
Type: Timestamp
Required: No

 ** ExpiryTime **
The time that the serverless cache snapshot will expire. Available for Valkey, Redis OSS and Serverless Memcached only.
Type: Timestamp
Required: No

 ** KmsKeyId **
The ID of the AWS Key Management Service (KMS) key of a serverless cache snapshot. Available for Valkey, Redis OSS and Serverless Memcached only.
Type: String
Required: No

 ** ServerlessCacheConfiguration **
The configuration of the serverless cache, at the time the snapshot was taken. Available for Valkey, Redis OSS and Serverless Memcached only.
Type: [ServerlessCacheConfiguration](API_ServerlessCacheConfiguration.md) object
Required: No

 ** ServerlessCacheSnapshotName **
The identifier of a serverless cache snapshot. Available for Valkey, Redis OSS and Serverless Memcached only.
Type: String
Required: No

 ** SnapshotType **
The type of snapshot of serverless cache. Available for Valkey, Redis OSS and Serverless Memcached only.
Type: String
Required: No

 ** Status **
The current status of the serverless cache. Available for Valkey, Redis OSS and Serverless Memcached only.
Type: String
Required: No

## See Also
<a name="API_ServerlessCacheSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/ServerlessCacheSnapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/ServerlessCacheSnapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/ServerlessCacheSnapshot)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
