---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-connect-predefinedattribute.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::PredefinedAttribute
<a name="aws-resource-connect-predefinedattribute"></a>

Textual or numeric value that describes an attribute.

## Syntax
<a name="aws-resource-connect-predefinedattribute-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-connect-predefinedattribute-syntax.json"></a>

```
{
  "Type" : "AWS::Connect::PredefinedAttribute",
  "Properties" : {
      "[AttributeConfiguration](#cfn-connect-predefinedattribute-attributeconfiguration)" : {{AttributeConfiguration}},
      "[InstanceArn](#cfn-connect-predefinedattribute-instancearn)" : {{String}},
      "[Name](#cfn-connect-predefinedattribute-name)" : {{String}},
      "[Purposes](#cfn-connect-predefinedattribute-purposes)" : {{[ String, ... ]}},
      "[Values](#cfn-connect-predefinedattribute-values)" : {{Values}}
    }
}
```

### YAML
<a name="aws-resource-connect-predefinedattribute-syntax.yaml"></a>

```
Type: AWS::Connect::PredefinedAttribute
Properties:
  [AttributeConfiguration](#cfn-connect-predefinedattribute-attributeconfiguration): {{
    AttributeConfiguration}}
  [InstanceArn](#cfn-connect-predefinedattribute-instancearn): {{String}}
  [Name](#cfn-connect-predefinedattribute-name): {{String}}
  [Purposes](#cfn-connect-predefinedattribute-purposes): {{
    - String}}
  [Values](#cfn-connect-predefinedattribute-values): {{
    Values}}
```

## Properties
<a name="aws-resource-connect-predefinedattribute-properties"></a>

`AttributeConfiguration`  <a name="cfn-connect-predefinedattribute-attributeconfiguration"></a>
Custom metadata that is associated to predefined attributes to control behavior in upstream services, such as controlling how a predefined attribute should be displayed in the Connect Customer admin website.
*Required*: No
*Type*: [AttributeConfiguration](aws-properties-connect-predefinedattribute-attributeconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceArn`  <a name="cfn-connect-predefinedattribute-instancearn"></a>
The Amazon Resource Name (ARN) of the instance.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-connect-predefinedattribute-name"></a>
The name of the predefined attribute.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Purposes`  <a name="cfn-connect-predefinedattribute-purposes"></a>
Values that enable you to categorize your predefined attributes. You can use them in custom UI elements across the Connect Customer admin website.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-connect-predefinedattribute-values"></a>
The values of a predefined attribute.
*Required*: No
*Type*: [Values](aws-properties-connect-predefinedattribute-values.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-connect-predefinedattribute-return-values"></a>

### Ref
<a name="aws-resource-connect-predefinedattribute-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the predefined attribute. For example:

 `{ "Ref": "myPredefinedAttribute" }`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-connect-predefinedattribute-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-connect-predefinedattribute-return-values-fn--getatt-fn--getatt"></a>

`LastModifiedRegion`  <a name="LastModifiedRegion-fn::getatt"></a>
Last modified region.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
Last modified time.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
