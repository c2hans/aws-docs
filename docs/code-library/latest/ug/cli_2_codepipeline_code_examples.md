---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cli_2_codepipeline_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# CodePipeline examples using AWS CLI
<a name="cli_2_codepipeline_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with CodePipeline.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `acknowledge-job`
<a name="codepipeline_AcknowledgeJob_cli_2_topic"></a>

The following code example shows how to use `acknowledge-job`.

**AWS CLI**
**To retrieve information about a specified job**
The following `acknowledge-job` example returns information about a specified job, including the status of that job if it exists. This is only used for job workers and custom actions. To determine the value of nonce and the job ID, use aws codepipeline poll-for-jobs.

```
aws codepipeline acknowledge-job \
    --job-id {{f4f4ff82-2d11-EXAMPLE}} \
    --nonce {{3}}
```
Output:

```
{
    "status": "InProgress"
}
```
For more information, see [Create and add a custom action in CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/actions-create-custom-action.html) in the *AWS CodePipeline User Guide*.
+  For API details, see [AcknowledgeJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/acknowledge-job.html) in *AWS CLI Command Reference*.

### `create-custom-action-type`
<a name="codepipeline_CreateCustomActionType_cli_2_topic"></a>

The following code example shows how to use `create-custom-action-type`.

**AWS CLI**
**To create a custom action**
The following `create-custom-action-type` example creates a custom action for AWS CodePipeline using an already-created JSON file (here named MyCustomAction.json) that contains the structure of the custom action.

```
aws codepipeline create-custom-action-type \
    --cli-input-json {{file://MyCustomAction.json}}
```
Contents of `MyCustomAction.json`:

```
{
    "category": "Build",
    "provider": "MyJenkinsProviderName",
    "version": "1",
    "settings": {
        "entityUrlTemplate": "https://192.0.2.4/job/{Config:ProjectName}/",
        "executionUrlTemplate": "https://192.0.2.4/job/{Config:ProjectName}/lastSuccessfulBuild/{ExternalExecutionId}/"
    },
    "configurationProperties": [
        {
            "name": "MyJenkinsExampleBuildProject",
            "required": true,
            "key": true,
            "secret": false,
            "queryable": false,
            "description": "The name of the build project must be provided when this action is added to the pipeline.",
            "type": "String"
        }
    ],
    "inputArtifactDetails": {
        "maximumCount": 1,
        "minimumCount": 0
    },
    "outputArtifactDetails": {
        "maximumCount": 1,
        "minimumCount": 0
    }
}
```
This command returns the structure of the custom action.
Output:

```
{
    "actionType": {
        "id": {
            "category": "Build",
            "owner": "Custom",
            "provider": "MyJenkinsProviderName",
            "version": "1"
        },
        "settings": {
            "entityUrlTemplate": "https://192.0.2.4/job/{Config:ProjectName}/",
            "executionUrlTemplate": "https://192.0.2.4/job/{Config:ProjectName}/lastSuccessfulBuild/{ExternalExecutionId}/"
        },
        "actionConfigurationProperties": [
            {
                "name": "MyJenkinsExampleBuildProject",
                "required": true,
                "key": true,
                "secret": false,
                "queryable": false,
                "description": "The name of the build project must be provided when this action is added to the pipeline.",
                "type": "String"
            }
        ],
        "inputArtifactDetails": {
            "minimumCount": 0,
            "maximumCount": 1
        },
        "outputArtifactDetails": {
            "minimumCount": 0,
            "maximumCount": 1
        }
    }
}
```
For more information, see [Create and add a custom action in CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/actions-create-custom-action.html) in the *AWS CodePipeline User Guide*.
+  For API details, see [CreateCustomActionType](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/create-custom-action-type.html) in *AWS CLI Command Reference*.

### `create-pipeline`
<a name="codepipeline_CreatePipeline_cli_2_topic"></a>

The following code example shows how to use `create-pipeline`.

**AWS CLI**
**To create a pipeline**
The following `create-pipeline` example creates a pipeline in AWS CodePipeline using an already-created JSON file (here named MySecondPipeline.json) that contains the structure of the pipeline.

```
aws codepipeline create-pipeline \
    --cli-input-json {{file://MySecondPipeline.json}}
```
Contents of `MySecondPipeline.json`:

```
{
    "pipeline": {
        "roleArn": "arn:aws:iam::123456789012:role/AWS-CodePipeline-Service",
        "stages": [
            {
                "name": "Source",
                "actions": [
                    {
                        "inputArtifacts": [],
                        "name": "Source",
                        "actionTypeId": {
                            "category": "Source",
                            "owner": "AWS",
                            "version": "1",
                            "provider": "S3"
                        },
                        "outputArtifacts": [
                            {
                                "name": "MyApp"
                            }
                        ],
                        "configuration": {
                            "S3Bucket": "awscodepipeline-demo-bucket",
                            "S3ObjectKey": "aws-codepipeline-s3-aws-codedeploy_linux.zip"
                        },
                        "runOrder": 1
                    }
                ]
            },
            {
                "name": "Beta",
                "actions": [
                    {
                        "inputArtifacts": [
                            {
                                "name": "MyApp"
                            }
                        ],
                        "name": "CodePipelineDemoFleet",
                        "actionTypeId": {
                            "category": "Deploy",
                            "owner": "AWS",
                            "version": "1",
                            "provider": "CodeDeploy"
                        },
                        "outputArtifacts": [],
                        "configuration": {
                            "ApplicationName": "CodePipelineDemoApplication",
                            "DeploymentGroupName": "CodePipelineDemoFleet"
                        },
                        "runOrder": 1
                    }
                ]
            }
        ],
        "artifactStore": {
            "type": "S3",
            "location": "codepipeline-us-east-1-11EXAMPLE11"
        },
        "name": "MySecondPipeline",
        "version": 1
    }
}
```
This command returns the structure of the pipeline.
Output:

