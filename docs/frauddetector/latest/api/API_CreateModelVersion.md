---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_CreateModelVersion.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# CreateModelVersion
<a name="API_CreateModelVersion"></a>

Creates a version of the model using the specified model type and model id.

## Request Syntax
<a name="API_CreateModelVersion_RequestSyntax"></a>

```
{
   "externalEventsDetail": {
      "dataAccessRoleArn": "{{string}}",
      "dataLocation": "{{string}}"
   },
   "ingestedEventsDetail": {
      "ingestedEventsTimeWindow": {
         "endTime": "{{string}}",
         "startTime": "{{string}}"
      }
   },
   "modelId": "{{string}}",
   "modelType": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "trainingDataSchema": {
      "labelSchema": {
         "labelMapper": {
            "{{string}}" : [ "{{string}}" ]
         },
         "unlabeledEventsTreatment": "{{string}}"
      },
      "modelVariables": [ "{{string}}" ]
   },
   "trainingDataSource": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateModelVersion_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [externalEventsDetail](#API_CreateModelVersion_RequestSyntax) **   <a name="FraudDetector-CreateModelVersion-request-externalEventsDetail"></a>
Details of the external events data used for model version training. Required if `trainingDataSource` is `EXTERNAL_EVENTS`.
Type: [ExternalEventsDetail](API_ExternalEventsDetail.md) object
Required: No

 ** [ingestedEventsDetail](#API_CreateModelVersion_RequestSyntax) **   <a name="FraudDetector-CreateModelVersion-request-ingestedEventsDetail"></a>
Details of the ingested events data used for model version training. Required if `trainingDataSource` is `INGESTED_EVENTS`.
Type: [IngestedEventsDetail](API_IngestedEventsDetail.md) object
Required: No

 ** [modelId](#API_CreateModelVersion_RequestSyntax) **   <a name="FraudDetector-CreateModelVersion-request-modelId"></a>
The model ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_]+$`
Required: Yes

 ** [modelType](#API_CreateModelVersion_RequestSyntax) **   <a name="FraudDetector-CreateModelVersion-request-modelType"></a>
The model type.
Type: String
Valid Values: `ONLINE_FRAUD_INSIGHTS | TRANSACTION_FRAUD_INSIGHTS | ACCOUNT_TAKEOVER_INSIGHTS`
Required: Yes

 ** [tags](#API_CreateModelVersion_RequestSyntax) **   <a name="FraudDetector-CreateModelVersion-request-tags"></a>
A collection of key and value pairs.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** [trainingDataSchema](#API_CreateModelVersion_RequestSyntax) **   <a name="FraudDetector-CreateModelVersion-request-trainingDataSchema"></a>
The training data schema.
Type: [TrainingDataSchema](API_TrainingDataSchema.md) object
Required: Yes

 ** [trainingDataSource](#API_CreateModelVersion_RequestSyntax) **   <a name="FraudDetector-CreateModelVersion-request-trainingDataSource"></a>
The training data source location in Amazon S3.
Type: String
Valid Values: `EXTERNAL_EVENTS | INGESTED_EVENTS`
Required: Yes

## Response Syntax
<a name="API_CreateModelVersion_ResponseSyntax"></a>

```
{
   "modelId": "string",
   "modelType": "string",
   "modelVersionNumber": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_CreateModelVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [modelId](#API_CreateModelVersion_ResponseSyntax) **   <a name="FraudDetector-CreateModelVersion-response-modelId"></a>
The model ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_]+$`

 ** [modelType](#API_CreateModelVersion_ResponseSyntax) **   <a name="FraudDetector-CreateModelVersion-response-modelType"></a>
The model type.
Type: String
Valid Values: `ONLINE_FRAUD_INSIGHTS | TRANSACTION_FRAUD_INSIGHTS | ACCOUNT_TAKEOVER_INSIGHTS`

 ** [modelVersionNumber](#API_CreateModelVersion_ResponseSyntax) **   <a name="FraudDetector-CreateModelVersion-response-modelVersionNumber"></a>
The model version number of the model version created.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 7.
Pattern: `^[1-9][0-9]{0,3}\.[0-9]{1,2}$`

 ** [status](#API_CreateModelVersion_ResponseSyntax) **   <a name="FraudDetector-CreateModelVersion-response-status"></a>
The model version status.
Type: String

## Errors
<a name="API_CreateModelVersion_Errors"></a>

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
<a name="API_CreateModelVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/frauddetector-2019-11-15/CreateModelVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/frauddetector-2019-11-15/CreateModelVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/CreateModelVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/frauddetector-2019-11-15/CreateModelVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/CreateModelVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/frauddetector-2019-11-15/CreateModelVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/frauddetector-2019-11-15/CreateModelVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/frauddetector-2019-11-15/CreateModelVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/frauddetector-2019-11-15/CreateModelVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/CreateModelVersion)
