---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cleanrooms-idnamespaceassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::IdNamespaceAssociation
<a name="aws-resource-cleanrooms-idnamespaceassociation"></a>

Provides information to create the ID namespace association.

## Syntax
<a name="aws-resource-cleanrooms-idnamespaceassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cleanrooms-idnamespaceassociation-syntax.json"></a>

```
{
  "Type" : "AWS::CleanRooms::IdNamespaceAssociation",
  "Properties" : {
      "[Description](#cfn-cleanrooms-idnamespaceassociation-description)" : {{String}},
      "[IdMappingConfig](#cfn-cleanrooms-idnamespaceassociation-idmappingconfig)" : {{IdMappingConfig}},
      "[InputReferenceConfig](#cfn-cleanrooms-idnamespaceassociation-inputreferenceconfig)" : {{IdNamespaceAssociationInputReferenceConfig}},
      "[MembershipIdentifier](#cfn-cleanrooms-idnamespaceassociation-membershipidentifier)" : {{String}},
      "[Name](#cfn-cleanrooms-idnamespaceassociation-name)" : {{String}},
      "[Tags](#cfn-cleanrooms-idnamespaceassociation-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-cleanrooms-idnamespaceassociation-syntax.yaml"></a>

```
Type: AWS::CleanRooms::IdNamespaceAssociation
Properties:
  [Description](#cfn-cleanrooms-idnamespaceassociation-description): {{String}}
  [IdMappingConfig](#cfn-cleanrooms-idnamespaceassociation-idmappingconfig): {{
    IdMappingConfig}}
  [InputReferenceConfig](#cfn-cleanrooms-idnamespaceassociation-inputreferenceconfig): {{
    IdNamespaceAssociationInputReferenceConfig}}
  [MembershipIdentifier](#cfn-cleanrooms-idnamespaceassociation-membershipidentifier): {{String}}
  [Name](#cfn-cleanrooms-idnamespaceassociation-name): {{String}}
  [Tags](#cfn-cleanrooms-idnamespaceassociation-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-cleanrooms-idnamespaceassociation-properties"></a>

`Description`  <a name="cfn-cleanrooms-idnamespaceassociation-description"></a>
The description of the ID namespace association.
*Required*: No
*Type*: String
*Pattern*: `^[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*$`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IdMappingConfig`  <a name="cfn-cleanrooms-idnamespaceassociation-idmappingconfig"></a>
The configuration settings for the ID mapping table.
*Required*: No
*Type*: [IdMappingConfig](aws-properties-cleanrooms-idnamespaceassociation-idmappingconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InputReferenceConfig`  <a name="cfn-cleanrooms-idnamespaceassociation-inputreferenceconfig"></a>
The input reference configuration for the ID namespace association.
*Required*: Yes
*Type*: [IdNamespaceAssociationInputReferenceConfig](aws-properties-cleanrooms-idnamespaceassociation-idnamespaceassociationinputreferenceconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MembershipIdentifier`  <a name="cfn-cleanrooms-idnamespaceassociation-membershipidentifier"></a>
The unique identifier of the membership that contains the ID namespace association.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
*Minimum*: `36`
*Maximum*: `36`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-cleanrooms-idnamespaceassociation-name"></a>
The name of this ID namespace association.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-cleanrooms-idnamespaceassociation-tags"></a>
An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-cleanrooms-idnamespaceassociation-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cleanrooms-idnamespaceassociation-return-values"></a>

### Ref
<a name="aws-resource-cleanrooms-idnamespaceassociation-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource name. For example:

 `{"Ref": "MyIdNamespaceAssociation"}`

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-cleanrooms-idnamespaceassociation-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cleanrooms-idnamespaceassociation-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the ID namespace association.

`CollaborationArn`  <a name="CollaborationArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the collaboration that contains this ID namespace association.

`CollaborationIdentifier`  <a name="CollaborationIdentifier-fn::getatt"></a>
The unique identifier of the collaboration that contains this ID namespace association.

`IdNamespaceAssociationIdentifier`  <a name="IdNamespaceAssociationIdentifier-fn::getatt"></a>
The unique identifier of the ID namespace association that you want to retrieve.

`MembershipArn`  <a name="MembershipArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the membership resource for this ID namespace association.
