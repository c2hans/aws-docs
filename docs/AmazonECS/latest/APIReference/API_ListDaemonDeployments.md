---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListDaemonDeployments.html
---

# ListDaemonDeployments
<a name="API_ListDaemonDeployments"></a>

Returns a list of daemon deployments for a specified daemon. You can filter the results by status or creation time.

## Request Syntax
<a name="API_ListDaemonDeployments_RequestSyntax"></a>

```
{
   "createdAt": {
      "after": {{number}},
      "before": {{number}}
   },
   "daemonArn": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "status": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_ListDaemonDeployments_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [createdAt](#API_ListDaemonDeployments_RequestSyntax) **   <a name="ECS-ListDaemonDeployments-request-createdAt"></a>
An optional filter to narrow the `ListDaemonDeployments` results by creation time. If you don't specify a time range, all deployments are returned.
Type: [CreatedAt](API_CreatedAt.md) object
Required: No

 ** [daemonArn](#API_ListDaemonDeployments_RequestSyntax) **   <a name="ECS-ListDaemonDeployments-request-daemonArn"></a>
The Amazon Resource Name (ARN) of the daemon to list deployments for.
Type: String
Required: Yes

 ** [maxResults](#API_ListDaemonDeployments_RequestSyntax) **   <a name="ECS-ListDaemonDeployments-request-maxResults"></a>
The maximum number of daemon deployment results that `ListDaemonDeployments` returned in paginated output. When this parameter is used, `ListDaemonDeployments` only returns `maxResults` results in a single page along with a `nextToken` response element. The remaining results of the initial request can be seen by sending another `ListDaemonDeployments` request with the returned `nextToken` value. This value can be between 1 and 100. If this parameter isn't used, then `ListDaemonDeployments` returns up to 20 results and a `nextToken` value if applicable.
Type: Integer
Required: No

 ** [nextToken](#API_ListDaemonDeployments_RequestSyntax) **   <a name="ECS-ListDaemonDeployments-request-nextToken"></a>
The `nextToken` value returned from a `ListDaemonDeployments` request indicating that more results are available to fulfill the request and further calls will be needed. If `maxResults` was provided, it's possible for the number of results to be fewer than `maxResults`.
This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
Type: String
Required: No

 ** [status](#API_ListDaemonDeployments_RequestSyntax) **   <a name="ECS-ListDaemonDeployments-request-status"></a>
An optional filter to narrow the `ListDaemonDeployments` results by deployment status. If you don't specify a status, all deployments are returned.
Type: Array of strings
Valid Values: `PENDING | SUCCESSFUL | STOPPED | STOP_REQUESTED | IN_PROGRESS | ROLLBACK_IN_PROGRESS | ROLLBACK_SUCCESSFUL | ROLLBACK_FAILED`
Required: No

## Response Syntax
<a name="API_ListDaemonDeployments_ResponseSyntax"></a>

```
{
   "daemonDeployments": [
      {
         "clusterArn": "string",
         "createdAt": number,
         "daemonArn": "string",
         "daemonDeploymentArn": "string",
         "finishedAt": number,
         "startedAt": number,
         "status": "string",
         "statusReason": "string",
         "stoppedAt": number,
         "targetDaemonRevisionArn": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListDaemonDeployments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [daemonDeployments](#API_ListDaemonDeployments_ResponseSyntax) **   <a name="ECS-ListDaemonDeployments-response-daemonDeployments"></a>
The list of daemon deployment summaries.
Type: Array of [DaemonDeploymentSummary](API_DaemonDeploymentSummary.md) objects

 ** [nextToken](#API_ListDaemonDeployments_ResponseSyntax) **   <a name="ECS-ListDaemonDeployments-response-nextToken"></a>
The `nextToken` value to include in a future `ListDaemonDeployments` request. When the results of a `ListDaemonDeployments` request exceed `maxResults`, this value can be used to retrieve the next page of results.
Type: String

## Errors
<a name="API_ListDaemonDeployments_Errors"></a>

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
<a name="API_ListDaemonDeployments_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to create them manually. When you use the [AWS Command Line Interface](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you, with the access key that you specify when you configure the tools. When you use these tools, you don't have to sign requests yourself.

### Example
<a name="API_ListDaemonDeployments_Example_1"></a>

This example lists all successful daemon deployments for the my-monitoring-daemon daemon.

#### Sample Request
<a name="API_ListDaemonDeployments_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ecs.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 130
X-Amz-Target: AmazonEC2ContainerServiceV20141113.ListDaemonDeployments
X-Amz-Date: 20250320T162000Z
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
  "daemonArn": "arn:aws:ecs:us-east-1:123456789012:daemon/my-cluster/my-monitoring-daemon",
  "status": [
    "SUCCESSFUL"
  ]
}
```

#### Sample Response
<a name="API_ListDaemonDeployments_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Thu, 20 Mar 2025 16:20:00 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 721
Connection: keep-alive
x-amzn-RequestId: 123a4b56-7c89-01d2-3ef4-example5678f

{
  "daemonDeployments": [
    {
      "daemonDeploymentArn": "arn:aws:ecs:us-east-1:123456789012:daemon-deployment/my-cluster/my-monitoring-daemon/aB1cD2eF3gH4iJ5k",
      "daemonArn": "arn:aws:ecs:us-east-1:123456789012:daemon/my-cluster/my-monitoring-daemon",
      "clusterArn": "arn:aws:ecs:us-east-1:123456789012:cluster/my-cluster",
      "status": "SUCCESSFUL",
      "statusReason": "Deployment completed successfully.",
      "targetDaemonRevisionArn": "arn:aws:ecs:us-east-1:123456789012:daemon-revision/my-cluster/my-monitoring-daemon/4980306466373577095",
      "createdAt": "2025-03-15T12:00:00.000Z",
      "startedAt": "2025-03-15T12:00:05.000Z",
      "finishedAt": "2025-03-15T12:15:00.000Z"
    }
  ]
}
```

## See Also
<a name="API_ListDaemonDeployments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/ListDaemonDeployments)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/ListDaemonDeployments)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ListDaemonDeployments)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/ListDaemonDeployments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ListDaemonDeployments)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/ListDaemonDeployments)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/ListDaemonDeployments)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/ListDaemonDeployments)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/ListDaemonDeployments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ListDaemonDeployments)
