---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dlm-lifecyclepolicy-fastrestorerule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DLM::LifecyclePolicy FastRestoreRule
<a name="aws-properties-dlm-lifecyclepolicy-fastrestorerule"></a>

**[Custom snapshot policies only]** Specifies a rule for enabling fast snapshot restore for snapshots created by snapshot policies. You can enable fast snapshot restore based on either a count or a time interval.

## Syntax
<a name="aws-properties-dlm-lifecyclepolicy-fastrestorerule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dlm-lifecyclepolicy-fastrestorerule-syntax.json"></a>

```
{
  "[AvailabilityZoneIds](#cfn-dlm-lifecyclepolicy-fastrestorerule-availabilityzoneids)" : {{[ String, ... ]}},
  "[AvailabilityZones](#cfn-dlm-lifecyclepolicy-fastrestorerule-availabilityzones)" : {{[ String, ... ]}},
  "[Count](#cfn-dlm-lifecyclepolicy-fastrestorerule-count)" : {{Integer}},
  "[Interval](#cfn-dlm-lifecyclepolicy-fastrestorerule-interval)" : {{Integer}},
  "[IntervalUnit](#cfn-dlm-lifecyclepolicy-fastrestorerule-intervalunit)" : {{String}}
}
```

### YAML
<a name="aws-properties-dlm-lifecyclepolicy-fastrestorerule-syntax.yaml"></a>

```
  [AvailabilityZoneIds](#cfn-dlm-lifecyclepolicy-fastrestorerule-availabilityzoneids): {{
    - String}}
  [AvailabilityZones](#cfn-dlm-lifecyclepolicy-fastrestorerule-availabilityzones): {{
    - String}}
  [Count](#cfn-dlm-lifecyclepolicy-fastrestorerule-count): {{Integer}}
  [Interval](#cfn-dlm-lifecyclepolicy-fastrestorerule-interval): {{Integer}}
  [IntervalUnit](#cfn-dlm-lifecyclepolicy-fastrestorerule-intervalunit): {{String}}
```

## Properties
<a name="aws-properties-dlm-lifecyclepolicy-fastrestorerule-properties"></a>

`AvailabilityZoneIds`  <a name="cfn-dlm-lifecyclepolicy-fastrestorerule-availabilityzoneids"></a>
The Availability Zone Ids in which to enable fast snapshot restore.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AvailabilityZones`  <a name="cfn-dlm-lifecyclepolicy-fastrestorerule-availabilityzones"></a>
The Availability Zones in which to enable fast snapshot restore.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Count`  <a name="cfn-dlm-lifecyclepolicy-fastrestorerule-count"></a>
The number of snapshots to be enabled with fast snapshot restore.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Interval`  <a name="cfn-dlm-lifecyclepolicy-fastrestorerule-interval"></a>
The amount of time to enable fast snapshot restore. The maximum is 100 years. This is equivalent to 1200 months, 5200 weeks, or 36500 days.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IntervalUnit`  <a name="cfn-dlm-lifecyclepolicy-fastrestorerule-intervalunit"></a>
The unit of time for enabling fast snapshot restore.
*Required*: No
*Type*: String
*Allowed values*: `HOURS | DAYS | WEEKS | MONTHS | YEARS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
