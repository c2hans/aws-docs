---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_BatchGetDeploymentInstances.html
---

# BatchGetDeploymentInstances
<a name="API_BatchGetDeploymentInstances"></a>

**Note**
 This method works, but is deprecated. Use `BatchGetDeploymentTargets` instead.

 Returns an array of one or more instances associated with a deployment. This method works with EC2/On-premises and AWS Lambda compute platforms. The newer `BatchGetDeploymentTargets` works with all compute platforms. The maximum number of instances that can be returned is 25.

## Request Syntax
<a name="API_BatchGetDeploymentInstances_RequestSyntax"></a>

```
{
   "deploymentId": "{{string}}",
   "instanceIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_BatchGetDeploymentInstances_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [deploymentId](#API_BatchGetDeploymentInstances_RequestSyntax) **   <a name="CodeDeploy-BatchGetDeploymentInstances-request-deploymentId"></a>
 The unique ID of a deployment.
Type: String
Required: Yes

 ** [instanceIds](#API_BatchGetDeploymentInstances_RequestSyntax) **   <a name="CodeDeploy-BatchGetDeploymentInstances-request-instanceIds"></a>
The unique IDs of instances used in the deployment. The maximum number of instance IDs you can specify is 25.
Type: Array of strings
Required: Yes

## Response Syntax
<a name="API_BatchGetDeploymentInstances_ResponseSyntax"></a>

```
{
   "errorMessage": "string",
   "instancesSummary": [
      {
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
   ]
}
```

## Response Elements
<a name="API_BatchGetDeploymentInstances_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errorMessage](#API_BatchGetDeploymentInstances_ResponseSyntax) **   <a name="CodeDeploy-BatchGetDeploymentInstances-response-errorMessage"></a>
Information about errors that might have occurred during the API call.
Type: String

 ** [instancesSummary](#API_BatchGetDeploymentInstances_ResponseSyntax) **   <a name="CodeDeploy-BatchGetDeploymentInstances-response-instancesSummary"></a>
Information about the instance.
Type: Array of [InstanceSummary](API_InstanceSummary.md) objects

## Errors
<a name="API_BatchGetDeploymentInstances_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BatchLimitExceededException **
The maximum number of names or IDs allowed for this request (100) was exceeded.
HTTP Status Code: 400

 ** DeploymentDoesNotExistException **
The deployment with the user or AWS account does not exist.
HTTP Status Code: 400

 ** DeploymentIdRequiredException **
At least one deployment ID must be specified.
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
<a name="API_BatchGetDeploymentInstances_Examples"></a>

### Example
<a name="API_BatchGetDeploymentInstances_Example_1"></a>

This example illustrates one usage of BatchGetDeploymentInstances.

#### Sample Request
<a name="API_BatchGetDeploymentInstances_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codedeploy.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 90
X-Amz-Target: CodeDeploy_20141006.BatchGetDeploymentInstances
X-Amz-Date: 20160707T175340Z
User-Agent: aws-cli/1.10.6 Python/2.7.9 Windows/7 botocore/1.3.28
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20160707/us-east-1/codedeploy/aws4_request,
SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
    "deploymentId": "d-DXT57CS2G",
    "instanceIds": [
        "i-2b4a36ad00EXAMPLE",
        "i-384a57d300EXAMPLE",
        "i-623g53b300EXAMPLE"
    ]
}
```

#### Sample Response
<a name="API_BatchGetDeploymentInstances_Example_1_Response"></a>

```
{
    "errorMessage": "",
    "instancesSummary": [
        {
            "deploymentId": "d-DXT57CS2G",
            "instanceId": "arn:aws:ec2:us-east-1:803981987763:instance/i-623g53b300EXAMPLE",
            "lastUpdatedAt": 1455988938.931,
            "lifecycleEvents": [
                {
                    "diagnostics": {
                        "errorCode": "Success",
                        "logTail": "",
                        "message": "Succeeded",
                        "scriptName": ""
                    },
                    "endTime": 1455988923.454,
                    "lifecycleEventName": "ApplicationStop",
                    "startTime": 1455988923.284,
                    "status": "Succeeded"
                },
                {
                    "diagnostics": {
                        "errorCode": "Success",
                        "logTail": "",
                        "message": "Succeeded",
                        "scriptName": ""
                    },
                    "endTime": 1455988925.903,
                    "lifecycleEventName": "DownloadBundle",
                    "startTime": 1455988925.574,
                    "status": "Succeeded"
                },
                {
                    "diagnostics": {
                        "errorCode": "Success",
                        "logTail": "",
                        "message": "Succeeded",
                        "scriptName": ""
                    },
                    "endTime": 1455988927.731,
                    "lifecycleEventName": "BeforeInstall",
                    "startTime": 1455988927.011,
                    "status": "Succeeded"
                },
                {
                    "diagnostics": {
                        "errorCode": "Success",
                        "logTail": "",
                        "message": "Succeeded",
                        "scriptName": ""
                    },
                    "endTime": 1455988931.435,
                    "lifecycleEventName": "Install",
                    "startTime": 1455988931.272,
                    "status": "Succeeded"
                },
                {
                    "diagnostics": {
                        "errorCode": "Success",
                        "logTail": "",
                        "message": "Succeeded",
                        "scriptName": ""
                    },
                    "endTime": 1455988933.129,
                    "lifecycleEventName": "AfterInstall",
                    "startTime": 1455988932.951,
                    "status": "Succeeded"
                },
                {
                    "diagnostics": {
                        "errorCode": "Success",
                        "logTail": "",
                        "message": "Succeeded",
                        "scriptName": ""
                    },
                    "endTime": 1455988935.599,
                    "lifecycleEventName": "ApplicationStart",
                    "startTime": 1455988935.459,
                    "status": "Succeeded"
                },
                {
                    "diagnostics": {
                        "errorCode": "Success",
                        "logTail": "",
                        "message": "Succeeded",
                        "scriptName": ""
                    },
                    "endTime": 1455988937.286,
                    "lifecycleEventName": "ValidateService",
                    "startTime": 1455988937.166,
                    "status": "Succeeded"
                }
            ],
            "status": "Succeeded"
        },
        {
            "deploymentId": "d-DXT57CS2G",
            "instanceId": "arn:aws:ec2:us-east-1:803981987763:instance/i-384a57d300EXAMPLE",
            "lastUpdatedAt": 1455988921.266,
            "lifecycleEvents": [
                {
                    "diagnostics": {
                        "errorCode": "Success",
                        "logTail": "",
                        "message": "Succeeded",
                        "scriptName": ""
                    },
                    "endTime": 1455988908.166,
                    "lifecycleEventName": "ApplicationStop",
                    "startTime": 1455988908.002,
                    "status": "Succeeded"
                },
                {
                    "diagnostics": {
                        "errorCode": "Success",
                        "logTail": "",
                        "message": "Succeeded",
                        "scriptName": ""
                    },
                    "endTime": 1455988910.007,
                    "lifecycleEventName": "DownloadBundle",
                    "startTime": 1455988909.817,
                    "status": "Succeeded"
                },
                {
                    "diagnostics": {
                        "errorCode": "Success",
                        "logTail": "",
                        "message": "Succeeded",
                        "scriptName": ""
                    },
                    "endTime": 1455988912.501,
                    "lifecycleEventName": "BeforeInstall",
                    "startTime": 1455988911.823,
                    "status": "Succeeded"
                },
                {
                    "diagnostics": {
                        "errorCode": "Success",
                        "logTail": "",
                        "message": "Succeeded",
                        "scriptName": ""
                    },
                    "endTime": 1455988914.18,
                    "lifecycleEventName": "Install",
                    "startTime": 1455988914.068,
                    "status": "Succeeded"
                },
                {
                    "diagnostics": {
                        "errorCode": "Success",
                        "logTail": "",
                        "message": "Succeeded",
                        "scriptName": ""
                    },
                    "endTime": 1455988916.288,
                    "lifecycleEventName": "AfterInstall",
                    "startTime": 1455988916.108,
                    "status": "Succeeded"
                },
                {
                    "diagnostics": {
                        "errorCode": "Success",
                        "logTail": "",
                        "message": "Succeeded",
                        "scriptName": ""
                    },
                    "endTime": 1455988917.63,
                    "lifecycleEventName": "ApplicationStart",
                    "startTime": 1455988917.513,
                    "status": "Succeeded"
                },
                {
                    "diagnostics": {
                        "errorCode": "Success",
                        "logTail": "",
                        "message": "Succeeded",
                        "scriptName": ""
                    },
                    "endTime": 1455988919.616,
                    "lifecycleEventName": "ValidateService",
                    "startTime": 1455988919.489,
                    "status": "Succeeded"
                }
            ],
            "status": "Succeeded"
        },
        {
            "deploymentId": "d-DXT57CS2G",
            "instanceId": "arn:aws:ec2:us-east-1:803981987763:instance/i-2b4a36ad00EXAMPLE",
            "lastUpdatedAt": 1455988905.795,
            "lifecycleEvents": [
                {
                    "diagnostics": {
                        "errorCode": "Success",
                        "logTail": "",
                        "message": "Succeeded",
                        "scriptName": ""
                    },
                    "endTime": 1455988835.41,
                    "lifecycleEventName": "ApplicationStop",
                    "startTime": 1455988835.243,
                    "status": "Succeeded"
                },
                {
                    "diagnostics": {
                        "errorCode": "Success",
                        "logTail": "",
                        "message": "Succeeded",
                        "scriptName": ""
                    },
                    "endTime": 1455988843.137,
                    "lifecycleEventName": "DownloadBundle",
                    "startTime": 1455988842.349,
                    "status": "Succeeded"
                },
                {
                    "diagnostics": {
                        "errorCode": "Success",
                        "logTail": "",
                        "message": "Succeeded",
                        "scriptName": ""
                    },
                    "endTime": 1455988845.424,
                    "lifecycleEventName": "BeforeInstall",
                    "startTime": 1455988844.707,
                    "status": "Succeeded"
                },
                {
                    "diagnostics": {
                        "errorCode": "Success",
                        "logTail": "",
                        "message": "Succeeded",
                        "scriptName": ""
                    },
                    "endTime": 1455988853.216,
                    "lifecycleEventName": "Install",
                    "startTime": 1455988853.096,
                    "status": "Succeeded"
                },
                {
                    "diagnostics": {
                        "errorCode": "Success",
                        "logTail": "",
                        "message": "Succeeded",
                        "scriptName": ""
                    },
                    "endTime": 1455988858.017,
                    "lifecycleEventName": "AfterInstall",
                    "startTime": 1455988857.916,
                    "status": "Succeeded"
                },
                {
                    "diagnostics": {
                        "errorCode": "Success",
                        "logTail": "",
                        "message": "Succeeded",
                        "scriptName": ""
                    },
                    "endTime": 1455988902.714,
                    "lifecycleEventName": "ApplicationStart",
                    "startTime": 1455988902.56,
                    "status": "Succeeded"
                },
                {
                    "diagnostics": {
                        "errorCode": "Success",
                        "logTail": "",
                        "message": "Succeeded",
                        "scriptName": ""
                    },
                    "endTime": 1455988904.577,
                    "lifecycleEventName": "ValidateService",
                    "startTime": 1455988904.38,
                    "status": "Succeeded"
                }
            ],
            "status": "Succeeded"
        }
    ]
}
```

## See Also
<a name="API_BatchGetDeploymentInstances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codedeploy-2014-10-06/BatchGetDeploymentInstances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codedeploy-2014-10-06/BatchGetDeploymentInstances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/BatchGetDeploymentInstances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codedeploy-2014-10-06/BatchGetDeploymentInstances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/BatchGetDeploymentInstances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codedeploy-2014-10-06/BatchGetDeploymentInstances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codedeploy-2014-10-06/BatchGetDeploymentInstances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codedeploy-2014-10-06/BatchGetDeploymentInstances)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codedeploy-2014-10-06/BatchGetDeploymentInstances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/BatchGetDeploymentInstances)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
