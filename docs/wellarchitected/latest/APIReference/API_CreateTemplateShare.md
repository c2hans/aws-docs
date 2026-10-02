---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CreateTemplateShare.html
---

# CreateTemplateShare
<a name="API_CreateTemplateShare"></a>

Create a review template share.

The owner of a review template can share it with other AWS accounts, users, an organization, and organizational units (OUs) in the same AWS Region.

 Shared access to a review template is not removed until the review template share invitation is deleted.

If you share a review template with an organization or OU, all accounts in the organization or OU are granted access to the review template.

**Note**
 **Disclaimer**
By sharing your review template with other AWS accounts, you acknowledge that AWS will make your review template available to those other accounts.

## Request Syntax
<a name="API_CreateTemplateShare_RequestSyntax"></a>

```
POST /templates/shares/{{TemplateArn}} HTTP/1.1
Content-type: application/json

{
   "ClientRequestToken": "{{string}}",
   "SharedWith": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateTemplateShare_RequestParameters"></a>

The request uses the following URI parameters.

 ** [TemplateArn](#API_CreateTemplateShare_RequestSyntax) **   <a name="wellarchitected-CreateTemplateShare-request-uri-TemplateArn"></a>
The review template ARN.
Length Constraints: Minimum length of 50. Maximum length of 250.
Pattern: `arn:aws(-us-gov|-iso(-[a-z])?|-cn)?:wellarchitected:[a-z]{2}(-gov|-iso([a-z])?)?-[a-z]+-\d:\d{12}:(review-template)/[a-f0-9]{32}`
Required: Yes

## Request Body
<a name="API_CreateTemplateShare_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_CreateTemplateShare_RequestSyntax) **   <a name="wellarchitected-CreateTemplateShare-request-ClientRequestToken"></a>
A unique case-sensitive string used to ensure that this request is idempotent (executes only once).
You should not reuse the same token for other requests. If you retry a request with the same client request token and the same parameters after the original request has completed successfully, the result of the original request is returned.
This token is listed as required, however, if you do not specify it, the AWS SDKs automatically generate one for you. If you are not using the AWS SDK or the AWS CLI, you must provide this token or the request will fail.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\x00-\x7F]*`
Required: Yes

 ** [SharedWith](#API_CreateTemplateShare_RequestSyntax) **   <a name="wellarchitected-CreateTemplateShare-request-SharedWith"></a>
The AWS account ID, organization ID, or organizational unit (OU) ID with which the workload, lens, profile, or review template is shared.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 2048.
Required: Yes

## Response Syntax
<a name="API_CreateTemplateShare_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ShareId": "string",
   "TemplateArn": "string"
}
```

## Response Elements
<a name="API_CreateTemplateShare_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ShareId](#API_CreateTemplateShare_ResponseSyntax) **   <a name="wellarchitected-CreateTemplateShare-response-ShareId"></a>
The ID associated with the share.
Type: String
Pattern: `[0-9a-f]{32}`

 ** [TemplateArn](#API_CreateTemplateShare_ResponseSyntax) **   <a name="wellarchitected-CreateTemplateShare-response-TemplateArn"></a>
The review template ARN.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 250.
Pattern: `arn:aws(-us-gov|-iso(-[a-z])?|-cn)?:wellarchitected:[a-z]{2}(-gov|-iso([a-z])?)?-[a-z]+-\d:\d{12}:(review-template)/[a-f0-9]{32}`

## Errors
<a name="API_CreateTemplateShare_Errors"></a>

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

 ** ServiceQuotaExceededException **
The user has reached their resource quota.
 ** Message **
Description of the error.
 ** QuotaCode **
Service Quotas requirement to identify originating quota.
 ** ResourceId **
Identifier of the resource affected.
 ** ResourceType **
Type of the resource affected.
 ** ServiceCode **
Service Quotas requirement to identify originating service.
HTTP Status Code: 402

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
<a name="API_CreateTemplateShare_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/CreateTemplateShare)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/CreateTemplateShare)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/CreateTemplateShare)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/CreateTemplateShare)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/CreateTemplateShare)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/CreateTemplateShare)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/CreateTemplateShare)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/CreateTemplateShare)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/CreateTemplateShare)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/CreateTemplateShare)
