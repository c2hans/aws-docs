---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_KafkaSettings.html
---

# KafkaSettings
<a name="API_KafkaSettings"></a>

Provides information that describes an Apache Kafka endpoint. This information includes the output format of records applied to the endpoint and details of transaction and control table data information.

## Contents
<a name="API_KafkaSettings_Contents"></a>

 ** Broker **   <a name="DMS-Type-KafkaSettings-Broker"></a>
A comma-separated list of one or more broker locations in your Kafka cluster that host your Kafka instance. Specify each broker location in the form ` broker-hostname-or-ip:port `. For example, `"ec2-12-345-678-901.compute-1.amazonaws.com:2345"`. For more information and examples of specifying a list of broker locations, see [Using Apache Kafka as a target for AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Kafka.html) in the * AWS Database Migration Service User Guide*.
Type: String
Required: No

 ** IncludeControlDetails **   <a name="DMS-Type-KafkaSettings-IncludeControlDetails"></a>
Shows detailed control information for table definition, column definition, and table and column changes in the Kafka message output. The default is `false`.
Type: Boolean
Required: No

 ** IncludeNullAndEmpty **   <a name="DMS-Type-KafkaSettings-IncludeNullAndEmpty"></a>
Include NULL and empty columns for records migrated to the endpoint. The default is `false`.
Type: Boolean
Required: No

 ** IncludePartitionValue **   <a name="DMS-Type-KafkaSettings-IncludePartitionValue"></a>
Shows the partition value within the Kafka message output unless the partition type is `schema-table-type`. The default is `false`.
Type: Boolean
Required: No

 ** IncludeTableAlterOperations **   <a name="DMS-Type-KafkaSettings-IncludeTableAlterOperations"></a>
Includes any data definition language (DDL) operations that change the table in the control data, such as `rename-table`, `drop-table`, `add-column`, `drop-column`, and `rename-column`. The default is `false`.
Type: Boolean
Required: No

 ** IncludeTransactionDetails **   <a name="DMS-Type-KafkaSettings-IncludeTransactionDetails"></a>
Provides detailed transaction information from the source database. This information includes a commit timestamp, a log position, and values for `transaction_id`, previous `transaction_id`, and `transaction_record_id` (the record offset within a transaction). The default is `false`.
Type: Boolean
Required: No

 ** MessageFormat **   <a name="DMS-Type-KafkaSettings-MessageFormat"></a>
The output format for the records created on the endpoint. The message format is `JSON` (default) or `JSON_UNFORMATTED` (a single line with no tab).
Type: String
Valid Values: `json | json-unformatted`
Required: No

 ** MessageMaxBytes **   <a name="DMS-Type-KafkaSettings-MessageMaxBytes"></a>
The maximum size in bytes for records created on the endpoint The default is 1,000,000.
Type: Integer
Required: No

 ** NoHexPrefix **   <a name="DMS-Type-KafkaSettings-NoHexPrefix"></a>
Set this optional parameter to `true` to avoid adding a '0x' prefix to raw data in hexadecimal format. For example, by default, AWS DMS adds a '0x' prefix to the LOB column type in hexadecimal format moving from an Oracle source to a Kafka target. Use the `NoHexPrefix` endpoint setting to enable migration of RAW data type columns without adding the '0x' prefix.
Type: Boolean
Required: No

 ** PartitionIncludeSchemaTable **   <a name="DMS-Type-KafkaSettings-PartitionIncludeSchemaTable"></a>
Prefixes schema and table names to partition values, when the partition type is `primary-key-type`. Doing this increases data distribution among Kafka partitions. For example, suppose that a SysBench schema has thousands of tables and each table has only limited range for a primary key. In this case, the same primary key is sent from thousands of tables to the same partition, which causes throttling. The default is `false`.
Type: Boolean
Required: No

 ** SaslMechanism **   <a name="DMS-Type-KafkaSettings-SaslMechanism"></a>
For SASL/SSL authentication, AWS DMS supports the `SCRAM-SHA-512` mechanism by default. AWS DMS versions 3.5.0 and later also support the `PLAIN` mechanism. To use the `PLAIN` mechanism, set this parameter to `PLAIN.`
Type: String
Valid Values: `scram-sha-512 | plain`
Required: No

 ** SaslPassword **   <a name="DMS-Type-KafkaSettings-SaslPassword"></a>
The secure password you created when you first set up your MSK cluster to validate a client identity and make an encrypted connection between server and client using SASL-SSL authentication.
Type: String
Required: No

 ** SaslUsername **   <a name="DMS-Type-KafkaSettings-SaslUsername"></a>
 The secure user name you created when you first set up your MSK cluster to validate a client identity and make an encrypted connection between server and client using SASL-SSL authentication.
Type: String
Required: No

 ** SecurityProtocol **   <a name="DMS-Type-KafkaSettings-SecurityProtocol"></a>
Set secure connection to a Kafka target endpoint using Transport Layer Security (TLS). Options include `ssl-encryption`, `ssl-authentication`, and `sasl-ssl`. `sasl-ssl` requires `SaslUsername` and `SaslPassword`.
Type: String
Valid Values: `plaintext | ssl-authentication | ssl-encryption | sasl-ssl`
Required: No

 ** SslCaCertificateArn **   <a name="DMS-Type-KafkaSettings-SslCaCertificateArn"></a>
 The Amazon Resource Name (ARN) for the private certificate authority (CA) cert that AWS DMS uses to securely connect to your Kafka target endpoint.
Type: String
Required: No

 ** SslClientCertificateArn **   <a name="DMS-Type-KafkaSettings-SslClientCertificateArn"></a>
The Amazon Resource Name (ARN) of the client certificate used to securely connect to a Kafka target endpoint.
Type: String
Required: No

 ** SslClientKeyArn **   <a name="DMS-Type-KafkaSettings-SslClientKeyArn"></a>
The Amazon Resource Name (ARN) for the client private key used to securely connect to a Kafka target endpoint.
Type: String
Required: No

 ** SslClientKeyPassword **   <a name="DMS-Type-KafkaSettings-SslClientKeyPassword"></a>
 The password for the client private key used to securely connect to a Kafka target endpoint.
Type: String
Required: No

 ** SslEndpointIdentificationAlgorithm **   <a name="DMS-Type-KafkaSettings-SslEndpointIdentificationAlgorithm"></a>
Sets hostname verification for the certificate. This setting is supported in AWS DMS version 3.5.1 and later.
Type: String
Valid Values: `none | https`
Required: No

 ** Topic **   <a name="DMS-Type-KafkaSettings-Topic"></a>
The topic to which you migrate the data. If you don't specify a topic, AWS DMS specifies `"kafka-default-topic"` as the migration topic.
Type: String
Required: No

 ** UseLargeIntegerValue **   <a name="DMS-Type-KafkaSettings-UseLargeIntegerValue"></a>
Specifies using the large integer value with Kafka.
Type: Boolean
Required: No

## See Also
<a name="API_KafkaSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/KafkaSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/KafkaSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/KafkaSettings)
