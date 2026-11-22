---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-networkconnector-elasticipconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::NetworkConnector ElasticIpConfiguration

Specifies whether Lambda assigns an Elastic IP address to each of the network connector's elastic network interfaces (ENIs).

When you specify `ServiceManaged`, Lambda allocates a service-managed Elastic IP address in your account for each ENI and associates it with that ENI. Outbound traffic from a public subnet then reaches the internet through that address. Each address stays the same for the life of its ENI. ENIs that Lambda creates later, for example after an update, get new addresses. Lambda releases the address when it deletes the ENI. The connector's operator role must allow the `ec2:AllocateAddress` and `ec2:AssociateAddress` actions on Elastic IP addresses and on the connector's ENIs.

If you don't specify an Elastic IP configuration, no Elastic IP address is assigned. When you update this configuration, the change applies to the ENIs of the new connector version.

## Syntax
<a name="aws-properties-lambda-networkconnector-elasticipconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-networkconnector-elasticipconfiguration-syntax.json"></a>

```json
{
  "[Type](#cfn-lambda-networkconnector-elasticipconfiguration-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-lambda-networkconnector-elasticipconfiguration-syntax.yaml"></a>

```yaml
  [Type](#cfn-lambda-networkconnector-elasticipconfiguration-type): {{String}}
```

## Properties
<a name="aws-properties-lambda-networkconnector-elasticipconfiguration-properties"></a>

`Type`  <a name="cfn-lambda-networkconnector-elasticipconfiguration-type"></a>
The Elastic IP address type for the connector's ENIs:
+ `None` – Lambda doesn't assign an Elastic IP address.
+ `ServiceManaged` – Lambda assigns a service-managed Elastic IP address to each ENI.
*Required*: Yes
*Type*: String
*Allowed values*: `None | ServiceManaged`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
