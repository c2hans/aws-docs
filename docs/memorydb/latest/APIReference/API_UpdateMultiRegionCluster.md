---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_UpdateMultiRegionCluster.html
---

# UpdateMultiRegionCluster
<a name="API_UpdateMultiRegionCluster"></a>

Updates the configuration of an existing multi-Region cluster.

## Request Syntax
<a name="API_UpdateMultiRegionCluster_RequestSyntax"></a>

```
{
   "Description": "{{string}}",
   "EngineVersion": "{{string}}",
   "MultiRegionClusterName": "{{string}}",
   "MultiRegionParameterGroupName": "{{string}}",
   "NodeType": "{{string}}",
   "ShardConfiguration": {
      "ShardCount": {{number}}
   },
   "UpdateStrategy": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateMultiRegionCluster_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateMultiRegionCluster_RequestSyntax) **   <a name="MemoryDB-UpdateMultiRegionCluster-request-Description"></a>
A new description for the multi-Region cluster.
Type: String
Required: No

 ** [EngineVersion](#API_UpdateMultiRegionCluster_RequestSyntax) **   <a name="MemoryDB-UpdateMultiRegionCluster-request-EngineVersion"></a>
The new engine version to be used for the multi-Region cluster.
Type: String
Required: No

 ** [MultiRegionClusterName](#API_UpdateMultiRegionCluster_RequestSyntax) **   <a name="MemoryDB-UpdateMultiRegionCluster-request-MultiRegionClusterName"></a>
The name of the multi-Region cluster to be updated.
Type: String
Required: Yes

 ** [MultiRegionParameterGroupName](#API_UpdateMultiRegionCluster_RequestSyntax) **   <a name="MemoryDB-UpdateMultiRegionCluster-request-MultiRegionParameterGroupName"></a>
The new multi-Region parameter group to be associated with the cluster.
Type: String
Required: No

 ** [NodeType](#API_UpdateMultiRegionCluster_RequestSyntax) **   <a name="MemoryDB-UpdateMultiRegionCluster-request-NodeType"></a>
The new node type to be used for the multi-Region cluster.
Type: String
Required: No

 ** [ShardConfiguration](#API_UpdateMultiRegionCluster_RequestSyntax) **   <a name="MemoryDB-UpdateMultiRegionCluster-request-ShardConfiguration"></a>
A request to configure the sharding properties of a cluster
Type: [ShardConfigurationRequest](API_ShardConfigurationRequest.md) object
Required: No

 ** [UpdateStrategy](#API_UpdateMultiRegionCluster_RequestSyntax) **   <a name="MemoryDB-UpdateMultiRegionCluster-request-UpdateStrategy"></a>
The strategy to use for the update operation. Supported values are "coordinated" or "uncoordinated".
Type: String
Valid Values: `coordinated | uncoordinated`
Required: No

## Response Syntax
<a name="API_UpdateMultiRegionCluster_ResponseSyntax"></a>

```
{
   "MultiRegionCluster": {
      "ARN": "string",
      "Clusters": [
         {
            "ARN": "string",
            "ClusterName": "string",
            "Region": "string",
            "Status": "string"
         }
      ],
      "Description": "string",
      "Engine": "string",
      "EngineVersion": "string",
      "MultiRegionClusterName": "string",
      "MultiRegionParameterGroupName": "string",
      "NodeType": "string",
      "NumberOfShards": number,
      "Status": "string",
      "TLSEnabled": boolean
   }
}
```

## Response Elements
<a name="API_UpdateMultiRegionCluster_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MultiRegionCluster](#API_UpdateMultiRegionCluster_ResponseSyntax) **   <a name="MemoryDB-UpdateMultiRegionCluster-response-MultiRegionCluster"></a>
The status of updating the multi-Region cluster.
Type: [MultiRegionCluster](API_MultiRegionCluster.md) object

## Errors
<a name="API_UpdateMultiRegionCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidMultiRegionClusterStateFault **
The requested operation cannot be performed on the multi-Region cluster in its current state.
HTTP Status Code: 400

 ** InvalidParameterCombinationException **

HTTP Status Code: 400

 ** InvalidParameterValueException **

HTTP Status Code: 400

 ** MultiRegionClusterNotFoundFault **
The specified multi-Region cluster does not exist.
HTTP Status Code: 400

 ** MultiRegionParameterGroupNotFoundFault **
The specified multi-Region parameter group does not exist.
HTTP Status Code: 400

## See Also
<a name="API_UpdateMultiRegionCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/memorydb-2021-01-01/UpdateMultiRegionCluster)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/memorydb-2021-01-01/UpdateMultiRegionCluster)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/UpdateMultiRegionCluster)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/memorydb-2021-01-01/UpdateMultiRegionCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/UpdateMultiRegionCluster)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/memorydb-2021-01-01/UpdateMultiRegionCluster)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/memorydb-2021-01-01/UpdateMultiRegionCluster)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/memorydb-2021-01-01/UpdateMultiRegionCluster)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/memorydb-2021-01-01/UpdateMultiRegionCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/UpdateMultiRegionCluster)
