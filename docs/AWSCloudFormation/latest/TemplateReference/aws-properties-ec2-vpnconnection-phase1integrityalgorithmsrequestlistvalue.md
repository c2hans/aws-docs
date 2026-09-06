---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-vpnconnection-phase1integrityalgorithmsrequestlistvalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::VPNConnection Phase1IntegrityAlgorithmsRequestListValue
<a name="aws-properties-ec2-vpnconnection-phase1integrityalgorithmsrequestlistvalue"></a>

Specifies the integrity algorithm for the VPN tunnel for phase 1 IKE negotiations.

## Syntax
<a name="aws-properties-ec2-vpnconnection-phase1integrityalgorithmsrequestlistvalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-vpnconnection-phase1integrityalgorithmsrequestlistvalue-syntax.json"></a>

```
{
  "[Value](#cfn-ec2-vpnconnection-phase1integrityalgorithmsrequestlistvalue-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-vpnconnection-phase1integrityalgorithmsrequestlistvalue-syntax.yaml"></a>

```
  [Value](#cfn-ec2-vpnconnection-phase1integrityalgorithmsrequestlistvalue-value): {{String}}
```

## Properties
<a name="aws-properties-ec2-vpnconnection-phase1integrityalgorithmsrequestlistvalue-properties"></a>

`Value`  <a name="cfn-ec2-vpnconnection-phase1integrityalgorithmsrequestlistvalue-value"></a>
The value for the integrity algorithm.
*Required*: No
*Type*: String
*Allowed values*: `SHA1 | SHA2-256 | SHA2-384 | SHA2-512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
