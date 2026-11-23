---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_StartTrustedAccessProgramProjectApplication.html
---

# StartTrustedAccessProgramProjectApplication

Prepare a provider application handoff for a named project. The project must be active in this Region and owned by the calling account. Archived projects return ValidationException. This does not submit an application, grant eligibility, or change enrollment. Programs without self-service applications return ValidationException with guidance to contact the AWS account team. Repeated calls can issue fresh tokens. Successful responses use Cache-Control: no-store.

## Request Syntax
<a name="API_StartTrustedAccessProgramProjectApplication_RequestSyntax"></a>

```
POST /trusted-access-programs/{{programIdentifier}}/project-application/{{projectIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_StartTrustedAccessProgramProjectApplication_RequestParameters"></a>

The request uses the following URI parameters.

 ** [programIdentifier](#API_StartTrustedAccessProgramProjectApplication_RequestSyntax) **   <a name="bedrock-StartTrustedAccessProgramProjectApplication-request-uri-programIdentifier"></a>
Identifier of the trusted access program.
Length Constraints: Minimum length of 3. Maximum length of 115.
Pattern: `([a-z0-9]+-[a-z0-9-]+|arn:aws(-[^:]+)?:bedrock::aws:trusted-access-program/[a-z0-9]+-[a-z0-9-]+)`
Required: Yes

 ** [projectIdentifier](#API_StartTrustedAccessProgramProjectApplication_RequestSyntax) **   <a name="bedrock-StartTrustedAccessProgramProjectApplication-request-uri-projectIdentifier"></a>
The id or ARN of the named Bedrock project. The default project is not supported; use StartTrustedAccessProgramAccountApplication for an account-level application. An ARN from another account, Region, or partition returns ValidationException. A project that does not exist in the calling account returns ResourceNotFoundException.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `([a-zA-Z0-9_-]+|arn:aws(-[^:]+)?:bedrock:[0-9a-z-]{1,20}:[0-9]{12}:project/[a-zA-Z0-9_-]+)`
Required: Yes

## Request Body
<a name="API_StartTrustedAccessProgramProjectApplication_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_StartTrustedAccessProgramProjectApplication_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "result": { ... }
}
```

## Response Elements
<a name="API_StartTrustedAccessProgramProjectApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [result](#API_StartTrustedAccessProgramProjectApplication_ResponseSyntax) **   <a name="bedrock-StartTrustedAccessProgramProjectApplication-response-result"></a>
Provider handoff for the named project.
Type: [TrustedAccessProgramApplicationResult](API_TrustedAccessProgramApplicationResult.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

## Errors
<a name="API_StartTrustedAccessProgramProjectApplication_Errors"></a>

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
<a name="API_StartTrustedAccessProgramProjectApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/StartTrustedAccessProgramProjectApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/StartTrustedAccessProgramProjectApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/StartTrustedAccessProgramProjectApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/StartTrustedAccessProgramProjectApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/StartTrustedAccessProgramProjectApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/StartTrustedAccessProgramProjectApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/StartTrustedAccessProgramProjectApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/StartTrustedAccessProgramProjectApplication)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/StartTrustedAccessProgramProjectApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/StartTrustedAccessProgramProjectApplication)
