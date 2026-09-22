---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-imagebuilder-containerrecipe.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::ContainerRecipe
<a name="aws-resource-imagebuilder-containerrecipe"></a>

Creates a new container recipe. Container recipes define how images are configured, tested, and assessed.

## Syntax
<a name="aws-resource-imagebuilder-containerrecipe-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-imagebuilder-containerrecipe-syntax.json"></a>

```
{
  "Type" : "AWS::ImageBuilder::ContainerRecipe",
  "Properties" : {
      "[Components](#cfn-imagebuilder-containerrecipe-components)" : {{[ ComponentConfiguration, ... ]}},
      "[ContainerType](#cfn-imagebuilder-containerrecipe-containertype)" : {{String}},
      "[Description](#cfn-imagebuilder-containerrecipe-description)" : {{String}},
      "[DockerfileTemplateData](#cfn-imagebuilder-containerrecipe-dockerfiletemplatedata)" : {{String}},
      "[DockerfileTemplateUri](#cfn-imagebuilder-containerrecipe-dockerfiletemplateuri)" : {{String}},
      "[ImageOsVersionOverride](#cfn-imagebuilder-containerrecipe-imageosversionoverride)" : {{String}},
      "[InstanceConfiguration](#cfn-imagebuilder-containerrecipe-instanceconfiguration)" : {{InstanceConfiguration}},
      "[KmsKeyId](#cfn-imagebuilder-containerrecipe-kmskeyid)" : {{String}},
      "[Name](#cfn-imagebuilder-containerrecipe-name)" : {{String}},
      "[ParentImage](#cfn-imagebuilder-containerrecipe-parentimage)" : {{String}},
      "[PlatformOverride](#cfn-imagebuilder-containerrecipe-platformoverride)" : {{String}},
      "[Tags](#cfn-imagebuilder-containerrecipe-tags)" : {{{{{Key}}: {{Value}}, ...}}},
      "[TargetRepository](#cfn-imagebuilder-containerrecipe-targetrepository)" : {{TargetContainerRepository}},
      "[Version](#cfn-imagebuilder-containerrecipe-version)" : {{String}},
      "[WorkingDirectory](#cfn-imagebuilder-containerrecipe-workingdirectory)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-imagebuilder-containerrecipe-syntax.yaml"></a>

```
Type: AWS::ImageBuilder::ContainerRecipe
Properties:
  [Components](#cfn-imagebuilder-containerrecipe-components): {{
    - ComponentConfiguration}}
  [ContainerType](#cfn-imagebuilder-containerrecipe-containertype): {{String}}
  [Description](#cfn-imagebuilder-containerrecipe-description): {{String}}
  [DockerfileTemplateData](#cfn-imagebuilder-containerrecipe-dockerfiletemplatedata): {{String}}
  [DockerfileTemplateUri](#cfn-imagebuilder-containerrecipe-dockerfiletemplateuri): {{String}}
  [ImageOsVersionOverride](#cfn-imagebuilder-containerrecipe-imageosversionoverride): {{String}}
  [InstanceConfiguration](#cfn-imagebuilder-containerrecipe-instanceconfiguration): {{
    InstanceConfiguration}}
  [KmsKeyId](#cfn-imagebuilder-containerrecipe-kmskeyid): {{String}}
  [Name](#cfn-imagebuilder-containerrecipe-name): {{String}}
  [ParentImage](#cfn-imagebuilder-containerrecipe-parentimage): {{String}}
  [PlatformOverride](#cfn-imagebuilder-containerrecipe-platformoverride): {{String}}
  [Tags](#cfn-imagebuilder-containerrecipe-tags): {{
    {{Key}}: {{Value}}}}
  [TargetRepository](#cfn-imagebuilder-containerrecipe-targetrepository): {{
    TargetContainerRepository}}
  [Version](#cfn-imagebuilder-containerrecipe-version): {{String}}
  [WorkingDirectory](#cfn-imagebuilder-containerrecipe-workingdirectory): {{String}}
```

## Properties
<a name="aws-resource-imagebuilder-containerrecipe-properties"></a>

`Components`  <a name="cfn-imagebuilder-containerrecipe-components"></a>
Build and test components that are included in the container recipe. A recipe can contain a maximum of 20 build and test components in any combination, by default. This maximum is an adjustable quota. For more information, see [EC2 Image Builder endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/imagebuilder.html) in the *AWS General Reference*.
*Required*: No
*Type*: Array of [ComponentConfiguration](aws-properties-imagebuilder-containerrecipe-componentconfiguration.md)
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ContainerType`  <a name="cfn-imagebuilder-containerrecipe-containertype"></a>
Specifies the type of container, such as Docker.
*Required*: No
*Type*: String
*Allowed values*: `DOCKER`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-imagebuilder-containerrecipe-description"></a>
The description of the container recipe.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DockerfileTemplateData`  <a name="cfn-imagebuilder-containerrecipe-dockerfiletemplatedata"></a>
The Dockerfile template that Image Builder uses to build the container image. The template can include contextual variables that Image Builder replaces with build information at build time. For the contextual variables that the template can include, see [Create a new version of a container recipe](https://docs.aws.amazon.com/imagebuilder/latest/userguide/create-container-recipes.html) in the *EC2 Image Builder User Guide*.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DockerfileTemplateUri`  <a name="cfn-imagebuilder-containerrecipe-dockerfiletemplateuri"></a>
The Amazon S3 URI for the Dockerfile template that is used to build your container image. You must have permission to read the object. Image Builder reads the object once, when it creates the recipe, and stores its content in the recipe. Later changes to the S3 object don't affect the recipe. You must specify exactly one of the `dockerfileTemplateData` or `dockerfileTemplateUri` properties.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ImageOsVersionOverride`  <a name="cfn-imagebuilder-containerrecipe-imageosversionoverride"></a>
Specifies the operating system version for the base image. Use this property only when the base image is a container image from a registry. When the base image is an Image Builder image, the operating system version comes from the parent image.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InstanceConfiguration`  <a name="cfn-imagebuilder-containerrecipe-instanceconfiguration"></a>
A group of options that can be used to configure an instance for building and testing container images.
*Required*: No
*Type*: [InstanceConfiguration](aws-properties-imagebuilder-containerrecipe-instanceconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KmsKeyId`  <a name="cfn-imagebuilder-containerrecipe-kmskeyid"></a>
The KMS key that Image Builder uses to encrypt the recipe's Dockerfile template data at rest. This can be either the Key ARN or the Alias ARN. For more information, see [Key identifiers (KeyId)](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN) in the *AWS Key Management Service Developer Guide*. If you don't specify a key, Image Builder encrypts the template data with a KMS key that Image Builder owns. This key isn't used to encrypt the output container image.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-imagebuilder-containerrecipe-name"></a>
The name of the container recipe.
*Required*: No
*Type*: String
*Pattern*: `^[-_A-Za-z-0-9][-_A-Za-z0-9 ]{1,126}[-_A-Za-z-0-9]$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ParentImage`  <a name="cfn-imagebuilder-containerrecipe-parentimage"></a>
The base image for customizations specified in the container recipe. This can contain an Image Builder image resource ARN or a container image URI, for example `amazonlinux:latest`.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PlatformOverride`  <a name="cfn-imagebuilder-containerrecipe-platformoverride"></a>
Specifies the operating system platform when you use a custom base image. Container recipes support only the Linux and Windows platforms.
*Required*: No
*Type*: String
*Allowed values*: `Windows | Linux`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-imagebuilder-containerrecipe-tags"></a>
Tags that are attached to the container recipe.
*Required*: No
*Type*: Object of String
*Pattern*: `.{1,}`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetRepository`  <a name="cfn-imagebuilder-containerrecipe-targetrepository"></a>
The destination repository for the container image.
*Required*: No
*Type*: [TargetContainerRepository](aws-properties-imagebuilder-containerrecipe-targetcontainerrepository.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Version`  <a name="cfn-imagebuilder-containerrecipe-version"></a>
The semantic version of the container recipe. This version follows the semantic version syntax.
The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.
**Assignment:** For the first three nodes, you can assign any positive integer value, including zero. The upper limit is 2^30-1, or 1073741823, for each node. Image Builder automatically assigns the build number to the fourth node.
**Patterns:** You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01.
*Required*: No
*Type*: String
*Pattern*: `^(?:[0-9]+|x)\.(?:[0-9]+|x)\.(?:[0-9]+|x)$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`WorkingDirectory`  <a name="cfn-imagebuilder-containerrecipe-workingdirectory"></a>
The working directory for use during build and test workflows.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-imagebuilder-containerrecipe-return-values"></a>

### Ref
<a name="aws-resource-imagebuilder-containerrecipe-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource ARN, such as `arn:aws:imagebuilder:us-east-1:111122223333:container-recipe/mybasicrecipe/2020.12.17`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-imagebuilder-containerrecipe-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-imagebuilder-containerrecipe-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Returns the Amazon Resource Name (ARN) of the container recipe. For example, `arn:aws:imagebuilder:us-east-1:111122223333:container-recipe/mybasicrecipe/2020.12.17`.

`LatestVersion.Arn`  <a name="LatestVersion.Arn-fn::getatt"></a>
The latest version Amazon Resource Name (ARN) of the Image Builder resource.

`LatestVersion.Major`  <a name="LatestVersion.Major-fn::getatt"></a>
The latest version Amazon Resource Name (ARN) with the same `major` version of the Image Builder resource.

`LatestVersion.Minor`  <a name="LatestVersion.Minor-fn::getatt"></a>
The latest version Amazon Resource Name (ARN) with the same `minor` version of the Image Builder resource.

`LatestVersion.Patch`  <a name="LatestVersion.Patch-fn::getatt"></a>
The latest version Amazon Resource Name (ARN) with the same `patch` version of the Image Builder resource.

`Name`  <a name="Name-fn::getatt"></a>
Returns the name of the container recipe.

## Examples
<a name="aws-resource-imagebuilder-containerrecipe--examples"></a>

### Create a container recipe
<a name="aws-resource-imagebuilder-containerrecipe--examples--Create_a_container_recipe"></a>

The following example shows the template for the ContainerRecipe resource in both YAML and JSON format.

#### YAML
<a name="aws-resource-imagebuilder-containerrecipe--examples--Create_a_container_recipe--yaml"></a>

```
Resources:
   ContainerRecipeAllParameters:
      Type: 'AWS::ImageBuilder::ContainerRecipe'
      Properties:
         Name: 'container-recipe-name'
         Version: '1.0.0'
         ParentImage: !Ref ParentImage
         Description: 'description'
         ContainerType: 'DOCKER'
         Components:
            - ComponentArn: !Ref ComponentArn
            - ComponentArn: !Ref AnotherComponentArn
         TargetRepository:
            Service: 'ECR'
            RepositoryName: !Ref RepositoryName
         DockerfileTemplateData: |
           FROM {{{ imagebuilder:parentImage }}}
           {{{ imagebuilder:environments }}}
           {{{ imagebuilder:components }}}
         WorkingDirectory: "dummy-working-directory"
         KmsKeyId: !Ref KmsKeyId
         Tags:
            Usage: 'Documentation'

Outputs:
   OutputContainerRecipeArn:
      Value:
         'Fn::GetAtt':
            - ContainerRecipeAllParameters
            - Arn
```

#### JSON
<a name="aws-resource-imagebuilder-containerrecipe--examples--Create_a_container_recipe--json"></a>

```
{
   "Resources": {
      "ContainerRecipeAllParameters": {
         "Type": "AWS::ImageBuilder::ContainerRecipe",
         "Properties": {
            "Name": "container-recipe-name",
            "Version": "1.0.0",
            "ParentImage": {
               "Ref": "ParentImage"
            },
            "Description": "description",
            "ContainerType": "DOCKER",
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
            "TargetRepository": {
               "Service": "ECR",
               "RepositoryName": {
                  "Ref": "RepositoryName"
               }
            },
            "DockerfileTemplateData": "FROM {{{ imagebuilder:parentImage }}}\n{{{ imagebuilder:environments }}}\n{{{ imagebuilder:components }}}\n",
            "WorkingDirectory": "dummy-working-directory",
            "KmsKeyId": {
               "Ref": "KmsKeyId"
            },
            "Tags": {
               "Usage": "Documentation"
            }
         }
      }
   },
   "Outputs": {
      "OutputContainerRecipeArn": {
         "Value": {
            "Fn::GetAtt": [
               "ContainerRecipeAllParameters",
               "Arn"
            ]
         }
      }
   }
}
```

## See also
<a name="aws-resource-imagebuilder-containerrecipe--seealso"></a>
+ [Create a container recipe](https://docs.aws.amazon.com/imagebuilder/latest/userguide/create-container-recipes.html) in the *Image Builder User Guide*.
