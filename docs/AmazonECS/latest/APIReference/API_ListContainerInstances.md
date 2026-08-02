---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListContainerInstances.html
---

# ListContainerInstances
<a name="API_ListContainerInstances"></a>

Returns a list of container instances in a specified cluster. You can filter the results of a `ListContainerInstances` operation with cluster query language statements inside the `filter` parameter. For more information, see [Cluster Query Language](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html) in the *Amazon Elastic Container Service Developer Guide*.

## Request Syntax
<a name="API_ListContainerInstances_RequestSyntax"></a>

```
{
   "cluster": "{{string}}",
   "filter": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "status": "{{string}}"
}
```

## Request Parameters
<a name="API_ListContainerInstances_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [cluster](#API_ListContainerInstances_RequestSyntax) **   <a name="ECS-ListContainerInstances-request-cluster"></a>
The short name or full Amazon Resource Name (ARN) of the cluster that hosts the container instances to list. If you do not specify a cluster, the default cluster is assumed.
Type: String
Required: No

 ** [filter](#API_ListContainerInstances_RequestSyntax) **   <a name="ECS-ListContainerInstances-request-filter"></a>
You can filter the results of a `ListContainerInstances` operation with cluster query language statements. For more information, see [Cluster Query Language](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html) in the *Amazon Elastic Container Service Developer Guide*.
Type: String
Required: No

 ** [maxResults](#API_ListContainerInstances_RequestSyntax) **   <a name="ECS-ListContainerInstances-request-maxResults"></a>
The maximum number of container instance results that `ListContainerInstances` returned in paginated output. When this parameter is used, `ListContainerInstances` only returns `maxResults` results in a single page along with a `nextToken` response element. The remaining results of the initial request can be seen by sending another `ListContainerInstances` request with the returned `nextToken` value. This value can be between 1 and 100. If this parameter isn't used, then `ListContainerInstances` returns up to 100 results and a `nextToken` value if applicable.
Type: Integer
Required: No

 ** [nextToken](#API_ListContainerInstances_RequestSyntax) **   <a name="ECS-ListContainerInstances-request-nextToken"></a>
The `nextToken` value returned from a `ListContainerInstances` request indicating that more results are available to fulfill the request and further calls are needed. If `maxResults` was provided, it's possible the number of results to be fewer than `maxResults`.
This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
Type: String
Required: No

 ** [status](#API_ListContainerInstances_RequestSyntax) **   <a name="ECS-ListContainerInstances-request-status"></a>
Filters the container instances by status. For example, if you specify the `DRAINING` status, the results include only container instances that have been set to `DRAINING` using [UpdateContainerInstancesState](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateContainerInstancesState.html). If you don't specify this parameter, the The default is to include container instances set to all states other than `INACTIVE`.
Type: String
Valid Values: `ACTIVE | DRAINING | REGISTERING | DEREGISTERING | REGISTRATION_FAILED`
Required: No

## Response Syntax
<a name="API_ListContainerInstances_ResponseSyntax"></a>

```
{
   "containerInstanceArns": [ "string" ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListContainerInstances_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [containerInstanceArns](#API_ListContainerInstances_ResponseSyntax) **   <a name="ECS-ListContainerInstances-response-containerInstanceArns"></a>
The list of container instances with full ARN entries for each container instance associated with the specified cluster.
Type: Array of strings

 ** [nextToken](#API_ListContainerInstances_ResponseSyntax) **   <a name="ECS-ListContainerInstances-response-nextToken"></a>
The `nextToken` value to include in a future `ListContainerInstances` request. When the results of a `ListContainerInstances` request exceed `maxResults`, this value can be used to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

## Errors
<a name="API_ListContainerInstances_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have authorization to perform the requested action.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** ClientException **
These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** ClusterNotFoundException **
The specified cluster wasn't found. You can view your available clusters with [ListClusters](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html). Amazon ECS clusters are Region specific.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** InvalidParameterException **
The specified parameter isn't valid. Review the available parameters for the API request.
For more information about service event errors, see [Amazon ECS service event messages](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html).
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** ServerException **
These errors are usually caused by a server issue.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 500

## Examples
<a name="API_ListContainerInstances_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to create them manually. When you use the [AWS Command Line Interface](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you, with the access key that you specify when you configure the tools. When you use these tools, you don't have to sign requests yourself.

### Example
<a name="API_ListContainerInstances_Example_1"></a>

This example request lists the container instances in the "example" cluster.

#### Sample Request
<a name="API_ListContainerInstances_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ecs.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 2
X-Amz-Target: AmazonEC2ContainerServiceV20141113.ListContainerInstances
X-Amz-Date: 20150429T175306Z
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{"containerInstanceArns":["arn:aws:ecs:us-east-1:012345678910:container-instance/example/1eb22c8ab33149b397dc769f68cc1319","arn:aws:ecs:us-east-1:012345678910:container-instance/example/5cf7e311a2b74d3882650353cf3b2214"]}
```

#### Sample Response
<a name="API_ListContainerInstances_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Wed, 29 Apr 2015 17:53:06 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 492
Connection: keep-alive
x-amzn-RequestId: 123a4b56-7c89-01d2-3ef4-example5678f

{
  "containerInstanceArns": [
    "arn:aws:ecs:us-east-1:012345678910:container-instance/example/1eb22c8ab33149b397dc769f68cc1319",
    "arn:aws:ecs:us-east-1:012345678910:container-instance/example/5cf7e311a2b74d3882650353cf3b2214"
  ]
}
```

## See Also
<a name="API_ListContainerInstances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/ListContainerInstances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/ListContainerInstances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ListContainerInstances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/ListContainerInstances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ListContainerInstances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/ListContainerInstances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/ListContainerInstances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/ListContainerInstances)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/ListContainerInstances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ListContainerInstances)
