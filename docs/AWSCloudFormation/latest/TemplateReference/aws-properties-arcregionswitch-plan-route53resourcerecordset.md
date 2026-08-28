---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-arcregionswitch-plan-route53resourcerecordset.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ARCRegionSwitch::Plan Route53ResourceRecordSet
<a name="aws-properties-arcregionswitch-plan-route53resourcerecordset"></a>

The Amazon Route 53 record set.

## Syntax
<a name="aws-properties-arcregionswitch-plan-route53resourcerecordset-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-arcregionswitch-plan-route53resourcerecordset-syntax.json"></a>

```
{
  "[RecordSetIdentifier](#cfn-arcregionswitch-plan-route53resourcerecordset-recordsetidentifier)" : {{String}},
  "[Region](#cfn-arcregionswitch-plan-route53resourcerecordset-region)" : {{String}}
}
```

### YAML
<a name="aws-properties-arcregionswitch-plan-route53resourcerecordset-syntax.yaml"></a>

```
  [RecordSetIdentifier](#cfn-arcregionswitch-plan-route53resourcerecordset-recordsetidentifier): {{String}}
  [Region](#cfn-arcregionswitch-plan-route53resourcerecordset-region): {{String}}
```

## Properties
<a name="aws-properties-arcregionswitch-plan-route53resourcerecordset-properties"></a>

`RecordSetIdentifier`  <a name="cfn-arcregionswitch-plan-route53resourcerecordset-recordsetidentifier"></a>
The Amazon Route 53 record set identifier.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Region`  <a name="cfn-arcregionswitch-plan-route53resourcerecordset-region"></a>
The Amazon Route 53 record set Region.
*Required*: No
*Type*: String
*Pattern*: `^[a-z]{2}-[a-z-]+-\d+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
