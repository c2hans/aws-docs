---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-agent-custompromptinterface.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Agent CustomPromptInterface
<a name="aws-properties-quicksight-agent-custompromptinterface"></a>

<a name="aws-properties-quicksight-agent-custompromptinterface-description"></a>The `CustomPromptInterface` property type specifies Property description not available. for an [AWS::QuickSight::Agent](aws-resource-quicksight-agent.md).

## Syntax
<a name="aws-properties-quicksight-agent-custompromptinterface-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-agent-custompromptinterface-syntax.json"></a>

```
{
  "[CustomInstructions](#cfn-quicksight-agent-custompromptinterface-custominstructions)" : {{String}},
  "[Identity](#cfn-quicksight-agent-custompromptinterface-identity)" : {{String}},
  "[ModelProfileId](#cfn-quicksight-agent-custompromptinterface-modelprofileid)" : {{String}},
  "[OutputStyle](#cfn-quicksight-agent-custompromptinterface-outputstyle)" : {{String}},
  "[PromptSummary](#cfn-quicksight-agent-custompromptinterface-promptsummary)" : {{String}},
  "[QbsAwsAccountId](#cfn-quicksight-agent-custompromptinterface-qbsawsaccountid)" : {{String}},
  "[ResponseLength](#cfn-quicksight-agent-custompromptinterface-responselength)" : {{String}},
  "[SubscriptionId](#cfn-quicksight-agent-custompromptinterface-subscriptionid)" : {{String}},
  "[Tone](#cfn-quicksight-agent-custompromptinterface-tone)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-agent-custompromptinterface-syntax.yaml"></a>

```
  [CustomInstructions](#cfn-quicksight-agent-custompromptinterface-custominstructions): {{String}}
  [Identity](#cfn-quicksight-agent-custompromptinterface-identity): {{String}}
  [ModelProfileId](#cfn-quicksight-agent-custompromptinterface-modelprofileid): {{String}}
  [OutputStyle](#cfn-quicksight-agent-custompromptinterface-outputstyle): {{String}}
  [PromptSummary](#cfn-quicksight-agent-custompromptinterface-promptsummary): {{String}}
  [QbsAwsAccountId](#cfn-quicksight-agent-custompromptinterface-qbsawsaccountid): {{String}}
  [ResponseLength](#cfn-quicksight-agent-custompromptinterface-responselength): {{String}}
  [SubscriptionId](#cfn-quicksight-agent-custompromptinterface-subscriptionid): {{String}}
  [Tone](#cfn-quicksight-agent-custompromptinterface-tone): {{String}}
```

## Properties
<a name="aws-properties-quicksight-agent-custompromptinterface-properties"></a>

`CustomInstructions`  <a name="cfn-quicksight-agent-custompromptinterface-custominstructions"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `5`
*Maximum*: `350000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Identity`  <a name="cfn-quicksight-agent-custompromptinterface-identity"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `5`
*Maximum*: `350000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelProfileId`  <a name="cfn-quicksight-agent-custompromptinterface-modelprofileid"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9-]{35}$`
*Minimum*: `36`
*Maximum*: `36`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutputStyle`  <a name="cfn-quicksight-agent-custompromptinterface-outputstyle"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `5`
*Maximum*: `350000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PromptSummary`  <a name="cfn-quicksight-agent-custompromptinterface-promptsummary"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QbsAwsAccountId`  <a name="cfn-quicksight-agent-custompromptinterface-qbsawsaccountid"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^QBS[0-9]{12}$`
*Minimum*: `15`
*Maximum*: `15`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResponseLength`  <a name="cfn-quicksight-agent-custompromptinterface-responselength"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `5`
*Maximum*: `350000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubscriptionId`  <a name="cfn-quicksight-agent-custompromptinterface-subscriptionid"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[a-z0-9]+$`
*Minimum*: `32`
*Maximum*: `32`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tone`  <a name="cfn-quicksight-agent-custompromptinterface-tone"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `5`
*Maximum*: `350000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
