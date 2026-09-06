---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cases-field.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cases::Field
<a name="aws-resource-cases-field"></a>

Creates a field in the Cases domain. This field is used to define the case object model (that is, defines what data can be captured on cases) in a Cases domain.

## Syntax
<a name="aws-resource-cases-field-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cases-field-syntax.json"></a>

```
{
  "Type" : "AWS::Cases::Field",
  "Properties" : {
      "[Attributes](#cfn-cases-field-attributes)" : {{FieldAttributes}},
      "[Description](#cfn-cases-field-description)" : {{String}},
      "[DomainId](#cfn-cases-field-domainid)" : {{String}},
      "[Name](#cfn-cases-field-name)" : {{String}},
      "[Tags](#cfn-cases-field-tags)" : {{[ Tag, ... ]}},
      "[Type](#cfn-cases-field-type)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-cases-field-syntax.yaml"></a>

```
Type: AWS::Cases::Field
Properties:
  [Attributes](#cfn-cases-field-attributes): {{
    FieldAttributes}}
  [Description](#cfn-cases-field-description): {{String}}
  [DomainId](#cfn-cases-field-domainid): {{String}}
  [Name](#cfn-cases-field-name): {{String}}
  [Tags](#cfn-cases-field-tags): {{
    - Tag}}
  [Type](#cfn-cases-field-type): {{String}}
```

## Properties
<a name="aws-resource-cases-field-properties"></a>

`Attributes`  <a name="cfn-cases-field-attributes"></a>
Union of field attributes.
*Required*: No
*Type*: [FieldAttributes](aws-properties-cases-field-fieldattributes.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-cases-field-description"></a>
Description of the field.
*Required*: No
*Type*: String
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DomainId`  <a name="cfn-cases-field-domainid"></a>
The unique identifier of the Cases domain.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `500`
*Update requires*: Updates are not supported.

`Name`  <a name="cfn-cases-field-name"></a>
Name of the field.
*Required*: Yes
*Type*: String
*Pattern*: `^.*[\S]$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-cases-field-tags"></a>
An array of key-value pairs to apply to this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-cases-field-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-cases-field-type"></a>
Type of the field.
*Required*: Yes
*Type*: String
*Allowed values*: `Text | Number | Boolean | DateTime | SingleSelect | Url | User`
*Update requires*: Updates are not supported.

## Return values
<a name="aws-resource-cases-field-return-values"></a>

### Ref
<a name="aws-resource-cases-field-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ARN of the field. For example:

 `arn:aws:cases:us-west-2:123456789012:domain/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/field/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-cases-field-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cases-field-return-values-fn--getatt-fn--getatt"></a>

`CreatedTime`  <a name="CreatedTime-fn::getatt"></a>
Timestamp at which the resource was created.

`FieldArn`  <a name="FieldArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the field.

`FieldId`  <a name="FieldId-fn::getatt"></a>
Unique identifier of the field.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
Timestamp at which the resource was created or last modified.

`Namespace`  <a name="Namespace-fn::getatt"></a>
Namespace of the field.
