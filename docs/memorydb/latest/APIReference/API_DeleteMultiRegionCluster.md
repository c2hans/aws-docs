---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DeleteMultiRegionCluster.html
---

# DeleteMultiRegionCluster
<a name="API_DeleteMultiRegionCluster"></a>

Deletes an existing multi-Region cluster.

## Request Syntax
<a name="API_DeleteMultiRegionCluster_RequestSyntax"></a>

```
{
   "MultiRegionClusterName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteMultiRegionCluster_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MultiRegionClusterName](#API_DeleteMultiRegionCluster_RequestSyntax) **   <a name="MemoryDB-DeleteMultiRegionCluster-request-MultiRegionClusterName"></a>
The name of the multi-Region cluster to be deleted.
Type: String
Required: Yes

## Response Syntax
<a name="API_DeleteMultiRegionCluster_ResponseSyntax"></a>

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
<a name="API_DeleteMultiRegionCluster_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MultiRegionCluster](#API_DeleteMultiRegionCluster_ResponseSyntax) **   <a name="MemoryDB-DeleteMultiRegionCluster-response-MultiRegionCluster"></a>
Details about the deleted multi-Region cluster.
Type: [MultiRegionCluster](API_MultiRegionCluster.md) object

## Errors
<a name="API_DeleteMultiRegionCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidMultiRegionClusterStateFault **
The requested operation cannot be performed on the multi-Region cluster in its current state.
HTTP Status Code: 400

 ** InvalidParameterValueException **

HTTP Status Code: 400

 ** MultiRegionClusterNotFoundFault **
The specified multi-Region cluster does not exist.
HTTP Status Code: 400

## See Also
<a name="API_DeleteMultiRegionCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/memorydb-2021-01-01/DeleteMultiRegionCluster)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/memorydb-2021-01-01/DeleteMultiRegionCluster)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/DeleteMultiRegionCluster)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/memorydb-2021-01-01/DeleteMultiRegionCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/DeleteMultiRegionCluster)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/memorydb-2021-01-01/DeleteMultiRegionCluster)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/memorydb-2021-01-01/DeleteMultiRegionCluster)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/memorydb-2021-01-01/DeleteMultiRegionCluster)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/memorydb-2021-01-01/DeleteMultiRegionCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/DeleteMultiRegionCluster)
