---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-docdb-dbinstance.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DocDB::DBInstance
<a name="aws-resource-docdb-dbinstance"></a>

The `AWS::DocDB::DBInstance`Amazon DocumentDB (with MongoDB compatibility) resource describes a DBInstance. For more information, see [DBInstance](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DBInstance.html) in the *Amazon DocumentDB Developer Guide*.

## Syntax
<a name="aws-resource-docdb-dbinstance-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-docdb-dbinstance-syntax.json"></a>

```
{
  "Type" : "AWS::DocDB::DBInstance",
  "Properties" : {
      "[AutoMinorVersionUpgrade](#cfn-docdb-dbinstance-autominorversionupgrade)" : {{Boolean}},
      "[AvailabilityZone](#cfn-docdb-dbinstance-availabilityzone)" : {{String}},
      "[CACertificateIdentifier](#cfn-docdb-dbinstance-cacertificateidentifier)" : {{String}},
      "[CertificateRotationRestart](#cfn-docdb-dbinstance-certificaterotationrestart)" : {{Boolean}},
      "[DBClusterIdentifier](#cfn-docdb-dbinstance-dbclusteridentifier)" : {{String}},
      "[DBInstanceClass](#cfn-docdb-dbinstance-dbinstanceclass)" : {{String}},
      "[DBInstanceIdentifier](#cfn-docdb-dbinstance-dbinstanceidentifier)" : {{String}},
      "[EnablePerformanceInsights](#cfn-docdb-dbinstance-enableperformanceinsights)" : {{Boolean}},
      "[PreferredMaintenanceWindow](#cfn-docdb-dbinstance-preferredmaintenancewindow)" : {{String}},
      "[Tags](#cfn-docdb-dbinstance-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-docdb-dbinstance-syntax.yaml"></a>

```
Type: AWS::DocDB::DBInstance
Properties:
  [AutoMinorVersionUpgrade](#cfn-docdb-dbinstance-autominorversionupgrade): {{Boolean}}
  [AvailabilityZone](#cfn-docdb-dbinstance-availabilityzone): {{String}}
  [CACertificateIdentifier](#cfn-docdb-dbinstance-cacertificateidentifier): {{String}}
  [CertificateRotationRestart](#cfn-docdb-dbinstance-certificaterotationrestart): {{Boolean}}
  [DBClusterIdentifier](#cfn-docdb-dbinstance-dbclusteridentifier): {{String}}
  [DBInstanceClass](#cfn-docdb-dbinstance-dbinstanceclass): {{String}}
  [DBInstanceIdentifier](#cfn-docdb-dbinstance-dbinstanceidentifier): {{String}}
  [EnablePerformanceInsights](#cfn-docdb-dbinstance-enableperformanceinsights): {{Boolean}}
  [PreferredMaintenanceWindow](#cfn-docdb-dbinstance-preferredmaintenancewindow): {{String}}
  [Tags](#cfn-docdb-dbinstance-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-docdb-dbinstance-properties"></a>

`AutoMinorVersionUpgrade`  <a name="cfn-docdb-dbinstance-autominorversionupgrade"></a>
This parameter does not apply to Amazon DocumentDB. Amazon DocumentDB does not perform minor version upgrades regardless of the value set.
Default: `false`
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AvailabilityZone`  <a name="cfn-docdb-dbinstance-availabilityzone"></a>
The Amazon EC2 Availability Zone that the instance is created in.
Default: A random, system-chosen Availability Zone in the endpoint's AWS Region.
Example: `us-east-1d`
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CACertificateIdentifier`  <a name="cfn-docdb-dbinstance-cacertificateidentifier"></a>
The identifier of the CA certificate for this DB instance.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CertificateRotationRestart`  <a name="cfn-docdb-dbinstance-certificaterotationrestart"></a>
Specifies whether the DB instance is restarted when you rotate your SSL/TLS certificate.
By default, the DB instance is restarted when you rotate your SSL/TLS certificate. The certificate is not updated until the DB instance is restarted.
Set this parameter only if you are *not* using SSL/TLS to connect to the DB instance.
If you are using SSL/TLS to connect to the DB instance, see [Updating Your Amazon DocumentDB TLS Certificates](https://docs.aws.amazon.com/documentdb/latest/devguide/ca_cert_rotation.html) and [ Encrypting Data in Transit](https://docs.aws.amazon.com/documentdb/latest/devguide/security.encryption.ssl.html) in the *Amazon DocumentDB Developer Guide*.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DBClusterIdentifier`  <a name="cfn-docdb-dbinstance-dbclusteridentifier"></a>
The identifier of the cluster that the instance will belong to.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DBInstanceClass`  <a name="cfn-docdb-dbinstance-dbinstanceclass"></a>
The compute and memory capacity of the instance; for example, `db.m4.large`. If you change the class of an instance there can be some interruption in the cluster's service.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DBInstanceIdentifier`  <a name="cfn-docdb-dbinstance-dbinstanceidentifier"></a>
The instance identifier. This parameter is stored as a lowercase string.
Constraints:
+ Must contain from 1 to 63 letters, numbers, or hyphens.
+ The first character must be a letter.
+ Cannot end with a hyphen or contain two consecutive hyphens.
Example: `mydbinstance`
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EnablePerformanceInsights`  <a name="cfn-docdb-dbinstance-enableperformanceinsights"></a>
A value that indicates whether to enable Performance Insights for the DB Instance. For more information, see [Using Amazon Performance Insights](https://docs.aws.amazon.com/documentdb/latest/devguide/performance-insights.html).
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PreferredMaintenanceWindow`  <a name="cfn-docdb-dbinstance-preferredmaintenancewindow"></a>
The time range each week during which system maintenance can occur, in Universal Coordinated Time (UTC).
 Format: `ddd:hh24:mi-ddd:hh24:mi`
The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week.
Valid days: Mon, Tue, Wed, Thu, Fri, Sat, Sun
Constraints: Minimum 30-minute window.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-docdb-dbinstance-tags"></a>
The tags to be assigned to the instance. You can assign up to 10 tags to an instance.
*Required*: No
*Type*: Array of [Tag](aws-properties-docdb-dbinstance-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-docdb-dbinstance-return-values"></a>

### Ref
<a name="aws-resource-docdb-dbinstance-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the DBInstance's name, such as `sample-cluster-instance`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-docdb-dbinstance-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-docdb-dbinstance-return-values-fn--getatt-fn--getatt"></a>

`Endpoint`  <a name="Endpoint-fn::getatt"></a>
The connection endpoint for the instance. For example: `sample-cluster.cluster-abcdefghijkl.us-east-1.docdb.amazonaws.com`.

`Port`  <a name="Port-fn::getatt"></a>
The port number on which the database accepts connections, such as `27017`.

## Examples
<a name="aws-resource-docdb-dbinstance--examples"></a>

###
<a name="aws-resource-docdb-dbinstance--examples--"></a>

#### JSON
<a name="aws-resource-docdb-dbinstance--examples----json"></a>

```
{
   "Type" : "AWS::DocDB::DBInstance",
   "Properties" : {
      "AutoMinorVersionUpgrade" : true,
      "AvailabilityZone" : "us-east-1c",
      "DBClusterIdentifier" : "sample-cluster",
      "DBInstanceClass" : "db.r5.large",
      "DBInstanceIdentifier" : "sample-cluster-instance-0",
      "PreferredMaintenanceWindow" : "sat:06:54-sat:07:24",
      "Tags" : [{ "Key": "String","Value": "String" }]
   }
}
```

#### YAML
<a name="aws-resource-docdb-dbinstance--examples----yaml"></a>

```
Type: "AWS::DocDB::DBInstance"
Properties:
   AutoMinorVersionUpgrade: true
   AvailabilityZone: "us-east-1c"
   DBClusterIdentifier: "sample-cluster"
   DBInstanceClass: "db.r5.large"
   DBInstanceIdentifier: "sample-cluster-instance-0"
   PreferredMaintenanceWindow: "sat:06:54-sat:07:24"
   Tags:
      -
         Key: "String"
         Value: "String"
```

## See also
<a name="aws-resource-docdb-dbinstance--seealso"></a>
+  [DBInstance](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DBInstance.html)
+  [CreateDBInstance](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_CreateDBInstance.html)
+  [DeleteDBInstance](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DeleteDBInstance.html)
+  [DescribeDBInstances](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DescribeDBInstances.html)
+  [ModifyDBInstance](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_ModifyDBInstance.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
