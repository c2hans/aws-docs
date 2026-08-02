---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-gameliftstreams-application-runtimeenvironment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GameLiftStreams::Application RuntimeEnvironment
<a name="aws-properties-gameliftstreams-application-runtimeenvironment"></a>

Configuration settings that identify the operating system for an application resource. This can also include a compatibility layer and other drivers.

A runtime environment can be one of the following:
+  For Linux applications
  +  Ubuntu 22.04 LTS (`Type=UBUNTU, Version=22_04_LTS`)
+  For Windows applications
  + Microsoft Windows Server 2022 Base (`Type=WINDOWS, Version=2022`)
  + Proton 10.0-4 (`Type=PROTON, Version=20260204`)
  + Proton 9.0-2 (`Type=PROTON, Version=20250516`)
  + Proton 8.0-5 (`Type=PROTON, Version=20241007`)
  + Proton 8.0-2c (`Type=PROTON, Version=20230704`)

## Syntax
<a name="aws-properties-gameliftstreams-application-runtimeenvironment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-gameliftstreams-application-runtimeenvironment-syntax.json"></a>

```
{
  "[Type](#cfn-gameliftstreams-application-runtimeenvironment-type)" : {{String}},
  "[Version](#cfn-gameliftstreams-application-runtimeenvironment-version)" : {{String}}
}
```

### YAML
<a name="aws-properties-gameliftstreams-application-runtimeenvironment-syntax.yaml"></a>

```
  [Type](#cfn-gameliftstreams-application-runtimeenvironment-type): {{String}}
  [Version](#cfn-gameliftstreams-application-runtimeenvironment-version): {{String}}
```

## Properties
<a name="aws-properties-gameliftstreams-application-runtimeenvironment-properties"></a>

`Type`  <a name="cfn-gameliftstreams-application-runtimeenvironment-type"></a>
The operating system and other drivers. For Proton, this also includes the Proton compatibility layer.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Version`  <a name="cfn-gameliftstreams-application-runtimeenvironment-version"></a>
Versioned container environment for the application operating system.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
