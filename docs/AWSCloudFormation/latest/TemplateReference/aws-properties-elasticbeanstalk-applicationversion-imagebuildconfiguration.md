---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticbeanstalk-applicationversion-imagebuildconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticBeanstalk::ApplicationVersion ImageBuildConfiguration
<a name="aws-properties-elasticbeanstalk-applicationversion-imagebuildconfiguration"></a>

The `ImageBuildConfiguration` property type specifies settings that Elastic Beanstalk uses to build a container image from the source bundle of an application version.

## Syntax
<a name="aws-properties-elasticbeanstalk-applicationversion-imagebuildconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticbeanstalk-applicationversion-imagebuildconfiguration-syntax.json"></a>

```
{
  "[Architecture](#cfn-elasticbeanstalk-applicationversion-imagebuildconfiguration-architecture)" : {{String}},
  "[Buildpack](#cfn-elasticbeanstalk-applicationversion-imagebuildconfiguration-buildpack)" : {{String}},
  "[CodeBuildServiceRole](#cfn-elasticbeanstalk-applicationversion-imagebuildconfiguration-codebuildservicerole)" : {{String}},
  "[ComputeType](#cfn-elasticbeanstalk-applicationversion-imagebuildconfiguration-computetype)" : {{String}},
  "[DockerfileLocation](#cfn-elasticbeanstalk-applicationversion-imagebuildconfiguration-dockerfilelocation)" : {{String}},
  "[TimeoutInMinutes](#cfn-elasticbeanstalk-applicationversion-imagebuildconfiguration-timeoutinminutes)" : {{Integer}},
  "[Type](#cfn-elasticbeanstalk-applicationversion-imagebuildconfiguration-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-elasticbeanstalk-applicationversion-imagebuildconfiguration-syntax.yaml"></a>

```
  [Architecture](#cfn-elasticbeanstalk-applicationversion-imagebuildconfiguration-architecture): {{String}}
  [Buildpack](#cfn-elasticbeanstalk-applicationversion-imagebuildconfiguration-buildpack): {{String}}
  [CodeBuildServiceRole](#cfn-elasticbeanstalk-applicationversion-imagebuildconfiguration-codebuildservicerole): {{String}}
  [ComputeType](#cfn-elasticbeanstalk-applicationversion-imagebuildconfiguration-computetype): {{String}}
  [DockerfileLocation](#cfn-elasticbeanstalk-applicationversion-imagebuildconfiguration-dockerfilelocation): {{String}}
  [TimeoutInMinutes](#cfn-elasticbeanstalk-applicationversion-imagebuildconfiguration-timeoutinminutes): {{Integer}}
  [Type](#cfn-elasticbeanstalk-applicationversion-imagebuildconfiguration-type): {{String}}
```

## Properties
<a name="aws-properties-elasticbeanstalk-applicationversion-imagebuildconfiguration-properties"></a>

`Architecture`  <a name="cfn-elasticbeanstalk-applicationversion-imagebuildconfiguration-architecture"></a>
The processor architecture that Elastic Beanstalk builds the container image for. The architecture must match the architecture of the instances in the environment that you deploy the application version to.
Valid values:
+ `amd64` – x86-64 instances. This is the default.
+ `arm64` – AWS Graviton instances.
*Required*: No
*Type*: String
*Allowed values*: `amd64 | arm64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Buildpack`  <a name="cfn-elasticbeanstalk-applicationversion-imagebuildconfiguration-buildpack"></a>
The Cloud Native Buildpacks builder image that Elastic Beanstalk uses to build the container image. For example, `paketobuildpacks/builder-jammy-base`.
This member is required when `Type` is `buildpack`. Elastic Beanstalk doesn't provide a default builder.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CodeBuildServiceRole`  <a name="cfn-elasticbeanstalk-applicationversion-imagebuildconfiguration-codebuildservicerole"></a>
The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that AWS CodeBuild assumes to run the build in your AWS account. Elastic Beanstalk rejects a `Build` that doesn't specify this role.
*Required*: Yes
*Type*: String
*Pattern*: `.*\S.*`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ComputeType`  <a name="cfn-elasticbeanstalk-applicationversion-imagebuildconfiguration-computetype"></a>
The size of the compute resources that run the build. If you don't specify it, Elastic Beanstalk uses `BUILD_GENERAL1_MEDIUM`.
Valid values:
+ `BUILD_GENERAL1_SMALL` – Use up to 3 GB memory and 2 vCPUs for builds.
+ `BUILD_GENERAL1_MEDIUM` – Use up to 7 GB memory and 4 vCPUs for builds.
+ `BUILD_GENERAL1_LARGE` – Use up to 15 GB memory and 8 vCPUs for builds.
*Required*: No
*Type*: String
*Allowed values*: `BUILD_GENERAL1_SMALL | BUILD_GENERAL1_MEDIUM | BUILD_GENERAL1_LARGE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DockerfileLocation`  <a name="cfn-elasticbeanstalk-applicationversion-imagebuildconfiguration-dockerfilelocation"></a>
The path to the Dockerfile within the source bundle, relative to the root of the source bundle. For example, `backend/Dockerfile`.
Elastic Beanstalk uses this member only when `Type` is `docker`. If you don't specify it, Elastic Beanstalk uses the Dockerfile at the root of the source bundle.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TimeoutInMinutes`  <a name="cfn-elasticbeanstalk-applicationversion-imagebuildconfiguration-timeoutinminutes"></a>
How long, in minutes from 5 to 480 (8 hours), Elastic Beanstalk waits before stopping a build that hasn't completed. The default is 60 minutes.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Type`  <a name="cfn-elasticbeanstalk-applicationversion-imagebuildconfiguration-type"></a>
How Elastic Beanstalk builds the container image. Elastic Beanstalk rejects a `Build` that doesn't specify it.
Valid values:
+ `docker` – Elastic Beanstalk builds the image from a Dockerfile in your source bundle. Specify the Dockerfile with `DockerfileLocation`.
+ `buildpack` – Elastic Beanstalk builds the image with a Cloud Native Buildpacks builder. Specify the builder with `Buildpack`.
*Required*: Yes
*Type*: String
*Allowed values*: `docker | buildpack`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
