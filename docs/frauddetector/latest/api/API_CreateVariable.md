---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_CreateVariable.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# CreateVariable
<a name="API_CreateVariable"></a>

Creates a variable.

## Request Syntax
<a name="API_CreateVariable_RequestSyntax"></a>

```
{
   "dataSource": "{{string}}",
   "dataType": "{{string}}",
   "defaultValue": "{{string}}",
   "description": "{{string}}",
   "name": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "variableType": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateVariable_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [dataSource](#API_CreateVariable_RequestSyntax) **   <a name="FraudDetector-CreateVariable-request-dataSource"></a>
The source of the data.
Type: String
Valid Values: `EVENT | MODEL_SCORE | EXTERNAL_MODEL_SCORE`
Required: Yes

 ** [dataType](#API_CreateVariable_RequestSyntax) **   <a name="FraudDetector-CreateVariable-request-dataType"></a>
The data type of the variable.
Type: String
Valid Values: `STRING | INTEGER | FLOAT | BOOLEAN | DATETIME`
Required: Yes

 ** [defaultValue](#API_CreateVariable_RequestSyntax) **   <a name="FraudDetector-CreateVariable-request-defaultValue"></a>
The default value for the variable when no value is received.
Type: String
Required: Yes

 ** [description](#API_CreateVariable_RequestSyntax) **   <a name="FraudDetector-CreateVariable-request-description"></a>
The description.
Type: String
Required: No

 ** [name](#API_CreateVariable_RequestSyntax) **   <a name="FraudDetector-CreateVariable-request-name"></a>
The name of the variable.
Type: String
Required: Yes

 ** [tags](#API_CreateVariable_RequestSyntax) **   <a name="FraudDetector-CreateVariable-request-tags"></a>
A collection of key and value pairs.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** [variableType](#API_CreateVariable_RequestSyntax) **   <a name="FraudDetector-CreateVariable-request-variableType"></a>
The variable type. For more information see [Variable types](https://docs.aws.amazon.com/frauddetector/latest/ug/create-a-variable.html#variable-types).
Valid Values: `AUTH_CODE | AVS | BILLING_ADDRESS_L1 | BILLING_ADDRESS_L2 | BILLING_CITY | BILLING_COUNTRY | BILLING_NAME | BILLING_PHONE | BILLING_STATE | BILLING_ZIP | CARD_BIN | CATEGORICAL | CURRENCY_CODE | EMAIL_ADDRESS | FINGERPRINT | FRAUD_LABEL | FREE_FORM_TEXT | IP_ADDRESS | NUMERIC | ORDER_ID | PAYMENT_TYPE | PHONE_NUMBER | PRICE | PRODUCT_CATEGORY | SHIPPING_ADDRESS_L1 | SHIPPING_ADDRESS_L2 | SHIPPING_CITY | SHIPPING_COUNTRY | SHIPPING_NAME | SHIPPING_PHONE | SHIPPING_STATE | SHIPPING_ZIP | USERAGENT`
Type: String
Required: No

## Response Elements
<a name="API_CreateVariable_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CreateVariable_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as `PutExternalModel`, that specifies a role that is not in your account.
HTTP Status Code: 400

 ** InternalServerException **
An exception indicating an internal server error.
HTTP Status Code: 500

 ** ThrottlingException **
An exception indicating a throttling error.
HTTP Status Code: 400

 ** ValidationException **
An exception indicating a specified value is not allowed.
HTTP Status Code: 400

## See Also
<a name="API_CreateVariable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/frauddetector-2019-11-15/CreateVariable)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/frauddetector-2019-11-15/CreateVariable)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/CreateVariable)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/frauddetector-2019-11-15/CreateVariable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/CreateVariable)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/frauddetector-2019-11-15/CreateVariable)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/frauddetector-2019-11-15/CreateVariable)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/frauddetector-2019-11-15/CreateVariable)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/frauddetector-2019-11-15/CreateVariable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/CreateVariable)
