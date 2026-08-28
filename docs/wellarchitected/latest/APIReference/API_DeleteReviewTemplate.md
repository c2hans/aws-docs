---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_DeleteReviewTemplate.html
---

# DeleteReviewTemplate
<a name="API_DeleteReviewTemplate"></a>

Delete a review template.

Only the owner of a review template can delete it.

After the review template is deleted, AWS accounts, users, organizations, and organizational units (OUs) that you shared the review template with will no longer be able to apply it to new workloads.

## Request Syntax
<a name="API_DeleteReviewTemplate_RequestSyntax"></a>

```
DELETE /reviewTemplates/{{TemplateArn}}?ClientRequestToken={{ClientRequestToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteReviewTemplate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ClientRequestToken](#API_DeleteReviewTemplate_RequestSyntax) **   <a name="wellarchitected-DeleteReviewTemplate-request-uri-ClientRequestToken"></a>
A unique case-sensitive string used to ensure that this request is idempotent (executes only once).
You should not reuse the same token for other requests. If you retry a request with the same client request token and the same parameters after the original request has completed successfully, the result of the original request is returned.
This token is listed as required, however, if you do not specify it, the AWS SDKs automatically generate one for you. If you are not using the AWS SDK or the AWS CLI, you must provide this token or the request will fail.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[\x00-\x7F]*$`
Required: Yes

 ** [TemplateArn](#API_DeleteReviewTemplate_RequestSyntax) **   <a name="wellarchitected-DeleteReviewTemplate-request-uri-TemplateArn"></a>
The review template ARN.
Length Constraints: Minimum length of 50. Maximum length of 250.
Pattern: `arn:aws(-us-gov|-iso(-[a-z])?|-cn)?:wellarchitected:[a-z]{2}(-gov|-iso([a-z])?)?-[a-z]+-\d:\d{12}:(review-template)/[a-f0-9]{32}`
Required: Yes

## Request Body
<a name="API_DeleteReviewTemplate_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteReviewTemplate_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteReviewTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteReviewTemplate_Errors"></a>

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
<a name="API_DeleteReviewTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/DeleteReviewTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/DeleteReviewTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/DeleteReviewTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/DeleteReviewTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/DeleteReviewTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/DeleteReviewTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/DeleteReviewTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/DeleteReviewTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/DeleteReviewTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/DeleteReviewTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected Tool. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
