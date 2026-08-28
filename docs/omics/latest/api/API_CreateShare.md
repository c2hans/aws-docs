---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_CreateShare.html
---

# CreateShare
<a name="API_CreateShare"></a>

Creates a cross-account shared resource. The resource owner makes an offer to share the resource with the principal subscriber (an AWS user with a different account than the resource owner).

The following resources support cross-account sharing:
+ HealthOmics variant stores
+ HealthOmics annotation stores
+ Private workflows

## Request Syntax
<a name="API_CreateShare_RequestSyntax"></a>

```
POST /share HTTP/1.1
Content-type: application/json

{
   "principalSubscriber": "{{string}}",
   "resourceArn": "{{string}}",
   "shareName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateShare_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateShare_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [principalSubscriber](#API_CreateShare_RequestSyntax) **   <a name="omics-CreateShare-request-principalSubscriber"></a>
The principal subscriber is the account being offered shared access to the resource.
Type: String
Required: Yes

 ** [resourceArn](#API_CreateShare_RequestSyntax) **   <a name="omics-CreateShare-request-resourceArn"></a>
The ARN of the resource to be shared.
Type: String
Required: Yes

 ** [shareName](#API_CreateShare_RequestSyntax) **   <a name="omics-CreateShare-request-shareName"></a>
A name that the owner defines for the share.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

## Response Syntax
<a name="API_CreateShare_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "shareId": "string",
   "shareName": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_CreateShare_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [shareId](#API_CreateShare_ResponseSyntax) **   <a name="omics-CreateShare-response-shareId"></a>
The ID that HealthOmics generates for the share.
Type: String

 ** [shareName](#API_CreateShare_ResponseSyntax) **   <a name="omics-CreateShare-response-shareName"></a>
The name of the share.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`

 ** [status](#API_CreateShare_ResponseSyntax) **   <a name="omics-CreateShare-response-status"></a>
The status of the share.
Type: String
Valid Values: `PENDING | ACTIVATING | ACTIVE | DELETING | DELETED | FAILED`

## Errors
<a name="API_CreateShare_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request cannot be applied to the target resource in its current state.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred. Try the request again.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The target resource was not found in the current Region.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request exceeds a service quota.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_CreateShare_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/CreateShare)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/CreateShare)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/CreateShare)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/CreateShare)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/CreateShare)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/CreateShare)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/CreateShare)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/CreateShare)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/CreateShare)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/CreateShare)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
