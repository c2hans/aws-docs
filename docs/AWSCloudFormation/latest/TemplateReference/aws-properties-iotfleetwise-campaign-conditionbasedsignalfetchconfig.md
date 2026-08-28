---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotfleetwise-campaign-conditionbasedsignalfetchconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTFleetWise::Campaign ConditionBasedSignalFetchConfig
<a name="aws-properties-iotfleetwise-campaign-conditionbasedsignalfetchconfig"></a>

Specifies the condition under which a signal fetch occurs.

## Syntax
<a name="aws-properties-iotfleetwise-campaign-conditionbasedsignalfetchconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotfleetwise-campaign-conditionbasedsignalfetchconfig-syntax.json"></a>

```
{
  "[ConditionExpression](#cfn-iotfleetwise-campaign-conditionbasedsignalfetchconfig-conditionexpression)" : {{String}},
  "[TriggerMode](#cfn-iotfleetwise-campaign-conditionbasedsignalfetchconfig-triggermode)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotfleetwise-campaign-conditionbasedsignalfetchconfig-syntax.yaml"></a>

```
  [ConditionExpression](#cfn-iotfleetwise-campaign-conditionbasedsignalfetchconfig-conditionexpression): {{String}}
  [TriggerMode](#cfn-iotfleetwise-campaign-conditionbasedsignalfetchconfig-triggermode): {{String}}
```

## Properties
<a name="aws-properties-iotfleetwise-campaign-conditionbasedsignalfetchconfig-properties"></a>

`ConditionExpression`  <a name="cfn-iotfleetwise-campaign-conditionbasedsignalfetchconfig-conditionexpression"></a>
The condition that must be satisfied to trigger a signal fetch.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TriggerMode`  <a name="cfn-iotfleetwise-campaign-conditionbasedsignalfetchconfig-triggermode"></a>
Indicates the mode in which the signal fetch is triggered.
*Required*: Yes
*Type*: String
*Allowed values*: `ALWAYS | RISING_EDGE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
