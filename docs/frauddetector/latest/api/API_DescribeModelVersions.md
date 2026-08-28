---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_DescribeModelVersions.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# DescribeModelVersions
<a name="API_DescribeModelVersions"></a>

Gets all of the model versions for the specified model type or for the specified model type and model ID. You can also get details for a single, specified model version.

## Request Syntax
<a name="API_DescribeModelVersions_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "modelId": "{{string}}",
   "modelType": "{{string}}",
   "modelVersionNumber": "{{string}}",
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeModelVersions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_DescribeModelVersions_RequestSyntax) **   <a name="FraudDetector-DescribeModelVersions-request-maxResults"></a>
The maximum number of results to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10.
Required: No

 ** [modelId](#API_DescribeModelVersions_RequestSyntax) **   <a name="FraudDetector-DescribeModelVersions-request-modelId"></a>
The model ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_]+$`
Required: No

 ** [modelType](#API_DescribeModelVersions_RequestSyntax) **   <a name="FraudDetector-DescribeModelVersions-request-modelType"></a>
The model type.
Type: String
Valid Values: `ONLINE_FRAUD_INSIGHTS | TRANSACTION_FRAUD_INSIGHTS | ACCOUNT_TAKEOVER_INSIGHTS`
Required: No

 ** [modelVersionNumber](#API_DescribeModelVersions_RequestSyntax) **   <a name="FraudDetector-DescribeModelVersions-request-modelVersionNumber"></a>
The model version number.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 7.
Pattern: `^[1-9][0-9]{0,3}\.[0-9]{1,2}$`
Required: No

 ** [nextToken](#API_DescribeModelVersions_RequestSyntax) **   <a name="FraudDetector-DescribeModelVersions-request-nextToken"></a>
The next token from the previous results.
Type: String
Required: No

## Response Syntax
<a name="API_DescribeModelVersions_ResponseSyntax"></a>

```
{
   "modelVersionDetails": [
      {
         "arn": "string",
         "createdTime": "string",
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
         "lastUpdatedTime": "string",
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
         "trainingDataSource": "string",
         "trainingResult": {
            "dataValidationMetrics": {
               "fieldLevelMessages": [
                  {
                     "content": "string",
                     "fieldName": "string",
                     "identifier": "string",
                     "title": "string",
                     "type": "string"
                  }
               ],
               "fileLevelMessages": [
                  {
                     "content": "string",
                     "title": "string",
                     "type": "string"
                  }
               ]
            },
            "trainingMetrics": {
               "auc": number,
               "metricDataPoints": [
                  {
                     "fpr": number,
                     "precision": number,
                     "threshold": number,
                     "tpr": number
                  }
               ]
            },
            "variableImportanceMetrics": {
               "logOddsMetrics": [
                  {
                     "variableImportance": number,
                     "variableName": "string",
                     "variableType": "string"
                  }
               ]
            }
         },
         "trainingResultV2": {
            "aggregatedVariablesImportanceMetrics": {
               "logOddsMetrics": [
                  {
                     "aggregatedVariablesImportance": number,
                     "variableNames": [ "string" ]
                  }
               ]
            },
            "dataValidationMetrics": {
               "fieldLevelMessages": [
                  {
                     "content": "string",
                     "fieldName": "string",
                     "identifier": "string",
                     "title": "string",
                     "type": "string"
                  }
               ],
               "fileLevelMessages": [
                  {
                     "content": "string",
                     "title": "string",
                     "type": "string"
                  }
               ]
            },
            "trainingMetricsV2": {
               "ati": {
                  "metricDataPoints": [
                     {
                        "adr": number,
                        "atodr": number,
                        "cr": number,
                        "threshold": number
                     }
                  ],
                  "modelPerformance": {
                     "asi": number
                  }
               },
               "ofi": {
                  "metricDataPoints": [
                     {
                        "fpr": number,
                        "precision": number,
                        "threshold": number,
                        "tpr": number
                     }
                  ],
                  "modelPerformance": {
                     "auc": number,
                     "uncertaintyRange": {
                        "lowerBoundValue": number,
                        "upperBoundValue": number
                     }
                  }
               },
               "tfi": {
                  "metricDataPoints": [
                     {
                        "fpr": number,
                        "precision": number,
                        "threshold": number,
                        "tpr": number
                     }
                  ],
                  "modelPerformance": {
                     "auc": number,
                     "uncertaintyRange": {
                        "lowerBoundValue": number,
                        "upperBoundValue": number
                     }
                  }
               }
            },
            "variableImportanceMetrics": {
               "logOddsMetrics": [
                  {
                     "variableImportance": number,
                     "variableName": "string",
                     "variableType": "string"
                  }
               ]
            }
         }
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeModelVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [modelVersionDetails](#API_DescribeModelVersions_ResponseSyntax) **   <a name="FraudDetector-DescribeModelVersions-response-modelVersionDetails"></a>
The model version details.
Type: Array of [ModelVersionDetail](API_ModelVersionDetail.md) objects

 ** [nextToken](#API_DescribeModelVersions_ResponseSyntax) **   <a name="FraudDetector-DescribeModelVersions-response-nextToken"></a>
The next token.
Type: String

## Errors
<a name="API_DescribeModelVersions_Errors"></a>

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
<a name="API_DescribeModelVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/frauddetector-2019-11-15/DescribeModelVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/frauddetector-2019-11-15/DescribeModelVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/DescribeModelVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/frauddetector-2019-11-15/DescribeModelVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/DescribeModelVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/frauddetector-2019-11-15/DescribeModelVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/frauddetector-2019-11-15/DescribeModelVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/frauddetector-2019-11-15/DescribeModelVersions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/frauddetector-2019-11-15/DescribeModelVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/DescribeModelVersions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Fraud Detector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query frauddetector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
