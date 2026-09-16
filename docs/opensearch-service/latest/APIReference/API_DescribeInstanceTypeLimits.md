---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeInstanceTypeLimits.html
---

# DescribeInstanceTypeLimits
<a name="API_DescribeInstanceTypeLimits"></a>

Describes the instance count, storage, and master node limits for a given OpenSearch or Elasticsearch version and instance type.

## Request Syntax
<a name="API_DescribeInstanceTypeLimits_RequestSyntax"></a>

```
GET /2021-01-01/opensearch/instanceTypeLimits/{{EngineVersion}}/{{InstanceType}}?domainName={{DomainName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeInstanceTypeLimits_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_DescribeInstanceTypeLimits_RequestSyntax) **   <a name="opensearchservice-DescribeInstanceTypeLimits-request-uri-DomainName"></a>
The name of the domain. Only specify if you need the limits for an existing domain.
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `[a-z][a-z0-9\-]+`

 ** [EngineVersion](#API_DescribeInstanceTypeLimits_RequestSyntax) **   <a name="opensearchservice-DescribeInstanceTypeLimits-request-uri-EngineVersion"></a>
Version of OpenSearch or Elasticsearch, in the format Elasticsearch\_X.Y or OpenSearch\_X.Y. Defaults to the latest version of OpenSearch.
Length Constraints: Minimum length of 14. Maximum length of 18.
Pattern: `^Elasticsearch_[0-9]{1}\.[0-9]{1,2}$|^OpenSearch_[0-9]{1,2}\.[0-9]{1,2}$`
Required: Yes

 ** [InstanceType](#API_DescribeInstanceTypeLimits_RequestSyntax) **   <a name="opensearchservice-DescribeInstanceTypeLimits-request-uri-InstanceType"></a>
The OpenSearch Service instance type for which you need limit information.
Valid Values: `m3.medium.search | m3.large.search | m3.xlarge.search | m3.2xlarge.search | m4.large.search | m4.xlarge.search | m4.2xlarge.search | m4.4xlarge.search | m4.10xlarge.search | m5.large.search | m5.xlarge.search | m5.2xlarge.search | m5.4xlarge.search | m5.12xlarge.search | m5.24xlarge.search | r5.large.search | r5.xlarge.search | r5.2xlarge.search | r5.4xlarge.search | r5.12xlarge.search | r5.24xlarge.search | c5.large.search | c5.xlarge.search | c5.2xlarge.search | c5.4xlarge.search | c5.9xlarge.search | c5.18xlarge.search | t3.nano.search | t3.micro.search | t3.small.search | t3.medium.search | t3.large.search | t3.xlarge.search | t3.2xlarge.search | or1.medium.search | or1.large.search | or1.xlarge.search | or1.2xlarge.search | or1.4xlarge.search | or1.8xlarge.search | or1.12xlarge.search | or1.16xlarge.search | ultrawarm1.medium.search | ultrawarm1.large.search | ultrawarm1.xlarge.search | t2.micro.search | t2.small.search | t2.medium.search | r3.large.search | r3.xlarge.search | r3.2xlarge.search | r3.4xlarge.search | r3.8xlarge.search | i2.xlarge.search | i2.2xlarge.search | d2.xlarge.search | d2.2xlarge.search | d2.4xlarge.search | d2.8xlarge.search | c4.large.search | c4.xlarge.search | c4.2xlarge.search | c4.4xlarge.search | c4.8xlarge.search | r4.large.search | r4.xlarge.search | r4.2xlarge.search | r4.4xlarge.search | r4.8xlarge.search | r4.16xlarge.search | i3.large.search | i3.xlarge.search | i3.2xlarge.search | i3.4xlarge.search | i3.8xlarge.search | i3.16xlarge.search | r6g.large.search | r6g.xlarge.search | r6g.2xlarge.search | r6g.4xlarge.search | r6g.8xlarge.search | r6g.12xlarge.search | m6g.large.search | m6g.xlarge.search | m6g.2xlarge.search | m6g.4xlarge.search | m6g.8xlarge.search | m6g.12xlarge.search | c6g.large.search | c6g.xlarge.search | c6g.2xlarge.search | c6g.4xlarge.search | c6g.8xlarge.search | c6g.12xlarge.search | r6gd.large.search | r6gd.xlarge.search | r6gd.2xlarge.search | r6gd.4xlarge.search | r6gd.8xlarge.search | r6gd.12xlarge.search | r6gd.16xlarge.search | t4g.small.search | t4g.medium.search`
Required: Yes

## Request Body
<a name="API_DescribeInstanceTypeLimits_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeInstanceTypeLimits_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "LimitsByRole": {
      "string" : {
         "AdditionalLimits": [
            {
               "LimitName": "string",
               "LimitValues": [ "string" ]
            }
         ],
         "InstanceLimits": {
            "InstanceCountLimits": {
               "MaximumInstanceCount": number,
               "MinimumInstanceCount": number
            }
         },
         "StorageTypes": [
            {
               "StorageSubTypeName": "string",
               "StorageTypeLimits": [
                  {
                     "LimitName": "string",
                     "LimitValues": [ "string" ]
                  }
               ],
               "StorageTypeName": "string"
            }
         ]
      }
   }
}
```

