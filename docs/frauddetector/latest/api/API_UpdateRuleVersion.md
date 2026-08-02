---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_UpdateRuleVersion.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# UpdateRuleVersion
<a name="API_UpdateRuleVersion"></a>

Updates a rule version resulting in a new rule version. Updates a rule version resulting in a new rule version (version 1, 2, 3 ...).

## Request Syntax
<a name="API_UpdateRuleVersion_RequestSyntax"></a>

```
{
   "description": "{{string}}",
   "expression": "{{string}}",
   "language": "{{string}}",
   "outcomes": [ "{{string}}" ],
   "rule": {
      "detectorId": "{{string}}",
      "ruleId": "{{string}}",
      "ruleVersion": "{{string}}"
   },
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_UpdateRuleVersion_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [description](#API_UpdateRuleVersion_RequestSyntax) **   <a name="FraudDetector-UpdateRuleVersion-request-description"></a>
The description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [expression](#API_UpdateRuleVersion_RequestSyntax) **   <a name="FraudDetector-UpdateRuleVersion-request-expression"></a>
The rule expression.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: Yes

 ** [language](#API_UpdateRuleVersion_RequestSyntax) **   <a name="FraudDetector-UpdateRuleVersion-request-language"></a>
The language.
Type: String
Valid Values: `DETECTORPL`
Required: Yes

 ** [outcomes](#API_UpdateRuleVersion_RequestSyntax) **   <a name="FraudDetector-UpdateRuleVersion-request-outcomes"></a>
The outcomes.
Type: Array of strings
Array Members: Minimum number of 1 item.
Required: Yes

 ** [rule](#API_UpdateRuleVersion_RequestSyntax) **   <a name="FraudDetector-UpdateRuleVersion-request-rule"></a>
The rule to update.
Type: [Rule](API_Rule.md) object
Required: Yes

 ** [tags](#API_UpdateRuleVersion_RequestSyntax) **   <a name="FraudDetector-UpdateRuleVersion-request-tags"></a>
The tags to assign to the rule version.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_UpdateRuleVersion_ResponseSyntax"></a>

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
<a name="API_UpdateRuleVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [rule](#API_UpdateRuleVersion_ResponseSyntax) **   <a name="FraudDetector-UpdateRuleVersion-response-rule"></a>
The new rule version that was created.
Type: [Rule](API_Rule.md) object

## Errors
<a name="API_UpdateRuleVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as `PutExternalModel`, that specifies a role that is not in your account.
HTTP Status Code: 400

 ** ConflictException **
An exception indicating there was a conflict during a delete operation.
HTTP Status Code: 400

 ** InternalServerException **
An exception indicating an internal server error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
An exception indicating the specified resource was not found.
HTTP Status Code: 400

 ** ThrottlingException **
An exception indicating a throttling error.
HTTP Status Code: 400

 ** ValidationException **
An exception indicating a specified value is not allowed.
HTTP Status Code: 400

## See Also
<a name="API_UpdateRuleVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/frauddetector-2019-11-15/UpdateRuleVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/frauddetector-2019-11-15/UpdateRuleVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/UpdateRuleVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/frauddetector-2019-11-15/UpdateRuleVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/UpdateRuleVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/frauddetector-2019-11-15/UpdateRuleVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/frauddetector-2019-11-15/UpdateRuleVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/frauddetector-2019-11-15/UpdateRuleVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/frauddetector-2019-11-15/UpdateRuleVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/UpdateRuleVersion)
