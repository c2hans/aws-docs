---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_GetTaskProtection.html
---

# GetTaskProtection
<a name="API_GetTaskProtection"></a>

Retrieves the protection status of tasks in an Amazon ECS service.

## Request Syntax
<a name="API_GetTaskProtection_RequestSyntax"></a>

```
{
   "cluster": "{{string}}",
   "tasks": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_GetTaskProtection_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [cluster](#API_GetTaskProtection_RequestSyntax) **   <a name="ECS-GetTaskProtection-request-cluster"></a>
The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service that the task sets exist in.
Type: String
Required: Yes

 ** [tasks](#API_GetTaskProtection_RequestSyntax) **   <a name="ECS-GetTaskProtection-request-tasks"></a>
A list of up to 100 task IDs or full ARN entries.
Type: Array of strings
Required: No

## Response Syntax
<a name="API_GetTaskProtection_ResponseSyntax"></a>

```
{
   "failures": [
      {
         "arn": "string",
         "detail": "string",
         "reason": "string"
      }
   ],
   "protectedTasks": [
      {
         "expirationDate": number,
         "protectionEnabled": boolean,
         "taskArn": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetTaskProtection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [failures](#API_GetTaskProtection_ResponseSyntax) **   <a name="ECS-GetTaskProtection-response-failures"></a>
Any failures associated with the call.
Type: Array of [Failure](API_Failure.md) objects

 ** [protectedTasks](#API_GetTaskProtection_ResponseSyntax) **   <a name="ECS-GetTaskProtection-response-protectedTasks"></a>
A list of tasks with the following information.
+  `taskArn`: The task ARN.
+  `protectionEnabled`: The protection status of the task. If scale-in protection is turned on for a task, the value is `true`. Otherwise, it is `false`.
+  `expirationDate`: The epoch time when protection for the task will expire.
Type: Array of [ProtectedTask](API_ProtectedTask.md) objects

## Errors
<a name="API_GetTaskProtection_Errors"></a>

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

 ** ResourceNotFoundException **
The specified resource wasn't found.
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
<a name="API_GetTaskProtection_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to create them manually. When you use the [AWS Command Line Interface](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you, with the access key that you specify when you configure the tools. When you use these tools, you don't have to sign requests yourself.

### Example
<a name="API_GetTaskProtection_Example_1"></a>

This example request gets the protection status for a task.

#### Sample Request
<a name="API_GetTaskProtection_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ecs.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length:81
X-Amz-Target: AmazonEC2ContainerServiceV20141113.GetTaskProtection
X-Amz-Date: 20221102T190406Z
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
    "cluster": "test-task-protection",
    "tasks": [
        "b8b1cf532d0e46ba8d44a40d1de16772"
    ]
}
```

#### Sample Response
<a name="API_GetTaskProtection_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Wed, 02 Nov 2022 19:04:06 GMT
Content-Type: application/x-amz-json-1.1
Content-Length:177
Connection: keep-alive
x-amzn-RequestId: 123a4b56-7c89-01d2-3ef4-example5678f

{
    "protectedTasks": [
        {
            "taskArn": "arn:aws:ecs:us-west-2:012345678910:task/b8b1cf532d0e46ba8d44a40d1de16772",
            "protectionEnabled": true,
            "expirationDate": 1667416437.0
        }
    ],
    "failures": []
}
```

## See Also
<a name="API_GetTaskProtection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/GetTaskProtection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/GetTaskProtection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/GetTaskProtection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/GetTaskProtection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/GetTaskProtection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/GetTaskProtection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/GetTaskProtection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/GetTaskProtection)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/GetTaskProtection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/GetTaskProtection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
