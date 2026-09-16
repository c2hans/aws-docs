---
source_url: https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListRecommendations.html
---

# ListRecommendations
<a name="API_ListRecommendations"></a>

**Note**
As of November 7, 2025, you cannot create new repository associations in Amazon CodeGuru Reviewer. To learn about services with capabilities similar to CodeGuru Reviewer, see [Amazon CodeGuru Reviewer availability change](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/codeguru-reviewer-availability-change.html).

Returns the list of all recommendations for a completed code review.

## Request Syntax
<a name="API_ListRecommendations_RequestSyntax"></a>

```
GET /codereviews/{{CodeReviewArn}}/Recommendations?MaxResults={{MaxResults}}&NextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListRecommendations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [CodeReviewArn](#API_ListRecommendations_RequestSyntax) **   <a name="reviewer-ListRecommendations-request-uri-CodeReviewArn"></a>
The Amazon Resource Name (ARN) of the [CodeReview](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReview.html) object.
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws:codeguru-reviewer:[^:\s]+:[\d]{12}:([a-z-]+|[a-z-]+:[\w-]+:[a-z-]+):[\w-]+$`
Required: Yes

 ** [MaxResults](#API_ListRecommendations_RequestSyntax) **   <a name="reviewer-ListRecommendations-request-uri-MaxResults"></a>
The maximum number of results that are returned per call. The default is 100.
Valid Range: Minimum value of 1. Maximum value of 300.

 ** [NextToken](#API_ListRecommendations_RequestSyntax) **   <a name="reviewer-ListRecommendations-request-uri-NextToken"></a>
Pagination token.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `\S+`

## Request Body
<a name="API_ListRecommendations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListRecommendations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "RecommendationSummaries": [
      {
         "ConfidenceScore": number,
         "Description": "string",
         "EndLine": number,
         "FilePath": "string",
         "RecommendationCategory": "string",
         "RecommendationId": "string",
         "RecommendationType": "string",
         "RecommenderId": "string",
         "RuleMetadata": {
            "LongDescription": "string",
            "RuleId": "string",
            "RuleName": "string",
            "RuleTags": [ "string" ],
            "ShortDescription": "string"
         },
         "Severity": "string",
         "StartLine": number
      }
   ]
}
```

## Response Elements
<a name="API_ListRecommendations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListRecommendations_ResponseSyntax) **   <a name="reviewer-ListRecommendations-response-NextToken"></a>
Pagination token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `\S+`

 ** [RecommendationSummaries](#API_ListRecommendations_ResponseSyntax) **   <a name="reviewer-ListRecommendations-response-RecommendationSummaries"></a>
List of recommendations for the requested code review.
Type: Array of [RecommendationSummary](API_RecommendationSummary.md) objects

## Errors
<a name="API_ListRecommendations_Errors"></a>

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
<a name="API_ListRecommendations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeguru-reviewer-2019-09-19/ListRecommendations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeguru-reviewer-2019-09-19/ListRecommendations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguru-reviewer-2019-09-19/ListRecommendations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeguru-reviewer-2019-09-19/ListRecommendations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguru-reviewer-2019-09-19/ListRecommendations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeguru-reviewer-2019-09-19/ListRecommendations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeguru-reviewer-2019-09-19/ListRecommendations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeguru-reviewer-2019-09-19/ListRecommendations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codeguru-reviewer-2019-09-19/ListRecommendations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguru-reviewer-2019-09-19/ListRecommendations)
