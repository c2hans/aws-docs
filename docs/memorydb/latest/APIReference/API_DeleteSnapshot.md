---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DeleteSnapshot.html
---

# DeleteSnapshot
<a name="API_DeleteSnapshot"></a>

Deletes an existing snapshot. When you receive a successful response from this operation, MemoryDB immediately begins deleting the snapshot; you cannot cancel or revert this operation.

## Request Syntax
<a name="API_DeleteSnapshot_RequestSyntax"></a>

```
{
   "SnapshotName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteSnapshot_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [SnapshotName](#API_DeleteSnapshot_RequestSyntax) **   <a name="MemoryDB-DeleteSnapshot-request-SnapshotName"></a>
The name of the snapshot to delete.
Type: String
Required: Yes

## Response Syntax
<a name="API_DeleteSnapshot_ResponseSyntax"></a>

```
{
   "Snapshot": {
      "ARN": "string",
      "ClusterConfiguration": {
         "Description": "string",
         "Engine": "string",
         "EngineVersion": "string",
         "MaintenanceWindow": "string",
         "MultiRegionClusterName": "string",
         "MultiRegionParameterGroupName": "string",
         "Name": "string",
         "NodeType": "string",
         "NumShards": number,
         "ParameterGroupName": "string",
         "Port": number,
         "Shards": [
            {
               "Configuration": {
                  "ReplicaCount": number,
                  "Slots": "string"
               },
               "Name": "string",
               "Size": "string",
               "SnapshotCreationTime": number
            }
         ],
         "SnapshotRetentionLimit": number,
         "SnapshotWindow": "string",
         "SubnetGroupName": "string",
         "TopicArn": "string",
         "VpcId": "string"
      },
      "DataTiering": "string",
      "KmsKeyId": "string",
      "Name": "string",
      "Source": "string",
      "Status": "string"
   }
}
```

## Response Elements
<a name="API_DeleteSnapshot_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Snapshot](#API_DeleteSnapshot_ResponseSyntax) **   <a name="MemoryDB-DeleteSnapshot-response-Snapshot"></a>
The snapshot object that has been deleted.
Type: [Snapshot](API_Snapshot.md) object

## Errors
<a name="API_DeleteSnapshot_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterCombinationException **

HTTP Status Code: 400

 ** InvalidParameterValueException **

HTTP Status Code: 400

 ** InvalidSnapshotStateFault **

HTTP Status Code: 400

 ** ServiceLinkedRoleNotFoundFault **

HTTP Status Code: 400

 ** SnapshotNotFoundFault **

HTTP Status Code: 400

## See Also
<a name="API_DeleteSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/memorydb-2021-01-01/DeleteSnapshot)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/memorydb-2021-01-01/DeleteSnapshot)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/DeleteSnapshot)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/memorydb-2021-01-01/DeleteSnapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/DeleteSnapshot)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/memorydb-2021-01-01/DeleteSnapshot)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/memorydb-2021-01-01/DeleteSnapshot)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/memorydb-2021-01-01/DeleteSnapshot)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/memorydb-2021-01-01/DeleteSnapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/DeleteSnapshot)
