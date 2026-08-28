---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-taskdefinition-fsxauthorizationconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::TaskDefinition FSxAuthorizationConfig
<a name="aws-properties-ecs-taskdefinition-fsxauthorizationconfig"></a>

The authorization configuration details for Amazon FSx for Windows File Server file system. See [FSxWindowsFileServerVolumeConfiguration](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_FSxWindowsFileServerVolumeConfiguration.html) in the *Amazon ECS API Reference*.

For more information and the input format, see [Amazon FSx for Windows File Server Volumes](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/wfsx-volumes.html) in the *Amazon Elastic Container Service Developer Guide*.

## Syntax
<a name="aws-properties-ecs-taskdefinition-fsxauthorizationconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-taskdefinition-fsxauthorizationconfig-syntax.json"></a>

```
{
  "[CredentialsParameter](#cfn-ecs-taskdefinition-fsxauthorizationconfig-credentialsparameter)" : {{String}},
  "[Domain](#cfn-ecs-taskdefinition-fsxauthorizationconfig-domain)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecs-taskdefinition-fsxauthorizationconfig-syntax.yaml"></a>

```
  [CredentialsParameter](#cfn-ecs-taskdefinition-fsxauthorizationconfig-credentialsparameter): {{String}}
  [Domain](#cfn-ecs-taskdefinition-fsxauthorizationconfig-domain): {{String}}
```

## Properties
<a name="aws-properties-ecs-taskdefinition-fsxauthorizationconfig-properties"></a>

`CredentialsParameter`  <a name="cfn-ecs-taskdefinition-fsxauthorizationconfig-credentialsparameter"></a>
The authorization credential option to use. The authorization credential options can be provided using either the Amazon Resource Name (ARN) of an AWS Secrets Manager secret or SSM Parameter Store parameter. The ARN refers to the stored credentials.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Domain`  <a name="cfn-ecs-taskdefinition-fsxauthorizationconfig-domain"></a>
A fully qualified domain name hosted by an [AWS Directory Service](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_microsoft_ad.html) Managed Microsoft AD (Active Directory) or self-hosted AD on Amazon EC2.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
