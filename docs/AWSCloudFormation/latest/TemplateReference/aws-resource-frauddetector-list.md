---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-frauddetector-list.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FraudDetector::List
<a name="aws-resource-frauddetector-list"></a>

 Creates a list.

List is a set of input data for a variable in your event dataset. You use the input data in a rule that's associated with your detector. For more information, see [Lists](https://docs.aws.amazon.com//frauddetector/latest/ug/lists.html).

## Syntax
<a name="aws-resource-frauddetector-list-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-frauddetector-list-syntax.json"></a>

```
{
  "Type" : "AWS::FraudDetector::List",
  "Properties" : {
      "[Description](#cfn-frauddetector-list-description)" : {{String}},
      "[Elements](#cfn-frauddetector-list-elements)" : {{[ String, ... ]}},
      "[Name](#cfn-frauddetector-list-name)" : {{String}},
      "[Tags](#cfn-frauddetector-list-tags)" : {{[ Tag, ... ]}},
      "[VariableType](#cfn-frauddetector-list-variabletype)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-frauddetector-list-syntax.yaml"></a>

```
Type: AWS::FraudDetector::List
Properties:
  [Description](#cfn-frauddetector-list-description): {{String}}
  [Elements](#cfn-frauddetector-list-elements): {{
    - String}}
  [Name](#cfn-frauddetector-list-name): {{String}}
  [Tags](#cfn-frauddetector-list-tags): {{
    - Tag}}
  [VariableType](#cfn-frauddetector-list-variabletype): {{String}}
```

## Properties
<a name="aws-resource-frauddetector-list-properties"></a>

`Description`  <a name="cfn-frauddetector-list-description"></a>
 The description of the list.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Elements`  <a name="cfn-frauddetector-list-elements"></a>
The elements in the list.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `100000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-frauddetector-list-name"></a>
 The name of the list.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-z_]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-frauddetector-list-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-frauddetector-list-tag.md)
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VariableType`  <a name="cfn-frauddetector-list-variabletype"></a>
 The variable type of the list. For more information, see [Variable types](https://docs.aws.amazon.com/frauddetector/latest/ug/variables.html#variable-types)
*Required*: No
*Type*: String
*Pattern*: `^[A-Z_]{1,64}$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-frauddetector-list-return-values"></a>

### Ref
<a name="aws-resource-frauddetector-list-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the primary identifier for the resource, which is the Arn.

Example: `{"Ref": "arn:aws:frauddetector:us-west-2:123123123123:outcome/outcome_name"}`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-frauddetector-list-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-frauddetector-list-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The event type ARN.

`CreatedTime`  <a name="CreatedTime-fn::getatt"></a>
Timestamp of when the list was created.

`LastUpdatedTime`  <a name="LastUpdatedTime-fn::getatt"></a>
Timestamp of when list was last updated.
