---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-instanceconnectendpoint-instanceconnectendpointpublicdnsnames.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::InstanceConnectEndpoint InstanceConnectEndpointPublicDnsNames
<a name="aws-properties-ec2-instanceconnectendpoint-instanceconnectendpointpublicdnsnames"></a>

The public DNS names of the endpoint, including IPv4-only and dualstack DNS names.

## Syntax
<a name="aws-properties-ec2-instanceconnectendpoint-instanceconnectendpointpublicdnsnames-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-instanceconnectendpoint-instanceconnectendpointpublicdnsnames-syntax.json"></a>

```
{
  "[Dualstack](#cfn-ec2-instanceconnectendpoint-instanceconnectendpointpublicdnsnames-dualstack)" : {{InstanceConnectEndpointDnsNames}},
  "[Ipv4](#cfn-ec2-instanceconnectendpoint-instanceconnectendpointpublicdnsnames-ipv4)" : {{InstanceConnectEndpointDnsNames}}
}
```

### YAML
<a name="aws-properties-ec2-instanceconnectendpoint-instanceconnectendpointpublicdnsnames-syntax.yaml"></a>

```
  [Dualstack](#cfn-ec2-instanceconnectendpoint-instanceconnectendpointpublicdnsnames-dualstack): {{
    InstanceConnectEndpointDnsNames}}
  [Ipv4](#cfn-ec2-instanceconnectendpoint-instanceconnectendpointpublicdnsnames-ipv4): {{
    InstanceConnectEndpointDnsNames}}
```

## Properties
<a name="aws-properties-ec2-instanceconnectendpoint-instanceconnectendpointpublicdnsnames-properties"></a>

`Dualstack`  <a name="cfn-ec2-instanceconnectendpoint-instanceconnectendpointpublicdnsnames-dualstack"></a>
The dualstack DNS name of the EC2 Instance Connect Endpoint. A dualstack DNS name supports connections from both IPv4 and IPv6 clients.
*Required*: No
*Type*: [InstanceConnectEndpointDnsNames](aws-properties-ec2-instanceconnectendpoint-instanceconnectendpointdnsnames.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ipv4`  <a name="cfn-ec2-instanceconnectendpoint-instanceconnectendpointpublicdnsnames-ipv4"></a>
The IPv4-only DNS name of the EC2 Instance Connect Endpoint.
*Required*: No
*Type*: [InstanceConnectEndpointDnsNames](aws-properties-ec2-instanceconnectendpoint-instanceconnectendpointdnsnames.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
