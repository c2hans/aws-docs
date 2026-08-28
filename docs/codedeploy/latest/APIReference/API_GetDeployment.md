---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_GetDeployment.html
---

# GetDeployment
<a name="API_GetDeployment"></a>

Gets information about a deployment.

**Note**
 The `content` property of the `appSpecContent` object in the returned revision is always null. Use `GetApplicationRevision` and the `sha256` property of the returned `appSpecContent` object to get the content of the deployment’s AppSpec file.

## Request Syntax
<a name="API_GetDeployment_RequestSyntax"></a>

```
{
   "deploymentId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetDeployment_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [deploymentId](#API_GetDeployment_RequestSyntax) **   <a name="CodeDeploy-GetDeployment-request-deploymentId"></a>
 The unique ID of a deployment associated with the user or AWS account.
Type: String
Required: Yes

## Response Syntax
<a name="API_GetDeployment_ResponseSyntax"></a>

```
{
   "deploymentInfo": {
      "additionalDeploymentStatusInfo": "string",
      "applicationName": "string",
      "autoRollbackConfiguration": {
         "enabled": boolean,
         "events": [ "string" ]
      },
      "blueGreenDeploymentConfiguration": {
         "deploymentReadyOption": {
            "actionOnTimeout": "string",
            "waitTimeInMinutes": number
         },
         "greenFleetProvisioningOption": {
            "action": "string"
         },
         "terminateBlueInstancesOnDeploymentSuccess": {
            "action": "string",
            "terminationWaitTimeInMinutes": number
         }
      },
      "completeTime": number,
      "computePlatform": "string",
      "createTime": number,
      "creator": "string",
      "deploymentConfigName": "string",
      "deploymentGroupName": "string",
      "deploymentId": "string",
      "deploymentOverview": {
         "Failed": number,
         "InProgress": number,
         "Pending": number,
         "Ready": number,
         "Skipped": number,
         "Succeeded": number
      },
      "deploymentStatusMessages": [ "string" ],
      "deploymentStyle": {
         "deploymentOption": "string",
         "deploymentType": "string"
      },
      "description": "string",
      "errorInformation": {
         "code": "string",
         "message": "string"
      },
      "externalId": "string",
      "fileExistsBehavior": "string",
      "ignoreApplicationStopFailures": boolean,
      "instanceTerminationWaitTimeStarted": boolean,
      "loadBalancerInfo": {
         "elbInfoList": [
            {
               "name": "string"
            }
         ],
         "targetGroupInfoList": [
            {
               "name": "string"
            }
         ],
         "targetGroupPairInfoList": [
            {
               "prodTrafficRoute": {
                  "listenerArns": [ "string" ]
               },
               "targetGroups": [
                  {
                     "name": "string"
                  }
               ],
               "testTrafficRoute": {
                  "listenerArns": [ "string" ]
               }
            }
         ]
      },
      "overrideAlarmConfiguration": {
         "alarms": [
            {
               "name": "string"
            }
         ],
         "enabled": boolean,
         "ignorePollAlarmFailure": boolean
      },
      "previousRevision": {
         "appSpecContent": {
            "content": "string",
            "sha256": "string"
         },
         "gitHubLocation": {
            "commitId": "string",
            "repository": "string"
         },
         "revisionType": "string",
         "s3Location": {
            "bucket": "string",
            "bundleType": "string",
            "eTag": "string",
            "key": "string",
            "version": "string"
         },
         "string": {
            "content": "string",
            "sha256": "string"
         }
      },
      "relatedDeployments": {
         "autoUpdateOutdatedInstancesDeploymentIds": [ "string" ],
         "autoUpdateOutdatedInstancesRootDeploymentId": "string"
      },
      "revision": {
         "appSpecContent": {
            "content": "string",
            "sha256": "string"
         },
         "gitHubLocation": {
            "commitId": "string",
            "repository": "string"
         },
         "revisionType": "string",
         "s3Location": {
            "bucket": "string",
            "bundleType": "string",
            "eTag": "string",
            "key": "string",
            "version": "string"
         },
         "string": {
            "content": "string",
            "sha256": "string"
         }
      },
      "rollbackInfo": {
         "rollbackDeploymentId": "string",
         "rollbackMessage": "string",
         "rollbackTriggeringDeploymentId": "string"
      },
      "startTime": number,
      "status": "string",
      "targetInstances": {
         "autoScalingGroups": [ "string" ],
         "ec2TagSet": {
            "ec2TagSetList": [
               [
                  {
                     "Key": "string",
                     "Type": "string",
                     "Value": "string"
                  }
               ]
            ]
         },
         "tagFilters": [
            {
               "Key": "string",
               "Type": "string",
               "Value": "string"
            }
         ]
      },
      "updateOutdatedInstancesOnly": boolean
   }
}
```

## Response Elements
<a name="API_GetDeployment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [deploymentInfo](#API_GetDeployment_ResponseSyntax) **   <a name="CodeDeploy-GetDeployment-response-deploymentInfo"></a>
Information about the deployment.
Type: [DeploymentInfo](API_DeploymentInfo.md) object

## Errors
<a name="API_GetDeployment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DeploymentDoesNotExistException **
The deployment with the user or AWS account does not exist.
HTTP Status Code: 400

 ** DeploymentIdRequiredException **
At least one deployment ID must be specified.
HTTP Status Code: 400

 ** InvalidDeploymentIdException **
At least one of the deployment IDs was specified in an invalid format.
HTTP Status Code: 400

## Examples
<a name="API_GetDeployment_Examples"></a>

### Example
<a name="API_GetDeployment_Example_1"></a>

This example illustrates one usage of GetDeployment.

#### Sample Request
<a name="API_GetDeployment_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codedeploy.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 31
X-Amz-Target: CodeDeploy_20141006.GetDeployment
X-Amz-Date: 20160707T015545Z
User-Agent: aws-cli/1.10.6 Python/2.7.9 Windows/7 botocore/1.3.28
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20160707/us-east-1/codedeploy/aws4_request,
	SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
    "deploymentId": "d-74D24AS7X"
}
```

