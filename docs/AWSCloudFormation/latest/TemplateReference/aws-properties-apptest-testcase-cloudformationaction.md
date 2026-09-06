---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apptest-testcase-cloudformationaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppTest::TestCase CloudFormationAction
<a name="aws-properties-apptest-testcase-cloudformationaction"></a>

Specifies the CloudFormation action.

## Syntax
<a name="aws-properties-apptest-testcase-cloudformationaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apptest-testcase-cloudformationaction-syntax.json"></a>

```
{
  "[ActionType](#cfn-apptest-testcase-cloudformationaction-actiontype)" : {{String}},
  "[Resource](#cfn-apptest-testcase-cloudformationaction-resource)" : {{String}}
}
```

### YAML
<a name="aws-properties-apptest-testcase-cloudformationaction-syntax.yaml"></a>

```
  [ActionType](#cfn-apptest-testcase-cloudformationaction-actiontype): {{String}}
  [Resource](#cfn-apptest-testcase-cloudformationaction-resource): {{String}}
```

## Properties
<a name="aws-properties-apptest-testcase-cloudformationaction-properties"></a>

`ActionType`  <a name="cfn-apptest-testcase-cloudformationaction-actiontype"></a>
The action type of the CloudFormation action.
*Required*: No
*Type*: String
*Allowed values*: `Create | Delete`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Resource`  <a name="cfn-apptest-testcase-cloudformationaction-resource"></a>
The resource of the CloudFormation action.
*Required*: Yes
*Type*: String
*Pattern*: `^\S{1,1000}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
