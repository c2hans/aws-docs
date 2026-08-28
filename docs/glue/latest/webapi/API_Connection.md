---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_Connection.html
---

# Connection
<a name="API_Connection"></a>

Defines a connection to a data source.

## Contents
<a name="API_Connection_Contents"></a>

 ** AthenaProperties **   <a name="Glue-Type-Connection-AthenaProperties"></a>
Connection properties specific to the Athena compute environment.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** AuthenticationConfiguration **   <a name="Glue-Type-Connection-AuthenticationConfiguration"></a>
The authentication properties of the connection.
Type: [AuthenticationConfiguration](API_AuthenticationConfiguration.md) object
Required: No

 ** CompatibleComputeEnvironments **   <a name="Glue-Type-Connection-CompatibleComputeEnvironments"></a>
A list of compute environments compatible with the connection.
Type: Array of strings
Valid Values: `SPARK | ATHENA | PYTHON`
Required: No

 ** ConnectionProperties **   <a name="Glue-Type-Connection-ConnectionProperties"></a>
These key-value pairs define parameters for the connection when using the version 1 Connection schema:
+  `HOST` - The host URI: either the fully qualified domain name (FQDN) or the IPv4 address of the database host.
+  `PORT` - The port number, between 1024 and 65535, of the port on which the database host is listening for database connections.
+  `USER_NAME` - The name under which to log in to the database. The value string for `USER_NAME` is "`USERNAME`".
+  `PASSWORD` - A password, if one is used, for the user name.
+  `ENCRYPTED_PASSWORD` - When you enable connection password protection by setting `ConnectionPasswordEncryption` in the Data Catalog encryption settings, this field stores the encrypted password.
+  `JDBC_DRIVER_JAR_URI` - The Amazon Simple Storage Service (Amazon S3) path of the JAR file that contains the JDBC driver to use.
+  `JDBC_DRIVER_CLASS_NAME` - The class name of the JDBC driver to use.
+  `JDBC_ENGINE` - The name of the JDBC engine to use.
+  `JDBC_ENGINE_VERSION` - The version of the JDBC engine to use.
+  `CONFIG_FILES` - (Reserved for future use.)
+  `INSTANCE_ID` - The instance ID to use.
+  `JDBC_CONNECTION_URL` - The URL for connecting to a JDBC data source.
+  `JDBC_ENFORCE_SSL` - A case-insensitive Boolean string (true, false) specifying whether Secure Sockets Layer (SSL) with hostname matching is enforced for the JDBC connection on the client. The default is false.
+  `CUSTOM_JDBC_CERT` - An Amazon S3 location specifying the customer's root certificate. AWS Glue uses this root certificate to validate the customer’s certificate when connecting to the customer database. AWS Glue only handles X.509 certificates. The certificate provided must be DER-encoded and supplied in Base64 encoding PEM format.
+  `SKIP_CUSTOM_JDBC_CERT_VALIDATION` - By default, this is `false`. AWS Glue validates the Signature algorithm and Subject Public Key Algorithm for the customer certificate. The only permitted algorithms for the Signature algorithm are SHA256withRSA, SHA384withRSA or SHA512withRSA. For the Subject Public Key Algorithm, the key length must be at least 2048. You can set the value of this property to `true` to skip AWS Glue’s validation of the customer certificate.
+  `CUSTOM_JDBC_CERT_STRING` - A custom JDBC certificate string which is used for domain match or distinguished name match to prevent a man-in-the-middle attack. In Oracle database, this is used as the `SSL_SERVER_CERT_DN`; in Microsoft SQL Server, this is used as the `hostNameInCertificate`.
+  `CONNECTION_URL` - The URL for connecting to a general (non-JDBC) data source.
+  `SECRET_ID` - The secret ID used for the secret manager of credentials.
+  `CONNECTOR_URL` - The connector URL for a MARKETPLACE or CUSTOM connection.
+  `CONNECTOR_TYPE` - The connector type for a MARKETPLACE or CUSTOM connection.
+  `CONNECTOR_CLASS_NAME` - The connector class name for a MARKETPLACE or CUSTOM connection.
+  `KAFKA_BOOTSTRAP_SERVERS` - A comma-separated list of host and port pairs that are the addresses of the Apache Kafka brokers in a Kafka cluster to which a Kafka client will connect to and bootstrap itself.
+  `KAFKA_SSL_ENABLED` - Whether to enable or disable SSL on an Apache Kafka connection. Default value is "true".
+  `KAFKA_CUSTOM_CERT` - The Amazon S3 URL for the private CA cert file (.pem format). The default is an empty string.
+  `KAFKA_SKIP_CUSTOM_CERT_VALIDATION` - Whether to skip the validation of the CA cert file or not. AWS Glue validates for three algorithms: SHA256withRSA, SHA384withRSA and SHA512withRSA. Default value is "false".
+  `KAFKA_CLIENT_KEYSTORE` - The Amazon S3 location of the client keystore file for Kafka client side authentication (Optional).
+  `KAFKA_CLIENT_KEYSTORE_PASSWORD` - The password to access the provided keystore (Optional).
+  `KAFKA_CLIENT_KEY_PASSWORD` - A keystore can consist of multiple keys, so this is the password to access the client key to be used with the Kafka server side key (Optional).
+  `ENCRYPTED_KAFKA_CLIENT_KEYSTORE_PASSWORD` - The encrypted version of the Kafka client keystore password (if the user has the AWS Glue encrypt passwords setting selected).
+  `ENCRYPTED_KAFKA_CLIENT_KEY_PASSWORD` - The encrypted version of the Kafka client key password (if the user has the AWS Glue encrypt passwords setting selected).
+  `KAFKA_SASL_MECHANISM` - `"SCRAM-SHA-512"`, `"GSSAPI"`, `"AWS_MSK_IAM"`, or `"PLAIN"`. These are the supported [SASL Mechanisms](https://www.iana.org/assignments/sasl-mechanisms/sasl-mechanisms.xhtml).
+  `KAFKA_SASL_PLAIN_USERNAME` - A plaintext username used to authenticate with the "PLAIN" mechanism.
+  `KAFKA_SASL_PLAIN_PASSWORD` - A plaintext password used to authenticate with the "PLAIN" mechanism.
+  `ENCRYPTED_KAFKA_SASL_PLAIN_PASSWORD` - The encrypted version of the Kafka SASL PLAIN password (if the user has the AWS Glue encrypt passwords setting selected).
+  `KAFKA_SASL_SCRAM_USERNAME` - A plaintext username used to authenticate with the "SCRAM-SHA-512" mechanism.
+  `KAFKA_SASL_SCRAM_PASSWORD` - A plaintext password used to authenticate with the "SCRAM-SHA-512" mechanism.
+  `ENCRYPTED_KAFKA_SASL_SCRAM_PASSWORD` - The encrypted version of the Kafka SASL SCRAM password (if the user has the AWS Glue encrypt passwords setting selected).
+  `KAFKA_SASL_SCRAM_SECRETS_ARN` - The Amazon Resource Name of a secret in AWS Secrets Manager.
+  `KAFKA_SASL_GSSAPI_KEYTAB` - The S3 location of a Kerberos `keytab` file. A keytab stores long-term keys for one or more principals. For more information, see [MIT Kerberos Documentation: Keytab](https://web.mit.edu/kerberos/krb5-latest/doc/basic/keytab_def.html).
+  `KAFKA_SASL_GSSAPI_KRB5_CONF` - The S3 location of a Kerberos `krb5.conf` file. A krb5.conf stores Kerberos configuration information, such as the location of the KDC server. For more information, see [MIT Kerberos Documentation: krb5.conf](https://web.mit.edu/kerberos/krb5-1.12/doc/admin/conf_files/krb5_conf.html).
+  `KAFKA_SASL_GSSAPI_SERVICE` - The Kerberos service name, as set with `sasl.kerberos.service.name` in your [Kafka Configuration](https://kafka.apache.org/documentation/#brokerconfigs_sasl.kerberos.service.name).
+  `KAFKA_SASL_GSSAPI_PRINCIPAL` - The name of the Kerberos princial used by AWS Glue. For more information, see [Kafka Documentation: Configuring Kafka Brokers](https://kafka.apache.org/documentation/#security_sasl_kerberos_clientconfig).
+  `ROLE_ARN` - The role to be used for running queries.
+  `REGION` - The AWS Region where queries will be run.
+  `WORKGROUP_NAME` - The name of an Amazon Redshift serverless workgroup or Amazon Athena workgroup in which queries will run.
+  `CLUSTER_IDENTIFIER` - The cluster identifier of an Amazon Redshift cluster in which queries will run.
+  `DATABASE` - The Amazon Redshift database that you are connecting to.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 100 items.
Valid Keys: `HOST | PORT | USERNAME | PASSWORD | ENCRYPTED_PASSWORD | JDBC_DRIVER_JAR_URI | JDBC_DRIVER_CLASS_NAME | JDBC_ENGINE | JDBC_ENGINE_VERSION | CONFIG_FILES | INSTANCE_ID | JDBC_CONNECTION_URL | JDBC_ENFORCE_SSL | CUSTOM_JDBC_CERT | SKIP_CUSTOM_JDBC_CERT_VALIDATION | CUSTOM_JDBC_CERT_STRING | CONNECTION_URL | KAFKA_BOOTSTRAP_SERVERS | KAFKA_SSL_ENABLED | KAFKA_CUSTOM_CERT | KAFKA_SKIP_CUSTOM_CERT_VALIDATION | KAFKA_CLIENT_KEYSTORE | KAFKA_CLIENT_KEYSTORE_PASSWORD | KAFKA_CLIENT_KEY_PASSWORD | ENCRYPTED_KAFKA_CLIENT_KEYSTORE_PASSWORD | ENCRYPTED_KAFKA_CLIENT_KEY_PASSWORD | KAFKA_SASL_MECHANISM | KAFKA_SASL_PLAIN_USERNAME | KAFKA_SASL_PLAIN_PASSWORD | ENCRYPTED_KAFKA_SASL_PLAIN_PASSWORD | KAFKA_SASL_SCRAM_USERNAME | KAFKA_SASL_SCRAM_PASSWORD | KAFKA_SASL_SCRAM_SECRETS_ARN | ENCRYPTED_KAFKA_SASL_SCRAM_PASSWORD | KAFKA_SASL_GSSAPI_KEYTAB | KAFKA_SASL_GSSAPI_KRB5_CONF | KAFKA_SASL_GSSAPI_SERVICE | KAFKA_SASL_GSSAPI_PRINCIPAL | SECRET_ID | CONNECTOR_URL | CONNECTOR_TYPE | CONNECTOR_CLASS_NAME | ENDPOINT | ENDPOINT_TYPE | ROLE_ARN | REGION | WORKGROUP_NAME | CLUSTER_IDENTIFIER | DATABASE`
Value Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** ConnectionSchemaVersion **   <a name="Glue-Type-Connection-ConnectionSchemaVersion"></a>
The version of the connection schema for this connection. Version 2 supports properties for specific compute environments.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 2.
Required: No

 ** ConnectionType **   <a name="Glue-Type-Connection-ConnectionType"></a>
The type of the connection. Currently, SFTP is not supported.
Type: String
Valid Values: `JDBC | SFTP | MONGODB | KAFKA | NETWORK | MARKETPLACE | CUSTOM | SALESFORCE | VIEW_VALIDATION_REDSHIFT | VIEW_VALIDATION_ATHENA | GOOGLEADS | GOOGLESHEETS | GOOGLEANALYTICS4 | SERVICENOW | MARKETO | SAPODATA | ZENDESK | JIRACLOUD | NETSUITEERP | HUBSPOT | FACEBOOKADS | INSTAGRAMADS | ZOHOCRM | SALESFORCEPARDOT | SALESFORCEMARKETINGCLOUD | ADOBEANALYTICS | SLACK | LINKEDIN | MIXPANEL | ASANA | STRIPE | SMARTSHEET | DATADOG | WOOCOMMERCE | INTERCOM | SNAPCHATADS | PAYPAL | QUICKBOOKS | FACEBOOKPAGEINSIGHTS | FRESHDESK | TWILIO | DOCUSIGNMONITOR | FRESHSALES | ZOOM | GOOGLESEARCHCONSOLE | SALESFORCECOMMERCECLOUD | SAPCONCUR | DYNATRACE | MICROSOFTDYNAMIC365FINANCEANDOPS | MICROSOFTTEAMS | BLACKBAUDRAISEREDGENXT | MAILCHIMP | GITLAB | PENDO | PRODUCTBOARD | CIRCLECI | PIPEDIVE | SENDGRID | AZURECOSMOS | AZURESQL | BIGQUERY | BLACKBAUD | CLOUDERAHIVE | CLOUDERAIMPALA | CLOUDWATCH | CLOUDWATCHMETRICS | CMDB | DATALAKEGEN2 | DB2 | DB2AS400 | DOCUMENTDB | DOMO | DYNAMODB | GOOGLECLOUDSTORAGE | HBASE | KUSTOMER | MICROSOFTDYNAMICS365CRM | MONDAY | MYSQL | OKTA | OPENSEARCH | ORACLE | PIPEDRIVE | POSTGRESQL | SAPHANA | SQLSERVER | SYNAPSE | TERADATA | TERADATANOS | TIMESTREAM | TPCDS | VERTICA`
Required: No

 ** CreationTime **   <a name="Glue-Type-Connection-CreationTime"></a>
The timestamp of the time that this connection definition was created.
Type: Timestamp
Required: No

 ** Description **   <a name="Glue-Type-Connection-Description"></a>
The description of the connection.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** LastConnectionValidationTime **   <a name="Glue-Type-Connection-LastConnectionValidationTime"></a>
A timestamp of the time this connection was last validated.
Type: Timestamp
Required: No

 ** LastUpdatedBy **   <a name="Glue-Type-Connection-LastUpdatedBy"></a>
The user, group, or role that last updated this connection definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** LastUpdatedTime **   <a name="Glue-Type-Connection-LastUpdatedTime"></a>
The timestamp of the last time the connection definition was updated.
Type: Timestamp
Required: No

 ** MatchCriteria **   <a name="Glue-Type-Connection-MatchCriteria"></a>
A list of criteria that can be used in selecting this connection.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** Name **   <a name="Glue-Type-Connection-Name"></a>
The name of the connection definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** PhysicalConnectionRequirements **   <a name="Glue-Type-Connection-PhysicalConnectionRequirements"></a>
The physical connection requirements, such as virtual private cloud (VPC) and `SecurityGroup`, that are needed to make this connection successfully.
Type: [PhysicalConnectionRequirements](API_PhysicalConnectionRequirements.md) object
Required: No

 ** PythonProperties **   <a name="Glue-Type-Connection-PythonProperties"></a>
Connection properties specific to the Python compute environment.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** SparkProperties **   <a name="Glue-Type-Connection-SparkProperties"></a>
Connection properties specific to the Spark compute environment.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** Status **   <a name="Glue-Type-Connection-Status"></a>
The status of the connection. Can be one of: `READY`, `IN_PROGRESS`, or `FAILED`.
Type: String
Valid Values: `READY | IN_PROGRESS | FAILED`
Required: No

 ** StatusReason **   <a name="Glue-Type-Connection-StatusReason"></a>
The reason for the connection status.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16384.
Required: No

## See Also
<a name="API_Connection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/Connection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/Connection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/Connection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
