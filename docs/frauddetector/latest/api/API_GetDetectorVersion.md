---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_GetDetectorVersion.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# GetDetectorVersion
<a name="API_GetDetectorVersion"></a>

Gets a particular detector version.

## Request Syntax
<a name="API_GetDetectorVersion_RequestSyntax"></a>

```
{
   "detectorId": "{{string}}",
   "detectorVersionId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetDetectorVersion_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [detectorId](#API_GetDetectorVersion_RequestSyntax) **   <a name="FraudDetector-GetDetectorVersion-request-detectorId"></a>
The detector ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_-]+$`
Required: Yes

 ** [detectorVersionId](#API_GetDetectorVersion_RequestSyntax) **   <a name="FraudDetector-GetDetectorVersion-request-detectorVersionId"></a>
The detector version ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^([1-9][0-9]*)$`
Required: Yes

## Response Syntax
<a name="API_GetDetectorVersion_ResponseSyntax"></a>

```
{
   "arn": "string",
   "createdTime": "string",
   "description": "string",
   "detectorId": "string",
   "detectorVersionId": "string",
   "externalModelEndpoints": [ "string" ],
   "lastUpdatedTime": "string",
   "modelVersions": [
      {
         "arn": "string",
         "modelId": "string",
         "modelType": "string",
         "modelVersionNumber": "string"
      }
   ],
   "ruleExecutionMode": "string",
   "rules": [
      {
         "detectorId": "string",
         "ruleId": "string",
         "ruleVersion": "string"
      }
   ],
   "status": "string"
}
```

## Response Elements
<a name="API_GetDetectorVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetDetectorVersion_ResponseSyntax) **   <a name="FraudDetector-GetDetectorVersion-response-arn"></a>
The detector version ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn\:aws[a-z-]{0,15}\:frauddetector\:[a-z0-9-]{3,20}\:[0-9]{12}\:[^\s]{2,128}$`

 ** [createdTime](#API_GetDetectorVersion_ResponseSyntax) **   <a name="FraudDetector-GetDetectorVersion-response-createdTime"></a>
The timestamp when the detector version was created.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 30.

 ** [description](#API_GetDetectorVersion_ResponseSyntax) **   <a name="FraudDetector-GetDetectorVersion-response-description"></a>
The detector version description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [detectorId](#API_GetDetectorVersion_ResponseSyntax) **   <a name="FraudDetector-GetDetectorVersion-response-detectorId"></a>
The detector ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_-]+$`

 ** [detectorVersionId](#API_GetDetectorVersion_ResponseSyntax) **   <a name="FraudDetector-GetDetectorVersion-response-detectorVersionId"></a>
The detector version ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^([1-9][0-9]*)$`

 ** [externalModelEndpoints](#API_GetDetectorVersion_ResponseSyntax) **   <a name="FraudDetector-GetDetectorVersion-response-externalModelEndpoints"></a>
The Amazon SageMaker model endpoints included in the detector version.
Type: Array of strings

 ** [lastUpdatedTime](#API_GetDetectorVersion_ResponseSyntax) **   <a name="FraudDetector-GetDetectorVersion-response-lastUpdatedTime"></a>
The timestamp when the detector version was last updated.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 30.

 ** [modelVersions](#API_GetDetectorVersion_ResponseSyntax) **   <a name="FraudDetector-GetDetectorVersion-response-modelVersions"></a>
The model versions included in the detector version.
Type: Array of [ModelVersion](API_ModelVersion.md) objects

 ** [ruleExecutionMode](#API_GetDetectorVersion_ResponseSyntax) **   <a name="FraudDetector-GetDetectorVersion-response-ruleExecutionMode"></a>
The execution mode of the rule in the dectector
 `FIRST_MATCHED` indicates that Amazon Fraud Detector evaluates rules sequentially, first to last, stopping at the first matched rule. Amazon Fraud dectector then provides the outcomes for that single rule.
 `ALL_MATCHED` indicates that Amazon Fraud Detector evaluates all rules and returns the outcomes for all matched rules. You can define and edit the rule mode at the detector version level, when it is in draft status.
Type: String
Valid Values: `ALL_MATCHED | FIRST_MATCHED`

 ** [rules](#API_GetDetectorVersion_ResponseSyntax) **   <a name="FraudDetector-GetDetectorVersion-response-rules"></a>
The rules included in the detector version.
Type: Array of [Rule](API_Rule.md) objects

 ** [status](#API_GetDetectorVersion_ResponseSyntax) **   <a name="FraudDetector-GetDetectorVersion-response-status"></a>
The status of the detector version.
Type: String
Valid Values: `DRAFT | ACTIVE | INACTIVE`

## Errors
<a name="API_GetDetectorVersion_Errors"></a>

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
<a name="API_GetDetectorVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/frauddetector-2019-11-15/GetDetectorVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/frauddetector-2019-11-15/GetDetectorVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/GetDetectorVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/frauddetector-2019-11-15/GetDetectorVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/GetDetectorVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/frauddetector-2019-11-15/GetDetectorVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/frauddetector-2019-11-15/GetDetectorVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/frauddetector-2019-11-15/GetDetectorVersion)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/frauddetector-2019-11-15/GetDetectorVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/GetDetectorVersion)
