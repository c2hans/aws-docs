---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-redshiftserverless-workgroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RedshiftServerless::Workgroup
<a name="aws-resource-redshiftserverless-workgroup"></a>

The collection of compute resources in Amazon Redshift Serverless.

## Syntax
<a name="aws-resource-redshiftserverless-workgroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-redshiftserverless-workgroup-syntax.json"></a>

```
{
  "Type" : "AWS::RedshiftServerless::Workgroup",
  "Properties" : {
      "[BaseCapacity](#cfn-redshiftserverless-workgroup-basecapacity)" : {{Integer}},
      "[ConfigParameters](#cfn-redshiftserverless-workgroup-configparameters)" : {{[ ConfigParameter, ... ]}},
      "[EnhancedVpcRouting](#cfn-redshiftserverless-workgroup-enhancedvpcrouting)" : {{Boolean}},
      "[MaxCapacity](#cfn-redshiftserverless-workgroup-maxcapacity)" : {{Integer}},
      "[NamespaceName](#cfn-redshiftserverless-workgroup-namespacename)" : {{String}},
      "[Port](#cfn-redshiftserverless-workgroup-port)" : {{Integer}},
      "[PricePerformanceTarget](#cfn-redshiftserverless-workgroup-priceperformancetarget)" : {{PerformanceTarget}},
      "[PubliclyAccessible](#cfn-redshiftserverless-workgroup-publiclyaccessible)" : {{Boolean}},
      "[RecoveryPointId](#cfn-redshiftserverless-workgroup-recoverypointid)" : {{String}},
      "[SecurityGroupIds](#cfn-redshiftserverless-workgroup-securitygroupids)" : {{[ String, ... ]}},
      "[SnapshotArn](#cfn-redshiftserverless-workgroup-snapshotarn)" : {{String}},
      "[SnapshotName](#cfn-redshiftserverless-workgroup-snapshotname)" : {{String}},
      "[SnapshotOwnerAccount](#cfn-redshiftserverless-workgroup-snapshotowneraccount)" : {{String}},
      "[SubnetIds](#cfn-redshiftserverless-workgroup-subnetids)" : {{[ String, ... ]}},
      "[Tags](#cfn-redshiftserverless-workgroup-tags)" : {{[ Tag, ... ]}},
      "[TrackName](#cfn-redshiftserverless-workgroup-trackname)" : {{String}},
      "[Workgroup](#cfn-redshiftserverless-workgroup-workgroup)" : {{Workgroup}},
      "[WorkgroupName](#cfn-redshiftserverless-workgroup-workgroupname)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-redshiftserverless-workgroup-syntax.yaml"></a>

```
Type: AWS::RedshiftServerless::Workgroup
Properties:
  [BaseCapacity](#cfn-redshiftserverless-workgroup-basecapacity): {{Integer}}
  [ConfigParameters](#cfn-redshiftserverless-workgroup-configparameters): {{
    - ConfigParameter}}
  [EnhancedVpcRouting](#cfn-redshiftserverless-workgroup-enhancedvpcrouting): {{Boolean}}
  [MaxCapacity](#cfn-redshiftserverless-workgroup-maxcapacity): {{Integer}}
  [NamespaceName](#cfn-redshiftserverless-workgroup-namespacename): {{String}}
  [Port](#cfn-redshiftserverless-workgroup-port): {{Integer}}
  [PricePerformanceTarget](#cfn-redshiftserverless-workgroup-priceperformancetarget): {{
    PerformanceTarget}}
  [PubliclyAccessible](#cfn-redshiftserverless-workgroup-publiclyaccessible): {{Boolean}}
  [RecoveryPointId](#cfn-redshiftserverless-workgroup-recoverypointid): {{String}}
  [SecurityGroupIds](#cfn-redshiftserverless-workgroup-securitygroupids): {{
    - String}}
  [SnapshotArn](#cfn-redshiftserverless-workgroup-snapshotarn): {{String}}
  [SnapshotName](#cfn-redshiftserverless-workgroup-snapshotname): {{String}}
  [SnapshotOwnerAccount](#cfn-redshiftserverless-workgroup-snapshotowneraccount): {{String}}
  [SubnetIds](#cfn-redshiftserverless-workgroup-subnetids): {{
    - String}}
  [Tags](#cfn-redshiftserverless-workgroup-tags): {{
    - Tag}}
  [TrackName](#cfn-redshiftserverless-workgroup-trackname): {{String}}
  [Workgroup](#cfn-redshiftserverless-workgroup-workgroup): {{
    Workgroup}}
  [WorkgroupName](#cfn-redshiftserverless-workgroup-workgroupname): {{String}}
```

## Properties
<a name="aws-resource-redshiftserverless-workgroup-properties"></a>

`BaseCapacity`  <a name="cfn-redshiftserverless-workgroup-basecapacity"></a>
The base compute capacity of the workgroup in Redshift Processing Units (RPUs).
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConfigParameters`  <a name="cfn-redshiftserverless-workgroup-configparameters"></a>
The key of the parameter. The options are `auto_mv`, `datestyle`, `enable_case_sensitive_identifier`, `enable_user_activity_logging`, `query_group`, `search_path`, `require_ssl`, `use_fips_ssl`, and query monitoring metrics that let you define performance boundaries. For more information about query monitoring rules and available metrics, see [ Query monitoring metrics for Amazon Redshift Serverless ](https://docs.aws.amazon.com/redshift/latest/dg/cm-c-wlm-query-monitoring-rules.html#cm-c-wlm-query-monitoring-metrics-serverless).
*Required*: No
*Type*: Array of [ConfigParameter](aws-properties-redshiftserverless-workgroup-configparameter.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnhancedVpcRouting`  <a name="cfn-redshiftserverless-workgroup-enhancedvpcrouting"></a>
The value that specifies whether to enable enhanced virtual private cloud (VPC) routing, which forces Amazon Redshift Serverless to route traffic through your VPC.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxCapacity`  <a name="cfn-redshiftserverless-workgroup-maxcapacity"></a>
The maximum data-warehouse capacity Amazon Redshift Serverless uses to serve queries. The max capacity is specified in RPUs.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NamespaceName`  <a name="cfn-redshiftserverless-workgroup-namespacename"></a>
The namespace the workgroup is associated with.
*Required*: No
*Type*: String
*Pattern*: `^(?=^[a-z0-9-]+$).{3,64}$`
*Minimum*: `3`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Port`  <a name="cfn-redshiftserverless-workgroup-port"></a>
The custom port to use when connecting to a workgroup. Valid port ranges are 5431-5455 and 8191-8215. The default is 5439.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PricePerformanceTarget`  <a name="cfn-redshiftserverless-workgroup-priceperformancetarget"></a>
An object that represents the price performance target settings for the workgroup.
*Required*: No
*Type*: [PerformanceTarget](aws-properties-redshiftserverless-workgroup-performancetarget.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PubliclyAccessible`  <a name="cfn-redshiftserverless-workgroup-publiclyaccessible"></a>
A value that specifies whether the workgroup can be accessible from a public network.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RecoveryPointId`  <a name="cfn-redshiftserverless-workgroup-recoverypointid"></a>
The identifier of the recovery point to restore the namespace from.
When this resource is first created, the namespace is restored from this recovery point. On subsequent updates, a restore occurs only when RecoveryPointId changes from its previous value. If the value is unchanged or removed, no restore takes place and existing data is preserved.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecurityGroupIds`  <a name="cfn-redshiftserverless-workgroup-securitygroupids"></a>
A list of security group IDs to associate with the workgroup.
*Required*: No
*Type*: Array of String
*Minimum*: `0 | 1`
*Maximum*: `255 | 32`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SnapshotArn`  <a name="cfn-redshiftserverless-workgroup-snapshotarn"></a>
The Amazon Resource Name (ARN) of the snapshot to restore the namespace from. Specify either SnapshotArn or SnapshotName, but not both.
When this resource is first created, the namespace is restored from this snapshot. On subsequent updates, a restore occurs only when SnapshotArn changes from its previous value. If the value is unchanged or removed, no restore takes place and existing data is preserved.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SnapshotName`  <a name="cfn-redshiftserverless-workgroup-snapshotname"></a>
The name of the snapshot to restore the namespace from. Because snapshot names are unique only within an account, also specify SnapshotOwnerAccount when restoring from a snapshot owned by a different account. Specify either SnapshotName or SnapshotArn, but not both.
When this resource is first created, the namespace is restored from this snapshot. On subsequent updates, a restore occurs only when SnapshotName or SnapshotOwnerAccount changes from its previous value. If both values are unchanged or SnapshotName is removed, no restore takes place and existing data is preserved.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SnapshotOwnerAccount`  <a name="cfn-redshiftserverless-workgroup-snapshotowneraccount"></a>
The Amazon Web Services Account ID that owns the snapshot. Required when restoring from a snapshot shared by another account. Used in combination with SnapshotName.
On updates, changing this value while SnapshotName is set triggers a restore from the newly referenced snapshot. If the value is unchanged, no restore takes place and existing data is preserved.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubnetIds`  <a name="cfn-redshiftserverless-workgroup-subnetids"></a>
A list of subnet IDs the workgroup is associated with.
*Required*: No
*Type*: Array of String
*Minimum*: `0 | 1`
*Maximum*: `255 | 32`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-redshiftserverless-workgroup-tags"></a>
The map of the key-value pairs used to tag the workgroup.
*Required*: No
*Type*: Array of [Tag](aws-properties-redshiftserverless-workgroup-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TrackName`  <a name="cfn-redshiftserverless-workgroup-trackname"></a>
An optional parameter for the name of the track for the workgroup. If you don't provide a track name, the workgroup is assigned to the current track.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Workgroup`  <a name="cfn-redshiftserverless-workgroup-workgroup"></a>
The collection of computing resources from which an endpoint is created.
*Required*: No
*Type*: [Workgroup](aws-properties-redshiftserverless-workgroup-workgroup.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WorkgroupName`  <a name="cfn-redshiftserverless-workgroup-workgroupname"></a>
The name of the workgroup.
*Required*: Yes
*Type*: String
*Pattern*: `^(?=^[a-z0-9-]+$).{3,64}$`
*Minimum*: `3`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-redshiftserverless-workgroup-return-values"></a>

### Ref
<a name="aws-resource-redshiftserverless-workgroup-return-values-ref"></a>

When the logical ID of this resource is provided to the Ref intrinsic function, Ref returns the WorkgroupName, such as `sample-workgroup.` For more information about using the Ref function, see [Ref](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-redshiftserverless-workgroup-return-values-fn--getatt"></a>

GetAtt returns a value for a specified attribute of this type. For more information, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html). The following are the available attributes and sample return values.

####
<a name="aws-resource-redshiftserverless-workgroup-return-values-fn--getatt-fn--getatt"></a>

`Workgroup.BaseCapacity`  <a name="Workgroup.BaseCapacity-fn::getatt"></a>
The base data warehouse capacity of the workgroup in Redshift Processing Units (RPUs).

`Workgroup.ConfigParameters`  <a name="Workgroup.ConfigParameters-fn::getatt"></a>
Property description not available.

`Workgroup.CreationDate`  <a name="Workgroup.CreationDate-fn::getatt"></a>
The creation date of the workgroup.

`Workgroup.Endpoint.Address`  <a name="Workgroup.Endpoint.Address-fn::getatt"></a>
The DNS address of the VPC endpoint.

`Workgroup.Endpoint.Port`  <a name="Workgroup.Endpoint.Port-fn::getatt"></a>
The custom port to use when connecting to a workgroup. Valid port ranges are 5431-5455 and 8191-8215. The default is 5439.

`Workgroup.EnhancedVpcRouting`  <a name="Workgroup.EnhancedVpcRouting-fn::getatt"></a>
The value that specifies whether to enable enhanced virtual private cloud (VPC) routing, which forces Amazon Redshift Serverless to route traffic through your VPC.

`Workgroup.MaxCapacity`  <a name="Workgroup.MaxCapacity-fn::getatt"></a>
The maximum data-warehouse capacity Amazon Redshift Serverless uses to serve queries. The max capacity is specified in RPUs.

`Workgroup.NamespaceName`  <a name="Workgroup.NamespaceName-fn::getatt"></a>
The namespace the workgroup is associated with.

`Workgroup.PubliclyAccessible`  <a name="Workgroup.PubliclyAccessible-fn::getatt"></a>
A value that specifies whether the workgroup can be accessible from a public network.

`Workgroup.SecurityGroupIds`  <a name="Workgroup.SecurityGroupIds-fn::getatt"></a>
An array of security group IDs to associate with the workgroup.

`Workgroup.Status`  <a name="Workgroup.Status-fn::getatt"></a>
The status of the workgroup.

`Workgroup.SubnetIds`  <a name="Workgroup.SubnetIds-fn::getatt"></a>
An array of subnet IDs the workgroup is associated with.

`Workgroup.TrackName`  <a name="Workgroup.TrackName-fn::getatt"></a>
An optional parameter for the name of the track for the workgroup. If you don't provide a track name, the workgroup is assigned to the current track.

`Workgroup.WorkgroupArn`  <a name="Workgroup.WorkgroupArn-fn::getatt"></a>
The Amazon Resource Name (ARN) that links to the workgroup.

`Workgroup.WorkgroupId`  <a name="Workgroup.WorkgroupId-fn::getatt"></a>
The unique identifier of the workgroup.

`Workgroup.WorkgroupName`  <a name="Workgroup.WorkgroupName-fn::getatt"></a>
The name of the workgroup.
