---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeContactEvaluation.html
---

# DescribeContactEvaluation
<a name="API_DescribeContactEvaluation"></a>

Describes a contact evaluation in the specified Connect Customer instance.

## Request Syntax
<a name="API_DescribeContactEvaluation_RequestSyntax"></a>

```
GET /contact-evaluations/{{InstanceId}}/{{EvaluationId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeContactEvaluation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [EvaluationId](#API_DescribeContactEvaluation_RequestSyntax) **   <a name="connect-DescribeContactEvaluation-request-uri-EvaluationId"></a>
A unique identifier for the contact evaluation.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** [InstanceId](#API_DescribeContactEvaluation_RequestSyntax) **   <a name="connect-DescribeContactEvaluation-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_DescribeContactEvaluation_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeContactEvaluation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Evaluation": {
      "Answers": {
         "string" : {
            "SuggestedAnswers": [
               {
                  "AnalysisDetails": { ... },
                  "AnalysisType": "string",
                  "Input": {
                     "TranscriptType": "string"
                  },
                  "Status": "string",
                  "Value": { ... }
               }
            ],
            "SystemSuggestedValue": { ... },
            "Value": { ... }
         }
      },
      "CreatedTime": number,
      "EvaluationArn": "string",
      "EvaluationId": "string",
      "EvaluationType": "string",
      "LastModifiedTime": number,
      "Metadata": {
         "Acknowledgement": {
            "AcknowledgedBy": "string",
            "AcknowledgedTime": number,
            "AcknowledgerComment": "string"
         },
         "AutoEvaluation": {
            "AutoEvaluationEnabled": boolean,
            "AutoEvaluationStatus": "string"
         },
         "CalibrationSessionId": "string",
         "ContactAgentId": "string",
         "ContactId": "string",
         "ContactParticipant": {
            "ContactParticipantId": "string",
            "ContactParticipantRole": "string"
         },
         "EvaluatorArn": "string",
         "Review": {
            "CreatedBy": "string",
            "CreatedTime": number,
            "RequestedBy": "string",
            "RequestedTime": number,
            "ReviewId": "string",
            "ReviewRequestComments": [
               {
                  "Comment": "string",
                  "CreatedBy": "string",
                  "CreatedTime": number
               }
            ]
         },
         "SamplingJobId": "string",
         "Score": {
            "AppliedWeight": number,
            "AutomaticFail": boolean,
            "EarnedPoints": number,
            "MaxBasePoint": number,
            "NotApplicable": boolean,
            "Percentage": number,
            "PerformanceCategory": "string"
         }
      },
      "Notes": {
         "string" : {
            "Value": "string"
         }
      },
      "Scores": {
         "string" : {
            "AppliedWeight": number,
            "AutomaticFail": boolean,
            "EarnedPoints": number,
            "MaxBasePoint": number,
            "NotApplicable": boolean,
            "Percentage": number,
            "PerformanceCategory": "string"
         }
      },
      "Status": "string",
      "Tags": {
         "string" : "string"
      }
   },
   "EvaluationForm": {
      "AutoEvaluationConfiguration": {
         "Enabled": boolean
      },
      "Description": "string",
      "EvaluationFormArn": "string",
      "EvaluationFormId": "string",
      "EvaluationFormVersion": number,
      "Items": [
         { ... }
      ],
      "LanguageConfiguration": {
         "FormLanguage": "string"
      },
      "ReviewConfiguration": {
         "EligibilityDays": number,
         "ReviewNotificationRecipients": [
            {
               "Type": "string",
               "Value": {
                  "UserId": "string"
               }
            }
         ]
      },
      "ScoringStrategy": {
         "Mode": "string",
         "ScoreThresholds": [
            {
               "MaxScorePercentage": number,
               "MinScorePercentage": number,
               "PerformanceCategory": "string"
            }
         ],
         "Status": "string"
      },
      "TargetConfiguration": {
         "ContactInteractionType": "string"
      },
      "Title": "string"
   }
}
```

