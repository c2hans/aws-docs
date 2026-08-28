---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-networkinterface-ipv4prefixspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::NetworkInterface Ipv4PrefixSpecification
<a name="aws-properties-ec2-networkinterface-ipv4prefixspecification"></a>

Describes an IPv4 prefix.

## Syntax
<a name="aws-properties-ec2-networkinterface-ipv4prefixspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-networkinterface-ipv4prefixspecification-syntax.json"></a>

```
{
  "[Ipv4Prefix](#cfn-ec2-networkinterface-ipv4prefixspecification-ipv4prefix)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-networkinterface-ipv4prefixspecification-syntax.yaml"></a>

```
  [Ipv4Prefix](#cfn-ec2-networkinterface-ipv4prefixspecification-ipv4prefix): {{String}}
```

## Properties
<a name="aws-properties-ec2-networkinterface-ipv4prefixspecification-properties"></a>

`Ipv4Prefix`  <a name="cfn-ec2-networkinterface-ipv4prefixspecification-ipv4prefix"></a>
The IPv4 prefix. For information, see [ Assigning prefixes to network interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-prefix-eni.html) in the *Amazon EC2 User Guide*.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
