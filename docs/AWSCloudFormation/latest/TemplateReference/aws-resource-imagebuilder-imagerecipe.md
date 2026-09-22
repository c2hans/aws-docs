---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-imagebuilder-imagerecipe.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::ImageRecipe
<a name="aws-resource-imagebuilder-imagerecipe"></a>

Creates a new image recipe. Image recipes define how images are configured, tested, and assessed.

## Syntax
<a name="aws-resource-imagebuilder-imagerecipe-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-imagebuilder-imagerecipe-syntax.json"></a>

```
{
  "Type" : "AWS::ImageBuilder::ImageRecipe",
  "Properties" : {
      "[AdditionalInstanceConfiguration](#cfn-imagebuilder-imagerecipe-additionalinstanceconfiguration)" : {{AdditionalInstanceConfiguration}},
      "[AmiTags](#cfn-imagebuilder-imagerecipe-amitags)" : {{{{{Key}}: {{Value}}, ...}}},
      "[AmiWatermarks](#cfn-imagebuilder-imagerecipe-amiwatermarks)" : {{[ String, ... ]}},
      "[BlockDeviceMappings](#cfn-imagebuilder-imagerecipe-blockdevicemappings)" : {{[ InstanceBlockDeviceMapping, ... ]}},
      "[Components](#cfn-imagebuilder-imagerecipe-components)" : {{[ ComponentConfiguration, ... ]}},
      "[Description](#cfn-imagebuilder-imagerecipe-description)" : {{String}},
      "[Name](#cfn-imagebuilder-imagerecipe-name)" : {{String}},
      "[ParentImage](#cfn-imagebuilder-imagerecipe-parentimage)" : {{String}},
      "[Tags](#cfn-imagebuilder-imagerecipe-tags)" : {{{{{Key}}: {{Value}}, ...}}},
      "[Version](#cfn-imagebuilder-imagerecipe-version)" : {{String}},
      "[WorkingDirectory](#cfn-imagebuilder-imagerecipe-workingdirectory)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-imagebuilder-imagerecipe-syntax.yaml"></a>

```
Type: AWS::ImageBuilder::ImageRecipe
Properties:
  [AdditionalInstanceConfiguration](#cfn-imagebuilder-imagerecipe-additionalinstanceconfiguration): {{
    AdditionalInstanceConfiguration}}
  [AmiTags](#cfn-imagebuilder-imagerecipe-amitags): {{
    {{Key}}: {{Value}}}}
  [AmiWatermarks](#cfn-imagebuilder-imagerecipe-amiwatermarks): {{
    - String}}
  [BlockDeviceMappings](#cfn-imagebuilder-imagerecipe-blockdevicemappings): {{
    - InstanceBlockDeviceMapping}}
  [Components](#cfn-imagebuilder-imagerecipe-components): {{
    - ComponentConfiguration}}
  [Description](#cfn-imagebuilder-imagerecipe-description): {{String}}
  [Name](#cfn-imagebuilder-imagerecipe-name): {{String}}
  [ParentImage](#cfn-imagebuilder-imagerecipe-parentimage): {{String}}
  [Tags](#cfn-imagebuilder-imagerecipe-tags): {{
    {{Key}}: {{Value}}}}
  [Version](#cfn-imagebuilder-imagerecipe-version): {{String}}
  [WorkingDirectory](#cfn-imagebuilder-imagerecipe-workingdirectory): {{String}}
```

## Properties
<a name="aws-resource-imagebuilder-imagerecipe-properties"></a>

`AdditionalInstanceConfiguration`  <a name="cfn-imagebuilder-imagerecipe-additionalinstanceconfiguration"></a>
The additional settings and launch scripts for your build instances.
*Required*: No
*Type*: [AdditionalInstanceConfiguration](aws-properties-imagebuilder-imagerecipe-additionalinstanceconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AmiTags`  <a name="cfn-imagebuilder-imagerecipe-amitags"></a>
Tags that are applied to the AMI that Image Builder creates during the Build phase prior to image distribution.
*Required*: No
*Type*: Object of String
*Pattern*: `.{1,}`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AmiWatermarks`  <a name="cfn-imagebuilder-imagerecipe-amiwatermarks"></a>
The AMI watermark names to attach to the output AMI from this recipe. AMI watermarks are lineage markers. They automatically propagate to derivative AMIs when the source AMI is copied or distributed across Regions or accounts.
AMI watermarks are supported only for image recipes. AMIs with watermarks cannot be made public.
*Required*: No
*Type*: Array of String
*Minimum*: `3 | 1`
*Maximum*: `128 | 5`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`BlockDeviceMappings`  <a name="cfn-imagebuilder-imagerecipe-blockdevicemappings"></a>
The block device mappings that Image Builder applies to the build instance and the output AMI. For example, you can override the size of the base image's root volume or attach additional EBS volumes.
*Required*: No
*Type*: Array of [InstanceBlockDeviceMapping](aws-properties-imagebuilder-imagerecipe-instanceblockdevicemapping.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Components`  <a name="cfn-imagebuilder-imagerecipe-components"></a>
The components included in the image recipe. Components are optional. A recipe with no components bakes the base image without additional customization. You can specify each component only one time in a recipe. Components with a status of `DEPRECATED` or `DISABLED` can't be added to new recipes.
*Required*: No
*Type*: Array of [ComponentConfiguration](aws-properties-imagebuilder-imagerecipe-componentconfiguration.md)
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-imagebuilder-imagerecipe-description"></a>
The description of the image recipe.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-imagebuilder-imagerecipe-name"></a>
The name of the image recipe. The recipe name, combined with the semantic version, must be unique to your account in each AWS Region. Image Builder generates the image recipe ARN from a normalized form of the name, so names that differ only in case, spaces, or underscores count as the same name.
*Required*: Yes
*Type*: String
*Pattern*: `^[-_A-Za-z-0-9][-_A-Za-z0-9 ]{1,126}[-_A-Za-z-0-9]$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ParentImage`  <a name="cfn-imagebuilder-imagerecipe-parentimage"></a>
The base image for customizations specified in the image recipe. You can specify the parent image using one of the following options:
+ AMI ID
+ Image Builder image Amazon Resource Name (ARN)
+ AWS Systems Manager (SSM) Parameter Store Parameter, prefixed by `ssm:`, followed by the parameter name or ARN.
+ AWS Marketplace product ID
If you enter an AMI ID or an SSM parameter that contains the AMI ID, you must have access to the AMI. The AMI must also be in the Region where you're creating the recipe.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-imagebuilder-imagerecipe-tags"></a>
The tags of the image recipe.
*Required*: No
*Type*: Object of String
*Pattern*: `.{1,}`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Version`  <a name="cfn-imagebuilder-imagerecipe-version"></a>
The semantic version of the image recipe. This version follows the semantic version syntax.
The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.
**Assignment:** For the first three nodes, you can assign any positive integer value, including zero. The upper limit is 2^30-1, or 1073741823, for each node. Image Builder automatically assigns the build number to the fourth node.
**Patterns:** You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01.
*Required*: Yes
*Type*: String
*Pattern*: `^(?:[0-9]+|x)\.(?:[0-9]+|x)\.(?:[0-9]+|x)$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`WorkingDirectory`  <a name="cfn-imagebuilder-imagerecipe-workingdirectory"></a>
The working directory used during build and test workflows. If you don't specify a working directory, Image Builder uses `/tmp` for Linux and macOS build instances, and `C:/` for Windows build instances.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-imagebuilder-imagerecipe-return-values"></a>

### Ref
<a name="aws-resource-imagebuilder-imagerecipe-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource ARN, such as `arn:aws:imagebuilder:us-east-1:111122223333:image-recipe/mybasicrecipe/2019.12.03`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-imagebuilder-imagerecipe-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-imagebuilder-imagerecipe-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Returns the Amazon Resource Name (ARN) of the image recipe. For example, `arn:aws:imagebuilder:us-east-1:111122223333:image-recipe/mybasicrecipe/2019.12.03`.

`LatestVersion.Arn`  <a name="LatestVersion.Arn-fn::getatt"></a>
The latest version Amazon Resource Name (ARN) of the Image Builder resource.

`LatestVersion.Major`  <a name="LatestVersion.Major-fn::getatt"></a>
The latest version Amazon Resource Name (ARN) with the same `major` version of the Image Builder resource.

`LatestVersion.Minor`  <a name="LatestVersion.Minor-fn::getatt"></a>
The latest version Amazon Resource Name (ARN) with the same `minor` version of the Image Builder resource.

`LatestVersion.Patch`  <a name="LatestVersion.Patch-fn::getatt"></a>
The latest version Amazon Resource Name (ARN) with the same `patch` version of the Image Builder resource.

`Name`  <a name="Name-fn::getatt"></a>
The name of the image recipe.

## Examples
<a name="aws-resource-imagebuilder-imagerecipe--examples"></a>

**Topics**
+ [Create an image recipe](#aws-resource-imagebuilder-imagerecipe--examples--Create_an_image_recipe)
+ [Create an image recipe with AMI tags and watermarks](#aws-resource-imagebuilder-imagerecipe--examples--Create_an_image_recipe_with_AMI_tags_and_watermarks)

### Create an image recipe
<a name="aws-resource-imagebuilder-imagerecipe--examples--Create_an_image_recipe"></a>

The following example shows the template for the ImageRecipe resource in both YAML and JSON format.

#### YAML
<a name="aws-resource-imagebuilder-imagerecipe--examples--Create_an_image_recipe--yaml"></a>

```
Resources:
  ImageRecipeAllParameters:
    Type: 'AWS::ImageBuilder::ImageRecipe'
    Properties:
      Name: 'image-recipe-name'
      Version: '1.0.0'
      ParentImage: !Ref ParentImage
      Description: 'description'
      Components:
        - ComponentArn: !Ref ComponentArn
        - ComponentArn: !Ref AnotherComponentArn
      BlockDeviceMappings:
        - DeviceName: "device-name"
          VirtualName: "virtual-name"
          Ebs:
            DeleteOnTermination: true
            Encrypted: true
            Iops: 100
            KmsKeyId: !Ref KmsKeyId
            SnapshotId: "snapshot-id"
            VolumeType: "gp2"
            VolumeSize: 100
      Tags:
        CustomerImageRecipeTagKey1: 'CustomerImageRecipeTagValue1'
        CustomerImageRecipeTagKey2: 'CustomerImageRecipeTagValue2'
```

#### JSON
<a name="aws-resource-imagebuilder-imagerecipe--examples--Create_an_image_recipe--json"></a>

```
{
    "Resources": {
        "ImageRecipeAllParameters": {
            "Type": "AWS::ImageBuilder::ImageRecipe",
            "Properties": {
                "Name": "image-recipe-name",
                "Version": "1.0.0",
                "ParentImage": {
                    "Ref": "ParentImage"
                },
                "Description": "description",
                "Components": [
                    {
                        "ComponentArn": {
                            "Ref": "ComponentArn"
                        }
                    },
                    {
                        "ComponentArn": {
                            "Ref": "AnotherComponentArn"
                        }
                    }
                ],
                "BlockDeviceMappings": [
                    {
                        "DeviceName": "device-name",
                        "VirtualName": "virtual-name",
                        "Ebs": {
                            "DeleteOnTermination": true,
                            "Encrypted": true,
                            "Iops": 100,
                            "KmsKeyId": {
                                "Ref": "KmsKeyId"
                            },
                            "SnapshotId": "snapshot-id",
                            "VolumeType": "gp2",
                            "VolumeSize": 100
                        }
                    }
                ],
                "Tags": {
                    "CustomerImageRecipeTagKey1": "CustomerImageRecipeTagValue1",
                    "CustomerImageRecipeTagKey2": "CustomerImageRecipeTagValue2"
                }
            }
        }
    }
}
```

### Create an image recipe with AMI tags and watermarks
<a name="aws-resource-imagebuilder-imagerecipe--examples--Create_an_image_recipe_with_AMI_tags_and_watermarks"></a>

The following example creates an image recipe that applies tags and watermarks to the output AMI, and provides a custom user data script for the build instance.

#### YAML
<a name="aws-resource-imagebuilder-imagerecipe--examples--Create_an_image_recipe_with_AMI_tags_and_watermarks--yaml"></a>

```
Resources:
  RecipeWithExtras:
    Type: AWS::ImageBuilder::ImageRecipe
    Properties:
      Name: recipe-with-extras
      Version: '1.0.0'
      ParentImage: !Ref LatestAmazonLinux2Ami
      Components:
        - ComponentArn: !GetAtt HardeningComponent.Arn
      AmiTags:
        CostCenter: '12345'
        PatchLevel: latest
      AmiWatermarks:
        - production-approved
        - security-hardened
      AdditionalInstanceConfiguration:
        SystemsManagerAgent:
          UninstallAfterBuild: true
        UserDataOverride: !Base64 |
          #!/bin/bash
          yum update -y
      WorkingDirectory: /tmp
      Tags:
        Team: platform
```

#### JSON
<a name="aws-resource-imagebuilder-imagerecipe--examples--Create_an_image_recipe_with_AMI_tags_and_watermarks--json"></a>

```
{
    "Resources": {
        "RecipeWithExtras": {
            "Type": "AWS::ImageBuilder::ImageRecipe",
            "Properties": {
                "Name": "recipe-with-extras",
                "Version": "1.0.0",
                "ParentImage": {
                    "Ref": "LatestAmazonLinux2Ami"
                },
                "Components": [
                    {
                        "ComponentArn": {
                            "Fn::GetAtt": ["HardeningComponent", "Arn"]
                        }
                    }
                ],
                "AmiTags": {
                    "CostCenter": "12345",
                    "PatchLevel": "latest"
                },
                "AmiWatermarks": [
                    "production-approved",
                    "security-hardened"
                ],
                "AdditionalInstanceConfiguration": {
                    "SystemsManagerAgent": {
                        "UninstallAfterBuild": true
                    },
                    "UserDataOverride": {
                        "Fn::Base64": "#!/bin/bash\nyum update -y\n"
                    }
                },
                "WorkingDirectory": "/tmp",
                "Tags": {
                    "Team": "platform"
                }
            }
        }
    }
}
```

## See also
<a name="aws-resource-imagebuilder-imagerecipe--seealso"></a>
+ [Create an image recipe](https://docs.aws.amazon.com/imagebuilder/latest/userguide/create-image-recipes.html) in the *Image Builder User Guide*.
