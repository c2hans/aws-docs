---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-expressgatewayservice-expressgatewaycontainer.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::ExpressGatewayService ExpressGatewayContainer
<a name="aws-properties-ecs-expressgatewayservice-expressgatewaycontainer"></a>

Defines the configuration for the primary container in an Express service. This container receives traffic from the Application Load Balancer and runs your application code.

The container configuration includes the container image, port mapping, logging settings, environment variables, and secrets. The container image is the only required parameter, with sensible defaults provided for other settings.

## Syntax
<a name="aws-properties-ecs-expressgatewayservice-expressgatewaycontainer-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-expressgatewayservice-expressgatewaycontainer-syntax.json"></a>

```
{
  "[AwsLogsConfiguration](#cfn-ecs-expressgatewayservice-expressgatewaycontainer-awslogsconfiguration)" : {{ExpressGatewayServiceAwsLogsConfiguration}},
  "[Command](#cfn-ecs-expressgatewayservice-expressgatewaycontainer-command)" : {{[ String, ... ]}},
  "[ContainerPort](#cfn-ecs-expressgatewayservice-expressgatewaycontainer-containerport)" : {{Integer}},
  "[Environment](#cfn-ecs-expressgatewayservice-expressgatewaycontainer-environment)" : {{[ KeyValuePair, ... ]}},
  "[Image](#cfn-ecs-expressgatewayservice-expressgatewaycontainer-image)" : {{String}},
  "[RepositoryCredentials](#cfn-ecs-expressgatewayservice-expressgatewaycontainer-repositorycredentials)" : {{ExpressGatewayRepositoryCredentials}},
  "[Secrets](#cfn-ecs-expressgatewayservice-expressgatewaycontainer-secrets)" : {{[ Secret, ... ]}}
}
```

### YAML
<a name="aws-properties-ecs-expressgatewayservice-expressgatewaycontainer-syntax.yaml"></a>

```
  [AwsLogsConfiguration](#cfn-ecs-expressgatewayservice-expressgatewaycontainer-awslogsconfiguration): {{
    ExpressGatewayServiceAwsLogsConfiguration}}
  [Command](#cfn-ecs-expressgatewayservice-expressgatewaycontainer-command): {{
    - String}}
  [ContainerPort](#cfn-ecs-expressgatewayservice-expressgatewaycontainer-containerport): {{Integer}}
  [Environment](#cfn-ecs-expressgatewayservice-expressgatewaycontainer-environment): {{
    - KeyValuePair}}
  [Image](#cfn-ecs-expressgatewayservice-expressgatewaycontainer-image): {{String}}
  [RepositoryCredentials](#cfn-ecs-expressgatewayservice-expressgatewaycontainer-repositorycredentials): {{
    ExpressGatewayRepositoryCredentials}}
  [Secrets](#cfn-ecs-expressgatewayservice-expressgatewaycontainer-secrets): {{
    - Secret}}
```

## Properties
<a name="aws-properties-ecs-expressgatewayservice-expressgatewaycontainer-properties"></a>

`AwsLogsConfiguration`  <a name="cfn-ecs-expressgatewayservice-expressgatewaycontainer-awslogsconfiguration"></a>
The log configuration for the container.
*Required*: No
*Type*: [ExpressGatewayServiceAwsLogsConfiguration](aws-properties-ecs-expressgatewayservice-expressgatewayserviceawslogsconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Command`  <a name="cfn-ecs-expressgatewayservice-expressgatewaycontainer-command"></a>
The command that is passed to the container.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ContainerPort`  <a name="cfn-ecs-expressgatewayservice-expressgatewaycontainer-containerport"></a>
The port number on the container that receives traffic from the load balancer. Default is 80.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Environment`  <a name="cfn-ecs-expressgatewayservice-expressgatewaycontainer-environment"></a>
The environment variables to pass to the container.
*Required*: No
*Type*: Array of [KeyValuePair](aws-properties-ecs-expressgatewayservice-keyvaluepair.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Image`  <a name="cfn-ecs-expressgatewayservice-expressgatewaycontainer-image"></a>
The image used to start a container. This string is passed directly to the Docker daemon. Images in the Docker Hub registry are available by default. Other repositories are specified with either `repository-url/image:tag` or `repository-url/image@digest`.
For Express services, the image typically contains a web application that listens on the specified container port. The image can be stored in Amazon ECR, Docker Hub, or any other container registry accessible to your execution role.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RepositoryCredentials`  <a name="cfn-ecs-expressgatewayservice-expressgatewaycontainer-repositorycredentials"></a>
The configuration for repository credentials for private registry authentication.
*Required*: No
*Type*: [ExpressGatewayRepositoryCredentials](aws-properties-ecs-expressgatewayservice-expressgatewayrepositorycredentials.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Secrets`  <a name="cfn-ecs-expressgatewayservice-expressgatewaycontainer-secrets"></a>
The secrets to pass to the container.
*Required*: No
*Type*: Array of [Secret](aws-properties-ecs-expressgatewayservice-secret.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
