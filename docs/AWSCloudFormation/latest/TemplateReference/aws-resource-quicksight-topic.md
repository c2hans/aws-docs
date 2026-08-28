---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-quicksight-topic.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Topic
<a name="aws-resource-quicksight-topic"></a>

Creates a new Q topic.

## Syntax
<a name="aws-resource-quicksight-topic-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-quicksight-topic-syntax.json"></a>

```
{
  "Type" : "AWS::QuickSight::Topic",
  "Properties" : {
      "[AwsAccountId](#cfn-quicksight-topic-awsaccountid)" : {{String}},
      "[ConfigOptions](#cfn-quicksight-topic-configoptions)" : {{TopicConfigOptions}},
      "[CustomInstructions](#cfn-quicksight-topic-custominstructions)" : {{CustomInstructions}},
      "[DataSets](#cfn-quicksight-topic-datasets)" : {{[ DatasetMetadata, ... ]}},
      "[Description](#cfn-quicksight-topic-description)" : {{String}},
      "[FolderArns](#cfn-quicksight-topic-folderarns)" : {{[ String, ... ]}},
      "[Name](#cfn-quicksight-topic-name)" : {{String}},
      "[Tags](#cfn-quicksight-topic-tags)" : {{[ Tag, ... ]}},
      "[TopicId](#cfn-quicksight-topic-topicid)" : {{String}},
      "[UserExperienceVersion](#cfn-quicksight-topic-userexperienceversion)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-quicksight-topic-syntax.yaml"></a>

```
Type: AWS::QuickSight::Topic
Properties:
  [AwsAccountId](#cfn-quicksight-topic-awsaccountid): {{String}}
  [ConfigOptions](#cfn-quicksight-topic-configoptions): {{
    TopicConfigOptions}}
  [CustomInstructions](#cfn-quicksight-topic-custominstructions): {{
    CustomInstructions}}
  [DataSets](#cfn-quicksight-topic-datasets): {{
    - DatasetMetadata}}
  [Description](#cfn-quicksight-topic-description): {{String}}
  [FolderArns](#cfn-quicksight-topic-folderarns): {{
    - String}}
  [Name](#cfn-quicksight-topic-name): {{String}}
  [Tags](#cfn-quicksight-topic-tags): {{
    - Tag}}
  [TopicId](#cfn-quicksight-topic-topicid): {{String}}
  [UserExperienceVersion](#cfn-quicksight-topic-userexperienceversion): {{String}}
```

## Properties
<a name="aws-resource-quicksight-topic-properties"></a>

`AwsAccountId`  <a name="cfn-quicksight-topic-awsaccountid"></a>
The ID of the AWS account that you want to create a topic in.
*Required*: No
*Type*: String
*Pattern*: `^[0-9]{12}$`
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ConfigOptions`  <a name="cfn-quicksight-topic-configoptions"></a>
Configuration options for a `Topic`.
*Required*: No
*Type*: [TopicConfigOptions](aws-properties-quicksight-topic-topicconfigoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomInstructions`  <a name="cfn-quicksight-topic-custominstructions"></a>
Custom instructions for the topic.
*Required*: No
*Type*: [CustomInstructions](aws-properties-quicksight-topic-custominstructions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataSets`  <a name="cfn-quicksight-topic-datasets"></a>
The data sets that the topic is associated with.
*Required*: No
*Type*: Array of [DatasetMetadata](aws-properties-quicksight-topic-datasetmetadata.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-quicksight-topic-description"></a>
The description of the topic.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FolderArns`  <a name="cfn-quicksight-topic-folderarns"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `20`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-quicksight-topic-name"></a>
The name of the topic.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-quicksight-topic-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-quicksight-topic-tag.md)
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TopicId`  <a name="cfn-quicksight-topic-topicid"></a>
The ID for the topic. This ID is unique per AWS Region for each AWS account.
*Required*: No
*Type*: String
*Pattern*: `^[A-Za-z0-9-_.\\+]*$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`UserExperienceVersion`  <a name="cfn-quicksight-topic-userexperienceversion"></a>
The user experience version of the topic.
*Required*: No
*Type*: String
*Allowed values*: `LEGACY | NEW_READER_EXPERIENCE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-quicksight-topic-return-values"></a>

### Ref
<a name="aws-resource-quicksight-topic-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-quicksight-topic-return-values-fn--getatt"></a>

####
<a name="aws-resource-quicksight-topic-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the topic.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
