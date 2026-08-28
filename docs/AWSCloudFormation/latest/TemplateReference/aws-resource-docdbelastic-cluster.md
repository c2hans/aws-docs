---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-docdbelastic-cluster.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DocDBElastic::Cluster
<a name="aws-resource-docdbelastic-cluster"></a>

Creates a new Amazon DocumentDB elastic cluster and returns its cluster structure.

## Syntax
<a name="aws-resource-docdbelastic-cluster-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-docdbelastic-cluster-syntax.json"></a>

```
{
  "Type" : "AWS::DocDBElastic::Cluster",
  "Properties" : {
      "[AdminUserName](#cfn-docdbelastic-cluster-adminusername)" : {{String}},
      "[AdminUserPassword](#cfn-docdbelastic-cluster-adminuserpassword)" : {{String}},
      "[AuthType](#cfn-docdbelastic-cluster-authtype)" : {{String}},
      "[BackupRetentionPeriod](#cfn-docdbelastic-cluster-backupretentionperiod)" : {{Integer}},
      "[ClusterName](#cfn-docdbelastic-cluster-clustername)" : {{String}},
      "[KmsKeyId](#cfn-docdbelastic-cluster-kmskeyid)" : {{String}},
      "[PreferredBackupWindow](#cfn-docdbelastic-cluster-preferredbackupwindow)" : {{String}},
      "[PreferredMaintenanceWindow](#cfn-docdbelastic-cluster-preferredmaintenancewindow)" : {{String}},
      "[ShardCapacity](#cfn-docdbelastic-cluster-shardcapacity)" : {{Integer}},
      "[ShardCount](#cfn-docdbelastic-cluster-shardcount)" : {{Integer}},
      "[ShardInstanceCount](#cfn-docdbelastic-cluster-shardinstancecount)" : {{Integer}},
      "[SubnetIds](#cfn-docdbelastic-cluster-subnetids)" : {{[ String, ... ]}},
      "[Tags](#cfn-docdbelastic-cluster-tags)" : {{[ Tag, ... ]}},
      "[VpcSecurityGroupIds](#cfn-docdbelastic-cluster-vpcsecuritygroupids)" : {{[ String, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-docdbelastic-cluster-syntax.yaml"></a>

```
Type: AWS::DocDBElastic::Cluster
Properties:
  [AdminUserName](#cfn-docdbelastic-cluster-adminusername): {{String}}
  [AdminUserPassword](#cfn-docdbelastic-cluster-adminuserpassword): {{String}}
  [AuthType](#cfn-docdbelastic-cluster-authtype): {{String}}
  [BackupRetentionPeriod](#cfn-docdbelastic-cluster-backupretentionperiod): {{Integer}}
  [ClusterName](#cfn-docdbelastic-cluster-clustername): {{String}}
  [KmsKeyId](#cfn-docdbelastic-cluster-kmskeyid): {{String}}
  [PreferredBackupWindow](#cfn-docdbelastic-cluster-preferredbackupwindow): {{String}}
  [PreferredMaintenanceWindow](#cfn-docdbelastic-cluster-preferredmaintenancewindow): {{String}}
  [ShardCapacity](#cfn-docdbelastic-cluster-shardcapacity): {{Integer}}
  [ShardCount](#cfn-docdbelastic-cluster-shardcount): {{Integer}}
  [ShardInstanceCount](#cfn-docdbelastic-cluster-shardinstancecount): {{Integer}}
  [SubnetIds](#cfn-docdbelastic-cluster-subnetids): {{
    - String}}
  [Tags](#cfn-docdbelastic-cluster-tags): {{
    - Tag}}
  [VpcSecurityGroupIds](#cfn-docdbelastic-cluster-vpcsecuritygroupids): {{
    - String}}
```

## Properties
<a name="aws-resource-docdbelastic-cluster-properties"></a>

`AdminUserName`  <a name="cfn-docdbelastic-cluster-adminusername"></a>
The name of the Amazon DocumentDB elastic clusters administrator.
*Constraints*:
+ Must be from 1 to 63 letters or numbers.
+ The first character must be a letter.
+ Cannot be a reserved word.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AdminUserPassword`  <a name="cfn-docdbelastic-cluster-adminuserpassword"></a>
The password for the Elastic DocumentDB cluster administrator and can contain any printable ASCII characters.
*Constraints*:
+ Must contain from 8 to 100 characters.
+ Cannot contain a forward slash (/), double quote ("), or the "at" symbol (@).
+ A valid `AdminUserName` entry is also required.
*Required*: Conditional
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AuthType`  <a name="cfn-docdbelastic-cluster-authtype"></a>
The authentication type used to determine where to fetch the password used for accessing the elastic cluster. Valid types are `PLAIN_TEXT` or `SECRET_ARN`.
*Required*: Yes
*Type*: String
*Allowed values*: `PLAIN_TEXT | SECRET_ARN`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`BackupRetentionPeriod`  <a name="cfn-docdbelastic-cluster-backupretentionperiod"></a>
The number of days for which automatic snapshots are retained.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClusterName`  <a name="cfn-docdbelastic-cluster-clustername"></a>
The name of the new elastic cluster. This parameter is stored as a lowercase string.
*Constraints*:
+ Must contain from 1 to 63 letters, numbers, or hyphens.
+ The first character must be a letter.
+ Cannot end with a hyphen or contain two consecutive hyphens.
*Example*: `my-cluster`
*Required*: Yes
*Type*: String
*Pattern*: `[a-zA-z][a-zA-Z0-9]*(-[a-zA-Z0-9]+)*`
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KmsKeyId`  <a name="cfn-docdbelastic-cluster-kmskeyid"></a>
The KMS key identifier to use to encrypt the new elastic cluster.
The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are creating a cluster using the same Amazon account that owns this KMS encryption key, you can use the KMS key alias instead of the ARN as the KMS encryption key.
If an encryption key is not specified, Amazon DocumentDB uses the default encryption key that KMS creates for your account. Your account has a different default encryption key for each Amazon Region.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PreferredBackupWindow`  <a name="cfn-docdbelastic-cluster-preferredbackupwindow"></a>
The daily time range during which automated backups are created if automated backups are enabled, as determined by `backupRetentionPeriod`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PreferredMaintenanceWindow`  <a name="cfn-docdbelastic-cluster-preferredmaintenancewindow"></a>
The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).
*Format*: `ddd:hh24:mi-ddd:hh24:mi`
*Default*: a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week.
*Valid days*: Mon, Tue, Wed, Thu, Fri, Sat, Sun
*Constraints*: Minimum 30-minute window.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShardCapacity`  <a name="cfn-docdbelastic-cluster-shardcapacity"></a>
The number of vCPUs assigned to each elastic cluster shard. Maximum is 64. Allowed values are 2, 4, 8, 16, 32, 64.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShardCount`  <a name="cfn-docdbelastic-cluster-shardcount"></a>
The number of shards assigned to the elastic cluster. Maximum is 32.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShardInstanceCount`  <a name="cfn-docdbelastic-cluster-shardinstancecount"></a>
The number of replica instances applying to all shards in the cluster. A `shardInstanceCount` value of 1 means there is one writer instance, and any additional instances are replicas that can be used for reads and to improve availability.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubnetIds`  <a name="cfn-docdbelastic-cluster-subnetids"></a>
The Amazon EC2 subnet IDs for the new elastic cluster.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-docdbelastic-cluster-tags"></a>
The tags to be assigned to the new elastic cluster.
*Required*: No
*Type*: Array of [Tag](aws-properties-docdbelastic-cluster-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcSecurityGroupIds`  <a name="cfn-docdbelastic-cluster-vpcsecuritygroupids"></a>
A list of EC2 VPC security groups to associate with the new elastic cluster.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-docdbelastic-cluster-return-values"></a>

### Ref
<a name="aws-resource-docdbelastic-cluster-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-docdbelastic-cluster-return-values-fn--getatt"></a>

####
<a name="aws-resource-docdbelastic-cluster-return-values-fn--getatt-fn--getatt"></a>

`ClusterArn`  <a name="ClusterArn-fn::getatt"></a>
Property description not available.

`ClusterEndpoint`  <a name="ClusterEndpoint-fn::getatt"></a>
The URL used to connect to the elastic cluster.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
