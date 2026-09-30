---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_CreateServerlessCache.html
---

# CreateServerlessCache
<a name="API_CreateServerlessCache"></a>

Creates a serverless cache.

## Request Parameters
<a name="API_CreateServerlessCache_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** Engine **
The name of the cache engine to be used for creating the serverless cache.
Type: String
Required: Yes

 ** ServerlessCacheName **
User-provided identifier for the serverless cache. This parameter is stored as a lowercase string.
Type: String
Required: Yes

 ** CacheUsageLimits **
Sets the cache usage limits for storage and ElastiCache Processing Units for the cache.
Type: [CacheUsageLimits](API_CacheUsageLimits.md) object
Required: No

 ** ConnectionType **
The connection type for the serverless cache. Must be either `vpc` \| `public`. Use `vpc` to access the cache through a VPC endpoint, or `public` to access the cache over the internet. If not specified, defaults to `vpc`. This value cannot be changed after the serverless cache is created. Setting this to `public` requires Valkey 9 or above.
Type: String
Valid Values: `vpc | public`
Required: No

 ** DailySnapshotTime **
The daily time that snapshots will be created from the new serverless cache. By default this number is populated with 0, i.e. no snapshots will be created on an automatic daily basis. Available for Valkey, Redis OSS and Serverless Memcached only.
Type: String
Required: No

 ** Description **
User-provided description for the serverless cache. The default is NULL, i.e. if no description is provided then an empty string will be returned. The maximum length is 255 characters.
Type: String
Required: No

 ** KmsKeyId **
ARN of the customer managed key for encrypting the data at rest. If no KMS key is provided, a default service key is used.
Type: String
Required: No

 ** MajorEngineVersion **
The version of the cache engine that will be used to create the serverless cache.
Type: String
Required: No

 ** NetworkType **
The IP protocol version used by the serverless cache. Must be either `ipv4` \| `ipv6` \| `dual_stack`. `ipv6` is only supported with IPv6-only subnets. If not specified, defaults to `ipv4`, unless all provided subnets are IPv6-only, in which case it defaults to `ipv6`.
Type: String
Valid Values: `ipv4 | ipv6 | dual_stack`
Required: No

 **SecurityGroupIds.SecurityGroupId.N**
A list of the one or more VPC security groups to be associated with the serverless cache. The security group will authorize traffic access for the VPC end-point (private-link). If no other information is given this will be the VPC’s Default Security Group that is associated with the cluster VPC end-point.
Type: Array of strings
Required: No

 **SnapshotArnsToRestore.SnapshotArn.N**
The ARN(s) of the snapshot that the new serverless cache will be created from. Available for Valkey, Redis OSS and Serverless Memcached only.
Type: Array of strings
Required: No

 ** SnapshotRetentionLimit **
The number of days for which ElastiCache retains automatic snapshots before deleting them. Available for Valkey, Redis OSS and Serverless Memcached only. The maximum value allowed is 35 days.
Type: Integer
Required: No

 **SubnetIds.SubnetId.N**
A list of the identifiers of the subnets where the VPC endpoint for the serverless cache will be deployed. All the subnetIds must belong to the same VPC.
Type: Array of strings
Required: No

 **Tags.Tag.N**
The list of tags (key, value) pairs to be added to the serverless cache resource. Default is NULL.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** UserGroupId **
The identifier of the UserGroup to be associated with the serverless cache. Available for Valkey and Redis OSS only. Default is NULL.
Type: String
Required: No

## Response Elements
<a name="API_CreateServerlessCache_ResponseElements"></a>

The following element is returned by the service.

 ** ServerlessCache **
The response for the attempt to create the serverless cache.
Type: [ServerlessCache](API_ServerlessCache.md) object

## Errors
<a name="API_CreateServerlessCache_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidCredentials **
You must enter valid credentials.
HTTP Status Code: 408

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

 ** InvalidServerlessCacheStateFault **
The account for these credentials is not currently active.
HTTP Status Code: 400

 ** InvalidUserGroupState **
The user group is not in an active state.
HTTP Status Code: 400

 ** ServerlessCacheAlreadyExistsFault **
A serverless cache with this name already exists.
HTTP Status Code: 400

 ** ServerlessCacheNotFoundFault **
The serverless cache was not found or does not exist.
HTTP Status Code: 404

 ** ServerlessCacheQuotaForCustomerExceededFault **
The number of serverless caches exceeds the customer quota.
HTTP Status Code: 400

 ** ServiceLinkedRoleNotFoundFault **
The specified service linked role (SLR) was not found.
HTTP Status Code: 400

 ** TagQuotaPerResourceExceeded **
The request cannot be processed because it would cause the resource to have more than the allowed number of tags. The maximum number of tags permitted on a resource is 50.
HTTP Status Code: 400

 ** UserGroupNotFound **
