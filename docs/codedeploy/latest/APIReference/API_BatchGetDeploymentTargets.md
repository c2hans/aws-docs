---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_BatchGetDeploymentTargets.html
---

# BatchGetDeploymentTargets
<a name="API_BatchGetDeploymentTargets"></a>

 Returns an array of one or more targets associated with a deployment. This method works with all compute types and should be used instead of the deprecated `BatchGetDeploymentInstances`. The maximum number of targets that can be returned is 25.

 The type of targets returned depends on the deployment's compute platform or deployment method:
+  **EC2/On-premises**: Information about Amazon EC2 instance targets.
+  ** AWS Lambda **: Information about Lambda functions targets.
+  **Amazon ECS**: Information about Amazon ECS service targets.
+  **CloudFormation**: Information about targets of blue/green deployments initiated by a CloudFormation stack update.

## Request Syntax
<a name="API_BatchGetDeploymentTargets_RequestSyntax"></a>

```
{
   "deploymentId": "{{string}}",
   "targetIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_BatchGetDeploymentTargets_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [deploymentId](#API_BatchGetDeploymentTargets_RequestSyntax) **   <a name="CodeDeploy-BatchGetDeploymentTargets-request-deploymentId"></a>
 The unique ID of a deployment.
Type: String
Required: Yes

 ** [targetIds](#API_BatchGetDeploymentTargets_RequestSyntax) **   <a name="CodeDeploy-BatchGetDeploymentTargets-request-targetIds"></a>
 The unique IDs of the deployment targets. The compute platform of the deployment determines the type of the targets and their formats. The maximum number of deployment target IDs you can specify is 25.
+  For deployments that use the EC2/On-premises compute platform, the target IDs are Amazon EC2 or on-premises instances IDs, and their target type is `instanceTarget`.
+  For deployments that use the AWS Lambda compute platform, the target IDs are the names of Lambda functions, and their target type is `instanceTarget`.
+  For deployments that use the Amazon ECS compute platform, the target IDs are pairs of Amazon ECS clusters and services specified using the format `<clustername>:<servicename>`. Their target type is `ecsTarget`.
+  For deployments that are deployed with CloudFormation, the target IDs are CloudFormation stack IDs. Their target type is `cloudFormationTarget`.
Type: Array of strings
Required: Yes

## Response Syntax
<a name="API_BatchGetDeploymentTargets_ResponseSyntax"></a>

```
{
   "deploymentTargets": [
      {
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
   ]
}
```

## Response Elements
<a name="API_BatchGetDeploymentTargets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [deploymentTargets](#API_BatchGetDeploymentTargets_ResponseSyntax) **   <a name="CodeDeploy-BatchGetDeploymentTargets-response-deploymentTargets"></a>
 A list of target objects for a deployment. Each target object contains details about the target, such as its status and lifecycle events. The type of the target objects depends on the deployment' compute platform.
+  **EC2/On-premises**: Each target object is an Amazon EC2 or on-premises instance.
+  ** AWS Lambda **: The target object is a specific version of an AWS Lambda function.
+  **Amazon ECS**: The target object is an Amazon ECS service.
+  **CloudFormation**: The target object is an CloudFormation blue/green deployment.
Type: Array of [DeploymentTarget](API_DeploymentTarget.md) objects

## Errors
<a name="API_BatchGetDeploymentTargets_Errors"></a>

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

 ** DeploymentTargetListSizeExceededException **
 The maximum number of targets that can be associated with an Amazon ECS or AWS Lambda deployment was exceeded. The target list of both types of deployments must have exactly one item. This exception does not apply to EC2/On-premises deployments.
HTTP Status Code: 400

 ** InstanceDoesNotExistException **
 *This error has been deprecated.*
The specified instance does not exist in the deployment group.
HTTP Status Code: 400

 ** InvalidDeploymentIdException **
At least one of the deployment IDs was specified in an invalid format.
HTTP Status Code: 400

 ** InvalidDeploymentTargetIdException **
 The target ID provided was not valid.
HTTP Status Code: 400

## See Also
<a name="API_BatchGetDeploymentTargets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codedeploy-2014-10-06/BatchGetDeploymentTargets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codedeploy-2014-10-06/BatchGetDeploymentTargets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/BatchGetDeploymentTargets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codedeploy-2014-10-06/BatchGetDeploymentTargets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/BatchGetDeploymentTargets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codedeploy-2014-10-06/BatchGetDeploymentTargets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codedeploy-2014-10-06/BatchGetDeploymentTargets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codedeploy-2014-10-06/BatchGetDeploymentTargets)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codedeploy-2014-10-06/BatchGetDeploymentTargets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/BatchGetDeploymentTargets)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
