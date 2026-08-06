---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-eventsourcemapping-provisionedpollerconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::EventSourceMapping ProvisionedPollerConfig
<a name="aws-properties-lambda-eventsourcemapping-provisionedpollerconfig"></a>

The [ provisioned mode](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventsourcemapping.html#invocation-eventsourcemapping-provisioned-mode) configuration for the event source. Use Provisioned Mode to customize the minimum and maximum number of event pollers for your event source.

## Syntax
<a name="aws-properties-lambda-eventsourcemapping-provisionedpollerconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-eventsourcemapping-provisionedpollerconfig-syntax.json"></a>

```
{
  "[MaximumPollers](#cfn-lambda-eventsourcemapping-provisionedpollerconfig-maximumpollers)" : {{Integer}},
  "[MinimumPollers](#cfn-lambda-eventsourcemapping-provisionedpollerconfig-minimumpollers)" : {{Integer}},
  "[PollerGroupName](#cfn-lambda-eventsourcemapping-provisionedpollerconfig-pollergroupname)" : {{String}}
}
```

### YAML
<a name="aws-properties-lambda-eventsourcemapping-provisionedpollerconfig-syntax.yaml"></a>

```
  [MaximumPollers](#cfn-lambda-eventsourcemapping-provisionedpollerconfig-maximumpollers): {{Integer}}
  [MinimumPollers](#cfn-lambda-eventsourcemapping-provisionedpollerconfig-minimumpollers): {{Integer}}
  [PollerGroupName](#cfn-lambda-eventsourcemapping-provisionedpollerconfig-pollergroupname): {{String}}
```

## Properties
<a name="aws-properties-lambda-eventsourcemapping-provisionedpollerconfig-properties"></a>

`MaximumPollers`  <a name="cfn-lambda-eventsourcemapping-provisionedpollerconfig-maximumpollers"></a>
The maximum number of event pollers this event source can scale up to. For Amazon SQS event source mappings, the accepted range is between 2 and 10,000, with a default of 200. For Amazon MSK and self-managed Apache Kafka event source mappings, the accepted range is between 1 and 2,000, with a default of 200.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinimumPollers`  <a name="cfn-lambda-eventsourcemapping-provisionedpollerconfig-minimumpollers"></a>
The minimum number of event pollers this event source can scale down to. For Amazon SQS events source mappings, default is 2, and minimum 2 required. For Amazon MSK and self-managed Apache Kafka event source mappings, default is 1.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PollerGroupName`  <a name="cfn-lambda-eventsourcemapping-provisionedpollerconfig-pollergroupname"></a>
(Amazon MSK and self-managed Apache Kafka) The name of the provisioned poller group. Use this option to group multiple ESMs within the event source's VPC to share Event Poller Unit (EPU) capacity. You can use this option to optimize Provisioned mode costs for your ESMs. You can group up to 100 ESMs per poller group and aggregate maximum pollers across all ESMs in a group cannot exceed 2000.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
