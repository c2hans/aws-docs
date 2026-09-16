---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServiceDeployments.html
---

# ListServiceDeployments
<a name="API_ListServiceDeployments"></a>

This operation lists all the service deployments that meet the specified filter criteria.

A service deployment happens when you release a software update for the service. You route traffic from the running service revisions to the new service revison and control the number of running tasks.

This API returns the values that you use for the request parameters in [DescribeServiceRevisions](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeServiceRevisions.html).

## Request Syntax
<a name="API_ListServiceDeployments_RequestSyntax"></a>

```
{
   "cluster": "{{string}}",
   "createdAt": {
      "after": {{number}},
      "before": {{number}}
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "service": "{{string}}",
   "status": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_ListServiceDeployments_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [cluster](#API_ListServiceDeployments_RequestSyntax) **   <a name="ECS-ListServiceDeployments-request-cluster"></a>
The cluster that hosts the service. This can either be the cluster name or ARN. Starting April 15, 2023, Amazon Web Services will not onboard new customers to Amazon Elastic Inference (EI), and will help current customers migrate their workloads to options that offer better price and performance. If you don't specify a cluster, `default` is used.
Type: String
Required: No

 ** [createdAt](#API_ListServiceDeployments_RequestSyntax) **   <a name="ECS-ListServiceDeployments-request-createdAt"></a>
An optional filter you can use to narrow the results by the service creation date. If you do not specify a value, the result includes all services created before the current time. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.
Type: [CreatedAt](API_CreatedAt.md) object
Required: No

 ** [maxResults](#API_ListServiceDeployments_RequestSyntax) **   <a name="ECS-ListServiceDeployments-request-maxResults"></a>
The maximum number of service deployment results that `ListServiceDeployments` returned in paginated output. When this parameter is used, `ListServiceDeployments` only returns `maxResults` results in a single page along with a `nextToken` response element. The remaining results of the initial request can be seen by sending another `ListServiceDeployments` request with the returned `nextToken` value. This value can be between 1 and 100. If this parameter isn't used, then `ListServiceDeployments` returns up to 20 results and a `nextToken` value if applicable.
Type: Integer
Required: No

 ** [nextToken](#API_ListServiceDeployments_RequestSyntax) **   <a name="ECS-ListServiceDeployments-request-nextToken"></a>
The `nextToken` value returned from a `ListServiceDeployments` request indicating that more results are available to fulfill the request and further calls are needed. If you provided `maxResults`, it's possible the number of results is fewer than `maxResults`.
Type: String
Required: No

 ** [service](#API_ListServiceDeployments_RequestSyntax) **   <a name="ECS-ListServiceDeployments-request-service"></a>
The ARN or name of the service
Type: String
Required: Yes

 ** [status](#API_ListServiceDeployments_RequestSyntax) **   <a name="ECS-ListServiceDeployments-request-status"></a>
An optional filter you can use to narrow the results. If you do not specify a status, then all status values are included in the result.
Type: Array of strings
Valid Values: `PENDING | SUCCESSFUL | STOPPED | STOP_REQUESTED | IN_PROGRESS | ROLLBACK_REQUESTED | ROLLBACK_IN_PROGRESS | ROLLBACK_SUCCESSFUL | ROLLBACK_FAILED`
Required: No

## Response Syntax
<a name="API_ListServiceDeployments_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "serviceDeployments": [
      {
         "clusterArn": "string",
         "createdAt": number,
         "finishedAt": number,
         "serviceArn": "string",
         "serviceDeploymentArn": "string",
         "startedAt": number,
         "status": "string",
         "statusReason": "string",
         "targetServiceRevisionArn": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListServiceDeployments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListServiceDeployments_ResponseSyntax) **   <a name="ECS-ListServiceDeployments-response-nextToken"></a>
The `nextToken` value to include in a future `ListServiceDeployments` request. When the results of a `ListServiceDeployments` request exceed `maxResults`, this value can be used to retrieve the next page of results. This value is null when there are no more results to return.
Type: String

 ** [serviceDeployments](#API_ListServiceDeployments_ResponseSyntax) **   <a name="ECS-ListServiceDeployments-response-serviceDeployments"></a>
An overview of the service deployment, including the following properties:
+ The ARN of the service deployment.
+ The ARN of the service being deployed.
+ The ARN of the cluster that hosts the service in the service deployment.
+ The time that the service deployment started.
+ The time that the service deployment completed.
+ The service deployment status.
+ Information about why the service deployment is in the current state.
+ The ARN of the service revision that is being deployed.
Type: Array of [ServiceDeploymentBrief](API_ServiceDeploymentBrief.md) objects

## Errors
<a name="API_ListServiceDeployments_Errors"></a>

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

 ** ServiceNotFoundException **
The specified service wasn't found. You can view your available services with [ListServices](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServices.html). Amazon ECS services are cluster specific and Region specific.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** UnsupportedFeatureException **
The specified task isn't supported in this Region.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

## Examples
<a name="API_ListServiceDeployments_Examples"></a>

### Example
<a name="API_ListServiceDeployments_Example_1"></a>

This example request lists the service deployments for the `sd-example` service on the `example` cluster.

#### Sample Request
<a name="API_ListServiceDeployments_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ecs.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 55
X-Amz-Target: AmazonEC2ContainerServiceV20141113.DescribeServiceDeployments
X-Amz-Date: 20150528T163859Z
User-Agent: aws-cli/2.17 Python/3.11.9 Darwin/14.3.0
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS
{
  "cluster": "example",
  "service": "sd-example"
}
```

#### Sample Response
<a name="API_ListServiceDeployments_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Tue, 10 Sep 2024 18:50:14 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 220
Connection: keep-alive
RequestId: 360c5551-123e-4e74-9914-7582d3a28807
{
    "serviceDeployments": [
        {
            "serviceDeploymentArn": "arn:aws:ecs:us-west-2:123456789012:service-deployment/example/sd-example/NCWGC2ZR-taawPAYrIaU5",
            "serviceArn": "arn:aws:ecs:us-west-2:123456789012:service/example/sd-example",
            "clusterArn": "arn:aws:ecs:us-west-2:123456789012:cluster/example",
            "targetServiceRevisionArn": "arn:aws:ecs:us-west-2:123456789012:service-revision/example/sd-example/4980306466373577095",
            "status": "SUCCESSFUL"
        }
    ]
}
```

## See Also
<a name="API_ListServiceDeployments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/ListServiceDeployments)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/ListServiceDeployments)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ListServiceDeployments)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/ListServiceDeployments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ListServiceDeployments)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/ListServiceDeployments)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/ListServiceDeployments)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/ListServiceDeployments)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/ListServiceDeployments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ListServiceDeployments)
