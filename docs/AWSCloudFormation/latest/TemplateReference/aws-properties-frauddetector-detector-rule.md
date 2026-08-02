---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-frauddetector-detector-rule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FraudDetector::Detector Rule
<a name="aws-properties-frauddetector-detector-rule"></a>

A rule.

## Syntax
<a name="aws-properties-frauddetector-detector-rule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-frauddetector-detector-rule-syntax.json"></a>

```
{
  "[Arn](#cfn-frauddetector-detector-rule-arn)" : {{String}},
  "[CreatedTime](#cfn-frauddetector-detector-rule-createdtime)" : {{String}},
  "[Description](#cfn-frauddetector-detector-rule-description)" : {{String}},
  "[DetectorId](#cfn-frauddetector-detector-rule-detectorid)" : {{String}},
  "[Expression](#cfn-frauddetector-detector-rule-expression)" : {{String}},
  "[Language](#cfn-frauddetector-detector-rule-language)" : {{String}},
  "[LastUpdatedTime](#cfn-frauddetector-detector-rule-lastupdatedtime)" : {{String}},
  "[Outcomes](#cfn-frauddetector-detector-rule-outcomes)" : {{[ Outcome, ... ]}},
  "[RuleId](#cfn-frauddetector-detector-rule-ruleid)" : {{String}},
  "[RuleVersion](#cfn-frauddetector-detector-rule-ruleversion)" : {{String}},
  "[Tags](#cfn-frauddetector-detector-rule-tags)" : {{[ Tag, ... ]}}
}
```

### YAML
<a name="aws-properties-frauddetector-detector-rule-syntax.yaml"></a>

```
  [Arn](#cfn-frauddetector-detector-rule-arn): {{String}}
  [CreatedTime](#cfn-frauddetector-detector-rule-createdtime): {{String}}
  [Description](#cfn-frauddetector-detector-rule-description): {{String}}
  [DetectorId](#cfn-frauddetector-detector-rule-detectorid): {{String}}
  [Expression](#cfn-frauddetector-detector-rule-expression): {{String}}
  [Language](#cfn-frauddetector-detector-rule-language): {{String}}
  [LastUpdatedTime](#cfn-frauddetector-detector-rule-lastupdatedtime): {{String}}
  [Outcomes](#cfn-frauddetector-detector-rule-outcomes): {{
    - Outcome}}
  [RuleId](#cfn-frauddetector-detector-rule-ruleid): {{String}}
  [RuleVersion](#cfn-frauddetector-detector-rule-ruleversion): {{String}}
  [Tags](#cfn-frauddetector-detector-rule-tags): {{
    - Tag}}
```

## Properties
<a name="aws-properties-frauddetector-detector-rule-properties"></a>

`Arn`  <a name="cfn-frauddetector-detector-rule-arn"></a>
The rule ARN.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreatedTime`  <a name="cfn-frauddetector-detector-rule-createdtime"></a>
Timestamp for when the rule was created.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-frauddetector-detector-rule-description"></a>
The rule description.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DetectorId`  <a name="cfn-frauddetector-detector-rule-detectorid"></a>
The detector for which the rule is associated.
*Required*: No
*Type*: String
*Pattern*: `^[0-9a-z_-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Expression`  <a name="cfn-frauddetector-detector-rule-expression"></a>
The rule expression. A rule expression captures the business logic. For more information, see [Rule language reference](https://docs.aws.amazon.com/frauddetector/latest/ug/rule-language-reference.html).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Language`  <a name="cfn-frauddetector-detector-rule-language"></a>
The rule language.
Valid Value: DETECTORPL
*Required*: No
*Type*: String
*Allowed values*: `DETECTORPL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LastUpdatedTime`  <a name="cfn-frauddetector-detector-rule-lastupdatedtime"></a>
Timestamp for when the rule was last updated.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Outcomes`  <a name="cfn-frauddetector-detector-rule-outcomes"></a>
The rule outcome.
*Required*: No
*Type*: Array of [Outcome](aws-properties-frauddetector-detector-outcome.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuleId`  <a name="cfn-frauddetector-detector-rule-ruleid"></a>
The rule ID.
*Required*: No
*Type*: String
*Pattern*: `^[0-9a-z_-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuleVersion`  <a name="cfn-frauddetector-detector-rule-ruleversion"></a>
The rule version.
*Required*: No
*Type*: String
*Pattern*: `^([1-9][0-9]*)$`
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-frauddetector-detector-rule-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-frauddetector-detector-tag.md)
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
