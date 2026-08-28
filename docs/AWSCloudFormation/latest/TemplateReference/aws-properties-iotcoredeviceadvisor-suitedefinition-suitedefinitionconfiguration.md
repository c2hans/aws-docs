---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTCoreDeviceAdvisor::SuiteDefinition SuiteDefinitionConfiguration
<a name="aws-properties-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration"></a>

The configuration of the Suite Definition. Listed below are the required elements of the `SuiteDefinitionConfiguration`.

 **devicePermissionRoleArn**
The device permission arn.
This is a required element.
**Type:** String

 **devices**
The list of configured devices under test. For more information on devices under test, see [DeviceUnderTest](https://amazonaws.com/iot/latest/apireference/API_iotdeviceadvisor_DeviceUnderTest.html)
Not a required element.
**Type:** List of devices under test

 **intendedForQualification**
The tests intended for qualification in a suite.
Not a required element.
**Type:** Boolean

 **rootGroup**
The test suite root group. For more information on creating and using root groups see the [Device Advisor workflow](https://docs.aws.amazon.com/iot/latest/developerguide/device-advisor-workflow.html).
This is a required element.
**Type:** String

 **suiteDefinitionName**
The Suite Definition Configuration name.
This is a required element.
**Type:** String

## Syntax
<a name="aws-properties-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration-syntax.json"></a>

```
{
  "[DevicePermissionRoleArn](#cfn-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration-devicepermissionrolearn)" : {{String}},
  "[Devices](#cfn-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration-devices)" : {{[ DeviceUnderTest, ... ]}},
  "[IntendedForQualification](#cfn-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration-intendedforqualification)" : {{Boolean}},
  "[RootGroup](#cfn-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration-rootgroup)" : {{String}},
  "[SuiteDefinitionName](#cfn-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration-suitedefinitionname)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration-syntax.yaml"></a>

```
  [DevicePermissionRoleArn](#cfn-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration-devicepermissionrolearn): {{String}}
  [Devices](#cfn-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration-devices): {{
    - DeviceUnderTest}}
  [IntendedForQualification](#cfn-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration-intendedforqualification): {{Boolean}}
  [RootGroup](#cfn-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration-rootgroup): {{String}}
  [SuiteDefinitionName](#cfn-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration-suitedefinitionname): {{String}}
```

## Properties
<a name="aws-properties-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration-properties"></a>

`DevicePermissionRoleArn`  <a name="cfn-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration-devicepermissionrolearn"></a>
Gets the device permission ARN. This is a required parameter.
*Required*: Yes
*Type*: String
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Devices`  <a name="cfn-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration-devices"></a>
Gets the devices configured.
*Required*: No
*Type*: Array of [DeviceUnderTest](aws-properties-iotcoredeviceadvisor-suitedefinition-deviceundertest.md)
*Minimum*: `0`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IntendedForQualification`  <a name="cfn-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration-intendedforqualification"></a>
Gets the tests intended for qualification in a suite.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RootGroup`  <a name="cfn-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration-rootgroup"></a>
Gets the test suite root group. This is a required parameter. For updating or creating the latest qualification suite, if `intendedForQualification` is set to true, `rootGroup` can be an empty string. If `intendedForQualification` is false, `rootGroup` cannot be an empty string. If `rootGroup` is empty, and `intendedForQualification` is set to true, all the qualification tests are included, and the configuration is default.
 For a qualification suite, the minimum length is 0, and the maximum is 2048. For a non-qualification suite, the minimum length is 1, and the maximum is 2048.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SuiteDefinitionName`  <a name="cfn-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration-suitedefinitionname"></a>
Gets the suite definition name. This is a required parameter.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
