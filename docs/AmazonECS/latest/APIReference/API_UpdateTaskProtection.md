---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateTaskProtection.html
---

# UpdateTaskProtection
<a name="API_UpdateTaskProtection"></a>

Updates the protection status of a task. You can set `protectionEnabled` to `true` to protect your task from termination during scale-in events from [Service Autoscaling](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-auto-scaling.html) or [deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html).

Task-protection, by default, expires after 2 hours at which point Amazon ECS clears the `protectionEnabled` property making the task eligible for termination by a subsequent scale-in event.

You can specify a custom expiration period for task protection from 1 minute to up to 2,880 minutes (48 hours). To specify the custom expiration period, set the `expiresInMinutes` property. The `expiresInMinutes` property is always reset when you invoke this operation for a task that already has `protectionEnabled` set to `true`. You can keep extending the protection expiration period of a task by invoking this operation repeatedly.

To learn more about Amazon ECS task protection, see [Task scale-in protection](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-scale-in-protection.html) in the * *Amazon Elastic Container Service Developer Guide* *.

**Note**
This operation is only supported for tasks belonging to an Amazon ECS service. Invoking this operation for a standalone task will result in an `TASK_NOT_VALID` failure. For more information, see [API failure reasons](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/api_failures_messages.html).

**Important**
If you prefer to set task protection from within the container, we recommend using the [Task scale-in protection endpoint](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-scale-in-protection-endpoint.html).

## Request Syntax
<a name="API_UpdateTaskProtection_RequestSyntax"></a>

```
{
   "cluster": "{{string}}",
   "expiresInMinutes": {{number}},
   "protectionEnabled": {{boolean}},
   "tasks": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_UpdateTaskProtection_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [cluster](#API_UpdateTaskProtection_RequestSyntax) **   <a name="ECS-UpdateTaskProtection-request-cluster"></a>
The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service that the task sets exist in.
Type: String
Required: Yes

 ** [expiresInMinutes](#API_UpdateTaskProtection_RequestSyntax) **   <a name="ECS-UpdateTaskProtection-request-expiresInMinutes"></a>
If you set `protectionEnabled` to `true`, you can specify the duration for task protection in minutes. You can specify a value from 1 minute to up to 2,880 minutes (48 hours). During this time, your task will not be terminated by scale-in events from Service Auto Scaling or deployments. After this time period lapses, `protectionEnabled` will be reset to `false`.
If you don’t specify the time, then the task is automatically protected for 120 minutes (2 hours).
Type: Integer
Required: No

 ** [protectionEnabled](#API_UpdateTaskProtection_RequestSyntax) **   <a name="ECS-UpdateTaskProtection-request-protectionEnabled"></a>
Specify `true` to mark a task for protection and `false` to unset protection, making it eligible for termination.
Type: Boolean
Required: Yes

 ** [tasks](#API_UpdateTaskProtection_RequestSyntax) **   <a name="ECS-UpdateTaskProtection-request-tasks"></a>
A list of up to 10 task IDs or full ARN entries.
Type: Array of strings
Required: Yes

## Response Syntax
<a name="API_UpdateTaskProtection_ResponseSyntax"></a>

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
<a name="API_UpdateTaskProtection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [failures](#API_UpdateTaskProtection_ResponseSyntax) **   <a name="ECS-UpdateTaskProtection-response-failures"></a>
Any failures associated with the call.
Type: Array of [Failure](API_Failure.md) objects

 ** [protectedTasks](#API_UpdateTaskProtection_ResponseSyntax) **   <a name="ECS-UpdateTaskProtection-response-protectedTasks"></a>
A list of tasks with the following information.
+  `taskArn`: The task ARN.
+  `protectionEnabled`: The protection status of the task. If scale-in protection is turned on for a task, the value is `true`. Otherwise, it is `false`.
+  `expirationDate`: The epoch time when protection for the task will expire.
Type: Array of [ProtectedTask](API_ProtectedTask.md) objects

## Errors
<a name="API_UpdateTaskProtection_Errors"></a>

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
<a name="API_UpdateTaskProtection_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to create them manually. When you use the [AWS Command Line Interface](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you, with the access key that you specify when you configure the tools. When you use these tools, you don't have to sign requests yourself.

### Example 1
<a name="API_UpdateTaskProtection_Example_1"></a>

This example request enables scale-in protection for a task for 60 minutes.

#### Sample Request
<a name="API_UpdateTaskProtection_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ecs.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 132
X-Amz-Target: AmazonEC2ContainerServiceV20141113.UpdateTaskProtection
X-Amz-Date: 20221102T184632Z Content-Type:
application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
    "cluster": "test-task-protection",
    "tasks": [
        "b8b1cf532d0e46ba8d44a40d1de16772"
    ],
    "protectionEnabled": true,
    "expiresInMinutes": 60
}
```

