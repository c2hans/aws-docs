---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-arcregionswitch-plan-ssmsendcommandconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ARCRegionSwitch::Plan SsmSendCommandConfiguration
<a name="aws-properties-arcregionswitch-plan-ssmsendcommandconfiguration"></a>

Configuration for an AWS Systems Manager `SendCommand` execution block in a Region switch plan. This execution block runs a Systems Manager document on the managed nodes that you target in each AWS Region of the plan.

## Syntax
<a name="aws-properties-arcregionswitch-plan-ssmsendcommandconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-arcregionswitch-plan-ssmsendcommandconfiguration-syntax.json"></a>

```
{
  "[RegionDocuments](#cfn-arcregionswitch-plan-ssmsendcommandconfiguration-regiondocuments)" : {{{{{Key}}: {{Value}}, ...}}},
  "[RetryIntervalMinutes](#cfn-arcregionswitch-plan-ssmsendcommandconfiguration-retryintervalminutes)" : {{Number}},
  "[TimeoutMinutes](#cfn-arcregionswitch-plan-ssmsendcommandconfiguration-timeoutminutes)" : {{Number}},
  "[Ungraceful](#cfn-arcregionswitch-plan-ssmsendcommandconfiguration-ungraceful)" : {{SsmSendCommandUngraceful}}
}
```

### YAML
<a name="aws-properties-arcregionswitch-plan-ssmsendcommandconfiguration-syntax.yaml"></a>

```
  [RegionDocuments](#cfn-arcregionswitch-plan-ssmsendcommandconfiguration-regiondocuments): {{
    {{Key}}: {{Value}}}}
  [RetryIntervalMinutes](#cfn-arcregionswitch-plan-ssmsendcommandconfiguration-retryintervalminutes): {{Number}}
  [TimeoutMinutes](#cfn-arcregionswitch-plan-ssmsendcommandconfiguration-timeoutminutes): {{Number}}
  [Ungraceful](#cfn-arcregionswitch-plan-ssmsendcommandconfiguration-ungraceful): {{
    SsmSendCommandUngraceful}}
```

## Properties
<a name="aws-properties-arcregionswitch-plan-ssmsendcommandconfiguration-properties"></a>

`RegionDocuments`  <a name="cfn-arcregionswitch-plan-ssmsendcommandconfiguration-regiondocuments"></a>
The Systems Manager document and target configuration for each AWS Region in the plan. Provide an entry for each AWS Region that you want the command to run in.
*Required*: Yes
*Type*: Object of [SsmDocumentConfig](aws-properties-arcregionswitch-plan-ssmdocumentconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RetryIntervalMinutes`  <a name="cfn-arcregionswitch-plan-ssmsendcommandconfiguration-retryintervalminutes"></a>
How often, in minutes, Region switch retries the command if it returns a failure.
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeoutMinutes`  <a name="cfn-arcregionswitch-plan-ssmsendcommandconfiguration-timeoutminutes"></a>
The timeout value specified for the configuration.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ungraceful`  <a name="cfn-arcregionswitch-plan-ssmsendcommandconfiguration-ungraceful"></a>
Specifies the settings that determine how the execution block behaves when the plan runs ungracefully, such as whether to skip the command.
*Required*: No
*Type*: [SsmSendCommandUngraceful](aws-properties-arcregionswitch-plan-ssmsendcommandungraceful.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
