---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_GetDeploymentTarget.html
---

# GetDeploymentTarget
<a name="API_GetDeploymentTarget"></a>

 Returns information about a deployment target.

## Request Syntax
<a name="API_GetDeploymentTarget_RequestSyntax"></a>

```
{
   "deploymentId": "{{string}}",
   "targetId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetDeploymentTarget_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [deploymentId](#API_GetDeploymentTarget_RequestSyntax) **   <a name="CodeDeploy-GetDeploymentTarget-request-deploymentId"></a>
 The unique ID of a deployment.
Type: String
Required: Yes

 ** [targetId](#API_GetDeploymentTarget_RequestSyntax) **   <a name="CodeDeploy-GetDeploymentTarget-request-targetId"></a>
 The unique ID of a deployment target.
Type: String
Required: Yes

## Response Syntax
<a name="API_GetDeploymentTarget_ResponseSyntax"></a>

```
{
   "deploymentTarget": {
      "cloudFormationTarget": {
         "deploymentId": "string",
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
         "resourceType": "string",
         "status": "string",
         "targetId": "string",
         "targetVersionWeight": number
      },
      "deploymentTargetType": "string",
      "ecsTarget": {
         "deploymentId": "string",
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
         "status": "string",
         "targetArn": "string",
         "targetId": "string",
         "taskSetsInfo": [
            {
               "desiredCount": number,
               "identifer": "string",
               "pendingCount": number,
               "runningCount": number,
               "status": "string",
               "targetGroup": {
                  "name": "string"
               },
               "taskSetLabel": "string",
               "trafficWeight": number
            }
         ]
      },
      "instanceTarget": {
         "deploymentId": "string",
         "instanceLabel": "string",
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
         "status": "string",
         "targetArn": "string",
         "targetId": "string"
      },
      "lambdaTarget": {
         "deploymentId": "string",
         "lambdaFunctionInfo": {
            "currentVersion": "string",
            "functionAlias": "string",
            "functionName": "string",
            "targetVersion": "string",
            "targetVersionWeight": number
         },
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
         "status": "string",
         "targetArn": "string",
         "targetId": "string"
      }
   }
}
```

## Response Elements
<a name="API_GetDeploymentTarget_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [deploymentTarget](#API_GetDeploymentTarget_ResponseSyntax) **   <a name="CodeDeploy-GetDeploymentTarget-response-deploymentTarget"></a>
 A deployment target that contains information about a deployment such as its status, lifecycle events, and when it was last updated. It also contains metadata about the deployment target. The deployment target metadata depends on the deployment target's type (`instanceTarget`, `lambdaTarget`, or `ecsTarget`).
Type: [DeploymentTarget](API_DeploymentTarget.md) object

## Errors
<a name="API_GetDeploymentTarget_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DeploymentDoesNotExistException **
The deployment with the user or AWS account does not exist.
HTTP Status Code: 400

 ** DeploymentIdRequiredException **
At least one deployment ID must be specified.
HTTP Status Code: 400

 ** DeploymentNotStartedException **
The specified deployment has not started.
HTTP Status Code: 400

 ** DeploymentTargetDoesNotExistException **
 The provided target ID does not belong to the attempted deployment.
HTTP Status Code: 400

 ** DeploymentTargetIdRequiredException **
 A deployment target ID was not provided.
HTTP Status Code: 400

 ** InvalidDeploymentIdException **
At least one of the deployment IDs was specified in an invalid format.
HTTP Status Code: 400

 ** InvalidDeploymentTargetIdException **
 The target ID provided was not valid.
HTTP Status Code: 400

 ** InvalidInstanceNameException **
The on-premises instance name was specified in an invalid format.
HTTP Status Code: 400

## See Also
<a name="API_GetDeploymentTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codedeploy-2014-10-06/GetDeploymentTarget)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codedeploy-2014-10-06/GetDeploymentTarget)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/GetDeploymentTarget)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codedeploy-2014-10-06/GetDeploymentTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/GetDeploymentTarget)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codedeploy-2014-10-06/GetDeploymentTarget)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codedeploy-2014-10-06/GetDeploymentTarget)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codedeploy-2014-10-06/GetDeploymentTarget)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codedeploy-2014-10-06/GetDeploymentTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/GetDeploymentTarget)
