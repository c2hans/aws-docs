---
source_url: https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_DescribeVirtualCluster.html
---

# DescribeVirtualCluster
<a name="API_DescribeVirtualCluster"></a>

Displays detailed information about a specified virtual cluster. Virtual cluster is a managed entity on Amazon EMR on EKS. You can create, update, describe, list and delete virtual clusters. They do not consume any additional resource in your system. A single virtual cluster maps to a single Kubernetes namespace. Given this relationship, you can model virtual clusters the same way you model Kubernetes namespaces to meet your requirements.

## Request Syntax
<a name="API_DescribeVirtualCluster_RequestSyntax"></a>

```
GET /virtualclusters/{{virtualClusterId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeVirtualCluster_RequestParameters"></a>

The request uses the following URI parameters.

 ** [virtualClusterId](#API_DescribeVirtualCluster_RequestSyntax) **   <a name="emroneks-DescribeVirtualCluster-request-uri-id"></a>
The ID of the virtual cluster that will be described.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`
Required: Yes

## Request Body
<a name="API_DescribeVirtualCluster_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeVirtualCluster_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "virtualCluster": {
      "arn": "string",
      "containerProvider": {
         "id": "string",
         "info": { ... },
         "type": "string"
      },
      "createdAt": "string",
      "id": "string",
      "name": "string",
      "schedulerConfiguration": {
         "maxConcurrentJobRuns": number,
         "maxInQueueJobRuns": number
      },
      "schedulerStatus": {
         "currentConcurrentJobRuns": number,
         "currentInQueueJobRuns": number
      },
      "securityConfigurationId": "string",
      "sessionEnabled": boolean,
      "state": "string",
      "tags": {
         "string" : "string"
      }
   }
}
```

## Response Elements
<a name="API_DescribeVirtualCluster_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [virtualCluster](#API_DescribeVirtualCluster_ResponseSyntax) **   <a name="emroneks-DescribeVirtualCluster-response-virtualCluster"></a>
This output displays information about the specified virtual cluster.
Type: [VirtualCluster](API_VirtualCluster.md) object

## Errors
<a name="API_DescribeVirtualCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
This is an internal server exception.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

 ** ValidationException **
There are invalid parameters in the client request.
HTTP Status Code: 400

## See Also
<a name="API_DescribeVirtualCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/emr-containers-2020-10-01/DescribeVirtualCluster)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/emr-containers-2020-10-01/DescribeVirtualCluster)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-containers-2020-10-01/DescribeVirtualCluster)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/emr-containers-2020-10-01/DescribeVirtualCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-containers-2020-10-01/DescribeVirtualCluster)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/emr-containers-2020-10-01/DescribeVirtualCluster)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/emr-containers-2020-10-01/DescribeVirtualCluster)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/emr-containers-2020-10-01/DescribeVirtualCluster)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/emr-containers-2020-10-01/DescribeVirtualCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-containers-2020-10-01/DescribeVirtualCluster)
