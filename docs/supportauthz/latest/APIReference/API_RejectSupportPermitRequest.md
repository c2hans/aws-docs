---
source_url: https://docs.aws.amazon.com/supportauthz/latest/APIReference/API_RejectSupportPermitRequest.html
---

# RejectSupportPermitRequest
<a name="API_RejectSupportPermitRequest"></a>

Rejects a permit request from an AWS support operator. The operator cannot proceed with the requested action.

## Request Syntax
<a name="API_RejectSupportPermitRequest_RequestSyntax"></a>

```
PUT /support-permit-requests/{{requestArn}}/reject HTTP/1.1
```

## URI Request Parameters
<a name="API_RejectSupportPermitRequest_RequestParameters"></a>

The request uses the following URI parameters.

 ** [requestArn](#API_RejectSupportPermitRequest_RequestSyntax) **   <a name="supportauthorization-RejectSupportPermitRequest-request-uri-requestArn"></a>
The ARN of the permit request to reject.
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[a-zA-Z0-9:/-]{1,512}`
Required: Yes

## Request Body
<a name="API_RejectSupportPermitRequest_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_RejectSupportPermitRequest_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "requestArn": "string"
}
```

## Response Elements
<a name="API_RejectSupportPermitRequest_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [requestArn](#API_RejectSupportPermitRequest_ResponseSyntax) **   <a name="supportauthorization-RejectSupportPermitRequest-response-requestArn"></a>
The ARN of the rejected permit request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[a-zA-Z0-9:/-]{1,512}`

## Errors
<a name="API_RejectSupportPermitRequest_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permissions to perform this operation.
HTTP Status Code: 403

 ** ConflictException **
The request conflicts with the current state of the resource.
 ** resourceId **
The identifier of the resource that caused the conflict.
 ** resourceType **
The type of the resource that caused the conflict.
HTTP Status Code: 409

 ** InternalServerException **
An internal service error occurred. Try again later.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** resourceId **
The identifier of the resource that was not found.
 ** resourceType **
The type of the resource that was not found.
HTTP Status Code: 404

 ** ThrottlingException **
The request rate exceeded the allowed limit. Try again later.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by the service.
 ** fieldList **
A list of fields that fail validation. Each entry identifies the field and the reason for the constraint violation.
HTTP Status Code: 400

## See Also
<a name="API_RejectSupportPermitRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/supportauthz-2026-06-30/RejectSupportPermitRequest)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/supportauthz-2026-06-30/RejectSupportPermitRequest)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/supportauthz-2026-06-30/RejectSupportPermitRequest)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/supportauthz-2026-06-30/RejectSupportPermitRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/supportauthz-2026-06-30/RejectSupportPermitRequest)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/supportauthz-2026-06-30/RejectSupportPermitRequest)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/supportauthz-2026-06-30/RejectSupportPermitRequest)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/supportauthz-2026-06-30/RejectSupportPermitRequest)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/supportauthz-2026-06-30/RejectSupportPermitRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/supportauthz-2026-06-30/RejectSupportPermitRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Support authorization. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query supportauthz` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
