---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-daemontaskdefinition-repositorycredentials.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::DaemonTaskDefinition RepositoryCredentials
<a name="aws-properties-ecs-daemontaskdefinition-repositorycredentials"></a>

The repository credentials for private registry authentication.

## Syntax
<a name="aws-properties-ecs-daemontaskdefinition-repositorycredentials-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-daemontaskdefinition-repositorycredentials-syntax.json"></a>

```
{
  "[CredentialsParameter](#cfn-ecs-daemontaskdefinition-repositorycredentials-credentialsparameter)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecs-daemontaskdefinition-repositorycredentials-syntax.yaml"></a>

```
  [CredentialsParameter](#cfn-ecs-daemontaskdefinition-repositorycredentials-credentialsparameter): {{String}}
```

## Properties
<a name="aws-properties-ecs-daemontaskdefinition-repositorycredentials-properties"></a>

`CredentialsParameter`  <a name="cfn-ecs-daemontaskdefinition-repositorycredentials-credentialsparameter"></a>
The Amazon Resource Name (ARN) of the secret containing the private repository credentials.
When you use the Amazon ECS API, AWS CLI, or AWS SDK, if the secret exists in the same Region as the task that you're launching then you can use either the full ARN or the name of the secret. When you use the AWS Management Console, you must specify the full ARN of the secret.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
