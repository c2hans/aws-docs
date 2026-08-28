---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeleteDaemon.html
---

# DeleteDaemon
<a name="API_DeleteDaemon"></a>

Deletes the specified daemon. The daemon must be in an `ACTIVE` state to be deleted. Deleting a daemon stops all running daemon tasks on the associated container instances. Amazon ECS drains existing container instances and provisions new instances without the deleted daemon. Amazon ECS automatically launches replacement tasks for your Amazon ECS services.

**Note**
ECS Managed Daemons is only supported for Amazon ECS Managed Instances Capacity Providers.

## Request Syntax
<a name="API_DeleteDaemon_RequestSyntax"></a>

```
{
   "daemonArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteDaemon_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [daemonArn](#API_DeleteDaemon_RequestSyntax) **   <a name="ECS-DeleteDaemon-request-daemonArn"></a>
The Amazon Resource Name (ARN) of the daemon to delete.
Type: String
Required: Yes

## Response Syntax
<a name="API_DeleteDaemon_ResponseSyntax"></a>

```
{
   "createdAt": number,
   "daemonArn": "string",
   "deploymentArn": "string",
   "status": "string",
   "updatedAt": number
}
```

## Response Elements
<a name="API_DeleteDaemon_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_DeleteDaemon_ResponseSyntax) **   <a name="ECS-DeleteDaemon-response-createdAt"></a>
The Unix timestamp for the time when the daemon was created.
Type: Timestamp

 ** [daemonArn](#API_DeleteDaemon_ResponseSyntax) **   <a name="ECS-DeleteDaemon-response-daemonArn"></a>
The Amazon Resource Name (ARN) of the daemon.
Type: String

 ** [deploymentArn](#API_DeleteDaemon_ResponseSyntax) **   <a name="ECS-DeleteDaemon-response-deploymentArn"></a>
The Amazon Resource Name (ARN) of the daemon deployment that was triggered by the delete operation. This deployment drains existing daemon tasks from the container instances.
Type: String

 ** [status](#API_DeleteDaemon_ResponseSyntax) **   <a name="ECS-DeleteDaemon-response-status"></a>
The status of the daemon. After you call `DeleteDaemon`, the status changes to `DELETE_IN_PROGRESS`.
Type: String
Valid Values: `ACTIVE | DELETE_IN_PROGRESS`

 ** [updatedAt](#API_DeleteDaemon_ResponseSyntax) **   <a name="ECS-DeleteDaemon-response-updatedAt"></a>
The Unix timestamp for the time when the daemon was last updated.
Type: Timestamp

## Errors
<a name="API_DeleteDaemon_Errors"></a>

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

 ** DaemonNotActiveException **
The specified daemon isn't active. You can't update a daemon that's inactive. If you have previously deleted a daemon, you can re-create it with [CreateDaemon](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateDaemon.html).
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** DaemonNotFoundException **
The specified daemon wasn't found. You can view your available daemons with [ListDaemons](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListDaemons.html). Amazon ECS daemons are cluster specific and Region specific.
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
<a name="API_DeleteDaemon_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to create them manually. When you use the [AWS Command Line Interface](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you, with the access key that you specify when you configure the tools. When you use these tools, you don't have to sign requests yourself.

### Example
<a name="API_DeleteDaemon_Example_1"></a>

This example deletes the my-monitoring-daemon daemon.

#### Sample Request
<a name="API_DeleteDaemon_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ecs.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 94
X-Amz-Target: AmazonEC2ContainerServiceV20141113.DeleteDaemon
X-Amz-Date: 20250325T090000Z
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
  "daemonArn": "arn:aws:ecs:us-east-1:123456789012:daemon/my-cluster/my-monitoring-daemon"
}
```

#### Sample Response
<a name="API_DeleteDaemon_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Tue, 25 Mar 2025 09:00:00 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 338
Connection: keep-alive
x-amzn-RequestId: 123a4b56-7c89-01d2-3ef4-example5678f

{
  "daemonArn": "arn:aws:ecs:us-east-1:123456789012:daemon/my-cluster/my-monitoring-daemon",
  "status": "DELETE_IN_PROGRESS",
  "createdAt": "2025-03-15T12:00:00.000Z",
  "updatedAt": "2025-03-25T09:00:00.000Z",
  "deploymentArn": "arn:aws:ecs:us-east-1:123456789012:daemon-deployment/my-cluster/my-monitoring-daemon/mN3oP4qR5sT6uV7w"
}
```

## See Also
<a name="API_DeleteDaemon_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/DeleteDaemon)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/DeleteDaemon)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/DeleteDaemon)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/DeleteDaemon)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DeleteDaemon)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/DeleteDaemon)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/DeleteDaemon)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/DeleteDaemon)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/DeleteDaemon)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/DeleteDaemon)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
