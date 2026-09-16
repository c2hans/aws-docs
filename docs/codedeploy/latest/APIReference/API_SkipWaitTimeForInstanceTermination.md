---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_SkipWaitTimeForInstanceTermination.html
---

# SkipWaitTimeForInstanceTermination
<a name="API_SkipWaitTimeForInstanceTermination"></a>

In a blue/green deployment, overrides any specified wait time and starts terminating instances immediately after the traffic routing is complete.

## Request Syntax
<a name="API_SkipWaitTimeForInstanceTermination_RequestSyntax"></a>

```
{
   "deploymentId": "{{string}}"
}
```

## Request Parameters
<a name="API_SkipWaitTimeForInstanceTermination_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [deploymentId](#API_SkipWaitTimeForInstanceTermination_RequestSyntax) **   <a name="CodeDeploy-SkipWaitTimeForInstanceTermination-request-deploymentId"></a>
 The unique ID of a blue/green deployment for which you want to skip the instance termination wait time.
Type: String
Required: No

## Response Elements
<a name="API_SkipWaitTimeForInstanceTermination_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_SkipWaitTimeForInstanceTermination_Errors"></a>

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

 ** DeploymentNotStartedException **
The specified deployment has not started.
HTTP Status Code: 400

 ** InvalidDeploymentIdException **
At least one of the deployment IDs was specified in an invalid format.
HTTP Status Code: 400

 ** UnsupportedActionForDeploymentTypeException **
A call was submitted that is not supported for the specified deployment type.
HTTP Status Code: 400

## Examples
<a name="API_SkipWaitTimeForInstanceTermination_Examples"></a>

### Example
<a name="API_SkipWaitTimeForInstanceTermination_Example_1"></a>

This example illustrates one usage of SkipWaitTimeForInstanceTermination.

#### Sample Request
<a name="API_SkipWaitTimeForInstanceTermination_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codedeploy.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 31
X-Amz-Target: CodeDeploy_20141006.SkipWaitTimeForInstanceTermination
X-Amz-Date: 20170412T203610Z
User-Agent: aws-cli/1.11.76 Python/2.7.9 Windows/8 botocore/1.5.39
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20160707/us-east-1/codedeploy/aws4_request,
	SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{"deploymentId": "d-UBCT41FSL"}
```

## See Also
<a name="API_SkipWaitTimeForInstanceTermination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codedeploy-2014-10-06/SkipWaitTimeForInstanceTermination)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codedeploy-2014-10-06/SkipWaitTimeForInstanceTermination)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/SkipWaitTimeForInstanceTermination)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codedeploy-2014-10-06/SkipWaitTimeForInstanceTermination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/SkipWaitTimeForInstanceTermination)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codedeploy-2014-10-06/SkipWaitTimeForInstanceTermination)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codedeploy-2014-10-06/SkipWaitTimeForInstanceTermination)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codedeploy-2014-10-06/SkipWaitTimeForInstanceTermination)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codedeploy-2014-10-06/SkipWaitTimeForInstanceTermination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/SkipWaitTimeForInstanceTermination)