```
{
    "pipeline": {
        "roleArn": "arn:aws:iam::123456789012:role/AWS-CodePipeline-Service",
        "stages": [
            {
                "name": "Source",
                "actions": [
                    {
                        "inputArtifacts": [],
                        "name": "Source",
                        "actionTypeId": {
                            "category": "Source",
                            "owner": "AWS",
                            "version": "1",
                            "provider": "S3"
                        },
                        "outputArtifacts": [
                            {
                                "name": "MyApp"
                            }
                        ],
                        "configuration": {
                            "S3Bucket": "awscodepipeline-demo-bucket",
                            "S3ObjectKey": "aws-codepipeline-s3-aws-codedeploy_linux.zip"
                        },
                        "runOrder": 1
                    }
                ]
            },
            {
                "name": "Beta",
                "actions": [
                    {
                        "inputArtifacts": [
                            {
                                "name": "MyApp"
                            }
                        ],
                        "name": "CodePipelineDemoFleet",
                        "actionTypeId": {
                            "category": "Deploy",
                            "owner": "AWS",
                            "version": "1",
                            "provider": "CodeDeploy"
                        },
                        "outputArtifacts": [],
                        "configuration": {
                            "ApplicationName": "CodePipelineDemoApplication",
                            "DeploymentGroupName": "CodePipelineDemoFleet"
                        },
                        "runOrder": 1
                    }
                ]
            }
        ],
        "artifactStore": {
            "type": "S3",
            "location": "codepipeline-us-east-1-11EXAMPLE11"
        },
        "name": "MySecondPipeline",
        "version": 1
    }
}
```
For more information, see [Create a pipeline, stages, and actions](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-create.html) in the *AWS CodePipeline User Guide*.
+  For API details, see [CreatePipeline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/create-pipeline.html) in *AWS CLI Command Reference*.

### `delete-custom-action-type`
<a name="codepipeline_DeleteCustomActionType_cli_2_topic"></a>

The following code example shows how to use `delete-custom-action-type`.

**AWS CLI**
**To delete a custom action**
The following `delete-custom-action-type` example deletes a custom action in AWS CodePipeline by using an already-created JSON file (here named DeleteMyCustomAction.json) that contains the action type, provider name, and version number of the action to be deleted. Use the list-action-types command to view the correct values for category, version, and provider.

```
aws codepipeline delete-custom-action-type \
    --cli-input-json {{file://DeleteMyCustomAction.json}}
```
Contents of `DeleteMyCustomAction.json`:

```
{
    "category": "Build",
    "version": "1",
    "provider": "MyJenkinsProviderName"
}
```
This command produces no output.
For more information, see [Create and add a custom action in CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/actions-create-custom-action.html) in the *AWS CodePipeline User Guide*.
+  For API details, see [DeleteCustomActionType](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/delete-custom-action-type.html) in *AWS CLI Command Reference*.

### `delete-pipeline`
<a name="codepipeline_DeletePipeline_cli_2_topic"></a>

The following code example shows how to use `delete-pipeline`.

**AWS CLI**
**To delete a pipeline**
The following `delete-pipeline` example deletes a pipeline named MySecondPipeline from AWS CodePipeline. Use the list-pipelines command to view a list of pipelines associated with your AWS account.

```
aws codepipeline delete-pipeline \
    --name {{MySecondPipeline}}
```
This command produces no output.
For more information, see [Delete a pipeline in CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-delete.html) in the *AWS CodePipeline User Guide*.
+  For API details, see [DeletePipeline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/delete-pipeline.html) in *AWS CLI Command Reference*.

### `delete-webhook`
<a name="codepipeline_DeleteWebhook_cli_2_topic"></a>

The following code example shows how to use `delete-webhook`.

**AWS CLI**
**To delete a webhook**
The following `delete-webhook` example deletes a webhook for a GitHub version 1 source action. You must use the `deregister-webhook-with-third-party` command to deregister the webhook before you delete it.

