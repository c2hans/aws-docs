---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-vpcconnection-networkinterface.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::VPCConnection NetworkInterface
<a name="aws-properties-quicksight-vpcconnection-networkinterface"></a>

The structure that contains information about a network interface.

## Syntax
<a name="aws-properties-quicksight-vpcconnection-networkinterface-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-vpcconnection-networkinterface-syntax.json"></a>

```
{
  "[AvailabilityZone](#cfn-quicksight-vpcconnection-networkinterface-availabilityzone)" : {{String}},
  "[ErrorMessage](#cfn-quicksight-vpcconnection-networkinterface-errormessage)" : {{String}},
  "[NetworkInterfaceId](#cfn-quicksight-vpcconnection-networkinterface-networkinterfaceid)" : {{String}},
  "[Status](#cfn-quicksight-vpcconnection-networkinterface-status)" : {{String}},
  "[SubnetId](#cfn-quicksight-vpcconnection-networkinterface-subnetid)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-vpcconnection-networkinterface-syntax.yaml"></a>

```
  [AvailabilityZone](#cfn-quicksight-vpcconnection-networkinterface-availabilityzone): {{String}}
  [ErrorMessage](#cfn-quicksight-vpcconnection-networkinterface-errormessage): {{String}}
  [NetworkInterfaceId](#cfn-quicksight-vpcconnection-networkinterface-networkinterfaceid): {{String}}
  [Status](#cfn-quicksight-vpcconnection-networkinterface-status): {{String}}
  [SubnetId](#cfn-quicksight-vpcconnection-networkinterface-subnetid): {{String}}
```

## Properties
<a name="aws-properties-quicksight-vpcconnection-networkinterface-properties"></a>

`AvailabilityZone`  <a name="cfn-quicksight-vpcconnection-networkinterface-availabilityzone"></a>
The availability zone that the network interface resides in.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ErrorMessage`  <a name="cfn-quicksight-vpcconnection-networkinterface-errormessage"></a>
An error message.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkInterfaceId`  <a name="cfn-quicksight-vpcconnection-networkinterface-networkinterfaceid"></a>
The network interface ID.
*Required*: No
*Type*: String
*Pattern*: `^eni-[0-9a-z]*$`
*Minimum*: `0`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-quicksight-vpcconnection-networkinterface-status"></a>
The status of the network interface.
*Required*: No
*Type*: String
*Allowed values*: `CREATING | AVAILABLE | CREATION_FAILED | UPDATING | UPDATE_FAILED | DELETING | DELETED | DELETION_FAILED | DELETION_SCHEDULED | ATTACHMENT_FAILED_ROLLBACK_FAILED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubnetId`  <a name="cfn-quicksight-vpcconnection-networkinterface-subnetid"></a>
The subnet ID associated with the network interface.
*Required*: No
*Type*: String
*Pattern*: `^subnet-[0-9a-z]*$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
