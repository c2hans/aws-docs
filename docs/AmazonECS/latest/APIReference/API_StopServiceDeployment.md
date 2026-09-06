---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_StopServiceDeployment.html
---

# StopServiceDeployment
<a name="API_StopServiceDeployment"></a>

Stops an ongoing service deployment.

The following stop types are avaiable:
+ ROLLBACK - This option rolls back the service deployment to the previous service revision.

  You can use this option even if you didn't configure the service deployment for the rollback option.

For more information, see [Stopping Amazon ECS service deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/stop-service-deployment.html) in the *Amazon Elastic Container Service Developer Guide*.

## Request Syntax
<a name="API_StopServiceDeployment_RequestSyntax"></a>

```
{
   "serviceDeploymentArn": "{{string}}",
   "stopType": "{{string}}"
}
```

## Request Parameters
<a name="API_StopServiceDeployment_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [serviceDeploymentArn](#API_StopServiceDeployment_RequestSyntax) **   <a name="ECS-StopServiceDeployment-request-serviceDeploymentArn"></a>
The ARN of the service deployment that you want to stop.
Type: String
Required: Yes

 ** [stopType](#API_StopServiceDeployment_RequestSyntax) **   <a name="ECS-StopServiceDeployment-request-stopType"></a>
How you want Amazon ECS to stop the service.
The valid values are `ROLLBACK`.
Type: String
Valid Values: `ABORT | ROLLBACK`
Required: No

## Response Syntax
<a name="API_StopServiceDeployment_ResponseSyntax"></a>

```
{
   "serviceDeploymentArn": "string"
}
```

## Response Elements
<a name="API_StopServiceDeployment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [serviceDeploymentArn](#API_StopServiceDeployment_ResponseSyntax) **   <a name="ECS-StopServiceDeployment-response-serviceDeploymentArn"></a>
The ARN of the stopped service deployment.
Type: String

## Errors
<a name="API_StopServiceDeployment_Errors"></a>

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

 ** ConflictException **
The request could not be processed because of conflict in the current state of the resource.
 ** message **
 Message that describes the cause of the exception.
 ** resourceIds **
The existing task ARNs which are already associated with the `clientToken`.
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
<a name="API_StopServiceDeployment_Examples"></a>

### Example
<a name="API_StopServiceDeployment_Example_1"></a>

This example request stops the service deployment with the ARN of `arn:aws:ecs:us-east-1:123456789012:service-deployment/MyCluster/MyService/r9i43YFjvgF_xlg7m2eJ1`using the `ROLLBACK` stop type.

#### Sample Request
<a name="API_StopServiceDeployment_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ecs.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 55
X-Amz-Target: AmazonEC2ContainerServiceV20141113.StopServiceDeployment
X-Amz-Date: 20250407T133521Z
User-Agent: aws-cli/2.26 Python/3.12.6 Darwin/14.3.0
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{

  "serviceDeploymentArn": "arn:aws:ecs:us-east-1:123456789012:service-deployment/MyCluster/MyService/r9i43YFjvgF_xlg7m2eJ1",
  "stopType": "ROLLBACK"
}
```

#### Sample Response
<a name="API_StopServiceDeployment_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Mon Apr 7, 2025 18:50:14 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 220
Connection: keep-alive
RequestId: 360c5551-123e-4e74-9914-7582d3a28807
{
     "serviceDeploymentArn": "arn:aws:ecs:us-east-1:123456789012:service-deployment/MyCluster/MyService/r9i43YFjvgF_xlg7m2eJ1",
}
}
```

## See Also
<a name="API_StopServiceDeployment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/StopServiceDeployment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/StopServiceDeployment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/StopServiceDeployment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/StopServiceDeployment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/StopServiceDeployment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/StopServiceDeployment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/StopServiceDeployment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/StopServiceDeployment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/StopServiceDeployment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/StopServiceDeployment)
