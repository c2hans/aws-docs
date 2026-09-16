---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateEvaluationForm.html
---

# UpdateEvaluationForm
<a name="API_UpdateEvaluationForm"></a>

Updates details about a specific evaluation form version in the specified Connect Customer instance. Question and section identifiers cannot be duplicated within the same evaluation form.

This operation does not support partial updates. Instead it does a full update of evaluation form content.

## Request Syntax
<a name="API_UpdateEvaluationForm_RequestSyntax"></a>

```
PUT /evaluation-forms/{{InstanceId}}/{{EvaluationFormId}} HTTP/1.1
Content-type: application/json

{
   "AsDraft": {{boolean}},
   "AutoEvaluationConfiguration": {
      "Enabled": {{boolean}}
   },
   "ClientToken": "{{string}}",
   "CreateNewVersion": {{boolean}},
   "Description": "{{string}}",
   "EvaluationFormVersion": {{number}},
   "Items": [
      { ... }
   ],
   "LanguageConfiguration": {
      "FormLanguage": "{{string}}"
   },
   "ReviewConfiguration": {
      "EligibilityDays": {{number}},
      "ReviewNotificationRecipients": [
         {
            "Type": "{{string}}",
            "Value": {
               "UserId": "{{string}}"
            }
         }
      ]
   },
   "ScoringStrategy": {
      "Mode": "{{string}}",
      "ScoreThresholds": [
         {
            "MaxScorePercentage": {{number}},
            "MinScorePercentage": {{number}},
            "PerformanceCategory": "{{string}}"
         }
      ],
      "Status": "{{string}}"
   },
   "TargetConfiguration": {
      "ContactInteractionType": "{{string}}"
   },
   "Title": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateEvaluationForm_RequestParameters"></a>

The request uses the following URI parameters.

 ** [EvaluationFormId](#API_UpdateEvaluationForm_RequestSyntax) **   <a name="connect-UpdateEvaluationForm-request-uri-EvaluationFormId"></a>
The unique identifier for the evaluation form.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** [InstanceId](#API_UpdateEvaluationForm_RequestSyntax) **   <a name="connect-UpdateEvaluationForm-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_UpdateEvaluationForm_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AsDraft](#API_UpdateEvaluationForm_RequestSyntax) **   <a name="connect-UpdateEvaluationForm-request-AsDraft"></a>
A boolean flag indicating whether to update evaluation form to draft state.
Type: Boolean
Required: No

 ** [AutoEvaluationConfiguration](#API_UpdateEvaluationForm_RequestSyntax) **   <a name="connect-UpdateEvaluationForm-request-AutoEvaluationConfiguration"></a>
Whether automated evaluations are enabled.
Type: [EvaluationFormAutoEvaluationConfiguration](API_EvaluationFormAutoEvaluationConfiguration.md) object
Required: No

 ** [ClientToken](#API_UpdateEvaluationForm_RequestSyntax) **   <a name="connect-UpdateEvaluationForm-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** [CreateNewVersion](#API_UpdateEvaluationForm_RequestSyntax) **   <a name="connect-UpdateEvaluationForm-request-CreateNewVersion"></a>
A flag indicating whether the operation must create a new version.
Type: Boolean
Required: No

 ** [Description](#API_UpdateEvaluationForm_RequestSyntax) **   <a name="connect-UpdateEvaluationForm-request-Description"></a>
The description of the evaluation form.
Type: String
Required: No

 ** [EvaluationFormVersion](#API_UpdateEvaluationForm_RequestSyntax) **   <a name="connect-UpdateEvaluationForm-request-EvaluationFormVersion"></a>
A version of the evaluation form to update.
Type: Integer
Required: Yes

 ** [Items](#API_UpdateEvaluationForm_RequestSyntax) **   <a name="connect-UpdateEvaluationForm-request-Items"></a>
Items that are part of the evaluation form. The total number of sections and questions must not exceed 100 each. Questions must be contained in a section.
Type: Array of [EvaluationFormItem](API_EvaluationFormItem.md) objects
Required: Yes

 ** [LanguageConfiguration](#API_UpdateEvaluationForm_RequestSyntax) **   <a name="connect-UpdateEvaluationForm-request-LanguageConfiguration"></a>
Configuration for language settings of the evaluation form.
Type: [EvaluationFormLanguageConfiguration](API_EvaluationFormLanguageConfiguration.md) object
Required: No

 ** [ReviewConfiguration](#API_UpdateEvaluationForm_RequestSyntax) **   <a name="connect-UpdateEvaluationForm-request-ReviewConfiguration"></a>
Configuration for evaluation review settings of the evaluation form.
Type: [EvaluationReviewConfiguration](API_EvaluationReviewConfiguration.md) object
Required: No

 ** [ScoringStrategy](#API_UpdateEvaluationForm_RequestSyntax) **   <a name="connect-UpdateEvaluationForm-request-ScoringStrategy"></a>
A scoring strategy of the evaluation form.
Type: [EvaluationFormScoringStrategy](API_EvaluationFormScoringStrategy.md) object
Required: No

 ** [TargetConfiguration](#API_UpdateEvaluationForm_RequestSyntax) **   <a name="connect-UpdateEvaluationForm-request-TargetConfiguration"></a>
Configuration that specifies the target for the evaluation form.
Type: [EvaluationFormTargetConfiguration](API_EvaluationFormTargetConfiguration.md) object
Required: No

 ** [Title](#API_UpdateEvaluationForm_RequestSyntax) **   <a name="connect-UpdateEvaluationForm-request-Title"></a>
A title of the evaluation form.
Type: String
Required: Yes

## Response Syntax
<a name="API_UpdateEvaluationForm_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "EvaluationFormArn": "string",
   "EvaluationFormId": "string",
   "EvaluationFormVersion": number
}
```

