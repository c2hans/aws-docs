---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateLensReview.html
---

# UpdateLensReview
<a name="API_UpdateLensReview"></a>

Update lens review for a particular workload.

## Request Syntax
<a name="API_UpdateLensReview_RequestSyntax"></a>

```
PATCH /workloads/{{WorkloadId}}/lensReviews/{{LensAlias}} HTTP/1.1
Content-type: application/json

{
   "JiraConfiguration": {
      "SelectedPillars": [
         {
            "PillarId": "{{string}}",
            "SelectedQuestionIds": [ "{{string}}" ]
         }
      ]
   },
   "LensNotes": "{{string}}",
   "PillarNotes": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateLensReview_RequestParameters"></a>

The request uses the following URI parameters.

 ** [LensAlias](#API_UpdateLensReview_RequestSyntax) **   <a name="wellarchitected-UpdateLensReview-request-uri-LensAlias"></a>
The alias of the lens.
For AWS official lenses, this is either the lens alias, such as `serverless`, or the lens ARN, such as `arn:aws:wellarchitected:us-east-1::lens/serverless`. Note that some operations (such as ExportLens and CreateLensShare) are not permitted on AWS official lenses.
For custom lenses, this is the lens ARN, such as `arn:aws:wellarchitected:us-west-2:123456789012:lens/0123456789abcdef01234567890abcdef`.
Each lens is identified by its [LensSummary:LensAlias](API_LensSummary.md#wellarchitected-Type-LensSummary-LensAlias).
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [WorkloadId](#API_UpdateLensReview_RequestSyntax) **   <a name="wellarchitected-UpdateLensReview-request-uri-WorkloadId"></a>
The ID assigned to the workload. This ID is unique within an AWS Region.
Length Constraints: Fixed length of 32.
Pattern: `[0-9a-f]{32}`
Required: Yes

## Request Body
<a name="API_UpdateLensReview_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [JiraConfiguration](#API_UpdateLensReview_RequestSyntax) **   <a name="wellarchitected-UpdateLensReview-request-JiraConfiguration"></a>
Configuration of the Jira integration.
Type: [JiraSelectedQuestionConfiguration](API_JiraSelectedQuestionConfiguration.md) object
Required: No

 ** [LensNotes](#API_UpdateLensReview_RequestSyntax) **   <a name="wellarchitected-UpdateLensReview-request-LensNotes"></a>
The notes associated with the workload.
For a review template, these are the notes that will be associated with the workload when the template is applied.
Type: String
Length Constraints: Maximum length of 2084.
Required: No

 ** [PillarNotes](#API_UpdateLensReview_RequestSyntax) **   <a name="wellarchitected-UpdateLensReview-request-PillarNotes"></a>
List of pillar notes of a lens review in a workload.
For a review template, these are the notes that will be associated with the workload when the template is applied.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Value Length Constraints: Maximum length of 2084.
Required: No

## Response Syntax
<a name="API_UpdateLensReview_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "LensReview": {
      "JiraConfiguration": {
         "SelectedPillars": [
            {
               "PillarId": "string",
               "SelectedQuestionIds": [ "string" ]
            }
         ]
      },
      "LensAlias": "string",
      "LensArn": "string",
      "LensName": "string",
      "LensStatus": "string",
      "LensVersion": "string",
      "NextToken": "string",
      "Notes": "string",
      "PillarReviewSummaries": [
         {
            "Notes": "string",
            "PillarId": "string",
            "PillarName": "string",
            "PrioritizedRiskCounts": {
               "string" : number
            },
            "RiskCounts": {
               "string" : number
            }
         }
      ],
      "PrioritizedRiskCounts": {
         "string" : number
      },
      "Profiles": [
         {
            "ProfileArn": "string",
            "ProfileVersion": "string"
         }
      ],
      "RiskCounts": {
         "string" : number
      },
      "UpdatedAt": number
   },
   "WorkloadId": "string"
}
```

## Response Elements
<a name="API_UpdateLensReview_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LensReview](#API_UpdateLensReview_ResponseSyntax) **   <a name="wellarchitected-UpdateLensReview-response-LensReview"></a>
A lens review of a question.
Type: [LensReview](API_LensReview.md) object

 ** [WorkloadId](#API_UpdateLensReview_ResponseSyntax) **   <a name="wellarchitected-UpdateLensReview-response-WorkloadId"></a>
The ID assigned to the workload. This ID is unique within an AWS Region.
Type: String
Length Constraints: Fixed length of 32.
Pattern: `[0-9a-f]{32}`

## Errors
<a name="API_UpdateLensReview_Errors"></a>

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
<a name="API_UpdateLensReview_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/UpdateLensReview)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/UpdateLensReview)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/UpdateLensReview)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/UpdateLensReview)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/UpdateLensReview)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/UpdateLensReview)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/UpdateLensReview)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/UpdateLensReview)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/UpdateLensReview)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/UpdateLensReview)
