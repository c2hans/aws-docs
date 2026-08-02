---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ConnectionInput.html
---

# ConnectionInput
<a name="API_ConnectionInput"></a>

A structure that is used to specify a connection to create or update.

## Contents
<a name="API_ConnectionInput_Contents"></a>

 ** ConnectionProperties **   <a name="Glue-Type-ConnectionInput-ConnectionProperties"></a>
These key-value pairs define parameters for the connection.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 100 items.
Valid Keys: `HOST | PORT | USERNAME | PASSWORD | ENCRYPTED_PASSWORD | JDBC_DRIVER_JAR_URI | JDBC_DRIVER_CLASS_NAME | JDBC_ENGINE | JDBC_ENGINE_VERSION | CONFIG_FILES | INSTANCE_ID | JDBC_CONNECTION_URL | JDBC_ENFORCE_SSL | CUSTOM_JDBC_CERT | SKIP_CUSTOM_JDBC_CERT_VALIDATION | CUSTOM_JDBC_CERT_STRING | CONNECTION_URL | KAFKA_BOOTSTRAP_SERVERS | KAFKA_SSL_ENABLED | KAFKA_CUSTOM_CERT | KAFKA_SKIP_CUSTOM_CERT_VALIDATION | KAFKA_CLIENT_KEYSTORE | KAFKA_CLIENT_KEYSTORE_PASSWORD | KAFKA_CLIENT_KEY_PASSWORD | ENCRYPTED_KAFKA_CLIENT_KEYSTORE_PASSWORD | ENCRYPTED_KAFKA_CLIENT_KEY_PASSWORD | KAFKA_SASL_MECHANISM | KAFKA_SASL_PLAIN_USERNAME | KAFKA_SASL_PLAIN_PASSWORD | ENCRYPTED_KAFKA_SASL_PLAIN_PASSWORD | KAFKA_SASL_SCRAM_USERNAME | KAFKA_SASL_SCRAM_PASSWORD | KAFKA_SASL_SCRAM_SECRETS_ARN | ENCRYPTED_KAFKA_SASL_SCRAM_PASSWORD | KAFKA_SASL_GSSAPI_KEYTAB | KAFKA_SASL_GSSAPI_KRB5_CONF | KAFKA_SASL_GSSAPI_SERVICE | KAFKA_SASL_GSSAPI_PRINCIPAL | SECRET_ID | CONNECTOR_URL | CONNECTOR_TYPE | CONNECTOR_CLASS_NAME | ENDPOINT | ENDPOINT_TYPE | ROLE_ARN | REGION | WORKGROUP_NAME | CLUSTER_IDENTIFIER | DATABASE`
Value Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** ConnectionType **   <a name="Glue-Type-ConnectionInput-ConnectionType"></a>
The type of the connection. Currently, these types are supported:
+  `JDBC` - Designates a connection to a database through Java Database Connectivity (JDBC).

   `JDBC` Connections use the following ConnectionParameters.
  + Required: All of (`HOST`, `PORT`, `JDBC_ENGINE`) or `JDBC_CONNECTION_URL`.
  + Required: All of (`USERNAME`, `PASSWORD`) or `SECRET_ID`.
  + Optional: `JDBC_ENFORCE_SSL`, `CUSTOM_JDBC_CERT`, `CUSTOM_JDBC_CERT_STRING`, `SKIP_CUSTOM_JDBC_CERT_VALIDATION`. These parameters are used to configure SSL with JDBC.
+  `KAFKA` - Designates a connection to an Apache Kafka streaming platform.

   `KAFKA` Connections use the following ConnectionParameters.
  + Required: `KAFKA_BOOTSTRAP_SERVERS`.
  + Optional: `KAFKA_SSL_ENABLED`, `KAFKA_CUSTOM_CERT`, `KAFKA_SKIP_CUSTOM_CERT_VALIDATION`. These parameters are used to configure SSL with `KAFKA`.
  + Optional: `KAFKA_CLIENT_KEYSTORE`, `KAFKA_CLIENT_KEYSTORE_PASSWORD`, `KAFKA_CLIENT_KEY_PASSWORD`, `ENCRYPTED_KAFKA_CLIENT_KEYSTORE_PASSWORD`, `ENCRYPTED_KAFKA_CLIENT_KEY_PASSWORD`. These parameters are used to configure TLS client configuration with SSL in `KAFKA`.
  + Optional: `KAFKA_SASL_MECHANISM`. Can be specified as `SCRAM-SHA-512`, `GSSAPI`, or `AWS_MSK_IAM`.
  + Optional: `KAFKA_SASL_SCRAM_USERNAME`, `KAFKA_SASL_SCRAM_PASSWORD`, `ENCRYPTED_KAFKA_SASL_SCRAM_PASSWORD`. These parameters are used to configure SASL/SCRAM-SHA-512 authentication with `KAFKA`.
  + Optional: `KAFKA_SASL_GSSAPI_KEYTAB`, `KAFKA_SASL_GSSAPI_KRB5_CONF`, `KAFKA_SASL_GSSAPI_SERVICE`, `KAFKA_SASL_GSSAPI_PRINCIPAL`. These parameters are used to configure SASL/GSSAPI authentication with `KAFKA`.
+  `MONGODB` - Designates a connection to a MongoDB document database.

   `MONGODB` Connections use the following ConnectionParameters.
  + Required: `CONNECTION_URL`.
  + Required: All of (`USERNAME`, `PASSWORD`) or `SECRET_ID`.
+  `VIEW_VALIDATION_REDSHIFT` - Designates a connection used for view validation by Amazon Redshift.
+  `VIEW_VALIDATION_ATHENA` - Designates a connection used for view validation by Amazon Athena.
+  `NETWORK` - Designates a network connection to a data source within an Amazon Virtual Private Cloud environment (Amazon VPC).

   `NETWORK` Connections do not require ConnectionParameters. Instead, provide a PhysicalConnectionRequirements.
