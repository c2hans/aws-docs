---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeEvaluationForm.html
---

# DescribeEvaluationForm
<a name="API_DescribeEvaluationForm"></a>

Describes an evaluation form in the specified Connect Customer instance. If the version property is not provided, the latest version of the evaluation form is described.

## Request Syntax
<a name="API_DescribeEvaluationForm_RequestSyntax"></a>

```
GET /evaluation-forms/{{InstanceId}}/{{EvaluationFormId}}?version={{EvaluationFormVersion}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeEvaluationForm_RequestParameters"></a>

The request uses the following URI parameters.

 ** [EvaluationFormId](#API_DescribeEvaluationForm_RequestSyntax) **   <a name="connect-DescribeEvaluationForm-request-uri-EvaluationFormId"></a>
A unique identifier for the contact evaluation.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** [EvaluationFormVersion](#API_DescribeEvaluationForm_RequestSyntax) **   <a name="connect-DescribeEvaluationForm-request-uri-EvaluationFormVersion"></a>
A version of the evaluation form.

 ** [InstanceId](#API_DescribeEvaluationForm_RequestSyntax) **   <a name="connect-DescribeEvaluationForm-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_DescribeEvaluationForm_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeEvaluationForm_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "EvaluationForm": {
      "AIVersion": "string",
      "AutoEvaluationConfiguration": {
         "Enabled": boolean
      },
      "CreatedBy": "string",
      "CreatedTime": number,
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
      "LastModifiedBy": "string",
      "LastModifiedTime": number,
      "LastValidationTime": number,
      "LatestValidationStatus": "string",
      "Locked": boolean,
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
      "Status": "string",
      "Tags": {
         "string" : "string"
      },
      "TargetConfiguration": {
         "ContactInteractionType": "string"
      },
      "Title": "string"
   }
}
```

## Response Elements
<a name="API_DescribeEvaluationForm_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EvaluationForm](#API_DescribeEvaluationForm_ResponseSyntax) **   <a name="connect-DescribeEvaluationForm-response-EvaluationForm"></a>
Information about the evaluation form.
Type: [EvaluationForm](API_EvaluationForm.md) object

## Errors
<a name="API_DescribeEvaluationForm_Errors"></a>

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
<a name="API_DescribeEvaluationForm_Examples"></a>

### Example
<a name="API_DescribeEvaluationForm_Example_1"></a>

The following example describes version 1 of an evaluation form.

#### Sample Request
<a name="API_DescribeEvaluationForm_Example_1_Request"></a>

```
{
   "InstanceId": "[instance_id]",
   "EvaluationFormId": "[evaluation_form_id]",
   "EvaluationFormVersion": 1
}
```

#### Sample Response
<a name="API_DescribeEvaluationForm_Example_1_Response"></a>

```
{
   "EvaluationForm": {
      "EvaluationFormId": "[evaluation_form_id]",
      "EvaluationFormVersion": 1,
      "Locked": false,
      "EvaluationFormArn": "arn:aws:connect:[aws_region_code]:[account_id]:instance/[instance_id]/evaluation-form/[evaluation_form_id]",
      "Title": "form-title",
      "Description": "form-description",
      "Status": "DRAFT",
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
      },
      "CreatedTime": "2023-05-04T00:24:01.490000-07:00",
      "CreatedBy": "arn:aws:sts::[account_id]:assumed-role/Admin/username",
      "LastModifiedTime": "2023-05-04T00:24:01.490000-07:00",
      "LastModifiedBy": "arn:aws:sts::[account_id]:assumed-role/Admin/username",
      "Tags": {}
   }
}
```

## See Also
<a name="API_DescribeEvaluationForm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/DescribeEvaluationForm)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/DescribeEvaluationForm)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DescribeEvaluationForm)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/DescribeEvaluationForm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DescribeEvaluationForm)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/DescribeEvaluationForm)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/DescribeEvaluationForm)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/DescribeEvaluationForm)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/DescribeEvaluationForm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DescribeEvaluationForm)
