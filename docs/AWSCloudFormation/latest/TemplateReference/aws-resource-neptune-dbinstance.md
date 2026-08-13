---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-neptune-dbinstance.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Neptune::DBInstance
<a name="aws-resource-neptune-dbinstance"></a>

The `AWS::Neptune::DBInstance` type creates an Amazon Neptune DB instance.

 **Updating DB Instances**

You can set a deletion policy for your DB instance to control how CloudFormation handles the instance when the stack is deleted. For Neptune DB instances, you can choose to *retain* the instance, to *delete* the instance, or to *create a snapshot* of the instance. The default CloudFormation behavior depends on the `DBClusterIdentifier` property:
+ For `AWS::Neptune::DBInstance` resources that don't specify the `DBClusterIdentifier` property, CloudFormation saves a snapshot of the DB instance.
+ For `AWS::Neptune::DBInstance` resources that do specify the `DBClusterIdentifier` property, CloudFormation deletes the DB instance.

 **Deleting DB Instances**

**Important**
If a DB instance is deleted or replaced during an update, CloudFormation deletes all automated snapshots. However, it retains manual DB snapshots. During an update that requires replacement, you can apply a stack policy to prevent DB instances from being replaced.

When properties labeled *Update requires: Replacement* are updated, CloudFormation first creates a replacement DB instance, changes references from other dependent resources to point to the replacement DB instance, and finally deletes the old DB instance.

**Important**
We highly recommend that you take a snapshot of the database before updating the stack. If you don't, you lose the data when CloudFormation replaces your DB instance. To preserve your data, perform the following procedure:
Deactivate any applications that are using the DB instance so that there's no activity on the DB instance.
Create a snapshot of the DB instance.
If you want to restore your instance using a DB snapshot, modify the updated template with your DB instance changes and add the `DBSnapshotIdentifier` property with the ID of the DB snapshot that you want to use.
Update the stack.

## Syntax
<a name="aws-resource-neptune-dbinstance-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-neptune-dbinstance-syntax.json"></a>

