---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cleanrooms-idmappingtable.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::IdMappingTable
<a name="aws-resource-cleanrooms-idmappingtable"></a>

Describes information about the ID mapping table.

## Syntax
<a name="aws-resource-cleanrooms-idmappingtable-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cleanrooms-idmappingtable-syntax.json"></a>

```
{
  "Type" : "AWS::CleanRooms::IdMappingTable",
  "Properties" : {
      "[Description](#cfn-cleanrooms-idmappingtable-description)" : {{String}},
      "[InputReferenceConfig](#cfn-cleanrooms-idmappingtable-inputreferenceconfig)" : {{IdMappingTableInputReferenceConfig}},
      "[KmsKeyArn](#cfn-cleanrooms-idmappingtable-kmskeyarn)" : {{String}},
      "[MembershipIdentifier](#cfn-cleanrooms-idmappingtable-membershipidentifier)" : {{String}},
      "[Name](#cfn-cleanrooms-idmappingtable-name)" : {{String}},
      "[Tags](#cfn-cleanrooms-idmappingtable-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-cleanrooms-idmappingtable-syntax.yaml"></a>

```
Type: AWS::CleanRooms::IdMappingTable
Properties:
  [Description](#cfn-cleanrooms-idmappingtable-description): {{String}}
  [InputReferenceConfig](#cfn-cleanrooms-idmappingtable-inputreferenceconfig): {{
    IdMappingTableInputReferenceConfig}}
  [KmsKeyArn](#cfn-cleanrooms-idmappingtable-kmskeyarn): {{String}}
  [MembershipIdentifier](#cfn-cleanrooms-idmappingtable-membershipidentifier): {{String}}
  [Name](#cfn-cleanrooms-idmappingtable-name): {{String}}
  [Tags](#cfn-cleanrooms-idmappingtable-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-cleanrooms-idmappingtable-properties"></a>

`Description`  <a name="cfn-cleanrooms-idmappingtable-description"></a>
The description of the ID mapping table.
*Required*: No
*Type*: String
*Pattern*: `^[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*$`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InputReferenceConfig`  <a name="cfn-cleanrooms-idmappingtable-inputreferenceconfig"></a>
The input reference configuration for the ID mapping table.
*Required*: Yes
*Type*: [IdMappingTableInputReferenceConfig](aws-properties-cleanrooms-idmappingtable-idmappingtableinputreferenceconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KmsKeyArn`  <a name="cfn-cleanrooms-idmappingtable-kmskeyarn"></a>
The Amazon Resource Name (ARN) of the AWS KMS key.
*Required*: No
*Type*: String
*Minimum*: `4`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MembershipIdentifier`  <a name="cfn-cleanrooms-idmappingtable-membershipidentifier"></a>
The unique identifier of the membership resource for the ID mapping table.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
*Minimum*: `36`
*Maximum*: `36`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-cleanrooms-idmappingtable-name"></a>
The name of the ID mapping table.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_](([a-zA-Z0-9_ ]+-)*([a-zA-Z0-9_ ]+))?$`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-cleanrooms-idmappingtable-tags"></a>
An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-cleanrooms-idmappingtable-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cleanrooms-idmappingtable-return-values"></a>

### Ref
<a name="aws-resource-cleanrooms-idmappingtable-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource name. For example:

 `{"Ref": "MyIdMappingTable"}`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-cleanrooms-idmappingtable-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cleanrooms-idmappingtable-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the ID mapping table.

`CollaborationArn`  <a name="CollaborationArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the collaboration that contains this ID mapping table.

`CollaborationIdentifier`  <a name="CollaborationIdentifier-fn::getatt"></a>
The unique identifier of the collaboration that contains this ID mapping table.

`IdMappingTableIdentifier`  <a name="IdMappingTableIdentifier-fn::getatt"></a>
The unique identifier of the ID mapping table identifier that you want to retrieve.

`MembershipArn`  <a name="MembershipArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the membership resource for the ID mapping table.