## Response Elements
<a name="API_DescribeInstanceTypeLimits_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LimitsByRole](#API_DescribeInstanceTypeLimits_ResponseSyntax) **   <a name="opensearchservice-DescribeInstanceTypeLimits-response-LimitsByRole"></a>
Map that contains all applicable instance type limits.`data` refers to data nodes.`master` refers to dedicated master nodes.
Type: String to [Limits](API_Limits.md) object map

## Errors
<a name="API_DescribeInstanceTypeLimits_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BaseException **
An error occurred while processing the request.
 ** message **
A description of the error.
HTTP Status Code: 400

 ** InternalException **
Request processing failed because of an unknown error, exception, or internal failure.
HTTP Status Code: 500

 ** InvalidTypeException **
An exception for trying to create or access a sub-resource that's either invalid or not supported.
HTTP Status Code: 409

 ** LimitExceededException **
An exception for trying to create more than the allowed number of resources or sub-resources.
HTTP Status Code: 409

 ** ResourceNotFoundException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 409

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## Examples
<a name="API_DescribeInstanceTypeLimits_Examples"></a>

### Example
<a name="API_DescribeInstanceTypeLimits_Example_1"></a>

This example illustrates one usage of DescribeInstanceTypeLimits.

#### Sample Request
<a name="API_DescribeInstanceTypeLimits_Example_1_Request"></a>

```
GET /2021-01-01/opensearch/instanceTypeLimits/OpenSearch_1.0/c5.large.search?domainName=mydomain HTTP/1.1
Host: es.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.15.0 Python/3.11.6 Darwin/23.2.0 exe/x86_64 prompt/off command/opensearch.describe-instance-type-limits
X-Amz-Date: 20240118T183818Z
X-Amz-Security-Token: IQoJb3JpZ2luX2VjEI3wEaCXVz==
Authorization: AWS4-HMAC-SHA256 Credential=ASIAU/20240118/us-east-1/es/aws4_request, SignedHeaders=host;x-amz-date;x-amz-security-token, Signature=b8e8474eba198ee0a30b422c5196860943c1ed944a599160aa070268db1c17fa
```

#### Sample Response
<a name="API_DescribeInstanceTypeLimits_Example_1_Response"></a>

```
{
	"LimitsByRole": {
		"data": {
			"AdditionalLimits": [{
				"LimitName": "MaximumNumberOfDataNodesWithoutMasterNode",
				"LimitValues": ["10"]
			}],
			"InstanceLimits": {
				"InstanceCountLimits": {
					"MaximumInstanceCount": 80,
					"MinimumInstanceCount": 1
				}
			},
			"StorageTypes": [{
				"StorageSubTypeName": "standard",
				"StorageTypeLimits": [{
					"LimitName": "MaximumVolumeSize",
					"LimitValues": ["100"]
				}, {
					"LimitName": "MinimumVolumeSize",
					"LimitValues": ["10"]
				}],
				"StorageTypeName": "ebs"
			}, {
				"StorageSubTypeName": "io1",
				"StorageTypeLimits": [{
					"LimitName": "MaximumVolumeSize",
					"LimitValues": ["256"]
				}, {
					"LimitName": "MinimumVolumeSize",
					"LimitValues": ["35"]
				}, {
					"LimitName": "MaximumIops",
					"LimitValues": ["16000"]
				}, {
					"LimitName": "MinimumIops",
					"LimitValues": ["1000"]
				}],
				"StorageTypeName": "ebs"
			}, {
				"StorageSubTypeName": "gp2",
				"StorageTypeLimits": [{
					"LimitName": "MaximumVolumeSize",
					"LimitValues": ["256"]
				}, {
					"LimitName": "MinimumVolumeSize",
					"LimitValues": ["10"]
				}],
				"StorageTypeName": "ebs"
			}, {
				"StorageSubTypeName": "gp3",
				"StorageTypeLimits": [{
					"LimitName": "MaximumVolumeSize",
					"LimitValues": ["256"]
				}, {
					"LimitName": "MinimumVolumeSize",
					"LimitValues": ["10"]
				}, {
					"LimitName": "MaximumIops",
					"LimitValues": ["20000"]
				}, {
					"LimitName": "MinimumIops",
					"LimitValues": ["3000"]
				}, {
					"LimitName": "MaximumThroughput",
					"LimitValues": ["593"]
				}, {
					"LimitName": "MinimumThroughput",
					"LimitValues": ["125"]
				}],
				"StorageTypeName": "ebs"
			}]
		},
		"master": {
			"AdditionalLimits": [{
				"LimitName": "MaximumNumberOfDataNodesSupported",
				"LimitValues": ["200"]
			}],
			"InstanceLimits": {
				"InstanceCountLimits": {
					"MaximumInstanceCount": 5,
					"MinimumInstanceCount": 2
				}
			},
			"StorageTypes": null
		}
	}
}
```

## See Also
<a name="API_DescribeInstanceTypeLimits_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/DescribeInstanceTypeLimits)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/DescribeInstanceTypeLimits)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/DescribeInstanceTypeLimits)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/DescribeInstanceTypeLimits)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/DescribeInstanceTypeLimits)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/DescribeInstanceTypeLimits)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/DescribeInstanceTypeLimits)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/DescribeInstanceTypeLimits)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/DescribeInstanceTypeLimits)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/DescribeInstanceTypeLimits)
