---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apptest-testcase-testcaselatestversion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppTest::TestCase TestCaseLatestVersion
<a name="aws-properties-apptest-testcase-testcaselatestversion"></a>

Specifies the latest version of a test case.

## Syntax
<a name="aws-properties-apptest-testcase-testcaselatestversion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apptest-testcase-testcaselatestversion-syntax.json"></a>

```
{
  "[Status](#cfn-apptest-testcase-testcaselatestversion-status)" : {{String}},
  "[Version](#cfn-apptest-testcase-testcaselatestversion-version)" : {{Number}}
}
```

### YAML
<a name="aws-properties-apptest-testcase-testcaselatestversion-syntax.yaml"></a>

```
  [Status](#cfn-apptest-testcase-testcaselatestversion-status): {{String}}
  [Version](#cfn-apptest-testcase-testcaselatestversion-version): {{Number}}
```

## Properties
<a name="aws-properties-apptest-testcase-testcaselatestversion-properties"></a>

`Status`  <a name="cfn-apptest-testcase-testcaselatestversion-status"></a>
The status of the test case latest version.
*Required*: Yes
*Type*: String
*Allowed values*: `Active | Deleting`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Version`  <a name="cfn-apptest-testcase-testcaselatestversion-version"></a>
The version of the test case latest version.
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
