---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-contentassociation-amazonconnectguideassociationdata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::ContentAssociation AmazonConnectGuideAssociationData
<a name="aws-properties-wisdom-contentassociation-amazonconnectguideassociationdata"></a>

Content association data for a [step-by-step guide](https://docs.aws.amazon.com/connect/latest/adminguide/step-by-step-guided-experiences.html).

## Syntax
<a name="aws-properties-wisdom-contentassociation-amazonconnectguideassociationdata-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-contentassociation-amazonconnectguideassociationdata-syntax.json"></a>

```
{
  "[FlowId](#cfn-wisdom-contentassociation-amazonconnectguideassociationdata-flowid)" : {{String}}
}
```

### YAML
<a name="aws-properties-wisdom-contentassociation-amazonconnectguideassociationdata-syntax.yaml"></a>

```
  [FlowId](#cfn-wisdom-contentassociation-amazonconnectguideassociationdata-flowid): {{String}}
```

## Properties
<a name="aws-properties-wisdom-contentassociation-amazonconnectguideassociationdata-properties"></a>

`FlowId`  <a name="cfn-wisdom-contentassociation-amazonconnectguideassociationdata-flowid"></a>
 The Amazon Resource Name (ARN) of an Connect Customer flow. Step-by-step guides are a type of flow.
*Required*: No
*Type*: String
*Pattern*: `^arn:[a-z-]+?:[a-z-]+?:[a-z0-9-]*?:([0-9]{12})?:[a-zA-Z0-9-:/]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
