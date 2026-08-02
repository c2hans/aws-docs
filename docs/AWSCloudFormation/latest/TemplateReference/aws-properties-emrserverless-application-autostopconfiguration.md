---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrserverless-application-autostopconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRServerless::Application AutoStopConfiguration
<a name="aws-properties-emrserverless-application-autostopconfiguration"></a>

The configuration for an application to automatically stop after a certain amount of time being idle.

## Syntax
<a name="aws-properties-emrserverless-application-autostopconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrserverless-application-autostopconfiguration-syntax.json"></a>

```
{
  "[Enabled](#cfn-emrserverless-application-autostopconfiguration-enabled)" : {{Boolean}},
  "[IdleTimeoutMinutes](#cfn-emrserverless-application-autostopconfiguration-idletimeoutminutes)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-emrserverless-application-autostopconfiguration-syntax.yaml"></a>

```
  [Enabled](#cfn-emrserverless-application-autostopconfiguration-enabled): {{Boolean}}
  [IdleTimeoutMinutes](#cfn-emrserverless-application-autostopconfiguration-idletimeoutminutes): {{Integer}}
```

## Properties
<a name="aws-properties-emrserverless-application-autostopconfiguration-properties"></a>

`Enabled`  <a name="cfn-emrserverless-application-autostopconfiguration-enabled"></a>
Enables the application to automatically stop after a certain amount of time being idle. Defaults to true.
*Required*: No
*Type*: Boolean
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`IdleTimeoutMinutes`  <a name="cfn-emrserverless-application-autostopconfiguration-idletimeoutminutes"></a>
The amount of idle time in minutes after which your application will automatically stop. Defaults to 15 minutes.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `10080`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)
