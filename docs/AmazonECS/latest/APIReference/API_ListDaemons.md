---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListDaemons.html
---

# ListDaemons
<a name="API_ListDaemons"></a>

Returns a list of daemons. You can filter the results by cluster or capacity provider.

## Request Syntax
<a name="API_ListDaemons_RequestSyntax"></a>

```
{
   "capacityProviderArns": [ "{{string}}" ],
   "clusterArn": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListDaemons_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [capacityProviderArns](#API_ListDaemons_RequestSyntax) **   <a name="ECS-ListDaemons-request-capacityProviderArns"></a>
The Amazon Resource Names (ARNs) of the capacity providers to filter daemons by. Only daemons associated with the specified capacity providers are returned.
Type: Array of strings
Required: No

 ** [clusterArn](#API_ListDaemons_RequestSyntax) **   <a name="ECS-ListDaemons-request-clusterArn"></a>
The Amazon Resource Name (ARN) of the cluster to filter daemons by. If you do not specify a cluster, the default cluster is assumed.
Type: String
Required: No

 ** [maxResults](#API_ListDaemons_RequestSyntax) **   <a name="ECS-ListDaemons-request-maxResults"></a>
The maximum number of daemon results that `ListDaemons` returned in paginated output. When this parameter is used, `ListDaemons` only returns `maxResults` results in a single page along with a `nextToken` response element. The remaining results of the initial request can be seen by sending another `ListDaemons` request with the returned `nextToken` value. This value can be between 1 and 100. If this parameter isn't used, then `ListDaemons` returns up to 100 results and a `nextToken` value if applicable.
Type: Integer
Required: No

 ** [nextToken](#API_ListDaemons_RequestSyntax) **   <a name="ECS-ListDaemons-request-nextToken"></a>
The `nextToken` value returned from a `ListDaemons` request indicating that more results are available to fulfill the request and further calls will be needed. If `maxResults` was provided, it's possible for the number of results to be fewer than `maxResults`.
This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
Type: String
Required: No

## Response Syntax
<a name="API_ListDaemons_ResponseSyntax"></a>

```
{
   "daemonSummariesList": [
      {
         "createdAt": number,
         "daemonArn": "string",
         "status": "string",
         "updatedAt": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListDaemons_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [daemonSummariesList](#API_ListDaemons_ResponseSyntax) **   <a name="ECS-ListDaemons-response-daemonSummariesList"></a>
The list of daemon summaries.
Type: Array of [DaemonSummary](API_DaemonSummary.md) objects

 ** [nextToken](#API_ListDaemons_ResponseSyntax) **   <a name="ECS-ListDaemons-response-nextToken"></a>
The `nextToken` value to include in a future `ListDaemons` request. When the results of a `ListDaemons` request exceed `maxResults`, this value can be used to retrieve the next page of results.
Type: String

## Errors
<a name="API_ListDaemons_Errors"></a>

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

 ** UnsupportedFeatureException **
The specified task isn't supported in this Region.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

## Examples
<a name="API_ListDaemons_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to create them manually. When you use the [AWS Command Line Interface](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you, with the access key that you specify when you configure the tools. When you use these tools, you don't have to sign requests yourself.

### Example
<a name="API_ListDaemons_Example_1"></a>

This example lists all daemons in the specified cluster.

#### Sample Request
<a name="API_ListDaemons_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ecs.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 75
X-Amz-Target: AmazonEC2ContainerServiceV20141113.ListDaemons
X-Amz-Date: 20250320T160500Z
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
  "clusterArn": "arn:aws:ecs:us-east-1:123456789012:cluster/my-cluster"
}
```

#### Sample Response
<a name="API_ListDaemons_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Thu, 20 Mar 2025 16:05:00 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 486
Connection: keep-alive
x-amzn-RequestId: 123a4b56-7c89-01d2-3ef4-example5678f

{
  "daemonSummariesList": [
    {
      "daemonArn": "arn:aws:ecs:us-east-1:123456789012:daemon/my-cluster/my-monitoring-daemon",
      "status": "ACTIVE",
      "createdAt": "2025-03-15T12:00:00.000Z",
      "updatedAt": "2025-03-20T15:30:00.000Z"
    },
    {
      "daemonArn": "arn:aws:ecs:us-east-1:123456789012:daemon/my-cluster/my-logging-daemon",
      "status": "ACTIVE",
      "createdAt": "2025-03-16T09:00:00.000Z",
      "updatedAt": "2025-03-16T09:00:00.000Z"
    }
  ]
}
```

## See Also
<a name="API_ListDaemons_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/ListDaemons)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/ListDaemons)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ListDaemons)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/ListDaemons)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ListDaemons)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/ListDaemons)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/ListDaemons)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/ListDaemons)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/ListDaemons)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ListDaemons)
