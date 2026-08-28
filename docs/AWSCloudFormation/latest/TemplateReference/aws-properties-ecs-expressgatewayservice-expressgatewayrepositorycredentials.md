---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-expressgatewayservice-expressgatewayrepositorycredentials.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::ExpressGatewayService ExpressGatewayRepositoryCredentials
<a name="aws-properties-ecs-expressgatewayservice-expressgatewayrepositorycredentials"></a>

The repository credentials for private registry authentication to pass to the container.

## Syntax
<a name="aws-properties-ecs-expressgatewayservice-expressgatewayrepositorycredentials-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-expressgatewayservice-expressgatewayrepositorycredentials-syntax.json"></a>

```
{
  "[CredentialsParameter](#cfn-ecs-expressgatewayservice-expressgatewayrepositorycredentials-credentialsparameter)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecs-expressgatewayservice-expressgatewayrepositorycredentials-syntax.yaml"></a>

```
  [CredentialsParameter](#cfn-ecs-expressgatewayservice-expressgatewayrepositorycredentials-credentialsparameter): {{String}}
```

## Properties
<a name="aws-properties-ecs-expressgatewayservice-expressgatewayrepositorycredentials-properties"></a>

`CredentialsParameter`  <a name="cfn-ecs-expressgatewayservice-expressgatewayrepositorycredentials-credentialsparameter"></a>
The Amazon Resource Name (ARN) of the secret containing the private repository credentials.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
