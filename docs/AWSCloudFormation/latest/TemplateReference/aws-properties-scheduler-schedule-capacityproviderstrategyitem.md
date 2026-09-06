---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-scheduler-schedule-capacityproviderstrategyitem.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Scheduler::Schedule CapacityProviderStrategyItem
<a name="aws-properties-scheduler-schedule-capacityproviderstrategyitem"></a>

The details of a capacity provider strategy.

## Syntax
<a name="aws-properties-scheduler-schedule-capacityproviderstrategyitem-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-scheduler-schedule-capacityproviderstrategyitem-syntax.json"></a>

```
{
  "[Base](#cfn-scheduler-schedule-capacityproviderstrategyitem-base)" : {{Number}},
  "[CapacityProvider](#cfn-scheduler-schedule-capacityproviderstrategyitem-capacityprovider)" : {{String}},
  "[Weight](#cfn-scheduler-schedule-capacityproviderstrategyitem-weight)" : {{Number}}
}
```

### YAML
<a name="aws-properties-scheduler-schedule-capacityproviderstrategyitem-syntax.yaml"></a>

```
  [Base](#cfn-scheduler-schedule-capacityproviderstrategyitem-base): {{Number}}
  [CapacityProvider](#cfn-scheduler-schedule-capacityproviderstrategyitem-capacityprovider): {{String}}
  [Weight](#cfn-scheduler-schedule-capacityproviderstrategyitem-weight): {{Number}}
```

## Properties
<a name="aws-properties-scheduler-schedule-capacityproviderstrategyitem-properties"></a>

`Base`  <a name="cfn-scheduler-schedule-capacityproviderstrategyitem-base"></a>
The base value designates how many tasks, at a minimum, to run on the specified capacity provider. Only one capacity provider in a capacity provider strategy can have a base defined. If no value is specified, the default value of `0` is used.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `100000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CapacityProvider`  <a name="cfn-scheduler-schedule-capacityproviderstrategyitem-capacityprovider"></a>
The short name of the capacity provider.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Weight`  <a name="cfn-scheduler-schedule-capacityproviderstrategyitem-weight"></a>
The weight value designates the relative percentage of the total number of tasks launched that should use the specified capacity provider. The weight value is taken into consideration after the base value, if defined, is satisfied.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
