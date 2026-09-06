---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_StopDeployment.html
---

# StopDeployment
<a name="API_StopDeployment"></a>

Attempts to stop an ongoing deployment.

## Request Syntax
<a name="API_StopDeployment_RequestSyntax"></a>

```
{
   "autoRollbackEnabled": {{boolean}},
   "deploymentId": "{{string}}"
}
```

## Request Parameters
<a name="API_StopDeployment_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [autoRollbackEnabled](#API_StopDeployment_RequestSyntax) **   <a name="CodeDeploy-StopDeployment-request-autoRollbackEnabled"></a>
 Indicates, when a deployment is stopped, whether instances that have been updated should be rolled back to the previous version of the application revision.
Type: Boolean
Required: No

 ** [deploymentId](#API_StopDeployment_RequestSyntax) **   <a name="CodeDeploy-StopDeployment-request-deploymentId"></a>
 The unique ID of a deployment.
Type: String
Required: Yes

## Response Syntax
<a name="API_StopDeployment_ResponseSyntax"></a>

```
{
   "status": "string",
   "statusMessage": "string"
}
```

## Response Elements
<a name="API_StopDeployment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [status](#API_StopDeployment_ResponseSyntax) **   <a name="CodeDeploy-StopDeployment-response-status"></a>
The status of the stop deployment operation:
+ Pending: The stop operation is pending.
+ Succeeded: The stop operation was successful.
Type: String
Valid Values: `Pending | Succeeded | Forced`

 ** [statusMessage](#API_StopDeployment_ResponseSyntax) **   <a name="CodeDeploy-StopDeployment-response-statusMessage"></a>
An accompanying status message.
Type: String

## Errors
<a name="API_StopDeployment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DeploymentAlreadyCompletedException **
The deployment is already complete.
HTTP Status Code: 400

 ** DeploymentDoesNotExistException **
The deployment with the user or AWS account does not exist.
HTTP Status Code: 400

 ** DeploymentGroupDoesNotExistException **
The named deployment group with the user or AWS account does not exist.
HTTP Status Code: 400

 ** DeploymentIdRequiredException **
At least one deployment ID must be specified.
HTTP Status Code: 400

 ** InvalidDeploymentIdException **
At least one of the deployment IDs was specified in an invalid format.
HTTP Status Code: 400

 ** UnsupportedActionForDeploymentTypeException **
A call was submitted that is not supported for the specified deployment type.
HTTP Status Code: 400

## Examples
<a name="API_StopDeployment_Examples"></a>

### Example
<a name="API_StopDeployment_Example_1"></a>

This example illustrates one usage of StopDeployment.

#### Sample Request
<a name="API_StopDeployment_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codedeploy.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 31
X-Amz-Target: CodeDeploy_20141006.StopDeployment
X-Amz-Date: 20160707T025157Z
User-Agent: aws-cli/1.10.6 Python/2.7.9 Windows/7 botocore/1.3.28
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20160707/us-east-1/codedeploy/aws4_request,
	SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
    "deploymentId": "d-LGUMS25CC"
}
```

#### Sample Response
<a name="API_StopDeployment_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 57a24279-88e8-11e5-a087-ab26ee53e16e
Content-Type: application/x-amz-json-1.1
Content-Length: 114

{
    "status": "Pending",
    "statusMessage": "Stopping Pending. Stopping to schedule commands in the deployment instances"
}
```

## See Also
<a name="API_StopDeployment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codedeploy-2014-10-06/StopDeployment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codedeploy-2014-10-06/StopDeployment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/StopDeployment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codedeploy-2014-10-06/StopDeployment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/StopDeployment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codedeploy-2014-10-06/StopDeployment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codedeploy-2014-10-06/StopDeployment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codedeploy-2014-10-06/StopDeployment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codedeploy-2014-10-06/StopDeployment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/StopDeployment)
