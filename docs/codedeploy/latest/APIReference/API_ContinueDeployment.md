---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ContinueDeployment.html
---

# ContinueDeployment
<a name="API_ContinueDeployment"></a>

For a blue/green deployment, starts the process of rerouting traffic from instances in the original environment to instances in the replacement environment without waiting for a specified wait time to elapse. (Traffic rerouting, which is achieved by registering instances in the replacement environment with the load balancer, can start as soon as all instances have a status of Ready.)

## Request Syntax
<a name="API_ContinueDeployment_RequestSyntax"></a>

```
{
   "deploymentId": "{{string}}",
   "deploymentWaitType": "{{string}}"
}
```

## Request Parameters
<a name="API_ContinueDeployment_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [deploymentId](#API_ContinueDeployment_RequestSyntax) **   <a name="CodeDeploy-ContinueDeployment-request-deploymentId"></a>
 The unique ID of a blue/green deployment for which you want to start rerouting traffic to the replacement environment.
Type: String
Required: No

 ** [deploymentWaitType](#API_ContinueDeployment_RequestSyntax) **   <a name="CodeDeploy-ContinueDeployment-request-deploymentWaitType"></a>
 The status of the deployment's waiting period. `READY_WAIT` indicates that the deployment is ready to start shifting traffic. `TERMINATION_WAIT` indicates that the traffic is shifted, but the original target is not terminated.
Type: String
Valid Values: `READY_WAIT | TERMINATION_WAIT`
Required: No

## Response Elements
<a name="API_ContinueDeployment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_ContinueDeployment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DeploymentAlreadyCompletedException **
The deployment is already complete.
HTTP Status Code: 400

 ** DeploymentDoesNotExistException **
The deployment with the user or AWS account does not exist.
HTTP Status Code: 400

 ** DeploymentIdRequiredException **
At least one deployment ID must be specified.
HTTP Status Code: 400

 ** DeploymentIsNotInReadyStateException **
The deployment does not have a status of Ready and can't continue yet.
HTTP Status Code: 400

 ** InvalidDeploymentIdException **
At least one of the deployment IDs was specified in an invalid format.
HTTP Status Code: 400

 ** InvalidDeploymentStatusException **
The specified deployment status doesn't exist or cannot be determined.
HTTP Status Code: 400

 ** InvalidDeploymentWaitTypeException **
 The wait type is invalid.
HTTP Status Code: 400

 ** UnsupportedActionForDeploymentTypeException **
A call was submitted that is not supported for the specified deployment type.
HTTP Status Code: 400

## Examples
<a name="API_ContinueDeployment_Examples"></a>

### Example
<a name="API_ContinueDeployment_Example_1"></a>

This example illustrates one usage of ContinueDeployment.

#### Sample Request
<a name="API_ContinueDeployment_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codedeploy.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 31
X-Amz-Target: CodeDeploy_20141006.ContinueDeployment
X-Amz-Date: 20170412T195720Z
User-Agent: aws-cli/1.11.76 Python/2.7.9 Windows/8 botocore/1.5.39
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20160707/us-east-1/codedeploy/aws4_request,
	SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{"deploymentId": "d-7S8EXAMPL"}
```

## See Also
<a name="API_ContinueDeployment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codedeploy-2014-10-06/ContinueDeployment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codedeploy-2014-10-06/ContinueDeployment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/ContinueDeployment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codedeploy-2014-10-06/ContinueDeployment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/ContinueDeployment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codedeploy-2014-10-06/ContinueDeployment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codedeploy-2014-10-06/ContinueDeployment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codedeploy-2014-10-06/ContinueDeployment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codedeploy-2014-10-06/ContinueDeployment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/ContinueDeployment)
