---
source_url: https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_DbInstanceSummary.html
---

# DbInstanceSummary
<a name="API_DbInstanceSummary"></a>

Contains a summary of a DB instance.

## Contents
<a name="API_DbInstanceSummary_Contents"></a>

 ** arn **   <a name="tsinfluxdb-Type-DbInstanceSummary-arn"></a>
The Amazon Resource Name (ARN) of the DB instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws[a-z\-]*:timestream\-influxdb:[a-z0-9\-]+:[0-9]{12}:(db\-instance|db\-cluster|db\-parameter\-group)/[a-zA-Z0-9]{3,64}`
Required: Yes

 ** id **   <a name="tsinfluxdb-Type-DbInstanceSummary-id"></a>
The service-generated unique identifier of the DB instance.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-zA-Z0-9]+`
Required: Yes

 ** name **   <a name="tsinfluxdb-Type-DbInstanceSummary-name"></a>
This customer-supplied name uniquely identifies the DB instance when interacting with the Amazon Timestream for InfluxDB API and AWS CLI commands.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `[a-zA-Z][a-zA-Z0-9]*(-[a-zA-Z0-9]+)*`
Required: Yes

 ** allocatedStorage **   <a name="tsinfluxdb-Type-DbInstanceSummary-allocatedStorage"></a>
The amount of storage to allocate for your DbStorageType in GiB (gibibytes).
Type: Integer
Valid Range: Minimum value of 20. Maximum value of 15360.
Required: No

 ** dbInstanceType **   <a name="tsinfluxdb-Type-DbInstanceSummary-dbInstanceType"></a>
The Timestream for InfluxDB instance type to run InfluxDB on.
Type: String
Valid Values: `db.influx.medium | db.influx.large | db.influx.xlarge | db.influx.2xlarge | db.influx.4xlarge | db.influx.8xlarge | db.influx.12xlarge | db.influx.16xlarge | db.influx.24xlarge`
Required: No

 ** dbStorageType **   <a name="tsinfluxdb-Type-DbInstanceSummary-dbStorageType"></a>
The storage type for your DB instance.
Type: String
Valid Values: `InfluxIOIncludedT1 | InfluxIOIncludedT2 | InfluxIOIncludedT3`
Required: No

 ** deploymentType **   <a name="tsinfluxdb-Type-DbInstanceSummary-deploymentType"></a>
Single-Instance or with a MultiAZ Standby for High availability.
Type: String
Valid Values: `SINGLE_AZ | WITH_MULTIAZ_STANDBY`
Required: No

 ** endpoint **   <a name="tsinfluxdb-Type-DbInstanceSummary-endpoint"></a>
The endpoint used to connect to InfluxDB. The default InfluxDB port is 8086.
Type: String
Required: No

 ** networkType **   <a name="tsinfluxdb-Type-DbInstanceSummary-networkType"></a>
Specifies whether the networkType of the Timestream for InfluxDB instance is IPV4, which can communicate over IPv4 protocol only, or DUAL, which can communicate over both IPv4 and IPv6 protocols.
Type: String
Valid Values: `IPV4 | DUAL`
Required: No

 ** port **   <a name="tsinfluxdb-Type-DbInstanceSummary-port"></a>
The port number on which InfluxDB accepts connections.
Type: Integer
Valid Range: Minimum value of 1024. Maximum value of 65535.
Required: No

 ** status **   <a name="tsinfluxdb-Type-DbInstanceSummary-status"></a>
The status of the DB instance.
Type: String
Valid Values: `CREATING | AVAILABLE | DELETING | MODIFYING | UPDATING | DELETED | FAILED | UPDATING_DEPLOYMENT_TYPE | UPDATING_INSTANCE_TYPE | MAINTENANCE | REBOOTING | REBOOT_FAILED`
Required: No

## See Also
<a name="API_DbInstanceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-influxdb-2023-01-27/DbInstanceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-influxdb-2023-01-27/DbInstanceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-influxdb-2023-01-27/DbInstanceSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Timestream for InfluxDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ts-influxdb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
