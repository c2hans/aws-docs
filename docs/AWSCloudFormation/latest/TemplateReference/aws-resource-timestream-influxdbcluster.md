---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-timestream-influxdbcluster.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Timestream::InfluxDBCluster
<a name="aws-resource-timestream-influxdbcluster"></a>

The `AWS::Timestream::InfluxDBCluster` resource specifies an Amazon Timestream for InfluxDB cluster. A cluster supports InfluxDB v2 with multi-node read replicas for high availability and read scaling, with a primary node and one or more read replicas distributed across availability zones. A cluster also supports InfluxDB v3 deployments in either Core (single-node for near real-time workloads) or Enterprise (multi-node with compaction for high-cardinality data and long-term analytics) configurations. You can configure instance types, storage, networking, failover behavior, and deployment type for your cluster.

## Syntax
<a name="aws-resource-timestream-influxdbcluster-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-timestream-influxdbcluster-syntax.json"></a>

```
{
  "Type" : "AWS::Timestream::InfluxDBCluster",
  "Properties" : {
      "[AllocatedStorage](#cfn-timestream-influxdbcluster-allocatedstorage)" : {{Integer}},
      "[Bucket](#cfn-timestream-influxdbcluster-bucket)" : {{String}},
      "[DbInstanceType](#cfn-timestream-influxdbcluster-dbinstancetype)" : {{String}},
      "[DbParameterGroupIdentifier](#cfn-timestream-influxdbcluster-dbparametergroupidentifier)" : {{String}},
      "[DbStorageType](#cfn-timestream-influxdbcluster-dbstoragetype)" : {{String}},
      "[DeploymentType](#cfn-timestream-influxdbcluster-deploymenttype)" : {{String}},
      "[FailoverMode](#cfn-timestream-influxdbcluster-failovermode)" : {{String}},
      "[LogDeliveryConfiguration](#cfn-timestream-influxdbcluster-logdeliveryconfiguration)" : {{LogDeliveryConfiguration}},
      "[MaintenanceSchedule](#cfn-timestream-influxdbcluster-maintenanceschedule)" : {{MaintenanceSchedule}},
      "[Name](#cfn-timestream-influxdbcluster-name)" : {{String}},
      "[NetworkType](#cfn-timestream-influxdbcluster-networktype)" : {{String}},
      "[Organization](#cfn-timestream-influxdbcluster-organization)" : {{String}},
      "[Password](#cfn-timestream-influxdbcluster-password)" : {{String}},
      "[Port](#cfn-timestream-influxdbcluster-port)" : {{Integer}},
      "[PubliclyAccessible](#cfn-timestream-influxdbcluster-publiclyaccessible)" : {{Boolean}},
      "[Tags](#cfn-timestream-influxdbcluster-tags)" : {{[ Tag, ... ]}},
      "[Username](#cfn-timestream-influxdbcluster-username)" : {{String}},
      "[VpcSecurityGroupIds](#cfn-timestream-influxdbcluster-vpcsecuritygroupids)" : {{[ String, ... ]}},
      "[VpcSubnetIds](#cfn-timestream-influxdbcluster-vpcsubnetids)" : {{[ String, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-timestream-influxdbcluster-syntax.yaml"></a>

```
Type: AWS::Timestream::InfluxDBCluster
Properties:
  [AllocatedStorage](#cfn-timestream-influxdbcluster-allocatedstorage): {{Integer}}
  [Bucket](#cfn-timestream-influxdbcluster-bucket): {{String}}
  [DbInstanceType](#cfn-timestream-influxdbcluster-dbinstancetype): {{String}}
  [DbParameterGroupIdentifier](#cfn-timestream-influxdbcluster-dbparametergroupidentifier): {{String}}
  [DbStorageType](#cfn-timestream-influxdbcluster-dbstoragetype): {{String}}
  [DeploymentType](#cfn-timestream-influxdbcluster-deploymenttype): {{String}}
  [FailoverMode](#cfn-timestream-influxdbcluster-failovermode): {{String}}
  [LogDeliveryConfiguration](#cfn-timestream-influxdbcluster-logdeliveryconfiguration): {{
    LogDeliveryConfiguration}}
  [MaintenanceSchedule](#cfn-timestream-influxdbcluster-maintenanceschedule): {{
    MaintenanceSchedule}}
  [Name](#cfn-timestream-influxdbcluster-name): {{String}}
  [NetworkType](#cfn-timestream-influxdbcluster-networktype): {{String}}
  [Organization](#cfn-timestream-influxdbcluster-organization): {{String}}
  [Password](#cfn-timestream-influxdbcluster-password): {{String}}
  [Port](#cfn-timestream-influxdbcluster-port): {{Integer}}
  [PubliclyAccessible](#cfn-timestream-influxdbcluster-publiclyaccessible): {{Boolean}}
  [Tags](#cfn-timestream-influxdbcluster-tags): {{
    - Tag}}
  [Username](#cfn-timestream-influxdbcluster-username): {{String}}
  [VpcSecurityGroupIds](#cfn-timestream-influxdbcluster-vpcsecuritygroupids): {{
    - String}}
  [VpcSubnetIds](#cfn-timestream-influxdbcluster-vpcsubnetids): {{
    - String}}
```

## Properties
<a name="aws-resource-timestream-influxdbcluster-properties"></a>

`AllocatedStorage`  <a name="cfn-timestream-influxdbcluster-allocatedstorage"></a>
The amount of storage to allocate for your DB storage type in GiB (gibibytes).
*Required*: No
*Type*: Integer
*Minimum*: `20`
*Maximum*: `15360`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Bucket`  <a name="cfn-timestream-influxdbcluster-bucket"></a>
The name of the initial InfluxDB bucket. All InfluxDB data is stored in a bucket. A bucket combines the concept of a database and a retention period (the duration of time that each data point persists). A bucket belongs to an organization.
*Required*: No
*Type*: String
*Pattern*: `^[^_][^"]*$`
*Minimum*: `2`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DbInstanceType`  <a name="cfn-timestream-influxdbcluster-dbinstancetype"></a>
The Timestream for InfluxDB DB instance type to run InfluxDB on.
*Required*: No
*Type*: String
*Allowed values*: `db.influx.medium | db.influx.large | db.influx.xlarge | db.influx.2xlarge | db.influx.4xlarge | db.influx.8xlarge | db.influx.12xlarge | db.influx.16xlarge | db.influx.24xlarge`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DbParameterGroupIdentifier`  <a name="cfn-timestream-influxdbcluster-dbparametergroupidentifier"></a>
The name or id of the DB parameter group to assign to your DB cluster. DB parameter groups specify how the database is configured. For example, DB parameter groups can specify the limit for query concurrency.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9]+$`
*Minimum*: `3`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DbStorageType`  <a name="cfn-timestream-influxdbcluster-dbstoragetype"></a>
The Timestream for InfluxDB DB storage type to read and write InfluxDB data.
You can choose between 3 different types of provisioned Influx IOPS included storage according to your workloads requirements:
+ Influx IO Included 3000 IOPS
+ Influx IO Included 12000 IOPS
+ Influx IO Included 16000 IOPS
*Required*: No
*Type*: String
*Allowed values*: `InfluxIOIncludedT1 | InfluxIOIncludedT2 | InfluxIOIncludedT3`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DeploymentType`  <a name="cfn-timestream-influxdbcluster-deploymenttype"></a>
Specifies the type of cluster to create.
*Required*: No
*Type*: String
*Allowed values*: `MULTI_NODE_READ_REPLICAS`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FailoverMode`  <a name="cfn-timestream-influxdbcluster-failovermode"></a>
Specifies the behavior of failure recovery when the primary node of the cluster fails.
*Required*: No
*Type*: String
*Allowed values*: `AUTOMATIC | NO_FAILOVER`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogDeliveryConfiguration`  <a name="cfn-timestream-influxdbcluster-logdeliveryconfiguration"></a>
Configuration for sending InfluxDB engine logs to a specified S3 bucket.
*Required*: No
*Type*: [LogDeliveryConfiguration](aws-properties-timestream-influxdbcluster-logdeliveryconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaintenanceSchedule`  <a name="cfn-timestream-influxdbcluster-maintenanceschedule"></a>
Property description not available.
*Required*: No
*Type*: [MaintenanceSchedule](aws-properties-timestream-influxdbcluster-maintenanceschedule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-timestream-influxdbcluster-name"></a>
The name that uniquely identifies the DB cluster when interacting with the Amazon Timestream for InfluxDB API and CLI commands. This name will also be a prefix included in the endpoint. Cluster names must be unique per customer and per region.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-z][a-zA-Z0-9]*(-[a-zA-Z0-9]+)*$`
*Minimum*: `3`
*Maximum*: `40`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NetworkType`  <a name="cfn-timestream-influxdbcluster-networktype"></a>
Specifies whether the network type of the Timestream for InfluxDB cluster is IPV4, which can communicate over IPv4 protocol only, or DUAL, which can communicate over both IPv4 and IPv6 protocols.
*Required*: No
*Type*: String
*Allowed values*: `IPV4 | DUAL`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Organization`  <a name="cfn-timestream-influxdbcluster-organization"></a>
The name of the initial organization for the initial admin user in InfluxDB. An InfluxDB organization is a workspace for a group of users.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Password`  <a name="cfn-timestream-influxdbcluster-password"></a>
The password of the initial admin user created in InfluxDB. This password will allow you to access the InfluxDB UI to perform various administrative tasks and also use the InfluxDB CLI to create an operator token. These attributes will be stored in a Secret created in Amazon Secrets Manager in your account.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9]+$`
*Minimum*: `8`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Port`  <a name="cfn-timestream-influxdbcluster-port"></a>
The port number on which InfluxDB accepts connections.
*Required*: No
*Type*: Integer
*Minimum*: `1024`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PubliclyAccessible`  <a name="cfn-timestream-influxdbcluster-publiclyaccessible"></a>
Configures the DB cluster with a public IP to facilitate access.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-timestream-influxdbcluster-tags"></a>
A list of key-value pairs to associate with the DB cluster.
*Required*: No
*Type*: Array of [Tag](aws-properties-timestream-influxdbcluster-tag.md)
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Username`  <a name="cfn-timestream-influxdbcluster-username"></a>
The username of the initial admin user created in InfluxDB. Must start with a letter and can't end with a hyphen or contain two consecutive hyphens. This username will allow you to access the InfluxDB UI to perform various administrative tasks and also use the InfluxDB CLI to create an operator token. These attributes will be stored in a Secret created in Amazon Secrets Manager in your account.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VpcSecurityGroupIds`  <a name="cfn-timestream-influxdbcluster-vpcsecuritygroupids"></a>
A list of VPC security group IDs to associate with the DB cluster.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VpcSubnetIds`  <a name="cfn-timestream-influxdbcluster-vpcsubnetids"></a>
A list of VPC subnet IDs to associate with the DB cluster. Provide at least two VPC subnet IDs in different availability zones when deploying with a Multi-AZ standby.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `3`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-timestream-influxdbcluster-return-values"></a>

### Ref
<a name="aws-resource-timestream-influxdbcluster-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-timestream-influxdbcluster-return-values-fn--getatt"></a>

####
<a name="aws-resource-timestream-influxdbcluster-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the DB cluster.

`Endpoint`  <a name="Endpoint-fn::getatt"></a>
The endpoint used to connect to the InfluxDB cluster. The default InfluxDB port is 8086.

`EngineType`  <a name="EngineType-fn::getatt"></a>
The database engine type of the DB cluster.

`Id`  <a name="Id-fn::getatt"></a>
A service-generated unique identifier for the InfluxDB cluster.

`InfluxAuthParametersSecretArn`  <a name="InfluxAuthParametersSecretArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the Amazon Secrets Manager secret containing the initial InfluxDB authorization parameters. The secret value is a JSON formatted key-value pair holding InfluxDB authorization values: organization, bucket, username, and password.

`NextMaintenanceTime`  <a name="NextMaintenanceTime-fn::getatt"></a>
Property description not available.

`ReaderEndpoint`  <a name="ReaderEndpoint-fn::getatt"></a>
The endpoint used to connect to the Timestream for InfluxDB cluster for read-only operations.

`Status`  <a name="Status-fn::getatt"></a>
The status of the DB cluster.
