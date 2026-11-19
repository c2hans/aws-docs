---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-transitgatewaypeeringattachment-transitgatewaypeeringattachmentoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::TransitGatewayPeeringAttachment TransitGatewayPeeringAttachmentOptions

Describes whether dynamic routing is enabled or disabled for the transit gateway peering request.

## Syntax
<a name="aws-properties-ec2-transitgatewaypeeringattachment-transitgatewaypeeringattachmentoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-transitgatewaypeeringattachment-transitgatewaypeeringattachmentoptions-syntax.json"></a>

```
{
  "[AllowMultipathResilience](#cfn-ec2-transitgatewaypeeringattachment-transitgatewaypeeringattachmentoptions-allowmultipathresilience)" : {{Boolean}},
  "[MultipathResilienceMode](#cfn-ec2-transitgatewaypeeringattachment-transitgatewaypeeringattachmentoptions-multipathresiliencemode)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-transitgatewaypeeringattachment-transitgatewaypeeringattachmentoptions-syntax.yaml"></a>

```
  [AllowMultipathResilience](#cfn-ec2-transitgatewaypeeringattachment-transitgatewaypeeringattachmentoptions-allowmultipathresilience): {{Boolean}}
  [MultipathResilienceMode](#cfn-ec2-transitgatewaypeeringattachment-transitgatewaypeeringattachmentoptions-multipathresiliencemode): {{String}}
```

## Properties
<a name="aws-properties-ec2-transitgatewaypeeringattachment-transitgatewaypeeringattachmentoptions-properties"></a>

`AllowMultipathResilience`  <a name="cfn-ec2-transitgatewaypeeringattachment-transitgatewaypeeringattachmentoptions-allowmultipathresilience"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MultipathResilienceMode`  <a name="cfn-ec2-transitgatewaypeeringattachment-transitgatewaypeeringattachmentoptions-multipathresiliencemode"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `always-on`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
