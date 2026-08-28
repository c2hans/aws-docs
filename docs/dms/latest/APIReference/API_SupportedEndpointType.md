---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_SupportedEndpointType.html
---

# SupportedEndpointType
<a name="API_SupportedEndpointType"></a>

Provides information about types of supported endpoints in response to a request by the `DescribeEndpointTypes` operation. This information includes the type of endpoint, the database engine name, and whether change data capture (CDC) is supported.

## Contents
<a name="API_SupportedEndpointType_Contents"></a>

 ** EndpointType **   <a name="DMS-Type-SupportedEndpointType-EndpointType"></a>
The type of endpoint. Valid values are `source` and `target`.
Type: String
Valid Values: `source | target`
Required: No

 ** EngineDisplayName **   <a name="DMS-Type-SupportedEndpointType-EngineDisplayName"></a>
The expanded name for the engine name. For example, if the `EngineName` parameter is "aurora", this value would be "Amazon Aurora MySQL".
Type: String
Required: No

 ** EngineName **   <a name="DMS-Type-SupportedEndpointType-EngineName"></a>
The database engine name. Valid values, depending on the EndpointType, include `"mysql"`, `"oracle"`, `"postgres"`, `"mariadb"`, `"aurora"`, `"aurora-postgresql"`, `"redshift"`, `"s3"`, `"db2"`, `"db2-zos"`, `"azuredb"`, `"sybase"`, `"dynamodb"`, `"mongodb"`, `"kinesis"`, `"kafka"`, `"elasticsearch"`, `"documentdb"`, `"sqlserver"`, `"neptune"`, and `"babelfish"`.
Type: String
Required: No

 ** ReplicationInstanceEngineMinimumVersion **   <a name="DMS-Type-SupportedEndpointType-ReplicationInstanceEngineMinimumVersion"></a>
The earliest AWS DMS engine version that supports this endpoint engine. Note that endpoint engines released with AWS DMS versions earlier than 3.1.1 do not return a value for this parameter.
Type: String
Required: No

 ** SupportsCDC **   <a name="DMS-Type-SupportedEndpointType-SupportsCDC"></a>
Indicates if change data capture (CDC) is supported.
Type: Boolean
Required: No

## See Also
<a name="API_SupportedEndpointType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/SupportedEndpointType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/SupportedEndpointType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/SupportedEndpointType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
