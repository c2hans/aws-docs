---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lightsail-container-containerservicedeployment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lightsail::Container ContainerServiceDeployment
<a name="aws-properties-lightsail-container-containerservicedeployment"></a>

`ContainerServiceDeployment` is a property of the [AWS::Lightsail::Container](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-container.html) resource. It describes a container deployment configuration of a container service.

A deployment specifies the settings, such as the ports and launch command, of containers that are deployed to your container service.

## Syntax
<a name="aws-properties-lightsail-container-containerservicedeployment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lightsail-container-containerservicedeployment-syntax.json"></a>

```
{
  "[Containers](#cfn-lightsail-container-containerservicedeployment-containers)" : {{[ Container, ... ]}},
  "[PublicEndpoint](#cfn-lightsail-container-containerservicedeployment-publicendpoint)" : {{PublicEndpoint}}
}
```

### YAML
<a name="aws-properties-lightsail-container-containerservicedeployment-syntax.yaml"></a>

```
  [Containers](#cfn-lightsail-container-containerservicedeployment-containers): {{
    - Container}}
  [PublicEndpoint](#cfn-lightsail-container-containerservicedeployment-publicendpoint): {{
    PublicEndpoint}}
```

## Properties
<a name="aws-properties-lightsail-container-containerservicedeployment-properties"></a>

`Containers`  <a name="cfn-lightsail-container-containerservicedeployment-containers"></a>
An object that describes the configuration for the containers of the deployment.
*Required*: No
*Type*: Array of [Container](aws-properties-lightsail-container-container.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PublicEndpoint`  <a name="cfn-lightsail-container-containerservicedeployment-publicendpoint"></a>
An object that describes the endpoint of the deployment.
*Required*: No
*Type*: [PublicEndpoint](aws-properties-lightsail-container-publicendpoint.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
