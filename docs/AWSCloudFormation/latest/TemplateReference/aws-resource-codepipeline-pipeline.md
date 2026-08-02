---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codepipeline-pipeline.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodePipeline::Pipeline
<a name="aws-resource-codepipeline-pipeline"></a>

The `AWS::CodePipeline::Pipeline` resource creates a CodePipeline pipeline that describes how software changes go through a release process. For more information, see [What Is CodePipeline?](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) in the *CodePipeline User Guide*.

For an example in YAML and JSON that contains the parameters in this reference, see [Examples](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codepipeline-pipeline.html#aws-resource-codepipeline-pipeline--examples).

## Syntax
<a name="aws-resource-codepipeline-pipeline-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-codepipeline-pipeline-syntax.json"></a>

```
{
  "Type" : "AWS::CodePipeline::Pipeline",
  "Properties" : {
      "[ArtifactStore](#cfn-codepipeline-pipeline-artifactstore)" : {{ArtifactStore}},
      "[ArtifactStores](#cfn-codepipeline-pipeline-artifactstores)" : {{[ ArtifactStoreMap, ... ]}},
      "[DisableInboundStageTransitions](#cfn-codepipeline-pipeline-disableinboundstagetransitions)" : {{[ StageTransition, ... ]}},
      "[ExecutionMode](#cfn-codepipeline-pipeline-executionmode)" : {{String}},
      "[Name](#cfn-codepipeline-pipeline-name)" : {{String}},
      "[PipelineType](#cfn-codepipeline-pipeline-pipelinetype)" : {{String}},
      "[RestartExecutionOnUpdate](#cfn-codepipeline-pipeline-restartexecutiononupdate)" : {{Boolean}},
      "[RoleArn](#cfn-codepipeline-pipeline-rolearn)" : {{String}},
      "[Stages](#cfn-codepipeline-pipeline-stages)" : {{[ StageDeclaration, ... ]}},
      "[Tags](#cfn-codepipeline-pipeline-tags)" : {{[ Tag, ... ]}},
      "[Triggers](#cfn-codepipeline-pipeline-triggers)" : {{[ PipelineTriggerDeclaration, ... ]}},
      "[Variables](#cfn-codepipeline-pipeline-variables)" : {{[ VariableDeclaration, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-codepipeline-pipeline-syntax.yaml"></a>

```
Type: AWS::CodePipeline::Pipeline
Properties:
  [ArtifactStore](#cfn-codepipeline-pipeline-artifactstore): {{
    ArtifactStore}}
  [ArtifactStores](#cfn-codepipeline-pipeline-artifactstores): {{
    - ArtifactStoreMap}}
  [DisableInboundStageTransitions](#cfn-codepipeline-pipeline-disableinboundstagetransitions): {{
    - StageTransition}}
  [ExecutionMode](#cfn-codepipeline-pipeline-executionmode): {{String}}
  [Name](#cfn-codepipeline-pipeline-name): {{String}}
  [PipelineType](#cfn-codepipeline-pipeline-pipelinetype): {{String}}
  [RestartExecutionOnUpdate](#cfn-codepipeline-pipeline-restartexecutiononupdate): {{Boolean}}
  [RoleArn](#cfn-codepipeline-pipeline-rolearn): {{String}}
  [Stages](#cfn-codepipeline-pipeline-stages): {{
    - StageDeclaration}}
  [Tags](#cfn-codepipeline-pipeline-tags): {{
    - Tag}}
  [Triggers](#cfn-codepipeline-pipeline-triggers): {{
    - PipelineTriggerDeclaration}}
  [Variables](#cfn-codepipeline-pipeline-variables): {{
    - VariableDeclaration}}
```

## Properties
<a name="aws-resource-codepipeline-pipeline-properties"></a>

`ArtifactStore`  <a name="cfn-codepipeline-pipeline-artifactstore"></a>
The S3 bucket where artifacts for the pipeline are stored.
You must include either `artifactStore` or `artifactStores` in your pipeline, but you cannot use both. If you create a cross-region action in your pipeline, you must use `artifactStores`.
*Required*: Conditional
*Type*: [ArtifactStore](aws-properties-codepipeline-pipeline-artifactstore.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ArtifactStores`  <a name="cfn-codepipeline-pipeline-artifactstores"></a>
A mapping of `artifactStore` objects and their corresponding AWS Regions. There must be an artifact store for the pipeline Region and for each cross-region action in the pipeline.
You must include either `artifactStore` or `artifactStores` in your pipeline, but you cannot use both. If you create a cross-region action in your pipeline, you must use `artifactStores`.
*Required*: Conditional
*Type*: Array of [ArtifactStoreMap](aws-properties-codepipeline-pipeline-artifactstoremap.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisableInboundStageTransitions`  <a name="cfn-codepipeline-pipeline-disableinboundstagetransitions"></a>
Represents the input of a `DisableStageTransition` action.
*Required*: No
*Type*: Array of [StageTransition](aws-properties-codepipeline-pipeline-stagetransition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExecutionMode`  <a name="cfn-codepipeline-pipeline-executionmode"></a>
The method that the pipeline will use to handle multiple executions. The default mode is SUPERSEDED.
*Required*: No
*Type*: String
*Allowed values*: `QUEUED | SUPERSEDED | PARALLEL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-codepipeline-pipeline-name"></a>
The name of the pipeline.
*Required*: No
*Type*: String
*Pattern*: `[A-Za-z0-9.@\-_]+`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PipelineType`  <a name="cfn-codepipeline-pipeline-pipelinetype"></a>
CodePipeline provides the following pipeline types, which differ in characteristics and price, so that you can tailor your pipeline features and cost to the needs of your applications.
+ V1 type pipelines have a JSON structure that contains standard pipeline, stage, and action-level parameters.
+ V2 type pipelines have the same structure as a V1 type, along with additional parameters for release safety and trigger configuration.
Including V2 parameters, such as triggers on Git tags, in the pipeline JSON when creating or updating a pipeline will result in the pipeline having the V2 type of pipeline and the associated costs.
For information about pricing for CodePipeline, see [Pricing](https://aws.amazon.com/codepipeline/pricing/).
 For information about which type of pipeline to choose, see [What type of pipeline is right for me?](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipeline-types-planning.html).
*Required*: No
*Type*: String
*Allowed values*: `V1 | V2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RestartExecutionOnUpdate`  <a name="cfn-codepipeline-pipeline-restartexecutiononupdate"></a>
Indicates whether to rerun the CodePipeline pipeline after you update it.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-codepipeline-pipeline-rolearn"></a>
The Amazon Resource Name (ARN) for CodePipeline to use to either perform actions with no `actionRoleArn`, or to use to assume roles for actions with an `actionRoleArn`.
*Required*: Yes
*Type*: String
*Pattern*: `arn:aws(-[\w]+)*:iam::[0-9]{12}:role/.*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Stages`  <a name="cfn-codepipeline-pipeline-stages"></a>
Represents information about a stage and its definition.
*Required*: Yes
*Type*: Array of [StageDeclaration](aws-properties-codepipeline-pipeline-stagedeclaration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-codepipeline-pipeline-tags"></a>
Specifies the tags applied to the pipeline.
*Required*: No
*Type*: Array of [Tag](aws-properties-codepipeline-pipeline-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Triggers`  <a name="cfn-codepipeline-pipeline-triggers"></a>
The trigger configuration specifying a type of event, such as Git tags, that starts the pipeline.
When a trigger configuration is specified, default change detection for repository and branch commits is disabled.
*Required*: No
*Type*: Array of [PipelineTriggerDeclaration](aws-properties-codepipeline-pipeline-pipelinetriggerdeclaration.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Variables`  <a name="cfn-codepipeline-pipeline-variables"></a>
A list that defines the pipeline variables for a pipeline resource. Variable names can have alphanumeric and underscore characters, and the values must match `[A-Za-z0-9@\-_]+`.
*Required*: No
*Type*: Array of [VariableDeclaration](aws-properties-codepipeline-pipeline-variabledeclaration.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-codepipeline-pipeline-return-values"></a>

### Ref
<a name="aws-resource-codepipeline-pipeline-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the pipeline name, such as mysta-MyPipeline-A1BCDEFGHIJ2.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-codepipeline-pipeline-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-codepipeline-pipeline-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`Version`  <a name="Version-fn::getatt"></a>
The version of the pipeline.
A new pipeline is always assigned a version number of 1. This number increments when a pipeline is updated.

## Examples
<a name="aws-resource-codepipeline-pipeline--examples"></a>

**Topics**
+ [Pipeline with two stages and trigger configuration](#aws-resource-codepipeline-pipeline--examples--Pipeline_with_two_stages_and_trigger_configuration)
+ [Pipeline with source stage and a stage configured for automatic rollback on failure](#aws-resource-codepipeline-pipeline--examples--Pipeline_with_source_stage_and_a_stage_configured_for_automatic_rollback_on_failure)

### Pipeline with two stages and trigger configuration
<a name="aws-resource-codepipeline-pipeline--examples--Pipeline_with_two_stages_and_trigger_configuration"></a>

The following example creates a pipeline with a source stage and a beta stage. For the source stage, CodePipeline uses a connection to a GitHub repository. The beta stage builds those changes by using CodeBuild. The pipeline is configured to start using trigger filtering. The pipeline will start when push events meet the Git tags, branches, and file path filter criteria specified. Also, the pipeline will start when pull requests meet the filter criteria for the branch names, file paths, and pull request events specified. For example, when a pull request for branches and file paths containing `release-*` is closed, the pipeline will start.

#### JSON
<a name="aws-resource-codepipeline-pipeline--examples--Pipeline_with_two_stages_and_trigger_configuration--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "CodePipeline sample",
    "Parameters": {
        "CodePipelineServiceRole": {
            "Type": "String"
        },
        "ArtifactStoreS3Location": {
            "Type": "String"
        },
        "SourceActionName": {
            "Type": "String"
        }
    },
    "Resources": {
        "CodePipelineForIntegTest": {
            "Type": "AWS::CodePipeline::Pipeline",
            "Properties": {
                "RoleArn": {
                    "Ref": "CodePipelineServiceRole"
                },
                "Stages": [
                    {
                        "Name": "Source",
                        "Actions": [
                            {
                                "Name": {
                                    "Ref": "SourceActionName"
                                },
                                "InputArtifacts": [],
                                "ActionTypeId": {
                                    "Category": "Source",
                                    "Owner": "AWS",
                                    "Version": "1",
                                    "Provider": "CodeStarSourceConnection"
                                },
                                "OutputArtifacts": [
                                    {
                                        "Name": "SourceOutput"
                                    }
                                ],
                                "Configuration": {
                                    "BranchName": "main",
                                    "ConnectionArn": "arn:aws:codestar-connections:us-east-1:123456789123:connection/id",
                                    "FullRepositoryId": "repo-owner/sample-project"
                                },
                                "RunOrder": 1
                            }
                        ]
                    },
                    {
                        "Name": "Beta",
                        "Actions": [
                            {
                                "Name": "BetaAction",
                                "InputArtifacts": [
                                    {
                                        "Name": "SourceOutput"
                                    }
                                ],
                                "ActionTypeId": {
                                    "Category": "Build",
                                    "Owner": "AWS",
                                    "Provider": "CodeBuild",
                                    "Version": "1"
                                },
                                "Configuration": {
                                    "ProjectName": "Sample"
                                },
                                "RunOrder": 1
                            }
                        ]
                    }
                ],
                "Triggers": [
                    {
                        "ProviderType": "CodeStarSourceConnection",
                        "GitConfiguration": {
                            "Push": [
                                {
                                    "Tags": {
                                        "Excludes": [
                                            "beta-*"
                                        ],
                                        "Includes": [
                                            "release-*"
                                        ]
                                    }
                                },
                                {
                                    "Branches": {
                                        "Excludes": [
                                            "beta-*"
                                        ],
                                        "Includes": [
                                            "release-*"
                                        ]
                                    },
                                    "FilePaths": {
                                        "Includes": [
                                            "projectA/**",
                                            "common/**/*.js"
                                        ],
                                        "Excludes": [
                                            "**/README.md",
                                            "**/LICENSE",
                                            "**/CONTRIBUTING.md"
                                        ]
                                    }
                                }
                            ],
                            "PullRequest": [
                                {
                                    "Branches": {
                                        "Excludes": [
                                            "stable-v1-*"
                                        ],
                                        "Includes": [
                                            "stable-*",
                                            "release-*"
                                        ]
                                    },
                                    "FilePaths": {
                                        "Includes": [
                                            "projectA/**",
                                            "common/**/*.js"
                                        ],
                                        "Excludes": [
                                            "**/README.md",
                                            "**/LICENSE",
                                            "**/CONTRIBUTING.md"
                                        ]
                                    },
                                    "Events": [
                                        "CLOSED"
                                    ]
                                }
                            ],
                            "SourceActionName": {
                                "Ref": "SourceActionName"
                            }
                        }
                    }
                ],
                "PipelineType": "V2",
                "ExecutionMode": "PARALLEL",
                "ArtifactStore": {
                    "Type": "S3",
                    "Location": {
                        "Ref": "ArtifactStoreS3Location"
                    }
                }
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-codepipeline-pipeline--examples--Pipeline_with_two_stages_and_trigger_configuration--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Description: CodePipeline sample
Parameters:
  CodePipelineServiceRole:
    Type: String
  ArtifactStoreS3Location:
    Type: String
  SourceActionName:
    Type: String
Resources:
  CodePipelineForIntegTest:
    Type: 'AWS::CodePipeline::Pipeline'
    Properties:
      RoleArn: !Ref CodePipelineServiceRole
      Stages:
        - Name: Source
          Actions:
            - Name: !Ref SourceActionName
              InputArtifacts: []
              ActionTypeId:
                Category: Source
                Owner: AWS
                Version: '1'
                Provider: CodeStarSourceConnection
              OutputArtifacts:
                - Name: SourceOutput
              Configuration:
                BranchName: main
                ConnectionArn: >-
                  arn:aws:codestar-connections:us-east-1:123456789123:connection/id
                FullRepositoryId: repo-owner/sample-project
              RunOrder: 1
        - Name: Beta
          Actions:
            - Name: BetaAction
              InputArtifacts:
                - Name: SourceOutput
              ActionTypeId:
                Category: Build
                Owner: AWS
                Provider: CodeBuild
                Version: '1'
              Configuration:
                ProjectName: Sample
              RunOrder: 1
      Triggers:
        - ProviderType: CodeStarSourceConnection
          GitConfiguration:
            Push:
              - Tags:
                  Excludes:
                    - beta-*
                  Includes:
                    - release-*
              - Branches:
                  Excludes:
                    - beta-*
                  Includes:
                    - release-*
                FilePaths:
                  Includes:
                    - projectA/**
                    - common/**/*.js
                  Excludes:
                    - '**/README.md'
                    - '**/LICENSE'
                    - '**/CONTRIBUTING.md'
            PullRequest:
              - Branches:
                  Excludes:
                    - stable-v1-*
                  Includes:
                    - stable-*
                    - release-*
                FilePaths:
                  Includes:
                    - projectA/**
                    - common/**/*.js
                  Excludes:
                    - '**/README.md'
                    - '**/LICENSE'
                    - '**/CONTRIBUTING.md'
                Events:
                  - CLOSED
            SourceActionName: !Ref SourceActionName
      PipelineType: V2
      ExecutionMode: PARALLEL
      ArtifactStore:
        Type: S3
        Location: !Ref ArtifactStoreS3Location
```

### Pipeline with source stage and a stage configured for automatic rollback on failure
<a name="aws-resource-codepipeline-pipeline--examples--Pipeline_with_source_stage_and_a_stage_configured_for_automatic_rollback_on_failure"></a>

The following example creates a pipeline with a source stage and a release stage.

#### JSON
<a name="aws-resource-codepipeline-pipeline--examples--Pipeline_with_source_stage_and_a_stage_configured_for_automatic_rollback_on_failure--json"></a>

```
{
    "AppPipeline": {
        "Type": "AWS::CodePipeline::Pipeline",
        "Properties": {
            "RoleArn": {
                "Ref": "CodePipelineServiceRole"
            },
            "Stages": [
                {
                    "Name": "Source",
                    "Actions": [
                        {
                            "Name": "SourceAction",
                            "ActionTypeId": {
                                "Category": "Source",
                                "Owner": "AWS",
                                "Version": 1,
                                "Provider": "S3"
                            },
                            "OutputArtifacts": [
                                {
                                    "Name": "SourceOutput"
                                }
                            ],
                            "Configuration": {
                                "S3Bucket": {
                                    "Ref": "SourceS3Bucket"
                                },
                                "S3ObjectKey": {
                                    "Ref": "SourceS3ObjectKey"
                                }
                            },
                            "RunOrder": 1
                        }
                    ]
                },
                {
                    "Name": "Release",
                    "Actions": [
                        {
                            "Name": "ReleaseAction",
                            "InputArtifacts": [
                                {
                                    "Name": "SourceOutput"
                                }
                            ],
                            "ActionTypeId": {
                                "Category": "Deploy",
                                "Owner": "AWS",
                                "Version": 1,
                                "Provider": "CodeDeploy"
                            },
                            "Configuration": {
                                "ApplicationName": {
                                    "Ref": "ApplicationName"
                                },
                                "DeploymentGroupName": {
                                    "Ref": "DeploymentGroupName"
                                }
                            },
                            "RunOrder": 1
                        }
                    ],
                    "OnFailure": {
                        "Result": "ROLLBACK"
                    }
                }
            ],
            "ArtifactStore": {
                "Type": "S3",
                "Location": {
                    "Ref": "ArtifactStoreS3Location"
                },
                "EncryptionKey": {
                    "Id": "arn:aws:kms:useast-1:ACCOUNT-ID:key/KEY-ID",
                    "Type": "KMS"
                }
            },
            "DisableInboundStageTransitions": [
                {
                    "StageName": "Release",
                    "Reason": "Disabling the transition until integration tests are completed"
                }
            ],
            "Tags": [
                {
                    "Key": "Project",
                    "Value": "ProjectA"
                },
                {
                    "Key": "IsContainerBased",
                    "Value": "true"
                }
            ]
        }
    }
}
```

#### YAML
<a name="aws-resource-codepipeline-pipeline--examples--Pipeline_with_source_stage_and_a_stage_configured_for_automatic_rollback_on_failure--yaml"></a>

```
AppPipeline:
  Type: AWS::CodePipeline::Pipeline
  Properties:
    RoleArn:
      Ref: CodePipelineServiceRole
    Stages:
      -
        Name: Source
        Actions:
          -
            Name: SourceAction
            ActionTypeId:
              Category: Source
              Owner: AWS
              Version: 1
              Provider: S3
            OutputArtifacts:
              -
                Name: SourceOutput
            Configuration:
              S3Bucket:
                Ref: SourceS3Bucket
              S3ObjectKey:
                Ref: SourceS3ObjectKey
            RunOrder: 1
      -
        Name: Release
        Actions:
          -
            Name: ReleaseAction
            InputArtifacts:
              -
                Name: SourceOutput
            ActionTypeId:
              Category: Deploy
              Owner: AWS
              Version: 1
              Provider: CodeDeploy
            Configuration:
              ApplicationName:
                Ref: ApplicationName
              DeploymentGroupName:
                Ref: DeploymentGroupName
            RunOrder: 1
        OnFailure:
            Result: ROLLBACK
    ArtifactStore:
      Type: S3
      Location:
        Ref: ArtifactStoreS3Location
      EncryptionKey:
        Id: arn:aws:kms:useast-1:ACCOUNT-ID:key/KEY-ID
        Type: KMS
    DisableInboundStageTransitions:
      -
        StageName: Release
        Reason: "Disabling the transition until integration tests are completed"
    Tags:
      - Key: Project
        Value: ProjectA
      - Key: IsContainerBased
        Value: 'true'
```
