---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ModifyServerlessCache.html
---

# ModifyServerlessCache
<a name="API_ModifyServerlessCache"></a>

This API modifies the attributes of a serverless cache.

## Request Parameters
<a name="API_ModifyServerlessCache_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ServerlessCacheName **
User-provided identifier for the serverless cache to be modified.
Type: String
Required: Yes

 ** CacheUsageLimits **
Modify the cache usage limit for the serverless cache.
Type: [CacheUsageLimits](API_CacheUsageLimits.md) object
Required: No

 ** DailySnapshotTime **
The daily time during which Elasticache begins taking a daily snapshot of the serverless cache. Available for Valkey, Redis OSS and Serverless Memcached only. The default is NULL, i.e. the existing snapshot time configured for the cluster is not removed.
Type: String
Required: No

 ** Description **
User provided description for the serverless cache. Default = NULL, i.e. the existing description is not removed/modified. The description has a maximum length of 255 characters.
Type: String
Required: No

 ** Engine **
Modifies the engine listed in a serverless cache request. The options are valkey, memcached or redis.
Type: String
Required: No

 ** MajorEngineVersion **
Modifies the engine vesion listed in a serverless cache request.
Type: String
Required: No

 ** RemoveUserGroup **
The identifier of the UserGroup to be removed from association with the Valkey and Redis OSS serverless cache. Available for Valkey and Redis OSS only. Default is NULL.
Type: Boolean
Required: No

 **SecurityGroupIds.SecurityGroupId.N**
The new list of VPC security groups to be associated with the serverless cache. Populating this list means the current VPC security groups will be removed. This security group is used to authorize traffic access for the VPC end-point (private-link). Default = NULL - the existing list of VPC security groups is not removed.
Type: Array of strings
Required: No

 ** SnapshotRetentionLimit **
The number of days for which Elasticache retains automatic snapshots before deleting them. Available for Valkey, Redis OSS and Serverless Memcached only. Default = NULL, i.e. the existing snapshot-retention-limit will not be removed or modified. The maximum value allowed is 35 days.
Type: Integer
Required: No

 ** UserGroupId **
The identifier of the UserGroup to be associated with the serverless cache. Available for Valkey and Redis OSS only. Default is NULL - the existing UserGroup is not removed.
Type: String
Required: No

## Response Elements
<a name="API_ModifyServerlessCache_ResponseElements"></a>

The following element is returned by the service.

 ** ServerlessCache **
The response for the attempt to modify the serverless cache.
Type: [ServerlessCache](API_ServerlessCache.md) object

## Errors
<a name="API_ModifyServerlessCache_Errors"></a>

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

 ** ServerlessCacheNotFoundFault **
The serverless cache was not found or does not exist.
HTTP Status Code: 404

 ** ServiceLinkedRoleNotFoundFault **
The specified service linked role (SLR) was not found.
HTTP Status Code: 400

 ** UserGroupNotFound **
The user group was not found or does not exist
HTTP Status Code: 404

## Examples
<a name="API_ModifyServerlessCache_Examples"></a>

### ModifyServerlessCache
<a name="API_ModifyServerlessCache_Example_1"></a>

This example illustrates one usage of ModifyServerlessCache.

#### Sample Request
<a name="API_ModifyServerlessCache_Example_1_Request"></a>

```
{
    "description": "Modify the daily snapshot time of cache",
    "input": {
        "ServerlessCacheName": "my-serverless-cache",
        "CacheUsageLimits": {
            "DataStorage" : {
                "Maximum" : 10,
                "Unit" : "GB"
            },
            "ECPUPerSecond" : {
                "Maximum" : 50000
            }
        },
        "DailySnapshotTime": "11:00"
    },
    "output": {
        "ServerlessCache": {
            "ServerlessCacheName": "my-serverless-cache",
            "Description": "A serverless cache.",
            "Status": "available",
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
            "Endpoint": {
                "Address": "my-serverless-cache-xxxxxx.serverless.use1qa.cache.amazonaws.com",
                "Port": 6379
            },
            "ARN": "arn:aws:elasticache:us-east-1:222222222222:serverlesscache:my-serverless-cache",
            "SnapshotRetentionLimit": 10,
            "DailySnapshotTime": "11:00",
            "NetworkType": "ipv4"
        }
    }
}
```

## See Also
<a name="API_ModifyServerlessCache_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticache-2015-02-02/ModifyServerlessCache)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticache-2015-02-02/ModifyServerlessCache)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/ModifyServerlessCache)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticache-2015-02-02/ModifyServerlessCache)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/ModifyServerlessCache)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticache-2015-02-02/ModifyServerlessCache)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticache-2015-02-02/ModifyServerlessCache)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticache-2015-02-02/ModifyServerlessCache)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticache-2015-02-02/ModifyServerlessCache)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/ModifyServerlessCache)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
