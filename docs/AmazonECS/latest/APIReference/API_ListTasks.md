---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListTasks.html
---

# ListTasks
<a name="API_ListTasks"></a>

Returns a list of tasks. You can filter the results by cluster, task definition family, container instance, launch type, what IAM principal started the task, or by the desired status of the task.

Recently stopped tasks might appear in the returned results.

## Request Syntax
<a name="API_ListTasks_RequestSyntax"></a>

```
{
   "cluster": "{{string}}",
   "containerInstance": "{{string}}",
   "daemonName": "{{string}}",
   "desiredStatus": "{{string}}",
   "family": "{{string}}",
   "launchType": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "serviceName": "{{string}}",
   "startedBy": "{{string}}"
}
```

## Request Parameters
<a name="API_ListTasks_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [cluster](#API_ListTasks_RequestSyntax) **   <a name="ECS-ListTasks-request-cluster"></a>
The short name or full Amazon Resource Name (ARN) of the cluster to use when filtering the `ListTasks` results. If you do not specify a cluster, the default cluster is assumed.
Type: String
Required: No

 ** [containerInstance](#API_ListTasks_RequestSyntax) **   <a name="ECS-ListTasks-request-containerInstance"></a>
The container instance ID or full ARN of the container instance to use when filtering the `ListTasks` results. Specifying a `containerInstance` limits the results to tasks that belong to that container instance.
Type: String
Required: No

 ** [daemonName](#API_ListTasks_RequestSyntax) **   <a name="ECS-ListTasks-request-daemonName"></a>
The name of the daemon to use when filtering the `ListTasks` results. Specifying a `daemonName` limits the results to tasks that belong to that daemon.
Type: String
Required: No

 ** [desiredStatus](#API_ListTasks_RequestSyntax) **   <a name="ECS-ListTasks-request-desiredStatus"></a>
The task desired status to use when filtering the `ListTasks` results. Specifying a `desiredStatus` of `STOPPED` limits the results to tasks that Amazon ECS has set the desired status to `STOPPED`. This can be useful for debugging tasks that aren't starting properly or have died or finished. The default status filter is `RUNNING`, which shows tasks that Amazon ECS has set the desired status to `RUNNING`.
Although you can filter results based on a desired status of `PENDING`, this doesn't return any results. Amazon ECS never sets the desired status of a task to that value (only a task's `lastStatus` may have a value of `PENDING`).
Type: String
Valid Values: `RUNNING | PENDING | STOPPED`
Required: No

 ** [family](#API_ListTasks_RequestSyntax) **   <a name="ECS-ListTasks-request-family"></a>
The name of the task definition family to use when filtering the `ListTasks` results. Specifying a `family` limits the results to tasks that belong to that family.
Type: String
Required: No

 ** [launchType](#API_ListTasks_RequestSyntax) **   <a name="ECS-ListTasks-request-launchType"></a>
The launch type to use when filtering the `ListTasks` results.
Type: String
Valid Values: `EC2 | FARGATE | EXTERNAL | MANAGED_INSTANCES`
Required: No

 ** [maxResults](#API_ListTasks_RequestSyntax) **   <a name="ECS-ListTasks-request-maxResults"></a>
The maximum number of task results that `ListTasks` returned in paginated output. When this parameter is used, `ListTasks` only returns `maxResults` results in a single page along with a `nextToken` response element. The remaining results of the initial request can be seen by sending another `ListTasks` request with the returned `nextToken` value. This value can be between 1 and 100. If this parameter isn't used, then `ListTasks` returns up to 100 results and a `nextToken` value if applicable.
Type: Integer
Required: No

 ** [nextToken](#API_ListTasks_RequestSyntax) **   <a name="ECS-ListTasks-request-nextToken"></a>
The `nextToken` value returned from a `ListTasks` request indicating that more results are available to fulfill the request and further calls will be needed. If `maxResults` was provided, it's possible the number of results to be fewer than `maxResults`.
This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
Type: String
Required: No

 ** [serviceName](#API_ListTasks_RequestSyntax) **   <a name="ECS-ListTasks-request-serviceName"></a>
The name of the service to use when filtering the `ListTasks` results. Specifying a `serviceName` limits the results to tasks that belong to that service.
Type: String
Required: No

 ** [startedBy](#API_ListTasks_RequestSyntax) **   <a name="ECS-ListTasks-request-startedBy"></a>
The `startedBy` value to filter the task results with. Specifying a `startedBy` value limits the results to tasks that were started with that value.
When you specify `startedBy` as the filter, it must be the only filter that you use.
Type: String
Required: No

## Response Syntax
<a name="API_ListTasks_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "taskArns": [ "string" ]
}
```

## Response Elements
<a name="API_ListTasks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListTasks_ResponseSyntax) **   <a name="ECS-ListTasks-response-nextToken"></a>
The `nextToken` value to include in a future `ListTasks` request. When the results of a `ListTasks` request exceed `maxResults`, this value can be used to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 ** [taskArns](#API_ListTasks_ResponseSyntax) **   <a name="ECS-ListTasks-response-taskArns"></a>
The list of task ARN entries for the `ListTasks` request.
Type: Array of strings

## Errors
<a name="API_ListTasks_Errors"></a>

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

## Examples
<a name="API_ListTasks_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to create them manually. When you use the [AWS Command Line Interface](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you, with the access key that you specify when you configure the tools. When you use these tools, you don't have to sign requests yourself.

### Example
<a name="API_ListTasks_Example_1"></a>

This example request lists all of the tasks in the default cluster.

#### Sample Request
<a name="API_ListTasks_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ecs.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 2
X-Amz-Target: AmazonEC2ContainerServiceV20141113.ListTasks
X-Amz-Date: 20150429T192615Z
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{}
```

#### Sample Response
<a name="API_ListTasks_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Wed, 29 Apr 2015 19:26:16 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 330
Connection: keep-alive
x-amzn-RequestId: 123a4b56-7c89-01d2-3ef4-example5678f

{
  "taskArns": [
    "arn:aws:ecs:us-east-1:012345678910:task/0b69d5c0-d655-4695-98cd-5d2d526d9d5a",
    "arn:aws:ecs:us-east-1:012345678910:task/51a01bdf-d00e-487e-ab14-7645330b6207",
    "arn:aws:ecs:us-east-1:012345678910:task/b0b28bb8-2be3-4810-b52b-88df129d893c",
    "arn:aws:ecs:us-east-1:012345678910:task/c09f0188-7f87-4b0f-bfc3-16296622b6fe"
  ]
}
```

## See Also
<a name="API_ListTasks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/ListTasks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/ListTasks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ListTasks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/ListTasks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ListTasks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/ListTasks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/ListTasks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/ListTasks)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/ListTasks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ListTasks)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
