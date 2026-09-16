---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_GetDeploymentInstance.html
---

# GetDeploymentInstance
<a name="API_GetDeploymentInstance"></a>

Gets information about an instance as part of a deployment.

## Request Syntax
<a name="API_GetDeploymentInstance_RequestSyntax"></a>

```
{
   "deploymentId": "{{string}}",
   "instanceId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetDeploymentInstance_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [deploymentId](#API_GetDeploymentInstance_RequestSyntax) **   <a name="CodeDeploy-GetDeploymentInstance-request-deploymentId"></a>
 The unique ID of a deployment.
Type: String
Required: Yes

 ** [instanceId](#API_GetDeploymentInstance_RequestSyntax) **   <a name="CodeDeploy-GetDeploymentInstance-request-instanceId"></a>
 The unique ID of an instance in the deployment group.
Type: String
Required: Yes

## Response Syntax
<a name="API_GetDeploymentInstance_ResponseSyntax"></a>

```
{
   "instanceSummary": {
      "deploymentId": "string",
      "instanceId": "string",
      "instanceType": "string",
      "lastUpdatedAt": number,
      "lifecycleEvents": [
         {
            "diagnostics": {
               "errorCode": "string",
               "logTail": "string",
               "message": "string",
               "scriptName": "string"
            },
            "endTime": number,
            "lifecycleEventName": "string",
            "startTime": number,
            "status": "string"
         }
      ],
      "status": "string"
   }
}
```

## Response Elements
<a name="API_GetDeploymentInstance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [instanceSummary](#API_GetDeploymentInstance_ResponseSyntax) **   <a name="CodeDeploy-GetDeploymentInstance-response-instanceSummary"></a>
 *This parameter has been deprecated.*
 Information about the instance.
Type: [InstanceSummary](API_InstanceSummary.md) object

## Errors
<a name="API_GetDeploymentInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DeploymentDoesNotExistException **
The deployment with the user or AWS account does not exist.
HTTP Status Code: 400

 ** DeploymentIdRequiredException **
At least one deployment ID must be specified.
HTTP Status Code: 400

 ** InstanceDoesNotExistException **
 *This error has been deprecated.*
The specified instance does not exist in the deployment group.
HTTP Status Code: 400

 ** InstanceIdRequiredException **
 *This error has been deprecated.*
The instance ID was not specified.
HTTP Status Code: 400

 ** InvalidComputePlatformException **
The computePlatform is invalid. The computePlatform should be `Lambda`, `Server`, or `ECS`.
HTTP Status Code: 400

 ** InvalidDeploymentIdException **
At least one of the deployment IDs was specified in an invalid format.
HTTP Status Code: 400

 ** InvalidInstanceNameException **
The on-premises instance name was specified in an invalid format.
HTTP Status Code: 400

## Examples
<a name="API_GetDeploymentInstance_Examples"></a>

### Example
<a name="API_GetDeploymentInstance_Example_1"></a>

This example illustrates one usage of GetDeploymentInstance.

#### Sample Request
<a name="API_GetDeploymentInstance_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codedeploy.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 59
X-Amz-Target: CodeDeploy_20141006.GetDeploymentInstance
X-Amz-Date: 20160707T020504Z
User-Agent: aws-cli/1.10.6 Python/2.7.9 Windows/7 botocore/1.3.28
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20160707/us-east-1/codedeploy/aws4_request,
	SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
    "instanceId": "i-496636f700EXAMPLE",
    "deploymentId": "d-7539MBT7C"
}
```

#### Sample Response
<a name="API_GetDeploymentInstance_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: caf06837-88e1-11e5-b0f5-a331fa97e4b5
Content-Type: application/x-amz-json-1.1
Content-Length: 1628

{
    "instanceSummary": {
        "deploymentId": "d-75I7MBT7C",
        "instanceId": "arn:aws:ec2:us-east-1:444455556666:instance/i-496589f700EXAMPLE",
        "lastUpdatedAt": 1446744207.564,
        "lifecycleEvents": [
            {
                "diagnostics": {
                    "errorCode": "Success",
                    "logTail": "",
                    "message": "Succeeded",
                    "scriptName": ""
                },
                "endTime": 1446744188.711,
                "lifecycleEventName": "ApplicationStop",
                "startTime": 1446744188.595,
                "status": "Succeeded"
            },
            {
                "diagnostics": {
                    "errorCode": "Success",
                    "logTail": "",
                    "message": "Succeeded",
                    "scriptName": ""
                },
                "endTime": 1446744190.402,
                "lifecycleEventName": "DownloadBundle",
                "startTime": 1446744189.827,
                "status": "Succeeded"
            },
            {
                "diagnostics": {
                    "errorCode": "Success",
                    "logTail": "",
                    "message": "Succeeded",
                    "scriptName": ""
                },
                "endTime": 1446744196.971,
                "lifecycleEventName": "BeforeInstall",
                "startTime": 1446744192.922,
                "status": "Succeeded"
            },
            {
                "diagnostics": {
                    "errorCode": "Success",
                    "logTail": "",
                    "message": "Succeeded",
                    "scriptName": ""
                },
                "endTime": 1446744198.23,
                "lifecycleEventName": "Install",
                "startTime": 1446744198.084,
                "status": "Succeeded"
            },
            {
                "diagnostics": {
                    "errorCode": "Success",
                    "logTail": "",
                    "message": "Succeeded",
                    "scriptName": ""
                },
                "endTime": 1446744200.299,
                "lifecycleEventName": "AfterInstall",
                "startTime": 1446744200.185,
                "status": "Succeeded"
            },
            {
                "diagnostics": {
                    "errorCode": "Success",
                    "logTail": "",
                    "message": "Succeeded",
                    "scriptName": ""
                },
                "endTime": 1446744203.12,
                "lifecycleEventName": "ApplicationStart",
                "startTime": 1446744202.983,
                "status": "Succeeded"
            },
            {
                "diagnostics": {
                    "errorCode": "Success",
                    "logTail": "",
                    "message": "Succeeded",
                    "scriptName": ""
                },
                "endTime": 1446744204.558,
                "lifecycleEventName": "ValidateService",
                "startTime": 1446744204.438,
                "status": "Succeeded"
            }
        ],
        "status": "Succeeded"
    }
}
```

## See Also
<a name="API_GetDeploymentInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codedeploy-2014-10-06/GetDeploymentInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codedeploy-2014-10-06/GetDeploymentInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/GetDeploymentInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codedeploy-2014-10-06/GetDeploymentInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/GetDeploymentInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codedeploy-2014-10-06/GetDeploymentInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codedeploy-2014-10-06/GetDeploymentInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codedeploy-2014-10-06/GetDeploymentInstance)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codedeploy-2014-10-06/GetDeploymentInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/GetDeploymentInstance)
