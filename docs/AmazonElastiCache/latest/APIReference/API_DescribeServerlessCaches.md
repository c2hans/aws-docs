---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DescribeServerlessCaches.html
---

# DescribeServerlessCaches
<a name="API_DescribeServerlessCaches"></a>

Returns information about a specific serverless cache. If no identifier is specified, then the API returns information on all the serverless caches belonging to this AWS account.

## Request Parameters
<a name="API_DescribeServerlessCaches_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** MaxResults **
The maximum number of records in the response. If more records exist than the specified max-records value, the next token is included in the response so that remaining results can be retrieved. The default is 50.
Type: Integer
Required: No

 ** NextToken **
An optional marker returned from a prior request to support pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxResults.
Type: String
Required: No

 ** ServerlessCacheName **
The identifier for the serverless cache. If this parameter is specified, only information about that specific serverless cache is returned. Default: NULL
Type: String
Required: No

## Response Elements
<a name="API_DescribeServerlessCaches_ResponseElements"></a>

The following elements are returned by the service.

 ** NextToken **
An optional marker returned from a prior request to support pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxResults.
Type: String

 **ServerlessCaches.member.N**
The serverless caches associated with a given description request.
Type: Array of [ServerlessCache](API_ServerlessCache.md) objects

## Errors
<a name="API_DescribeServerlessCaches_Errors"></a>

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

 ** ServerlessCacheNotFoundFault **
The serverless cache was not found or does not exist.
HTTP Status Code: 404

## Examples
<a name="API_DescribeServerlessCaches_Examples"></a>

### DescribeServerlessCaches
<a name="API_DescribeServerlessCaches_Example_1"></a>

This example illustrates one usage of DescribeServerlessCaches.

#### Sample Request
<a name="API_DescribeServerlessCaches_Example_1_Request"></a>

```
{
    "input": {
    },
    "output": {
        "ServerlessCaches": [
            {
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
        ]
    }
}
```

## See Also
<a name="API_DescribeServerlessCaches_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticache-2015-02-02/DescribeServerlessCaches)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticache-2015-02-02/DescribeServerlessCaches)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/DescribeServerlessCaches)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticache-2015-02-02/DescribeServerlessCaches)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/DescribeServerlessCaches)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticache-2015-02-02/DescribeServerlessCaches)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticache-2015-02-02/DescribeServerlessCaches)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticache-2015-02-02/DescribeServerlessCaches)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticache-2015-02-02/DescribeServerlessCaches)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/DescribeServerlessCaches)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
