---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotmanagedintegrations-managedthing-capabilityreport.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTManagedIntegrations::ManagedThing CapabilityReport
<a name="aws-properties-iotmanagedintegrations-managedthing-capabilityreport"></a>

A report of the capabilities for the managed thing.

## Syntax
<a name="aws-properties-iotmanagedintegrations-managedthing-capabilityreport-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotmanagedintegrations-managedthing-capabilityreport-syntax.json"></a>

```
{
  "[Endpoints](#cfn-iotmanagedintegrations-managedthing-capabilityreport-endpoints)" : {{[ CapabilityReportEndpoint, ... ]}},
  "[NodeId](#cfn-iotmanagedintegrations-managedthing-capabilityreport-nodeid)" : {{String}},
  "[Version](#cfn-iotmanagedintegrations-managedthing-capabilityreport-version)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotmanagedintegrations-managedthing-capabilityreport-syntax.yaml"></a>

```
  [Endpoints](#cfn-iotmanagedintegrations-managedthing-capabilityreport-endpoints): {{
    - CapabilityReportEndpoint}}
  [NodeId](#cfn-iotmanagedintegrations-managedthing-capabilityreport-nodeid): {{String}}
  [Version](#cfn-iotmanagedintegrations-managedthing-capabilityreport-version): {{String}}
```

## Properties
<a name="aws-properties-iotmanagedintegrations-managedthing-capabilityreport-properties"></a>

`Endpoints`  <a name="cfn-iotmanagedintegrations-managedthing-capabilityreport-endpoints"></a>
The endpoints used in the capability report.
*Required*: Yes
*Type*: Array of [CapabilityReportEndpoint](aws-properties-iotmanagedintegrations-managedthing-capabilityreportendpoint.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NodeId`  <a name="cfn-iotmanagedintegrations-managedthing-capabilityreport-nodeid"></a>
The numeric identifier of the node.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9=_.,@\+\-/]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Version`  <a name="cfn-iotmanagedintegrations-managedthing-capabilityreport-version"></a>
The version of the capability report.
*Required*: Yes
*Type*: String
*Pattern*: `^1\.0\.0$`
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
