---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_Variable.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# Variable
<a name="API_Variable"></a>

The variable.

## Contents
<a name="API_Variable_Contents"></a>

 ** arn **   <a name="FraudDetector-Type-Variable-arn"></a>
The ARN of the variable.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn\:aws[a-z-]{0,15}\:frauddetector\:[a-z0-9-]{3,20}\:[0-9]{12}\:[^\s]{2,128}$`
Required: No

 ** createdTime **   <a name="FraudDetector-Type-Variable-createdTime"></a>
The time when the variable was created.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 30.
Required: No

 ** dataSource **   <a name="FraudDetector-Type-Variable-dataSource"></a>
The data source of the variable.
Type: String
Valid Values: `EVENT | MODEL_SCORE | EXTERNAL_MODEL_SCORE`
Required: No

 ** dataType **   <a name="FraudDetector-Type-Variable-dataType"></a>
The data type of the variable. For more information see [Variable types](https://docs.aws.amazon.com/frauddetector/latest/ug/create-a-variable.html#variable-types).
Type: String
Valid Values: `STRING | INTEGER | FLOAT | BOOLEAN | DATETIME`
Required: No

 ** defaultValue **   <a name="FraudDetector-Type-Variable-defaultValue"></a>
The default value of the variable.
Type: String
Required: No

 ** description **   <a name="FraudDetector-Type-Variable-description"></a>
The description of the variable.
Type: String
Required: No

 ** lastUpdatedTime **   <a name="FraudDetector-Type-Variable-lastUpdatedTime"></a>
The time when variable was last updated.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 30.
Required: No

 ** name **   <a name="FraudDetector-Type-Variable-name"></a>
The name of the variable.
Type: String
Required: No

 ** variableType **   <a name="FraudDetector-Type-Variable-variableType"></a>
The variable type of the variable.
Valid Values: `AUTH_CODE | AVS | BILLING_ADDRESS_L1 | BILLING_ADDRESS_L2 | BILLING_CITY | BILLING_COUNTRY | BILLING_NAME | BILLING_PHONE | BILLING_STATE | BILLING_ZIP | CARD_BIN | CATEGORICAL | CURRENCY_CODE | EMAIL_ADDRESS | FINGERPRINT | FRAUD_LABEL | FREE_FORM_TEXT | IP_ADDRESS | NUMERIC | ORDER_ID | PAYMENT_TYPE | PHONE_NUMBER | PRICE | PRODUCT_CATEGORY | SHIPPING_ADDRESS_L1 | SHIPPING_ADDRESS_L2 | SHIPPING_CITY | SHIPPING_COUNTRY | SHIPPING_NAME | SHIPPING_PHONE | SHIPPING_STATE | SHIPPING_ZIP | USERAGENT `
Type: String
Required: No

## See Also
<a name="API_Variable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/Variable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/Variable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/Variable)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Fraud Detector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query frauddetector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
