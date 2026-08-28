---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotcoredeviceadvisor-suitedefinition-deviceundertest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTCoreDeviceAdvisor::SuiteDefinition DeviceUnderTest
<a name="aws-properties-iotcoredeviceadvisor-suitedefinition-deviceundertest"></a>

Information of a test device. A thing ARN, certificate ARN or device role ARN is required.

## Syntax
<a name="aws-properties-iotcoredeviceadvisor-suitedefinition-deviceundertest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotcoredeviceadvisor-suitedefinition-deviceundertest-syntax.json"></a>

```
{
  "[CertificateArn](#cfn-iotcoredeviceadvisor-suitedefinition-deviceundertest-certificatearn)" : {{String}},
  "[ThingArn](#cfn-iotcoredeviceadvisor-suitedefinition-deviceundertest-thingarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotcoredeviceadvisor-suitedefinition-deviceundertest-syntax.yaml"></a>

```
  [CertificateArn](#cfn-iotcoredeviceadvisor-suitedefinition-deviceundertest-certificatearn): {{String}}
  [ThingArn](#cfn-iotcoredeviceadvisor-suitedefinition-deviceundertest-thingarn): {{String}}
```

## Properties
<a name="aws-properties-iotcoredeviceadvisor-suitedefinition-deviceundertest-properties"></a>

`CertificateArn`  <a name="cfn-iotcoredeviceadvisor-suitedefinition-deviceundertest-certificatearn"></a>
Lists device's certificate ARN.
*Required*: No
*Type*: String
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ThingArn`  <a name="cfn-iotcoredeviceadvisor-suitedefinition-deviceundertest-thingarn"></a>
Lists device's thing ARN.
*Required*: No
*Type*: String
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
