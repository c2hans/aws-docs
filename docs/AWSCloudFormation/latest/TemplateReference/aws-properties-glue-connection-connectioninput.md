---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-connection-connectioninput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Connection ConnectionInput
<a name="aws-properties-glue-connection-connectioninput"></a>

A structure that is used to specify a connection to create or update.

## Syntax
<a name="aws-properties-glue-connection-connectioninput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-connection-connectioninput-syntax.json"></a>

```
{
  "[AthenaProperties](#cfn-glue-connection-connectioninput-athenaproperties)" : {{Json}},
  "[AuthenticationConfiguration](#cfn-glue-connection-connectioninput-authenticationconfiguration)" : {{AuthenticationConfigurationInput}},
  "[ConnectionProperties](#cfn-glue-connection-connectioninput-connectionproperties)" : {{Json}},
  "[ConnectionType](#cfn-glue-connection-connectioninput-connectiontype)" : {{String}},
  "[Description](#cfn-glue-connection-connectioninput-description)" : {{String}},
  "[MatchCriteria](#cfn-glue-connection-connectioninput-matchcriteria)" : {{[ String, ... ]}},
  "[Name](#cfn-glue-connection-connectioninput-name)" : {{String}},
  "[PhysicalConnectionRequirements](#cfn-glue-connection-connectioninput-physicalconnectionrequirements)" : {{PhysicalConnectionRequirements}},
  "[PythonProperties](#cfn-glue-connection-connectioninput-pythonproperties)" : {{Json}},
  "[SparkProperties](#cfn-glue-connection-connectioninput-sparkproperties)" : {{Json}},
  "[ValidateCredentials](#cfn-glue-connection-connectioninput-validatecredentials)" : {{Boolean}},
  "[ValidateForComputeEnvironments](#cfn-glue-connection-connectioninput-validateforcomputeenvironments)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-glue-connection-connectioninput-syntax.yaml"></a>

```
  [AthenaProperties](#cfn-glue-connection-connectioninput-athenaproperties): {{Json}}
  [AuthenticationConfiguration](#cfn-glue-connection-connectioninput-authenticationconfiguration): {{
    AuthenticationConfigurationInput}}
  [ConnectionProperties](#cfn-glue-connection-connectioninput-connectionproperties): {{Json}}
  [ConnectionType](#cfn-glue-connection-connectioninput-connectiontype): {{String}}
  [Description](#cfn-glue-connection-connectioninput-description): {{String}}
  [MatchCriteria](#cfn-glue-connection-connectioninput-matchcriteria): {{
    - String}}
  [Name](#cfn-glue-connection-connectioninput-name): {{String}}
  [PhysicalConnectionRequirements](#cfn-glue-connection-connectioninput-physicalconnectionrequirements): {{
    PhysicalConnectionRequirements}}
  [PythonProperties](#cfn-glue-connection-connectioninput-pythonproperties): {{Json}}
  [SparkProperties](#cfn-glue-connection-connectioninput-sparkproperties): {{Json}}
  [ValidateCredentials](#cfn-glue-connection-connectioninput-validatecredentials): {{Boolean}}
  [ValidateForComputeEnvironments](#cfn-glue-connection-connectioninput-validateforcomputeenvironments): {{
    - String}}
```

## Properties
<a name="aws-properties-glue-connection-connectioninput-properties"></a>

`AthenaProperties`  <a name="cfn-glue-connection-connectioninput-athenaproperties"></a>
Connection properties specific to the Athena compute environment.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AuthenticationConfiguration`  <a name="cfn-glue-connection-connectioninput-authenticationconfiguration"></a>
The authentication properties of the connection.
*Required*: No
*Type*: [AuthenticationConfigurationInput](aws-properties-glue-connection-authenticationconfigurationinput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConnectionProperties`  <a name="cfn-glue-connection-connectioninput-connectionproperties"></a>
These key-value pairs define parameters for the connection.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConnectionType`  <a name="cfn-glue-connection-connectioninput-connectiontype"></a>
The type of the connection. Currently, these types are supported:
+ `JDBC` - Designates a connection to a database through Java Database Connectivity (JDBC).

  `JDBC` Connections use the following ConnectionParameters.
  + Required: All of (`HOST`, `PORT`, `JDBC_ENGINE`) or `JDBC_CONNECTION_URL`.
  + Required: All of (`USERNAME`, `PASSWORD`) or `SECRET_ID`.
  + Optional: `JDBC_ENFORCE_SSL`, `CUSTOM_JDBC_CERT`, `CUSTOM_JDBC_CERT_STRING`, `SKIP_CUSTOM_JDBC_CERT_VALIDATION`. These parameters are used to configure SSL with JDBC.
+ `KAFKA` - Designates a connection to an Apache Kafka streaming platform.

  `KAFKA` Connections use the following ConnectionParameters.
  + Required: `KAFKA_BOOTSTRAP_SERVERS`.
  + Optional: `KAFKA_SSL_ENABLED`, `KAFKA_CUSTOM_CERT`, `KAFKA_SKIP_CUSTOM_CERT_VALIDATION`. These parameters are used to configure SSL with `KAFKA`.
  + Optional: `KAFKA_CLIENT_KEYSTORE`, `KAFKA_CLIENT_KEYSTORE_PASSWORD`, `KAFKA_CLIENT_KEY_PASSWORD`, `ENCRYPTED_KAFKA_CLIENT_KEYSTORE_PASSWORD`, `ENCRYPTED_KAFKA_CLIENT_KEY_PASSWORD`. These parameters are used to configure TLS client configuration with SSL in `KAFKA`.
  + Optional: `KAFKA_SASL_MECHANISM`. Can be specified as `SCRAM-SHA-512`, `GSSAPI`, or `AWS_MSK_IAM`.
  + Optional: `KAFKA_SASL_SCRAM_USERNAME`, `KAFKA_SASL_SCRAM_PASSWORD`, `ENCRYPTED_KAFKA_SASL_SCRAM_PASSWORD`. These parameters are used to configure SASL/SCRAM-SHA-512 authentication with `KAFKA`.
  + Optional: `KAFKA_SASL_GSSAPI_KEYTAB`, `KAFKA_SASL_GSSAPI_KRB5_CONF`, `KAFKA_SASL_GSSAPI_SERVICE`, `KAFKA_SASL_GSSAPI_PRINCIPAL`. These parameters are used to configure SASL/GSSAPI authentication with `KAFKA`.
+ `MONGODB` - Designates a connection to a MongoDB document database.

  `MONGODB` Connections use the following ConnectionParameters.
  + Required: `CONNECTION_URL`.
  + Required: All of (`USERNAME`, `PASSWORD`) or `SECRET_ID`.
+ `VIEW_VALIDATION_REDSHIFT` - Designates a connection used for view validation by Amazon Redshift.
+ `VIEW_VALIDATION_ATHENA` - Designates a connection used for view validation by Amazon Athena.
+ `NETWORK` - Designates a network connection to a data source within an Amazon Virtual Private Cloud environment (Amazon VPC).

  `NETWORK` Connections do not require ConnectionParameters. Instead, provide a PhysicalConnectionRequirements.
+ `MARKETPLACE` - Uses configuration settings contained in a connector purchased from AWS Marketplace to read from and write to data stores that are not natively supported by AWS Glue.

  `MARKETPLACE` Connections use the following ConnectionParameters.
  + Required: `CONNECTOR_TYPE`, `CONNECTOR_URL`, `CONNECTOR_CLASS_NAME`, `CONNECTION_URL`.
  + Required for `JDBC``CONNECTOR_TYPE` connections: All of (`USERNAME`, `PASSWORD`) or `SECRET_ID`.
+ `CUSTOM` - Uses configuration settings contained in a custom connector to read from and write to data stores that are not natively supported by AWS Glue.
For more information on the connection parameters needed for a particular connector, see the documentation for the connector in [Adding an AWS Glue connection](https://docs.aws.amazon.com/glue/latest/dg/console-connections.html)in the AWS Glue User Guide.
`SFTP` is not supported.
For more information about how optional ConnectionProperties are used to configure features in AWS Glue, consult [AWS Glue connection properties](https://docs.aws.amazon.com/glue/latest/dg/connection-defining.html).
For more information about how optional ConnectionProperties are used to configure features in AWS Glue Studio, consult [Using connectors and connections](https://docs.aws.amazon.com/glue/latest/ug/connectors-chapter.html).
*Required*: Yes
*Type*: String
*Allowed values*: `JDBC | SFTP | MONGODB | KAFKA | NETWORK | MARKETPLACE | CUSTOM | SALESFORCE | VIEW_VALIDATION_REDSHIFT | VIEW_VALIDATION_ATHENA | GOOGLEADS | GOOGLESHEETS | GOOGLEANALYTICS4 | SERVICENOW | MARKETO | SAPODATA | ZENDESK | JIRACLOUD | NETSUITEERP | HUBSPOT | FACEBOOKADS | INSTAGRAMADS | ZOHOCRM | SALESFORCEPARDOT | SALESFORCEMARKETINGCLOUD | ADOBEANALYTICS | SLACK | LINKEDIN | MIXPANEL | ASANA | STRIPE | SMARTSHEET | DATADOG | WOOCOMMERCE | INTERCOM | SNAPCHATADS | PAYPAL | QUICKBOOKS | FACEBOOKPAGEINSIGHTS | FRESHDESK | TWILIO | DOCUSIGNMONITOR | FRESHSALES | ZOOM | GOOGLESEARCHCONSOLE | SALESFORCECOMMERCECLOUD | SAPCONCUR | DYNATRACE | MICROSOFTDYNAMIC365FINANCEANDOPS | MICROSOFTTEAMS | BLACKBAUDRAISEREDGENXT | MAILCHIMP | GITLAB | PENDO | PRODUCTBOARD | CIRCLECI | PIPEDIVE | SENDGRID | AZURECOSMOS | AZURESQL | BIGQUERY | BLACKBAUD | CLOUDERAHIVE | CLOUDERAIMPALA | CLOUDWATCH | CLOUDWATCHMETRICS | CMDB | DATALAKEGEN2 | DB2 | DB2AS400 | DOCUMENTDB | DOMO | DYNAMODB | GOOGLECLOUDSTORAGE | HBASE | KUSTOMER | MICROSOFTDYNAMICS365CRM | MONDAY | MYSQL | OKTA | OPENSEARCH | ORACLE | PIPEDRIVE | POSTGRESQL | SAPHANA | SQLSERVER | SYNAPSE | TERADATA | TERADATANOS | TIMESTREAM | TPCDS | VERTICA`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-glue-connection-connectioninput-description"></a>
The description of the connection.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MatchCriteria`  <a name="cfn-glue-connection-connectioninput-matchcriteria"></a>
A list of criteria that can be used in selecting this connection.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-glue-connection-connectioninput-name"></a>
The name of the connection.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PhysicalConnectionRequirements`  <a name="cfn-glue-connection-connectioninput-physicalconnectionrequirements"></a>
The physical connection requirements, such as virtual private cloud (VPC) and `SecurityGroup`, that are needed to successfully make this connection.
*Required*: No
*Type*: [PhysicalConnectionRequirements](aws-properties-glue-connection-physicalconnectionrequirements.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PythonProperties`  <a name="cfn-glue-connection-connectioninput-pythonproperties"></a>
Connection properties specific to the Python compute environment.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SparkProperties`  <a name="cfn-glue-connection-connectioninput-sparkproperties"></a>
Connection properties specific to the Spark compute environment.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ValidateCredentials`  <a name="cfn-glue-connection-connectioninput-validatecredentials"></a>
A flag to validate the credentials during create connection. Default is true.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ValidateForComputeEnvironments`  <a name="cfn-glue-connection-connectioninput-validateforcomputeenvironments"></a>
The compute environments that the specified connection properties are validated against.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