## Response Elements
<a name="API_UpdateEvaluationForm_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EvaluationFormArn](#API_UpdateEvaluationForm_ResponseSyntax) **   <a name="connect-UpdateEvaluationForm-response-EvaluationFormArn"></a>
The Amazon Resource Name (ARN) for the contact evaluation resource.
Type: String

 ** [EvaluationFormId](#API_UpdateEvaluationForm_ResponseSyntax) **   <a name="connect-UpdateEvaluationForm-response-EvaluationFormId"></a>
The unique identifier for the evaluation form.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.

 ** [EvaluationFormVersion](#API_UpdateEvaluationForm_ResponseSyntax) **   <a name="connect-UpdateEvaluationForm-response-EvaluationFormVersion"></a>
The version of the updated evaluation form resource.
Type: Integer

## Errors
<a name="API_UpdateEvaluationForm_Errors"></a>

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

 ** ResourceConflictException **
A resource already has that name.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The service quota has been exceeded.
 ** Reason **
The reason for the exception.
HTTP Status Code: 402

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## Examples
<a name="API_UpdateEvaluationForm_Examples"></a>

### Example
<a name="API_UpdateEvaluationForm_Example_1"></a>

The following example updates version 2 of an evaluation form. This results in another, new version.

#### Sample Request
<a name="API_UpdateEvaluationForm_Example_1_Request"></a>

```
{
   "InstanceId": "[instance_id]",
   "EvaluationFormId": "[evaluation_form_id]",
   "EvaluationFormVersion": 2,
   "CreateNewVersion": true,
   "Title": "form-title",
   "Description": "form-description",
   "ScoringStrategy": {
      "Mode": "SECTION_ONLY",
      "Status": "ENABLED"
   },
   "Items": [
      {
         "Section": {
            "Title": "section-title-1",
            "RefId": "section-1",
            "Instructions": "section-instruction-1",
            "Weight": 50,
            "Items": [
               {
                  "Question": {
                     "Title": "question-title-11",
                     "RefId": "question-1-111",
                     "Instructions": "question-instructions",
                     "NotApplicableEnabled": false,
                     "QuestionType": "TEXT"
                  }
               },
               {
                  "Question": {
                     "Title": "question-title-12",
                     "RefId": "question-1-222",
                     "QuestionType": "SINGLESELECT",
                     "NotApplicableEnabled": false,
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
            ]
         }
      },
      {
         "Section": {
            "Title": "section-title-2",
            "RefId": "section-2",
            "Instructions": "section-instruction-2",
            "Weight": 50,
            "Items": [
               {
                  "Question": {
                     "Title": "question-title-21",
                     "RefId": "question-2-1",
                     "QuestionType": "TEXT",
                     "NotApplicableEnabled": true
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
            ]
         }
      }
   ]
}
```

#### Sample Response
<a name="API_UpdateEvaluationForm_Example_1_Response"></a>

```
{
   "EvaluationFormId": "[evaluation_form_id]",
   "EvaluationFormArn": "arn:aws:connect:[aws_region_code]:[account_id]:instance/[instance_id]/evaluation-form/[evaluation_form_id]",
   "EvaluationFormVersion": 2
}
```

## See Also
<a name="API_UpdateEvaluationForm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/UpdateEvaluationForm)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/UpdateEvaluationForm)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UpdateEvaluationForm)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/UpdateEvaluationForm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UpdateEvaluationForm)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/UpdateEvaluationForm)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/UpdateEvaluationForm)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/UpdateEvaluationForm)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/UpdateEvaluationForm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UpdateEvaluationForm)
