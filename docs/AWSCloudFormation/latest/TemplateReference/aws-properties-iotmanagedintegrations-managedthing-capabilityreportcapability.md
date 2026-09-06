---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotmanagedintegrations-managedthing-capabilityreportcapability.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTManagedIntegrations::ManagedThing CapabilityReportCapability
<a name="aws-properties-iotmanagedintegrations-managedthing-capabilityreportcapability"></a>

The capability used in capability report.

## Syntax
<a name="aws-properties-iotmanagedintegrations-managedthing-capabilityreportcapability-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotmanagedintegrations-managedthing-capabilityreportcapability-syntax.json"></a>

```
{
  "[Actions](#cfn-iotmanagedintegrations-managedthing-capabilityreportcapability-actions)" : {{[ String, ... ]}},
  "[Events](#cfn-iotmanagedintegrations-managedthing-capabilityreportcapability-events)" : {{[ String, ... ]}},
  "[Id](#cfn-iotmanagedintegrations-managedthing-capabilityreportcapability-id)" : {{String}},
  "[Name](#cfn-iotmanagedintegrations-managedthing-capabilityreportcapability-name)" : {{String}},
  "[Properties](#cfn-iotmanagedintegrations-managedthing-capabilityreportcapability-properties)" : {{[ String, ... ]}},
  "[Version](#cfn-iotmanagedintegrations-managedthing-capabilityreportcapability-version)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotmanagedintegrations-managedthing-capabilityreportcapability-syntax.yaml"></a>

```
  [Actions](#cfn-iotmanagedintegrations-managedthing-capabilityreportcapability-actions): {{
    - String}}
  [Events](#cfn-iotmanagedintegrations-managedthing-capabilityreportcapability-events): {{
    - String}}
  [Id](#cfn-iotmanagedintegrations-managedthing-capabilityreportcapability-id): {{String}}
  [Name](#cfn-iotmanagedintegrations-managedthing-capabilityreportcapability-name): {{String}}
  [Properties](#cfn-iotmanagedintegrations-managedthing-capabilityreportcapability-properties): {{
    - String}}
  [Version](#cfn-iotmanagedintegrations-managedthing-capabilityreportcapability-version): {{String}}
```

## Properties
<a name="aws-properties-iotmanagedintegrations-managedthing-capabilityreportcapability-properties"></a>

`Actions`  <a name="cfn-iotmanagedintegrations-managedthing-capabilityreportcapability-actions"></a>
The capability actions used in the capability report.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1 | 0`
*Maximum*: `128 | 100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Events`  <a name="cfn-iotmanagedintegrations-managedthing-capabilityreportcapability-events"></a>
The capability events used in the capability report.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1 | 0`
*Maximum*: `128 | 100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Id`  <a name="cfn-iotmanagedintegrations-managedthing-capabilityreportcapability-id"></a>
The id of the schema version.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9.\/]+(@(\d+\.\d+|\$latest))?$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-iotmanagedintegrations-managedthing-capabilityreportcapability-name"></a>
The name of the capability.
*Required*: Yes
*Type*: String
*Pattern*: `^[/a-zA-Z0-9\._ ]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Properties`  <a name="cfn-iotmanagedintegrations-managedthing-capabilityreportcapability-properties"></a>
The capability properties used in the capability report.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1 | 0`
*Maximum*: `128 | 100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Version`  <a name="cfn-iotmanagedintegrations-managedthing-capabilityreportcapability-version"></a>
The version of the capability.
*Required*: Yes
*Type*: String
*Pattern*: `^(0|[1-9][0-9]*)$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
