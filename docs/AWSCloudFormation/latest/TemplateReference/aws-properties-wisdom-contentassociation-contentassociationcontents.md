---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-contentassociation-contentassociationcontents.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::ContentAssociation ContentAssociationContents
<a name="aws-properties-wisdom-contentassociation-contentassociationcontents"></a>

The contents of a content association.

## Syntax
<a name="aws-properties-wisdom-contentassociation-contentassociationcontents-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-contentassociation-contentassociationcontents-syntax.json"></a>

```
{
  "[AmazonConnectGuideAssociation](#cfn-wisdom-contentassociation-contentassociationcontents-amazonconnectguideassociation)" : {{AmazonConnectGuideAssociationData}}
}
```

### YAML
<a name="aws-properties-wisdom-contentassociation-contentassociationcontents-syntax.yaml"></a>

```
  [AmazonConnectGuideAssociation](#cfn-wisdom-contentassociation-contentassociationcontents-amazonconnectguideassociation): {{
    AmazonConnectGuideAssociationData}}
```

## Properties
<a name="aws-properties-wisdom-contentassociation-contentassociationcontents-properties"></a>

`AmazonConnectGuideAssociation`  <a name="cfn-wisdom-contentassociation-contentassociationcontents-amazonconnectguideassociation"></a>
The data of the step-by-step guide association.
*Required*: Yes
*Type*: [AmazonConnectGuideAssociationData](aws-properties-wisdom-contentassociation-amazonconnectguideassociationdata.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
