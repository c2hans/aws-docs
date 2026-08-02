---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_CreateDetectorVersion.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# CreateDetectorVersion
<a name="API_CreateDetectorVersion"></a>

Creates a detector version. The detector version starts in a `DRAFT` status.

## Request Syntax
<a name="API_CreateDetectorVersion_RequestSyntax"></a>

```
{
   "description": "{{string}}",
   "detectorId": "{{string}}",
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
   ],
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateDetectorVersion_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [description](#API_CreateDetectorVersion_RequestSyntax) **   <a name="FraudDetector-CreateDetectorVersion-request-description"></a>
The description of the detector version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [detectorId](#API_CreateDetectorVersion_RequestSyntax) **   <a name="FraudDetector-CreateDetectorVersion-request-detectorId"></a>
The ID of the detector under which you want to create a new version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_-]+$`
Required: Yes

 ** [externalModelEndpoints](#API_CreateDetectorVersion_RequestSyntax) **   <a name="FraudDetector-CreateDetectorVersion-request-externalModelEndpoints"></a>
The Amazon Sagemaker model endpoints to include in the detector version.
Type: Array of strings
Required: No

 ** [modelVersions](#API_CreateDetectorVersion_RequestSyntax) **   <a name="FraudDetector-CreateDetectorVersion-request-modelVersions"></a>
The model versions to include in the detector version.
Type: Array of [ModelVersion](API_ModelVersion.md) objects
Required: No

 ** [ruleExecutionMode](#API_CreateDetectorVersion_RequestSyntax) **   <a name="FraudDetector-CreateDetectorVersion-request-ruleExecutionMode"></a>
The rule execution mode for the rules included in the detector version.
You can define and edit the rule mode at the detector version level, when it is in draft status.
If you specify `FIRST_MATCHED`, Amazon Fraud Detector evaluates rules sequentially, first to last, stopping at the first matched rule. Amazon Fraud dectector then provides the outcomes for that single rule.
If you specifiy `ALL_MATCHED`, Amazon Fraud Detector evaluates all rules and returns the outcomes for all matched rules.
The default behavior is `FIRST_MATCHED`.
Type: String
Valid Values: `ALL_MATCHED | FIRST_MATCHED`
Required: No

 ** [rules](#API_CreateDetectorVersion_RequestSyntax) **   <a name="FraudDetector-CreateDetectorVersion-request-rules"></a>
The rules to include in the detector version.
Type: Array of [Rule](API_Rule.md) objects
Required: Yes

 ** [tags](#API_CreateDetectorVersion_RequestSyntax) **   <a name="FraudDetector-CreateDetectorVersion-request-tags"></a>
A collection of key and value pairs.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreateDetectorVersion_ResponseSyntax"></a>

```
{
   "detectorId": "string",
   "detectorVersionId": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_CreateDetectorVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [detectorId](#API_CreateDetectorVersion_ResponseSyntax) **   <a name="FraudDetector-CreateDetectorVersion-response-detectorId"></a>
The ID for the created version's parent detector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_-]+$`

 ** [detectorVersionId](#API_CreateDetectorVersion_ResponseSyntax) **   <a name="FraudDetector-CreateDetectorVersion-response-detectorVersionId"></a>
The ID for the created detector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^([1-9][0-9]*)$`

 ** [status](#API_CreateDetectorVersion_ResponseSyntax) **   <a name="FraudDetector-CreateDetectorVersion-response-status"></a>
The status of the detector version.
Type: String
Valid Values: `DRAFT | ACTIVE | INACTIVE`

## Errors
<a name="API_CreateDetectorVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as `PutExternalModel`, that specifies a role that is not in your account.
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
<a name="API_CreateDetectorVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/frauddetector-2019-11-15/CreateDetectorVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/frauddetector-2019-11-15/CreateDetectorVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/CreateDetectorVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/frauddetector-2019-11-15/CreateDetectorVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/CreateDetectorVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/frauddetector-2019-11-15/CreateDetectorVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/frauddetector-2019-11-15/CreateDetectorVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/frauddetector-2019-11-15/CreateDetectorVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/frauddetector-2019-11-15/CreateDetectorVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/CreateDetectorVersion)