```
aws codepipeline delete-webhook \
    --name {{my-webhook}}
```
This command produces no output.
For more information, see [Delete the webhook for your GitHub source](https://docs.aws.amazon.com/codepipeline/latest/userguide/appendix-github-oauth.html) in the *AWS CodePipeline User Guide*.
+  For API details, see [DeleteWebhook](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/delete-webhook.html) in *AWS CLI Command Reference*.

### `deregister-webhook-with-third-party`
<a name="codepipeline_DeregisterWebhookWithThirdParty_cli_2_topic"></a>

The following code example shows how to use `deregister-webhook-with-third-party`.

**AWS CLI**
**To deregister a webhook**
The following `deregister-webhook-with-third-party` example deletes a webhook for a GitHub version 1 source action. You must deregister the webhook before you delete it.

```
aws codepipeline deregister-webhook-with-third-party \
    --webhook-name {{my-webhook}}
```
This command produces no output.
For more information, see [Delete the webhook for your GitHub source](https://docs.aws.amazon.com/codepipeline/latest/userguide/appendix-github-oauth.html) in the *AWS CodePipeline User Guide*.
+  For API details, see [DeregisterWebhookWithThirdParty](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/deregister-webhook-with-third-party.html) in *AWS CLI Command Reference*.

### `disable-stage-transition`
<a name="codepipeline_DisableStageTransition_cli_2_topic"></a>

The following code example shows how to use `disable-stage-transition`.

**AWS CLI**
**To disable a transition to a stage in a pipeline**
The following `disable-stage-transition` example disables transitions into the Beta stage of the MyFirstPipeline pipeline in AWS CodePipeline.

```
aws codepipeline disable-stage-transition \
    --pipeline-name {{MyFirstPipeline}} \
    --stage-name {{Beta}}  \
    --transition-type {{Inbound}} \
    --reason {{"An example reason"}}
```
This command produces no output.
For more information, see [Working with stage transitions in CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/transitions.html) in the *AWS CodePipeline User Guide*.
+  For API details, see [DisableStageTransition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/disable-stage-transition.html) in *AWS CLI Command Reference*.

### `enable-stage-transition`
<a name="codepipeline_EnableStageTransition_cli_2_topic"></a>

The following code example shows how to use `enable-stage-transition`.

**AWS CLI**
**To enable a transition to a stage in a pipeline**
The following `enable-stage-transition` example enables transitions into the Beta stage of the MyFirstPipeline pipeline in AWS CodePipeline.

```
aws codepipeline enable-stage-transition \
    --pipeline-name {{MyFirstPipeline}} \
    --stage-name {{Beta}} \
    --transition-type {{Inbound}}
```
This command produces no output.
For more information, see [Working with stage transitions in CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/transitions.html) in the *AWS CodePipeline User Guide*.
+  For API details, see [EnableStageTransition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/enable-stage-transition.html) in *AWS CLI Command Reference*.

### `get-job-details`
<a name="codepipeline_GetJobDetails_cli_2_topic"></a>

The following code example shows how to use `get-job-details`.

**AWS CLI**
**To get details of a job**
The following `get-job-details` example returns details about a job whose ID is represented by f4f4ff82-2d11-EXAMPLE. This command is only used for custom actions. When this command is called, AWS CodePipeline returns temporary credentials for the Amazon S3 bucket used to store artifacts for the pipeline, if required for the custom action. This command will also return any secret values defined for the action, if any are defined.

```
aws codepipeline get-job-details \
    --job-id {{f4f4ff82-2d11-EXAMPLE}}
```
Output:

```
{
    "jobDetails": {
        "accountId": "123456789012",
        "data": {
            "actionConfiguration": {
                "configuration": {
                    "ProjectName": "MyJenkinsExampleTestProject"
                }
            },
            "actionTypeId": {
                "category": "Test",
                "owner": "Custom",
                "provider": "MyJenkinsProviderName",
                "version": "1"
            },
            "artifactCredentials": {
                "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
                "secretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
                "sessionToken": "fICCQD6m7oRw0uXOjANBgkqhkiG9w0BAQUFADCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb20wHhcNMTEwNDI1MjA0NTIxWhcNMTIwNDI0MjA0NTIxWjCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb20wgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMaK0dn+a4GmWIWJ21uUSfwfEvySWtC2XADZ4nB+BLYgVIk60CpiwsZ3G93vUEIO3IyNoH/f0wYK8m9TrDHudUZg3qX4waLG5M43q7Wgc/MbQITxOUSQv7c7ugFFDzQGBzZswY6786m86gpEIbb3OhjZnzcvQAaRHhdlQWIMm2nrAgMBAAEwDQYJKoZIhvcNAQEFBQADgYEAtCu4nUhVVxYUntneD9+h8Mg9q6q+auNKyExzyLwaxlAoo7TJHidbtS4J5iNmZgXL0FkbFFBjvSfpJIlJ00zbhNYS5f6GuoEDmFJl0ZxBHjJnyp378OD8uTs7fLvjx79LjSTbNYiytVbZPQUQ5Yaxu2jXnimvw3rrszlaEXAMPLE="
            },
            "inputArtifacts": [
                {
                    "location": {
                        "s3Location": {
                            "bucketName": "codepipeline-us-east-1-11EXAMPLE11",
                            "objectKey": "MySecondPipeline/MyAppBuild/EXAMPLE"
                        },
                        "type": "S3"
                    },
                    "name": "MyAppBuild"
                }
            ],
            "outputArtifacts": [],
            "pipelineContext": {
                "action": {
                    "name": "MyJenkinsTest-Action"
                },
                "pipelineName": "MySecondPipeline",
                "stage": {
                    "name": "Testing"
                }
            }
        },
        "id": "f4f4ff82-2d11-EXAMPLE"
    }
}
```
For more information, see [Create and add a custom action in CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/actions-create-custom-action.html) in the *AWS CodePipeline User Guide*.
+  For API details, see [GetJobDetails](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/get-job-details.html) in *AWS CLI Command Reference*.

### `get-pipeline-state`
<a name="codepipeline_GetPipelineState_cli_2_topic"></a>

The following code example shows how to use `get-pipeline-state`.

**AWS CLI**
**To get information about the state of a pipeline**
The following `get-pipeline-state` example returns the most recent state of a pipeline named MyFirstPipeline.

```
aws codepipeline get-pipeline-state \
    --name {{MyFirstPipeline}}
```
Output:

```
{
    "created": 1446137312.204,
    "pipelineName": "MyFirstPipeline",
    "pipelineVersion": 1,
    "stageStates": [
        {
            "actionStates": [
                {
                    "actionName": "Source",
                    "entityUrl": "https://console.aws.amazon.com/s3/home?#",
                    "latestExecution": {
                        "lastStatusChange": 1446137358.328,
                        "status": "Succeeded"
                    }
                }
            ],
            "stageName": "Source"
        },
        {
            "actionStates": [
                {
                    "actionName": "CodePipelineDemoFleet",
                    "entityUrl": "https://console.aws.amazon.com/codedeploy/home?#/applications/CodePipelineDemoApplication/deployment-groups/CodePipelineDemoFleet",
                    "latestExecution": {
                        "externalExecutionId": "d-EXAMPLE",
                        "externalExecutionUrl": "https://console.aws.amazon.com/codedeploy/home?#/deployments/d-EXAMPLE",
                        "lastStatusChange": 1446137493.131,
                        "status": "Succeeded",
                        "summary": "Deployment Succeeded"
                    }
                }
            ],
            "inboundTransitionState": {
                "enabled": true
            },
            "stageName": "Beta"
        }
    ],
    "updated": 1446137312.204
}
```
For more information, see [View pipeline details and history (CLI)](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-view-cli.html) in the *AWS CodePipeline User Guide*.
+  For API details, see [GetPipelineState](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/get-pipeline-state.html) in *AWS CLI Command Reference*.

### `get-pipeline`
<a name="codepipeline_GetPipeline_cli_2_topic"></a>

The following code example shows how to use `get-pipeline`.

**AWS CLI**
**To view the structure of a pipeline**
The following `get-pipeline` example returns the structure of a pipeline named MyFirstPipeline.

```
aws codepipeline get-pipeline \
    --name {{MyFirstPipeline}}
```
Output:

```
{
    "pipeline": {
        "roleArn": "arn:aws:iam::123456789012:role/AWS-CodePipeline-Service",
        "stages": [
            {
                "name": "Source",
                "actions": [
                    {
                        "inputArtifacts": [],
                        "name": "Source",
                        "actionTypeId": {
                            "category": "Source",
                            "owner": "AWS",
                            "version": "1",
                            "provider": "S3"
                        },
                        "outputArtifacts": [
                            {
                                "name": "MyApp"
                            }
                        ],
                        "configuration": {
                            "S3Bucket": "awscodepipeline-demo-bucket",
                            "S3ObjectKey": "aws-codepipeline-s3-aws-codedeploy_linux.zip"
                        },
                        "runOrder": 1
                    }
                ]
            },
            {
                "name": "Beta",
                "actions": [
                    {
                        "inputArtifacts": [
                            {
                                "name": "MyApp"
                            }
                        ],
                        "name": "CodePipelineDemoFleet",
                        "actionTypeId": {
                            "category": "Deploy",
                            "owner": "AWS",
                            "version": "1",
                            "provider": "CodeDeploy"
                        },
                        "outputArtifacts": [],
                        "configuration": {
                            "ApplicationName": "CodePipelineDemoApplication",
                            "DeploymentGroupName": "CodePipelineDemoFleet"
                        },
                        "runOrder": 1
                    }
                ]
            }
        ],
        "artifactStore": {
            "type": "S3",
            "location": "codepipeline-us-east-1-11EXAMPLE11"
        },
        "name": "MyFirstPipeline",
        "version": 1
    }
}
```
For more information, see [View pipeline details and history (CLI)](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-view-cli.html) in the *AWS CodePipeline User Guide*.
+  For API details, see [GetPipeline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/get-pipeline.html) in *AWS CLI Command Reference*.

### `list-action-executions`
<a name="codepipeline_ListActionExecutions_cli_2_topic"></a>

The following code example shows how to use `list-action-executions`.

**AWS CLI**
**To list action executions**
The following `list-action-executions` example views action execution details for a pipeline, such as action execution ID, input artifacts, output artifacts, execution result, and status.

```
aws codepipeline list-action-executions \
    --pipeline-name {{myPipeline}}
```
Output:

```
{
    "actionExecutionDetails": [
        {
            "pipelineExecutionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "actionExecutionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
            "pipelineVersion": 12,
            "stageName": "Deploy",
            "actionName": "Deploy",
            "startTime": 1598572628.6,
            "lastUpdateTime": 1598572661.255,
            "status": "Succeeded",
            "input": {
                "actionTypeId": {
                    "category": "Deploy",
                    "owner": "AWS",
                    "provider": "CodeDeploy",
                    "version": "1"
                },
                "configuration": {
                    "ApplicationName": "my-application",
                    "DeploymentGroupName": "my-deployment-group"
                },
                "resolvedConfiguration": {
                    "ApplicationName": "my-application",
                    "DeploymentGroupName": "my-deployment-group"
                },
                "region": "us-west-2",
                "inputArtifacts": [
                    {
                        "name": "SourceArtifact",
                        "s3location": {
                            "bucket": "artifact-bucket",
                            "key": "myPipeline/SourceArti/key"
                        }
                    }
                ],
                "namespace": "DeployVariables"
            },
            "output": {
                "outputArtifacts": [],
                "executionResult": {
                    "externalExecutionId": "d-EXAMPLEE5",
                    "externalExecutionSummary": "Deployment Succeeded",
                    "externalExecutionUrl": "https://myaddress.com"
                },
                "outputVariables": {}
            }
        },
        {
            "pipelineExecutionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "actionExecutionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
            "pipelineVersion": 12,
            "stageName": "Source",
            "actionName": "Source",
            "startTime": 1598572624.387,
            "lastUpdateTime": 1598572628.16,
            "status": "Succeeded",
            "input": {
                "actionTypeId": {
                    "category": "Source",
                    "owner": "AWS",
                    "provider": "CodeCommit",
                    "version": "1"
                },
                "configuration": {
                    "BranchName": "production",
                    "PollForSourceChanges": "false",
                    "RepositoryName": "my-repo"
                },
                "resolvedConfiguration": {
                    "BranchName": "production",
                    "PollForSourceChanges": "false",
                    "RepositoryName": "my-repo"
                },
                "region": "us-west-2",
                "inputArtifacts": [],
                "namespace": "SourceVariables"
            },
            "output": {
                "outputArtifacts": [
                    {
                        "name": "SourceArtifact",
                        "s3location": {
                            "bucket": "amzn-s3-demo-bucket",
                            "key": "myPipeline/SourceArti/key"
                        }
                    }
                ],
                "executionResult": {
                    "externalExecutionId": "1111111ad99dcd35914c00b7fbea13995EXAMPLE",
                    "externalExecutionSummary": "Edited template.yml",
                    "externalExecutionUrl": "https://myaddress.com"
                },
                "outputVariables": {
                    "AuthorDate": "2020-05-08T17:45:43Z",
                    "BranchName": "production",
                    "CommitId": "1111111ad99dcd35914c00b7fbea13995EXAMPLE",
                    "CommitMessage": "Edited template.yml",
                    "CommitterDate": "2020-05-08T17:45:43Z",
                    "RepositoryName": "my-repo"
                }
            }
        }
    ]
}
```
For more information, see [View action executions (CLI)](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-view-cli.html) in the *AWS CodePipeline User Guide*.
+  For API details, see [ListActionExecutions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/list-action-executions.html) in *AWS CLI Command Reference*.

### `list-action-types`
<a name="codepipeline_ListActionTypes_cli_2_topic"></a>

The following code example shows how to use `list-action-types`.

**AWS CLI**
**To view the action types available**
The following `list-action-types` example uses the `--action-owner-filter` option to return only custom actions. Used by itself, the `list-action-types` command returns the structure of all actions available to your AWS account.

```
aws codepipeline list-action-types \
    --action-owner-filter {{Custom}}
```
Output:

```
{
    "actionTypes": [
        {
            "inputArtifactDetails": {
                "maximumCount": 5,
                "minimumCount": 0
            },
            "actionConfigurationProperties": [
                {
                    "secret": false,
                    "required": true,
                    "name": "MyJenkinsExampleBuildProject",
                    "key": true,
                    "queryable": true
                }
            ],
            "outputArtifactDetails": {
                "maximumCount": 5,
                "minimumCount": 0
            },
            "id": {
                "category": "Build",
                "owner": "Custom",
                "version": "1",
                "provider": "MyJenkinsProviderName"
            },
            "settings": {
                "entityUrlTemplate": "http://192.0.2.4/job/{Config:ProjectName}",
                "executionUrlTemplate": "http://192.0.2.4/job/{Config:ProjectName}/{ExternalExecutionId}"
            }
        },
        {
            "inputArtifactDetails": {
                "maximumCount": 5,
                "minimumCount": 0
            },
            "actionConfigurationProperties": [
                {
                    "secret": false,
                    "required": true,
                    "name": "MyJenkinsExampleTestProject",
                    "key": true,
                    "queryable": true
                }
            ],
            "outputArtifactDetails": {
                "maximumCount": 5,
                "minimumCount": 0
            },
            "id": {
                "category": "Test",
                "owner": "Custom",
                "version": "1",
                "provider": "MyJenkinsProviderName"
            },
            "settings": {
                "entityUrlTemplate": "http://192.0.2.4/job/{Config:ProjectName}",
                "executionUrlTemplate": "http://192.0.2.4/job/{Config:ProjectName}/{ExternalExecutionId}"
            }
        }
    ]
}
```
For more information, see [Use action types, custom actions, and approval actions](https://docs.aws.amazon.com/codepipeline/latest/userguide/actions.html) in the *AWS CodePipeline User Guide*.
+  For API details, see [ListActionTypes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/list-action-types.html) in *AWS CLI Command Reference*.

### `list-pipeline-executions`
<a name="codepipeline_ListPipelineExecutions_cli_2_topic"></a>

The following code example shows how to use `list-pipeline-executions`.

**AWS CLI**
**To view pipeline execution history**
The following `list-pipeline-executions` example shows the pipeline execution history for a pipeline in your AWS account.

```
aws codepipeline list-pipeline-executions \
    --pipeline-name {{MyPipeline}}
```
Output:

```
{
    "pipelineExecutionSummaries": [
        {
            "lastUpdateTime": 1496380678.648,
            "pipelineExecutionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "startTime": 1496380258.243,
            "status": "Succeeded"
        },
        {
            "lastUpdateTime": 1496591045.634,
            "pipelineExecutionId": "3137f7cb-8d494hj4-039j-d84l-d7eu3EXAMPLE",
            "startTime": 1496590401.222,
            "status": "Succeeded"
        },
        {
            "lastUpdateTime": 1496946071.6456,
            "pipelineExecutionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
            "startTime": 1496945471.5645,
            "status": "Succeeded"
        }
    ]
}
```
For more information, see [View execution history](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-view-cli.html) in the *AWS CodePipeline User Guide*.
+  For API details, see [ListPipelineExecutions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/list-pipeline-executions.html) in *AWS CLI Command Reference*.

### `list-pipelines`
<a name="codepipeline_ListPipelines_cli_2_topic"></a>

The following code example shows how to use `list-pipelines`.

**AWS CLI**
**To view a list of pipelines**
The following `list-pipelines` example lists all AWS CodePipeline pipelines associated with the user's AWS account.

```
aws codepipeline list-pipelines
```
Output:

```
{
    "pipelines": [
        {
            "updated": 1439504274.641,
            "version": 1,
            "name": "MyFirstPipeline",
            "created": 1439504274.641
        },
        {
            "updated": 1436461837.992,
            "version": 2,
            "name": "MySecondPipeline",
            "created": 1436460801.381
        }
    ]
}
```
For more information, see [View pipeline details and history (CLI)](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-view-cli.html) in the *AWS CodePipeline User Guide*.
+  For API details, see [ListPipelines](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/list-pipelines.html) in *AWS CLI Command Reference*.

### `list-tags-for-resource`
<a name="codepipeline_ListTagsForResource_cli_2_topic"></a>

The following code example shows how to use `list-tags-for-resource`.

**AWS CLI**
**To list tags**
The following `list-tags-for-resource` example retrieves a list of all tags attached to the specified pipeline resource.

```
aws codepipeline list-tags-for-resource \
    --resource-arn {{arn:aws:codepipeline:us-west-2:123456789012:MyPipeline}}
```
Output:

```
{
    "tags": [
        {
            "key": "Project",
            "value": "ProjectA"
        },
        {
            "key": "IscontainerBased",
            "value": "true"
        }
    ]
}
```
For more information, see [View tags for a pipeline (CLI)](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-tag.html#pipelines-tag-list-cli) in the *AWS CodePipeline User Guide*.
+  For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/list-tags-for-resource.html) in *AWS CLI Command Reference*.

### `list-webhooks`
<a name="codepipeline_ListWebhooks_cli_2_topic"></a>

The following code example shows how to use `list-webhooks`.

**AWS CLI**
**To list webhooks**
The following `list-webhooks` example retrieves a list of all tags attached to the specified pipeline resource.

```
aws codepipeline list-webhooks
```
Output:

```
{
    "webhooks": [
        {
            "definition": {
                "authenticationConfiguration": {
                    "SecretToken": "Secret"
                },
                "name": "my-webhook",
                "authentication": "GITHUB_HMAC",
                "targetPipeline": "my-Pipeline",
                "targetAction": "Source",
                "filters": [
                    {
                        "jsonPath": "$.ref",
                        "matchEquals": "refs/heads/{Branch}"
                    }
                ]
            },
            "url": "https://webhooks.domain.com/trigger111111111EXAMPLE11111111111111111",
            "arn": "arn:aws:codepipeline:us-west-2:123456789012:webhook:my-webhook"
        }
    ]
}
```
For more information, see [List webhooks in your account](https://docs.aws.amazon.com/codepipeline/latest/userguide/appendix-github-oauth.html) in the *AWS CodePipeline User Guide*.
+  For API details, see [ListWebhooks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/list-webhooks.html) in *AWS CLI Command Reference*.

### `poll-for-jobs`
<a name="codepipeline_PollForJobs_cli_2_topic"></a>

The following code example shows how to use `poll-for-jobs`.

**AWS CLI**
**To view any available jobs**
The following `poll-for-jobs` example returns information about any jobs for a job worker to act upon. This example uses a pre-defined JSON file (MyActionTypeInfo.json) to supply information about the action type for which the job worker processes jobs. This command is only used for custom actions. When this command is called, AWS CodePipeline returns temporary credentials for the Amazon S3 bucket used to store artifacts for the pipeline. This command will also return any secret values defined for the action, if any are defined.

```
aws codepipeline poll-for-jobs \
    --cli-input-json {{file://MyActionTypeInfo.json}}
```
Contents of `MyActionTypeInfo.json`:

```
{
    "actionTypeId": {
        "category": "Test",
        "owner": "Custom",
        "provider": "MyJenkinsProviderName",
        "version": "1"
    },
    "maxBatchSize": 5,
    "queryParam": {
        "ProjectName": "MyJenkinsTestProject"
    }
}
```
Output:

```
{
    "jobs": [
        {
            "accountId": "123456789012",
            "data": {
                "actionConfiguration": {
                    "configuration": {
                        "ProjectName": "MyJenkinsExampleTestProject"
                    }
                },
                "actionTypeId": {
                    "category": "Test",
                    "owner": "Custom",
                    "provider": "MyJenkinsProviderName",
                    "version": "1"
                },
                "artifactCredentials": {
                    "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
                    "secretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
                    "sessionToken": "fICCQD6m7oRw0uXOjANBgkqhkiG9w0BAQUFADCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb20wHhcNMTEwNDI1MjA0NTIxWhcNMTIwNDI0MjA0NTIxWjCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb20wgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMaK0dn+a4GmWIWJ21uUSfwfEvySWtC2XADZ4nB+BLYgVIk60CpiwsZ3G93vUEIO3IyNoH/f0wYK8m9TrDHudUZg3qX4waLG5M43q7Wgc/MbQITxOUSQv7c7ugFFDzQGBzZswY6786m86gpEIbb3OhjZnzcvQAaRHhdlQWIMm2nrAgMBAAEwDQYJKoZIhvcNAQEFBQADgYEAtCu4nUhVVxYUntneD9+h8Mg9q6q+auNKyExzyLwaxlAoo7TJHidbtS4J5iNmZgXL0FkbFFBjvSfpJIlJ00zbhNYS5f6GuoEDmFJl0ZxBHjJnyp378OD8uTs7fLvjx79LjSTbNYiytVbZPQUQ5Yaxu2jXnimvw3rrszlaEXAMPLE="
                },
                "inputArtifacts": [
                    {
                        "location": {
                            "s3Location": {
                                "bucketName": "codepipeline-us-east-1-11EXAMPLE11",
                                "objectKey": "MySecondPipeline/MyAppBuild/EXAMPLE"
                            },
                            "type": "S3"
                        },
                        "name": "MyAppBuild"
                    }
                ],
                "outputArtifacts": [],
                "pipelineContext": {
                    "action": {
                        "name": "MyJenkinsTest-Action"
                    },
                    "pipelineName": "MySecondPipeline",
                    "stage": {
                        "name": "Testing"
                    }
                }
            },
            "id": "ef66c259-64f9-EXAMPLE",
            "nonce": "3"
        }
    ]
}
```
For more information, see [Create and add a custom action in CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/actions-create-custom-action.html) in the *AWS CodePipeline User Guide*.
+  For API details, see [PollForJobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/poll-for-jobs.html) in *AWS CLI Command Reference*.

### `put-webhook`
<a name="codepipeline_PutWebhook_cli_2_topic"></a>

The following code example shows how to use `put-webhook`.

**AWS CLI**
**To create a webhook**
The following `put-webhook` example creates a webhook for a GitHub version 1 source action. After you create the webhook, you must use the register-webhook-with-third-party command to register it.

```
aws codepipeline put-webhook \
    --cli-input-json {{file://webhook_json.json}}
```
Contents of `webhook_json.json`:

```
{
    "webhook": {
        "name": "my-webhook",
        "targetPipeline": "pipeline_name",
        "targetAction": "source_action_name",
        "filters": [
            {
                "jsonPath": "$.ref",
                "matchEquals": "refs/heads/{Branch}"
            }
        ],
        "authentication": "GITHUB_HMAC",
        "authenticationConfiguration": {
            "SecretToken": "secret"
        }
    }
}
```
Output:

```
{
    "webhook": {
        "url": "https://webhooks.domain.com/trigger111111111EXAMPLE11111111111111111",
        "definition": {
            "authenticationConfiguration": {
                "SecretToken": "secret"
            },
            "name": "my-webhook",
            "authentication": "GITHUB_HMAC",
            "targetPipeline": "pipeline_name",
            "targetAction": "Source",
            "filters": [
                {
                    "jsonPath": "$.ref",
                    "matchEquals": "refs/heads/{Branch}"
                }
            ]
        },
        "arn": "arn:aws:codepipeline:us-west-2:123456789012:webhook:my-webhook"
    }
}
```
For more information, see [Create a webhook for a GitHub source](https://docs.aws.amazon.com/codepipeline/latest/userguide/appendix-github-oauth.html) in the *AWS CodePipeline User Guide*.
+  For API details, see [PutWebhook](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/put-webhook.html) in *AWS CLI Command Reference*.

### `retry-stage-execution`
<a name="codepipeline_RetryStageExecution_cli_2_topic"></a>

The following code example shows how to use `retry-stage-execution`.

**AWS CLI**
**To retry a failed action**
The following `retry-stage-execution` example retries a stage that has a failed action.

```
aws codepipeline retry-stage-execution \
    --pipeline-name {{MyPipeline}} \
    --stage-name {{Deploy}} \
    --pipeline-execution-id {{b59babff-5f34-EXAMPLE}} \
    --retry-mode {{FAILED_ACTIONS}}
```
Output:

```
{
    "pipelineExecutionId": "b59babff-5f34-EXAMPLE"
}
```
For more information, see [Configuring stage retry for a failed stage or failed actions](https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-retry.html#stage-retry-cli) in the *AWS CodePipeline User Guide*.
+  For API details, see [RetryStageExecution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/retry-stage-execution.html) in *AWS CLI Command Reference*.

### `start-pipeline-execution`
<a name="codepipeline_StartPipelineExecution_cli_2_topic"></a>

The following code example shows how to use `start-pipeline-execution`.

**AWS CLI**
**To run the latest revision through a pipeline**
The following `start-pipeline-execution` example runs the latest revision present in the source stage of a pipeline through the pipeline named "MyFirstPipeline".

```
aws codepipeline start-pipeline-execution \
    --name {{MyFirstPipeline}}
```
Output:

```
{
    "pipelineExecutionId": "3137f7cb-7cf7-EXAMPLE"
}
```
For more information, see [Start a pipeline manually](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-rerun-manually.html) in the *AWS CodePipeline User Guide*.
+  For API details, see [StartPipelineExecution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/start-pipeline-execution.html) in *AWS CLI Command Reference*.

### `stop-pipeline-execution`
<a name="codepipeline_StopPipelineExecution_cli_2_topic"></a>

The following code example shows how to use `stop-pipeline-execution`.

**AWS CLI**
**To stop a pipeline execution**
The following `stop-pipeline-execution` example defaults to waiting until in-progress actions finish, and then stops the pipeline. You cannot choose to stop and wait if the execution is already in a Stopping state. You can choose to stop and abandon an execution that is already in a Stopping state.

```
aws codepipeline stop-pipeline-execution \
    --pipeline-name {{MyFirstPipeline}} \
    --pipeline-execution-id {{d-EXAMPLE}} \
    --reason {{"Stopping pipeline after the build action is done"}}
```
Output:

```
{
    "pipelineExecutionId": "d-EXAMPLE"
}
```
For more information, see [Stop a pipeline execution (CLI)](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-stop.html#pipelines-stop-cli) in the *AWS CodePipeline User Guide*.
+  For API details, see [StopPipelineExecution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/stop-pipeline-execution.html) in *AWS CLI Command Reference*.

### `tag-resource`
<a name="codepipeline_TagResource_cli_2_topic"></a>

The following code example shows how to use `tag-resource`.

**AWS CLI**
**To tag a resource**
The following `tag-resource` example associates a set of provided tags with a pipeline. Use this command to add or edit tags.

```
aws codepipeline tag-resource \
    --resource-arn {{arn:aws:codepipeline:us-west-2:123456789012:MyPipeline}} \
    --tags {{key=Project,value=ProjectA}} {{key=IscontainerBased,value=true}}
```
This command produces no output.
For more information, see [Add tags to a pipeline (CLI)](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-tag.html#pipelines-tag-add-cli) in the *AWS CodePipeline User Guide*.
+  For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/tag-resource.html) in *AWS CLI Command Reference*.

### `untag-resource`
<a name="codepipeline_UntagResource_cli_2_topic"></a>

The following code example shows how to use `untag-resource`.

**AWS CLI**
**To remove AWS tags from a connections resource**
The following `untag-resource` example removes a tag from the specified resource.

```
aws codepipeline untag-resource \
    --resource-arn {{arn:aws:codepipeline:us-west-2:123456789012:MyPipeline}} \
    --tag-keys {{Project}} {{IscontainerBased}}
```
This command produces no output.
For more information, see [Remove tags from a pipeline (CLI)](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-tag.html#pipelines-tag-delete-cli) in the *AWS CodePipeline User Guide*.
+  For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/untag-resource.html) in *AWS CLI Command Reference*.

### `update-pipeline`
<a name="codepipeline_UpdatePipeline_cli_2_topic"></a>

The following code example shows how to use `update-pipeline`.

**AWS CLI**
**To update the structure of a pipeline**
The following `update-pipeline` example uses the `--cli-input-json` argument with a pre-defined JSON file (MyFirstPipeline.json) to update the structure of a pipeline. AWS CodePipeline recognizes the pipeline name contained in the JSON file, and then applies any changes from modified fields in the pipeline structure to update the pipeline.
Use the following guidelines when creating the pre-defined JSON file:
If you are working with a pipeline structure retrieved using the get-pipeline command, you must remove the metadata section from the pipeline structure in the JSON file (the "metadata": { } lines and the "created," "pipelineARN," and "updated" fields within).The pipeline name cannot be changed.
Run the following command to update the pipeline.

```
aws codepipeline update-pipeline \
    --cli-input-json {{file://MyFirstPipeline.json}}
```
Contents of `MyFirstPipeline.json`:

```
{
    "pipeline": {
        "roleArn": "arn:aws:iam::123456789012:role/AWS-CodePipeline-Service",
        "stages": [
            {
                "name": "Source",
                "actions": [
                    {
                        "inputArtifacts": [],
                        "name": "Source",
                        "actionTypeId": {
                            "category": "Source",
                            "owner": "AWS",
                            "version": "1",
                            "provider": "S3"
                        },
                        "outputArtifacts": [
                            {
                                "name": "MyApp"
                            }
                        ],
                        "configuration": {
                            "S3Bucket": "awscodepipeline-demo-bucket2",
                            "S3ObjectKey": "aws-codepipeline-s3-aws-codedeploy_linux.zip"
                        },
                        "runOrder": 1
                    }
                ]
            },
            {
                "name": "Beta",
                "actions": [
                    {
                        "inputArtifacts": [
                            {
                                "name": "MyApp"
                            }
                        ],
                        "name": "CodePipelineDemoFleet",
                        "actionTypeId": {
                            "category": "Deploy",
                            "owner": "AWS",
                            "version": "1",
                            "provider": "CodeDeploy"
                        },
                        "outputArtifacts": [],
                        "configuration": {
                            "ApplicationName": "CodePipelineDemoApplication",
                            "DeploymentGroupName": "CodePipelineDemoFleet"
                        },
                        "runOrder": 1
                    }
                ]
            }
        ],
        "artifactStore": {
            "type": "S3",
            "location": "codepipeline-us-east-1-11EXAMPLE11"
        },
        "name": "MyFirstPipeline",
        "version": 1
    }
}
```
Output:

```
{
    "pipeline": {
        "artifactStore": {
            "location": "codepipeline-us-east-1-11EXAMPLE11",
            "type": "S3"
        },
        "name": "MyFirstPipeline",
        "roleArn": "arn:aws:iam::123456789012:role/AWS-CodePipeline-Service",
        "stages": [
            {
                "actions": [
                    {
                        "actionTypeId": {
                            "category": "Source",
                            "owner": "AWS",
                            "provider": "S3",
                            "version": "1"
                        },
                        "configuration": {
                            "S3Bucket": "awscodepipeline-demo-bucket2",
                            "S3ObjectKey": "aws-codepipeline-s3-aws-codedeploy_linux.zip"
                        },
                        "inputArtifacts": [],
                        "name": "Source",
                        "outputArtifacts": [
                            {
                                "name": "MyApp"
                            }
                        ],
                        "runOrder": 1
                    }
                ],
                "name": "Source"
            },
            {
                "actions": [
                    {
                        "actionTypeId": {
                            "category": "Deploy",
                            "owner": "AWS",
                            "provider": "CodeDeploy",
                            "version": "1"
                        },
                        "configuration": {
                            "ApplicationName": "CodePipelineDemoApplication",
                            "DeploymentGroupName": "CodePipelineDemoFleet"
                        },
                        "inputArtifacts": [
                            {
                                "name": "MyApp"
                            }
                        ],
                        "name": "CodePipelineDemoFleet",
                        "outputArtifacts": [],
                        "runOrder": 1
                    }
                ],
                "name": "Beta"
            }
        ],
        "version": 3
    }
}
```
For more information, see [Edit a pipeline in CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-edit.html) in the *AWS CodePipeline User Guide*.
+  For API details, see [UpdatePipeline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/update-pipeline.html) in *AWS CLI Command Reference*.
