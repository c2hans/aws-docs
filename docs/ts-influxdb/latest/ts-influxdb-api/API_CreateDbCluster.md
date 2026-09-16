---
source_url: https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_CreateDbCluster.html
---

# CreateDbCluster
<a name="API_CreateDbCluster"></a>

Creates a new Timestream for InfluxDB cluster.

## Request Syntax
<a name="API_CreateDbCluster_RequestSyntax"></a>

```
{
   "allocatedStorage": {{number}},
   "bucket": "{{string}}",
   "dbInstanceType": "{{string}}",
   "dbParameterGroupIdentifier": "{{string}}",
   "dbStorageType": "{{string}}",
   "deploymentType": "{{string}}",
   "failoverMode": "{{string}}",
   "logDeliveryConfiguration": {
      "s3Configuration": {
         "bucketName": "{{string}}",
         "enabled": {{boolean}}
      }
   },
   "name": "{{string}}",
   "networkType": "{{string}}",
   "organization": "{{string}}",
   "password": "{{string}}",
   "port": {{number}},
   "publiclyAccessible": {{boolean}},
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "username": "{{string}}",
   "vpcSecurityGroupIds": [ "{{string}}" ],
   "vpcSubnetIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_CreateDbCluster_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [allocatedStorage](#API_CreateDbCluster_RequestSyntax) **   <a name="tsinfluxdb-CreateDbCluster-request-allocatedStorage"></a>
The amount of storage to allocate for your DB storage type in GiB (gibibytes).
Type: Integer
Valid Range: Minimum value of 20. Maximum value of 15360.
Required: No

 ** [bucket](#API_CreateDbCluster_RequestSyntax) **   <a name="tsinfluxdb-CreateDbCluster-request-bucket"></a>
The name of the initial InfluxDB bucket. All InfluxDB data is stored in a bucket. A bucket combines the concept of a database and a retention period (the duration of time that each data point persists). A bucket belongs to an organization.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 64.
Pattern: `[^_"][^"]*`
Required: No

 ** [dbInstanceType](#API_CreateDbCluster_RequestSyntax) **   <a name="tsinfluxdb-CreateDbCluster-request-dbInstanceType"></a>
The Timestream for InfluxDB DB instance type to run InfluxDB on.
Type: String
Valid Values: `db.influx.medium | db.influx.large | db.influx.xlarge | db.influx.2xlarge | db.influx.4xlarge | db.influx.8xlarge | db.influx.12xlarge | db.influx.16xlarge | db.influx.24xlarge`
Required: Yes

 ** [dbParameterGroupIdentifier](#API_CreateDbCluster_RequestSyntax) **   <a name="tsinfluxdb-CreateDbCluster-request-dbParameterGroupIdentifier"></a>
The ID of the DB parameter group to assign to your DB cluster. DB parameter groups specify how the database is configured. For example, DB parameter groups can specify the limit for query concurrency.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-zA-Z0-9]+`
Required: No

 ** [dbStorageType](#API_CreateDbCluster_RequestSyntax) **   <a name="tsinfluxdb-CreateDbCluster-request-dbStorageType"></a>
The Timestream for InfluxDB DB storage type to read and write InfluxDB data.
You can choose between three different types of provisioned Influx IOPS Included storage according to your workload requirements:
+ Influx I/O Included 3000 IOPS
+ Influx I/O Included 12000 IOPS
+ Influx I/O Included 16000 IOPS
Type: String
Valid Values: `InfluxIOIncludedT1 | InfluxIOIncludedT2 | InfluxIOIncludedT3`
Required: No

 ** [deploymentType](#API_CreateDbCluster_RequestSyntax) **   <a name="tsinfluxdb-CreateDbCluster-request-deploymentType"></a>
Specifies the type of cluster to create.
Type: String
Valid Values: `MULTI_NODE_READ_REPLICAS`
Required: No

 ** [failoverMode](#API_CreateDbCluster_RequestSyntax) **   <a name="tsinfluxdb-CreateDbCluster-request-failoverMode"></a>
Specifies the behavior of failure recovery when the primary node of the cluster fails.
Type: String
Valid Values: `AUTOMATIC | NO_FAILOVER`
Required: No

 ** [logDeliveryConfiguration](#API_CreateDbCluster_RequestSyntax) **   <a name="tsinfluxdb-CreateDbCluster-request-logDeliveryConfiguration"></a>
Configuration for sending InfluxDB engine logs to a specified S3 bucket.
Type: [LogDeliveryConfiguration](API_LogDeliveryConfiguration.md) object
Required: No

 ** [name](#API_CreateDbCluster_RequestSyntax) **   <a name="tsinfluxdb-CreateDbCluster-request-name"></a>
The name that uniquely identifies the DB cluster when interacting with the Amazon Timestream for InfluxDB API and CLI commands. This name will also be a prefix included in the endpoint. DB cluster names must be unique per customer and per region.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `[a-zA-z][a-zA-Z0-9]*(-[a-zA-Z0-9]+)*`
Required: Yes

 ** [networkType](#API_CreateDbCluster_RequestSyntax) **   <a name="tsinfluxdb-CreateDbCluster-request-networkType"></a>
Specifies whether the network type of the Timestream for InfluxDB cluster is IPv4, which can communicate over IPv4 protocol only, or DUAL, which can communicate over both IPv4 and IPv6 protocols.
Type: String
Valid Values: `IPV4 | DUAL`
Required: No

 ** [organization](#API_CreateDbCluster_RequestSyntax) **   <a name="tsinfluxdb-CreateDbCluster-request-organization"></a>
The name of the initial organization for the initial admin user in InfluxDB. An InfluxDB organization is a workspace for a group of users.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** [password](#API_CreateDbCluster_RequestSyntax) **   <a name="tsinfluxdb-CreateDbCluster-request-password"></a>
The password of the initial admin user created in InfluxDB. This password will allow you to access the InfluxDB UI to perform various administrative tasks and also use the InfluxDB CLI to create an operator token. These attributes will be stored in a secret created in AWS Secrets Manager in your account.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 64.
Pattern: `[a-zA-Z0-9]+`
Required: No

 ** [port](#API_CreateDbCluster_RequestSyntax) **   <a name="tsinfluxdb-CreateDbCluster-request-port"></a>
The port number on which InfluxDB accepts connections.
Valid Values: 1024-65535
Default: 8086 for InfluxDB v2, 8181 for InfluxDB v3
Constraints: The value can't be 2375-2376, 7788-7799, 8090, or 51678-51680
Type: Integer
Valid Range: Minimum value of 1024. Maximum value of 65535.
Required: No

 ** [publiclyAccessible](#API_CreateDbCluster_RequestSyntax) **   <a name="tsinfluxdb-CreateDbCluster-request-publiclyAccessible"></a>
Configures the Timestream for InfluxDB cluster with a public IP to facilitate access from outside the VPC.
Type: Boolean
Required: No

 ** [tags](#API_CreateDbCluster_RequestSyntax) **   <a name="tsinfluxdb-CreateDbCluster-request-tags"></a>
A list of key-value pairs to associate with the DB instance.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [username](#API_CreateDbCluster_RequestSyntax) **   <a name="tsinfluxdb-CreateDbCluster-request-username"></a>
The username of the initial admin user created in InfluxDB. Must start with a letter and can't end with a hyphen or contain two consecutive hyphens. For example, my-user1. This username will allow you to access the InfluxDB UI to perform various administrative tasks and also use the InfluxDB CLI to create an operator token. These attributes will be stored in a secret created in AWS Secrets Manager in your account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** [vpcSecurityGroupIds](#API_CreateDbCluster_RequestSyntax) **   <a name="tsinfluxdb-CreateDbCluster-request-vpcSecurityGroupIds"></a>
A list of VPC security group IDs to associate with the Timestream for InfluxDB cluster.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `sg-[a-z0-9]+`
Required: Yes

 ** [vpcSubnetIds](#API_CreateDbCluster_RequestSyntax) **   <a name="tsinfluxdb-CreateDbCluster-request-vpcSubnetIds"></a>
A list of VPC subnet IDs to associate with the DB cluster. Provide at least two VPC subnet IDs in different Availability Zones when deploying with a Multi-AZ standby.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 6 items.
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `subnet-[a-z0-9]+`
Required: Yes

## Response Syntax
<a name="API_CreateDbCluster_ResponseSyntax"></a>

```
{
   "dbClusterId": "string",
   "dbClusterStatus": "string"
}
```

## Response Elements
<a name="API_CreateDbCluster_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [dbClusterId](#API_CreateDbCluster_ResponseSyntax) **   <a name="tsinfluxdb-CreateDbCluster-response-dbClusterId"></a>
A service-generated unique identifier.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-zA-Z0-9]+`

 ** [dbClusterStatus](#API_CreateDbCluster_ResponseSyntax) **   <a name="tsinfluxdb-CreateDbCluster-response-dbClusterStatus"></a>
The status of the DB cluster.
Type: String
Valid Values: `CREATING | UPDATING | DELETING | AVAILABLE | FAILED | DELETED | MAINTENANCE | UPDATING_INSTANCE_TYPE | REBOOTING | REBOOT_FAILED | PARTIALLY_AVAILABLE`

## Errors
<a name="API_CreateDbCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** ConflictException **
The request conflicts with an existing resource in Timestream for InfluxDB.
 ** resourceId **
The identifier for the Timestream for InfluxDB resource associated with the request.
 ** resourceType **
The type of Timestream for InfluxDB resource associated with the request.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource was not found or does not exist.
 ** resourceId **
The identifier for the Timestream for InfluxDB resource associated with the request.
 ** resourceType **
The type of Timestream for InfluxDB resource associated with the request.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
The request exceeds the service quota.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
 ** retryAfterSeconds **
The number of seconds the caller should wait before retrying.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by Timestream for InfluxDB.
 ** reason **
The reason that validation failed.
HTTP Status Code: 400

## See Also
<a name="API_CreateDbCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/timestream-influxdb-2023-01-27/CreateDbCluster)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/timestream-influxdb-2023-01-27/CreateDbCluster)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-influxdb-2023-01-27/CreateDbCluster)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/timestream-influxdb-2023-01-27/CreateDbCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-influxdb-2023-01-27/CreateDbCluster)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/timestream-influxdb-2023-01-27/CreateDbCluster)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/timestream-influxdb-2023-01-27/CreateDbCluster)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/timestream-influxdb-2023-01-27/CreateDbCluster)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/timestream-influxdb-2023-01-27/CreateDbCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-influxdb-2023-01-27/CreateDbCluster)