## Response Elements
<a name="API_DescribeContactEvaluation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Evaluation](#API_DescribeContactEvaluation_ResponseSyntax) **   <a name="connect-DescribeContactEvaluation-response-Evaluation"></a>
Information about the evaluation form completed for a specific contact.
Type: [Evaluation](API_Evaluation.md) object

 ** [EvaluationForm](#API_DescribeContactEvaluation_ResponseSyntax) **   <a name="connect-DescribeContactEvaluation-response-EvaluationForm"></a>
Information about the evaluation form.
Type: [EvaluationFormContent](API_EvaluationFormContent.md) object

## Errors
<a name="API_DescribeContactEvaluation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## Examples
<a name="API_DescribeContactEvaluation_Examples"></a>

### Example
<a name="API_DescribeContactEvaluation_Example_1"></a>

The following example describes a contact evaluation.

#### Sample Request
<a name="API_DescribeContactEvaluation_Example_1_Request"></a>

```
{
   "InstanceId": "[instance_id]",
   "EvaluationId": "[evaluation_id]"
}
```

#### Sample Response
<a name="API_DescribeContactEvaluation_Example_1_Response"></a>

```
{
   "Evaluation": {
      "EvaluationId": "[evaluation_id]",
      "EvaluationArn": "arn:aws:connect:[aws_region_code]:[account_id]:instance/[instance_id]/contact-evaluation/[evaluation_id]",
      "Metadata": {
         "ContactId": "[contact_id]",
         "EvaluatorArn": "arn:aws:connect:[aws_region_code]:[account_id]:instance/[instance_id]/agent/arn:aws:sts::[account_id]:assumed-role/Admin/username",
         "ContactAgentId": "[contact_agent_id]"
      },
      "Answers": {},
      "Notes": {},
      "Status": "DRAFT",
      "CreatedTime": "2023-05-04T01:16:29.693000-07:00",
      "LastModifiedTime": "2023-05-04T01:16:29.693000-07:00",
      "Tags": {}
   },
   "EvaluationForm": {
      "EvaluationFormVersion": 1,
      "EvaluationFormId": "[evaluation_form_id]",
      "EvaluationFormArn": "arn:aws:connect:[aws_region_code]:[account_id]:instance/[instance_id]/evaluation-form/[evaluation_form_id]",
      "Title": "form-title",
      "Description": "form-description",
      "Items": [
         {
            "Section": {
               "Title": "section-title-1",
               "RefId": "section-1",
               "Instructions": "section-instruction-1",
               "Items": [
                  {
                     "Question": {
                        "Title": "question-title-11",
                        "Instructions": "question-instructions",
                        "RefId": "question-1-111",
                        "NotApplicableEnabled": false,
                        "QuestionType": "TEXT"
                     }
                  },
                  {
                     "Question": {
                        "Title": "question-title-12",
                        "RefId": "question-1-222",
                        "NotApplicableEnabled": false,
                        "QuestionType": "SINGLESELECT",
                        "QuestionTypeProperties": {
                           "SingleSelect": {
                              "Options": [
                                 {
                                    "RefId": "option-1-2-1",
                                    "Text": "first-option",
                                    "Score": 1,
                                    "AutomaticFail": true
                                 },
                                 {
                                    "RefId": "option-1-2-2",
                                    "Text": "second-option",
                                    "Score": 1,
                                    "AutomaticFail": false
                                 },
                                 {
                                    "RefId": "option-1-2-3",
                                    "Text": "third-option",
                                    "Score": 1,
                                    "AutomaticFail": true
                                 }
                              ],
                              "DisplayAs": "DROPDOWN",
                              "Automation": {
                                 "Options": [
                                    {
                                       "RuleCategory": {
                                          "Category": "CATEGORY_LABEL",
                                          "Condition": "PRESENT",
                                          "OptionRefId": "option-1-2-2"
                                       }
                                    }
                                 ],
                                 "DefaultOptionRefId": "option-1-2-1"
                              }
                           }
                        }
                     }
                  }
               ],
               "Weight": 50
            }
         },
         {
            "Section": {
               "Title": "section-title-2",
               "RefId": "section-2",
               "Instructions": "section-instruction-2",
               "Items": [
                  {
                     "Question": {
                        "Title": "question-title-21",
                        "RefId": "question-2-1",
                        "NotApplicableEnabled": true,
                        "QuestionType": "TEXT"
                     }
                  },
                  {
                     "Question": {
                        "Title": "question-title-2-2",
                        "RefId": "question-2-222",
                        "QuestionType": "NUMERIC",
                        "QuestionTypeProperties": {
                           "Numeric": {
                              "MinValue": 0,
                              "MaxValue": 28800,
                              "Options": [
                                 {
                                    "MinValue": 0,
                                    "MaxValue": 28800,
                                    "Score": 1,
                                    "AutomaticFail": false
                                 }
                              ],
                              "Automation": {
                                 "PropertyValue": {
                                    "Label": "AGENT_INTERACTION_DURATION"
                                 }
                              }
                           }
                        }
                     }
                  }
               ],
               "Weight": 50
            }
         }
      ],
      "ScoringStrategy": {
         "Mode": "SECTION_ONLY",
         "Status": "ENABLED"
      }
   }
}
```

## See Also
<a name="API_DescribeContactEvaluation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/DescribeContactEvaluation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/DescribeContactEvaluation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DescribeContactEvaluation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/DescribeContactEvaluation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DescribeContactEvaluation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/DescribeContactEvaluation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/DescribeContactEvaluation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/DescribeContactEvaluation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/DescribeContactEvaluation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DescribeContactEvaluation)
