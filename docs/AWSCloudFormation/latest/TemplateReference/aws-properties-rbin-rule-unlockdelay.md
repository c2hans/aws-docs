---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rbin-rule-unlockdelay.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Rbin::Rule UnlockDelay
<a name="aws-properties-rbin-rule-unlockdelay"></a>

Information about the retention rule unlock delay. The unlock delay is the period after which a retention rule can be modified or edited after it has been unlocked by a user with the required permissions. The retention rule can't be modified or deleted during the unlock delay.

## Syntax
<a name="aws-properties-rbin-rule-unlockdelay-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rbin-rule-unlockdelay-syntax.json"></a>

```
{
  "[UnlockDelayUnit](#cfn-rbin-rule-unlockdelay-unlockdelayunit)" : {{String}},
  "[UnlockDelayValue](#cfn-rbin-rule-unlockdelay-unlockdelayvalue)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-rbin-rule-unlockdelay-syntax.yaml"></a>

```
  [UnlockDelayUnit](#cfn-rbin-rule-unlockdelay-unlockdelayunit): {{String}}
  [UnlockDelayValue](#cfn-rbin-rule-unlockdelay-unlockdelayvalue): {{Integer}}
```

## Properties
<a name="aws-properties-rbin-rule-unlockdelay-properties"></a>

`UnlockDelayUnit`  <a name="cfn-rbin-rule-unlockdelay-unlockdelayunit"></a>
The unit of time in which to measure the unlock delay. Currently, the unlock delay can be measured only in days.
*Required*: No
*Type*: String
*Allowed values*: `DAYS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UnlockDelayValue`  <a name="cfn-rbin-rule-unlockdelay-unlockdelayvalue"></a>
The unlock delay period, measured in the unit specified for ** UnlockDelayUnit**.
*Required*: No
*Type*: Integer
*Minimum*: `7`
*Maximum*: `30`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
