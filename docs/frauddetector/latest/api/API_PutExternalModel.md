---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_PutExternalModel.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# PutExternalModel
<a name="API_PutExternalModel"></a>

Creates or updates an Amazon SageMaker model endpoint. You can also use this action to update the configuration of the model endpoint, including the IAM role and/or the mapped variables.

## Request Syntax
<a name="API_PutExternalModel_RequestSyntax"></a>

```
{
   "inputConfiguration": {
      "csvInputTemplate": "{{string}}",
      "eventTypeName": "{{string}}",
      "format": "{{string}}",
      "jsonInputTemplate": "{{string}}",
      "useEventVariables": {{boolean}}
   },
   "invokeModelEndpointRoleArn": "{{string}}",
   "modelEndpoint": "{{string}}",
   "modelEndpointStatus": "{{string}}",
   "modelSource": "{{string}}",
   "outputConfiguration": {
      "csvIndexToVariableMap": {
         "{{string}}" : "{{string}}"
      },
      "format": "{{string}}",
      "jsonKeyToVariableMap": {
         "{{string}}" : "{{string}}"
      }
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
<a name="API_PutExternalModel_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [inputConfiguration](#API_PutExternalModel_RequestSyntax) **   <a name="FraudDetector-PutExternalModel-request-inputConfiguration"></a>
The model endpoint input configuration.
Type: [ModelInputConfiguration](API_ModelInputConfiguration.md) object
Required: Yes

 ** [invokeModelEndpointRoleArn](#API_PutExternalModel_RequestSyntax) **   <a name="FraudDetector-PutExternalModel-request-invokeModelEndpointRoleArn"></a>
The IAM role used to invoke the model endpoint.
Type: String
Required: Yes

 ** [modelEndpoint](#API_PutExternalModel_RequestSyntax) **   <a name="FraudDetector-PutExternalModel-request-modelEndpoint"></a>
The model endpoints name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `^[0-9A-Za-z_-]+$`
Required: Yes

 ** [modelEndpointStatus](#API_PutExternalModel_RequestSyntax) **   <a name="FraudDetector-PutExternalModel-request-modelEndpointStatus"></a>
The model endpoint’s status in Amazon Fraud Detector.
Type: String
Valid Values: `ASSOCIATED | DISSOCIATED`
Required: Yes

 ** [modelSource](#API_PutExternalModel_RequestSyntax) **   <a name="FraudDetector-PutExternalModel-request-modelSource"></a>
The source of the model.
Type: String
Valid Values: `SAGEMAKER`
Required: Yes

 ** [outputConfiguration](#API_PutExternalModel_RequestSyntax) **   <a name="FraudDetector-PutExternalModel-request-outputConfiguration"></a>
The model endpoint output configuration.
Type: [ModelOutputConfiguration](API_ModelOutputConfiguration.md) object
Required: Yes

 ** [tags](#API_PutExternalModel_RequestSyntax) **   <a name="FraudDetector-PutExternalModel-request-tags"></a>
A collection of key and value pairs.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Elements
<a name="API_PutExternalModel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutExternalModel_Errors"></a>

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

 ** ThrottlingException **
An exception indicating a throttling error.
HTTP Status Code: 400

 ** ValidationException **
An exception indicating a specified value is not allowed.
HTTP Status Code: 400

## See Also
<a name="API_PutExternalModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/frauddetector-2019-11-15/PutExternalModel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/frauddetector-2019-11-15/PutExternalModel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/PutExternalModel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/frauddetector-2019-11-15/PutExternalModel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/PutExternalModel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/frauddetector-2019-11-15/PutExternalModel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/frauddetector-2019-11-15/PutExternalModel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/frauddetector-2019-11-15/PutExternalModel)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/frauddetector-2019-11-15/PutExternalModel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/PutExternalModel)
