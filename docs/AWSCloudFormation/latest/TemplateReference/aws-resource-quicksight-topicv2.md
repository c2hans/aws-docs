---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-quicksight-topicv2.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::TopicV2
<a name="aws-resource-quicksight-topicv2"></a>

Creates a new Q topic.

## Syntax
<a name="aws-resource-quicksight-topicv2-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-quicksight-topicv2-syntax.json"></a>

```
{
  "Type" : "AWS::QuickSight::TopicV2",
  "Properties" : {
      "[AwsAccountId](#cfn-quicksight-topicv2-awsaccountid)" : {{String}},
      "[CustomInstructions](#cfn-quicksight-topicv2-custominstructions)" : {{CustomInstructions}},
      "[DataSetRelations](#cfn-quicksight-topicv2-datasetrelations)" : {{[ DataSetRelation, ... ]}},
      "[DataSets](#cfn-quicksight-topicv2-datasets)" : {{[ DataSetReference, ... ]}},
      "[Description](#cfn-quicksight-topicv2-description)" : {{String}},
      "[FolderArns](#cfn-quicksight-topicv2-folderarns)" : {{[ String, ... ]}},
      "[Name](#cfn-quicksight-topicv2-name)" : {{String}},
      "[Permissions](#cfn-quicksight-topicv2-permissions)" : {{[ ResourcePermission, ... ]}},
      "[Tags](#cfn-quicksight-topicv2-tags)" : {{[ Tag, ... ]}},
      "[TopicId](#cfn-quicksight-topicv2-topicid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-quicksight-topicv2-syntax.yaml"></a>

```
Type: AWS::QuickSight::TopicV2
Properties:
  [AwsAccountId](#cfn-quicksight-topicv2-awsaccountid): {{String}}
  [CustomInstructions](#cfn-quicksight-topicv2-custominstructions): {{
    CustomInstructions}}
  [DataSetRelations](#cfn-quicksight-topicv2-datasetrelations): {{
    - DataSetRelation}}
  [DataSets](#cfn-quicksight-topicv2-datasets): {{
    - DataSetReference}}
  [Description](#cfn-quicksight-topicv2-description): {{String}}
  [FolderArns](#cfn-quicksight-topicv2-folderarns): {{
    - String}}
  [Name](#cfn-quicksight-topicv2-name): {{String}}
  [Permissions](#cfn-quicksight-topicv2-permissions): {{
    - ResourcePermission}}
  [Tags](#cfn-quicksight-topicv2-tags): {{
    - Tag}}
  [TopicId](#cfn-quicksight-topicv2-topicid): {{String}}
```

## Properties
<a name="aws-resource-quicksight-topicv2-properties"></a>

`AwsAccountId`  <a name="cfn-quicksight-topicv2-awsaccountid"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[0-9]{12}$`
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CustomInstructions`  <a name="cfn-quicksight-topicv2-custominstructions"></a>
Property description not available.
*Required*: No
*Type*: [CustomInstructions](aws-properties-quicksight-topicv2-custominstructions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataSetRelations`  <a name="cfn-quicksight-topicv2-datasetrelations"></a>
The relations between the data sets that the topic is associated with.
*Required*: No
*Type*: Array of [DataSetRelation](aws-properties-quicksight-topicv2-datasetrelation.md)
*Minimum*: `0`
*Maximum*: `32`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataSets`  <a name="cfn-quicksight-topicv2-datasets"></a>
The data sets that the topic is associated with.
*Required*: No
*Type*: Array of [DataSetReference](aws-properties-quicksight-topicv2-datasetreference.md)
*Minimum*: `1`
*Maximum*: `32`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-quicksight-topicv2-description"></a>
The description of the topic.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FolderArns`  <a name="cfn-quicksight-topicv2-folderarns"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `20`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-quicksight-topicv2-name"></a>
The name of the topic.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Permissions`  <a name="cfn-quicksight-topicv2-permissions"></a>
A list of permissions for the topics that you want to apply overrides to.
*Required*: No
*Type*: Array of [ResourcePermission](aws-properties-quicksight-topicv2-resourcepermission.md)
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-quicksight-topicv2-tags"></a>
A list of tags for the topics that you want to apply overrides to.
*Required*: No
*Type*: Array of [Tag](aws-properties-quicksight-topicv2-tag.md)
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TopicId`  <a name="cfn-quicksight-topicv2-topicid"></a>
The ID of the topic. This ID is unique per AWS Region for each AWS account.
*Required*: No
*Type*: String
*Pattern*: `^[A-Za-z0-9-_.\\+]*$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-quicksight-topicv2-return-values"></a>

### Ref
<a name="aws-resource-quicksight-topicv2-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-quicksight-topicv2-return-values-fn--getatt"></a>

####
<a name="aws-resource-quicksight-topicv2-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the topic.
