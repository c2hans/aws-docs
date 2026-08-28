---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-virtualgateway-virtualgatewayspec.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::VirtualGateway VirtualGatewaySpec
<a name="aws-properties-appmesh-virtualgateway-virtualgatewayspec"></a>

An object that represents the specification of a service mesh resource.

## Syntax
<a name="aws-properties-appmesh-virtualgateway-virtualgatewayspec-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-virtualgateway-virtualgatewayspec-syntax.json"></a>

```
{
  "[BackendDefaults](#cfn-appmesh-virtualgateway-virtualgatewayspec-backenddefaults)" : {{VirtualGatewayBackendDefaults}},
  "[Listeners](#cfn-appmesh-virtualgateway-virtualgatewayspec-listeners)" : {{[ VirtualGatewayListener, ... ]}},
  "[Logging](#cfn-appmesh-virtualgateway-virtualgatewayspec-logging)" : {{VirtualGatewayLogging}}
}
```

### YAML
<a name="aws-properties-appmesh-virtualgateway-virtualgatewayspec-syntax.yaml"></a>

```
  [BackendDefaults](#cfn-appmesh-virtualgateway-virtualgatewayspec-backenddefaults): {{
    VirtualGatewayBackendDefaults}}
  [Listeners](#cfn-appmesh-virtualgateway-virtualgatewayspec-listeners): {{
    - VirtualGatewayListener}}
  [Logging](#cfn-appmesh-virtualgateway-virtualgatewayspec-logging): {{
    VirtualGatewayLogging}}
```

## Properties
<a name="aws-properties-appmesh-virtualgateway-virtualgatewayspec-properties"></a>

`BackendDefaults`  <a name="cfn-appmesh-virtualgateway-virtualgatewayspec-backenddefaults"></a>
A reference to an object that represents the defaults for backends.
*Required*: No
*Type*: [VirtualGatewayBackendDefaults](aws-properties-appmesh-virtualgateway-virtualgatewaybackenddefaults.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Listeners`  <a name="cfn-appmesh-virtualgateway-virtualgatewayspec-listeners"></a>
The listeners that the mesh endpoint is expected to receive inbound traffic from. You can specify one listener.
*Required*: Yes
*Type*: Array of [VirtualGatewayListener](aws-properties-appmesh-virtualgateway-virtualgatewaylistener.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Logging`  <a name="cfn-appmesh-virtualgateway-virtualgatewayspec-logging"></a>
An object that represents logging information.
*Required*: No
*Type*: [VirtualGatewayLogging](aws-properties-appmesh-virtualgateway-virtualgatewaylogging.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
