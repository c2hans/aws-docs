---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-agent-custompromptprofile.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Agent CustomPromptProfile
<a name="aws-properties-quicksight-agent-custompromptprofile"></a>

A reference to an existing custom prompt profile.

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
The identifier of the model profile.
*Required*: Yes
*Type*: String
*Maximum*: `36`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QbsAwsAccountId`  <a name="cfn-quicksight-agent-custompromptprofile-qbsawsaccountid"></a>
The AWS account ID for the Q Business service.
*Required*: Yes
*Type*: String
*Pattern*: `^QBS[0-9]{12}$`
*Maximum*: `15`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubscriptionId`  <a name="cfn-quicksight-agent-custompromptprofile-subscriptionid"></a>
The subscription identifier.
*Required*: Yes
*Type*: String
*Maximum*: `32`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
