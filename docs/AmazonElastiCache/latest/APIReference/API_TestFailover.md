---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_TestFailover.html
---

# TestFailover
<a name="API_TestFailover"></a>

Represents the input of a `TestFailover` operation which tests automatic failover on a specified node group (called shard in the console) in a replication group (called cluster in the console).

This API is designed for testing the behavior of your application in case of ElastiCache failover. It is not designed to be an operational tool for initiating a failover to overcome a problem you may have with the cluster. Moreover, in certain conditions such as large-scale operational events, Amazon may block this API.

**Note the following**
+ A customer can use this operation to test automatic failover on up to 15 shards (called node groups in the ElastiCache API and Amazon CLI) in any rolling 24-hour period.
+ If calling this operation on shards in different clusters (called replication groups in the API and CLI), the calls can be made concurrently.

+ If calling this operation multiple times on different shards in the same Valkey or Redis OSS (cluster mode enabled) replication group, the first node replacement must complete before a subsequent call can be made.
+ To determine whether the node replacement is complete you can check Events using the Amazon ElastiCache console, the Amazon CLI, or the ElastiCache API. Look for the following automatic failover related events, listed here in order of occurrance:

  1. Replication group message: `Test Failover API called for node group <node-group-id>`

  1. Cache cluster message: `Failover from primary node <primary-node-id> to replica node <node-id> completed`

  1. Replication group message: `Failover from primary node <primary-node-id> to replica node <node-id> completed`

  1. Cache cluster message: `Recovering cache nodes <node-id>`

  1. Cache cluster message: `Finished recovery for cache nodes <node-id>`

  For more information see:
  +  [Viewing ElastiCache Events](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/ECEvents.Viewing.html) in the *ElastiCache User Guide*
  +  [DescribeEvents](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DescribeEvents.html) in the ElastiCache API Reference

Also see, [Testing Multi-AZ ](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoFailover.html#auto-failover-test) in the *ElastiCache User Guide*.

## Request Parameters
<a name="API_TestFailover_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** NodeGroupId **
The name of the node group (called shard in the console) in this replication group on which automatic failover is to be tested. You may test automatic failover on up to 15 node groups in any rolling 24-hour period.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4.
Pattern: `\d+`
Required: Yes

 ** ReplicationGroupId **
The name of the replication group (console: cluster) whose automatic failover is being tested by this operation.
Type: String
Required: Yes

## Response Elements
<a name="API_TestFailover_ResponseElements"></a>

The following element is returned by the service.

 ** ReplicationGroup **
Contains all of the attributes of a specific Valkey or Redis OSS replication group.
Type: [ReplicationGroup](API_ReplicationGroup.md) object

## Errors
<a name="API_TestFailover_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** APICallRateForCustomerExceeded **
The customer has exceeded the allowed rate of API calls.
HTTP Status Code: 400

 ** InvalidCacheClusterState **
The requested cluster is not in the `available` state.
HTTP Status Code: 400

 ** InvalidKMSKeyFault **
The KMS key supplied is not valid.
HTTP Status Code: 400

 ** InvalidParameterCombination **
Two or more incompatible parameters were specified.
 ** message **
Two or more parameters that must not be used together were used together.
HTTP Status Code: 400

 ** InvalidParameterValue **
The value for a parameter is invalid.
 ** message **
A parameter value is invalid.
HTTP Status Code: 400

 ** InvalidReplicationGroupState **
The requested replication group is not in the `available` state.
HTTP Status Code: 400

 ** NodeGroupNotFoundFault **
The node group specified by the `NodeGroupId` parameter could not be found. Please verify that the node group exists and that you spelled the `NodeGroupId` value correctly.
HTTP Status Code: 404

 ** ReplicationGroupNotFoundFault **
The specified replication group does not exist.
HTTP Status Code: 404

 ** TestFailoverNotAvailableFault **
The `TestFailover` action is not available.
HTTP Status Code: 400

## Examples
<a name="API_TestFailover_Examples"></a>

### Example
<a name="API_TestFailover_Example_1"></a>

The following example tests automatic failover on the Valkey or Redis OSS (cluster mode disabled) replication group (console: cluster) `redis00`. Since there is only one node group in Valkey or Redis OSS (cluster mode disabled) clusters, the *NodeGroupId* will always be `<cluster-name>-0001`.

#### Sample Request
<a name="API_TestFailover_Example_1_Request"></a>

```
https://elasticache.us-west-2.amazonaws.com/
   ?Action=TestFailover
   &NodeGroupId=redis00-0001
   &ReplicationGroupId=redis00
   &Version=2015-02-02
   &SignatureVersion=4
   &SignatureMethod=HmacSHA256
   &Timestamp=20170418T192317Z
   &X-Amz-Credential=<credential>
```

## See Also
<a name="API_TestFailover_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticache-2015-02-02/TestFailover)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticache-2015-02-02/TestFailover)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/TestFailover)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticache-2015-02-02/TestFailover)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/TestFailover)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticache-2015-02-02/TestFailover)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticache-2015-02-02/TestFailover)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticache-2015-02-02/TestFailover)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticache-2015-02-02/TestFailover)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/TestFailover)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
