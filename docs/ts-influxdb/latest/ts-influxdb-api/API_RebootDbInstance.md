---
source_url: https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_RebootDbInstance.html
---

# RebootDbInstance
<a name="API_RebootDbInstance"></a>

Reboots a Timestream for InfluxDB instance.

## Request Syntax
<a name="API_RebootDbInstance_RequestSyntax"></a>

```
{
   "identifier": "{{string}}"
}
```

## Request Parameters
<a name="API_RebootDbInstance_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [identifier](#API_RebootDbInstance_RequestSyntax) **   <a name="tsinfluxdb-RebootDbInstance-request-identifier"></a>
The id of the DB instance to reboot.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-zA-Z0-9]+`
Required: Yes

## Response Syntax
<a name="API_RebootDbInstance_ResponseSyntax"></a>

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
<a name="API_RebootDbInstance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [allocatedStorage](#API_RebootDbInstance_ResponseSyntax) **   <a name="tsinfluxdb-RebootDbInstance-response-allocatedStorage"></a>
The amount of storage allocated for your DB storage type (in gibibytes).
Type: Integer
Valid Range: Minimum value of 20. Maximum value of 15360.

 ** [arn](#API_RebootDbInstance_ResponseSyntax) **   <a name="tsinfluxdb-RebootDbInstance-response-arn"></a>
The Amazon Resource Name (ARN) of the DB instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws[a-z\-]*:timestream\-influxdb:[a-z0-9\-]+:[0-9]{12}:(db\-instance|db\-cluster|db\-parameter\-group)/[a-zA-Z0-9]{3,64}`

 ** [availabilityZone](#API_RebootDbInstance_ResponseSyntax) **   <a name="tsinfluxdb-RebootDbInstance-response-availabilityZone"></a>
The Availability Zone in which the DB instance resides.
Type: String

 ** [dbClusterId](#API_RebootDbInstance_ResponseSyntax) **   <a name="tsinfluxdb-RebootDbInstance-response-dbClusterId"></a>
Specifies the DbCluster to which this DbInstance belongs to.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-zA-Z0-9]+`

 ** [dbInstanceType](#API_RebootDbInstance_ResponseSyntax) **   <a name="tsinfluxdb-RebootDbInstance-response-dbInstanceType"></a>
The Timestream for InfluxDB instance type that InfluxDB runs on.
Type: String
Valid Values: `db.influx.medium | db.influx.large | db.influx.xlarge | db.influx.2xlarge | db.influx.4xlarge | db.influx.8xlarge | db.influx.12xlarge | db.influx.16xlarge | db.influx.24xlarge`

 ** [dbParameterGroupIdentifier](#API_RebootDbInstance_ResponseSyntax) **   <a name="tsinfluxdb-RebootDbInstance-response-dbParameterGroupIdentifier"></a>
The id of the DB parameter group assigned to your DB instance.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-zA-Z0-9]+`

 ** [dbStorageType](#API_RebootDbInstance_ResponseSyntax) **   <a name="tsinfluxdb-RebootDbInstance-response-dbStorageType"></a>
The Timestream for InfluxDB DB storage type that InfluxDB stores data on.
Type: String
Valid Values: `InfluxIOIncludedT1 | InfluxIOIncludedT2 | InfluxIOIncludedT3`

 ** [deploymentType](#API_RebootDbInstance_ResponseSyntax) **   <a name="tsinfluxdb-RebootDbInstance-response-deploymentType"></a>
Specifies whether the Timestream for InfluxDB is deployed as Single-AZ or with a MultiAZ Standby for High availability.
Type: String
Valid Values: `SINGLE_AZ | WITH_MULTIAZ_STANDBY`

 ** [endpoint](#API_RebootDbInstance_ResponseSyntax) **   <a name="tsinfluxdb-RebootDbInstance-response-endpoint"></a>
The endpoint used to connect to InfluxDB. The default InfluxDB port is 8086.
Type: String

 ** [id](#API_RebootDbInstance_ResponseSyntax) **   <a name="tsinfluxdb-RebootDbInstance-response-id"></a>
A service-generated unique identifier.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-zA-Z0-9]+`

 ** [influxAuthParametersSecretArn](#API_RebootDbInstance_ResponseSyntax) **   <a name="tsinfluxdb-RebootDbInstance-response-influxAuthParametersSecretArn"></a>
The Amazon Resource Name (ARN) of the AWS Secrets Manager secret containing the initial InfluxDB authorization parameters. The secret value is a JSON formatted key-value pair holding InfluxDB authorization values: organization, bucket, username, and password.
Type: String

 ** [instanceMode](#API_RebootDbInstance_ResponseSyntax) **   <a name="tsinfluxdb-RebootDbInstance-response-instanceMode"></a>
Specifies the DbInstance's role in the cluster.
Type: String
Valid Values: `PRIMARY | STANDBY | REPLICA | INGEST | QUERY | COMPACT | PROCESS`

 ** [instanceModes](#API_RebootDbInstance_ResponseSyntax) **   <a name="tsinfluxdb-RebootDbInstance-response-instanceModes"></a>
Specifies the DbInstance's roles in the cluster.
Type: Array of strings
Valid Values: `PRIMARY | STANDBY | REPLICA | INGEST | QUERY | COMPACT | PROCESS`

 ** [logDeliveryConfiguration](#API_RebootDbInstance_ResponseSyntax) **   <a name="tsinfluxdb-RebootDbInstance-response-logDeliveryConfiguration"></a>
Configuration for sending InfluxDB engine logs to send to specified S3 bucket.
Type: [LogDeliveryConfiguration](API_LogDeliveryConfiguration.md) object

 ** [name](#API_RebootDbInstance_ResponseSyntax) **   <a name="tsinfluxdb-RebootDbInstance-response-name"></a>
The customer-supplied name that uniquely identifies the DB instance when interacting with the Amazon Timestream for InfluxDB API and CLI commands.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `[a-zA-Z][a-zA-Z0-9]*(-[a-zA-Z0-9]+)*`

 ** [networkType](#API_RebootDbInstance_ResponseSyntax) **   <a name="tsinfluxdb-RebootDbInstance-response-networkType"></a>
Specifies whether the networkType of the Timestream for InfluxDB instance is IPV4, which can communicate over IPv4 protocol only, or DUAL, which can communicate over both IPv4 and IPv6 protocols.
Type: String
Valid Values: `IPV4 | DUAL`

 ** [port](#API_RebootDbInstance_ResponseSyntax) **   <a name="tsinfluxdb-RebootDbInstance-response-port"></a>
The port number on which InfluxDB accepts connections.
Type: Integer
Valid Range: Minimum value of 1024. Maximum value of 65535.

 ** [publiclyAccessible](#API_RebootDbInstance_ResponseSyntax) **   <a name="tsinfluxdb-RebootDbInstance-response-publiclyAccessible"></a>
Indicates if the DB instance has a public IP to facilitate access.
Type: Boolean

 ** [secondaryAvailabilityZone](#API_RebootDbInstance_ResponseSyntax) **   <a name="tsinfluxdb-RebootDbInstance-response-secondaryAvailabilityZone"></a>
The Availability Zone in which the standby instance is located when deploying with a MultiAZ standby instance.
Type: String

 ** [status](#API_RebootDbInstance_ResponseSyntax) **   <a name="tsinfluxdb-RebootDbInstance-response-status"></a>
The status of the DB instance.
Type: String
Valid Values: `CREATING | AVAILABLE | DELETING | MODIFYING | UPDATING | DELETED | FAILED | UPDATING_DEPLOYMENT_TYPE | UPDATING_INSTANCE_TYPE | MAINTENANCE | REBOOTING | REBOOT_FAILED`

 ** [vpcSecurityGroupIds](#API_RebootDbInstance_ResponseSyntax) **   <a name="tsinfluxdb-RebootDbInstance-response-vpcSecurityGroupIds"></a>
A list of VPC security group IDs associated with the DB instance.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `sg-[a-z0-9]+`

 ** [vpcSubnetIds](#API_RebootDbInstance_ResponseSyntax) **   <a name="tsinfluxdb-RebootDbInstance-response-vpcSubnetIds"></a>
A list of VPC subnet IDs associated with the DB instance.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 6 items.
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `subnet-[a-z0-9]+`

## Errors
<a name="API_RebootDbInstance_Errors"></a>

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
<a name="API_RebootDbInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/timestream-influxdb-2023-01-27/RebootDbInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/timestream-influxdb-2023-01-27/RebootDbInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-influxdb-2023-01-27/RebootDbInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/timestream-influxdb-2023-01-27/RebootDbInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-influxdb-2023-01-27/RebootDbInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/timestream-influxdb-2023-01-27/RebootDbInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/timestream-influxdb-2023-01-27/RebootDbInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/timestream-influxdb-2023-01-27/RebootDbInstance)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/timestream-influxdb-2023-01-27/RebootDbInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-influxdb-2023-01-27/RebootDbInstance)
