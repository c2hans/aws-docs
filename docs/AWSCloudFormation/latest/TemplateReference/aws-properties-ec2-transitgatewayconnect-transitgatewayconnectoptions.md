---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-transitgatewayconnect-transitgatewayconnectoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::TransitGatewayConnect TransitGatewayConnectOptions
<a name="aws-properties-ec2-transitgatewayconnect-transitgatewayconnectoptions"></a>

Describes the Connect attachment options.

## Syntax
<a name="aws-properties-ec2-transitgatewayconnect-transitgatewayconnectoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-transitgatewayconnect-transitgatewayconnectoptions-syntax.json"></a>

```
{
  "[Protocol](#cfn-ec2-transitgatewayconnect-transitgatewayconnectoptions-protocol)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-transitgatewayconnect-transitgatewayconnectoptions-syntax.yaml"></a>

```
  [Protocol](#cfn-ec2-transitgatewayconnect-transitgatewayconnectoptions-protocol): {{String}}
```

## Properties
<a name="aws-properties-ec2-transitgatewayconnect-transitgatewayconnectoptions-properties"></a>

`Protocol`  <a name="cfn-ec2-transitgatewayconnect-transitgatewayconnectoptions-protocol"></a>
The tunnel protocol.
*Required*: No
*Type*: String
*Allowed values*: `gre`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
