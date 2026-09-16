---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetAnswer.html
---

# GetAnswer
<a name="API_GetAnswer"></a>

Get the answer to a specific question in a workload review.

## Request Syntax
<a name="API_GetAnswer_RequestSyntax"></a>

```
GET /workloads/{{WorkloadId}}/lensReviews/{{LensAlias}}/answers/{{QuestionId}}?MilestoneNumber={{MilestoneNumber}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAnswer_RequestParameters"></a>

The request uses the following URI parameters.

 ** [LensAlias](#API_GetAnswer_RequestSyntax) **   <a name="wellarchitected-GetAnswer-request-uri-LensAlias"></a>
The alias of the lens.
For AWS official lenses, this is either the lens alias, such as `serverless`, or the lens ARN, such as `arn:aws:wellarchitected:us-east-1::lens/serverless`. Note that some operations (such as ExportLens and CreateLensShare) are not permitted on AWS official lenses.
For custom lenses, this is the lens ARN, such as `arn:aws:wellarchitected:us-west-2:123456789012:lens/0123456789abcdef01234567890abcdef`.
Each lens is identified by its [LensSummary:LensAlias](API_LensSummary.md#wellarchitected-Type-LensSummary-LensAlias).
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [MilestoneNumber](#API_GetAnswer_RequestSyntax) **   <a name="wellarchitected-GetAnswer-request-uri-MilestoneNumber"></a>
The milestone number.
A workload can have a maximum of 100 milestones.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [QuestionId](#API_GetAnswer_RequestSyntax) **   <a name="wellarchitected-GetAnswer-request-uri-QuestionId"></a>
The ID of the question.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [WorkloadId](#API_GetAnswer_RequestSyntax) **   <a name="wellarchitected-GetAnswer-request-uri-WorkloadId"></a>
The ID assigned to the workload. This ID is unique within an AWS Region.
Length Constraints: Fixed length of 32.
Pattern: `[0-9a-f]{32}`
Required: Yes

## Request Body
<a name="API_GetAnswer_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAnswer_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Answer": {
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
      "JiraConfiguration": {
         "JiraIssueUrl": "string",
         "LastSyncedTime": number
      },
      "Notes": "string",
      "PillarId": "string",
      "QuestionDescription": "string",
      "QuestionId": "string",
      "QuestionTitle": "string",
      "Reason": "string",
      "Risk": "string",
      "SelectedChoices": [ "string" ]
   },
   "LensAlias": "string",
   "LensArn": "string",
   "MilestoneNumber": number,
   "WorkloadId": "string"
}
```

## Response Elements
<a name="API_GetAnswer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Answer](#API_GetAnswer_ResponseSyntax) **   <a name="wellarchitected-GetAnswer-response-Answer"></a>
An answer of the question.
Type: [Answer](API_Answer.md) object

 ** [LensAlias](#API_GetAnswer_ResponseSyntax) **   <a name="wellarchitected-GetAnswer-response-LensAlias"></a>
The alias of the lens.
For AWS official lenses, this is either the lens alias, such as `serverless`, or the lens ARN, such as `arn:aws:wellarchitected:us-east-1::lens/serverless`. Note that some operations (such as ExportLens and CreateLensShare) are not permitted on AWS official lenses.
For custom lenses, this is the lens ARN, such as `arn:aws:wellarchitected:us-west-2:123456789012:lens/0123456789abcdef01234567890abcdef`.
Each lens is identified by its [LensSummary:LensAlias](API_LensSummary.md#wellarchitected-Type-LensSummary-LensAlias).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [LensArn](#API_GetAnswer_ResponseSyntax) **   <a name="wellarchitected-GetAnswer-response-LensArn"></a>
The ARN for the lens.
Type: String

 ** [MilestoneNumber](#API_GetAnswer_ResponseSyntax) **   <a name="wellarchitected-GetAnswer-response-MilestoneNumber"></a>
The milestone number.
A workload can have a maximum of 100 milestones.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [WorkloadId](#API_GetAnswer_ResponseSyntax) **   <a name="wellarchitected-GetAnswer-response-WorkloadId"></a>
The ID assigned to the workload. This ID is unique within an AWS Region.
Type: String
Length Constraints: Fixed length of 32.
Pattern: `[0-9a-f]{32}`

## Errors
<a name="API_GetAnswer_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
 ** Message **
Description of the error.
HTTP Status Code: 403

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
<a name="API_GetAnswer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/GetAnswer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/GetAnswer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/GetAnswer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/GetAnswer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/GetAnswer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/GetAnswer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/GetAnswer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/GetAnswer)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/GetAnswer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/GetAnswer)
