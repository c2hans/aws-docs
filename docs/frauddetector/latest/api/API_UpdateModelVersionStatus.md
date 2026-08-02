---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_UpdateModelVersionStatus.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# UpdateModelVersionStatus
<a name="API_UpdateModelVersionStatus"></a>

Updates the status of a model version.

You can perform the following status updates:

1. Change the `TRAINING_IN_PROGRESS` status to `TRAINING_CANCELLED`.

1. Change the `TRAINING_COMPLETE` status to `ACTIVE`.

1. Change `ACTIVE` to `INACTIVE`.

## Request Syntax
<a name="API_UpdateModelVersionStatus_RequestSyntax"></a>

```
{
   "modelId": "{{string}}",
   "modelType": "{{string}}",
   "modelVersionNumber": "{{string}}",
   "status": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateModelVersionStatus_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [modelId](#API_UpdateModelVersionStatus_RequestSyntax) **   <a name="FraudDetector-UpdateModelVersionStatus-request-modelId"></a>
The model ID of the model version to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_]+$`
Required: Yes

 ** [modelType](#API_UpdateModelVersionStatus_RequestSyntax) **   <a name="FraudDetector-UpdateModelVersionStatus-request-modelType"></a>
The model type.
Type: String
Valid Values: `ONLINE_FRAUD_INSIGHTS | TRANSACTION_FRAUD_INSIGHTS | ACCOUNT_TAKEOVER_INSIGHTS`
Required: Yes

 ** [modelVersionNumber](#API_UpdateModelVersionStatus_RequestSyntax) **   <a name="FraudDetector-UpdateModelVersionStatus-request-modelVersionNumber"></a>
The model version number.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 7.
Pattern: `^[1-9][0-9]{0,3}\.[0-9]{1,2}$`
Required: Yes

 ** [status](#API_UpdateModelVersionStatus_RequestSyntax) **   <a name="FraudDetector-UpdateModelVersionStatus-request-status"></a>
The model version status.
Type: String
Valid Values: `ACTIVE | INACTIVE | TRAINING_CANCELLED`
Required: Yes

## Response Elements
<a name="API_UpdateModelVersionStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateModelVersionStatus_Errors"></a>

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
<a name="API_UpdateModelVersionStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/frauddetector-2019-11-15/UpdateModelVersionStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/frauddetector-2019-11-15/UpdateModelVersionStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/UpdateModelVersionStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/frauddetector-2019-11-15/UpdateModelVersionStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/UpdateModelVersionStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/frauddetector-2019-11-15/UpdateModelVersionStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/frauddetector-2019-11-15/UpdateModelVersionStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/frauddetector-2019-11-15/UpdateModelVersionStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/frauddetector-2019-11-15/UpdateModelVersionStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/UpdateModelVersionStatus)
