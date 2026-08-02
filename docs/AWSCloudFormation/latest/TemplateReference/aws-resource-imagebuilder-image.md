---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-imagebuilder-image.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::Image
<a name="aws-resource-imagebuilder-image"></a>

An image resource represents a versioned AMI or container image that Image Builder produces. Each image is built from a recipe, tested, and then distributed to the Regions and accounts that you specify.

Creates a new image in one of the following ways:
+ **From an image recipe** - Specify an `ImageRecipeArn` and an `InfrastructureConfigurationArn`. Image Builder launches an instance, applies your components, and creates an AMI.
+ **From a container recipe** - Specify a `ContainerRecipeArn` and an `InfrastructureConfigurationArn`. Image Builder builds a Docker container image and pushes it to your target repository.
+ **From a pipeline** - Specify `ImagePipelineExecutionSettings` with a `DeploymentId` that references an existing image pipeline. Image Builder runs the pipeline to create the image. The pipeline already defines the recipe and infrastructure configuration.

## Syntax
<a name="aws-resource-imagebuilder-image-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-imagebuilder-image-syntax.json"></a>

```
{
  "Type" : "AWS::ImageBuilder::Image",
  "Properties" : {
      "[ContainerRecipeArn](#cfn-imagebuilder-image-containerrecipearn)" : {{String}},
      "[DeletionSettings](#cfn-imagebuilder-image-deletionsettings)" : {{DeletionSettings}},
      "[DistributionConfigurationArn](#cfn-imagebuilder-image-distributionconfigurationarn)" : {{String}},
      "[EnhancedImageMetadataEnabled](#cfn-imagebuilder-image-enhancedimagemetadataenabled)" : {{Boolean}},
      "[ExecutionRole](#cfn-imagebuilder-image-executionrole)" : {{String}},
      "[ImagePipelineExecutionSettings](#cfn-imagebuilder-image-imagepipelineexecutionsettings)" : {{ImagePipelineExecutionSettings}},
      "[ImageRecipeArn](#cfn-imagebuilder-image-imagerecipearn)" : {{String}},
      "[ImageScanningConfiguration](#cfn-imagebuilder-image-imagescanningconfiguration)" : {{ImageScanningConfiguration}},
      "[ImageTestsConfiguration](#cfn-imagebuilder-image-imagetestsconfiguration)" : {{ImageTestsConfiguration}},
      "[InfrastructureConfigurationArn](#cfn-imagebuilder-image-infrastructureconfigurationarn)" : {{String}},
      "[LoggingConfiguration](#cfn-imagebuilder-image-loggingconfiguration)" : {{ImageLoggingConfiguration}},
      "[Tags](#cfn-imagebuilder-image-tags)" : {{{{{Key}}: {{Value}}, ...}}},
      "[Workflows](#cfn-imagebuilder-image-workflows)" : {{[ WorkflowConfiguration, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-imagebuilder-image-syntax.yaml"></a>

```
Type: AWS::ImageBuilder::Image
Properties:
  [ContainerRecipeArn](#cfn-imagebuilder-image-containerrecipearn): {{String}}
  [DeletionSettings](#cfn-imagebuilder-image-deletionsettings): {{
    DeletionSettings}}
  [DistributionConfigurationArn](#cfn-imagebuilder-image-distributionconfigurationarn): {{String}}
  [EnhancedImageMetadataEnabled](#cfn-imagebuilder-image-enhancedimagemetadataenabled): {{Boolean}}
  [ExecutionRole](#cfn-imagebuilder-image-executionrole): {{String}}
  [ImagePipelineExecutionSettings](#cfn-imagebuilder-image-imagepipelineexecutionsettings): {{
    ImagePipelineExecutionSettings}}
  [ImageRecipeArn](#cfn-imagebuilder-image-imagerecipearn): {{String}}
  [ImageScanningConfiguration](#cfn-imagebuilder-image-imagescanningconfiguration): {{
    ImageScanningConfiguration}}
  [ImageTestsConfiguration](#cfn-imagebuilder-image-imagetestsconfiguration): {{
    ImageTestsConfiguration}}
  [InfrastructureConfigurationArn](#cfn-imagebuilder-image-infrastructureconfigurationarn): {{String}}
  [LoggingConfiguration](#cfn-imagebuilder-image-loggingconfiguration): {{
    ImageLoggingConfiguration}}
  [Tags](#cfn-imagebuilder-image-tags): {{
    {{Key}}: {{Value}}}}
  [Workflows](#cfn-imagebuilder-image-workflows): {{
    - WorkflowConfiguration}}
