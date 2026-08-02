---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListLensReviewImprovements.html
---

# ListLensReviewImprovements
<a name="API_ListLensReviewImprovements"></a>

List the improvements of a particular lens review.

## Request Syntax
<a name="API_ListLensReviewImprovements_RequestSyntax"></a>

```
GET /workloads/{{WorkloadId}}/lensReviews/{{LensAlias}}/improvements?MaxResults={{MaxResults}}&MilestoneNumber={{MilestoneNumber}}&NextToken={{NextToken}}&PillarId={{PillarId}}&QuestionPriority={{QuestionPriority}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListLensReviewImprovements_RequestParameters"></a>

The request uses the following URI parameters.

 ** [LensAlias](#API_ListLensReviewImprovements_RequestSyntax) **   <a name="wellarchitected-ListLensReviewImprovements-request-uri-LensAlias"></a>
The alias of the lens.
For AWS official lenses, this is either the lens alias, such as `serverless`, or the lens ARN, such as `arn:aws:wellarchitected:us-east-1::lens/serverless`. Note that some operations (such as ExportLens and CreateLensShare) are not permitted on AWS official lenses.
For custom lenses, this is the lens ARN, such as `arn:aws:wellarchitected:us-west-2:123456789012:lens/0123456789abcdef01234567890abcdef`.
Each lens is identified by its [LensSummary:LensAlias](API_LensSummary.md#wellarchitected-Type-LensSummary-LensAlias).
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [MaxResults](#API_ListLensReviewImprovements_RequestSyntax) **   <a name="wellarchitected-ListLensReviewImprovements-request-uri-MaxResults"></a>
The maximum number of results to return for this request.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [MilestoneNumber](#API_ListLensReviewImprovements_RequestSyntax) **   <a name="wellarchitected-ListLensReviewImprovements-request-uri-MilestoneNumber"></a>
The milestone number.
A workload can have a maximum of 100 milestones.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListLensReviewImprovements_RequestSyntax) **   <a name="wellarchitected-ListLensReviewImprovements-request-uri-NextToken"></a>
The token to use to retrieve the next set of results.

 ** [PillarId](#API_ListLensReviewImprovements_RequestSyntax) **   <a name="wellarchitected-ListLensReviewImprovements-request-uri-PillarId"></a>
The ID used to identify a pillar, for example, `security`.
A pillar is identified by its [PillarReviewSummary:PillarId](API_PillarReviewSummary.md#wellarchitected-Type-PillarReviewSummary-PillarId).
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [QuestionPriority](#API_ListLensReviewImprovements_RequestSyntax) **   <a name="wellarchitected-ListLensReviewImprovements-request-uri-QuestionPriority"></a>
The priority of the question.
Valid Values: `PRIORITIZED | NONE`

 ** [WorkloadId](#API_ListLensReviewImprovements_RequestSyntax) **   <a name="wellarchitected-ListLensReviewImprovements-request-uri-WorkloadId"></a>
The ID assigned to the workload. This ID is unique within an AWS Region.
Length Constraints: Fixed length of 32.
Pattern: `[0-9a-f]{32}`
Required: Yes

## Request Body
<a name="API_ListLensReviewImprovements_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListLensReviewImprovements_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ImprovementSummaries": [
      {
         "ImprovementPlans": [
            {
               "ChoiceId": "string",
               "DisplayText": "string",
               "ImprovementPlanUrl": "string"
            }
         ],
         "ImprovementPlanUrl": "string",
         "JiraConfiguration": {
            "JiraIssueUrl": "string",
            "LastSyncedTime": number
         },
         "PillarId": "string",
         "QuestionId": "string",
         "QuestionTitle": "string",
         "Risk": "string"
      }
   ],
   "LensAlias": "string",
   "LensArn": "string",
   "MilestoneNumber": number,
   "NextToken": "string",
   "WorkloadId": "string"
}
```

## Response Elements
<a name="API_ListLensReviewImprovements_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ImprovementSummaries](#API_ListLensReviewImprovements_ResponseSyntax) **   <a name="wellarchitected-ListLensReviewImprovements-response-ImprovementSummaries"></a>
List of improvement summaries of lens review in a workload.
Type: Array of [ImprovementSummary](API_ImprovementSummary.md) objects

 ** [LensAlias](#API_ListLensReviewImprovements_ResponseSyntax) **   <a name="wellarchitected-ListLensReviewImprovements-response-LensAlias"></a>
The alias of the lens.
For AWS official lenses, this is either the lens alias, such as `serverless`, or the lens ARN, such as `arn:aws:wellarchitected:us-east-1::lens/serverless`. Note that some operations (such as ExportLens and CreateLensShare) are not permitted on AWS official lenses.
For custom lenses, this is the lens ARN, such as `arn:aws:wellarchitected:us-west-2:123456789012:lens/0123456789abcdef01234567890abcdef`.
Each lens is identified by its [LensSummary:LensAlias](API_LensSummary.md#wellarchitected-Type-LensSummary-LensAlias).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [LensArn](#API_ListLensReviewImprovements_ResponseSyntax) **   <a name="wellarchitected-ListLensReviewImprovements-response-LensArn"></a>
The ARN for the lens.
Type: String

 ** [MilestoneNumber](#API_ListLensReviewImprovements_ResponseSyntax) **   <a name="wellarchitected-ListLensReviewImprovements-response-MilestoneNumber"></a>
The milestone number.
A workload can have a maximum of 100 milestones.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListLensReviewImprovements_ResponseSyntax) **   <a name="wellarchitected-ListLensReviewImprovements-response-NextToken"></a>
The token to use to retrieve the next set of results.
Type: String

 ** [WorkloadId](#API_ListLensReviewImprovements_ResponseSyntax) **   <a name="wellarchitected-ListLensReviewImprovements-response-WorkloadId"></a>
The ID assigned to the workload. This ID is unique within an AWS Region.
Type: String
Length Constraints: Fixed length of 32.
Pattern: `[0-9a-f]{32}`

## Errors
<a name="API_ListLensReviewImprovements_Errors"></a>

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
<a name="API_ListLensReviewImprovements_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/ListLensReviewImprovements)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/ListLensReviewImprovements)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/ListLensReviewImprovements)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/ListLensReviewImprovements)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/ListLensReviewImprovements)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/ListLensReviewImprovements)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/ListLensReviewImprovements)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/ListLensReviewImprovements)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/ListLensReviewImprovements)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/ListLensReviewImprovements)
