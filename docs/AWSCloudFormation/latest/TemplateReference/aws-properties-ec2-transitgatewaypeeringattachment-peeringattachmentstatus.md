---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-transitgatewaypeeringattachment-peeringattachmentstatus.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::TransitGatewayPeeringAttachment PeeringAttachmentStatus
<a name="aws-properties-ec2-transitgatewaypeeringattachment-peeringattachmentstatus"></a>

The status of the transit gateway peering attachment.

## Syntax
<a name="aws-properties-ec2-transitgatewaypeeringattachment-peeringattachmentstatus-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-transitgatewaypeeringattachment-peeringattachmentstatus-syntax.json"></a>

```
{
  "[Code](#cfn-ec2-transitgatewaypeeringattachment-peeringattachmentstatus-code)" : {{String}},
  "[Message](#cfn-ec2-transitgatewaypeeringattachment-peeringattachmentstatus-message)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-transitgatewaypeeringattachment-peeringattachmentstatus-syntax.yaml"></a>

```
  [Code](#cfn-ec2-transitgatewaypeeringattachment-peeringattachmentstatus-code): {{String}}
  [Message](#cfn-ec2-transitgatewaypeeringattachment-peeringattachmentstatus-message): {{String}}
```

## Properties
<a name="aws-properties-ec2-transitgatewaypeeringattachment-peeringattachmentstatus-properties"></a>

`Code`  <a name="cfn-ec2-transitgatewaypeeringattachment-peeringattachmentstatus-code"></a>
The status code.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Message`  <a name="cfn-ec2-transitgatewaypeeringattachment-peeringattachmentstatus-message"></a>
The status message, if applicable.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
