---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apptest-testcase-resourceaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppTest::TestCase ResourceAction
<a name="aws-properties-apptest-testcase-resourceaction"></a>

Specifies a resource action.

## Syntax
<a name="aws-properties-apptest-testcase-resourceaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apptest-testcase-resourceaction-syntax.json"></a>

```
{
  "[CloudFormationAction](#cfn-apptest-testcase-resourceaction-cloudformationaction)" : {{CloudFormationAction}},
  "[M2ManagedApplicationAction](#cfn-apptest-testcase-resourceaction-m2managedapplicationaction)" : {{M2ManagedApplicationAction}},
  "[M2NonManagedApplicationAction](#cfn-apptest-testcase-resourceaction-m2nonmanagedapplicationaction)" : {{M2NonManagedApplicationAction}}
}
```

### YAML
<a name="aws-properties-apptest-testcase-resourceaction-syntax.yaml"></a>

```
  [CloudFormationAction](#cfn-apptest-testcase-resourceaction-cloudformationaction): {{
    CloudFormationAction}}
  [M2ManagedApplicationAction](#cfn-apptest-testcase-resourceaction-m2managedapplicationaction): {{
    M2ManagedApplicationAction}}
  [M2NonManagedApplicationAction](#cfn-apptest-testcase-resourceaction-m2nonmanagedapplicationaction): {{
    M2NonManagedApplicationAction}}
```

## Properties
<a name="aws-properties-apptest-testcase-resourceaction-properties"></a>

`CloudFormationAction`  <a name="cfn-apptest-testcase-resourceaction-cloudformationaction"></a>
The CloudFormation action of the resource action.
*Required*: No
*Type*: [CloudFormationAction](aws-properties-apptest-testcase-cloudformationaction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`M2ManagedApplicationAction`  <a name="cfn-apptest-testcase-resourceaction-m2managedapplicationaction"></a>
The AWS Mainframe Modernization managed application action of the resource action.
*Required*: No
*Type*: [M2ManagedApplicationAction](aws-properties-apptest-testcase-m2managedapplicationaction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`M2NonManagedApplicationAction`  <a name="cfn-apptest-testcase-resourceaction-m2nonmanagedapplicationaction"></a>
The AWS Mainframe Modernization non-managed application action of the resource action.
*Required*: No
*Type*: [M2NonManagedApplicationAction](aws-properties-apptest-testcase-m2nonmanagedapplicationaction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
