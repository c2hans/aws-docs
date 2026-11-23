---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_PutTrustedAccessProgramAccountEnrollment.html
---

# PutTrustedAccessProgramAccountEnrollment

Sets your account's enrollment preference for a trusted access program. Amazon Bedrock identifies the account from your authenticated request. To enable enrollment, your account needs applicable approval and no applicable revocation, including when you repeat an enabled setting. Otherwise, Amazon Bedrock returns `ConflictException` and preserves the stored setting. With the required permissions, you can set `disabled` or `inherit` even if your account is ineligible or its eligibility is revoked.

## Request Syntax
<a name="API_PutTrustedAccessProgramAccountEnrollment_RequestSyntax"></a>

```
PUT /trusted-access-programs/{{programIdentifier}}/account-enrollment HTTP/1.1
Content-type: application/json

{
   "optIn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutTrustedAccessProgramAccountEnrollment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [programIdentifier](#API_PutTrustedAccessProgramAccountEnrollment_RequestSyntax) **   <a name="bedrock-PutTrustedAccessProgramAccountEnrollment-request-uri-programIdentifier"></a>
The identifier of the trusted access program.
Length Constraints: Minimum length of 3. Maximum length of 115.
Pattern: `([a-z0-9]+-[a-z0-9-]+|arn:aws(-[^:]+)?:bedrock::aws:trusted-access-program/[a-z0-9]+-[a-z0-9-]+)`
Required: Yes

## Request Body
<a name="API_PutTrustedAccessProgramAccountEnrollment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [optIn](#API_PutTrustedAccessProgramAccountEnrollment_RequestSyntax) **   <a name="bedrock-PutTrustedAccessProgramAccountEnrollment-request-optIn"></a>
The enrollment preference to store. A transition to enabled accepts the program's terms. Changing the preference records a new updatedAt. Repeating the same stored preference preserves updatedAt.
Type: String
Valid Values: `inherit | enabled | disabled`
Required: Yes

## Response Syntax
<a name="API_PutTrustedAccessProgramAccountEnrollment_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "optIn": "string",
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_PutTrustedAccessProgramAccountEnrollment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [optIn](#API_PutTrustedAccessProgramAccountEnrollment_ResponseSyntax) **   <a name="bedrock-PutTrustedAccessProgramAccountEnrollment-response-optIn"></a>
Stored preference at the addressed scope. A missing enrollment returns inherit without updatedAt.
Type: String
Valid Values: `inherit | enabled | disabled`

 ** [updatedAt](#API_PutTrustedAccessProgramAccountEnrollment_ResponseSyntax) **   <a name="bedrock-PutTrustedAccessProgramAccountEnrollment-response-updatedAt"></a>
The time the stored enrollment setting last changed.
Type: Timestamp

## Errors
<a name="API_PutTrustedAccessProgramAccountEnrollment_Errors"></a>

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
<a name="API_PutTrustedAccessProgramAccountEnrollment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/PutTrustedAccessProgramAccountEnrollment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/PutTrustedAccessProgramAccountEnrollment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/PutTrustedAccessProgramAccountEnrollment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/PutTrustedAccessProgramAccountEnrollment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/PutTrustedAccessProgramAccountEnrollment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/PutTrustedAccessProgramAccountEnrollment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/PutTrustedAccessProgramAccountEnrollment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/PutTrustedAccessProgramAccountEnrollment)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/PutTrustedAccessProgramAccountEnrollment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/PutTrustedAccessProgramAccountEnrollment)
