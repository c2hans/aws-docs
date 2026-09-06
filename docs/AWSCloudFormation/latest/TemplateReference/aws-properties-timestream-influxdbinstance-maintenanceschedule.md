---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-timestream-influxdbinstance-maintenanceschedule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Timestream::InfluxDBInstance MaintenanceSchedule
<a name="aws-properties-timestream-influxdbinstance-maintenanceschedule"></a>

<a name="aws-properties-timestream-influxdbinstance-maintenanceschedule-description"></a>The `MaintenanceSchedule` property type specifies Property description not available. for an [AWS::Timestream::InfluxDBInstance](aws-resource-timestream-influxdbinstance.md).

## Syntax
<a name="aws-properties-timestream-influxdbinstance-maintenanceschedule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-timestream-influxdbinstance-maintenanceschedule-syntax.json"></a>

```
{
  "[PreferredMaintenanceWindow](#cfn-timestream-influxdbinstance-maintenanceschedule-preferredmaintenancewindow)" : {{String}},
  "[Timezone](#cfn-timestream-influxdbinstance-maintenanceschedule-timezone)" : {{String}}
}
```

### YAML
<a name="aws-properties-timestream-influxdbinstance-maintenanceschedule-syntax.yaml"></a>

```
  [PreferredMaintenanceWindow](#cfn-timestream-influxdbinstance-maintenanceschedule-preferredmaintenancewindow): {{String}}
  [Timezone](#cfn-timestream-influxdbinstance-maintenanceschedule-timezone): {{String}}
```

## Properties
<a name="aws-properties-timestream-influxdbinstance-maintenanceschedule-properties"></a>

`PreferredMaintenanceWindow`  <a name="cfn-timestream-influxdbinstance-maintenanceschedule-preferredmaintenancewindow"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^$|^(Mon|Tue|Wed|Thu|Fri|Sat|Sun):([01]\d|2[0-3]):[0-5]\d-(Mon|Tue|Wed|Thu|Fri|Sat|Sun):([01]\d|2[0-3]):[0-5]\d$`
*Minimum*: `0`
*Maximum*: `19`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Timezone`  <a name="cfn-timestream-influxdbinstance-maintenanceschedule-timezone"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^(UTC|[A-Za-z_]+/[A-Za-z0-9_]+(/[A-Za-z0-9_]+)?)$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
