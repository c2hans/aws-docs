---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lightsail-container-portinfo.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lightsail::Container PortInfo
<a name="aws-properties-lightsail-container-portinfo"></a>

`PortInfo` is a property of the [Container](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-container.html) property. It describes the ports to open and the protocols to use for a container on a Amazon Lightsail container service.

## Syntax
<a name="aws-properties-lightsail-container-portinfo-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lightsail-container-portinfo-syntax.json"></a>

```
{
  "[Port](#cfn-lightsail-container-portinfo-port)" : {{String}},
  "[Protocol](#cfn-lightsail-container-portinfo-protocol)" : {{String}}
}
```

### YAML
<a name="aws-properties-lightsail-container-portinfo-syntax.yaml"></a>

```
  [Port](#cfn-lightsail-container-portinfo-port): {{String}}
  [Protocol](#cfn-lightsail-container-portinfo-protocol): {{String}}
```

## Properties
<a name="aws-properties-lightsail-container-portinfo-properties"></a>

`Port`  <a name="cfn-lightsail-container-portinfo-port"></a>
The open firewall ports of the container.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Protocol`  <a name="cfn-lightsail-container-portinfo-protocol"></a>
The protocol name for the open ports.
*Allowed values*: `HTTP` \| `HTTPS` \| `TCP` \| `UDP`
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
