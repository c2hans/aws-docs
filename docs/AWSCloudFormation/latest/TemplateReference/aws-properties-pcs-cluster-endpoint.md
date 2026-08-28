---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pcs-cluster-endpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PCS::Cluster Endpoint
<a name="aws-properties-pcs-cluster-endpoint"></a>

An endpoint available for interaction with the scheduler.

## Syntax
<a name="aws-properties-pcs-cluster-endpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pcs-cluster-endpoint-syntax.json"></a>

```
{
  "[Ipv6Address](#cfn-pcs-cluster-endpoint-ipv6address)" : {{String}},
  "[Port](#cfn-pcs-cluster-endpoint-port)" : {{String}},
  "[PrivateIpAddress](#cfn-pcs-cluster-endpoint-privateipaddress)" : {{String}},
  "[PublicIpAddress](#cfn-pcs-cluster-endpoint-publicipaddress)" : {{String}},
  "[Type](#cfn-pcs-cluster-endpoint-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-pcs-cluster-endpoint-syntax.yaml"></a>

```
  [Ipv6Address](#cfn-pcs-cluster-endpoint-ipv6address): {{String}}
  [Port](#cfn-pcs-cluster-endpoint-port): {{String}}
  [PrivateIpAddress](#cfn-pcs-cluster-endpoint-privateipaddress): {{String}}
  [PublicIpAddress](#cfn-pcs-cluster-endpoint-publicipaddress): {{String}}
  [Type](#cfn-pcs-cluster-endpoint-type): {{String}}
```

## Properties
<a name="aws-properties-pcs-cluster-endpoint-properties"></a>

`Ipv6Address`  <a name="cfn-pcs-cluster-endpoint-ipv6address"></a>
The endpoint's IPv6 address.
Example: `2001:db8::1`
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Port`  <a name="cfn-pcs-cluster-endpoint-port"></a>
The endpoint's connection port number.
 Example: `1234`
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrivateIpAddress`  <a name="cfn-pcs-cluster-endpoint-privateipaddress"></a>
For clusters that use IPv4, this is the endpoint's private IP address.
Example: `10.1.2.3`
For clusters configured to use IPv6, this is an empty string.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PublicIpAddress`  <a name="cfn-pcs-cluster-endpoint-publicipaddress"></a>
The endpoint's public IP address.
Example: `192.0.2.1`
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-pcs-cluster-endpoint-type"></a>
Indicates the type of endpoint running at the specific IP address.
*Required*: Yes
*Type*: String
*Allowed values*: `SLURMCTLD | SLURMDBD | SLURMRESTD`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
