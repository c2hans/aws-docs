---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContinueServiceDeployment.html
---

# ContinueServiceDeployment
<a name="API_ContinueServiceDeployment"></a>

Continues or rolls back an Amazon ECS service deployment that is paused at a lifecycle hook.

When a service deployment reaches a lifecycle stage that has a `PAUSE` hook configured, the deployment pauses and waits for an explicit action. Use this API to either continue the deployment to the next stage or roll back to the previous service revision.

To find the `hookId` of the paused hook, call [DescribeServiceDeployments](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeServiceDeployments.html) and inspect the `lifecycleHookDetails` field.

For more information, see [Continuing Amazon ECS service deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/continue-service-deployment.html) in the *Amazon Elastic Container Service Developer Guide*.

## Request Syntax
<a name="API_ContinueServiceDeployment_RequestSyntax"></a>

```
{
   "action": "{{string}}",
   "hookId": "{{string}}",
   "serviceDeploymentArn": "{{string}}"
}
```

## Request Parameters
<a name="API_ContinueServiceDeployment_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [action](#API_ContinueServiceDeployment_RequestSyntax) **   <a name="ECS-ContinueServiceDeployment-request-action"></a>
The action to take on the paused lifecycle hook. Valid values are:
+  `CONTINUE` - Proceeds the deployment to the next lifecycle stage.
+  `ROLLBACK` - Rolls back the deployment to the previous service revision.
If no value is specified, the default action is `CONTINUE`.
Type: String
Valid Values: `ROLLBACK | CONTINUE`
Required: No

 ** [hookId](#API_ContinueServiceDeployment_RequestSyntax) **   <a name="ECS-ContinueServiceDeployment-request-hookId"></a>
The ID of the paused lifecycle hook to act on. You can find the `hookId` by calling [DescribeServiceDeployments](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeServiceDeployments.html) and inspecting the `lifecycleHookDetails` field of the service deployment.
Type: String
Required: Yes

 ** [serviceDeploymentArn](#API_ContinueServiceDeployment_RequestSyntax) **   <a name="ECS-ContinueServiceDeployment-request-serviceDeploymentArn"></a>
The ARN of the service deployment to continue or roll back.
Type: String
Required: Yes

## Response Syntax
<a name="API_ContinueServiceDeployment_ResponseSyntax"></a>

```
{
   "serviceDeploymentArn": "string"
}
```

## Response Elements
<a name="API_ContinueServiceDeployment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [serviceDeploymentArn](#API_ContinueServiceDeployment_ResponseSyntax) **   <a name="ECS-ContinueServiceDeployment-response-serviceDeploymentArn"></a>
The ARN of the service deployment that was continued or rolled back.
Type: String

## Errors
<a name="API_ContinueServiceDeployment_Errors"></a>

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

 ** ServiceDeploymentNotFoundException **
The service deploy ARN that you specified in the `ContinueServiceDeployment` doesn't exist. You can use `ListServiceDeployments` to retrieve the service deployment ARNs.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** UnsupportedFeatureException **
The specified task isn't supported in this Region.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

## Examples
<a name="API_ContinueServiceDeployment_Examples"></a>

### Example 1
<a name="API_ContinueServiceDeployment_Example_1"></a>

This example continues a paused service deployment, allowing it to proceed to the next lifecycle stage.

#### Sample Request
<a name="API_ContinueServiceDeployment_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ecs.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 180
X-Amz-Target: AmazonEC2ContainerServiceV20141113.ContinueServiceDeployment
X-Amz-Date: 20260506T160000Z
User-Agent: aws-cli/2.26 Python/3.12.6 Darwin/14.3.0
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
  "serviceDeploymentArn": "arn:aws:ecs:us-east-1:123456789012:service-deployment/MyCluster/MyService/abc123DEF456",
  "hookId": "ecs-pause-Xk7rT2mP9sLwQn4vB8fYd3hJ6gA1cE5iO0uR_ZpWq",
  "action": "CONTINUE"
}
```

#### Sample Response
<a name="API_ContinueServiceDeployment_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Tue May 6, 2026 16:00:00 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 130
Connection: keep-alive
RequestId: 360c5551-123e-4e74-9914-7582d3a28807

{
    "serviceDeploymentArn": "arn:aws:ecs:us-east-1:123456789012:service-deployment/MyCluster/MyService/abc123DEF456"
}
```

### Example 2
<a name="API_ContinueServiceDeployment_Example_2"></a>

This example rolls back a paused service deployment to the previous service revision.

#### Sample Request
<a name="API_ContinueServiceDeployment_Example_2_Request"></a>

```
POST / HTTP/1.1
Host: ecs.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 180
X-Amz-Target: AmazonEC2ContainerServiceV20141113.ContinueServiceDeployment
X-Amz-Date: 20260506T160500Z
User-Agent: aws-cli/2.26 Python/3.12.6 Darwin/14.3.0
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
  "serviceDeploymentArn": "arn:aws:ecs:us-east-1:123456789012:service-deployment/MyCluster/MyService/abc123DEF456",
  "hookId": "ecs-pause-Xk7rT2mP9sLwQn4vB8fYd3hJ6gA1cE5iO0uR_ZpWq",
  "action": "ROLLBACK"
}
```

#### Sample Response
<a name="API_ContinueServiceDeployment_Example_2_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Tue May 6, 2026 16:05:00 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 130
Connection: keep-alive
RequestId: 470d6662-234f-5e85-0025-fg2345678901

{
    "serviceDeploymentArn": "arn:aws:ecs:us-east-1:123456789012:service-deployment/MyCluster/MyService/abc123DEF456"
}
```

## See Also
<a name="API_ContinueServiceDeployment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/ContinueServiceDeployment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/ContinueServiceDeployment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ContinueServiceDeployment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/ContinueServiceDeployment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ContinueServiceDeployment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/ContinueServiceDeployment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/ContinueServiceDeployment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/ContinueServiceDeployment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/ContinueServiceDeployment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ContinueServiceDeployment)
