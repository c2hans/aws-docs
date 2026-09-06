---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-arcregionswitch-plan-customactionlambdaconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ARCRegionSwitch::Plan CustomActionLambdaConfiguration
<a name="aws-properties-arcregionswitch-plan-customactionlambdaconfiguration"></a>

Configuration for AWS Lambda functions that perform custom actions during a Region switch.

## Syntax
<a name="aws-properties-arcregionswitch-plan-customactionlambdaconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-arcregionswitch-plan-customactionlambdaconfiguration-syntax.json"></a>

```
{
  "[Lambdas](#cfn-arcregionswitch-plan-customactionlambdaconfiguration-lambdas)" : {{[ Lambdas, ... ]}},
  "[RegionToRun](#cfn-arcregionswitch-plan-customactionlambdaconfiguration-regiontorun)" : {{String}},
  "[RetryIntervalMinutes](#cfn-arcregionswitch-plan-customactionlambdaconfiguration-retryintervalminutes)" : {{Number}},
  "[TimeoutMinutes](#cfn-arcregionswitch-plan-customactionlambdaconfiguration-timeoutminutes)" : {{Number}},
  "[Ungraceful](#cfn-arcregionswitch-plan-customactionlambdaconfiguration-ungraceful)" : {{LambdaUngraceful}}
}
```

### YAML
<a name="aws-properties-arcregionswitch-plan-customactionlambdaconfiguration-syntax.yaml"></a>

```
  [Lambdas](#cfn-arcregionswitch-plan-customactionlambdaconfiguration-lambdas): {{
    - Lambdas}}
  [RegionToRun](#cfn-arcregionswitch-plan-customactionlambdaconfiguration-regiontorun): {{String}}
  [RetryIntervalMinutes](#cfn-arcregionswitch-plan-customactionlambdaconfiguration-retryintervalminutes): {{Number}}
  [TimeoutMinutes](#cfn-arcregionswitch-plan-customactionlambdaconfiguration-timeoutminutes): {{Number}}
  [Ungraceful](#cfn-arcregionswitch-plan-customactionlambdaconfiguration-ungraceful): {{
    LambdaUngraceful}}
```

## Properties
<a name="aws-properties-arcregionswitch-plan-customactionlambdaconfiguration-properties"></a>

`Lambdas`  <a name="cfn-arcregionswitch-plan-customactionlambdaconfiguration-lambdas"></a>
The AWS Lambda functions for the execution block.
*Required*: Yes
*Type*: [Array](aws-properties-arcregionswitch-plan-lambdas.md) of [Lambdas](aws-properties-arcregionswitch-plan-lambdas.md)
*Minimum*: `1`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RegionToRun`  <a name="cfn-arcregionswitch-plan-customactionlambdaconfiguration-regiontorun"></a>
The AWS Region for the function to run in. For recovery workflows use `activatingRegion` or `deactivatingRegion`. For post-recovery workflows, use `activeRegion` (the Region with customer traffic) or `inactiveRegion` (the Region with no customer traffic).
*Required*: Yes
*Type*: String
*Allowed values*: `activatingRegion | deactivatingRegion | activeRegion | inactiveRegion`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RetryIntervalMinutes`  <a name="cfn-arcregionswitch-plan-customactionlambdaconfiguration-retryintervalminutes"></a>
The retry interval specified.
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeoutMinutes`  <a name="cfn-arcregionswitch-plan-customactionlambdaconfiguration-timeoutminutes"></a>
The timeout value specified for the configuration.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ungraceful`  <a name="cfn-arcregionswitch-plan-customactionlambdaconfiguration-ungraceful"></a>
The settings for ungraceful execution.
*Required*: No
*Type*: [LambdaUngraceful](aws-properties-arcregionswitch-plan-lambdaungraceful.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
