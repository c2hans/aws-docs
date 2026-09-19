---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticbeanstalk-applicationversion-buildconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticBeanstalk::ApplicationVersion BuildConfiguration
<a name="aws-properties-elasticbeanstalk-applicationversion-buildconfiguration"></a>

Settings for an AWS CodeBuild build.

## Syntax
<a name="aws-properties-elasticbeanstalk-applicationversion-buildconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticbeanstalk-applicationversion-buildconfiguration-syntax.json"></a>

```
{
  "[ArtifactName](#cfn-elasticbeanstalk-applicationversion-buildconfiguration-artifactname)" : {{String}},
  "[CodeBuildServiceRole](#cfn-elasticbeanstalk-applicationversion-buildconfiguration-codebuildservicerole)" : {{String}},
  "[ComputeType](#cfn-elasticbeanstalk-applicationversion-buildconfiguration-computetype)" : {{String}},
  "[Image](#cfn-elasticbeanstalk-applicationversion-buildconfiguration-image)" : {{String}},
  "[TimeoutInMinutes](#cfn-elasticbeanstalk-applicationversion-buildconfiguration-timeoutinminutes)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-elasticbeanstalk-applicationversion-buildconfiguration-syntax.yaml"></a>

```
  [ArtifactName](#cfn-elasticbeanstalk-applicationversion-buildconfiguration-artifactname): {{String}}
  [CodeBuildServiceRole](#cfn-elasticbeanstalk-applicationversion-buildconfiguration-codebuildservicerole): {{String}}
  [ComputeType](#cfn-elasticbeanstalk-applicationversion-buildconfiguration-computetype): {{String}}
  [Image](#cfn-elasticbeanstalk-applicationversion-buildconfiguration-image): {{String}}
  [TimeoutInMinutes](#cfn-elasticbeanstalk-applicationversion-buildconfiguration-timeoutinminutes): {{Integer}}
```

## Properties
<a name="aws-properties-elasticbeanstalk-applicationversion-buildconfiguration-properties"></a>

`ArtifactName`  <a name="cfn-elasticbeanstalk-applicationversion-buildconfiguration-artifactname"></a>
The name of the artifact of the CodeBuild build. If provided, Elastic Beanstalk stores the build artifact in the S3 location *S3-bucket*/resources/*application-name*/codebuild/codebuild-*version-label*-*artifact-name*.zip. If not provided, Elastic Beanstalk stores the build artifact in the S3 location *S3-bucket*/resources/*application-name*/codebuild/codebuild-*version-label*.zip.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CodeBuildServiceRole`  <a name="cfn-elasticbeanstalk-applicationversion-buildconfiguration-codebuildservicerole"></a>
The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS service on behalf of the AWS account.
*Required*: Yes
*Type*: String
*Pattern*: `.*\S.*`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ComputeType`  <a name="cfn-elasticbeanstalk-applicationversion-buildconfiguration-computetype"></a>
Information about the compute resources the build project will use.
+  `BUILD_GENERAL1_SMALL: Use up to 3 GB memory and 2 vCPUs for builds`
+  `BUILD_GENERAL1_MEDIUM: Use up to 7 GB memory and 4 vCPUs for builds`
+  `BUILD_GENERAL1_LARGE: Use up to 15 GB memory and 8 vCPUs for builds`
*Required*: No
*Type*: String
*Allowed values*: `BUILD_GENERAL1_SMALL | BUILD_GENERAL1_MEDIUM | BUILD_GENERAL1_LARGE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Image`  <a name="cfn-elasticbeanstalk-applicationversion-buildconfiguration-image"></a>
The ID of the Docker image to use for this build project.
*Required*: Yes
*Type*: String
*Pattern*: `.*\S.*`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TimeoutInMinutes`  <a name="cfn-elasticbeanstalk-applicationversion-buildconfiguration-timeoutinminutes"></a>
How long in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait until timing out any related build that does not get marked as completed. The default is 60 minutes.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
