---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codebuild-project-dockerserver.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeBuild::Project DockerServer
<a name="aws-properties-codebuild-project-dockerserver"></a>

Contains the configuration details for the dedicated Docker server associated with this build project, including the compute type and network security settings. For more information, see [Docker image build server sample for CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-docker-server.html) in the *AWS CodeBuild User Guide*.

## Syntax
<a name="aws-properties-codebuild-project-dockerserver-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codebuild-project-dockerserver-syntax.json"></a>

```
{
  "[ComputeType](#cfn-codebuild-project-dockerserver-computetype)" : {{String}},
  "[SecurityGroupIds](#cfn-codebuild-project-dockerserver-securitygroupids)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-codebuild-project-dockerserver-syntax.yaml"></a>

```
  [ComputeType](#cfn-codebuild-project-dockerserver-computetype): {{String}}
  [SecurityGroupIds](#cfn-codebuild-project-dockerserver-securitygroupids): {{
    - String}}
```

## Properties
<a name="aws-properties-codebuild-project-dockerserver-properties"></a>

`ComputeType`  <a name="cfn-codebuild-project-dockerserver-computetype"></a>
The type of compute environment to use for the Docker server.
*Required*: Yes
*Type*: String
*Allowed values*: `BUILD_GENERAL1_SMALL | BUILD_GENERAL1_MEDIUM | BUILD_GENERAL1_LARGE | BUILD_GENERAL1_XLARGE | BUILD_GENERAL1_2XLARGE | BUILD_LAMBDA_1GB | BUILD_LAMBDA_2GB | BUILD_LAMBDA_4GB | BUILD_LAMBDA_8GB | BUILD_LAMBDA_10GB | ATTRIBUTE_BASED_COMPUTE | CUSTOM_INSTANCE_TYPE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecurityGroupIds`  <a name="cfn-codebuild-project-dockerserver-securitygroupids"></a>
A list of security group IDs for the Docker server. Security groups for the Docker server must allow ingress traffic from the VPC configured in the project on port 9876.
*Required*: No
*Type*: Array of String
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
