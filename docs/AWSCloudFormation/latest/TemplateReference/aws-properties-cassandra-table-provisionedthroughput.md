---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cassandra-table-provisionedthroughput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cassandra::Table ProvisionedThroughput
<a name="aws-properties-cassandra-table-provisionedthroughput"></a>

The provisioned throughput for the table, which consists of `ReadCapacityUnits` and `WriteCapacityUnits`.

## Syntax
<a name="aws-properties-cassandra-table-provisionedthroughput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cassandra-table-provisionedthroughput-syntax.json"></a>

```
{
  "[ReadCapacityUnits](#cfn-cassandra-table-provisionedthroughput-readcapacityunits)" : {{Integer}},
  "[WriteCapacityUnits](#cfn-cassandra-table-provisionedthroughput-writecapacityunits)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-cassandra-table-provisionedthroughput-syntax.yaml"></a>

```
  [ReadCapacityUnits](#cfn-cassandra-table-provisionedthroughput-readcapacityunits): {{Integer}}
  [WriteCapacityUnits](#cfn-cassandra-table-provisionedthroughput-writecapacityunits): {{Integer}}
```

## Properties
<a name="aws-properties-cassandra-table-provisionedthroughput-properties"></a>

`ReadCapacityUnits`  <a name="cfn-cassandra-table-provisionedthroughput-readcapacityunits"></a>
The amount of read capacity that's provisioned for the table. For more information, see [Read/write capacity mode](https://docs.aws.amazon.com/keyspaces/latest/devguide/ReadWriteCapacityMode.html) in the *Amazon Keyspaces Developer Guide*.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WriteCapacityUnits`  <a name="cfn-cassandra-table-provisionedthroughput-writecapacityunits"></a>
The amount of write capacity that's provisioned for the table. For more information, see [Read/write capacity mode](https://docs.aws.amazon.com/keyspaces/latest/devguide/ReadWriteCapacityMode.html) in the *Amazon Keyspaces Developer Guide*.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
