---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-virtualnode-virtualnodespec.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::VirtualNode VirtualNodeSpec
<a name="aws-properties-appmesh-virtualnode-virtualnodespec"></a>

An object that represents the specification of a virtual node.

## Syntax
<a name="aws-properties-appmesh-virtualnode-virtualnodespec-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-virtualnode-virtualnodespec-syntax.json"></a>

```
{
  "[BackendDefaults](#cfn-appmesh-virtualnode-virtualnodespec-backenddefaults)" : {{BackendDefaults}},
  "[Backends](#cfn-appmesh-virtualnode-virtualnodespec-backends)" : {{[ Backend, ... ]}},
  "[Listeners](#cfn-appmesh-virtualnode-virtualnodespec-listeners)" : {{[ Listener, ... ]}},
  "[Logging](#cfn-appmesh-virtualnode-virtualnodespec-logging)" : {{Logging}},
  "[ServiceDiscovery](#cfn-appmesh-virtualnode-virtualnodespec-servicediscovery)" : {{ServiceDiscovery}}
}
```

### YAML
<a name="aws-properties-appmesh-virtualnode-virtualnodespec-syntax.yaml"></a>

```
  [BackendDefaults](#cfn-appmesh-virtualnode-virtualnodespec-backenddefaults): {{
    BackendDefaults}}
  [Backends](#cfn-appmesh-virtualnode-virtualnodespec-backends): {{
    - Backend}}
  [Listeners](#cfn-appmesh-virtualnode-virtualnodespec-listeners): {{
    - Listener}}
  [Logging](#cfn-appmesh-virtualnode-virtualnodespec-logging): {{
    Logging}}
  [ServiceDiscovery](#cfn-appmesh-virtualnode-virtualnodespec-servicediscovery): {{
    ServiceDiscovery}}
```

## Properties
<a name="aws-properties-appmesh-virtualnode-virtualnodespec-properties"></a>

`BackendDefaults`  <a name="cfn-appmesh-virtualnode-virtualnodespec-backenddefaults"></a>
A reference to an object that represents the defaults for backends.
*Required*: No
*Type*: [BackendDefaults](aws-properties-appmesh-virtualnode-backenddefaults.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Backends`  <a name="cfn-appmesh-virtualnode-virtualnodespec-backends"></a>
The backends that the virtual node is expected to send outbound traffic to.
App Mesh doesn't validate the existence of those virtual services specified in backends. This is to prevent a cyclic dependency between virtual nodes and virtual services creation. Make sure the virtual service name is correct. The virtual service can be created afterwards if it doesn't already exist.
*Required*: No
*Type*: Array of [Backend](aws-properties-appmesh-virtualnode-backend.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Listeners`  <a name="cfn-appmesh-virtualnode-virtualnodespec-listeners"></a>
The listener that the virtual node is expected to receive inbound traffic from. You can specify one listener.
*Required*: No
*Type*: Array of [Listener](aws-properties-appmesh-virtualnode-listener.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Logging`  <a name="cfn-appmesh-virtualnode-virtualnodespec-logging"></a>
The inbound and outbound access logging information for the virtual node.
*Required*: No
*Type*: [Logging](aws-properties-appmesh-virtualnode-logging.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServiceDiscovery`  <a name="cfn-appmesh-virtualnode-virtualnodespec-servicediscovery"></a>
The service discovery information for the virtual node. If your virtual node does not expect ingress traffic, you can omit this parameter. If you specify a `listener`, then you must specify service discovery information.
*Required*: No
*Type*: [ServiceDiscovery](aws-properties-appmesh-virtualnode-servicediscovery.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
