---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpgradeReviewTemplateLensReview.html
---

# UpgradeReviewTemplateLensReview
<a name="API_UpgradeReviewTemplateLensReview"></a>

Upgrade the lens review of a review template.

## Request Syntax
<a name="API_UpgradeReviewTemplateLensReview_RequestSyntax"></a>

```
PUT /reviewTemplates/{{TemplateArn}}/lensReviews/{{LensAlias}}/upgrade HTTP/1.1
Content-type: application/json

{
   "ClientRequestToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpgradeReviewTemplateLensReview_RequestParameters"></a>

The request uses the following URI parameters.

 ** [LensAlias](#API_UpgradeReviewTemplateLensReview_RequestSyntax) **   <a name="wellarchitected-UpgradeReviewTemplateLensReview-request-uri-LensAlias"></a>
The alias of the lens.
For AWS official lenses, this is either the lens alias, such as `serverless`, or the lens ARN, such as `arn:aws:wellarchitected:us-east-1::lens/serverless`. Note that some operations (such as ExportLens and CreateLensShare) are not permitted on AWS official lenses.
For custom lenses, this is the lens ARN, such as `arn:aws:wellarchitected:us-west-2:123456789012:lens/0123456789abcdef01234567890abcdef`.
Each lens is identified by its [LensSummary:LensAlias](API_LensSummary.md#wellarchitected-Type-LensSummary-LensAlias).
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [TemplateArn](#API_UpgradeReviewTemplateLensReview_RequestSyntax) **   <a name="wellarchitected-UpgradeReviewTemplateLensReview-request-uri-TemplateArn"></a>
The ARN of the review template.
Length Constraints: Minimum length of 50. Maximum length of 250.
Pattern: `arn:aws(-us-gov|-iso(-[a-z])?|-cn)?:wellarchitected:[a-z]{2}(-gov|-iso([a-z])?)?-[a-z]+-\d:\d{12}:(review-template)/[a-f0-9]{32}`
Required: Yes

## Request Body
<a name="API_UpgradeReviewTemplateLensReview_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_UpgradeReviewTemplateLensReview_RequestSyntax) **   <a name="wellarchitected-UpgradeReviewTemplateLensReview-request-ClientRequestToken"></a>
A unique case-sensitive string used to ensure that this request is idempotent (executes only once).
You should not reuse the same token for other requests. If you retry a request with the same client request token and the same parameters after the original request has completed successfully, the result of the original request is returned.
This token is listed as required, however, if you do not specify it, the AWS SDKs automatically generate one for you. If you are not using the AWS SDK or the AWS CLI, you must provide this token or the request will fail.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[\x00-\x7F]*$`
Required: No

## Response Syntax
<a name="API_UpgradeReviewTemplateLensReview_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpgradeReviewTemplateLensReview_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpgradeReviewTemplateLensReview_Errors"></a>

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
<a name="API_UpgradeReviewTemplateLensReview_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/UpgradeReviewTemplateLensReview)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/UpgradeReviewTemplateLensReview)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/UpgradeReviewTemplateLensReview)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/UpgradeReviewTemplateLensReview)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/UpgradeReviewTemplateLensReview)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/UpgradeReviewTemplateLensReview)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/UpgradeReviewTemplateLensReview)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/UpgradeReviewTemplateLensReview)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/UpgradeReviewTemplateLensReview)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/UpgradeReviewTemplateLensReview)
