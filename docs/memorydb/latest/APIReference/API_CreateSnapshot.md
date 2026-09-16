---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_CreateSnapshot.html
---

# CreateSnapshot
<a name="API_CreateSnapshot"></a>

Creates a copy of an entire cluster at a specific moment in time.

## Request Syntax
<a name="API_CreateSnapshot_RequestSyntax"></a>

```
{
   "ClusterName": "{{string}}",
   "KmsKeyId": "{{string}}",
   "SnapshotName": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateSnapshot_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterName](#API_CreateSnapshot_RequestSyntax) **   <a name="MemoryDB-CreateSnapshot-request-ClusterName"></a>
The snapshot is created from this cluster.
Type: String
Required: Yes

 ** [KmsKeyId](#API_CreateSnapshot_RequestSyntax) **   <a name="MemoryDB-CreateSnapshot-request-KmsKeyId"></a>
The ID of the KMS key used to encrypt the snapshot.
Type: String
Required: No

 ** [SnapshotName](#API_CreateSnapshot_RequestSyntax) **   <a name="MemoryDB-CreateSnapshot-request-SnapshotName"></a>
A name for the snapshot being created. This value is stored as a lowercase string.
Type: String
Required: Yes

 ** [Tags](#API_CreateSnapshot_RequestSyntax) **   <a name="MemoryDB-CreateSnapshot-request-Tags"></a>
A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreateSnapshot_ResponseSyntax"></a>

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
<a name="API_CreateSnapshot_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Snapshot](#API_CreateSnapshot_ResponseSyntax) **   <a name="MemoryDB-CreateSnapshot-response-Snapshot"></a>
The newly-created snapshot.
Type: [Snapshot](API_Snapshot.md) object

## Errors
<a name="API_CreateSnapshot_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterNotFoundFault **

HTTP Status Code: 400

 ** InvalidClusterStateFault **

HTTP Status Code: 400

 ** InvalidParameterCombinationException **

HTTP Status Code: 400

 ** InvalidParameterValueException **

HTTP Status Code: 400

 ** ServiceLinkedRoleNotFoundFault **

HTTP Status Code: 400

 ** SnapshotAlreadyExistsFault **

HTTP Status Code: 400

 ** SnapshotQuotaExceededFault **

HTTP Status Code: 400

 ** TagQuotaPerResourceExceeded **

HTTP Status Code: 400

## See Also
<a name="API_CreateSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/memorydb-2021-01-01/CreateSnapshot)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/memorydb-2021-01-01/CreateSnapshot)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/CreateSnapshot)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/memorydb-2021-01-01/CreateSnapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/CreateSnapshot)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/memorydb-2021-01-01/CreateSnapshot)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/memorydb-2021-01-01/CreateSnapshot)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/memorydb-2021-01-01/CreateSnapshot)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/memorydb-2021-01-01/CreateSnapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/CreateSnapshot)
