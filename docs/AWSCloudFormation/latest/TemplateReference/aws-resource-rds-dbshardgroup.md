---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbshardgroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RDS::DBShardGroup
<a name="aws-resource-rds-dbshardgroup"></a>

Creates a new DB shard group for Aurora Limitless Database. You must enable Aurora Limitless Database to create a DB shard group.

Valid for: Aurora DB clusters only

## Syntax
<a name="aws-resource-rds-dbshardgroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-rds-dbshardgroup-syntax.json"></a>

```
{
  "Type" : "AWS::RDS::DBShardGroup",
  "Properties" : {
      "[ComputeRedundancy](#cfn-rds-dbshardgroup-computeredundancy)" : {{Integer}},
      "[DBClusterIdentifier](#cfn-rds-dbshardgroup-dbclusteridentifier)" : {{String}},
      "[DBShardGroupIdentifier](#cfn-rds-dbshardgroup-dbshardgroupidentifier)" : {{String}},
      "[MaxACU](#cfn-rds-dbshardgroup-maxacu)" : {{Number}},
      "[MinACU](#cfn-rds-dbshardgroup-minacu)" : {{Number}},
      "[PubliclyAccessible](#cfn-rds-dbshardgroup-publiclyaccessible)" : {{Boolean}},
      "[Tags](#cfn-rds-dbshardgroup-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-rds-dbshardgroup-syntax.yaml"></a>

```
Type: AWS::RDS::DBShardGroup
Properties:
  [ComputeRedundancy](#cfn-rds-dbshardgroup-computeredundancy): {{Integer}}
  [DBClusterIdentifier](#cfn-rds-dbshardgroup-dbclusteridentifier): {{String}}
  [DBShardGroupIdentifier](#cfn-rds-dbshardgroup-dbshardgroupidentifier): {{String}}
  [MaxACU](#cfn-rds-dbshardgroup-maxacu): {{Number}}
  [MinACU](#cfn-rds-dbshardgroup-minacu): {{Number}}
  [PubliclyAccessible](#cfn-rds-dbshardgroup-publiclyaccessible): {{Boolean}}
  [Tags](#cfn-rds-dbshardgroup-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-rds-dbshardgroup-properties"></a>

`ComputeRedundancy`  <a name="cfn-rds-dbshardgroup-computeredundancy"></a>
Specifies whether to create standby standby DB data access shard for the DB shard group. Valid values are the following:
+ 0 - Creates a DB shard group without a standby DB data access shard. This is the default value.
+ 1 - Creates a DB shard group with a standby DB data access shard in a different Availability Zone (AZ).
+ 2 - Creates a DB shard group with two standby DB data access shard in two different AZs.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DBClusterIdentifier`  <a name="cfn-rds-dbshardgroup-dbclusteridentifier"></a>
The name of the primary DB cluster for the DB shard group.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DBShardGroupIdentifier`  <a name="cfn-rds-dbshardgroup-dbshardgroupidentifier"></a>
The name of the DB shard group.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MaxACU`  <a name="cfn-rds-dbshardgroup-maxacu"></a>
The maximum capacity of the DB shard group in Aurora capacity units (ACUs).
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinACU`  <a name="cfn-rds-dbshardgroup-minacu"></a>
The minimum capacity of the DB shard group in Aurora capacity units (ACUs).
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PubliclyAccessible`  <a name="cfn-rds-dbshardgroup-publiclyaccessible"></a>
Specifies whether the DB shard group is publicly accessible.
When the DB shard group is publicly accessible, its Domain Name System (DNS) endpoint resolves to the private IP address from within the DB shard group's virtual private cloud (VPC). It resolves to the public IP address from outside of the DB shard group's VPC. Access to the DB shard group is ultimately controlled by the security group it uses. That public access is not permitted if the security group assigned to the DB shard group doesn't permit it.
When the DB shard group isn't publicly accessible, it is an internal DB shard group with a DNS name that resolves to a private IP address.
Default: The default behavior varies depending on whether `DBSubnetGroupName` is specified.
If `DBSubnetGroupName` isn't specified, and `PubliclyAccessible` isn't specified, the following applies:
+ If the default VPC in the target Region doesn’t have an internet gateway attached to it, the DB shard group is private.
+ If the default VPC in the target Region has an internet gateway attached to it, the DB shard group is public.
If `DBSubnetGroupName` is specified, and `PubliclyAccessible` isn't specified, the following applies:
+ If the subnets are part of a VPC that doesn’t have an internet gateway attached to it, the DB shard group is private.
+ If the subnets are part of a VPC that has an internet gateway attached to it, the DB shard group is public.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-rds-dbshardgroup-tags"></a>
An optional set of key-value pairs to associate arbitrary data of your choosing with the DB shard group.
*Required*: No
*Type*: Array of [Tag](aws-properties-rds-dbshardgroup-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-rds-dbshardgroup-return-values"></a>

### Ref
<a name="aws-resource-rds-dbshardgroup-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the name (`DBClusterIdentifier`) of the DB cluster.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-rds-dbshardgroup-return-values-fn--getatt"></a>

####
<a name="aws-resource-rds-dbshardgroup-return-values-fn--getatt-fn--getatt"></a>

`DBShardGroupResourceId`  <a name="DBShardGroupResourceId-fn::getatt"></a>
The AWS Region-unique, immutable identifier for the DB shard group.

`Endpoint`  <a name="Endpoint-fn::getatt"></a>
This data type represents the information you need to connect to an Amazon RDS DB instance. This data type is used as a response element in the following actions:
+  `CreateDBInstance`
+  `DescribeDBInstances`
+  `DeleteDBInstance`
For the data structure that represents Amazon Aurora DB cluster endpoints, see `DBClusterEndpoint`.
