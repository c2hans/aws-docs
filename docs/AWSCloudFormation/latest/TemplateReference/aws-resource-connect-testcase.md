---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-connect-testcase.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::TestCase
<a name="aws-resource-connect-testcase"></a>

Creates a test case with its content and metadata for the specified Amazon Connect instance.

## Syntax
<a name="aws-resource-connect-testcase-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-connect-testcase-syntax.json"></a>

```
{
  "Type" : "AWS::Connect::TestCase",
  "Properties" : {
      "[Content](#cfn-connect-testcase-content)" : {{String}},
      "[Description](#cfn-connect-testcase-description)" : {{String}},
      "[EntryPoint](#cfn-connect-testcase-entrypoint)" : {{EntryPoint}},
      "[InitializationData](#cfn-connect-testcase-initializationdata)" : {{String}},
      "[InstanceArn](#cfn-connect-testcase-instancearn)" : {{String}},
      "[Name](#cfn-connect-testcase-name)" : {{String}},
      "[Status](#cfn-connect-testcase-status)" : {{String}},
      "[Tags](#cfn-connect-testcase-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-connect-testcase-syntax.yaml"></a>

```
Type: AWS::Connect::TestCase
Properties:
  [Content](#cfn-connect-testcase-content): {{String}}
  [Description](#cfn-connect-testcase-description): {{String}}
  [EntryPoint](#cfn-connect-testcase-entrypoint): {{
    EntryPoint}}
  [InitializationData](#cfn-connect-testcase-initializationdata): {{String}}
  [InstanceArn](#cfn-connect-testcase-instancearn): {{String}}
  [Name](#cfn-connect-testcase-name): {{String}}
  [Status](#cfn-connect-testcase-status): {{String}}
  [Tags](#cfn-connect-testcase-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-connect-testcase-properties"></a>

`Content`  <a name="cfn-connect-testcase-content"></a>
The JSON string that represents the content of the test.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-connect-testcase-description"></a>
The description of the test case.
*Required*: No
*Type*: String
*Pattern*: `.*\S.*`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EntryPoint`  <a name="cfn-connect-testcase-entrypoint"></a>
Defines the starting point for the test, including channel type and parameters.
*Required*: No
*Type*: [EntryPoint](aws-properties-connect-testcase-entrypoint.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InitializationData`  <a name="cfn-connect-testcase-initializationdata"></a>
Defines the test attributes for precise data representation. The value must be a valid JSON string.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceArn`  <a name="cfn-connect-testcase-instancearn"></a>
The Amazon Resource Name (ARN) of the instance.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-connect-testcase-name"></a>
The name of the test case.
*Required*: Yes
*Type*: String
*Pattern*: `.*\S.*`
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-connect-testcase-status"></a>
Indicates the test status as either SAVED or PUBLISHED.
*Required*: No
*Type*: String
*Allowed values*: `SAVED | PUBLISHED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-connect-testcase-tags"></a>
The tags used to organize, track, or control access for this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-connect-testcase-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-connect-testcase-return-values"></a>

### Ref
<a name="aws-resource-connect-testcase-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-connect-testcase-return-values-fn--getatt"></a>

####
<a name="aws-resource-connect-testcase-return-values-fn--getatt-fn--getatt"></a>

`LastModifiedRegion`  <a name="LastModifiedRegion-fn::getatt"></a>
The region in which the test case was last modified.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
The time at which the test case was last modified.

`TestCaseArn`  <a name="TestCaseArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the test case.