#### Sample Response
<a name="API_UpdateTaskProtection_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Wed, 02 Nov 2022 17:56:32 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 180
Connection: keep-alive
x-amzn-RequestId: 123a4b56-7c89-01d2-3ef4-example5678f

{
    "protectedTasks": [
        {
            "taskArn": "arn:aws:ecs:us-west-2:012345678910:task/default/b8b1cf532d0e46ba8d44a40d1de16772",
            "protectionEnabled": true,
            "expirationDate": 1667415392.553
        }
    ],
    "failures": []
}
```

### Example 2
<a name="API_UpdateTaskProtection_Example_2"></a>

This example request enables scale-in protection for a task without specifying the `expiresInMinutes` parameter. By default, the task will be protected from scale-in events for 120 minutes.

#### Sample Request
<a name="API_UpdateTaskProtection_Example_2_Request"></a>

```
POST / HTTP/1.1
Host: ecs.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 132
X-Amz-Target: AmazonEC2ContainerServiceV20141113.UpdateTaskProtection
X-Amz-Date: 20221103T212558Z
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
    "cluster": "test-task-protection",
    "tasks": [
        "b8b1cf532d0e46ba8d44a40d1de16772"
    ],
    "protectionEnabled": true
}
```

#### Sample Response
<a name="API_UpdateTaskProtection_Example_2_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Thu, 03 Nov 2022 21:25:57 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 180
Connection: keep-alive
x-amzn-RequestId: 123a4b56-7c89-01d2-3ef4-example5678f

{
    "protectedTasks": [
        {
            "taskArn": "arn:aws:ecs:us-west-2:012345678910:task/default/b8b1cf532d0e46ba8d44a40d1de16772",
            "protectionEnabled": true,
            "expirationDate": 1667517958.355
        }
    ],
    "failures": []
}
```

### Example 3
<a name="API_UpdateTaskProtection_Example_3"></a>

This example request turns off scale-in protection for a task.

#### Sample Request
<a name="API_UpdateTaskProtection_Example_3_Request"></a>

```
POST / HTTP/1.1
Host: ecs.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length:109
X-Amz-Target: AmazonEC2ContainerServiceV20141113.UpdateTaskProtection
X-Amz-Date: 20221103T213134Z
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
    "cluster": "test-task-protection",
    "tasks": [
        "b8b1cf532d0e46ba8d44a40d1de16772"
    ],
    "protectionEnabled":false
}
```

#### Sample Response
<a name="API_UpdateTaskProtection_Example_3_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Thu, 03 Nov 2022 21:31:34 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 180
Connection: keep-alive
x-amzn-RequestId: 123a4b56-7c89-01d2-3ef4-example5678f

{
    "protectedTasks": [
        {
            "taskArn": "arn:aws:ecs:us-west-2:012345678910:task/default/b8b1cf532d0e46ba8d44a40d1de16772",
            "protectionEnabled": false
        }
    ],
    "failures": []
}
```

## See Also
<a name="API_UpdateTaskProtection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/UpdateTaskProtection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/UpdateTaskProtection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/UpdateTaskProtection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/UpdateTaskProtection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/UpdateTaskProtection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/UpdateTaskProtection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/UpdateTaskProtection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/UpdateTaskProtection)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/UpdateTaskProtection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/UpdateTaskProtection)