The user group was not found or does not exist
HTTP Status Code: 404

## Examples
<a name="API_CreateServerlessCache_Examples"></a>

### CreateServerlessCache with Redis OSS
<a name="API_CreateServerlessCache_Example_1"></a>

This example illustrates one usage of CreateServerlessCache.

#### Sample Request
<a name="API_CreateServerlessCache_Example_1_Request"></a>

```
{
    "input": {
        "ServerlessCacheName": "my-serverless-cache",
        "Description": "A serverless cache.",
        "Engine": "redis",
        "MajorEngineVersion": "7",
        "SubnetIds": [
            "subnet-xxx8c982",
            "subnet-xxx382f3",
            "subnet-xxxb3e7c0"
        ],
        "CacheUsageLimits": {
            "DataStorage" : {
                "Maximum" : 10,
                "Unit" : "GB"
            },
            "ECPUPerSecond" : {
                "Maximum" : 50000
            }
        },
        "SecurityGroupIds": [
            "sg-xxx0c9af"
        ],
        "SnapshotRetentionLimit": 10,
        "DailySnapshotTime": "09:00",
        "NetworkType": "ipv4"
    },
    "output": {
        "ServerlessCache": {
            "ServerlessCacheName": "my-serverless-cache",
            "Description": "A serverless cache.",
            "Status": "creating",
            "Engine": "redis",
            "MajorEngineVersion": "7",
            "FullEngineVersion": "7.0",
            "SubnetIds": [
                "subnet-xxx8c982",
                "subnet-xxx382f3",
                "subnet-xxxb3e7c0"
            ],
            "CacheUsageLimits": {
                "DataStorage" : {
                    "Maximum" : 10,
                    "Unit" : "GB"
                },
                "ECPUPerSecond" : {
                    "Maximum" : 50000
                }
            },
            "SecurityGroupIds": [
                "sg-xxx0c9af"
            ],
            "ARN": "arn:aws:elasticache:us-east-1:222222222222:serverlesscache:my-serverless-cache",
            "SnapshotRetentionLimit": 10,
            "DailySnapshotTime": "09:00",
            "NetworkType": "ipv4"
        }
    }
}
```

### CreateServerlessCache (Memcached)
<a name="API_CreateServerlessCache_Example_2"></a>

This example illustrates one usage of CreateServerlessCache.

#### Sample Request
<a name="API_CreateServerlessCache_Example_2_Request"></a>

```
{
    "input": {
        "ServerlessCacheName": "my-serverless-cache",
        "Description": "A serverless cache.",
        "Engine": "memcached",
        "MajorEngineVersion": "1.6",
        "SubnetIds": [
            "subnet-xxx8c982",
            "subnet-xxx382f3",
            "subnet-xxxb3e7c0"
        ],
        "CacheUsageLimits": {
            "DataStorage" : {
                "Maximum" : 10,
                "Unit" : "GB"
            },
            "ECPUPerSecond" : {
                "Maximum" : 50000
            }
        },
        "SecurityGroupIds": [
            "sg-xxx0c9af"
        ],
        "ARN": "arn:aws:elasticache:us-east-1:222222222222:serverlesscache:my-serverless-cache",
        "SnapshotRetentionLimit": 10,
        "DailySnapshotTime": "09:00",
        "NetworkType": "ipv4"
    },
    "output": {
        "ServerlessCache": {
            "ServerlessCacheName": "my-serverless-cache",
            "Description": "A serverless cache.",
            "Status": "creating",
            "Engine": "memcached",
            "MajorEngineVersion": "1.6",
            "FullEngineVersion": "1.6.21",
            "SubnetIds": [
                "subnet-xxx8c982",
                "subnet-xxx382f3",
                "subnet-xxxb3e7c0"
            ],
            "CacheUsageLimits": {
                "DataStorage" : {
                    "Maximum" : 10,
                    "Unit" : "GB"
                },
                "ECPUPerSecond" : {
                    "Maximum" : 50000
                }
            },
            "SecurityGroupIds": [
                "sg-xxx0c9af"
            ],
            "ARN": "arn:aws:elasticache:us-east-1:222222222222:serverlesscache:my-serverless-cache",
            "SnapshotRetentionLimit": 10,
            "DailySnapshotTime": "09:00",
            "NetworkType": "ipv4"
        }
    }
}
```

## See Also
<a name="API_CreateServerlessCache_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticache-2015-02-02/CreateServerlessCache)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticache-2015-02-02/CreateServerlessCache)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/CreateServerlessCache)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticache-2015-02-02/CreateServerlessCache)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/CreateServerlessCache)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticache-2015-02-02/CreateServerlessCache)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticache-2015-02-02/CreateServerlessCache)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticache-2015-02-02/CreateServerlessCache)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticache-2015-02-02/CreateServerlessCache)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/CreateServerlessCache)
