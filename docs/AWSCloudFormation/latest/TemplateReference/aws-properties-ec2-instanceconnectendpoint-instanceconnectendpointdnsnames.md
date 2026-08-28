---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-instanceconnectendpoint-instanceconnectendpointdnsnames.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::InstanceConnectEndpoint InstanceConnectEndpointDnsNames
<a name="aws-properties-ec2-instanceconnectendpoint-instanceconnectendpointdnsnames"></a>

The DNS names of the endpoint.

## Syntax
<a name="aws-properties-ec2-instanceconnectendpoint-instanceconnectendpointdnsnames-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-instanceconnectendpoint-instanceconnectendpointdnsnames-syntax.json"></a>

```
{
  "[DnsName](#cfn-ec2-instanceconnectendpoint-instanceconnectendpointdnsnames-dnsname)" : {{String}},
  "[FipsDnsName](#cfn-ec2-instanceconnectendpoint-instanceconnectendpointdnsnames-fipsdnsname)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-instanceconnectendpoint-instanceconnectendpointdnsnames-syntax.yaml"></a>

```
  [DnsName](#cfn-ec2-instanceconnectendpoint-instanceconnectendpointdnsnames-dnsname): {{String}}
  [FipsDnsName](#cfn-ec2-instanceconnectendpoint-instanceconnectendpointdnsnames-fipsdnsname): {{String}}
```

## Properties
<a name="aws-properties-ec2-instanceconnectendpoint-instanceconnectendpointdnsnames-properties"></a>

`DnsName`  <a name="cfn-ec2-instanceconnectendpoint-instanceconnectendpointdnsnames-dnsname"></a>
The DNS name of the EC2 Instance Connect Endpoint.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FipsDnsName`  <a name="cfn-ec2-instanceconnectendpoint-instanceconnectendpointdnsnames-fipsdnsname"></a>
The Federal Information Processing Standards (FIPS) compliant DNS name of the EC2 Instance Connect Endpoint.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
