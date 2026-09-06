---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-wisdom-assistantassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::AssistantAssociation
<a name="aws-resource-wisdom-assistantassociation"></a>

Specifies an association between an Connect Customer Wisdom assistant and another resource. Currently, the only supported association is with a knowledge base. An assistant can have only a single association.

## Syntax
<a name="aws-resource-wisdom-assistantassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-wisdom-assistantassociation-syntax.json"></a>

```
{
  "Type" : "AWS::Wisdom::AssistantAssociation",
  "Properties" : {
      "[AssistantId](#cfn-wisdom-assistantassociation-assistantid)" : {{String}},
      "[Association](#cfn-wisdom-assistantassociation-association)" : {{AssociationData}},
      "[AssociationType](#cfn-wisdom-assistantassociation-associationtype)" : {{String}},
      "[Tags](#cfn-wisdom-assistantassociation-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-wisdom-assistantassociation-syntax.yaml"></a>

```
Type: AWS::Wisdom::AssistantAssociation
Properties:
  [AssistantId](#cfn-wisdom-assistantassociation-assistantid): {{String}}
  [Association](#cfn-wisdom-assistantassociation-association): {{
    AssociationData}}
  [AssociationType](#cfn-wisdom-assistantassociation-associationtype): {{String}}
  [Tags](#cfn-wisdom-assistantassociation-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-wisdom-assistantassociation-properties"></a>

`AssistantId`  <a name="cfn-wisdom-assistantassociation-assistantid"></a>
The identifier of the Wisdom assistant.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Association`  <a name="cfn-wisdom-assistantassociation-association"></a>
The identifier of the associated resource.
*Required*: Yes
*Type*: [AssociationData](aws-properties-wisdom-assistantassociation-associationdata.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AssociationType`  <a name="cfn-wisdom-assistantassociation-associationtype"></a>
The type of association.
*Required*: Yes
*Type*: String
*Allowed values*: `KNOWLEDGE_BASE | EXTERNAL_BEDROCK_KNOWLEDGE_BASE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-wisdom-assistantassociation-tags"></a>
The tags used to organize, track, or control access for this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-wisdom-assistantassociation-tag.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-wisdom-assistantassociation-return-values"></a>

### Ref
<a name="aws-resource-wisdom-assistantassociation-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the association ID.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-wisdom-assistantassociation-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-wisdom-assistantassociation-return-values-fn--getatt-fn--getatt"></a>

`AssistantArn`  <a name="AssistantArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the Wisdom assistant.

`AssistantAssociationArn`  <a name="AssistantAssociationArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the assistant association.

`AssistantAssociationId`  <a name="AssistantAssociationId-fn::getatt"></a>
The ID of the association.
