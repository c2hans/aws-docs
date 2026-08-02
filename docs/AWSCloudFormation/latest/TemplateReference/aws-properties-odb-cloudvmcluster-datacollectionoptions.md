---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-odb-cloudvmcluster-datacollectionoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ODB::CloudVmCluster DataCollectionOptions
<a name="aws-properties-odb-cloudvmcluster-datacollectionoptions"></a>

Information about the data collection options enabled for a VM cluster.

## Syntax
<a name="aws-properties-odb-cloudvmcluster-datacollectionoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-odb-cloudvmcluster-datacollectionoptions-syntax.json"></a>

```
{
  "[IsDiagnosticsEventsEnabled](#cfn-odb-cloudvmcluster-datacollectionoptions-isdiagnosticseventsenabled)" : {{Boolean}},
  "[IsHealthMonitoringEnabled](#cfn-odb-cloudvmcluster-datacollectionoptions-ishealthmonitoringenabled)" : {{Boolean}},
  "[IsIncidentLogsEnabled](#cfn-odb-cloudvmcluster-datacollectionoptions-isincidentlogsenabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-odb-cloudvmcluster-datacollectionoptions-syntax.yaml"></a>

```
  [IsDiagnosticsEventsEnabled](#cfn-odb-cloudvmcluster-datacollectionoptions-isdiagnosticseventsenabled): {{Boolean}}
  [IsHealthMonitoringEnabled](#cfn-odb-cloudvmcluster-datacollectionoptions-ishealthmonitoringenabled): {{Boolean}}
  [IsIncidentLogsEnabled](#cfn-odb-cloudvmcluster-datacollectionoptions-isincidentlogsenabled): {{Boolean}}
```

## Properties
<a name="aws-properties-odb-cloudvmcluster-datacollectionoptions-properties"></a>

`IsDiagnosticsEventsEnabled`  <a name="cfn-odb-cloudvmcluster-datacollectionoptions-isdiagnosticseventsenabled"></a>
Specifies whether diagnostic collection is enabled for the VM cluster.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IsHealthMonitoringEnabled`  <a name="cfn-odb-cloudvmcluster-datacollectionoptions-ishealthmonitoringenabled"></a>
Specifies whether health monitoring is enabled for the VM cluster.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IsIncidentLogsEnabled`  <a name="cfn-odb-cloudvmcluster-datacollectionoptions-isincidentlogsenabled"></a>
Specifies whether incident logs are enabled for the VM cluster.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
