---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_CopySnapshot.html
---

# CopySnapshot
<a name="API_CopySnapshot"></a>

Makes a copy of an existing snapshot.

## Request Syntax
<a name="API_CopySnapshot_RequestSyntax"></a>

```
{
   "KmsKeyId": "{{string}}",
   "SourceSnapshotName": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "TargetBucket": "{{string}}",
   "TargetSnapshotName": "{{string}}"
}
```

## Request Parameters
<a name="API_CopySnapshot_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [KmsKeyId](#API_CopySnapshot_RequestSyntax) **   <a name="MemoryDB-CopySnapshot-request-KmsKeyId"></a>
The ID of the KMS key used to encrypt the target snapshot.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

 ** [SourceSnapshotName](#API_CopySnapshot_RequestSyntax) **   <a name="MemoryDB-CopySnapshot-request-SourceSnapshotName"></a>
The name of an existing snapshot from which to make a copy.
Type: String
Required: Yes

 ** [Tags](#API_CopySnapshot_RequestSyntax) **   <a name="MemoryDB-CopySnapshot-request-Tags"></a>
A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Maximum number of 200 items.
Required: No

 ** [TargetBucket](#API_CopySnapshot_RequestSyntax) **   <a name="MemoryDB-CopySnapshot-request-TargetBucket"></a>
The Amazon S3 bucket to which the snapshot is exported. This parameter is used only when exporting a snapshot for external access. When using this parameter to export a snapshot, be sure MemoryDB has the needed permissions to this S3 bucket. For more information, see [Step 2: Grant MemoryDB Access to Your Amazon S3 Bucket](https://docs.aws.amazon.com/MemoryDB/latest/devguide/snapshots-exporting.html).
Type: String
Length Constraints: Maximum length of 255.
Pattern: `^[A-Za-z0-9._-]+$`
Required: No

 ** [TargetSnapshotName](#API_CopySnapshot_RequestSyntax) **   <a name="MemoryDB-CopySnapshot-request-TargetSnapshotName"></a>
A name for the snapshot copy. MemoryDB does not permit overwriting a snapshot, therefore this name must be unique within its context - MemoryDB or an Amazon S3 bucket if exporting. This value is stored as a lowercase string.
Type: String
Required: Yes

## Response Syntax
<a name="API_CopySnapshot_ResponseSyntax"></a>

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
<a name="API_CopySnapshot_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Snapshot](#API_CopySnapshot_ResponseSyntax) **   <a name="MemoryDB-CopySnapshot-response-Snapshot"></a>
Represents a copy of an entire cluster as of the time when the snapshot was taken.
Type: [Snapshot](API_Snapshot.md) object

## Errors
<a name="API_CopySnapshot_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterCombinationException **

HTTP Status Code: 400

 ** InvalidParameterValueException **

HTTP Status Code: 400

 ** InvalidSnapshotStateFault **

HTTP Status Code: 400

 ** ServiceLinkedRoleNotFoundFault **

HTTP Status Code: 400

 ** SnapshotAlreadyExistsFault **

HTTP Status Code: 400

 ** SnapshotNotFoundFault **

HTTP Status Code: 400

 ** SnapshotQuotaExceededFault **

HTTP Status Code: 400

 ** TagQuotaPerResourceExceeded **

HTTP Status Code: 400

## See Also
<a name="API_CopySnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/memorydb-2021-01-01/CopySnapshot)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/memorydb-2021-01-01/CopySnapshot)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/CopySnapshot)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/memorydb-2021-01-01/CopySnapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/CopySnapshot)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/memorydb-2021-01-01/CopySnapshot)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/memorydb-2021-01-01/CopySnapshot)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/memorydb-2021-01-01/CopySnapshot)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/memorydb-2021-01-01/CopySnapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/CopySnapshot)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MemoryDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query memorydb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
