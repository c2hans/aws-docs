---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_CreateGlobalReplicationGroup.html
---

# CreateGlobalReplicationGroup
<a name="API_CreateGlobalReplicationGroup"></a>

Global Datastore offers fully managed, fast, reliable and secure cross-region replication. Using Global Datastore with Valkey or Redis OSS, you can create cross-region read replica clusters for ElastiCache to enable low-latency reads and disaster recovery across regions. For more information, see [Replication Across Regions Using Global Datastore](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Redis-Global-Datastore.html).
+ The **GlobalReplicationGroupIdSuffix** is the name of the Global datastore.
+ The **PrimaryReplicationGroupId** represents the name of the primary cluster that accepts writes and will replicate updates to the secondary cluster.

## Request Parameters
<a name="API_CreateGlobalReplicationGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** GlobalReplicationGroupIdSuffix **
The suffix name of a Global datastore. Amazon ElastiCache automatically applies a prefix to the Global datastore ID when it is created. Each Amazon Region has its own prefix. For instance, a Global datastore ID created in the US-West-1 region will begin with "dsdfu" along with the suffix name you provide. The suffix, combined with the auto-generated prefix, guarantees uniqueness of the Global datastore name across multiple regions.
For a full list of Amazon Regions and their respective Global datastore iD prefixes, see [Using the Amazon CLI with Global datastores ](http://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Redis-Global-Datastores-CLI.html).
Type: String
Required: Yes

 ** PrimaryReplicationGroupId **
The name of the primary cluster that accepts writes and will replicate updates to the secondary cluster. This value is stored as a lowercase string.
Type: String
Required: Yes

 ** GlobalReplicationGroupDescription **
Provides details of the Global datastore
Type: String
Required: No

## Response Elements
<a name="API_CreateGlobalReplicationGroup_ResponseElements"></a>

The following element is returned by the service.

 ** GlobalReplicationGroup **
Consists of a primary cluster that accepts writes and an associated secondary cluster that resides in a different Amazon region. The secondary cluster accepts only reads. The primary cluster automatically replicates updates to the secondary cluster.
+ The **GlobalReplicationGroupIdSuffix** represents the name of the Global datastore, which is what you use to associate a secondary cluster.
Type: [GlobalReplicationGroup](API_GlobalReplicationGroup.md) object

## Errors
<a name="API_CreateGlobalReplicationGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** GlobalReplicationGroupAlreadyExistsFault **
The Global datastore name already exists.
HTTP Status Code: 400

 ** InvalidParameterValue **
The value for a parameter is invalid.
 ** message **
A parameter value is invalid.
HTTP Status Code: 400

 ** InvalidReplicationGroupState **
The requested replication group is not in the `available` state.
HTTP Status Code: 400

 ** ReplicationGroupNotFoundFault **
The specified replication group does not exist.
HTTP Status Code: 404

 ** ServiceLinkedRoleNotFoundFault **
The specified service linked role (SLR) was not found.
HTTP Status Code: 400

## See Also
<a name="API_CreateGlobalReplicationGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticache-2015-02-02/CreateGlobalReplicationGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticache-2015-02-02/CreateGlobalReplicationGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/CreateGlobalReplicationGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticache-2015-02-02/CreateGlobalReplicationGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/CreateGlobalReplicationGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticache-2015-02-02/CreateGlobalReplicationGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticache-2015-02-02/CreateGlobalReplicationGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticache-2015-02-02/CreateGlobalReplicationGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticache-2015-02-02/CreateGlobalReplicationGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/CreateGlobalReplicationGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
