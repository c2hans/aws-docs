---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateReviewTemplateAnswer.html
---

# UpdateReviewTemplateAnswer
<a name="API_UpdateReviewTemplateAnswer"></a>

Update a review template answer.

## Request Syntax
<a name="API_UpdateReviewTemplateAnswer_RequestSyntax"></a>

```
PATCH /reviewTemplates/{{TemplateArn}}/lensReviews/{{LensAlias}}/answers/{{QuestionId}} HTTP/1.1
Content-type: application/json

{
   "ChoiceUpdates": {
      "{{string}}" : {
         "Notes": "{{string}}",
         "Reason": "{{string}}",
         "Status": "{{string}}"
      }
   },
   "IsApplicable": {{boolean}},
   "Notes": "{{string}}",
   "Reason": "{{string}}",
   "SelectedChoices": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_UpdateReviewTemplateAnswer_RequestParameters"></a>

The request uses the following URI parameters.

 ** [LensAlias](#API_UpdateReviewTemplateAnswer_RequestSyntax) **   <a name="wellarchitected-UpdateReviewTemplateAnswer-request-uri-LensAlias"></a>
The alias of the lens.
For AWS official lenses, this is either the lens alias, such as `serverless`, or the lens ARN, such as `arn:aws:wellarchitected:us-east-1::lens/serverless`. Note that some operations (such as ExportLens and CreateLensShare) are not permitted on AWS official lenses.
For custom lenses, this is the lens ARN, such as `arn:aws:wellarchitected:us-west-2:123456789012:lens/0123456789abcdef01234567890abcdef`.
Each lens is identified by its [LensSummary:LensAlias](API_LensSummary.md#wellarchitected-Type-LensSummary-LensAlias).
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [QuestionId](#API_UpdateReviewTemplateAnswer_RequestSyntax) **   <a name="wellarchitected-UpdateReviewTemplateAnswer-request-uri-QuestionId"></a>
The ID of the question.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [TemplateArn](#API_UpdateReviewTemplateAnswer_RequestSyntax) **   <a name="wellarchitected-UpdateReviewTemplateAnswer-request-uri-TemplateArn"></a>
The review template ARN.
Length Constraints: Minimum length of 50. Maximum length of 250.
Pattern: `arn:aws(-us-gov|-iso(-[a-z])?|-cn)?:wellarchitected:[a-z]{2}(-gov|-iso([a-z])?)?-[a-z]+-\d:\d{12}:(review-template)/[a-f0-9]{32}`
Required: Yes

## Request Body
<a name="API_UpdateReviewTemplateAnswer_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ChoiceUpdates](#API_UpdateReviewTemplateAnswer_RequestSyntax) **   <a name="wellarchitected-UpdateReviewTemplateAnswer-request-ChoiceUpdates"></a>
A list of choices to be updated.
Type: String to [ChoiceUpdate](API_ChoiceUpdate.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** [IsApplicable](#API_UpdateReviewTemplateAnswer_RequestSyntax) **   <a name="wellarchitected-UpdateReviewTemplateAnswer-request-IsApplicable"></a>
Defines whether this question is applicable to a lens review.
Type: Boolean
Required: No

 ** [Notes](#API_UpdateReviewTemplateAnswer_RequestSyntax) **   <a name="wellarchitected-UpdateReviewTemplateAnswer-request-Notes"></a>
The notes associated with the workload.
For a review template, these are the notes that will be associated with the workload when the template is applied.
Type: String
Length Constraints: Maximum length of 2084.
Required: No

 ** [Reason](#API_UpdateReviewTemplateAnswer_RequestSyntax) **   <a name="wellarchitected-UpdateReviewTemplateAnswer-request-Reason"></a>
The update reason.
Type: String
Valid Values: `OUT_OF_SCOPE | BUSINESS_PRIORITIES | ARCHITECTURE_CONSTRAINTS | OTHER | NONE`
Required: No

 ** [SelectedChoices](#API_UpdateReviewTemplateAnswer_RequestSyntax) **   <a name="wellarchitected-UpdateReviewTemplateAnswer-request-SelectedChoices"></a>
List of selected choice IDs in a question answer.
The values entered replace the previously selected choices.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## Response Syntax
<a name="API_UpdateReviewTemplateAnswer_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Answer": {
      "AnswerStatus": "string",
      "ChoiceAnswers": [
         {
            "ChoiceId": "string",
            "Notes": "string",
            "Reason": "string",
            "Status": "string"
         }
      ],
      "Choices": [
         {
            "AdditionalResources": [
               {
                  "Content": [
                     {
                        "DisplayText": "string",
                        "Url": "string"
                     }
                  ],
                  "Type": "string"
               }
            ],
            "ChoiceId": "string",
            "Description": "string",
            "HelpfulResource": {
               "DisplayText": "string",
               "Url": "string"
            },
            "ImprovementPlan": {
               "DisplayText": "string",
               "Url": "string"
            },
            "Title": "string"
         }
      ],
      "HelpfulResourceDisplayText": "string",
      "HelpfulResourceUrl": "string",
      "ImprovementPlanUrl": "string",
      "IsApplicable": boolean,
      "Notes": "string",
      "PillarId": "string",
      "QuestionDescription": "string",
      "QuestionId": "string",
      "QuestionTitle": "string",
      "Reason": "string",
      "SelectedChoices": [ "string" ]
   },
   "LensAlias": "string",
   "TemplateArn": "string"
}
```