#### Sample Response
<a name="API_GetDeployment_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 7dca4dcf-88e0-11e5-96e5-5hj1ee0ce84e
Content-Type: application/x-amz-json-1.1
Content-Length: 622

{
    "deploymentInfo": {
        "applicationName": "TestApp-us-east-1",
        "completeTime": 1446232681.319,
        "createTime": 1446232639.487,
        "creator": "user",
        "deploymentConfigName": "CodeDeployDefault.OneAtATime",
        "deploymentGroupName": "dep-group-def-456",
        "deploymentId": "d-74D35AS7C",
        "deploymentOverview": {
            "Failed": 0,
            "InProgress": 0,
            "Pending": 0,
            "Skipped": 0,
            "Succeeded": 1
        },
        "description": "Deployment for project 8FHE43",
        "ignoreApplicationStopFailures": false,
        "revision": {
            "revisionType": "S3",
            "s3Location": {
                "bucket": "project-1234",
                "bundleType": "zip",
                "eTag": "3fdd7b968314a096d5af1d649e26a4a",
                "key": "North-App.zip"
            }
        },
        "startTime": 1446744188.711,
        "status": "Succeeded"
    }
}
```

## See Also
<a name="API_GetDeployment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codedeploy-2014-10-06/GetDeployment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codedeploy-2014-10-06/GetDeployment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/GetDeployment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codedeploy-2014-10-06/GetDeployment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/GetDeployment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codedeploy-2014-10-06/GetDeployment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codedeploy-2014-10-06/GetDeployment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codedeploy-2014-10-06/GetDeployment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codedeploy-2014-10-06/GetDeployment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/GetDeployment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
