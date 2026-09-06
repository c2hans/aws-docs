---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ConnectionTypeBrief.html
---

# ConnectionTypeBrief
<a name="API_ConnectionTypeBrief"></a>

Brief information about a supported connection type returned by the `ListConnectionTypes` API.

## Contents
<a name="API_ConnectionTypeBrief_Contents"></a>

 ** Capabilities **   <a name="Glue-Type-ConnectionTypeBrief-Capabilities"></a>
The supported authentication types, data interface types (compute environments), and data operations of the connector.
Type: [Capabilities](API_Capabilities.md) object
Required: No

 ** Categories **   <a name="Glue-Type-ConnectionTypeBrief-Categories"></a>
A list of categories that this connection type belongs to. Categories help users filter and find appropriate connection types based on their use cases.
Type: Array of strings
Required: No

 ** ConnectionType **   <a name="Glue-Type-ConnectionTypeBrief-ConnectionType"></a>
The name of the connection type.
Type: String
Valid Values: `JDBC | SFTP | MONGODB | KAFKA | NETWORK | MARKETPLACE | CUSTOM | SALESFORCE | VIEW_VALIDATION_REDSHIFT | VIEW_VALIDATION_ATHENA | GOOGLEADS | GOOGLESHEETS | GOOGLEANALYTICS4 | SERVICENOW | MARKETO | SAPODATA | ZENDESK | JIRACLOUD | NETSUITEERP | HUBSPOT | FACEBOOKADS | INSTAGRAMADS | ZOHOCRM | SALESFORCEPARDOT | SALESFORCEMARKETINGCLOUD | ADOBEANALYTICS | SLACK | LINKEDIN | MIXPANEL | ASANA | STRIPE | SMARTSHEET | DATADOG | WOOCOMMERCE | INTERCOM | SNAPCHATADS | PAYPAL | QUICKBOOKS | FACEBOOKPAGEINSIGHTS | FRESHDESK | TWILIO | DOCUSIGNMONITOR | FRESHSALES | ZOOM | GOOGLESEARCHCONSOLE | SALESFORCECOMMERCECLOUD | SAPCONCUR | DYNATRACE | MICROSOFTDYNAMIC365FINANCEANDOPS | MICROSOFTTEAMS | BLACKBAUDRAISEREDGENXT | MAILCHIMP | GITLAB | PENDO | PRODUCTBOARD | CIRCLECI | PIPEDIVE | SENDGRID | AZURECOSMOS | AZURESQL | BIGQUERY | BLACKBAUD | CLOUDERAHIVE | CLOUDERAIMPALA | CLOUDWATCH | CLOUDWATCHMETRICS | CMDB | DATALAKEGEN2 | DB2 | DB2AS400 | DOCUMENTDB | DOMO | DYNAMODB | GOOGLECLOUDSTORAGE | HBASE | KUSTOMER | MICROSOFTDYNAMICS365CRM | MONDAY | MYSQL | OKTA | OPENSEARCH | ORACLE | PIPEDRIVE | POSTGRESQL | SAPHANA | SQLSERVER | SYNAPSE | TERADATA | TERADATANOS | TIMESTREAM | TPCDS | VERTICA`
Required: No

 ** ConnectionTypeVariants **   <a name="Glue-Type-ConnectionTypeBrief-ConnectionTypeVariants"></a>
A list of variants available for this connection type. Different variants may provide specialized configurations for specific use cases or implementations of the same general connection type.
Type: Array of [ConnectionTypeVariant](API_ConnectionTypeVariant.md) objects
Required: No

 ** Description **   <a name="Glue-Type-ConnectionTypeBrief-Description"></a>
A description of the connection type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** DisplayName **   <a name="Glue-Type-ConnectionTypeBrief-DisplayName"></a>
The human-readable name for the connection type that is displayed in the AWS Glue console.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** LogoUrl **   <a name="Glue-Type-ConnectionTypeBrief-LogoUrl"></a>
The URL of the logo associated with a connection type.
Type: String
Required: No

 ** Vendor **   <a name="Glue-Type-ConnectionTypeBrief-Vendor"></a>
The name of the vendor or provider that created or maintains this connection type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_ConnectionTypeBrief_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ConnectionTypeBrief)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ConnectionTypeBrief)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ConnectionTypeBrief)
