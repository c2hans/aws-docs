---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-timestream-influxdbinstance.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Timestream::InfluxDBInstance
<a name="aws-resource-timestream-influxdbinstance"></a>

A DB instance is an isolated database environment running in the cloud. It is the basic building block of Amazon Timestream for InfluxDB. A DB instance can contain multiple user-created databases (or organizations and buckets for the case of InfluxDb 2.x databases), and can be accessed using the same client tools and applications you might use to access a standalone self-managed InfluxDB instance.

## Syntax
<a name="aws-resource-timestream-influxdbinstance-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-timestream-influxdbinstance-syntax.json"></a>

```
{
  "Type" : "AWS::Timestream::InfluxDBInstance",
  "Properties" : {
      "[AllocatedStorage](#cfn-timestream-influxdbinstance-allocatedstorage)" : {{Integer}},
      "[Bucket](#cfn-timestream-influxdbinstance-bucket)" : {{String}},
      "[DbInstanceType](#cfn-timestream-influxdbinstance-dbinstancetype)" : {{String}},
      "[DbParameterGroupIdentifier](#cfn-timestream-influxdbinstance-dbparametergroupidentifier)" : {{String}},
      "[DbStorageType](#cfn-timestream-influxdbinstance-dbstoragetype)" : {{String}},
      "[DeploymentType](#cfn-timestream-influxdbinstance-deploymenttype)" : {{String}},
      "[LogDeliveryConfiguration](#cfn-timestream-influxdbinstance-logdeliveryconfiguration)" : {{LogDeliveryConfiguration}},
      "[MaintenanceSchedule](#cfn-timestream-influxdbinstance-maintenanceschedule)" : {{MaintenanceSchedule}},
      "[Name](#cfn-timestream-influxdbinstance-name)" : {{String}},
      "[NetworkType](#cfn-timestream-influxdbinstance-networktype)" : {{String}},
      "[Organization](#cfn-timestream-influxdbinstance-organization)" : {{String}},
      "[Password](#cfn-timestream-influxdbinstance-password)" : {{String}},
      "[Port](#cfn-timestream-influxdbinstance-port)" : {{Integer}},
      "[PubliclyAccessible](#cfn-timestream-influxdbinstance-publiclyaccessible)" : {{Boolean}},
      "[Tags](#cfn-timestream-influxdbinstance-tags)" : {{[ Tag, ... ]}},
      "[Username](#cfn-timestream-influxdbinstance-username)" : {{String}},
      "[VpcSecurityGroupIds](#cfn-timestream-influxdbinstance-vpcsecuritygroupids)" : {{[ String, ... ]}},
      "[VpcSubnetIds](#cfn-timestream-influxdbinstance-vpcsubnetids)" : {{[ String, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-timestream-influxdbinstance-syntax.yaml"></a>

```
Type: AWS::Timestream::InfluxDBInstance
Properties:
  [AllocatedStorage](#cfn-timestream-influxdbinstance-allocatedstorage): {{Integer}}
  [Bucket](#cfn-timestream-influxdbinstance-bucket): {{String}}
  [DbInstanceType](#cfn-timestream-influxdbinstance-dbinstancetype): {{String}}
  [DbParameterGroupIdentifier](#cfn-timestream-influxdbinstance-dbparametergroupidentifier): {{String}}
  [DbStorageType](#cfn-timestream-influxdbinstance-dbstoragetype): {{String}}
  [DeploymentType](#cfn-timestream-influxdbinstance-deploymenttype): {{String}}
  [LogDeliveryConfiguration](#cfn-timestream-influxdbinstance-logdeliveryconfiguration): {{
    LogDeliveryConfiguration}}
  [MaintenanceSchedule](#cfn-timestream-influxdbinstance-maintenanceschedule): {{
    MaintenanceSchedule}}
  [Name](#cfn-timestream-influxdbinstance-name): {{String}}
  [NetworkType](#cfn-timestream-influxdbinstance-networktype): {{String}}
  [Organization](#cfn-timestream-influxdbinstance-organization): {{String}}
  [Password](#cfn-timestream-influxdbinstance-password): {{String}}
  [Port](#cfn-timestream-influxdbinstance-port): {{Integer}}
  [PubliclyAccessible](#cfn-timestream-influxdbinstance-publiclyaccessible): {{Boolean}}
  [Tags](#cfn-timestream-influxdbinstance-tags): {{
    - Tag}}
  [Username](#cfn-timestream-influxdbinstance-username): {{String}}
  [VpcSecurityGroupIds](#cfn-timestream-influxdbinstance-vpcsecuritygroupids): {{
    - String}}
  [VpcSubnetIds](#cfn-timestream-influxdbinstance-vpcsubnetids): {{
    - String}}
```

## Properties
<a name="aws-resource-timestream-influxdbinstance-properties"></a>

`AllocatedStorage`  <a name="cfn-timestream-influxdbinstance-allocatedstorage"></a>
The amount of storage to allocate for your DB storage type in GiB (gibibytes).
*Required*: No
*Type*: Integer
*Minimum*: `20`
*Maximum*: `16384`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Bucket`  <a name="cfn-timestream-influxdbinstance-bucket"></a>
The name of the initial InfluxDB bucket. All InfluxDB data is stored in a bucket. A bucket combines the concept of a database and a retention period (the duration of time that each data point persists). A bucket belongs to an organization.
*Required*: No
*Type*: String
*Pattern*: `^[^_][^"]*$`
*Minimum*: `2`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DbInstanceType`  <a name="cfn-timestream-influxdbinstance-dbinstancetype"></a>
The Timestream for InfluxDB DB instance type to run on.
*Required*: No
*Type*: String
*Allowed values*: `db.influx.medium | db.influx.large | db.influx.xlarge | db.influx.2xlarge | db.influx.4xlarge | db.influx.8xlarge | db.influx.12xlarge | db.influx.16xlarge | db.influx.24xlarge`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DbParameterGroupIdentifier`  <a name="cfn-timestream-influxdbinstance-dbparametergroupidentifier"></a>
The name or id of the DB parameter group to assign to your DB instance. DB parameter groups specify how the database is configured. For example, DB parameter groups can specify the limit for query concurrency.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9]+$`
*Minimum*: `3`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DbStorageType`  <a name="cfn-timestream-influxdbinstance-dbstoragetype"></a>
The Timestream for InfluxDB DB storage type to read and write InfluxDB data.
You can choose between 3 different types of provisioned Influx IOPS included storage according to your workloads requirements:
+ Influx IO Included 3000 IOPS
+ Influx IO Included 12000 IOPS
+ Influx IO Included 16000 IOPS
*Required*: No
*Type*: String
*Allowed values*: `InfluxIOIncludedT1 | InfluxIOIncludedT2 | InfluxIOIncludedT3`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeploymentType`  <a name="cfn-timestream-influxdbinstance-deploymenttype"></a>
Specifies whether the Timestream for InfluxDB is deployed as Single-AZ or with a MultiAZ Standby for High availability.
*Required*: No
*Type*: String
*Allowed values*: `SINGLE_AZ | WITH_MULTIAZ_STANDBY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogDeliveryConfiguration`  <a name="cfn-timestream-influxdbinstance-logdeliveryconfiguration"></a>
Configuration for sending InfluxDB engine logs to a specified S3 bucket.
*Required*: No
*Type*: [LogDeliveryConfiguration](aws-properties-timestream-influxdbinstance-logdeliveryconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaintenanceSchedule`  <a name="cfn-timestream-influxdbinstance-maintenanceschedule"></a>
Property description not available.
*Required*: No
*Type*: [MaintenanceSchedule](aws-properties-timestream-influxdbinstance-maintenanceschedule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-timestream-influxdbinstance-name"></a>
The name that uniquely identifies the DB instance when interacting with the Amazon Timestream for InfluxDB API and CLI commands. This name will also be a prefix included in the endpoint. DB instance names must be unique per customer and per region.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z][a-zA-Z0-9]*(-[a-zA-Z0-9]+)*$`
*Minimum*: `3`
*Maximum*: `40`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NetworkType`  <a name="cfn-timestream-influxdbinstance-networktype"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `IPV4 | DUAL`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Organization`  <a name="cfn-timestream-influxdbinstance-organization"></a>
The name of the initial organization for the initial admin user in InfluxDB. An InfluxDB organization is a workspace for a group of users.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Password`  <a name="cfn-timestream-influxdbinstance-password"></a>
The password of the initial admin user created in InfluxDB. This password will allow you to access the InfluxDB UI to perform various administrative tasks and also use the InfluxDB CLI to create an operator token. These attributes will be stored in a Secret created in Amazon SecretManager in your account.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9]+$`
*Minimum*: `8`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Port`  <a name="cfn-timestream-influxdbinstance-port"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Minimum*: `1024`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PubliclyAccessible`  <a name="cfn-timestream-influxdbinstance-publiclyaccessible"></a>
Configures the DB instance with a public IP to facilitate access.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-timestream-influxdbinstance-tags"></a>
A list of key-value pairs to associate with the DB instance.
*Required*: No
*Type*: Array of [Tag](aws-properties-timestream-influxdbinstance-tag.md)
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Username`  <a name="cfn-timestream-influxdbinstance-username"></a>
The username of the initial admin user created in InfluxDB. Must start with a letter and can't end with a hyphen or contain two consecutive hyphens. For example, my-user1. This username will allow you to access the InfluxDB UI to perform various administrative tasks and also use the InfluxDB CLI to create an operator token. These attributes will be stored in a Secret created in Amazon Secrets Manager in your account.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VpcSecurityGroupIds`  <a name="cfn-timestream-influxdbinstance-vpcsecuritygroupids"></a>
A list of VPC security group IDs to associate with the DB instance.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VpcSubnetIds`  <a name="cfn-timestream-influxdbinstance-vpcsubnetids"></a>
A list of VPC subnet IDs to associate with the DB instance. Provide at least two VPC subnet IDs in different availability zones when deploying with a Multi-AZ standby.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `3`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-timestream-influxdbinstance-return-values"></a>

### Ref
<a name="aws-resource-timestream-influxdbinstance-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-timestream-influxdbinstance-return-values-fn--getatt"></a>

####
<a name="aws-resource-timestream-influxdbinstance-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the DB instance

`AvailabilityZone`  <a name="AvailabilityZone-fn::getatt"></a>
The Availability Zone in which the DB instance resides.

`Endpoint`  <a name="Endpoint-fn::getatt"></a>
The endpoint used to connect to InfluxDB. The default InfluxDB port is 8086.

`Id`  <a name="Id-fn::getatt"></a>
A service-generated unique identifier

`InfluxAuthParametersSecretArn`  <a name="InfluxAuthParametersSecretArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the Amazon Secrets Manager secret containing the initial InfluxDB authorization parameters. The secret value is a JSON formatted key-value pair holding InfluxDB authorization values: organization, bucket, username, and password.

`NextMaintenanceTime`  <a name="NextMaintenanceTime-fn::getatt"></a>
Property description not available.

`SecondaryAvailabilityZone`  <a name="SecondaryAvailabilityZone-fn::getatt"></a>
Describes an Availability Zone in which the InfluxDB instance is located

`Status`  <a name="Status-fn::getatt"></a>
The status of the DB instance.
 Valid Values: `CREATING` \| `AVAILABLE` \| `DELETING` \| `MODIFYING` \| `UPDATING` \| `DELETED` \| `FAILED`