+  `MARKETPLACE` - Uses configuration settings contained in a connector purchased from AWS Marketplace to read from and write to data stores that are not natively supported by AWS Glue.

   `MARKETPLACE` Connections use the following ConnectionParameters.
  + Required: `CONNECTOR_TYPE`, `CONNECTOR_URL`, `CONNECTOR_CLASS_NAME`, `CONNECTION_URL`.
  + Required for `JDBC` `CONNECTOR_TYPE` connections: All of (`USERNAME`, `PASSWORD`) or `SECRET_ID`.
+  `CUSTOM` - Uses configuration settings contained in a custom connector to read from and write to data stores that are not natively supported by AWS Glue.
For more information on the connection parameters needed for a particular connector, see the documentation for the connector in [Adding an AWS Glue connection](https://docs.aws.amazon.com/glue/latest/dg/console-connections.html)in the AWS Glue User Guide.
 `SFTP` is not supported.
For more information about how optional ConnectionProperties are used to configure features in AWS Glue, consult [AWS Glue connection properties](https://docs.aws.amazon.com/glue/latest/dg/connection-defining.html).
For more information about how optional ConnectionProperties are used to configure features in AWS Glue Studio, consult [Using connectors and connections](https://docs.aws.amazon.com/glue/latest/ug/connectors-chapter.html).
Type: String
Valid Values: `JDBC | SFTP | MONGODB | KAFKA | NETWORK | MARKETPLACE | CUSTOM | SALESFORCE | VIEW_VALIDATION_REDSHIFT | VIEW_VALIDATION_ATHENA | GOOGLEADS | GOOGLESHEETS | GOOGLEANALYTICS4 | SERVICENOW | MARKETO | SAPODATA | ZENDESK | JIRACLOUD | NETSUITEERP | HUBSPOT | FACEBOOKADS | INSTAGRAMADS | ZOHOCRM | SALESFORCEPARDOT | SALESFORCEMARKETINGCLOUD | ADOBEANALYTICS | SLACK | LINKEDIN | MIXPANEL | ASANA | STRIPE | SMARTSHEET | DATADOG | WOOCOMMERCE | INTERCOM | SNAPCHATADS | PAYPAL | QUICKBOOKS | FACEBOOKPAGEINSIGHTS | FRESHDESK | TWILIO | DOCUSIGNMONITOR | FRESHSALES | ZOOM | GOOGLESEARCHCONSOLE | SALESFORCECOMMERCECLOUD | SAPCONCUR | DYNATRACE | MICROSOFTDYNAMIC365FINANCEANDOPS | MICROSOFTTEAMS | BLACKBAUDRAISEREDGENXT | MAILCHIMP | GITLAB | PENDO | PRODUCTBOARD | CIRCLECI | PIPEDIVE | SENDGRID | AZURECOSMOS | AZURESQL | BIGQUERY | BLACKBAUD | CLOUDERAHIVE | CLOUDERAIMPALA | CLOUDWATCH | CLOUDWATCHMETRICS | CMDB | DATALAKEGEN2 | DB2 | DB2AS400 | DOCUMENTDB | DOMO | DYNAMODB | GOOGLECLOUDSTORAGE | HBASE | KUSTOMER | MICROSOFTDYNAMICS365CRM | MONDAY | MYSQL | OKTA | OPENSEARCH | ORACLE | PIPEDRIVE | POSTGRESQL | SAPHANA | SQLSERVER | SYNAPSE | TERADATA | TERADATANOS | TIMESTREAM | TPCDS | VERTICA`
Required: Yes

 ** Name **   <a name="Glue-Type-ConnectionInput-Name"></a>
The name of the connection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** AthenaProperties **   <a name="Glue-Type-ConnectionInput-AthenaProperties"></a>
Connection properties specific to the Athena compute environment.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** AuthenticationConfiguration **   <a name="Glue-Type-ConnectionInput-AuthenticationConfiguration"></a>
The authentication properties of the connection.
Type: [AuthenticationConfigurationInput](API_AuthenticationConfigurationInput.md) object
Required: No

 ** Description **   <a name="Glue-Type-ConnectionInput-Description"></a>
The description of the connection.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** MatchCriteria **   <a name="Glue-Type-ConnectionInput-MatchCriteria"></a>
A list of criteria that can be used in selecting this connection.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** PhysicalConnectionRequirements **   <a name="Glue-Type-ConnectionInput-PhysicalConnectionRequirements"></a>
The physical connection requirements, such as virtual private cloud (VPC) and `SecurityGroup`, that are needed to successfully make this connection.
Type: [PhysicalConnectionRequirements](API_PhysicalConnectionRequirements.md) object
Required: No

 ** PythonProperties **   <a name="Glue-Type-ConnectionInput-PythonProperties"></a>
Connection properties specific to the Python compute environment.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** SparkProperties **   <a name="Glue-Type-ConnectionInput-SparkProperties"></a>
Connection properties specific to the Spark compute environment.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** ValidateCredentials **   <a name="Glue-Type-ConnectionInput-ValidateCredentials"></a>
A flag to validate the credentials during create connection. Default is true.
Type: Boolean
Required: No

 ** ValidateForComputeEnvironments **   <a name="Glue-Type-ConnectionInput-ValidateForComputeEnvironments"></a>
The compute environments that the specified connection properties are validated against.
Type: Array of strings
Valid Values: `SPARK | ATHENA | PYTHON`
Required: No

## See Also
<a name="API_ConnectionInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ConnectionInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ConnectionInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ConnectionInput)
