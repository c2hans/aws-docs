---
source_url: https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_DbInstanceForClusterSummary.html
---

# DbInstanceForClusterSummary
<a name="API_DbInstanceForClusterSummary"></a>

Contains a summary of a DB instance belonging to a DB cluster.

## Contents
<a name="API_DbInstanceForClusterSummary_Contents"></a>

 ** arn **   <a name="tsinfluxdb-Type-DbInstanceForClusterSummary-arn"></a>
The Amazon Resource Name (ARN) of the DB instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws[a-z\-]*:timestream\-influxdb:[a-z0-9\-]+:[0-9]{12}:(db\-instance|db\-cluster|db\-parameter\-group)/[a-zA-Z0-9]{3,64}`
Required: Yes

 ** id **   <a name="tsinfluxdb-Type-DbInstanceForClusterSummary-id"></a>
The service-generated unique identifier of the DB instance.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-zA-Z0-9]+`
Required: Yes

 ** name **   <a name="tsinfluxdb-Type-DbInstanceForClusterSummary-name"></a>
A service-generated name for the DB instance based on the customer-supplied name for the DB cluster.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `[a-zA-Z][a-zA-Z0-9]*(-[a-zA-Z0-9]+)*`
Required: Yes

 ** allocatedStorage **   <a name="tsinfluxdb-Type-DbInstanceForClusterSummary-allocatedStorage"></a>
The amount of storage allocated for your DB storage type in GiB (gibibytes).
Type: Integer
Valid Range: Minimum value of 20. Maximum value of 15360.
Required: No

 ** dbInstanceType **   <a name="tsinfluxdb-Type-DbInstanceForClusterSummary-dbInstanceType"></a>
The Timestream for InfluxDB instance type to run InfluxDB on.
Type: String
Valid Values: `db.influx.medium | db.influx.large | db.influx.xlarge | db.influx.2xlarge | db.influx.4xlarge | db.influx.8xlarge | db.influx.12xlarge | db.influx.16xlarge | db.influx.24xlarge`
Required: No

 ** dbStorageType **   <a name="tsinfluxdb-Type-DbInstanceForClusterSummary-dbStorageType"></a>
The storage type for your DB instance.
Type: String
Valid Values: `InfluxIOIncludedT1 | InfluxIOIncludedT2 | InfluxIOIncludedT3`
Required: No

 ** deploymentType **   <a name="tsinfluxdb-Type-DbInstanceForClusterSummary-deploymentType"></a>
Specifies the deployment type if applicable.
Type: String
Valid Values: `SINGLE_AZ | WITH_MULTIAZ_STANDBY`
Required: No

 ** endpoint **   <a name="tsinfluxdb-Type-DbInstanceForClusterSummary-endpoint"></a>
The endpoint used to connect to InfluxDB. The default InfluxDB port is 8086.
Type: String
Required: No

 ** instanceMode **   <a name="tsinfluxdb-Type-DbInstanceForClusterSummary-instanceMode"></a>
Specifies the DB instance's role in the cluster.
Type: String
Valid Values: `PRIMARY | STANDBY | REPLICA | INGEST | QUERY | COMPACT | PROCESS`
Required: No

 ** instanceModes **   <a name="tsinfluxdb-Type-DbInstanceForClusterSummary-instanceModes"></a>
Specifies the DB instance's roles in the cluster.
Type: Array of strings
Valid Values: `PRIMARY | STANDBY | REPLICA | INGEST | QUERY | COMPACT | PROCESS`
Required: No

 ** networkType **   <a name="tsinfluxdb-Type-DbInstanceForClusterSummary-networkType"></a>
Specifies whether the network type of the Timestream for InfluxDB instance is IPv4, which can communicate over IPv4 protocol only, or DUAL, which can communicate over both IPv4 and IPv6 protocols.
Type: String
Valid Values: `IPV4 | DUAL`
Required: No

 ** port **   <a name="tsinfluxdb-Type-DbInstanceForClusterSummary-port"></a>
The port number on which InfluxDB accepts connections.
Type: Integer
Valid Range: Minimum value of 1024. Maximum value of 65535.
Required: No

 ** status **   <a name="tsinfluxdb-Type-DbInstanceForClusterSummary-status"></a>
The status of the DB instance.
Type: String
Valid Values: `CREATING | AVAILABLE | DELETING | MODIFYING | UPDATING | DELETED | FAILED | UPDATING_DEPLOYMENT_TYPE | UPDATING_INSTANCE_TYPE | MAINTENANCE | REBOOTING | REBOOT_FAILED`
Required: No

## See Also
<a name="API_DbInstanceForClusterSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-influxdb-2023-01-27/DbInstanceForClusterSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-influxdb-2023-01-27/DbInstanceForClusterSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-influxdb-2023-01-27/DbInstanceForClusterSummary)
