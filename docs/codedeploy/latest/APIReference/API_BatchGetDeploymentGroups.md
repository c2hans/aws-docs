---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_BatchGetDeploymentGroups.html
---

# BatchGetDeploymentGroups
<a name="API_BatchGetDeploymentGroups"></a>

Gets information about one or more deployment groups.

## Request Syntax
<a name="API_BatchGetDeploymentGroups_RequestSyntax"></a>

```
{
   "applicationName": "{{string}}",
   "deploymentGroupNames": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_BatchGetDeploymentGroups_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [applicationName](#API_BatchGetDeploymentGroups_RequestSyntax) **   <a name="CodeDeploy-BatchGetDeploymentGroups-request-applicationName"></a>
The name of an AWS CodeDeploy application associated with the applicable user or AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [deploymentGroupNames](#API_BatchGetDeploymentGroups_RequestSyntax) **   <a name="CodeDeploy-BatchGetDeploymentGroups-request-deploymentGroupNames"></a>
The names of the deployment groups.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Response Syntax
<a name="API_BatchGetDeploymentGroups_ResponseSyntax"></a>

```
{
   "deploymentGroupsInfo": [
      {
         "alarmConfiguration": {
            "alarms": [
               {
                  "name": "string"
               }
            ],
            "enabled": boolean,
            "ignorePollAlarmFailure": boolean
         },
         "applicationName": "string",
         "autoRollbackConfiguration": {
            "enabled": boolean,
            "events": [ "string" ]
         },
         "autoScalingGroups": [
            {
               "hook": "string",
               "name": "string",
               "terminationHook": "string"
            }
         ],
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
         "computePlatform": "string",
         "deploymentConfigName": "string",
         "deploymentGroupId": "string",
         "deploymentGroupName": "string",
         "deploymentStyle": {
            "deploymentOption": "string",
            "deploymentType": "string"
         },
         "ec2TagFilters": [
            {
               "Key": "string",
               "Type": "string",
               "Value": "string"
            }
         ],
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
         "ecsServices": [
            {
               "clusterName": "string",
               "serviceName": "string"
            }
         ],
         "lastAttemptedDeployment": {
            "createTime": number,
            "deploymentId": "string",
            "endTime": number,
            "status": "string"
         },
         "lastSuccessfulDeployment": {
            "createTime": number,
            "deploymentId": "string",
            "endTime": number,
            "status": "string"
         },
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
         "onPremisesInstanceTagFilters": [
            {
               "Key": "string",
               "Type": "string",
               "Value": "string"
            }
         ],
         "onPremisesTagSet": {
            "onPremisesTagSetList": [
               [
                  {
                     "Key": "string",
                     "Type": "string",
                     "Value": "string"
                  }
               ]
            ]
         },
         "outdatedInstancesStrategy": "string",
         "serviceRoleArn": "string",
         "targetRevision": {
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
         "terminationHookEnabled": boolean,
         "triggerConfigurations": [
            {
               "triggerEvents": [ "string" ],
               "triggerName": "string",
               "triggerTargetArn": "string"
            }
         ]
      }
   ],
   "errorMessage": "string"
}
```

## Response Elements
<a name="API_BatchGetDeploymentGroups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [deploymentGroupsInfo](#API_BatchGetDeploymentGroups_ResponseSyntax) **   <a name="CodeDeploy-BatchGetDeploymentGroups-response-deploymentGroupsInfo"></a>
Information about the deployment groups.
Type: Array of [DeploymentGroupInfo](API_DeploymentGroupInfo.md) objects

 ** [errorMessage](#API_BatchGetDeploymentGroups_ResponseSyntax) **   <a name="CodeDeploy-BatchGetDeploymentGroups-response-errorMessage"></a>
Information about errors that might have occurred during the API call.
Type: String

## Errors
<a name="API_BatchGetDeploymentGroups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ApplicationDoesNotExistException **
The application does not exist with the user or AWS account.
HTTP Status Code: 400

 ** ApplicationNameRequiredException **
The minimum number of required application names was not specified.
HTTP Status Code: 400

 ** BatchLimitExceededException **
The maximum number of names or IDs allowed for this request (100) was exceeded.
HTTP Status Code: 400

 ** DeploymentConfigDoesNotExistException **
The deployment configuration does not exist with the user or AWS account.
HTTP Status Code: 400

 ** DeploymentGroupNameRequiredException **
The deployment group name was not specified.
HTTP Status Code: 400

 ** InvalidApplicationNameException **
The application name was specified in an invalid format.
HTTP Status Code: 400

 ** InvalidDeploymentGroupNameException **
The deployment group name was specified in an invalid format.
HTTP Status Code: 400

## Examples
<a name="API_BatchGetDeploymentGroups_Examples"></a>

### Example
<a name="API_BatchGetDeploymentGroups_Example_1"></a>

This example illustrates one usage of BatchGetDeploymentGroups.

#### Sample Request
<a name="API_BatchGetDeploymentGroups_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codedeploy.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 90
X-Amz-Target: CodeDeploy_20141006.BatchGetDeploymentGroups
X-Amz-Date: 20160317T175340Z
User-Agent: aws-cli/1.10.6 Python/2.7.9 Windows/7 botocore/1.3.28
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20160317/us-east-1/codedeploy/aws4_request,
SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
    "applicationName": "TestApp-us-east-1",
    "deploymentGroupNames": [
        "dep-group-def-456",
        "dep-group-jkl-234"
    ]
}
```

#### Sample Response
<a name="API_BatchGetDeploymentGroups_Example_1_Response"></a>

```
{
    "deploymentGroupsInfo": [
        {
            "applicationName": "TestApp-us-east-1",
            "autoRollbackConfiguration": {
                "enabled": false
            },
            "autoScalingGroups": [],
            "deploymentConfigName": "CodeDeployDefault.OneAtATime",
            "deploymentGroupId": "d-DBF57CS3H",
            "deploymentGroupName": "dep-group-def-456",
            "deploymentStyle": {
                "deploymentOption": "WITHOUT_TRAFFIC_CONTROL",
                "deploymentType": "IN_PLACE"
            },
            "ec2TagFilters": [
                {
                    "Key": "Name",
                    "Type": "KEY_AND_VALUE",
                    "Value": "Project-ABC"
                }
            ],
            "onPremisesInstanceTagFilters": [],
            "serviceRoleArn": "arn:aws:iam::444455556666:role/AnyCompany-service-role",
            "targetRevision": {
                "revisionType": "S3",
                "s3Location": {
                    "bucket": "project-abc",
                    "bundleType": "zip",
                    "eTag": "ffe5402cff48b652bf903700453f7408",
                    "key": "North-App-3.zip",
                    "version": "4eQLXx7nw0iP22hxwt2_YXrUq972qkG6"
                }
            },
            "triggerConfigurations": [
                {
                    "triggerEvents": [
                        "DeploymentFailure"
                    ],
                    "triggerName": "Trigger-group-us-east-1-deploy-fail",
                    "triggerTargetArn": "arn:aws:sns:us-east-1:80398EXAMPLE:us-east-deploy-fail"
                }
            ]
        },
        {
            "applicationName": "TestApp-us-east-1",
            "autoRollbackConfiguration": {
                "enabled": false
            },
            "autoScalingGroups": [],
            "deploymentConfigName": "CodeDeployDefault.OneAtATime",
            "deploymentGroupId": "d-DCS73HBF5",
            "deploymentGroupName": "dep-group-def-456",
            "deploymentStyle": {
                "deploymentOption": "WITHOUT_TRAFFIC_CONTROL",
                "deploymentType": "IN_PLACE"
            },
            "ec2TagFilters": [
                {
                    "Key": "Name",
                    "Type": "KEY_AND_VALUE",
                    "Value": "Project-DEF"
                }
            ],
            "onPremisesInstanceTagFilters": [],
            "serviceRoleArn": "arn:aws:iam::444455556666:role/AnyCompany-service-role",
            "targetRevision": {
                "revisionType": "S3",
                "s3Location": {
                    "bucket": "project-def",
                    "bundleType": "zip",
                    "eTag": "3fdd7b9196697a096d5af1d649e26a4a",
                    "key": "North-App-3.zip",
                    "version": "BXrUq974e0iP22hxwt2_QLXx7nw3kjB9"
                }
            },
            "triggerConfigurations": [
                {
                    "triggerEvents": [
                        "DeploymentSuccess"
                    ],
                    "triggerName": "Trigger-group-us-east-1-deploy-succeed",
                    "triggerTargetArn": "arn:aws:sns:us-east-1:80398EXAMPLE:us-east-deploy-succeed"
                }
            ]
        }
    ],
    "errorMessage": ""
}
```

## See Also
<a name="API_BatchGetDeploymentGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codedeploy-2014-10-06/BatchGetDeploymentGroups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codedeploy-2014-10-06/BatchGetDeploymentGroups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/BatchGetDeploymentGroups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codedeploy-2014-10-06/BatchGetDeploymentGroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/BatchGetDeploymentGroups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codedeploy-2014-10-06/BatchGetDeploymentGroups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codedeploy-2014-10-06/BatchGetDeploymentGroups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codedeploy-2014-10-06/BatchGetDeploymentGroups)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codedeploy-2014-10-06/BatchGetDeploymentGroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/BatchGetDeploymentGroups)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
