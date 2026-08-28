---
source_url: https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_PutRecommendationFeedback.html
---

# PutRecommendationFeedback
<a name="API_PutRecommendationFeedback"></a>

**Note**
As of November 7, 2025, you cannot create new repository associations in Amazon CodeGuru Reviewer. To learn about services with capabilities similar to CodeGuru Reviewer, see [Amazon CodeGuru Reviewer availability change](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/codeguru-reviewer-availability-change.html).

Stores customer feedback for a CodeGuru Reviewer recommendation. When this API is called again with different reactions the previous feedback is overwritten.

## Request Syntax
<a name="API_PutRecommendationFeedback_RequestSyntax"></a>

```
PUT /feedback HTTP/1.1
Content-type: application/json

{
   "CodeReviewArn": "{{string}}",
   "Reactions": [ "{{string}}" ],
   "RecommendationId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutRecommendationFeedback_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_PutRecommendationFeedback_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CodeReviewArn](#API_PutRecommendationFeedback_RequestSyntax) **   <a name="reviewer-PutRecommendationFeedback-request-CodeReviewArn"></a>
The Amazon Resource Name (ARN) of the [CodeReview](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReview.html) object.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws:codeguru-reviewer:[^:\s]+:[\d]{12}:([a-z-]+|[a-z-]+:[\w-]+:[a-z-]+):[\w-]+$`
Required: Yes

 ** [Reactions](#API_PutRecommendationFeedback_RequestSyntax) **   <a name="reviewer-PutRecommendationFeedback-request-Reactions"></a>
List for storing reactions. Reactions are utf-8 text code for emojis. If you send an empty list it clears all your feedback.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Valid Values: `ThumbsUp | ThumbsDown`
Required: Yes

 ** [RecommendationId](#API_PutRecommendationFeedback_RequestSyntax) **   <a name="reviewer-PutRecommendationFeedback-request-RecommendationId"></a>
The recommendation ID that can be used to track the provided recommendations and then to collect the feedback.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Response Syntax
<a name="API_PutRecommendationFeedback_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutRecommendationFeedback_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutRecommendationFeedback_Errors"></a>

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
<a name="API_PutRecommendationFeedback_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeguru-reviewer-2019-09-19/PutRecommendationFeedback)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeguru-reviewer-2019-09-19/PutRecommendationFeedback)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguru-reviewer-2019-09-19/PutRecommendationFeedback)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeguru-reviewer-2019-09-19/PutRecommendationFeedback)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguru-reviewer-2019-09-19/PutRecommendationFeedback)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeguru-reviewer-2019-09-19/PutRecommendationFeedback)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeguru-reviewer-2019-09-19/PutRecommendationFeedback)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeguru-reviewer-2019-09-19/PutRecommendationFeedback)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codeguru-reviewer-2019-09-19/PutRecommendationFeedback)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguru-reviewer-2019-09-19/PutRecommendationFeedback)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeGuru Reviewer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeguru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