```

## Properties
<a name="aws-resource-imagebuilder-image-properties"></a>

`ContainerRecipeArn`  <a name="cfn-imagebuilder-image-containerrecipearn"></a>
The Amazon Resource Name (ARN) of the container recipe that defines how images are configured and tested.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):container-recipe/[a-z0-9-_]+/(?:[0-9]+|x)\.(?:[0-9]+|x)\.(?:[0-9]+|x)$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DeletionSettings`  <a name="cfn-imagebuilder-image-deletionsettings"></a>
Enables deletion of underlying resources of an image when it is replaced or deleted, including its Amazon Machine Images (AMIs), snapshots, or containers.
*Required*: No
*Type*: [DeletionSettings](aws-properties-imagebuilder-image-deletionsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DistributionConfigurationArn`  <a name="cfn-imagebuilder-image-distributionconfigurationarn"></a>
The Amazon Resource Name (ARN) of the distribution configuration that defines and configures the outputs of your pipeline.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):distribution-configuration/[a-z0-9-_]+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EnhancedImageMetadataEnabled`  <a name="cfn-imagebuilder-image-enhancedimagemetadataenabled"></a>
Collects additional information about the image being created, including the operating system (OS) version and package list. This information is used to enhance the overall experience of using EC2 Image Builder. Enabled by default.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ExecutionRole`  <a name="cfn-imagebuilder-image-executionrole"></a>
The name or Amazon Resource Name (ARN) for the IAM role you create that grants Image Builder access to perform workflow actions.
*Required*: No
*Type*: String
*Pattern*: `^(?:arn:aws(?:-[a-z]+)*:iam::[0-9]{12}:role/)?[a-zA-Z_0-9+=,.@\-_/]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ImagePipelineExecutionSettings`  <a name="cfn-imagebuilder-image-imagepipelineexecutionsettings"></a>
The settings for creating the image by running an existing image pipeline, instead of building it from a recipe. When you specify these settings, do not specify recipe or infrastructure properties. The pipeline that you reference already defines them.
*Required*: No
*Type*: [ImagePipelineExecutionSettings](aws-properties-imagebuilder-image-imagepipelineexecutionsettings.md)
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`ImageRecipeArn`  <a name="cfn-imagebuilder-image-imagerecipearn"></a>
The Amazon Resource Name (ARN) of the image recipe that defines how images are configured, tested, and assessed.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):image-recipe/[a-z0-9-_]+/(?:[0-9]+|x)\.(?:[0-9]+|x)\.(?:[0-9]+|x)$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ImageScanningConfiguration`  <a name="cfn-imagebuilder-image-imagescanningconfiguration"></a>
Contains settings for vulnerability scans.
*Required*: No
*Type*: [ImageScanningConfiguration](aws-properties-imagebuilder-image-imagescanningconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ImageTestsConfiguration`  <a name="cfn-imagebuilder-image-imagetestsconfiguration"></a>
The image tests configuration of the image.
*Required*: No
*Type*: [ImageTestsConfiguration](aws-properties-imagebuilder-image-imagetestsconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InfrastructureConfigurationArn`  <a name="cfn-imagebuilder-image-infrastructureconfigurationarn"></a>
The Amazon Resource Name (ARN) of the infrastructure configuration that defines the environment in which your image will be built and tested.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):infrastructure-configuration/[a-z0-9-_]+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LoggingConfiguration`  <a name="cfn-imagebuilder-image-loggingconfiguration"></a>
The logging configuration that's defined for the image. Image Builder uses the defined settings to direct execution log output during image creation.
*Required*: No
*Type*: [ImageLoggingConfiguration](aws-properties-imagebuilder-image-imageloggingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-imagebuilder-image-tags"></a>
The tags of the image.
*Required*: No
*Type*: Object of String
*Pattern*: `.{1,}`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Workflows`  <a name="cfn-imagebuilder-image-workflows"></a>
Contains an array of workflow configuration objects.
*Required*: No
*Type*: Array of [WorkflowConfiguration](aws-properties-imagebuilder-image-workflowconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-imagebuilder-image-return-values"></a>

### Ref
<a name="aws-resource-imagebuilder-image-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource ARN, such as `arn:aws:imagebuilder:us-west-2:111122223333:image/my-example-image`.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-imagebuilder-image-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-imagebuilder-image-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Returns the Amazon Resource Name (ARN) of the image. For example, `arn:aws:imagebuilder:us-west-2:111122223333:image/mybasicrecipe/2019.12.03/1`.

`ImageId`  <a name="ImageId-fn::getatt"></a>
Returns the AMI ID of the Amazon EC2 AMI in the Region in which you are using Image Builder. Values are returned only for AMIs, and not for container images.

`ImageUri`  <a name="ImageUri-fn::getatt"></a>
Returns the URI for a container image created in the context Region. Values are returned only for container images, and not for AMIs.

`LatestVersion.Arn`  <a name="LatestVersion.Arn-fn::getatt"></a>
The latest version Amazon Resource Name (ARN) of the Image Builder resource.

`LatestVersion.Major`  <a name="LatestVersion.Major-fn::getatt"></a>
The latest version Amazon Resource Name (ARN) with the same `major` version of the Image Builder resource.

`LatestVersion.Minor`  <a name="LatestVersion.Minor-fn::getatt"></a>
The latest version Amazon Resource Name (ARN) with the same `minor` version of the Image Builder resource.

`LatestVersion.Patch`  <a name="LatestVersion.Patch-fn::getatt"></a>
The latest version Amazon Resource Name (ARN) with the same `patch` version of the Image Builder resource.

`Name`  <a name="Name-fn::getatt"></a>
Returns the name of the image.

## Examples
<a name="aws-resource-imagebuilder-image--examples"></a>

**Topics**
+ [Create an image](#aws-resource-imagebuilder-image--examples--Create_an_image)
+ [Create a pipeline-driven image](#aws-resource-imagebuilder-image--examples--Create_a_pipeline-driven_image)

### Create an image
<a name="aws-resource-imagebuilder-image--examples--Create_an_image"></a>

The following example shows the template for the Image resource in both YAML and JSON format.

#### YAML
<a name="aws-resource-imagebuilder-image--examples--Create_an_image--yaml"></a>

```
Resources:
  ImageAllParameters:
    Type: 'AWS::ImageBuilder::Image'
    Properties:
      ImageRecipeArn: !Ref ImageRecipeArn
      InfrastructureConfigurationArn: !Ref InfrastructureConfigurationArn
      DistributionConfigurationArn: !Ref DistributionConfigurationArn
      ImageTestsConfiguration:
        ImageTestsEnabled: false
        TimeoutMinutes: 60
      Tags:
        CustomerImageTagKey1: 'CustomerImageTagValue1'
        CustomerImageTagKey2: 'CustomerImageTagValue2'
```

#### JSON
<a name="aws-resource-imagebuilder-image--examples--Create_an_image--json"></a>

```
{
    "Resources": {
        "ImageAllParameters": {
            "Type": "AWS::ImageBuilder::Image",
            "Properties": {
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
                    "TimeoutMinutes": 60
                },
                "Tags": {
                    "CustomerImageTagKey1": "CustomerImageTagValue1",
                    "CustomerImageTagKey2": "CustomerImageTagValue2"
                }
            }
        }
    }
}
```

### Create a pipeline-driven image
<a name="aws-resource-imagebuilder-image--examples--Create_a_pipeline-driven_image"></a>

The following example creates an image by running an existing image pipeline. When the pipeline configuration changes, updating the stack triggers a new pipeline execution. This mode does not require a recipe or infrastructure configuration because the referenced pipeline defines them.

#### YAML
<a name="aws-resource-imagebuilder-image--examples--Create_a_pipeline-driven_image--yaml"></a>

```
Resources:
  PipelineDrivenImage:
    Type: AWS::ImageBuilder::Image
    Properties:
      ImagePipelineExecutionSettings:
        DeploymentId: !GetAtt MyImagePipeline.DeploymentId
        OnUpdate: true
      Tags:
        Environment: production
```

#### JSON
<a name="aws-resource-imagebuilder-image--examples--Create_a_pipeline-driven_image--json"></a>

```
{
    "Resources": {
        "PipelineDrivenImage": {
            "Type": "AWS::ImageBuilder::Image",
            "Properties": {
                "ImagePipelineExecutionSettings": {
                    "DeploymentId": {
                        "Fn::GetAtt": ["MyImagePipeline", "DeploymentId"]
                    },
                    "OnUpdate": true
                },
                "Tags": {
                    "Environment": "production"
                }
            }
        }
    }
}
```

## See also
<a name="aws-resource-imagebuilder-image--seealso"></a>
+ [Manage images](https://docs.aws.amazon.com/imagebuilder/latest/userguide/manage-images.html) in the *Image Builder User Guide*.
