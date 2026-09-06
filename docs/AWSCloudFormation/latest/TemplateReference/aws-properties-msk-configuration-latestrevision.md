---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-configuration-latestrevision.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Configuration LatestRevision
<a name="aws-properties-msk-configuration-latestrevision"></a>

Describes a configuration revision.

## Syntax
<a name="aws-properties-msk-configuration-latestrevision-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-configuration-latestrevision-syntax.json"></a>

```
{
  "[CreationTime](#cfn-msk-configuration-latestrevision-creationtime)" : {{String}},
  "[Description](#cfn-msk-configuration-latestrevision-description)" : {{String}},
  "[Revision](#cfn-msk-configuration-latestrevision-revision)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-msk-configuration-latestrevision-syntax.yaml"></a>

```
  [CreationTime](#cfn-msk-configuration-latestrevision-creationtime): {{String}}
  [Description](#cfn-msk-configuration-latestrevision-description): {{String}}
  [Revision](#cfn-msk-configuration-latestrevision-revision): {{Integer}}
```

## Properties
<a name="aws-properties-msk-configuration-latestrevision-properties"></a>

`CreationTime`  <a name="cfn-msk-configuration-latestrevision-creationtime"></a>
The time when the configuration revision was created.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-msk-configuration-latestrevision-description"></a>
The description of the configuration revision.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Revision`  <a name="cfn-msk-configuration-latestrevision-revision"></a>
The revision number.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
