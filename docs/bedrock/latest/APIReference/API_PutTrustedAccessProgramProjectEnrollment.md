---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_PutTrustedAccessProgramProjectEnrollment.html
---

# PutTrustedAccessProgramProjectEnrollment

Sets a named project's enrollment preference for a trusted access program. The project must be active in this Region and owned by the calling account. Enabling requires applicable project, account, or organization approval and no applicable revocation, including when repeating an enabled setting; otherwise returns ConflictException and preserves the stored setting. Authorized disable and inherit writes are allowed while ineligible or revoked. Archived projects reject all writes with ValidationException.

## Request Syntax
<a name="API_PutTrustedAccessProgramProjectEnrollment_RequestSyntax"></a>

```
PUT /trusted-access-programs/{{programIdentifier}}/project-enrollment/{{projectIdentifier}} HTTP/1.1
Content-type: application/json

{
   "optIn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutTrustedAccessProgramProjectEnrollment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [programIdentifier](#API_PutTrustedAccessProgramProjectEnrollment_RequestSyntax) **   <a name="bedrock-PutTrustedAccessProgramProjectEnrollment-request-uri-programIdentifier"></a>
The identifier of the trusted access program.
Length Constraints: Minimum length of 3. Maximum length of 115.
Pattern: `([a-z0-9]+-[a-z0-9-]+|arn:aws(-[^:]+)?:bedrock::aws:trusted-access-program/[a-z0-9]+-[a-z0-9-]+)`
Required: Yes

 ** [projectIdentifier](#API_PutTrustedAccessProgramProjectEnrollment_RequestSyntax) **   <a name="bedrock-PutTrustedAccessProgramProjectEnrollment-request-uri-projectIdentifier"></a>
The id or ARN of the named Bedrock project. The default project is not supported; use PutTrustedAccessProgramAccountEnrollment for account-level enrollment. An ARN from another account, Region, or partition returns ValidationException. A project that does not exist in the calling account returns ResourceNotFoundException.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `([a-zA-Z0-9_-]+|arn:aws(-[^:]+)?:bedrock:[0-9a-z-]{1,20}:[0-9]{12}:project/[a-zA-Z0-9_-]+)`
Required: Yes

## Request Body
<a name="API_PutTrustedAccessProgramProjectEnrollment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [optIn](#API_PutTrustedAccessProgramProjectEnrollment_RequestSyntax) **   <a name="bedrock-PutTrustedAccessProgramProjectEnrollment-request-optIn"></a>
The enrollment preference to store. A transition to enabled accepts the program's terms. Changing the preference records a new updatedAt. Repeating the same stored preference preserves updatedAt.
Type: String
Valid Values: `inherit | enabled | disabled`
Required: Yes

## Response Syntax
<a name="API_PutTrustedAccessProgramProjectEnrollment_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "optIn": "string",
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_PutTrustedAccessProgramProjectEnrollment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [optIn](#API_PutTrustedAccessProgramProjectEnrollment_ResponseSyntax) **   <a name="bedrock-PutTrustedAccessProgramProjectEnrollment-response-optIn"></a>
Stored preference at the addressed scope. A missing enrollment returns inherit without updatedAt.
Type: String
Valid Values: `inherit | enabled | disabled`

 ** [updatedAt](#API_PutTrustedAccessProgramProjectEnrollment_ResponseSyntax) **   <a name="bedrock-PutTrustedAccessProgramProjectEnrollment-response-updatedAt"></a>
The time the stored enrollment setting last changed.
Type: Timestamp

## Errors
<a name="API_PutTrustedAccessProgramProjectEnrollment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request is denied because of missing access permissions.
HTTP Status Code: 403

 ** ConflictException **
Error occurred because of a conflict while performing an operation.
HTTP Status Code: 400

 ** InternalServerException **
An internal server error occurred. Retry your request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.
HTTP Status Code: 404

 ** ThrottlingException **
The number of requests exceeds the limit. Resubmit your request later.
HTTP Status Code: 429

 ** ValidationException **
Input validation failed. Check your request parameters and retry the request.
HTTP Status Code: 400

## See Also
<a name="API_PutTrustedAccessProgramProjectEnrollment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/PutTrustedAccessProgramProjectEnrollment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/PutTrustedAccessProgramProjectEnrollment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/PutTrustedAccessProgramProjectEnrollment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/PutTrustedAccessProgramProjectEnrollment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/PutTrustedAccessProgramProjectEnrollment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/PutTrustedAccessProgramProjectEnrollment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/PutTrustedAccessProgramProjectEnrollment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/PutTrustedAccessProgramProjectEnrollment)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/PutTrustedAccessProgramProjectEnrollment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/PutTrustedAccessProgramProjectEnrollment)
