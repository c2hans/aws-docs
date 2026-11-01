---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/codepipeline_example_codepipeline_CreateCustomActionType_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `CreateCustomActionType` with a CLI
<a name="codepipeline_example_codepipeline_CreateCustomActionType_section"></a>

The following code examples show how to use `CreateCustomActionType`.

------
#### [ CLI ]

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

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example creates a new custom action with the specified properties.**

```
New-CPCustomActionType -Category Build -ConfigurationProperty @{"Description" = "The name of the build project must be provided when this action is added to the pipeline."; "Key" = $True; "Name" = "ProjectName"; "Queryable" = $False; "Required" = $True; "Secret" = $False; "Type" = "String"} -Settings_EntityUrlTemplate "https://my-build-instance/job/{Config:ProjectName}/" -Settings_ExecutionUrlTemplate "https://my-build-instance/job/mybuildjob/lastSuccessfulBuild{ExternalExecutionId}/" -InputArtifactDetails_MaximumCount 1 -OutputArtifactDetails_MaximumCount 1 -InputArtifactDetails_MinimumCount 0 -OutputArtifactDetails_MinimumCount 0 -Provider "MyBuildProviderName" -Version 1
```
**Output:**

```
ActionConfigurationProperties : {ProjectName}
Id                            : Amazon.CodePipeline.Model.ActionTypeId
InputArtifactDetails          : Amazon.CodePipeline.Model.ArtifactDetails
OutputArtifactDetails         : Amazon.CodePipeline.Model.ArtifactDetails
Settings                      : Amazon.CodePipeline.Model.ActionTypeSettings
```
+  For API details, see [CreateCustomActionType](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example creates a new custom action with the specified properties.**

```
New-CPCustomActionType -Category Build -ConfigurationProperty @{"Description" = "The name of the build project must be provided when this action is added to the pipeline."; "Key" = $True; "Name" = "ProjectName"; "Queryable" = $False; "Required" = $True; "Secret" = $False; "Type" = "String"} -Settings_EntityUrlTemplate "https://my-build-instance/job/{Config:ProjectName}/" -Settings_ExecutionUrlTemplate "https://my-build-instance/job/mybuildjob/lastSuccessfulBuild{ExternalExecutionId}/" -InputArtifactDetails_MaximumCount 1 -OutputArtifactDetails_MaximumCount 1 -InputArtifactDetails_MinimumCount 0 -OutputArtifactDetails_MinimumCount 0 -Provider "MyBuildProviderName" -Version 1
```
**Output:**

```
ActionConfigurationProperties : {ProjectName}
Id                            : Amazon.CodePipeline.Model.ActionTypeId
InputArtifactDetails          : Amazon.CodePipeline.Model.ArtifactDetails
OutputArtifactDetails         : Amazon.CodePipeline.Model.ArtifactDetails
Settings                      : Amazon.CodePipeline.Model.ActionTypeSettings
```
+  For API details, see [CreateCustomActionType](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
