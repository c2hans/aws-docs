---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_ConnectorOperator.html
---

# ConnectorOperator
<a name="API_ConnectorOperator"></a>

 The operation to be performed on the provided source fields.

## Contents
<a name="API_ConnectorOperator_Contents"></a>

 ** Amplitude **   <a name="appflow-Type-ConnectorOperator-Amplitude"></a>
 The operation to be performed on the provided Amplitude source fields.
Type: String
Valid Values: `BETWEEN`
Required: No

 ** CustomConnector **   <a name="appflow-Type-ConnectorOperator-CustomConnector"></a>
Operators supported by the custom connector.
Type: String
Valid Values: `PROJECTION | LESS_THAN | GREATER_THAN | CONTAINS | BETWEEN | LESS_THAN_OR_EQUAL_TO | GREATER_THAN_OR_EQUAL_TO | EQUAL_TO | NOT_EQUAL_TO | ADDITION | MULTIPLICATION | DIVISION | SUBTRACTION | MASK_ALL | MASK_FIRST_N | MASK_LAST_N | VALIDATE_NON_NULL | VALIDATE_NON_ZERO | VALIDATE_NON_NEGATIVE | VALIDATE_NUMERIC | NO_OP`
Required: No

 ** Datadog **   <a name="appflow-Type-ConnectorOperator-Datadog"></a>
 The operation to be performed on the provided Datadog source fields.
Type: String
Valid Values: `PROJECTION | BETWEEN | EQUAL_TO | ADDITION | MULTIPLICATION | DIVISION | SUBTRACTION | MASK_ALL | MASK_FIRST_N | MASK_LAST_N | VALIDATE_NON_NULL | VALIDATE_NON_ZERO | VALIDATE_NON_NEGATIVE | VALIDATE_NUMERIC | NO_OP`
Required: No

 ** Dynatrace **   <a name="appflow-Type-ConnectorOperator-Dynatrace"></a>
 The operation to be performed on the provided Dynatrace source fields.
Type: String
Valid Values: `PROJECTION | BETWEEN | EQUAL_TO | ADDITION | MULTIPLICATION | DIVISION | SUBTRACTION | MASK_ALL | MASK_FIRST_N | MASK_LAST_N | VALIDATE_NON_NULL | VALIDATE_NON_ZERO | VALIDATE_NON_NEGATIVE | VALIDATE_NUMERIC | NO_OP`
Required: No

 ** GoogleAnalytics **   <a name="appflow-Type-ConnectorOperator-GoogleAnalytics"></a>
 The operation to be performed on the provided Google Analytics source fields.
Type: String
Valid Values: `PROJECTION | BETWEEN`
Required: No

 ** InforNexus **   <a name="appflow-Type-ConnectorOperator-InforNexus"></a>
 The operation to be performed on the provided Infor Nexus source fields.
Type: String
Valid Values: `PROJECTION | BETWEEN | EQUAL_TO | ADDITION | MULTIPLICATION | DIVISION | SUBTRACTION | MASK_ALL | MASK_FIRST_N | MASK_LAST_N | VALIDATE_NON_NULL | VALIDATE_NON_ZERO | VALIDATE_NON_NEGATIVE | VALIDATE_NUMERIC | NO_OP`
Required: No

 ** Marketo **   <a name="appflow-Type-ConnectorOperator-Marketo"></a>
 The operation to be performed on the provided Marketo source fields.
Type: String
Valid Values: `PROJECTION | LESS_THAN | GREATER_THAN | BETWEEN | ADDITION | MULTIPLICATION | DIVISION | SUBTRACTION | MASK_ALL | MASK_FIRST_N | MASK_LAST_N | VALIDATE_NON_NULL | VALIDATE_NON_ZERO | VALIDATE_NON_NEGATIVE | VALIDATE_NUMERIC | NO_OP`
Required: No

 ** Pardot **   <a name="appflow-Type-ConnectorOperator-Pardot"></a>
The operation to be performed on the provided Salesforce Pardot source fields.
Type: String
Valid Values: `PROJECTION | EQUAL_TO | NO_OP | ADDITION | MULTIPLICATION | DIVISION | SUBTRACTION | MASK_ALL | MASK_FIRST_N | MASK_LAST_N | VALIDATE_NON_NULL | VALIDATE_NON_ZERO | VALIDATE_NON_NEGATIVE | VALIDATE_NUMERIC`
Required: No

 ** S3 **   <a name="appflow-Type-ConnectorOperator-S3"></a>
 The operation to be performed on the provided Amazon S3 source fields.
Type: String
Valid Values: `PROJECTION | LESS_THAN | GREATER_THAN | BETWEEN | LESS_THAN_OR_EQUAL_TO | GREATER_THAN_OR_EQUAL_TO | EQUAL_TO | NOT_EQUAL_TO | ADDITION | MULTIPLICATION | DIVISION | SUBTRACTION | MASK_ALL | MASK_FIRST_N | MASK_LAST_N | VALIDATE_NON_NULL | VALIDATE_NON_ZERO | VALIDATE_NON_NEGATIVE | VALIDATE_NUMERIC | NO_OP`
Required: No

 ** Salesforce **   <a name="appflow-Type-ConnectorOperator-Salesforce"></a>
 The operation to be performed on the provided Salesforce source fields.
