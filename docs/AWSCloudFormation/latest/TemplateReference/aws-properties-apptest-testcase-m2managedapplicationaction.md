---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apptest-testcase-m2managedapplicationaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppTest::TestCase M2ManagedApplicationAction
<a name="aws-properties-apptest-testcase-m2managedapplicationaction"></a>

Specifies the AWS Mainframe Modernization managed application action.

## Syntax
<a name="aws-properties-apptest-testcase-m2managedapplicationaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apptest-testcase-m2managedapplicationaction-syntax.json"></a>

```
{
  "[ActionType](#cfn-apptest-testcase-m2managedapplicationaction-actiontype)" : {{String}},
  "[Properties](#cfn-apptest-testcase-m2managedapplicationaction-properties)" : {{M2ManagedActionProperties}},
  "[Resource](#cfn-apptest-testcase-m2managedapplicationaction-resource)" : {{String}}
}
```

### YAML
<a name="aws-properties-apptest-testcase-m2managedapplicationaction-syntax.yaml"></a>

```
  [ActionType](#cfn-apptest-testcase-m2managedapplicationaction-actiontype): {{String}}
  [Properties](#cfn-apptest-testcase-m2managedapplicationaction-properties): {{
    M2ManagedActionProperties}}
  [Resource](#cfn-apptest-testcase-m2managedapplicationaction-resource): {{String}}
```

## Properties
<a name="aws-properties-apptest-testcase-m2managedapplicationaction-properties"></a>

`ActionType`  <a name="cfn-apptest-testcase-m2managedapplicationaction-actiontype"></a>
The action type of the AWS Mainframe Modernization managed application action.
*Required*: Yes
*Type*: String
*Allowed values*: `Configure | Deconfigure`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Properties`  <a name="cfn-apptest-testcase-m2managedapplicationaction-properties"></a>
The properties of the AWS Mainframe Modernization managed application action.
*Required*: No
*Type*: [M2ManagedActionProperties](aws-properties-apptest-testcase-m2managedactionproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Resource`  <a name="cfn-apptest-testcase-m2managedapplicationaction-resource"></a>
The resource of the AWS Mainframe Modernization managed application action.
*Required*: Yes
*Type*: String
*Pattern*: `^\S{1,1000}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
