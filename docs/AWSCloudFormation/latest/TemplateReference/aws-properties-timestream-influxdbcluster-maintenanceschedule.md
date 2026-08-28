---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-timestream-influxdbcluster-maintenanceschedule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Timestream::InfluxDBCluster MaintenanceSchedule
<a name="aws-properties-timestream-influxdbcluster-maintenanceschedule"></a>

<a name="aws-properties-timestream-influxdbcluster-maintenanceschedule-description"></a>The `MaintenanceSchedule` property type specifies Property description not available. for an [AWS::Timestream::InfluxDBCluster](aws-resource-timestream-influxdbcluster.md).

## Syntax
<a name="aws-properties-timestream-influxdbcluster-maintenanceschedule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-timestream-influxdbcluster-maintenanceschedule-syntax.json"></a>

```
{
  "[PreferredMaintenanceWindow](#cfn-timestream-influxdbcluster-maintenanceschedule-preferredmaintenancewindow)" : {{String}},
  "[Timezone](#cfn-timestream-influxdbcluster-maintenanceschedule-timezone)" : {{String}}
}
```

### YAML
<a name="aws-properties-timestream-influxdbcluster-maintenanceschedule-syntax.yaml"></a>

```
  [PreferredMaintenanceWindow](#cfn-timestream-influxdbcluster-maintenanceschedule-preferredmaintenancewindow): {{String}}
  [Timezone](#cfn-timestream-influxdbcluster-maintenanceschedule-timezone): {{String}}
```

## Properties
<a name="aws-properties-timestream-influxdbcluster-maintenanceschedule-properties"></a>

`PreferredMaintenanceWindow`  <a name="cfn-timestream-influxdbcluster-maintenanceschedule-preferredmaintenancewindow"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^$|^(Mon|Tue|Wed|Thu|Fri|Sat|Sun):([01]\d|2[0-3]):[0-5]\d-(Mon|Tue|Wed|Thu|Fri|Sat|Sun):([01]\d|2[0-3]):[0-5]\d$`
*Minimum*: `0`
*Maximum*: `19`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Timezone`  <a name="cfn-timestream-influxdbcluster-maintenanceschedule-timezone"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^(UTC|[A-Za-z_]+/[A-Za-z0-9_]+(/[A-Za-z0-9_]+)?)$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
