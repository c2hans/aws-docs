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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
