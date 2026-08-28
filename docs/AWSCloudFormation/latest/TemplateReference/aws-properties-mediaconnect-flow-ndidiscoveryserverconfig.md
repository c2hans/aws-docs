---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-flow-ndidiscoveryserverconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::Flow NdiDiscoveryServerConfig
<a name="aws-properties-mediaconnect-flow-ndidiscoveryserverconfig"></a>

Specifies the configuration settings for individual NDI® discovery servers. A maximum of 3 servers is allowed.

## Syntax
<a name="aws-properties-mediaconnect-flow-ndidiscoveryserverconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-flow-ndidiscoveryserverconfig-syntax.json"></a>

```
{
  "[DiscoveryServerAddress](#cfn-mediaconnect-flow-ndidiscoveryserverconfig-discoveryserveraddress)" : {{String}},
  "[DiscoveryServerPort](#cfn-mediaconnect-flow-ndidiscoveryserverconfig-discoveryserverport)" : {{Integer}},
  "[VpcInterfaceAdapter](#cfn-mediaconnect-flow-ndidiscoveryserverconfig-vpcinterfaceadapter)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-flow-ndidiscoveryserverconfig-syntax.yaml"></a>

```
  [DiscoveryServerAddress](#cfn-mediaconnect-flow-ndidiscoveryserverconfig-discoveryserveraddress): {{String}}
  [DiscoveryServerPort](#cfn-mediaconnect-flow-ndidiscoveryserverconfig-discoveryserverport): {{Integer}}
  [VpcInterfaceAdapter](#cfn-mediaconnect-flow-ndidiscoveryserverconfig-vpcinterfaceadapter): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-flow-ndidiscoveryserverconfig-properties"></a>

`DiscoveryServerAddress`  <a name="cfn-mediaconnect-flow-ndidiscoveryserverconfig-discoveryserveraddress"></a>
The unique network address of the NDI discovery server.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DiscoveryServerPort`  <a name="cfn-mediaconnect-flow-ndidiscoveryserverconfig-discoveryserverport"></a>
The port for the NDI discovery server. Defaults to 5959 if a custom port isn't specified.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcInterfaceAdapter`  <a name="cfn-mediaconnect-flow-ndidiscoveryserverconfig-vpcinterfaceadapter"></a>
The identifier for the Virtual Private Cloud (VPC) network interface used by the flow.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
