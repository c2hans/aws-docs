---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-eventtrigger-period.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::EventTrigger Period
<a name="aws-properties-customerprofiles-eventtrigger-period"></a>

Defines a limit and the time period during which it is enforced.

## Syntax
<a name="aws-properties-customerprofiles-eventtrigger-period-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-eventtrigger-period-syntax.json"></a>

```
{
  "[MaxInvocationsPerProfile](#cfn-customerprofiles-eventtrigger-period-maxinvocationsperprofile)" : {{Integer}},
  "[Unit](#cfn-customerprofiles-eventtrigger-period-unit)" : {{String}},
  "[Unlimited](#cfn-customerprofiles-eventtrigger-period-unlimited)" : {{Boolean}},
  "[Value](#cfn-customerprofiles-eventtrigger-period-value)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-customerprofiles-eventtrigger-period-syntax.yaml"></a>

```
  [MaxInvocationsPerProfile](#cfn-customerprofiles-eventtrigger-period-maxinvocationsperprofile): {{Integer}}
  [Unit](#cfn-customerprofiles-eventtrigger-period-unit): {{String}}
  [Unlimited](#cfn-customerprofiles-eventtrigger-period-unlimited): {{Boolean}}
  [Value](#cfn-customerprofiles-eventtrigger-period-value): {{Integer}}
```

## Properties
<a name="aws-properties-customerprofiles-eventtrigger-period-properties"></a>

`MaxInvocationsPerProfile`  <a name="cfn-customerprofiles-eventtrigger-period-maxinvocationsperprofile"></a>
The maximum allowed number of destination invocations per profile.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Unit`  <a name="cfn-customerprofiles-eventtrigger-period-unit"></a>
The unit of time.
*Required*: Yes
*Type*: String
*Allowed values*: `MINUTES | HOURS | DAYS | WEEKS | MONTHS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Unlimited`  <a name="cfn-customerprofiles-eventtrigger-period-unlimited"></a>
If set to true, there is no limit on the number of destination invocations per profile. The default is false.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-customerprofiles-eventtrigger-period-value"></a>
The amount of time of the specified unit.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `60`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
