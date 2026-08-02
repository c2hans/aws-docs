---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-agent-custompromptprofile.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Agent CustomPromptProfile
<a name="aws-properties-quicksight-agent-custompromptprofile"></a>

<a name="aws-properties-quicksight-agent-custompromptprofile-description"></a>The `CustomPromptProfile` property type specifies Property description not available. for an [AWS::QuickSight::Agent](aws-resource-quicksight-agent.md).

## Syntax
<a name="aws-properties-quicksight-agent-custompromptprofile-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-agent-custompromptprofile-syntax.json"></a>

```
{
  "[ModelProfileId](#cfn-quicksight-agent-custompromptprofile-modelprofileid)" : {{String}},
  "[QbsAwsAccountId](#cfn-quicksight-agent-custompromptprofile-qbsawsaccountid)" : {{String}},
  "[SubscriptionId](#cfn-quicksight-agent-custompromptprofile-subscriptionid)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-agent-custompromptprofile-syntax.yaml"></a>

```
  [ModelProfileId](#cfn-quicksight-agent-custompromptprofile-modelprofileid): {{String}}
  [QbsAwsAccountId](#cfn-quicksight-agent-custompromptprofile-qbsawsaccountid): {{String}}
  [SubscriptionId](#cfn-quicksight-agent-custompromptprofile-subscriptionid): {{String}}
```

## Properties
<a name="aws-properties-quicksight-agent-custompromptprofile-properties"></a>

`ModelProfileId`  <a name="cfn-quicksight-agent-custompromptprofile-modelprofileid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Maximum*: `36`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QbsAwsAccountId`  <a name="cfn-quicksight-agent-custompromptprofile-qbsawsaccountid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^QBS[0-9]{12}$`
*Maximum*: `15`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubscriptionId`  <a name="cfn-quicksight-agent-custompromptprofile-subscriptionid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Maximum*: `32`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
