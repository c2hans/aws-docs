---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_VariableEntry.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# VariableEntry
<a name="API_VariableEntry"></a>

A variable in the list of variables for the batch create variable request.

## Contents
<a name="API_VariableEntry_Contents"></a>

 ** dataSource **   <a name="FraudDetector-Type-VariableEntry-dataSource"></a>
The data source of the variable.
Type: String
Required: No

 ** dataType **   <a name="FraudDetector-Type-VariableEntry-dataType"></a>
The data type of the variable.
Type: String
Required: No

 ** defaultValue **   <a name="FraudDetector-Type-VariableEntry-defaultValue"></a>
The default value of the variable.
Type: String
Required: No

 ** description **   <a name="FraudDetector-Type-VariableEntry-description"></a>
The description of the variable.
Type: String
Required: No

 ** name **   <a name="FraudDetector-Type-VariableEntry-name"></a>
The name of the variable.
Type: String
Required: No

 ** variableType **   <a name="FraudDetector-Type-VariableEntry-variableType"></a>
The type of the variable. For more information see [Variable types](https://docs.aws.amazon.com/frauddetector/latest/ug/create-a-variable.html#variable-types).
Valid Values: `AUTH_CODE | AVS | BILLING_ADDRESS_L1 | BILLING_ADDRESS_L2 | BILLING_CITY | BILLING_COUNTRY | BILLING_NAME | BILLING_PHONE | BILLING_STATE | BILLING_ZIP | CARD_BIN | CATEGORICAL | CURRENCY_CODE | EMAIL_ADDRESS | FINGERPRINT | FRAUD_LABEL | FREE_FORM_TEXT | IP_ADDRESS | NUMERIC | ORDER_ID | PAYMENT_TYPE | PHONE_NUMBER | PRICE | PRODUCT_CATEGORY | SHIPPING_ADDRESS_L1 | SHIPPING_ADDRESS_L2 | SHIPPING_CITY | SHIPPING_COUNTRY | SHIPPING_NAME | SHIPPING_PHONE | SHIPPING_STATE | SHIPPING_ZIP | USERAGENT `
Type: String
Required: No

## See Also
<a name="API_VariableEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/VariableEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/VariableEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/VariableEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Fraud Detector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query frauddetector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
