---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apptest-testcase-m2nonmanagedapplicationaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppTest::TestCase M2NonManagedApplicationAction
<a name="aws-properties-apptest-testcase-m2nonmanagedapplicationaction"></a>

Specifies the AWS Mainframe Modernization non-managed application action.

## Syntax
<a name="aws-properties-apptest-testcase-m2nonmanagedapplicationaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apptest-testcase-m2nonmanagedapplicationaction-syntax.json"></a>

```
{
  "[ActionType](#cfn-apptest-testcase-m2nonmanagedapplicationaction-actiontype)" : {{String}},
  "[Resource](#cfn-apptest-testcase-m2nonmanagedapplicationaction-resource)" : {{String}}
}
```

### YAML
<a name="aws-properties-apptest-testcase-m2nonmanagedapplicationaction-syntax.yaml"></a>

```
  [ActionType](#cfn-apptest-testcase-m2nonmanagedapplicationaction-actiontype): {{String}}
  [Resource](#cfn-apptest-testcase-m2nonmanagedapplicationaction-resource): {{String}}
```

## Properties
<a name="aws-properties-apptest-testcase-m2nonmanagedapplicationaction-properties"></a>

`ActionType`  <a name="cfn-apptest-testcase-m2nonmanagedapplicationaction-actiontype"></a>
The action type of the AWS Mainframe Modernization non-managed application action.
*Required*: Yes
*Type*: String
*Allowed values*: `Configure | Deconfigure`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Resource`  <a name="cfn-apptest-testcase-m2nonmanagedapplicationaction-resource"></a>
The resource of the AWS Mainframe Modernization non-managed application action.
*Required*: Yes
*Type*: String
*Pattern*: `^\S{1,1000}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
