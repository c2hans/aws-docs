---
source_url: https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_CreateDbInstance.html
---

# CreateDbInstance
<a name="API_CreateDbInstance"></a>

Creates a new Timestream for InfluxDB DB instance.

## Request Syntax
<a name="API_CreateDbInstance_RequestSyntax"></a>

```
{
   "allocatedStorage": {{number}},
   "bucket": "{{string}}",
   "dbInstanceType": "{{string}}",
   "dbParameterGroupIdentifier": "{{string}}",
   "dbStorageType": "{{string}}",
   "deploymentType": "{{string}}",
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
<a name="API_CreateDbInstance_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [allocatedStorage](#API_CreateDbInstance_RequestSyntax) **   <a name="tsinfluxdb-CreateDbInstance-request-allocatedStorage"></a>
The amount of storage to allocate for your DB storage type in GiB (gibibytes).
Type: Integer
Valid Range: Minimum value of 20. Maximum value of 15360.
Required: Yes

 ** [bucket](#API_CreateDbInstance_RequestSyntax) **   <a name="tsinfluxdb-CreateDbInstance-request-bucket"></a>
The name of the initial InfluxDB bucket. All InfluxDB data is stored in a bucket. A bucket combines the concept of a database and a retention period (the duration of time that each data point persists). A bucket belongs to an organization.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 64.
Pattern: `[^_"][^"]*`
Required: No

 ** [dbInstanceType](#API_CreateDbInstance_RequestSyntax) **   <a name="tsinfluxdb-CreateDbInstance-request-dbInstanceType"></a>
The Timestream for InfluxDB DB instance type to run InfluxDB on.
Type: String
Valid Values: `db.influx.medium | db.influx.large | db.influx.xlarge | db.influx.2xlarge | db.influx.4xlarge | db.influx.8xlarge | db.influx.12xlarge | db.influx.16xlarge | db.influx.24xlarge`
Required: Yes

 ** [dbParameterGroupIdentifier](#API_CreateDbInstance_RequestSyntax) **   <a name="tsinfluxdb-CreateDbInstance-request-dbParameterGroupIdentifier"></a>
The id of the DB parameter group to assign to your DB instance. DB parameter groups specify how the database is configured. For example, DB parameter groups can specify the limit for query concurrency.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-zA-Z0-9]+`
Required: No

 ** [dbStorageType](#API_CreateDbInstance_RequestSyntax) **   <a name="tsinfluxdb-CreateDbInstance-request-dbStorageType"></a>
The Timestream for InfluxDB DB storage type to read and write InfluxDB data.
You can choose between 3 different types of provisioned Influx IOPS included storage according to your workloads requirements:
+ Influx IO Included 3000 IOPS
+ Influx IO Included 12000 IOPS
+ Influx IO Included 16000 IOPS
Type: String
Valid Values: `InfluxIOIncludedT1 | InfluxIOIncludedT2 | InfluxIOIncludedT3`
Required: No

 ** [deploymentType](#API_CreateDbInstance_RequestSyntax) **   <a name="tsinfluxdb-CreateDbInstance-request-deploymentType"></a>
Specifies whether the DB instance will be deployed as a standalone instance or with a Multi-AZ standby for high availability.
Type: String
Valid Values: `SINGLE_AZ | WITH_MULTIAZ_STANDBY`
Required: No

 ** [logDeliveryConfiguration](#API_CreateDbInstance_RequestSyntax) **   <a name="tsinfluxdb-CreateDbInstance-request-logDeliveryConfiguration"></a>
Configuration for sending InfluxDB engine logs to a specified S3 bucket.
Type: [LogDeliveryConfiguration](API_LogDeliveryConfiguration.md) object
Required: No

 ** [name](#API_CreateDbInstance_RequestSyntax) **   <a name="tsinfluxdb-CreateDbInstance-request-name"></a>
The name that uniquely identifies the DB instance when interacting with the Amazon Timestream for InfluxDB API and CLI commands. This name will also be a prefix included in the endpoint. DB instance names must be unique per customer and per region.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `[a-zA-Z][a-zA-Z0-9]*(-[a-zA-Z0-9]+)*`
Required: Yes

 ** [networkType](#API_CreateDbInstance_RequestSyntax) **   <a name="tsinfluxdb-CreateDbInstance-request-networkType"></a>
Specifies whether the networkType of the Timestream for InfluxDB instance is IPV4, which can communicate over IPv4 protocol only, or DUAL, which can communicate over both IPv4 and IPv6 protocols.
Type: String
Valid Values: `IPV4 | DUAL`
Required: No

 ** [organization](#API_CreateDbInstance_RequestSyntax) **   <a name="tsinfluxdb-CreateDbInstance-request-organization"></a>
The name of the initial organization for the initial admin user in InfluxDB. An InfluxDB organization is a workspace for a group of users.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** [password](#API_CreateDbInstance_RequestSyntax) **   <a name="tsinfluxdb-CreateDbInstance-request-password"></a>
The password of the initial admin user created in InfluxDB v2. This password will allow you to access the InfluxDB UI to perform various administrative tasks and also use the InfluxDB CLI to create an operator token. These attributes will be stored in a Secret created in AWS Secrets Manager in your account.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 64.
Pattern: `[a-zA-Z0-9]+`
Required: Yes

 ** [port](#API_CreateDbInstance_RequestSyntax) **   <a name="tsinfluxdb-CreateDbInstance-request-port"></a>
The port number on which InfluxDB accepts connections.
Valid Values: 1024-65535
Default: 8086
Constraints: The value can't be 2375-2376, 7788-7799, 8090, or 51678-51680
Type: Integer
Valid Range: Minimum value of 1024. Maximum value of 65535.
Required: No

 ** [publiclyAccessible](#API_CreateDbInstance_RequestSyntax) **   <a name="tsinfluxdb-CreateDbInstance-request-publiclyAccessible"></a>
Configures the DB instance with a public IP to facilitate access.
Type: Boolean
Required: No

 ** [tags](#API_CreateDbInstance_RequestSyntax) **   <a name="tsinfluxdb-CreateDbInstance-request-tags"></a>
A list of key-value pairs to associate with the DB instance.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [username](#API_CreateDbInstance_RequestSyntax) **   <a name="tsinfluxdb-CreateDbInstance-request-username"></a>
The username of the initial admin user created in InfluxDB. Must start with a letter and can't end with a hyphen or contain two consecutive hyphens. For example, my-user1. This username will allow you to access the InfluxDB UI to perform various administrative tasks and also use the InfluxDB CLI to create an operator token. These attributes will be stored in a Secret created in Amazon Secrets Manager in your account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** [vpcSecurityGroupIds](#API_CreateDbInstance_RequestSyntax) **   <a name="tsinfluxdb-CreateDbInstance-request-vpcSecurityGroupIds"></a>
A list of VPC security group IDs to associate with the DB instance.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `sg-[a-z0-9]+`
Required: Yes

 ** [vpcSubnetIds](#API_CreateDbInstance_RequestSyntax) **   <a name="tsinfluxdb-CreateDbInstance-request-vpcSubnetIds"></a>
A list of VPC subnet IDs to associate with the DB instance. Provide at least two VPC subnet IDs in different availability zones when deploying with a Multi-AZ standby.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 6 items.
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `subnet-[a-z0-9]+`
Required: Yes

## Response Syntax
<a name="API_CreateDbInstance_ResponseSyntax"></a>

```
{
   "allocatedStorage": number,
   "arn": "string",
   "availabilityZone": "string",
   "dbClusterId": "string",
   "dbInstanceType": "string",
   "dbParameterGroupIdentifier": "string",
   "dbStorageType": "string",
   "deploymentType": "string",
   "endpoint": "string",
   "id": "string",
   "influxAuthParametersSecretArn": "string",
   "instanceMode": "string",
   "instanceModes": [ "string" ],
   "logDeliveryConfiguration": {
      "s3Configuration": {
         "bucketName": "string",
         "enabled": boolean
      }
   },
   "name": "string",
   "networkType": "string",
   "port": number,
   "publiclyAccessible": boolean,
   "secondaryAvailabilityZone": "string",
   "status": "string",
   "vpcSecurityGroupIds": [ "string" ],
   "vpcSubnetIds": [ "string" ]
}
```

## Response Elements
<a name="API_CreateDbInstance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [allocatedStorage](#API_CreateDbInstance_ResponseSyntax) **   <a name="tsinfluxdb-CreateDbInstance-response-allocatedStorage"></a>
The amount of storage allocated for your DB storage type (in gibibytes).
Type: Integer
Valid Range: Minimum value of 20. Maximum value of 15360.

 ** [arn](#API_CreateDbInstance_ResponseSyntax) **   <a name="tsinfluxdb-CreateDbInstance-response-arn"></a>
The Amazon Resource Name (ARN) of the DB instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws[a-z\-]*:timestream\-influxdb:[a-z0-9\-]+:[0-9]{12}:(db\-instance|db\-cluster|db\-parameter\-group)/[a-zA-Z0-9]{3,64}`

 ** [availabilityZone](#API_CreateDbInstance_ResponseSyntax) **   <a name="tsinfluxdb-CreateDbInstance-response-availabilityZone"></a>
The Availability Zone in which the DB instance resides.
Type: String

 ** [dbClusterId](#API_CreateDbInstance_ResponseSyntax) **   <a name="tsinfluxdb-CreateDbInstance-response-dbClusterId"></a>
Specifies the DbCluster to which this DbInstance belongs to.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-zA-Z0-9]+`

 ** [dbInstanceType](#API_CreateDbInstance_ResponseSyntax) **   <a name="tsinfluxdb-CreateDbInstance-response-dbInstanceType"></a>
The Timestream for InfluxDB instance type that InfluxDB runs on.
Type: String
Valid Values: `db.influx.medium | db.influx.large | db.influx.xlarge | db.influx.2xlarge | db.influx.4xlarge | db.influx.8xlarge | db.influx.12xlarge | db.influx.16xlarge | db.influx.24xlarge`

 ** [dbParameterGroupIdentifier](#API_CreateDbInstance_ResponseSyntax) **   <a name="tsinfluxdb-CreateDbInstance-response-dbParameterGroupIdentifier"></a>
The id of the DB parameter group assigned to your DB instance.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-zA-Z0-9]+`

 ** [dbStorageType](#API_CreateDbInstance_ResponseSyntax) **   <a name="tsinfluxdb-CreateDbInstance-response-dbStorageType"></a>
The Timestream for InfluxDB DB storage type that InfluxDB stores data on.
Type: String
Valid Values: `InfluxIOIncludedT1 | InfluxIOIncludedT2 | InfluxIOIncludedT3`

 ** [deploymentType](#API_CreateDbInstance_ResponseSyntax) **   <a name="tsinfluxdb-CreateDbInstance-response-deploymentType"></a>
Specifies whether the Timestream for InfluxDB is deployed as Single-AZ or with a MultiAZ Standby for High availability.
Type: String
Valid Values: `SINGLE_AZ | WITH_MULTIAZ_STANDBY`

 ** [endpoint](#API_CreateDbInstance_ResponseSyntax) **   <a name="tsinfluxdb-CreateDbInstance-response-endpoint"></a>
The endpoint used to connect to InfluxDB. The default InfluxDB port is 8086.
Type: String

 ** [id](#API_CreateDbInstance_ResponseSyntax) **   <a name="tsinfluxdb-CreateDbInstance-response-id"></a>
A service-generated unique identifier.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-zA-Z0-9]+`

 ** [influxAuthParametersSecretArn](#API_CreateDbInstance_ResponseSyntax) **   <a name="tsinfluxdb-CreateDbInstance-response-influxAuthParametersSecretArn"></a>
The Amazon Resource Name (ARN) of the AWS Secrets Manager secret containing the initial InfluxDB authorization parameters. The secret value is a JSON formatted key-value pair holding InfluxDB authorization values: organization, bucket, username, and password.
Type: String

 ** [instanceMode](#API_CreateDbInstance_ResponseSyntax) **   <a name="tsinfluxdb-CreateDbInstance-response-instanceMode"></a>
Specifies the DbInstance's role in the cluster.
Type: String
Valid Values: `PRIMARY | STANDBY | REPLICA | INGEST | QUERY | COMPACT | PROCESS`

 ** [instanceModes](#API_CreateDbInstance_ResponseSyntax) **   <a name="tsinfluxdb-CreateDbInstance-response-instanceModes"></a>
Specifies the DbInstance's roles in the cluster.
Type: Array of strings
Valid Values: `PRIMARY | STANDBY | REPLICA | INGEST | QUERY | COMPACT | PROCESS`

 ** [logDeliveryConfiguration](#API_CreateDbInstance_ResponseSyntax) **   <a name="tsinfluxdb-CreateDbInstance-response-logDeliveryConfiguration"></a>
Configuration for sending InfluxDB engine logs to send to specified S3 bucket.
Type: [LogDeliveryConfiguration](API_LogDeliveryConfiguration.md) object

 ** [name](#API_CreateDbInstance_ResponseSyntax) **   <a name="tsinfluxdb-CreateDbInstance-response-name"></a>
The customer-supplied name that uniquely identifies the DB instance when interacting with the Amazon Timestream for InfluxDB API and CLI commands.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `[a-zA-Z][a-zA-Z0-9]*(-[a-zA-Z0-9]+)*`

 ** [networkType](#API_CreateDbInstance_ResponseSyntax) **   <a name="tsinfluxdb-CreateDbInstance-response-networkType"></a>
Specifies whether the networkType of the Timestream for InfluxDB instance is IPV4, which can communicate over IPv4 protocol only, or DUAL, which can communicate over both IPv4 and IPv6 protocols.
Type: String
Valid Values: `IPV4 | DUAL`

 ** [port](#API_CreateDbInstance_ResponseSyntax) **   <a name="tsinfluxdb-CreateDbInstance-response-port"></a>
The port number on which InfluxDB accepts connections. The default value is 8086.
Type: Integer
Valid Range: Minimum value of 1024. Maximum value of 65535.

 ** [publiclyAccessible](#API_CreateDbInstance_ResponseSyntax) **   <a name="tsinfluxdb-CreateDbInstance-response-publiclyAccessible"></a>
Indicates if the DB instance has a public IP to facilitate access.
Type: Boolean

 ** [secondaryAvailabilityZone](#API_CreateDbInstance_ResponseSyntax) **   <a name="tsinfluxdb-CreateDbInstance-response-secondaryAvailabilityZone"></a>
The Availability Zone in which the standby instance is located when deploying with a MultiAZ standby instance.
Type: String

 ** [status](#API_CreateDbInstance_ResponseSyntax) **   <a name="tsinfluxdb-CreateDbInstance-response-status"></a>
The status of the DB instance.
Type: String
Valid Values: `CREATING | AVAILABLE | DELETING | MODIFYING | UPDATING | DELETED | FAILED | UPDATING_DEPLOYMENT_TYPE | UPDATING_INSTANCE_TYPE | MAINTENANCE | REBOOTING | REBOOT_FAILED`

 ** [vpcSecurityGroupIds](#API_CreateDbInstance_ResponseSyntax) **   <a name="tsinfluxdb-CreateDbInstance-response-vpcSecurityGroupIds"></a>
A list of VPC security group IDs associated with the DB instance.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `sg-[a-z0-9]+`

 ** [vpcSubnetIds](#API_CreateDbInstance_ResponseSyntax) **   <a name="tsinfluxdb-CreateDbInstance-response-vpcSubnetIds"></a>
A list of VPC subnet IDs associated with the DB instance.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 6 items.
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `subnet-[a-z0-9]+`

## Errors
<a name="API_CreateDbInstance_Errors"></a>

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
<a name="API_CreateDbInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/timestream-influxdb-2023-01-27/CreateDbInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/timestream-influxdb-2023-01-27/CreateDbInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-influxdb-2023-01-27/CreateDbInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/timestream-influxdb-2023-01-27/CreateDbInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-influxdb-2023-01-27/CreateDbInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/timestream-influxdb-2023-01-27/CreateDbInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/timestream-influxdb-2023-01-27/CreateDbInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/timestream-influxdb-2023-01-27/CreateDbInstance)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/timestream-influxdb-2023-01-27/CreateDbInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-influxdb-2023-01-27/CreateDbInstance)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Timestream for InfluxDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ts-influxdb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
