---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CreateProfileShare.html
---

# CreateProfileShare
<a name="API_CreateProfileShare"></a>

Create a profile share.

## Request Syntax
<a name="API_CreateProfileShare_RequestSyntax"></a>

```
POST /profiles/{{ProfileArn}}/shares HTTP/1.1
Content-type: application/json

{
   "ClientRequestToken": "{{string}}",
   "SharedWith": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateProfileShare_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ProfileArn](#API_CreateProfileShare_RequestSyntax) **   <a name="wellarchitected-CreateProfileShare-request-uri-ProfileArn"></a>
The profile ARN.
Length Constraints: Maximum length of 2084.
Pattern: `arn:aws[-a-z]*:wellarchitected:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:profile/[a-z0-9]+`
Required: Yes

## Request Body
<a name="API_CreateProfileShare_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_CreateProfileShare_RequestSyntax) **   <a name="wellarchitected-CreateProfileShare-request-ClientRequestToken"></a>
A unique case-sensitive string used to ensure that this request is idempotent (executes only once).
You should not reuse the same token for other requests. If you retry a request with the same client request token and the same parameters after the original request has completed successfully, the result of the original request is returned.
This token is listed as required, however, if you do not specify it, the AWS SDKs automatically generate one for you. If you are not using the AWS SDK or the AWS CLI, you must provide this token or the request will fail.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[\x00-\x7F]*$`
Required: Yes

 ** [SharedWith](#API_CreateProfileShare_RequestSyntax) **   <a name="wellarchitected-CreateProfileShare-request-SharedWith"></a>
The AWS account ID, organization ID, or organizational unit (OU) ID with which the workload, lens, profile, or review template is shared.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 2048.
Required: Yes

## Response Syntax
<a name="API_CreateProfileShare_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ProfileArn": "string",
   "ShareId": "string"
}
```

## Response Elements
<a name="API_CreateProfileShare_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ProfileArn](#API_CreateProfileShare_ResponseSyntax) **   <a name="wellarchitected-CreateProfileShare-response-ProfileArn"></a>
The profile ARN.
Type: String
Length Constraints: Maximum length of 2084.
Pattern: `arn:aws[-a-z]*:wellarchitected:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:profile/[a-z0-9]+`

 ** [ShareId](#API_CreateProfileShare_ResponseSyntax) **   <a name="wellarchitected-CreateProfileShare-response-ShareId"></a>
The ID associated with the share.
Type: String
Pattern: `[0-9a-f]{32}`

## Errors
<a name="API_CreateProfileShare_Errors"></a>

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
<a name="API_CreateProfileShare_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/CreateProfileShare)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/CreateProfileShare)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/CreateProfileShare)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/CreateProfileShare)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/CreateProfileShare)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/CreateProfileShare)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/CreateProfileShare)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/CreateProfileShare)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/CreateProfileShare)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/CreateProfileShare)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected Tool. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
