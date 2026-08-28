---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_GetModelVersion.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# GetModelVersion
<a name="API_GetModelVersion"></a>

Gets the details of the specified model version.

## Request Syntax
<a name="API_GetModelVersion_RequestSyntax"></a>

```
{
   "modelId": "{{string}}",
   "modelType": "{{string}}",
   "modelVersionNumber": "{{string}}"
}
```

## Request Parameters
<a name="API_GetModelVersion_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [modelId](#API_GetModelVersion_RequestSyntax) **   <a name="FraudDetector-GetModelVersion-request-modelId"></a>
The model ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_]+$`
Required: Yes

 ** [modelType](#API_GetModelVersion_RequestSyntax) **   <a name="FraudDetector-GetModelVersion-request-modelType"></a>
The model type.
Type: String
Valid Values: `ONLINE_FRAUD_INSIGHTS | TRANSACTION_FRAUD_INSIGHTS | ACCOUNT_TAKEOVER_INSIGHTS`
Required: Yes

 ** [modelVersionNumber](#API_GetModelVersion_RequestSyntax) **   <a name="FraudDetector-GetModelVersion-request-modelVersionNumber"></a>
The model version number.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 7.
Pattern: `^[1-9][0-9]{0,3}\.[0-9]{1,2}$`
Required: Yes

## Response Syntax
<a name="API_GetModelVersion_ResponseSyntax"></a>

```
{
   "arn": "string",
   "externalEventsDetail": {
      "dataAccessRoleArn": "string",
      "dataLocation": "string"
   },
   "ingestedEventsDetail": {
      "ingestedEventsTimeWindow": {
         "endTime": "string",
         "startTime": "string"
      }
   },
   "modelId": "string",
   "modelType": "string",
   "modelVersionNumber": "string",
   "status": "string",
   "trainingDataSchema": {
      "labelSchema": {
         "labelMapper": {
            "string" : [ "string" ]
         },
         "unlabeledEventsTreatment": "string"
      },
      "modelVariables": [ "string" ]
   },
   "trainingDataSource": "string"
}
```

## Response Elements
<a name="API_GetModelVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetModelVersion_ResponseSyntax) **   <a name="FraudDetector-GetModelVersion-response-arn"></a>
The model version ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn\:aws[a-z-]{0,15}\:frauddetector\:[a-z0-9-]{3,20}\:[0-9]{12}\:[^\s]{2,128}$`

 ** [externalEventsDetail](#API_GetModelVersion_ResponseSyntax) **   <a name="FraudDetector-GetModelVersion-response-externalEventsDetail"></a>
The details of the external events data used for training the model version. This will be populated if the `trainingDataSource` is `EXTERNAL_EVENTS`
Type: [ExternalEventsDetail](API_ExternalEventsDetail.md) object

 ** [ingestedEventsDetail](#API_GetModelVersion_ResponseSyntax) **   <a name="FraudDetector-GetModelVersion-response-ingestedEventsDetail"></a>
The details of the ingested events data used for training the model version. This will be populated if the `trainingDataSource` is `INGESTED_EVENTS`.
Type: [IngestedEventsDetail](API_IngestedEventsDetail.md) object

 ** [modelId](#API_GetModelVersion_ResponseSyntax) **   <a name="FraudDetector-GetModelVersion-response-modelId"></a>
The model ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_]+$`

 ** [modelType](#API_GetModelVersion_ResponseSyntax) **   <a name="FraudDetector-GetModelVersion-response-modelType"></a>
The model type.
Type: String
Valid Values: `ONLINE_FRAUD_INSIGHTS | TRANSACTION_FRAUD_INSIGHTS | ACCOUNT_TAKEOVER_INSIGHTS`

 ** [modelVersionNumber](#API_GetModelVersion_ResponseSyntax) **   <a name="FraudDetector-GetModelVersion-response-modelVersionNumber"></a>
The model version number.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 7.
Pattern: `^[1-9][0-9]{0,3}\.[0-9]{1,2}$`

 ** [status](#API_GetModelVersion_ResponseSyntax) **   <a name="FraudDetector-GetModelVersion-response-status"></a>
The model version status.
Possible values are:
+  `TRAINING_IN_PROGRESS`
+  `TRAINING_COMPLETE`
+  `ACTIVATE_REQUESTED`
+  `ACTIVATE_IN_PROGRESS`
+  `ACTIVE`
+  `INACTIVATE_REQUESTED`
+  `INACTIVATE_IN_PROGRESS`
+  `INACTIVE`
+  `ERROR`
Type: String

 ** [trainingDataSchema](#API_GetModelVersion_ResponseSyntax) **   <a name="FraudDetector-GetModelVersion-response-trainingDataSchema"></a>
The training data schema.
Type: [TrainingDataSchema](API_TrainingDataSchema.md) object

 ** [trainingDataSource](#API_GetModelVersion_ResponseSyntax) **   <a name="FraudDetector-GetModelVersion-response-trainingDataSource"></a>
The training data source.
Type: String
Valid Values: `EXTERNAL_EVENTS | INGESTED_EVENTS`

## Errors
<a name="API_GetModelVersion_Errors"></a>

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
<a name="API_GetModelVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/frauddetector-2019-11-15/GetModelVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/frauddetector-2019-11-15/GetModelVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/GetModelVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/frauddetector-2019-11-15/GetModelVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/GetModelVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/frauddetector-2019-11-15/GetModelVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/frauddetector-2019-11-15/GetModelVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/frauddetector-2019-11-15/GetModelVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/frauddetector-2019-11-15/GetModelVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/GetModelVersion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Fraud Detector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query frauddetector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
