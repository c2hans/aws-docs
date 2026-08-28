---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeleteDaemonTaskDefinition.html
---

# DeleteDaemonTaskDefinition
<a name="API_DeleteDaemonTaskDefinition"></a>

Deletes the specified daemon task definition. After a daemon task definition is deleted, no new daemons can be created using this definition. Existing daemons that reference the deleted daemon task definition continue to run.

A daemon task definition must be in an `ACTIVE` state to be deleted.

## Request Syntax
<a name="API_DeleteDaemonTaskDefinition_RequestSyntax"></a>

```
{
   "daemonTaskDefinition": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteDaemonTaskDefinition_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [daemonTaskDefinition](#API_DeleteDaemonTaskDefinition_RequestSyntax) **   <a name="ECS-DeleteDaemonTaskDefinition-request-daemonTaskDefinition"></a>
The `family` and `revision` (`family:revision`) or full Amazon Resource Name (ARN) of the daemon task definition to delete.
Type: String
Required: Yes

## Response Syntax
<a name="API_DeleteDaemonTaskDefinition_ResponseSyntax"></a>

```
{
   "daemonTaskDefinitionArn": "string"
}
```

## Response Elements
<a name="API_DeleteDaemonTaskDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [daemonTaskDefinitionArn](#API_DeleteDaemonTaskDefinition_ResponseSyntax) **   <a name="ECS-DeleteDaemonTaskDefinition-response-daemonTaskDefinitionArn"></a>
The full Amazon Resource Name (ARN) of the deleted daemon task definition.
Type: String

## Errors
<a name="API_DeleteDaemonTaskDefinition_Errors"></a>

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
<a name="API_DeleteDaemonTaskDefinition_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to create them manually. When you use the [AWS Command Line Interface](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you, with the access key that you specify when you configure the tools. When you use these tools, you don't have to sign requests yourself.

### Example
<a name="API_DeleteDaemonTaskDefinition_Example_1"></a>

This example deletes the first revision of the monitoring-agent daemon task definition.

#### Sample Request
<a name="API_DeleteDaemonTaskDefinition_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ecs.us-east-1.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonEC2ContainerServiceV20141113.DeleteDaemonTaskDefinition
X-Amz-Date: 20250315T103000Z
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
  "daemonTaskDefinition": "monitoring-agent:1"
}
```

#### Sample Response
<a name="API_DeleteDaemonTaskDefinition_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Sat, 15 Mar 2025 10:30:00 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 97
Connection: keep-alive
x-amzn-RequestId: 123a4b56-7c89-01d2-3ef4-example5678f

{
  "daemonTaskDefinitionArn": "arn:aws:ecs:us-east-1:123456789012:daemon-task-definition/monitoring-agent:1"
}
```

## See Also
<a name="API_DeleteDaemonTaskDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/DeleteDaemonTaskDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/DeleteDaemonTaskDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/DeleteDaemonTaskDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/DeleteDaemonTaskDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DeleteDaemonTaskDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/DeleteDaemonTaskDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/DeleteDaemonTaskDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/DeleteDaemonTaskDefinition)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/DeleteDaemonTaskDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/DeleteDaemonTaskDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