Type: String
Valid Values: `PROJECTION | LESS_THAN | CONTAINS | GREATER_THAN | BETWEEN | LESS_THAN_OR_EQUAL_TO | GREATER_THAN_OR_EQUAL_TO | EQUAL_TO | NOT_EQUAL_TO | ADDITION | MULTIPLICATION | DIVISION | SUBTRACTION | MASK_ALL | MASK_FIRST_N | MASK_LAST_N | VALIDATE_NON_NULL | VALIDATE_NON_ZERO | VALIDATE_NON_NEGATIVE | VALIDATE_NUMERIC | NO_OP`
Required: No

 ** SAPOData **   <a name="appflow-Type-ConnectorOperator-SAPOData"></a>
 The operation to be performed on the provided SAPOData source fields.
Type: String
Valid Values: `PROJECTION | LESS_THAN | CONTAINS | GREATER_THAN | BETWEEN | LESS_THAN_OR_EQUAL_TO | GREATER_THAN_OR_EQUAL_TO | EQUAL_TO | NOT_EQUAL_TO | ADDITION | MULTIPLICATION | DIVISION | SUBTRACTION | MASK_ALL | MASK_FIRST_N | MASK_LAST_N | VALIDATE_NON_NULL | VALIDATE_NON_ZERO | VALIDATE_NON_NEGATIVE | VALIDATE_NUMERIC | NO_OP`
Required: No

 ** ServiceNow **   <a name="appflow-Type-ConnectorOperator-ServiceNow"></a>
 The operation to be performed on the provided ServiceNow source fields.
Type: String
Valid Values: `PROJECTION | CONTAINS | LESS_THAN | GREATER_THAN | BETWEEN | LESS_THAN_OR_EQUAL_TO | GREATER_THAN_OR_EQUAL_TO | EQUAL_TO | NOT_EQUAL_TO | ADDITION | MULTIPLICATION | DIVISION | SUBTRACTION | MASK_ALL | MASK_FIRST_N | MASK_LAST_N | VALIDATE_NON_NULL | VALIDATE_NON_ZERO | VALIDATE_NON_NEGATIVE | VALIDATE_NUMERIC | NO_OP`
Required: No

 ** Singular **   <a name="appflow-Type-ConnectorOperator-Singular"></a>
 The operation to be performed on the provided Singular source fields.
Type: String
Valid Values: `PROJECTION | EQUAL_TO | ADDITION | MULTIPLICATION | DIVISION | SUBTRACTION | MASK_ALL | MASK_FIRST_N | MASK_LAST_N | VALIDATE_NON_NULL | VALIDATE_NON_ZERO | VALIDATE_NON_NEGATIVE | VALIDATE_NUMERIC | NO_OP`
Required: No

 ** Slack **   <a name="appflow-Type-ConnectorOperator-Slack"></a>
 The operation to be performed on the provided Slack source fields.
Type: String
Valid Values: `PROJECTION | LESS_THAN | GREATER_THAN | BETWEEN | LESS_THAN_OR_EQUAL_TO | GREATER_THAN_OR_EQUAL_TO | EQUAL_TO | ADDITION | MULTIPLICATION | DIVISION | SUBTRACTION | MASK_ALL | MASK_FIRST_N | MASK_LAST_N | VALIDATE_NON_NULL | VALIDATE_NON_ZERO | VALIDATE_NON_NEGATIVE | VALIDATE_NUMERIC | NO_OP`
Required: No

 ** Trendmicro **   <a name="appflow-Type-ConnectorOperator-Trendmicro"></a>
 The operation to be performed on the provided Trend Micro source fields.
Type: String
Valid Values: `PROJECTION | EQUAL_TO | ADDITION | MULTIPLICATION | DIVISION | SUBTRACTION | MASK_ALL | MASK_FIRST_N | MASK_LAST_N | VALIDATE_NON_NULL | VALIDATE_NON_ZERO | VALIDATE_NON_NEGATIVE | VALIDATE_NUMERIC | NO_OP`
Required: No

 ** Veeva **   <a name="appflow-Type-ConnectorOperator-Veeva"></a>
 The operation to be performed on the provided Veeva source fields.
Type: String
Valid Values: `PROJECTION | LESS_THAN | GREATER_THAN | CONTAINS | BETWEEN | LESS_THAN_OR_EQUAL_TO | GREATER_THAN_OR_EQUAL_TO | EQUAL_TO | NOT_EQUAL_TO | ADDITION | MULTIPLICATION | DIVISION | SUBTRACTION | MASK_ALL | MASK_FIRST_N | MASK_LAST_N | VALIDATE_NON_NULL | VALIDATE_NON_ZERO | VALIDATE_NON_NEGATIVE | VALIDATE_NUMERIC | NO_OP`
Required: No

 ** Zendesk **   <a name="appflow-Type-ConnectorOperator-Zendesk"></a>
 The operation to be performed on the provided Zendesk source fields.
Type: String
Valid Values: `PROJECTION | GREATER_THAN | ADDITION | MULTIPLICATION | DIVISION | SUBTRACTION | MASK_ALL | MASK_FIRST_N | MASK_LAST_N | VALIDATE_NON_NULL | VALIDATE_NON_ZERO | VALIDATE_NON_NEGATIVE | VALIDATE_NUMERIC | NO_OP`
Required: No

## See Also
<a name="API_ConnectorOperator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/ConnectorOperator)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/ConnectorOperator)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/ConnectorOperator)
