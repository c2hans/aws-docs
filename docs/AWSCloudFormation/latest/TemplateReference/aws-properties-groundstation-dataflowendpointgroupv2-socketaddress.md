---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-groundstation-dataflowendpointgroupv2-socketaddress.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GroundStation::DataflowEndpointGroupV2 SocketAddress
<a name="aws-properties-groundstation-dataflowendpointgroupv2-socketaddress"></a>

Information about the socket address.

## Syntax
<a name="aws-properties-groundstation-dataflowendpointgroupv2-socketaddress-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-groundstation-dataflowendpointgroupv2-socketaddress-syntax.json"></a>

```
{
  "[Name](#cfn-groundstation-dataflowendpointgroupv2-socketaddress-name)" : {{String}},
  "[Port](#cfn-groundstation-dataflowendpointgroupv2-socketaddress-port)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-groundstation-dataflowendpointgroupv2-socketaddress-syntax.yaml"></a>

```
  [Name](#cfn-groundstation-dataflowendpointgroupv2-socketaddress-name): {{String}}
  [Port](#cfn-groundstation-dataflowendpointgroupv2-socketaddress-port): {{Integer}}
```

## Properties
<a name="aws-properties-groundstation-dataflowendpointgroupv2-socketaddress-properties"></a>

`Name`  <a name="cfn-groundstation-dataflowendpointgroupv2-socketaddress-name"></a>
Name of a socket address.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Port`  <a name="cfn-groundstation-dataflowendpointgroupv2-socketaddress-port"></a>
Port of a socket address.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
