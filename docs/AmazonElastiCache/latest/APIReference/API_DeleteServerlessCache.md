---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DeleteServerlessCache.html
---

# DeleteServerlessCache
<a name="API_DeleteServerlessCache"></a>

Deletes a specified existing serverless cache.

**Note**
 `CreateServerlessCacheSnapshot` permission is required to create a final snapshot. Without this permission, the API call will fail with an `Access Denied` exception.

## Request Parameters
<a name="API_DeleteServerlessCache_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ServerlessCacheName **
The identifier of the serverless cache to be deleted.
Type: String
Required: Yes

 ** FinalSnapshotName **
Name of the final snapshot to be taken before the serverless cache is deleted. Available for Valkey, Redis OSS and Serverless Memcached only. Default: NULL, i.e. a final snapshot is not taken.
Type: String
Required: No

## Response Elements
<a name="API_DeleteServerlessCache_ResponseElements"></a>

The following element is returned by the service.

 ** ServerlessCache **
Provides the details of the specified serverless cache that is about to be deleted.
Type: [ServerlessCache](API_ServerlessCache.md) object

## Errors
<a name="API_DeleteServerlessCache_Errors"></a>

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

 ** ServerlessCacheNotFoundFault **
The serverless cache was not found or does not exist.
HTTP Status Code: 404

 ** ServerlessCacheSnapshotAlreadyExistsFault **
A serverless cache snapshot with this name already exists. Available for Valkey, Redis OSS and Serverless Memcached only.
HTTP Status Code: 400

 ** ServiceLinkedRoleNotFoundFault **
The specified service linked role (SLR) was not found.
HTTP Status Code: 400

## Examples
<a name="API_DeleteServerlessCache_Examples"></a>

### DeleteServerlessCache
<a name="API_DeleteServerlessCache_Example_1"></a>

This example illustrates one usage of DeleteServerlessCache.

#### Sample Request
<a name="API_DeleteServerlessCache_Example_1_Request"></a>

```
{
    "input": {
        "ServerlessCacheName": "my-serverless-cache"
    },
    "output": {
        "ServerlessCache": {
            "ServerlessCacheName": "my-serverless-cache",
            "Description": "A serverless cache.",
            "Status": "deleting",
            "Engine": "redis",
            "MajorEngineVersion": "7",
            "FullEngineVersion": "7.0",
            "SubnetIds": [
                "subnet-xxx8c982",
                "subnet-xxx382f3",
                "subnet-xxxb3e7c0"
            ],
            "SecurityGroupIds": [
                "sg-xxx0c9af"
            ],
            "Endpoint": {
                "Address": "my-serverless-cache-xxxxx.serverless.use1qa.cache.amazonaws.com",
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
<a name="API_DeleteServerlessCache_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticache-2015-02-02/DeleteServerlessCache)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticache-2015-02-02/DeleteServerlessCache)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/DeleteServerlessCache)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticache-2015-02-02/DeleteServerlessCache)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/DeleteServerlessCache)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticache-2015-02-02/DeleteServerlessCache)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticache-2015-02-02/DeleteServerlessCache)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticache-2015-02-02/DeleteServerlessCache)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticache-2015-02-02/DeleteServerlessCache)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/DeleteServerlessCache)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
