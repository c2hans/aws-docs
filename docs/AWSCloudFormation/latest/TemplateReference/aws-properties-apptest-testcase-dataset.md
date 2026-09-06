---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apptest-testcase-dataset.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppTest::TestCase DataSet
<a name="aws-properties-apptest-testcase-dataset"></a>

Defines a data set.

## Syntax
<a name="aws-properties-apptest-testcase-dataset-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apptest-testcase-dataset-syntax.json"></a>

```
{
  "[Ccsid](#cfn-apptest-testcase-dataset-ccsid)" : {{String}},
  "[Format](#cfn-apptest-testcase-dataset-format)" : {{String}},
  "[Length](#cfn-apptest-testcase-dataset-length)" : {{Number}},
  "[Name](#cfn-apptest-testcase-dataset-name)" : {{String}},
  "[Type](#cfn-apptest-testcase-dataset-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-apptest-testcase-dataset-syntax.yaml"></a>

```
  [Ccsid](#cfn-apptest-testcase-dataset-ccsid): {{String}}
  [Format](#cfn-apptest-testcase-dataset-format): {{String}}
  [Length](#cfn-apptest-testcase-dataset-length): {{Number}}
  [Name](#cfn-apptest-testcase-dataset-name): {{String}}
  [Type](#cfn-apptest-testcase-dataset-type): {{String}}
```

## Properties
<a name="aws-properties-apptest-testcase-dataset-properties"></a>

`Ccsid`  <a name="cfn-apptest-testcase-dataset-ccsid"></a>
The CCSID of the data set.
*Required*: Yes
*Type*: String
*Pattern*: `^\S{1,50}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Format`  <a name="cfn-apptest-testcase-dataset-format"></a>
The format of the data set.
*Required*: Yes
*Type*: String
*Allowed values*: `FIXED | VARIABLE | LINE_SEQUENTIAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Length`  <a name="cfn-apptest-testcase-dataset-length"></a>
The length of the data set.
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-apptest-testcase-dataset-name"></a>
The name of the data set.
*Required*: Yes
*Type*: String
*Pattern*: `^\S{1,100}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-apptest-testcase-dataset-type"></a>
The type of the data set.
*Required*: Yes
*Type*: String
*Allowed values*: `PS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
