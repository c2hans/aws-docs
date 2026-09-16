---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_UpdateDetectorVersion.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# UpdateDetectorVersion
<a name="API_UpdateDetectorVersion"></a>

 Updates a detector version. The detector version attributes that you can update include models, external model endpoints, rules, rule execution mode, and description. You can only update a `DRAFT` detector version.

## Request Syntax
<a name="API_UpdateDetectorVersion_RequestSyntax"></a>

```
{
   "description": "{{string}}",
   "detectorId": "{{string}}",
   "detectorVersionId": "{{string}}",
   "externalModelEndpoints": [ "{{string}}" ],
   "modelVersions": [
      {
         "arn": "{{string}}",
         "modelId": "{{string}}",
         "modelType": "{{string}}",
         "modelVersionNumber": "{{string}}"
      }
   ],
   "ruleExecutionMode": "{{string}}",
   "rules": [
      {
         "detectorId": "{{string}}",
         "ruleId": "{{string}}",
         "ruleVersion": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_UpdateDetectorVersion_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [description](#API_UpdateDetectorVersion_RequestSyntax) **   <a name="FraudDetector-UpdateDetectorVersion-request-description"></a>
The detector version description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [detectorId](#API_UpdateDetectorVersion_RequestSyntax) **   <a name="FraudDetector-UpdateDetectorVersion-request-detectorId"></a>
The parent detector ID for the detector version you want to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_-]+$`
Required: Yes

 ** [detectorVersionId](#API_UpdateDetectorVersion_RequestSyntax) **   <a name="FraudDetector-UpdateDetectorVersion-request-detectorVersionId"></a>
The detector version ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^([1-9][0-9]*)$`
Required: Yes

 ** [externalModelEndpoints](#API_UpdateDetectorVersion_RequestSyntax) **   <a name="FraudDetector-UpdateDetectorVersion-request-externalModelEndpoints"></a>
The Amazon SageMaker model endpoints to include in the detector version.
Type: Array of strings
Required: Yes

 ** [modelVersions](#API_UpdateDetectorVersion_RequestSyntax) **   <a name="FraudDetector-UpdateDetectorVersion-request-modelVersions"></a>
The model versions to include in the detector version.
Type: Array of [ModelVersion](API_ModelVersion.md) objects
Required: No

 ** [ruleExecutionMode](#API_UpdateDetectorVersion_RequestSyntax) **   <a name="FraudDetector-UpdateDetectorVersion-request-ruleExecutionMode"></a>
The rule execution mode to add to the detector.
If you specify `FIRST_MATCHED`, Amazon Fraud Detector evaluates rules sequentially, first to last, stopping at the first matched rule. Amazon Fraud dectector then provides the outcomes for that single rule.
If you specifiy `ALL_MATCHED`, Amazon Fraud Detector evaluates all rules and returns the outcomes for all matched rules. You can define and edit the rule mode at the detector version level, when it is in draft status.
The default behavior is `FIRST_MATCHED`.
Type: String
Valid Values: `ALL_MATCHED | FIRST_MATCHED`
Required: No

 ** [rules](#API_UpdateDetectorVersion_RequestSyntax) **   <a name="FraudDetector-UpdateDetectorVersion-request-rules"></a>
The rules to include in the detector version.
Type: Array of [Rule](API_Rule.md) objects
Required: Yes

## Response Elements
<a name="API_UpdateDetectorVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateDetectorVersion_Errors"></a>

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
<a name="API_UpdateDetectorVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/frauddetector-2019-11-15/UpdateDetectorVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/frauddetector-2019-11-15/UpdateDetectorVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/UpdateDetectorVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/frauddetector-2019-11-15/UpdateDetectorVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/UpdateDetectorVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/frauddetector-2019-11-15/UpdateDetectorVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/frauddetector-2019-11-15/UpdateDetectorVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/frauddetector-2019-11-15/UpdateDetectorVersion)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/frauddetector-2019-11-15/UpdateDetectorVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/UpdateDetectorVersion)
