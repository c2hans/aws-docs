---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apprunner-service-authenticationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppRunner::Service AuthenticationConfiguration
<a name="aws-properties-apprunner-service-authenticationconfiguration"></a>

Describes resources needed to authenticate access to some source repositories. The specific resource depends on the repository provider.

## Syntax
<a name="aws-properties-apprunner-service-authenticationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apprunner-service-authenticationconfiguration-syntax.json"></a>

```
{
  "[AccessRoleArn](#cfn-apprunner-service-authenticationconfiguration-accessrolearn)" : {{String}},
  "[ConnectionArn](#cfn-apprunner-service-authenticationconfiguration-connectionarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-apprunner-service-authenticationconfiguration-syntax.yaml"></a>

```
  [AccessRoleArn](#cfn-apprunner-service-authenticationconfiguration-accessrolearn): {{String}}
  [ConnectionArn](#cfn-apprunner-service-authenticationconfiguration-connectionarn): {{String}}
```

## Properties
<a name="aws-properties-apprunner-service-authenticationconfiguration-properties"></a>

`AccessRoleArn`  <a name="cfn-apprunner-service-authenticationconfiguration-accessrolearn"></a>
The Amazon Resource Name (ARN) of the IAM role that grants the App Runner service access to a source repository. It's required for ECR image repositories (but not for ECR Public repositories).
*Required*: No
*Type*: String
*Pattern*: `arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):iam::[0-9]{12}:role/[\w+=,.@-]{1,64}`
*Minimum*: `29`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConnectionArn`  <a name="cfn-apprunner-service-authenticationconfiguration-connectionarn"></a>
The Amazon Resource Name (ARN) of the App Runner connection that enables the App Runner service to connect to a source repository. It's required for GitHub code repositories.
*Required*: No
*Type*: String
*Pattern*: `arn:aws(-[\w]+)*:[a-z0-9-\\.]{0,63}:[a-z0-9-\\.]{0,63}:[0-9]{12}:(\w|\/|-){1,1011}`
*Minimum*: `1`
*Maximum*: `1011`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
