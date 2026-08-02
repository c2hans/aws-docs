---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServices.html
---

# ListServices
<a name="API_ListServices"></a>

Returns a list of services. You can filter the results by cluster, launch type, and scheduling strategy.

## Request Syntax
<a name="API_ListServices_RequestSyntax"></a>

```
{
   "cluster": "{{string}}",
   "launchType": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "resourceManagementType": "{{string}}",
   "schedulingStrategy": "{{string}}"
}
```

## Request Parameters
<a name="API_ListServices_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [cluster](#API_ListServices_RequestSyntax) **   <a name="ECS-ListServices-request-cluster"></a>
The short name or full Amazon Resource Name (ARN) of the cluster to use when filtering the `ListServices` results. If you do not specify a cluster, the default cluster is assumed.
Type: String
Required: No

 ** [launchType](#API_ListServices_RequestSyntax) **   <a name="ECS-ListServices-request-launchType"></a>
The launch type to use when filtering the `ListServices` results.
Type: String
Valid Values: `EC2 | FARGATE | EXTERNAL | MANAGED_INSTANCES`
Required: No

 ** [maxResults](#API_ListServices_RequestSyntax) **   <a name="ECS-ListServices-request-maxResults"></a>
The maximum number of service results that `ListServices` returned in paginated output. When this parameter is used, `ListServices` only returns `maxResults` results in a single page along with a `nextToken` response element. The remaining results of the initial request can be seen by sending another `ListServices` request with the returned `nextToken` value. This value can be between 1 and 100. If this parameter isn't used, then `ListServices` returns up to 10 results and a `nextToken` value if applicable.
Type: Integer
Required: No

 ** [nextToken](#API_ListServices_RequestSyntax) **   <a name="ECS-ListServices-request-nextToken"></a>
The `nextToken` value returned from a `ListServices` request indicating that more results are available to fulfill the request and further calls will be needed. If `maxResults` was provided, it is possible the number of results to be fewer than `maxResults`.
This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
Type: String
Required: No

 ** [resourceManagementType](#API_ListServices_RequestSyntax) **   <a name="ECS-ListServices-request-resourceManagementType"></a>
The resourceManagementType type to use when filtering the `ListServices` results.
Type: String
Valid Values: `CUSTOMER | ECS`
Required: No

 ** [schedulingStrategy](#API_ListServices_RequestSyntax) **   <a name="ECS-ListServices-request-schedulingStrategy"></a>
The scheduling strategy to use when filtering the `ListServices` results.
Type: String
Valid Values: `REPLICA | DAEMON`
Required: No

## Response Syntax
<a name="API_ListServices_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "serviceArns": [ "string" ]
}
```

## Response Elements
<a name="API_ListServices_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListServices_ResponseSyntax) **   <a name="ECS-ListServices-response-nextToken"></a>
The `nextToken` value to include in a future `ListServices` request. When the results of a `ListServices` request exceed `maxResults`, this value can be used to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 ** [serviceArns](#API_ListServices_ResponseSyntax) **   <a name="ECS-ListServices-response-serviceArns"></a>
The list of full ARN entries for each service that's associated with the specified cluster.
Type: Array of strings

## Errors
<a name="API_ListServices_Errors"></a>

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
<a name="API_ListServices_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to create them manually. When you use the [AWS Command Line Interface](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you, with the access key that you specify when you configure the tools. When you use these tools, you don't have to sign requests yourself.

### Example
<a name="API_ListServices_Example_1"></a>

This example request lists the services in the default cluster.

#### Sample Request
<a name="API_ListServices_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ecs.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 2
X-Amz-Target: AmazonEC2ContainerServiceV20141113.ListServices
X-Amz-Date: 20150429T191342Z
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{}
```

#### Sample Response
<a name="API_ListServices_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Wed, 29 Apr 2015 19:13:42 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 138
Connection: keep-alive
x-amzn-RequestId: 123a4b56-7c89-01d2-3ef4-example5678f

{
  "serviceArns": [
    "arn:aws:ecs:us-east-1:111122223333:service/default/hello_world",
    "arn:aws:ecs:us-east-1:111122223333:service/default/ecs-simple-service"
  ]
}
```

## See Also
<a name="API_ListServices_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/ListServices)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/ListServices)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ListServices)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/ListServices)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ListServices)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/ListServices)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/ListServices)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/ListServices)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/ListServices)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ListServices)
