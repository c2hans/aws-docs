---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetTrustedAccessProgram.html
---

# GetTrustedAccessProgram

Gets trusted access program details and resolves participation for your account and its current organization. If you specify a project, Amazon Bedrock resolves participation for the project, including inheritance from the account and organization. Archived projects remain readable until they expire. Returns the same flat summary as a ListTrustedAccessPrograms item. An absent or invisible program returns ResourceNotFoundException.

## Request Syntax
<a name="API_GetTrustedAccessProgram_RequestSyntax"></a>

```
GET /trusted-access-programs/{{programIdentifier}}?projectIdentifier={{projectIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetTrustedAccessProgram_RequestParameters"></a>

The request uses the following URI parameters.

 ** [programIdentifier](#API_GetTrustedAccessProgram_RequestSyntax) **   <a name="bedrock-GetTrustedAccessProgram-request-uri-programIdentifier"></a>
Identifier of the trusted access program.
Length Constraints: Minimum length of 3. Maximum length of 115.
Pattern: `([a-z0-9]+-[a-z0-9-]+|arn:aws(-[^:]+)?:bedrock::aws:trusted-access-program/[a-z0-9]+-[a-z0-9-]+)`
Required: Yes

 ** [projectIdentifier](#API_GetTrustedAccessProgram_RequestSyntax) **   <a name="bedrock-GetTrustedAccessProgram-request-uri-projectIdentifier"></a>
The ID or ARN of a named Bedrock project owned by the calling account in this Region. When omitted, resolves participation for the calling account, including participation inherited from its current organization. When specified, resolves participation for the project, including participation inherited from the account and its current organization. You cannot specify the default project. Omit this field to resolve its inherited participation. An ARN from another account, Region, or partition returns ValidationException. A project that does not exist in the calling account returns ResourceNotFoundException.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `([a-zA-Z0-9_-]+|arn:aws(-[^:]+)?:bedrock:[0-9a-z-]{1,20}:[0-9]{12}:project/[a-zA-Z0-9_-]+)`

## Request Body
<a name="API_GetTrustedAccessProgram_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetTrustedAccessProgram_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "description": "string",
   "detailsUrl": "string",
   "eligibilityScope": "string",
   "enrollmentUrl": "string",
   "name": "string",
   "optIn": "string",
   "programId": "string",
   "providerName": "string",
   "resolvedFor": {
      "accountId": "string",
      "projectArn": "string"
   },
   "source": "string",
   "status": "string",
   "statusReason": "string",
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_GetTrustedAccessProgram_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [description](#API_GetTrustedAccessProgram_ResponseSyntax) **   <a name="bedrock-GetTrustedAccessProgram-response-description"></a>
Description of the program and its effects on model access or data handling.
Type: String

 ** [detailsUrl](#API_GetTrustedAccessProgram_ResponseSyntax) **   <a name="bedrock-GetTrustedAccessProgram-response-detailsUrl"></a>
URL with program details, terms, and instructions for obtaining access.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `https://[^\s]+`

 ** [eligibilityScope](#API_GetTrustedAccessProgram_ResponseSyntax) **   <a name="bedrock-GetTrustedAccessProgram-response-eligibilityScope"></a>
Scope supplying the applicable approval or most-specific revocation. Omitted when no approval or revocation applies.
Type: String
Valid Values: `organization | account | project | program_default`

 ** [enrollmentUrl](#API_GetTrustedAccessProgram_ResponseSyntax) **   <a name="bedrock-GetTrustedAccessProgram-response-enrollmentUrl"></a>
Provider application intake URL. Omitted when the program has no customer-facing intake URL.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `https://[^\s]+`

 ** [name](#API_GetTrustedAccessProgram_ResponseSyntax) **   <a name="bedrock-GetTrustedAccessProgram-response-name"></a>
Display name of the program.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [optIn](#API_GetTrustedAccessProgram_ResponseSyntax) **   <a name="bedrock-GetTrustedAccessProgram-response-optIn"></a>
Resolved customer preference, preserved independently of eligibility, including while revoked.
Type: String
Valid Values: `inherit | enabled | disabled`

 ** [programId](#API_GetTrustedAccessProgram_ResponseSyntax) **   <a name="bedrock-GetTrustedAccessProgram-response-programId"></a>
Identifier of the trusted access program.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-z0-9]+-[a-z0-9-]+`

 ** [providerName](#API_GetTrustedAccessProgram_ResponseSyntax) **   <a name="bedrock-GetTrustedAccessProgram-response-providerName"></a>
Name of the model provider offering the program.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `.*`

 ** [resolvedFor](#API_GetTrustedAccessProgram_ResponseSyntax) **   <a name="bedrock-GetTrustedAccessProgram-response-resolvedFor"></a>
Account and optional project context for which participation was resolved.
Type: [TrustedAccessResolutionContext](API_TrustedAccessResolutionContext.md) object

 ** [source](#API_GetTrustedAccessProgram_ResponseSyntax) **   <a name="bedrock-GetTrustedAccessProgram-response-source"></a>
Scope deciding the status. This can differ from the scope supplying the resolved opt-in preference and enrollment timestamps.
Type: String
Valid Values: `organization | account | project | program_default`

 ** [status](#API_GetTrustedAccessProgram_ResponseSyntax) **   <a name="bedrock-GetTrustedAccessProgram-response-status"></a>
Participation status resolved for the account and optional project context.
Type: String
Valid Values: `requestable | eligible | enabled | disabled | revoked`

 ** [statusReason](#API_GetTrustedAccessProgram_ResponseSyntax) **   <a name="bedrock-GetTrustedAccessProgram-response-statusReason"></a>
Nonempty explanation for requestable or revoked status. Omitted for other statuses.
Type: String

 ** [updatedAt](#API_GetTrustedAccessProgram_ResponseSyntax) **   <a name="bedrock-GetTrustedAccessProgram-response-updatedAt"></a>
Last change to the enrollment supplying the resolved opt-in. Present for enabled or disabled, including while revoked; omitted for inherit.
Type: Timestamp

## Errors
<a name="API_GetTrustedAccessProgram_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request is denied because of missing access permissions.
HTTP Status Code: 403

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
<a name="API_GetTrustedAccessProgram_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/GetTrustedAccessProgram)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/GetTrustedAccessProgram)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/GetTrustedAccessProgram)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/GetTrustedAccessProgram)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/GetTrustedAccessProgram)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/GetTrustedAccessProgram)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/GetTrustedAccessProgram)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/GetTrustedAccessProgram)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/GetTrustedAccessProgram)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/GetTrustedAccessProgram)
