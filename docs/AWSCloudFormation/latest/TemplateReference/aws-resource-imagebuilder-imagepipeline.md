---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-imagebuilder-imagepipeline.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::ImagePipeline
<a name="aws-resource-imagebuilder-imagepipeline"></a>

An image pipeline is the automation configuration for building secure OS images on AWS. The Image Builder image pipeline is associated with an image recipe that defines the build, validation, and test phases for an image build lifecycle. An image pipeline can be associated with an infrastructure configuration that defines where your image is built. You can define attributes, such as instance types, a subnet for your VPC, security groups, logging, and other infrastructure-related configurations. You can also associate your image pipeline with a distribution configuration to define how you would like to deploy your image.

## Syntax
<a name="aws-resource-imagebuilder-imagepipeline-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-imagebuilder-imagepipeline-syntax.json"></a>

```
{
  "Type" : "AWS::ImageBuilder::ImagePipeline",
  "Properties" : {
      "[ContainerRecipeArn](#cfn-imagebuilder-imagepipeline-containerrecipearn)" : {{String}},
      "[Description](#cfn-imagebuilder-imagepipeline-description)" : {{String}},
      "[DistributionConfigurationArn](#cfn-imagebuilder-imagepipeline-distributionconfigurationarn)" : {{String}},
      "[EnhancedImageMetadataEnabled](#cfn-imagebuilder-imagepipeline-enhancedimagemetadataenabled)" : {{Boolean}},
      "[ExecutionRole](#cfn-imagebuilder-imagepipeline-executionrole)" : {{String}},
      "[ImageRecipeArn](#cfn-imagebuilder-imagepipeline-imagerecipearn)" : {{String}},
      "[ImageScanningConfiguration](#cfn-imagebuilder-imagepipeline-imagescanningconfiguration)" : {{ImageScanningConfiguration}},
      "[ImageTags](#cfn-imagebuilder-imagepipeline-imagetags)" : {{{{{Key}}: {{Value}}, ...}}},
      "[ImageTestsConfiguration](#cfn-imagebuilder-imagepipeline-imagetestsconfiguration)" : {{ImageTestsConfiguration}},
      "[InfrastructureConfigurationArn](#cfn-imagebuilder-imagepipeline-infrastructureconfigurationarn)" : {{String}},
      "[LoggingConfiguration](#cfn-imagebuilder-imagepipeline-loggingconfiguration)" : {{PipelineLoggingConfiguration}},
      "[Name](#cfn-imagebuilder-imagepipeline-name)" : {{String}},
      "[Schedule](#cfn-imagebuilder-imagepipeline-schedule)" : {{Schedule}},
      "[Status](#cfn-imagebuilder-imagepipeline-status)" : {{String}},
      "[Tags](#cfn-imagebuilder-imagepipeline-tags)" : {{{{{Key}}: {{Value}}, ...}}},
      "[Workflows](#cfn-imagebuilder-imagepipeline-workflows)" : {{[ WorkflowConfiguration, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-imagebuilder-imagepipeline-syntax.yaml"></a>

```
Type: AWS::ImageBuilder::ImagePipeline
Properties:
  [ContainerRecipeArn](#cfn-imagebuilder-imagepipeline-containerrecipearn): {{String}}
  [Description](#cfn-imagebuilder-imagepipeline-description): {{String}}
  [DistributionConfigurationArn](#cfn-imagebuilder-imagepipeline-distributionconfigurationarn): {{String}}
  [EnhancedImageMetadataEnabled](#cfn-imagebuilder-imagepipeline-enhancedimagemetadataenabled): {{Boolean}}
  [ExecutionRole](#cfn-imagebuilder-imagepipeline-executionrole): {{String}}
  [ImageRecipeArn](#cfn-imagebuilder-imagepipeline-imagerecipearn): {{String}}
  [ImageScanningConfiguration](#cfn-imagebuilder-imagepipeline-imagescanningconfiguration): {{
    ImageScanningConfiguration}}
  [ImageTags](#cfn-imagebuilder-imagepipeline-imagetags): {{
    {{Key}}: {{Value}}}}
  [ImageTestsConfiguration](#cfn-imagebuilder-imagepipeline-imagetestsconfiguration): {{
    ImageTestsConfiguration}}
  [InfrastructureConfigurationArn](#cfn-imagebuilder-imagepipeline-infrastructureconfigurationarn): {{String}}
  [LoggingConfiguration](#cfn-imagebuilder-imagepipeline-loggingconfiguration): {{
    PipelineLoggingConfiguration}}
  [Name](#cfn-imagebuilder-imagepipeline-name): {{String}}
  [Schedule](#cfn-imagebuilder-imagepipeline-schedule): {{
    Schedule}}
  [Status](#cfn-imagebuilder-imagepipeline-status): {{String}}
  [Tags](#cfn-imagebuilder-imagepipeline-tags): {{
    {{Key}}: {{Value}}}}
  [Workflows](#cfn-imagebuilder-imagepipeline-workflows): {{
    - WorkflowConfiguration}}
```

## Properties
<a name="aws-resource-imagebuilder-imagepipeline-properties"></a>

`ContainerRecipeArn`  <a name="cfn-imagebuilder-imagepipeline-containerrecipearn"></a>
The Amazon Resource Name (ARN) of the container recipe that is used for this pipeline.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-imagebuilder-imagepipeline-description"></a>
The description of the image pipeline.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DistributionConfigurationArn`  <a name="cfn-imagebuilder-imagepipeline-distributionconfigurationarn"></a>
The Amazon Resource Name (ARN) of the distribution configuration associated with this image pipeline.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnhancedImageMetadataEnabled`  <a name="cfn-imagebuilder-imagepipeline-enhancedimagemetadataenabled"></a>
Collects additional information about the image being created, including the operating system (OS) version and package list. This information is used to enhance the overall experience of using EC2 Image Builder. Enabled by default.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExecutionRole`  <a name="cfn-imagebuilder-imagepipeline-executionrole"></a>
The name or Amazon Resource Name (ARN) for the IAM role you create that grants Image Builder access to perform workflow actions.
*Required*: No
*Type*: String
*Pattern*: `^(?:arn:aws(?:-[a-z]+)*:iam::[0-9]{12}:role/)?[a-zA-Z_0-9+=,.@\-_/]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ImageRecipeArn`  <a name="cfn-imagebuilder-imagepipeline-imagerecipearn"></a>
The Amazon Resource Name (ARN) of the image recipe associated with this image pipeline.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ImageScanningConfiguration`  <a name="cfn-imagebuilder-imagepipeline-imagescanningconfiguration"></a>
Contains settings for vulnerability scans.
*Required*: No
*Type*: [ImageScanningConfiguration](aws-properties-imagebuilder-imagepipeline-imagescanningconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ImageTags`  <a name="cfn-imagebuilder-imagepipeline-imagetags"></a>
The tags to apply to every image that this pipeline produces. Unlike the `Tags` property, which tags the pipeline resource itself, `ImageTags` tag each image version that the pipeline creates. These tags appear on the resulting AMI or container image. To tag the AMI during the Build phase before distribution, use the `AmiTags` property on the image recipe instead.
*Required*: No
*Type*: Object of String
*Pattern*: `.{1,}`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ImageTestsConfiguration`  <a name="cfn-imagebuilder-imagepipeline-imagetestsconfiguration"></a>
The image tests configuration of the image pipeline.
*Required*: No
*Type*: [ImageTestsConfiguration](aws-properties-imagebuilder-imagepipeline-imagetestsconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InfrastructureConfigurationArn`  <a name="cfn-imagebuilder-imagepipeline-infrastructureconfigurationarn"></a>
The Amazon Resource Name (ARN) of the infrastructure configuration associated with this image pipeline.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LoggingConfiguration`  <a name="cfn-imagebuilder-imagepipeline-loggingconfiguration"></a>
Defines logging configuration for the output image.
*Required*: No
*Type*: [PipelineLoggingConfiguration](aws-properties-imagebuilder-imagepipeline-pipelineloggingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-imagebuilder-imagepipeline-name"></a>
The name of the image pipeline.
*Required*: No
*Type*: String
*Pattern*: `^[-_A-Za-z-0-9][-_A-Za-z0-9 ]{1,126}[-_A-Za-z-0-9]$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Schedule`  <a name="cfn-imagebuilder-imagepipeline-schedule"></a>
The schedule of the image pipeline.
*Required*: No
*Type*: [Schedule](aws-properties-imagebuilder-imagepipeline-schedule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-imagebuilder-imagepipeline-status"></a>
The status of the image pipeline.
*Required*: No
*Type*: String
*Allowed values*: `DISABLED | ENABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-imagebuilder-imagepipeline-tags"></a>
The tags of this image pipeline.
*Required*: No
*Type*: Object of String
*Pattern*: `.{1,}`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Workflows`  <a name="cfn-imagebuilder-imagepipeline-workflows"></a>
Contains the workflows that run for the image pipeline.
*Required*: No
*Type*: Array of [WorkflowConfiguration](aws-properties-imagebuilder-imagepipeline-workflowconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-imagebuilder-imagepipeline-return-values"></a>

### Ref
<a name="aws-resource-imagebuilder-imagepipeline-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource ARN, such as `arn:aws:imagebuilder:us-west-2:111122223333:image-pipeline/mywindows2016pipeline`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-imagebuilder-imagepipeline-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-imagebuilder-imagepipeline-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Returns the Amazon Resource Name (ARN) of the image pipeline. For example, `arn:aws:imagebuilder:us-west-2:111122223333:image-pipeline/mywindows2016pipeline`.

`DeploymentId`  <a name="DeploymentId-fn::getatt"></a>
Returns the deployment ID of the pipeline. The deployment ID changes each time the pipeline configuration changes. Use this attribute to set the `ImagePipelineExecutionSettings.DeploymentId` property of an `AWS::ImageBuilder::Image` resource, so that the pipeline runs when your template creates or updates the image resource.

`Name`  <a name="Name-fn::getatt"></a>
Returns the name of the image pipeline.

## Examples
<a name="aws-resource-imagebuilder-imagepipeline--examples"></a>

**Topics**
+ [Create an image pipeline](#aws-resource-imagebuilder-imagepipeline--examples--Create_an_image_pipeline)
+ [Create an image pipeline with workflows and logging](#aws-resource-imagebuilder-imagepipeline--examples--Create_an_image_pipeline_with_workflows_and_logging)

### Create an image pipeline
<a name="aws-resource-imagebuilder-imagepipeline--examples--Create_an_image_pipeline"></a>

The following example shows the template for the ImagePipeline resource in both YAML and JSON format.

#### YAML
<a name="aws-resource-imagebuilder-imagepipeline--examples--Create_an_image_pipeline--yaml"></a>

```
Resources:
  ImagePipelineAllParameters:
    Type: 'AWS::ImageBuilder::ImagePipeline'
    Properties:
      Name: 'image-pipeline-name'
      Description: 'description'
      ImageRecipeArn: !Ref ImageRecipeArn
      InfrastructureConfigurationArn: !Ref InfrastructureConfigurationArn
      DistributionConfigurationArn: !Ref DistributionConfigurationArn
      ImageTestsConfiguration:
        ImageTestsEnabled: false
        TimeoutMinutes: 90
      Schedule:
        ScheduleExpression: 'cron(0 0 * * ? *)'
        PipelineExecutionStartCondition: 'EXPRESSION_MATCH_ONLY'
      Status: 'DISABLED'
      Tags:
        CustomerImagePipelineTagKey1: 'CustomerImagePipelineTagValue1'
        CustomerImagePipelineTagKey2: 'CustomerImagePipelineTagValue2'
```

#### JSON
<a name="aws-resource-imagebuilder-imagepipeline--examples--Create_an_image_pipeline--json"></a>

```
{
    "Resources": {
        "ImagePipelineAllParameters": {
            "Type": "AWS::ImageBuilder::ImagePipeline",
            "Properties": {
                "Name": "image-pipeline-name",
                "Description": "description",
                "ImageRecipeArn": {
                    "Ref": "ImageRecipeArn"
                },
                "InfrastructureConfigurationArn": {
                    "Ref": "InfrastructureConfigurationArn"
                },
                "DistributionConfigurationArn": {
                    "Ref": "DistributionConfigurationArn"
                },
                "ImageTestsConfiguration": {
                    "ImageTestsEnabled": false,
                    "TimeoutMinutes": 90
                },
                "Schedule": {
                "ScheduleExpression": "cron(0 0 * * ? *)",
                    "PipelineExecutionStartCondition": "EXPRESSION_MATCH_ONLY"
                },
                "Status": "DISABLED",
                "Tags": {
                    "CustomerImagePipelineTagKey1": "CustomerImagePipelineTagValue1",
                    "CustomerImagePipelineTagKey2": "CustomerImagePipelineTagValue2"
                }
            }
        }
    }
}
```

### Create an image pipeline with workflows and logging
<a name="aws-resource-imagebuilder-imagepipeline--examples--Create_an_image_pipeline_with_workflows_and_logging"></a>

The following example creates an image pipeline that uses a custom workflow, writes logs to a custom Amazon CloudWatch Logs log group, and applies tags to the images it produces.

#### YAML
<a name="aws-resource-imagebuilder-imagepipeline--examples--Create_an_image_pipeline_with_workflows_and_logging--yaml"></a>

```
Resources:
  PipelineWithWorkflows:
    Type: AWS::ImageBuilder::ImagePipeline
    Properties:
      Name: pipeline-with-workflows
      ImageRecipeArn: !Ref ImageRecipeArn
      InfrastructureConfigurationArn: !Ref InfrastructureConfigurationArn
      DistributionConfigurationArn: !Ref DistributionConfigurationArn
      ExecutionRole: !GetAtt PipelineExecutionRole.Arn
      Workflows:
        - WorkflowArn: !GetAtt BuildWorkflow.Arn
          OnFailure: ABORT
        - WorkflowArn: !GetAtt TestWorkflow.Arn
          OnFailure: CONTINUE
          ParallelGroup: test-group
      LoggingConfiguration:
        PipelineLogGroupName: /mycompany/imagebuilder/pipelines
        ImageLogGroupName: /mycompany/imagebuilder/images
      ImageTags:
        Application: web-server
        BuildDate: '{{ imagebuilder:buildDate }}'
      Schedule:
        ScheduleExpression: 'cron(0 8 ? * mon *)'
        PipelineExecutionStartCondition: EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE
      Status: ENABLED
```

#### JSON
<a name="aws-resource-imagebuilder-imagepipeline--examples--Create_an_image_pipeline_with_workflows_and_logging--json"></a>

```
{
    "Resources": {
        "PipelineWithWorkflows": {
            "Type": "AWS::ImageBuilder::ImagePipeline",
            "Properties": {
                "Name": "pipeline-with-workflows",
                "ImageRecipeArn": {
                    "Ref": "ImageRecipeArn"
                },
                "InfrastructureConfigurationArn": {
                    "Ref": "InfrastructureConfigurationArn"
                },
                "DistributionConfigurationArn": {
                    "Ref": "DistributionConfigurationArn"
                },
                "ExecutionRole": {
                    "Fn::GetAtt": ["PipelineExecutionRole", "Arn"]
                },
                "Workflows": [
                    {
                        "WorkflowArn": {
                            "Fn::GetAtt": ["BuildWorkflow", "Arn"]
                        },
                        "OnFailure": "ABORT"
                    },
                    {
                        "WorkflowArn": {
                            "Fn::GetAtt": ["TestWorkflow", "Arn"]
                        },
                        "OnFailure": "CONTINUE",
                        "ParallelGroup": "test-group"
                    }
                ],
                "LoggingConfiguration": {
                    "PipelineLogGroupName": "/mycompany/imagebuilder/pipelines",
                    "ImageLogGroupName": "/mycompany/imagebuilder/images"
                },
                "ImageTags": {
                    "Application": "web-server",
                    "BuildDate": "{{ imagebuilder:buildDate }}"
                },
                "Schedule": {
                    "ScheduleExpression": "cron(0 8 ? * mon *)",
                    "PipelineExecutionStartCondition": "EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE"
                },
                "Status": "ENABLED"
            }
        }
    }
}
```
