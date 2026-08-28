---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-arcregionswitch-plan-executionapprovalconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ARCRegionSwitch::Plan ExecutionApprovalConfiguration
<a name="aws-properties-arcregionswitch-plan-executionapprovalconfiguration"></a>

Configuration for approval steps in a Region switch plan execution. Approval steps require manual intervention before the execution can proceed.

## Syntax
<a name="aws-properties-arcregionswitch-plan-executionapprovalconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-arcregionswitch-plan-executionapprovalconfiguration-syntax.json"></a>

```
{
  "[ApprovalRole](#cfn-arcregionswitch-plan-executionapprovalconfiguration-approvalrole)" : {{String}},
  "[TimeoutMinutes](#cfn-arcregionswitch-plan-executionapprovalconfiguration-timeoutminutes)" : {{Number}}
}
```

### YAML
<a name="aws-properties-arcregionswitch-plan-executionapprovalconfiguration-syntax.yaml"></a>

```
  [ApprovalRole](#cfn-arcregionswitch-plan-executionapprovalconfiguration-approvalrole): {{String}}
  [TimeoutMinutes](#cfn-arcregionswitch-plan-executionapprovalconfiguration-timeoutminutes): {{Number}}
```

## Properties
<a name="aws-properties-arcregionswitch-plan-executionapprovalconfiguration-properties"></a>

`ApprovalRole`  <a name="cfn-arcregionswitch-plan-executionapprovalconfiguration-approvalrole"></a>
The IAM approval role for the configuration.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeoutMinutes`  <a name="cfn-arcregionswitch-plan-executionapprovalconfiguration-timeoutminutes"></a>
The timeout value specified for the configuration.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
