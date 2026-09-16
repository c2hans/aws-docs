---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_CreateRule.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# CreateRule
<a name="API_CreateRule"></a>

Creates a rule for use with the specified detector.

## Request Syntax
<a name="API_CreateRule_RequestSyntax"></a>

```
{
   "description": "{{string}}",
   "detectorId": "{{string}}",
   "expression": "{{string}}",
   "language": "{{string}}",
   "outcomes": [ "{{string}}" ],
   "ruleId": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateRule_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [description](#API_CreateRule_RequestSyntax) **   <a name="FraudDetector-CreateRule-request-description"></a>
The rule description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [detectorId](#API_CreateRule_RequestSyntax) **   <a name="FraudDetector-CreateRule-request-detectorId"></a>
The detector ID for the rule's parent detector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_-]+$`
Required: Yes

 ** [expression](#API_CreateRule_RequestSyntax) **   <a name="FraudDetector-CreateRule-request-expression"></a>
The rule expression.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: Yes

 ** [language](#API_CreateRule_RequestSyntax) **   <a name="FraudDetector-CreateRule-request-language"></a>
The language of the rule.
Type: String
Valid Values: `DETECTORPL`
Required: Yes

 ** [outcomes](#API_CreateRule_RequestSyntax) **   <a name="FraudDetector-CreateRule-request-outcomes"></a>
The outcome or outcomes returned when the rule expression matches.
Type: Array of strings
Array Members: Minimum number of 1 item.
Required: Yes

 ** [ruleId](#API_CreateRule_RequestSyntax) **   <a name="FraudDetector-CreateRule-request-ruleId"></a>
The rule ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_-]+$`
Required: Yes

 ** [tags](#API_CreateRule_RequestSyntax) **   <a name="FraudDetector-CreateRule-request-tags"></a>
A collection of key and value pairs.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreateRule_ResponseSyntax"></a>

```
{
   "rule": {
      "detectorId": "string",
      "ruleId": "string",
      "ruleVersion": "string"
   }
}
```

## Response Elements
<a name="API_CreateRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [rule](#API_CreateRule_ResponseSyntax) **   <a name="FraudDetector-CreateRule-response-rule"></a>
The created rule.
Type: [Rule](API_Rule.md) object

## Errors
<a name="API_CreateRule_Errors"></a>

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
<a name="API_CreateRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/frauddetector-2019-11-15/CreateRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/frauddetector-2019-11-15/CreateRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/CreateRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/frauddetector-2019-11-15/CreateRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/CreateRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/frauddetector-2019-11-15/CreateRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/frauddetector-2019-11-15/CreateRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/frauddetector-2019-11-15/CreateRule)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/frauddetector-2019-11-15/CreateRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/CreateRule)
