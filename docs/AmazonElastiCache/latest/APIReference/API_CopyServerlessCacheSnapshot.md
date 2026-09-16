---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_CopyServerlessCacheSnapshot.html
---

# CopyServerlessCacheSnapshot
<a name="API_CopyServerlessCacheSnapshot"></a>

Creates a copy of an existing serverless cache’s snapshot. Available for Valkey, Redis OSS and Serverless Memcached only.

## Request Parameters
<a name="API_CopyServerlessCacheSnapshot_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** SourceServerlessCacheSnapshotName **
The identifier of the existing serverless cache’s snapshot to be copied. Available for Valkey, Redis OSS and Serverless Memcached only.
Type: String
Required: Yes

 ** TargetServerlessCacheSnapshotName **
The identifier for the snapshot to be created. Available for Valkey, Redis OSS and Serverless Memcached only. This value is stored as a lowercase string.
Type: String
Required: Yes

 ** KmsKeyId **
The identifier of the KMS key used to encrypt the target snapshot. Available for Valkey, Redis OSS and Serverless Memcached only.
Type: String
Required: No

 **Tags.Tag.N**
A list of tags to be added to the target snapshot resource. A tag is a key-value pair. Available for Valkey, Redis OSS and Serverless Memcached only. Default: NULL
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Elements
<a name="API_CopyServerlessCacheSnapshot_ResponseElements"></a>

The following element is returned by the service.

 ** ServerlessCacheSnapshot **
The response for the attempt to copy the serverless cache snapshot. Available for Valkey, Redis OSS and Serverless Memcached only.
Type: [ServerlessCacheSnapshot](API_ServerlessCacheSnapshot.md) object

## Errors
<a name="API_CopyServerlessCacheSnapshot_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** InvalidServerlessCacheSnapshotStateFault **
The state of the serverless cache snapshot was not received. Available for Valkey, Redis OSS and Serverless Memcached only.
HTTP Status Code: 400

 ** ServerlessCacheSnapshotAlreadyExistsFault **
A serverless cache snapshot with this name already exists. Available for Valkey, Redis OSS and Serverless Memcached only.
HTTP Status Code: 400

 ** ServerlessCacheSnapshotNotFoundFault **
This serverless cache snapshot could not be found or does not exist. Available for Valkey, Redis OSS and Serverless Memcached only.
HTTP Status Code: 404

 ** ServerlessCacheSnapshotQuotaExceededFault **
The number of serverless cache snapshots exceeds the customer snapshot quota. Available for Valkey, Redis OSS and Serverless Memcached only.
HTTP Status Code: 400

 ** ServiceLinkedRoleNotFoundFault **
The specified service linked role (SLR) was not found.
HTTP Status Code: 400

 ** TagQuotaPerResourceExceeded **
The request cannot be processed because it would cause the resource to have more than the allowed number of tags. The maximum number of tags permitted on a resource is 50.
HTTP Status Code: 400

## Examples
<a name="API_CopyServerlessCacheSnapshot_Examples"></a>

### CopyServerlessCacheSnapshot
<a name="API_CopyServerlessCacheSnapshot_Example_1"></a>

This example illustrates one usage of CopyServerlessCacheSnapshot.

#### Sample Request
<a name="API_CopyServerlessCacheSnapshot_Example_1_Request"></a>

```
{
    "input": {
        "SourceServerlessCacheSnapshotName": "my-serverless-cache-snapshot",
        "TargetServerlessCacheSnapshotName": "my-serverless-cache-snapshot-copy"
    },
    "output": {
        "ServerlessCacheSnapshot": {
            "ServerlessCacheSnapshotName": "my-serverless-cache-snapshot-copy",
            "ARN": "arn:aws:elasticache:us-east-1:222222222222:serverlesscachesnapshot:my-serverless-cache-snapshot-copy",
            "SnapshotType": "manual",
            "Status": "creating",
            "ServerlessCacheConfiguration": {
                "ServerlessCacheName": "my-serverless-cache",
                "Engine": "redis",
                "MajorEngineVersion": "7"
            }
        }
    }
}
```

## See Also
<a name="API_CopyServerlessCacheSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticache-2015-02-02/CopyServerlessCacheSnapshot)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticache-2015-02-02/CopyServerlessCacheSnapshot)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/CopyServerlessCacheSnapshot)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticache-2015-02-02/CopyServerlessCacheSnapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/CopyServerlessCacheSnapshot)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticache-2015-02-02/CopyServerlessCacheSnapshot)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticache-2015-02-02/CopyServerlessCacheSnapshot)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticache-2015-02-02/CopyServerlessCacheSnapshot)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticache-2015-02-02/CopyServerlessCacheSnapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/CopyServerlessCacheSnapshot)
