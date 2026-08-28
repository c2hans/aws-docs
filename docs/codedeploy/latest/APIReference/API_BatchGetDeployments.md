---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_BatchGetDeployments.html
---

# BatchGetDeployments
<a name="API_BatchGetDeployments"></a>

Gets information about one or more deployments. The maximum number of deployments that can be returned is 25.

## Request Syntax
<a name="API_BatchGetDeployments_RequestSyntax"></a>

```
{
   "deploymentIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_BatchGetDeployments_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [deploymentIds](#API_BatchGetDeployments_RequestSyntax) **   <a name="CodeDeploy-BatchGetDeployments-request-deploymentIds"></a>
 A list of deployment IDs, separated by spaces. The maximum number of deployment IDs you can specify is 25.
Type: Array of strings
Required: Yes

## Response Syntax
<a name="API_BatchGetDeployments_ResponseSyntax"></a>

```
{
   "deploymentsInfo": [
      {
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
   ]
}
```

## Response Elements
<a name="API_BatchGetDeployments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [deploymentsInfo](#API_BatchGetDeployments_ResponseSyntax) **   <a name="CodeDeploy-BatchGetDeployments-response-deploymentsInfo"></a>
 Information about the deployments.
Type: Array of [DeploymentInfo](API_DeploymentInfo.md) objects

## Errors
<a name="API_BatchGetDeployments_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BatchLimitExceededException **
The maximum number of names or IDs allowed for this request (100) was exceeded.
HTTP Status Code: 400

 ** DeploymentIdRequiredException **
At least one deployment ID must be specified.
HTTP Status Code: 400

 ** InvalidDeploymentIdException **
At least one of the deployment IDs was specified in an invalid format.
HTTP Status Code: 400

## Examples
<a name="API_BatchGetDeployments_Examples"></a>

### Example
<a name="API_BatchGetDeployments_Example_1"></a>

This example illustrates one usage of BatchGetDeployments.

#### Sample Request
<a name="API_BatchGetDeployments_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codedeploy.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 49
X-Amz-Target: CodeDeploy_20141006.BatchGetDeployments
X-Amz-Date: 20160707T232439Z
User-Agent: aws-cli/1.10.6 Python/2.7.9 Windows/7 botocore/1.3.28
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20160707/us-east-1/codedeploy/aws4_request,
	SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
    "deploymentIds": [
        "d-5SJAOL04C",
        "d-75H25AT3C"
    ]
}
```

#### Sample Response
<a name="API_BatchGetDeployments_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 620484b7-88cb-11e5-b497-75c49EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 1236

{
	"deploymentsInfo": [{
		"applicationName": "TestApp-us-east-1",
		"autoRollbackConfiguration": {
                "enabled": true
            },
		"completeTime": 1.446232681319E9,
		"createTime": 1.446232639487E9,
		"creator": "user",
		"deploymentConfigName": "CodeDeployDefault.OneAtATime",
		"deploymentGroupName": "dep-group-def-456",
		"deploymentId": "d-74D25AS7C",
		"deploymentOverview": {
			"Failed": 0,
			"InProgress": 0,
			"Pending": 0,
			"Skipped": 0,
			"Succeeded": 1
		},
		"deploymentStyle": {
                "deploymentOption": "WITHOUT_TRAFFIC_CONTROL",
                "deploymentType": "IN_PLACE"
            },
		"description": "Deployment for Project 5678",
		"ignoreApplicationStopFailures": false,
		"revision": {
			"revisionType": "S3",
			"s3Location": {
				"bucket": "project-1234",
				"bundleType": "zip",
				"eTag": "3fdd7b9196697a096d5af1d649e26a4a",
				"key": "North-App.zip"
			}
		},
		"startTime": 1.446246024315E9,
		"status": "Succeeded",
		"updateOutdatedInstancesOnly": false
	},
	{
		"applicationName": "ProductionApp-eu-central-1",
		 "autoRollbackConfiguration": {
                "enabled": false
            },
		"completeTime": 1.446246198207E9,
		"createTime": 1.446246024315E9,
		"creator": "user",
		"deploymentConfigName": "CodeDeployDefault.OneAtATime",
		"deploymentGroupName": "dep-group-jkl-234",
		"deploymentId": "d-5SJAOL04C",
		"deploymentOverview": {
			"Failed": 1,
			"InProgress": 0,
			"Pending": 0,
			"Skipped": 0,
			"Succeeded": 0
		},
		"deploymentStyle": {
                "deploymentOption": "WITHOUT_TRAFFIC_CONTROL",
                "deploymentType": "IN_PLACE"
            },
        "errorInformation": {
                "code": "HEALTH_CONSTRAINTS",
                "message": "The overall deployment failed because too many individual
                instances failed deployment, too few healthy instances are available
                for deployment, or some instances in your deployment group are experiencing
                problems."
            },
		"ignoreApplicationStopFailures": false,
		"revision": {
			"revisionType": "S3",
			"s3Location": {
				"bucket": "project-5678",
				"bundleType": "zip",
				"eTag": "9007397ea759a2f535bc9b6ef5414f04-1",
				"key": "Pipeline-123/AppBuild-1/CeGy55t"
			}
		},
		"startTime": 1.446246024315E9,
		"rollbackInfo": {},
		"status": "Failed",
		"updateOutdatedInstancesOnly": false
	}]
}
```

## See Also
<a name="API_BatchGetDeployments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codedeploy-2014-10-06/BatchGetDeployments)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codedeploy-2014-10-06/BatchGetDeployments)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/BatchGetDeployments)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codedeploy-2014-10-06/BatchGetDeployments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/BatchGetDeployments)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codedeploy-2014-10-06/BatchGetDeployments)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codedeploy-2014-10-06/BatchGetDeployments)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codedeploy-2014-10-06/BatchGetDeployments)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codedeploy-2014-10-06/BatchGetDeployments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/BatchGetDeployments)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