```
{
  "Type" : "AWS::Neptune::DBInstance",
  "Properties" : {
      "[AllowMajorVersionUpgrade](#cfn-neptune-dbinstance-allowmajorversionupgrade)" : {{Boolean}},
      "[AutoMinorVersionUpgrade](#cfn-neptune-dbinstance-autominorversionupgrade)" : {{Boolean}},
      "[AvailabilityZone](#cfn-neptune-dbinstance-availabilityzone)" : {{String}},
      "[DBClusterIdentifier](#cfn-neptune-dbinstance-dbclusteridentifier)" : {{String}},
      "[DBInstanceClass](#cfn-neptune-dbinstance-dbinstanceclass)" : {{String}},
      "[DBInstanceIdentifier](#cfn-neptune-dbinstance-dbinstanceidentifier)" : {{String}},
      "[DBParameterGroupName](#cfn-neptune-dbinstance-dbparametergroupname)" : {{String}},
      "[DBSubnetGroupName](#cfn-neptune-dbinstance-dbsubnetgroupname)" : {{String}},
      "[PreferredMaintenanceWindow](#cfn-neptune-dbinstance-preferredmaintenancewindow)" : {{String}},
      "[PubliclyAccessible](#cfn-neptune-dbinstance-publiclyaccessible)" : {{Boolean}},
      "[Tags](#cfn-neptune-dbinstance-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-neptune-dbinstance-syntax.yaml"></a>

```
Type: AWS::Neptune::DBInstance
Properties:
  [AllowMajorVersionUpgrade](#cfn-neptune-dbinstance-allowmajorversionupgrade): {{Boolean}}
  [AutoMinorVersionUpgrade](#cfn-neptune-dbinstance-autominorversionupgrade): {{Boolean}}
  [AvailabilityZone](#cfn-neptune-dbinstance-availabilityzone): {{String}}
  [DBClusterIdentifier](#cfn-neptune-dbinstance-dbclusteridentifier): {{String}}
  [DBInstanceClass](#cfn-neptune-dbinstance-dbinstanceclass): {{String}}
  [DBInstanceIdentifier](#cfn-neptune-dbinstance-dbinstanceidentifier): {{String}}
  [DBParameterGroupName](#cfn-neptune-dbinstance-dbparametergroupname): {{String}}
  [DBSubnetGroupName](#cfn-neptune-dbinstance-dbsubnetgroupname): {{String}}
  [PreferredMaintenanceWindow](#cfn-neptune-dbinstance-preferredmaintenancewindow): {{String}}
  [PubliclyAccessible](#cfn-neptune-dbinstance-publiclyaccessible): {{Boolean}}
  [Tags](#cfn-neptune-dbinstance-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-neptune-dbinstance-properties"></a>

`AllowMajorVersionUpgrade`  <a name="cfn-neptune-dbinstance-allowmajorversionupgrade"></a>
Indicates that major version upgrades are allowed. Changing this parameter doesn't result in an outage and the change is asynchronously applied as soon as possible. This parameter must be set to true when specifying a value for the EngineVersion parameter that is a different major version than the DB instance's current version.
When you change this parameter for an existing DB cluster, CloudFormation will replace your existing DB cluster with a new, empty one that uses the engine version you specified.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AutoMinorVersionUpgrade`  <a name="cfn-neptune-dbinstance-autominorversionupgrade"></a>
Indicates that minor version patches are applied automatically.
When updating this property, some interruptions may occur.
*Required*: No
*Type*: Boolean
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`AvailabilityZone`  <a name="cfn-neptune-dbinstance-availabilityzone"></a>
Specifies the name of the Availability Zone the DB instance is located in.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DBClusterIdentifier`  <a name="cfn-neptune-dbinstance-dbclusteridentifier"></a>
If the DB instance is a member of a DB cluster, contains the name of the DB cluster that the DB instance is a member of.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DBInstanceClass`  <a name="cfn-neptune-dbinstance-dbinstanceclass"></a>
Contains the name of the compute and memory capacity class of the DB instance.
If you update this property, some interruptions may occur.
*Required*: Yes
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`DBInstanceIdentifier`  <a name="cfn-neptune-dbinstance-dbinstanceidentifier"></a>
Contains a user-supplied database identifier. This identifier is the unique key that identifies a DB instance.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DBParameterGroupName`  <a name="cfn-neptune-dbinstance-dbparametergroupname"></a>
The name of an existing DB parameter group or a reference to an AWS::Neptune::DBParameterGroup resource created in the template. If any of the data members of the referenced parameter group are changed during an update, the DB instance might need to be restarted, which causes some interruption. If the parameter group contains static parameters, whether they were changed or not, an update triggers a reboot.
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`DBSubnetGroupName`  <a name="cfn-neptune-dbinstance-dbsubnetgroupname"></a>
A DB subnet group to associate with the DB instance. If you update this value, the new subnet group must be a subnet group in a new virtual private cloud (VPC).
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PreferredMaintenanceWindow`  <a name="cfn-neptune-dbinstance-preferredmaintenancewindow"></a>
Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`PubliclyAccessible`  <a name="cfn-neptune-dbinstance-publiclyaccessible"></a>
Indicates whether the DB instance is publicly accessible.
When the DB instance is publicly accessible and you connect from outside of the DB instance's virtual private cloud (VPC), its Domain Name System (DNS) endpoint resolves to the public IP address. When you connect from within the same VPC as the DB instance, the endpoint resolves to the private IP address. Access to the DB instance is ultimately controlled by the security group it uses. That public access isn't permitted if the security group assigned to the DB cluster doesn't permit it.
When the DB instance isn't publicly accessible, it is an internal DB instance with a DNS name that resolves to a private IP address.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-neptune-dbinstance-tags"></a>
An arbitrary set of tags (key-value pairs) for this DB instance.
*Required*: No
*Type*: Array of [Tag](aws-properties-neptune-dbinstance-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-neptune-dbinstance-return-values"></a>

### Ref
<a name="aws-resource-neptune-dbinstance-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource name.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-neptune-dbinstance-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-neptune-dbinstance-return-values-fn--getatt-fn--getatt"></a>

`Endpoint`  <a name="Endpoint-fn::getatt"></a>
The connection endpoint for the database. For example: `mystack-mydb-1apw1j4phylrk.cg034hpkmmjt.us-east-2.rds.amazonaws.com`.

`Port`  <a name="Port-fn::getatt"></a>
The port number on which the database accepts connections. For example: `8182`.
