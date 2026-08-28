---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lightsail-container-publicendpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lightsail::Container PublicEndpoint
<a name="aws-properties-lightsail-container-publicendpoint"></a>

`PublicEndpoint` is a property of the [ContainerServiceDeployment](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-containerservicedeployment.html) property. It describes describes the settings of the public endpoint of a container on a container service.

## Syntax
<a name="aws-properties-lightsail-container-publicendpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lightsail-container-publicendpoint-syntax.json"></a>

```
{
  "[ContainerName](#cfn-lightsail-container-publicendpoint-containername)" : {{String}},
  "[ContainerPort](#cfn-lightsail-container-publicendpoint-containerport)" : {{Integer}},
  "[HealthCheckConfig](#cfn-lightsail-container-publicendpoint-healthcheckconfig)" : {{HealthCheckConfig}}
}
```

### YAML
<a name="aws-properties-lightsail-container-publicendpoint-syntax.yaml"></a>

```
  [ContainerName](#cfn-lightsail-container-publicendpoint-containername): {{String}}
  [ContainerPort](#cfn-lightsail-container-publicendpoint-containerport): {{Integer}}
  [HealthCheckConfig](#cfn-lightsail-container-publicendpoint-healthcheckconfig): {{
    HealthCheckConfig}}
```

## Properties
<a name="aws-properties-lightsail-container-publicendpoint-properties"></a>

`ContainerName`  <a name="cfn-lightsail-container-publicendpoint-containername"></a>
The name of the container entry of the deployment that the endpoint configuration applies to.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ContainerPort`  <a name="cfn-lightsail-container-publicendpoint-containerport"></a>
The port of the specified container to which traffic is forwarded to.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HealthCheckConfig`  <a name="cfn-lightsail-container-publicendpoint-healthcheckconfig"></a>
An object that describes the health check configuration of the container.
*Required*: No
*Type*: [HealthCheckConfig](aws-properties-lightsail-container-healthcheckconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
