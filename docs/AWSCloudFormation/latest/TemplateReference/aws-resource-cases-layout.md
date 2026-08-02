---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cases-layout.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cases::Layout
<a name="aws-resource-cases-layout"></a>

Creates a layout in the Cases domain. Layouts define the following configuration in the top section and More Info tab of the Cases user interface:
+ Fields to display to the users
+ Field ordering

**Note**
Title and Status fields cannot be part of layouts since they are not configurable.

## Syntax
<a name="aws-resource-cases-layout-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cases-layout-syntax.json"></a>

```
{
  "Type" : "AWS::Cases::Layout",
  "Properties" : {
      "[Content](#cfn-cases-layout-content)" : {{LayoutContent}},
      "[DomainId](#cfn-cases-layout-domainid)" : {{String}},
      "[Name](#cfn-cases-layout-name)" : {{String}},
      "[Tags](#cfn-cases-layout-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-cases-layout-syntax.yaml"></a>

```
Type: AWS::Cases::Layout
Properties:
  [Content](#cfn-cases-layout-content): {{
    LayoutContent}}
  [DomainId](#cfn-cases-layout-domainid): {{String}}
  [Name](#cfn-cases-layout-name): {{String}}
  [Tags](#cfn-cases-layout-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-cases-layout-properties"></a>

`Content`  <a name="cfn-cases-layout-content"></a>
Object to store union of different versions of layout content.
*Required*: Yes
*Type*: [LayoutContent](aws-properties-cases-layout-layoutcontent.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DomainId`  <a name="cfn-cases-layout-domainid"></a>
The unique identifier of the Cases domain.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `500`
*Update requires*: Updates are not supported.

`Name`  <a name="cfn-cases-layout-name"></a>
The name of the layout.
*Required*: Yes
*Type*: String
*Pattern*: `^.*[\S]$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-cases-layout-tags"></a>
An array of key-value pairs to apply to this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-cases-layout-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cases-layout-return-values"></a>

### Ref
<a name="aws-resource-cases-layout-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ARN of the layout. For example:

 `arn:aws:cases:us-west-2:123456789012:domain/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/layout/a1b2c3d4-5678-90ab-cdef-EXAMPLE44444`

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-cases-layout-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cases-layout-return-values-fn--getatt-fn--getatt"></a>

`CreatedTime`  <a name="CreatedTime-fn::getatt"></a>
Timestamp at which the resource was created.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
Timestamp at which the resource was created or last modified.

`LayoutArn`  <a name="LayoutArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the newly created layout.

`LayoutId`  <a name="LayoutId-fn::getatt"></a>
The unique identifier of the layout.
