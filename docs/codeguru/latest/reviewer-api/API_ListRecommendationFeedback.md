---
source_url: https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListRecommendationFeedback.html
---

# ListRecommendationFeedback
<a name="API_ListRecommendationFeedback"></a>

**Note**
As of November 7, 2025, you cannot create new repository associations in Amazon CodeGuru Reviewer. To learn about services with capabilities similar to CodeGuru Reviewer, see [Amazon CodeGuru Reviewer availability change](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/codeguru-reviewer-availability-change.html).

Returns a list of [RecommendationFeedbackSummary](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RecommendationFeedbackSummary.html) objects that contain customer recommendation feedback for all CodeGuru Reviewer users.

## Request Syntax
<a name="API_ListRecommendationFeedback_RequestSyntax"></a>

```
GET /feedback/{{CodeReviewArn}}/RecommendationFeedback?MaxResults={{MaxResults}}&NextToken={{NextToken}}&RecommendationIds={{RecommendationIds}}&UserIds={{UserIds}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListRecommendationFeedback_RequestParameters"></a>

The request uses the following URI parameters.

 ** [CodeReviewArn](#API_ListRecommendationFeedback_RequestSyntax) **   <a name="reviewer-ListRecommendationFeedback-request-uri-CodeReviewArn"></a>
The Amazon Resource Name (ARN) of the [CodeReview](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReview.html) object.
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws:codeguru-reviewer:[^:\s]+:[\d]{12}:([a-z-]+|[a-z-]+:[\w-]+:[a-z-]+):[\w-]+$`
Required: Yes

 ** [MaxResults](#API_ListRecommendationFeedback_RequestSyntax) **   <a name="reviewer-ListRecommendationFeedback-request-uri-MaxResults"></a>
The maximum number of results that are returned per call. The default is 100.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListRecommendationFeedback_RequestSyntax) **   <a name="reviewer-ListRecommendationFeedback-request-uri-NextToken"></a>
If `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `\S+`

 ** [RecommendationIds](#API_ListRecommendationFeedback_RequestSyntax) **   <a name="reviewer-ListRecommendationFeedback-request-uri-RecommendationIds"></a>
Used to query the recommendation feedback for a given recommendation.
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [UserIds](#API_ListRecommendationFeedback_RequestSyntax) **   <a name="reviewer-ListRecommendationFeedback-request-uri-UserIds"></a>
An AWS user's account ID or Amazon Resource Name (ARN). Use this ID to query the recommendation feedback for a code review from that user.
 The `UserId` is an IAM principal that can be specified as an AWS account ID or an Amazon Resource Name (ARN). For more information, see [ Specifying a Principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#Principal_specifying) in the * AWS Identity and Access Management User Guide*.
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 256.

## Request Body
<a name="API_ListRecommendationFeedback_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListRecommendationFeedback_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "RecommendationFeedbackSummaries": [
      {
         "Reactions": [ "string" ],
         "RecommendationId": "string",
         "UserId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListRecommendationFeedback_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListRecommendationFeedback_ResponseSyntax) **   <a name="reviewer-ListRecommendationFeedback-response-NextToken"></a>
If `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `\S+`

 ** [RecommendationFeedbackSummaries](#API_ListRecommendationFeedback_ResponseSyntax) **   <a name="reviewer-ListRecommendationFeedback-response-RecommendationFeedbackSummaries"></a>
Recommendation feedback summaries corresponding to the code review ARN.
Type: Array of [RecommendationFeedbackSummary](API_RecommendationFeedbackSummary.md) objects

## Errors
<a name="API_ListRecommendationFeedback_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The server encountered an internal error and is unable to complete the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
 The resource specified in the request was not found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the specified constraints.
HTTP Status Code: 400

## See Also
<a name="API_ListRecommendationFeedback_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeguru-reviewer-2019-09-19/ListRecommendationFeedback)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeguru-reviewer-2019-09-19/ListRecommendationFeedback)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguru-reviewer-2019-09-19/ListRecommendationFeedback)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeguru-reviewer-2019-09-19/ListRecommendationFeedback)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguru-reviewer-2019-09-19/ListRecommendationFeedback)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeguru-reviewer-2019-09-19/ListRecommendationFeedback)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeguru-reviewer-2019-09-19/ListRecommendationFeedback)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeguru-reviewer-2019-09-19/ListRecommendationFeedback)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codeguru-reviewer-2019-09-19/ListRecommendationFeedback)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguru-reviewer-2019-09-19/ListRecommendationFeedback)
