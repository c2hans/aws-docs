---
source_url: https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_Parameters.html
---

# Parameters
<a name="API_Parameters"></a>

The parameters that comprise the parameter group.

## Contents
<a name="API_Parameters_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** InfluxDBv2 **   <a name="tsinfluxdb-Type-Parameters-InfluxDBv2"></a>
All the customer-modifiable InfluxDB v2 parameters in Timestream for InfluxDB.
Type: [InfluxDBv2Parameters](API_InfluxDBv2Parameters.md) object
Required: No

 ** InfluxDBv3Core **   <a name="tsinfluxdb-Type-Parameters-InfluxDBv3Core"></a>
All the customer-modifiable InfluxDB v3 Core parameters in Timestream for InfluxDB.
Type: [InfluxDBv3CoreParameters](API_InfluxDBv3CoreParameters.md) object
Required: No

 ** InfluxDBv3Enterprise **   <a name="tsinfluxdb-Type-Parameters-InfluxDBv3Enterprise"></a>
All the customer-modifiable InfluxDB v3 Enterprise parameters in Timestream for InfluxDB.
Type: [InfluxDBv3EnterpriseParameters](API_InfluxDBv3EnterpriseParameters.md) object
Required: No

## See Also
<a name="API_Parameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-influxdb-2023-01-27/Parameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-influxdb-2023-01-27/Parameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-influxdb-2023-01-27/Parameters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Timestream for InfluxDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ts-influxdb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
