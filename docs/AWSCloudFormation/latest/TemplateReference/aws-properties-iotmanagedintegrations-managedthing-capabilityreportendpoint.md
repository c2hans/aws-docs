---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotmanagedintegrations-managedthing-capabilityreportendpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTManagedIntegrations::ManagedThing CapabilityReportEndpoint
<a name="aws-properties-iotmanagedintegrations-managedthing-capabilityreportendpoint"></a>

The endpoints used in the capability report.

## Syntax
<a name="aws-properties-iotmanagedintegrations-managedthing-capabilityreportendpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotmanagedintegrations-managedthing-capabilityreportendpoint-syntax.json"></a>

```
{
  "[Capabilities](#cfn-iotmanagedintegrations-managedthing-capabilityreportendpoint-capabilities)" : {{[ CapabilityReportCapability, ... ]}},
  "[DeviceTypes](#cfn-iotmanagedintegrations-managedthing-capabilityreportendpoint-devicetypes)" : {{[ String, ... ]}},
  "[Id](#cfn-iotmanagedintegrations-managedthing-capabilityreportendpoint-id)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotmanagedintegrations-managedthing-capabilityreportendpoint-syntax.yaml"></a>

```
  [Capabilities](#cfn-iotmanagedintegrations-managedthing-capabilityreportendpoint-capabilities): {{
    - CapabilityReportCapability}}
  [DeviceTypes](#cfn-iotmanagedintegrations-managedthing-capabilityreportendpoint-devicetypes): {{
    - String}}
  [Id](#cfn-iotmanagedintegrations-managedthing-capabilityreportendpoint-id): {{String}}
```

## Properties
<a name="aws-properties-iotmanagedintegrations-managedthing-capabilityreportendpoint-properties"></a>

`Capabilities`  <a name="cfn-iotmanagedintegrations-managedthing-capabilityreportendpoint-capabilities"></a>
The capabilities used in the capability report.
*Required*: Yes
*Type*: Array of [CapabilityReportCapability](aws-properties-iotmanagedintegrations-managedthing-capabilityreportcapability.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeviceTypes`  <a name="cfn-iotmanagedintegrations-managedthing-capabilityreportendpoint-devicetypes"></a>
The type of device.
*Required*: Yes
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `256 | 50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Id`  <a name="cfn-iotmanagedintegrations-managedthing-capabilityreportendpoint-id"></a>
The id of the endpoint used in the capability report.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-zA-Z]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
