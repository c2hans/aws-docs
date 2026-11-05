---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-timestream-influxdbcluster-membermodecount.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Timestream::InfluxDBCluster MemberModeCount
<a name="aws-properties-timestream-influxdbcluster-membermodecount"></a>

<a name="aws-properties-timestream-influxdbcluster-membermodecount-description"></a>The `MemberModeCount` property type specifies Property description not available. for an [AWS::Timestream::InfluxDBCluster](aws-resource-timestream-influxdbcluster.md).

## Syntax
<a name="aws-properties-timestream-influxdbcluster-membermodecount-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-timestream-influxdbcluster-membermodecount-syntax.json"></a>

```
{
  "[Count](#cfn-timestream-influxdbcluster-membermodecount-count)" : {{Integer}},
  "[Mode](#cfn-timestream-influxdbcluster-membermodecount-mode)" : {{String}}
}
```

### YAML
<a name="aws-properties-timestream-influxdbcluster-membermodecount-syntax.yaml"></a>

```
  [Count](#cfn-timestream-influxdbcluster-membermodecount-count): {{Integer}}
  [Mode](#cfn-timestream-influxdbcluster-membermodecount-mode): {{String}}
```

## Properties
<a name="aws-properties-timestream-influxdbcluster-membermodecount-properties"></a>

`Count`  <a name="cfn-timestream-influxdbcluster-membermodecount-count"></a>
Property description not available.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Mode`  <a name="cfn-timestream-influxdbcluster-membermodecount-mode"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `PRIMARY | STANDBY | REPLICA | INGEST | QUERY | COMPACT | PROCESS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
