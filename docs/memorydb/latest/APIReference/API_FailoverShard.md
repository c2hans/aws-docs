---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_FailoverShard.html
---

# FailoverShard
<a name="API_FailoverShard"></a>

Used to failover a shard. This API is designed for testing the behavior of your application in case of MemoryDB failover. It is not designed to be used as a production-level tool for initiating a failover to overcome a problem you may have with the cluster. Moreover, in certain conditions such as large scale operational events, Amazon may block this API.

## Request Syntax
<a name="API_FailoverShard_RequestSyntax"></a>

```
{
   "ClusterName": "{{string}}",
   "ShardName": "{{string}}"
}
```

## Request Parameters
<a name="API_FailoverShard_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterName](#API_FailoverShard_RequestSyntax) **   <a name="MemoryDB-FailoverShard-request-ClusterName"></a>
The cluster being failed over.
Type: String
Required: Yes

 ** [ShardName](#API_FailoverShard_RequestSyntax) **   <a name="MemoryDB-FailoverShard-request-ShardName"></a>
The name of the shard.
Type: String
Required: Yes

## Response Syntax
<a name="API_FailoverShard_ResponseSyntax"></a>

```
{
   "Cluster": {
      "ACLName": "string",
      "ARN": "string",
      "AutoMinorVersionUpgrade": boolean,
      "AvailabilityMode": "string",
      "ClusterEndpoint": {
         "Address": "string",
         "Port": number
      },
      "DataTiering": "string",
      "Description": "string",
      "Engine": "string",
      "EnginePatchVersion": "string",
      "EngineVersion": "string",
      "IpDiscovery": "string",
      "KmsKeyId": "string",
      "MaintenanceWindow": "string",
      "MultiRegionClusterName": "string",
      "Name": "string",
      "NetworkType": "string",
      "NodeType": "string",
      "NumberOfShards": number,
      "ParameterGroupName": "string",
      "ParameterGroupStatus": "string",
      "PendingUpdates": {
         "ACLs": {
            "ACLToApply": "string"
         },
         "Resharding": {
            "SlotMigration": {
               "ProgressPercentage": number
            }
         },
         "ServiceUpdates": [
            {
               "ServiceUpdateName": "string",
               "Status": "string"
            }
         ]
      },
      "SecurityGroups": [
         {
            "SecurityGroupId": "string",
            "Status": "string"
         }
      ],
      "Shards": [
         {
            "Name": "string",
            "Nodes": [
               {
                  "AvailabilityZone": "string",
                  "CreateTime": number,
                  "Endpoint": {
                     "Address": "string",
                     "Port": number
                  },
                  "Name": "string",
                  "Status": "string"
               }
            ],
            "NumberOfNodes": number,
            "Slots": "string",
            "Status": "string"
         }
      ],
      "SnapshotRetentionLimit": number,
      "SnapshotWindow": "string",
      "SnsTopicArn": "string",
      "SnsTopicStatus": "string",
      "Status": "string",
      "SubnetGroupName": "string",
      "TLSEnabled": boolean
   }
}
```

## Response Elements
<a name="API_FailoverShard_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Cluster](#API_FailoverShard_ResponseSyntax) **   <a name="MemoryDB-FailoverShard-response-Cluster"></a>
The cluster being failed over.
Type: [Cluster](API_Cluster.md) object

## Errors
<a name="API_FailoverShard_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** APICallRateForCustomerExceededFault **

HTTP Status Code: 400

 ** ClusterNotFoundFault **

HTTP Status Code: 400

 ** InvalidClusterStateFault **

HTTP Status Code: 400

 ** InvalidKMSKeyFault **

HTTP Status Code: 400

 ** InvalidParameterCombinationException **

HTTP Status Code: 400

 ** InvalidParameterValueException **

HTTP Status Code: 400

 ** ShardNotFoundFault **

HTTP Status Code: 400

 ** TestFailoverNotAvailableFault **

HTTP Status Code: 400

## See Also
<a name="API_FailoverShard_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/memorydb-2021-01-01/FailoverShard)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/memorydb-2021-01-01/FailoverShard)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/FailoverShard)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/memorydb-2021-01-01/FailoverShard)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/FailoverShard)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/memorydb-2021-01-01/FailoverShard)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/memorydb-2021-01-01/FailoverShard)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/memorydb-2021-01-01/FailoverShard)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/memorydb-2021-01-01/FailoverShard)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/FailoverShard)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MemoryDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query memorydb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
