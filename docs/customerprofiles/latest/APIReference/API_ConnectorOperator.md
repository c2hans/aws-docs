---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ConnectorOperator.html
---

# ConnectorOperator
<a name="API_connect-customer-profiles_ConnectorOperator"></a>

The operation to be performed on the provided source fields.

## Contents
<a name="API_connect-customer-profiles_ConnectorOperator_Contents"></a>

 ** Marketo **   <a name="connect-Type-connect-customer-profiles_ConnectorOperator-Marketo"></a>
The operation to be performed on the provided Marketo source fields.
Type: String
Valid Values: `PROJECTION | LESS_THAN | GREATER_THAN | BETWEEN | ADDITION | MULTIPLICATION | DIVISION | SUBTRACTION | MASK_ALL | MASK_FIRST_N | MASK_LAST_N | VALIDATE_NON_NULL | VALIDATE_NON_ZERO | VALIDATE_NON_NEGATIVE | VALIDATE_NUMERIC | NO_OP`
Required: No

 ** S3 **   <a name="connect-Type-connect-customer-profiles_ConnectorOperator-S3"></a>
The operation to be performed on the provided Amazon S3 source fields.
Type: String
Valid Values: `PROJECTION | LESS_THAN | GREATER_THAN | BETWEEN | LESS_THAN_OR_EQUAL_TO | GREATER_THAN_OR_EQUAL_TO | EQUAL_TO | NOT_EQUAL_TO | ADDITION | MULTIPLICATION | DIVISION | SUBTRACTION | MASK_ALL | MASK_FIRST_N | MASK_LAST_N | VALIDATE_NON_NULL | VALIDATE_NON_ZERO | VALIDATE_NON_NEGATIVE | VALIDATE_NUMERIC | NO_OP`
Required: No

 ** Salesforce **   <a name="connect-Type-connect-customer-profiles_ConnectorOperator-Salesforce"></a>
The operation to be performed on the provided Salesforce source fields.
Type: String
Valid Values: `PROJECTION | LESS_THAN | CONTAINS | GREATER_THAN | BETWEEN | LESS_THAN_OR_EQUAL_TO | GREATER_THAN_OR_EQUAL_TO | EQUAL_TO | NOT_EQUAL_TO | ADDITION | MULTIPLICATION | DIVISION | SUBTRACTION | MASK_ALL | MASK_FIRST_N | MASK_LAST_N | VALIDATE_NON_NULL | VALIDATE_NON_ZERO | VALIDATE_NON_NEGATIVE | VALIDATE_NUMERIC | NO_OP`
Required: No

 ** ServiceNow **   <a name="connect-Type-connect-customer-profiles_ConnectorOperator-ServiceNow"></a>
The operation to be performed on the provided ServiceNow source fields.
Type: String
Valid Values: `PROJECTION | CONTAINS | LESS_THAN | GREATER_THAN | BETWEEN | LESS_THAN_OR_EQUAL_TO | GREATER_THAN_OR_EQUAL_TO | EQUAL_TO | NOT_EQUAL_TO | ADDITION | MULTIPLICATION | DIVISION | SUBTRACTION | MASK_ALL | MASK_FIRST_N | MASK_LAST_N | VALIDATE_NON_NULL | VALIDATE_NON_ZERO | VALIDATE_NON_NEGATIVE | VALIDATE_NUMERIC | NO_OP`
Required: No

 ** Zendesk **   <a name="connect-Type-connect-customer-profiles_ConnectorOperator-Zendesk"></a>
The operation to be performed on the provided Zendesk source fields.
Type: String
Valid Values: `PROJECTION | GREATER_THAN | ADDITION | MULTIPLICATION | DIVISION | SUBTRACTION | MASK_ALL | MASK_FIRST_N | MASK_LAST_N | VALIDATE_NON_NULL | VALIDATE_NON_ZERO | VALIDATE_NON_NEGATIVE | VALIDATE_NUMERIC | NO_OP`
Required: No

## See Also
<a name="API_connect-customer-profiles_ConnectorOperator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/ConnectorOperator)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/ConnectorOperator)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/ConnectorOperator)
