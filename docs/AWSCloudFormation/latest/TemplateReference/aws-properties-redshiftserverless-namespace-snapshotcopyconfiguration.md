---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-redshiftserverless-namespace-snapshotcopyconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RedshiftServerless::Namespace SnapshotCopyConfiguration
<a name="aws-properties-redshiftserverless-namespace-snapshotcopyconfiguration"></a>

The object that you configure to copy snapshots from one namespace to a namespace in another AWS Region.

## Syntax
<a name="aws-properties-redshiftserverless-namespace-snapshotcopyconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-redshiftserverless-namespace-snapshotcopyconfiguration-syntax.json"></a>

```
{
  "[DestinationKmsKeyId](#cfn-redshiftserverless-namespace-snapshotcopyconfiguration-destinationkmskeyid)" : {{String}},
  "[DestinationRegion](#cfn-redshiftserverless-namespace-snapshotcopyconfiguration-destinationregion)" : {{String}},
  "[SnapshotRetentionPeriod](#cfn-redshiftserverless-namespace-snapshotcopyconfiguration-snapshotretentionperiod)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-redshiftserverless-namespace-snapshotcopyconfiguration-syntax.yaml"></a>

```
  [DestinationKmsKeyId](#cfn-redshiftserverless-namespace-snapshotcopyconfiguration-destinationkmskeyid): {{String}}
  [DestinationRegion](#cfn-redshiftserverless-namespace-snapshotcopyconfiguration-destinationregion): {{String}}
  [SnapshotRetentionPeriod](#cfn-redshiftserverless-namespace-snapshotcopyconfiguration-snapshotretentionperiod): {{Integer}}
```

## Properties
<a name="aws-properties-redshiftserverless-namespace-snapshotcopyconfiguration-properties"></a>

`DestinationKmsKeyId`  <a name="cfn-redshiftserverless-namespace-snapshotcopyconfiguration-destinationkmskeyid"></a>
The ID of the KMS key to use to encrypt your snapshots in the destination AWS Region.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DestinationRegion`  <a name="cfn-redshiftserverless-namespace-snapshotcopyconfiguration-destinationregion"></a>
The destination AWS Region to copy snapshots to.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SnapshotRetentionPeriod`  <a name="cfn-redshiftserverless-namespace-snapshotcopyconfiguration-snapshotretentionperiod"></a>
The retention period of snapshots that are copied to the destination AWS Region.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
