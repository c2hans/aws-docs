---
source_url: https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_GetDbCluster.html
---

# GetDbCluster
<a name="API_GetDbCluster"></a>

Retrieves information about a Timestream for InfluxDB cluster.

## Request Syntax
<a name="API_GetDbCluster_RequestSyntax"></a>

```
{
   "dbClusterId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetDbCluster_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [dbClusterId](#API_GetDbCluster_RequestSyntax) **   <a name="tsinfluxdb-GetDbCluster-request-dbClusterId"></a>
Service-generated unique identifier of the DB cluster to retrieve.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-zA-Z0-9]+`
Required: Yes

## Response Syntax
<a name="API_GetDbCluster_ResponseSyntax"></a>

```
{
   "allocatedStorage": number,
   "arn": "string",
   "dbInstanceType": "string",
   "dbParameterGroupIdentifier": "string",
   "dbStorageType": "string",
   "deploymentType": "string",
   "endpoint": "string",
   "engineType": "string",
   "failoverMode": "string",
   "id": "string",
   "influxAuthParametersSecretArn": "string",
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
   "readerEndpoint": "string",
   "status": "string",
   "vpcSecurityGroupIds": [ "string" ],
   "vpcSubnetIds": [ "string" ]
}
```

## Response Elements
<a name="API_GetDbCluster_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [allocatedStorage](#API_GetDbCluster_ResponseSyntax) **   <a name="tsinfluxdb-GetDbCluster-response-allocatedStorage"></a>
The amount of storage allocated for your DB storage type (in gibibytes).
Type: Integer
Valid Range: Minimum value of 20. Maximum value of 15360.

 ** [arn](#API_GetDbCluster_ResponseSyntax) **   <a name="tsinfluxdb-GetDbCluster-response-arn"></a>
The Amazon Resource Name (ARN) of the DB cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws[a-z\-]*:timestream\-influxdb:[a-z0-9\-]+:[0-9]{12}:(db\-instance|db\-cluster|db\-parameter\-group)/[a-zA-Z0-9]{3,64}`

 ** [dbInstanceType](#API_GetDbCluster_ResponseSyntax) **   <a name="tsinfluxdb-GetDbCluster-response-dbInstanceType"></a>
The Timestream for InfluxDB instance type that InfluxDB runs on.
Type: String
Valid Values: `db.influx.medium | db.influx.large | db.influx.xlarge | db.influx.2xlarge | db.influx.4xlarge | db.influx.8xlarge | db.influx.12xlarge | db.influx.16xlarge | db.influx.24xlarge`

 ** [dbParameterGroupIdentifier](#API_GetDbCluster_ResponseSyntax) **   <a name="tsinfluxdb-GetDbCluster-response-dbParameterGroupIdentifier"></a>
The ID of the DB parameter group assigned to your DB cluster.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-zA-Z0-9]+`

 ** [dbStorageType](#API_GetDbCluster_ResponseSyntax) **   <a name="tsinfluxdb-GetDbCluster-response-dbStorageType"></a>
The Timestream for InfluxDB DB storage type that InfluxDB stores data on.
Type: String
Valid Values: `InfluxIOIncludedT1 | InfluxIOIncludedT2 | InfluxIOIncludedT3`

 ** [deploymentType](#API_GetDbCluster_ResponseSyntax) **   <a name="tsinfluxdb-GetDbCluster-response-deploymentType"></a>
Deployment type of the DB cluster.
Type: String
Valid Values: `MULTI_NODE_READ_REPLICAS`

 ** [endpoint](#API_GetDbCluster_ResponseSyntax) **   <a name="tsinfluxdb-GetDbCluster-response-endpoint"></a>
The endpoint used to connect to the Timestream for InfluxDB cluster for write and read operations.
Type: String

 ** [engineType](#API_GetDbCluster_ResponseSyntax) **   <a name="tsinfluxdb-GetDbCluster-response-engineType"></a>
The engine type of your DB cluster.
Type: String
Valid Values: `INFLUXDB_V2 | INFLUXDB_V3_CORE | INFLUXDB_V3_ENTERPRISE`

 ** [failoverMode](#API_GetDbCluster_ResponseSyntax) **   <a name="tsinfluxdb-GetDbCluster-response-failoverMode"></a>
The configured failover mode for the DB cluster.
Type: String
Valid Values: `AUTOMATIC | NO_FAILOVER`

 ** [id](#API_GetDbCluster_ResponseSyntax) **   <a name="tsinfluxdb-GetDbCluster-response-id"></a>
Service-generated unique identifier of the DB cluster to retrieve.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-zA-Z0-9]+`

 ** [influxAuthParametersSecretArn](#API_GetDbCluster_ResponseSyntax) **   <a name="tsinfluxdb-GetDbCluster-response-influxAuthParametersSecretArn"></a>
The Amazon Resource Name (ARN) of the AWS Secrets Manager secret containing the initial InfluxDB authorization parameters. The secret value is a JSON formatted key-value pair holding InfluxDB authorization values: organization, bucket, username, and password.
Type: String

 ** [logDeliveryConfiguration](#API_GetDbCluster_ResponseSyntax) **   <a name="tsinfluxdb-GetDbCluster-response-logDeliveryConfiguration"></a>
Configuration for sending InfluxDB engine logs to send to specified S3 bucket.
Type: [LogDeliveryConfiguration](API_LogDeliveryConfiguration.md) object

 ** [name](#API_GetDbCluster_ResponseSyntax) **   <a name="tsinfluxdb-GetDbCluster-response-name"></a>
Customer-supplied name of the Timestream for InfluxDB cluster.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `[a-zA-z][a-zA-Z0-9]*(-[a-zA-Z0-9]+)*`

 ** [networkType](#API_GetDbCluster_ResponseSyntax) **   <a name="tsinfluxdb-GetDbCluster-response-networkType"></a>
Specifies whether the network type of the Timestream for InfluxDB cluster is IPv4, which can communicate over IPv4 protocol only, or DUAL, which can communicate over both IPv4 and IPv6 protocols.
Type: String
Valid Values: `IPV4 | DUAL`

 ** [port](#API_GetDbCluster_ResponseSyntax) **   <a name="tsinfluxdb-GetDbCluster-response-port"></a>
The port number on which InfluxDB accepts connections.
Type: Integer
Valid Range: Minimum value of 1024. Maximum value of 65535.

 ** [publiclyAccessible](#API_GetDbCluster_ResponseSyntax) **   <a name="tsinfluxdb-GetDbCluster-response-publiclyAccessible"></a>
Indicates if the DB cluster has a public IP to facilitate access from outside the VPC.
Type: Boolean

 ** [readerEndpoint](#API_GetDbCluster_ResponseSyntax) **   <a name="tsinfluxdb-GetDbCluster-response-readerEndpoint"></a>
The endpoint used to connect to the Timestream for InfluxDB cluster for read-only operations.
Type: String

 ** [status](#API_GetDbCluster_ResponseSyntax) **   <a name="tsinfluxdb-GetDbCluster-response-status"></a>
The status of the DB cluster.
Type: String
Valid Values: `CREATING | UPDATING | DELETING | AVAILABLE | FAILED | DELETED | MAINTENANCE | UPDATING_INSTANCE_TYPE | REBOOTING | REBOOT_FAILED | PARTIALLY_AVAILABLE`

 ** [vpcSecurityGroupIds](#API_GetDbCluster_ResponseSyntax) **   <a name="tsinfluxdb-GetDbCluster-response-vpcSecurityGroupIds"></a>
A list of VPC security group IDs associated with the DB cluster.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `sg-[a-z0-9]+`

 ** [vpcSubnetIds](#API_GetDbCluster_ResponseSyntax) **   <a name="tsinfluxdb-GetDbCluster-response-vpcSubnetIds"></a>
A list of VPC subnet IDs associated with the DB cluster.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 6 items.
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `subnet-[a-z0-9]+`

## Errors
<a name="API_GetDbCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
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
<a name="API_GetDbCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/timestream-influxdb-2023-01-27/GetDbCluster)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/timestream-influxdb-2023-01-27/GetDbCluster)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-influxdb-2023-01-27/GetDbCluster)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/timestream-influxdb-2023-01-27/GetDbCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-influxdb-2023-01-27/GetDbCluster)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/timestream-influxdb-2023-01-27/GetDbCluster)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/timestream-influxdb-2023-01-27/GetDbCluster)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/timestream-influxdb-2023-01-27/GetDbCluster)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/timestream-influxdb-2023-01-27/GetDbCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-influxdb-2023-01-27/GetDbCluster)
