---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeDomainNodes.html
---

# DescribeDomainNodes
<a name="API_DescribeDomainNodes"></a>

Returns information about domain and nodes, including data nodes, master nodes, ultrawarm nodes, Availability Zone(s), standby nodes, node configurations, and node states.

## Request Syntax
<a name="API_DescribeDomainNodes_RequestSyntax"></a>

```
GET /2021-01-01/opensearch/domain/{{DomainName}}/nodes HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeDomainNodes_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_DescribeDomainNodes_RequestSyntax) **   <a name="opensearchservice-DescribeDomainNodes-request-uri-DomainName"></a>
The name of the domain.
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `[a-z][a-z0-9\-]+`
Required: Yes

## Request Body
<a name="API_DescribeDomainNodes_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeDomainNodes_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DomainNodesStatusList": [
      {
         "AvailabilityZone": "string",
         "InstanceType": "string",
         "NodeId": "string",
         "NodeStatus": "string",
         "NodeType": "string",
         "StorageSize": "string",
         "StorageType": "string",
         "StorageVolumeType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeDomainNodes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DomainNodesStatusList](#API_DescribeDomainNodes_ResponseSyntax) **   <a name="opensearchservice-DescribeDomainNodes-response-DomainNodesStatusList"></a>
Contains nodes information list `DomainNodesStatusList` with details about the all nodes on the requested domain.
Type: Array of [DomainNodesStatus](API_DomainNodesStatus.md) objects

## Errors
<a name="API_DescribeDomainNodes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BaseException **
An error occurred while processing the request.
 ** message **
A description of the error.
HTTP Status Code: 400

 ** DependencyFailureException **
An exception for when a failure in one of the dependencies results in the service being unable to fetch details about the resource.
HTTP Status Code: 424

 ** DisabledOperationException **
An error occured because the client wanted to access an unsupported operation.
HTTP Status Code: 409

 ** InternalException **
Request processing failed because of an unknown error, exception, or internal failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 409

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## Examples
<a name="API_DescribeDomainNodes_Examples"></a>

### Example
<a name="API_DescribeDomainNodes_Example_1"></a>

This example illustrates one usage of DescribeDomainNodes.

#### Sample Request
<a name="API_DescribeDomainNodes_Example_1_Request"></a>

```
GET /2021-01-01/opensearch/domain/amazonrocks/nodes HTTP/1.1
Host: es.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.15.13 Python/3.11.6 Windows/10 exe/AMD64 prompt/off command/opensearch.describe-domain-nodes
X-Amz-Date: 20240209T222942Z
X-Amz-Security-Token: IQoJb3JpZ2luX2VjEEcaCXVz==
Authorization: AWS4-HMAC-SHA256 Credential=ASIAU/20240209/us-east-1/es/aws4_request, SignedHeaders=host;x-amz-date;x-amz-security-token, Signature=6cc839c3e9dcf0a11a52de4e0c0b9c07ffb0fed0e60a76d01062e3de18502927
```

#### Sample Response
<a name="API_DescribeDomainNodes_Example_1_Response"></a>

```
{
   "DomainNodesStatusList":[
      {
         "AvailabilityZone":"us-east-1d",
         "InstanceType":"r6g.large",
         "NodeId":"MRJ8TdTEQBuaMp9kmR9i6Q",
         "NodeStatus":"Active",
         "NodeType":"Data",
         "StorageSize":"10",
         "StorageType":"EBS",
         "StorageVolumeType":"gp2"
      },
      {
         "AvailabilityZone":"us-east-1c",
         "InstanceType":"r6g.large",
         "NodeId":"-Rx5kkj3RAuf3h2WlS0cpw",
         "NodeStatus":"Active",
         "NodeType":"Data",
         "StorageSize":"10",
         "StorageType":"EBS",
         "StorageVolumeType":"gp2"
      },
      {
         "AvailabilityZone":"us-east-1b",
         "InstanceType":"r6g.large",
         "NodeId":"VLEn_jYTTzSapI54pdnBtA",
         "NodeStatus":"Active",
         "NodeType":"Data",
         "StorageSize":"10",
         "StorageType":"EBS",
         "StorageVolumeType":"gp2"
      }
   ]
}
```

## See Also
<a name="API_DescribeDomainNodes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/DescribeDomainNodes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/DescribeDomainNodes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/DescribeDomainNodes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/DescribeDomainNodes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/DescribeDomainNodes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/DescribeDomainNodes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/DescribeDomainNodes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/DescribeDomainNodes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/DescribeDomainNodes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/DescribeDomainNodes)
