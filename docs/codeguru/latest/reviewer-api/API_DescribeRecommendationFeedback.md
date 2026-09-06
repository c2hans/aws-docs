---
source_url: https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_DescribeRecommendationFeedback.html
---

# DescribeRecommendationFeedback
<a name="API_DescribeRecommendationFeedback"></a>

**Note**
As of November 7, 2025, you cannot create new repository associations in Amazon CodeGuru Reviewer. To learn about services with capabilities similar to CodeGuru Reviewer, see [Amazon CodeGuru Reviewer availability change](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/codeguru-reviewer-availability-change.html).

Describes the customer feedback for a CodeGuru Reviewer recommendation.

## Request Syntax
<a name="API_DescribeRecommendationFeedback_RequestSyntax"></a>

```
GET /feedback/{{CodeReviewArn}}?RecommendationId={{RecommendationId}}&UserId={{UserId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeRecommendationFeedback_RequestParameters"></a>

The request uses the following URI parameters.

 ** [CodeReviewArn](#API_DescribeRecommendationFeedback_RequestSyntax) **   <a name="reviewer-DescribeRecommendationFeedback-request-uri-CodeReviewArn"></a>
The Amazon Resource Name (ARN) of the [CodeReview](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReview.html) object.
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws:codeguru-reviewer:[^:\s]+:[\d]{12}:([a-z-]+|[a-z-]+:[\w-]+:[a-z-]+):[\w-]+$`
Required: Yes

 ** [RecommendationId](#API_DescribeRecommendationFeedback_RequestSyntax) **   <a name="reviewer-DescribeRecommendationFeedback-request-uri-RecommendationId"></a>
The recommendation ID that can be used to track the provided recommendations and then to collect the feedback.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [UserId](#API_DescribeRecommendationFeedback_RequestSyntax) **   <a name="reviewer-DescribeRecommendationFeedback-request-uri-UserId"></a>
Optional parameter to describe the feedback for a given user. If this is not supplied, it defaults to the user making the request.
 The `UserId` is an IAM principal that can be specified as an AWS account ID or an Amazon Resource Name (ARN). For more information, see [ Specifying a Principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#Principal_specifying) in the * AWS Identity and Access Management User Guide*.
Length Constraints: Minimum length of 1. Maximum length of 256.

## Request Body
<a name="API_DescribeRecommendationFeedback_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeRecommendationFeedback_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "RecommendationFeedback": {
      "CodeReviewArn": "string",
      "CreatedTimeStamp": number,
      "LastUpdatedTimeStamp": number,
      "Reactions": [ "string" ],
      "RecommendationId": "string",
      "UserId": "string"
   }
}
```

## Response Elements
<a name="API_DescribeRecommendationFeedback_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RecommendationFeedback](#API_DescribeRecommendationFeedback_ResponseSyntax) **   <a name="reviewer-DescribeRecommendationFeedback-response-RecommendationFeedback"></a>
The recommendation feedback given by the user.
Type: [RecommendationFeedback](API_RecommendationFeedback.md) object

## Errors
<a name="API_DescribeRecommendationFeedback_Errors"></a>

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
<a name="API_DescribeRecommendationFeedback_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeguru-reviewer-2019-09-19/DescribeRecommendationFeedback)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeguru-reviewer-2019-09-19/DescribeRecommendationFeedback)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguru-reviewer-2019-09-19/DescribeRecommendationFeedback)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeguru-reviewer-2019-09-19/DescribeRecommendationFeedback)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguru-reviewer-2019-09-19/DescribeRecommendationFeedback)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeguru-reviewer-2019-09-19/DescribeRecommendationFeedback)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeguru-reviewer-2019-09-19/DescribeRecommendationFeedback)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeguru-reviewer-2019-09-19/DescribeRecommendationFeedback)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codeguru-reviewer-2019-09-19/DescribeRecommendationFeedback)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguru-reviewer-2019-09-19/DescribeRecommendationFeedback)
