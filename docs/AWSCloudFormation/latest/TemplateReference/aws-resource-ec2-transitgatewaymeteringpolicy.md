---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-transitgatewaymeteringpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::TransitGatewayMeteringPolicy
<a name="aws-resource-ec2-transitgatewaymeteringpolicy"></a>

Describes a transit gateway metering policy.

## Syntax
<a name="aws-resource-ec2-transitgatewaymeteringpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-transitgatewaymeteringpolicy-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::TransitGatewayMeteringPolicy",
  "Properties" : {
      "[MiddleboxAttachmentIds](#cfn-ec2-transitgatewaymeteringpolicy-middleboxattachmentids)" : {{[ String, ... ]}},
      "[Tags](#cfn-ec2-transitgatewaymeteringpolicy-tags)" : {{[ Tag, ... ]}},
      "[TransitGatewayId](#cfn-ec2-transitgatewaymeteringpolicy-transitgatewayid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ec2-transitgatewaymeteringpolicy-syntax.yaml"></a>

```
Type: AWS::EC2::TransitGatewayMeteringPolicy
Properties:
  [MiddleboxAttachmentIds](#cfn-ec2-transitgatewaymeteringpolicy-middleboxattachmentids): {{
    - String}}
  [Tags](#cfn-ec2-transitgatewaymeteringpolicy-tags): {{
    - Tag}}
  [TransitGatewayId](#cfn-ec2-transitgatewaymeteringpolicy-transitgatewayid): {{String}}
```

## Properties
<a name="aws-resource-ec2-transitgatewaymeteringpolicy-properties"></a>

`MiddleboxAttachmentIds`  <a name="cfn-ec2-transitgatewaymeteringpolicy-middleboxattachmentids"></a>
The IDs of the middlebox attachments associated with the metering policy.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-ec2-transitgatewaymeteringpolicy-tags"></a>
The tags assigned to the transit gateway metering policy.
*Required*: No
*Type*: Array of [Tag](aws-properties-ec2-transitgatewaymeteringpolicy-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TransitGatewayId`  <a name="cfn-ec2-transitgatewaymeteringpolicy-transitgatewayid"></a>
The ID of the transit gateway associated with the metering policy.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ec2-transitgatewaymeteringpolicy-return-values"></a>

### Ref
<a name="aws-resource-ec2-transitgatewaymeteringpolicy-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-ec2-transitgatewaymeteringpolicy-return-values-fn--getatt"></a>

####
<a name="aws-resource-ec2-transitgatewaymeteringpolicy-return-values-fn--getatt-fn--getatt"></a>

`State`  <a name="State-fn::getatt"></a>
The state of the transit gateway metering policy.

`TransitGatewayMeteringPolicyId`  <a name="TransitGatewayMeteringPolicyId-fn::getatt"></a>
The ID of the transit gateway metering policy.

`UpdateEffectiveAt`  <a name="UpdateEffectiveAt-fn::getatt"></a>
The date and time when the metering policy update becomes effective.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
