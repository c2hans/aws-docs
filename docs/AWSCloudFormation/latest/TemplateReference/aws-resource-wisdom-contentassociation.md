---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-wisdom-contentassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::ContentAssociation
<a name="aws-resource-wisdom-contentassociation"></a>

Creates an association between a content resource in a knowledge base and [step-by-step guides](https://docs.aws.amazon.com/connect/latest/adminguide/step-by-step-guided-experiences.html). Step-by-step guides offer instructions to agents for resolving common customer issues. You create a content association to integrate Amazon Q in Connect and step-by-step guides.

After you integrate Amazon Q and step-by-step guides, when Amazon Q provides a recommendation to an agent based on the intent that it's detected, it also provides them with the option to start the step-by-step guide that you have associated with the content.

Note the following limitations:
+ You can create only one content association for each content resource in a knowledge base.
+ You can associate a step-by-step guide with multiple content resources.

For more information, see [Integrate Amazon Q in Connect with step-by-step guides](https://docs.aws.amazon.com/connect/latest/adminguide/integrate-q-with-guides.html) in the *Connect Customer Administrator Guide*.

## Syntax
<a name="aws-resource-wisdom-contentassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-wisdom-contentassociation-syntax.json"></a>

```
{
  "Type" : "AWS::Wisdom::ContentAssociation",
  "Properties" : {
      "[Association](#cfn-wisdom-contentassociation-association)" : {{ContentAssociationContents}},
      "[AssociationType](#cfn-wisdom-contentassociation-associationtype)" : {{String}},
      "[ContentId](#cfn-wisdom-contentassociation-contentid)" : {{String}},
      "[KnowledgeBaseId](#cfn-wisdom-contentassociation-knowledgebaseid)" : {{String}},
      "[Tags](#cfn-wisdom-contentassociation-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-wisdom-contentassociation-syntax.yaml"></a>

```
Type: AWS::Wisdom::ContentAssociation
Properties:
  [Association](#cfn-wisdom-contentassociation-association): {{
    ContentAssociationContents}}
  [AssociationType](#cfn-wisdom-contentassociation-associationtype): {{String}}
  [ContentId](#cfn-wisdom-contentassociation-contentid): {{String}}
  [KnowledgeBaseId](#cfn-wisdom-contentassociation-knowledgebaseid): {{String}}
  [Tags](#cfn-wisdom-contentassociation-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-wisdom-contentassociation-properties"></a>

`Association`  <a name="cfn-wisdom-contentassociation-association"></a>
Property description not available.
*Required*: Yes
*Type*: [ContentAssociationContents](aws-properties-wisdom-contentassociation-contentassociationcontents.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AssociationType`  <a name="cfn-wisdom-contentassociation-associationtype"></a>
The type of association.
*Required*: Yes
*Type*: String
*Allowed values*: `AMAZON_CONNECT_GUIDE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ContentId`  <a name="cfn-wisdom-contentassociation-contentid"></a>
The identifier of the content.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KnowledgeBaseId`  <a name="cfn-wisdom-contentassociation-knowledgebaseid"></a>
The identifier of the knowledge base.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-wisdom-contentassociation-tags"></a>
The tags used to organize, track, or control access for this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-wisdom-contentassociation-tag.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-wisdom-contentassociation-return-values"></a>

### Ref
<a name="aws-resource-wisdom-contentassociation-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-wisdom-contentassociation-return-values-fn--getatt"></a>

####
<a name="aws-resource-wisdom-contentassociation-return-values-fn--getatt-fn--getatt"></a>

`ContentArn`  <a name="ContentArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the content.

`ContentAssociationArn`  <a name="ContentAssociationArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the content association.

`ContentAssociationId`  <a name="ContentAssociationId-fn::getatt"></a>
The identifier of the content association. Can be either the ID or the ARN. URLs cannot contain the ARN.

`KnowledgeBaseArn`  <a name="KnowledgeBaseArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the knowledge base.