## Response Elements
<a name="API_UpdateReviewTemplateAnswer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Answer](#API_UpdateReviewTemplateAnswer_ResponseSyntax) **   <a name="wellarchitected-UpdateReviewTemplateAnswer-response-Answer"></a>
An answer of the question.
Type: [ReviewTemplateAnswer](API_ReviewTemplateAnswer.md) object

 ** [LensAlias](#API_UpdateReviewTemplateAnswer_ResponseSyntax) **   <a name="wellarchitected-UpdateReviewTemplateAnswer-response-LensAlias"></a>
The alias of the lens.
For AWS official lenses, this is either the lens alias, such as `serverless`, or the lens ARN, such as `arn:aws:wellarchitected:us-east-1::lens/serverless`. Note that some operations (such as ExportLens and CreateLensShare) are not permitted on AWS official lenses.
For custom lenses, this is the lens ARN, such as `arn:aws:wellarchitected:us-west-2:123456789012:lens/0123456789abcdef01234567890abcdef`.
Each lens is identified by its [LensSummary:LensAlias](API_LensSummary.md#wellarchitected-Type-LensSummary-LensAlias).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [TemplateArn](#API_UpdateReviewTemplateAnswer_ResponseSyntax) **   <a name="wellarchitected-UpdateReviewTemplateAnswer-response-TemplateArn"></a>
The review template ARN.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 250.
Pattern: `arn:aws(-us-gov|-iso(-[a-z])?|-cn)?:wellarchitected:[a-z]{2}(-gov|-iso([a-z])?)?-[a-z]+-\d:\d{12}:(review-template)/[a-f0-9]{32}`

## Errors
<a name="API_UpdateReviewTemplateAnswer_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
 ** Message **
Description of the error.
HTTP Status Code: 403

 ** ConflictException **
The resource has already been processed, was deleted, or is too large.
 ** Message **
Description of the error.
 ** ResourceId **
Identifier of the resource affected.
 ** ResourceType **
Type of the resource affected.
HTTP Status Code: 409

 ** InternalServerException **
There is a problem with the AWS Well-Architected Tool API service.
 ** Message **
Description of the error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource was not found.
 ** Message **
Description of the error.
 ** ResourceId **
Identifier of the resource affected.
 ** ResourceType **
Type of the resource affected.
HTTP Status Code: 404

 ** ThrottlingException **
Request was denied due to request throttling.
 ** Message **
Description of the error.
 ** QuotaCode **
Service Quotas requirement to identify originating quota.
 ** ServiceCode **
Service Quotas requirement to identify originating service.
HTTP Status Code: 429

 ** ValidationException **
The user input is not valid.
 ** Fields **
The fields that caused the error, if applicable.
 ** Message **
Description of the error.
 ** Reason **
The reason why the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_UpdateReviewTemplateAnswer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/UpdateReviewTemplateAnswer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/UpdateReviewTemplateAnswer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/UpdateReviewTemplateAnswer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/UpdateReviewTemplateAnswer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/UpdateReviewTemplateAnswer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/UpdateReviewTemplateAnswer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/UpdateReviewTemplateAnswer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/UpdateReviewTemplateAnswer)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/UpdateReviewTemplateAnswer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/UpdateReviewTemplateAnswer)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected Tool. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
