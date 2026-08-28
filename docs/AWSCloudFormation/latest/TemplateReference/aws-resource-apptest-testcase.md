---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apptest-testcase.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppTest::TestCase
<a name="aws-resource-apptest-testcase"></a>

Creates a test case for an application.

For more information about test cases, see [Test cases](https://docs.aws.amazon.com/m2/latest/userguide/testing-test-cases.html) and [Application Testing concepts](https://docs.aws.amazon.com/m2/latest/userguide/concepts-apptest.html) in the *AWS Mainframe Modernization User Guide*.

## Syntax
<a name="aws-resource-apptest-testcase-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-apptest-testcase-syntax.json"></a>

```
{
  "Type" : "AWS::AppTest::TestCase",
  "Properties" : {
      "[Description](#cfn-apptest-testcase-description)" : {{String}},
      "[Name](#cfn-apptest-testcase-name)" : {{String}},
      "[Steps](#cfn-apptest-testcase-steps)" : {{[ Step, ... ]}},
      "[Tags](#cfn-apptest-testcase-tags)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-apptest-testcase-syntax.yaml"></a>

```
Type: AWS::AppTest::TestCase
Properties:
  [Description](#cfn-apptest-testcase-description): {{String}}
  [Name](#cfn-apptest-testcase-name): {{String}}
  [Steps](#cfn-apptest-testcase-steps): {{
    - Step}}
  [Tags](#cfn-apptest-testcase-tags): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-apptest-testcase-properties"></a>

`Description`  <a name="cfn-apptest-testcase-description"></a>
The description of the test case.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-apptest-testcase-name"></a>
The name of the test case.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z][A-Za-z0-9_\-]{1,59}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Steps`  <a name="cfn-apptest-testcase-steps"></a>
The steps in the test case.
*Required*: Yes
*Type*: Array of [Step](aws-properties-apptest-testcase-step.md)
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-apptest-testcase-tags"></a>
The specified tags of the test case.
*Required*: No
*Type*: Object of String
*Pattern*: `^(?!aws:).+$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-apptest-testcase-return-values"></a>

### Ref
<a name="aws-resource-apptest-testcase-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the test case Amazon Resource Name (ARN), such as the following:

 `{ "Ref": "SampleTestCase" }`

Returns a value similar to the following:

 `arn:aws:apptest:us-east-1:123456789012:testcase/y3ca6bhaife2bcvxar3lpivfou`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-apptest-testcase-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-apptest-testcase-return-values-fn--getatt-fn--getatt"></a>

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
The creation time of the test case.

`LastUpdateTime`  <a name="LastUpdateTime-fn::getatt"></a>
The last update time of the test case.

`Status`  <a name="Status-fn::getatt"></a>
The status of the test case.

`TestCaseArn`  <a name="TestCaseArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the test case.

`TestCaseId`  <a name="TestCaseId-fn::getatt"></a>
The response test case ID of the test case.

`TestCaseVersion`  <a name="TestCaseVersion-fn::getatt"></a>
The version of the test case.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
