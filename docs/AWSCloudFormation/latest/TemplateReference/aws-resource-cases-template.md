---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cases-template.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cases::Template
<a name="aws-resource-cases-template"></a>

Creates a template in the Cases domain. This template is used to define the case object model (that is, to define what data can be captured on cases) in a Cases domain. A template must have a unique name within a domain, and it must reference existing field IDs and layout IDs. Additionally, multiple fields with same IDs are not allowed within the same Template. A template can be either Active or Inactive, as indicated by its status. Inactive templates cannot be used to create cases.

 Other template APIs are:
+  [DeleteTemplate](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_DeleteTemplate.html)
+  [GetTemplate](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_GetTemplate.html)
+  [ListTemplates](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_ListTemplates.html)
+  [UpdateTemplate](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_UpdateTemplate.html)

## Syntax
<a name="aws-resource-cases-template-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cases-template-syntax.json"></a>

```
{
  "Type" : "AWS::Cases::Template",
  "Properties" : {
      "[Description](#cfn-cases-template-description)" : {{String}},
      "[DomainId](#cfn-cases-template-domainid)" : {{String}},
      "[LayoutConfiguration](#cfn-cases-template-layoutconfiguration)" : {{LayoutConfiguration}},
      "[Name](#cfn-cases-template-name)" : {{String}},
      "[RequiredFields](#cfn-cases-template-requiredfields)" : {{[ RequiredField, ... ]}},
      "[Rules](#cfn-cases-template-rules)" : {{[ TemplateRule, ... ]}},
      "[Status](#cfn-cases-template-status)" : {{String}},
      "[Tags](#cfn-cases-template-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-cases-template-syntax.yaml"></a>

```
Type: AWS::Cases::Template
Properties:
  [Description](#cfn-cases-template-description): {{String}}
  [DomainId](#cfn-cases-template-domainid): {{String}}
  [LayoutConfiguration](#cfn-cases-template-layoutconfiguration): {{
    LayoutConfiguration}}
  [Name](#cfn-cases-template-name): {{String}}
  [RequiredFields](#cfn-cases-template-requiredfields): {{
    - RequiredField}}
  [Rules](#cfn-cases-template-rules): {{
    - TemplateRule}}
  [Status](#cfn-cases-template-status): {{String}}
  [Tags](#cfn-cases-template-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-cases-template-properties"></a>

`Description`  <a name="cfn-cases-template-description"></a>
A brief description of the template.
*Required*: No
*Type*: String
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DomainId`  <a name="cfn-cases-template-domainid"></a>
The unique identifier of the Cases domain.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `500`
*Update requires*: Updates are not supported.

`LayoutConfiguration`  <a name="cfn-cases-template-layoutconfiguration"></a>
Object to store configuration of layouts associated to the template.
*Required*: No
*Type*: [LayoutConfiguration](aws-properties-cases-template-layoutconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-cases-template-name"></a>
The template name.
*Required*: Yes
*Type*: String
*Pattern*: `^.*[\S]$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RequiredFields`  <a name="cfn-cases-template-requiredfields"></a>
A list of fields that must contain a value for a case to be successfully created with this template.
*Required*: No
*Type*: Array of [RequiredField](aws-properties-cases-template-requiredfield.md)
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Rules`  <a name="cfn-cases-template-rules"></a>
A list of case rules (also known as [case field conditions](https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html)) on a template.
*Required*: No
*Type*: Array of [TemplateRule](aws-properties-cases-template-templaterule.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-cases-template-status"></a>
The status of the template.
*Required*: No
*Type*: String
*Allowed values*: `Active | Inactive`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-cases-template-tags"></a>
An array of key-value pairs to apply to this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-cases-template-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cases-template-return-values"></a>

### Ref
<a name="aws-resource-cases-template-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ARN of the template. For example:

 `arn:aws:cases:us-west-2:123456789012:domain/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/template/a1b2c3d4-5678-90ab-cdef-EXAMPLE55555`

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-cases-template-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cases-template-return-values-fn--getatt-fn--getatt"></a>

`CreatedTime`  <a name="CreatedTime-fn::getatt"></a>
Timestamp at which the resource was created.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
Timestamp at which the resource was created or last modified.

`TemplateArn`  <a name="TemplateArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the template.

`TemplateId`  <a name="TemplateId-fn::getatt"></a>
A unique identifier of a template.
