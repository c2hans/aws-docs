---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-deadline-fleet-customermanagedfleetconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Deadline::Fleet CustomerManagedFleetConfiguration
<a name="aws-properties-deadline-fleet-customermanagedfleetconfiguration"></a>

The configuration details for a customer managed fleet.

## Syntax
<a name="aws-properties-deadline-fleet-customermanagedfleetconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-deadline-fleet-customermanagedfleetconfiguration-syntax.json"></a>

```
{
  "[AutoScalingConfiguration](#cfn-deadline-fleet-customermanagedfleetconfiguration-autoscalingconfiguration)" : {{CustomerManagedAutoScalingConfiguration}},
  "[Mode](#cfn-deadline-fleet-customermanagedfleetconfiguration-mode)" : {{String}},
  "[StorageProfileId](#cfn-deadline-fleet-customermanagedfleetconfiguration-storageprofileid)" : {{String}},
  "[TagPropagationMode](#cfn-deadline-fleet-customermanagedfleetconfiguration-tagpropagationmode)" : {{String}},
  "[WorkerCapabilities](#cfn-deadline-fleet-customermanagedfleetconfiguration-workercapabilities)" : {{CustomerManagedWorkerCapabilities}}
}
```

### YAML
<a name="aws-properties-deadline-fleet-customermanagedfleetconfiguration-syntax.yaml"></a>

```
  [AutoScalingConfiguration](#cfn-deadline-fleet-customermanagedfleetconfiguration-autoscalingconfiguration): {{
    CustomerManagedAutoScalingConfiguration}}
  [Mode](#cfn-deadline-fleet-customermanagedfleetconfiguration-mode): {{String}}
  [StorageProfileId](#cfn-deadline-fleet-customermanagedfleetconfiguration-storageprofileid): {{String}}
  [TagPropagationMode](#cfn-deadline-fleet-customermanagedfleetconfiguration-tagpropagationmode): {{String}}
  [WorkerCapabilities](#cfn-deadline-fleet-customermanagedfleetconfiguration-workercapabilities): {{
    CustomerManagedWorkerCapabilities}}
```

## Properties
<a name="aws-properties-deadline-fleet-customermanagedfleetconfiguration-properties"></a>

`AutoScalingConfiguration`  <a name="cfn-deadline-fleet-customermanagedfleetconfiguration-autoscalingconfiguration"></a>
The auto scaling configuration settings for the customer managed fleet.
*Required*: No
*Type*: [CustomerManagedAutoScalingConfiguration](aws-properties-deadline-fleet-customermanagedautoscalingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Mode`  <a name="cfn-deadline-fleet-customermanagedfleetconfiguration-mode"></a>
The Auto Scaling mode for the customer managed fleet.
*Required*: Yes
*Type*: String
*Allowed values*: `NO_SCALING | EVENT_BASED_AUTO_SCALING`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StorageProfileId`  <a name="cfn-deadline-fleet-customermanagedfleetconfiguration-storageprofileid"></a>
The storage profile ID for the customer managed fleet.
*Required*: No
*Type*: String
*Pattern*: `^sp-[0-9a-f]{32}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TagPropagationMode`  <a name="cfn-deadline-fleet-customermanagedfleetconfiguration-tagpropagationmode"></a>
The tag propagation mode for the customer managed fleet.
*Required*: No
*Type*: String
*Allowed values*: `NO_PROPAGATION | PROPAGATE_TAGS_TO_WORKERS_AT_LAUNCH`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WorkerCapabilities`  <a name="cfn-deadline-fleet-customermanagedfleetconfiguration-workercapabilities"></a>
The worker capabilities for the customer managed fleet.
*Required*: Yes
*Type*: [CustomerManagedWorkerCapabilities](aws-properties-deadline-fleet-customermanagedworkercapabilities.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
