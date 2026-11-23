---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListTrustedAccessPrograms.html
---

# ListTrustedAccessPrograms

Lists all trusted access programs visible to your account, ordered by program ID. Amazon Bedrock resolves participation for your account and its current organization. If you specify a project, Amazon Bedrock resolves participation for the project, including inheritance from the account and organization. Archived projects remain readable until they expire. Amazon Bedrock returns all visible programs in one response.

## Request Syntax
<a name="API_ListTrustedAccessPrograms_RequestSyntax"></a>

```
GET /trusted-access-programs?maxResults={{maxResults}}&nextToken={{nextToken}}&projectIdentifier={{projectIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListTrustedAccessPrograms_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListTrustedAccessPrograms_RequestSyntax) **   <a name="bedrock-ListTrustedAccessPrograms-request-uri-maxResults"></a>
Reserved for future pagination support. Currently ignored; the response includes all visible programs.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [nextToken](#API_ListTrustedAccessPrograms_RequestSyntax) **   <a name="bedrock-ListTrustedAccessPrograms-request-uri-nextToken"></a>
Reserved for future pagination support. Omit this field.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `\S*`

 ** [projectIdentifier](#API_ListTrustedAccessPrograms_RequestSyntax) **   <a name="bedrock-ListTrustedAccessPrograms-request-uri-projectIdentifier"></a>
The ID or ARN of a named Bedrock project owned by the calling account in this Region. When omitted, resolves participation for the calling account, including participation inherited from its current organization. When specified, resolves participation for the project, including participation inherited from the account and its current organization. You cannot specify the default project. Omit this field to resolve its inherited participation. An ARN from another account, Region, or partition returns ValidationException. A project that does not exist in the calling account returns ResourceNotFoundException.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `([a-zA-Z0-9_-]+|arn:aws(-[^:]+)?:bedrock:[0-9a-z-]{1,20}:[0-9]{12}:project/[a-zA-Z0-9_-]+)`

## Request Body
<a name="API_ListTrustedAccessPrograms_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListTrustedAccessPrograms_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "programSummaries": [
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
   ]
}
```

## Response Elements
<a name="API_ListTrustedAccessPrograms_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListTrustedAccessPrograms_ResponseSyntax) **   <a name="bedrock-ListTrustedAccessPrograms-response-nextToken"></a>
Reserved for future pagination support. Currently omitted because the response contains the complete list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `\S*`

 ** [programSummaries](#API_ListTrustedAccessPrograms_ResponseSyntax) **   <a name="bedrock-ListTrustedAccessPrograms-response-programSummaries"></a>
All visible programs with resolved participation, ordered by program ID. Always present, including an empty array when no programs are visible.
Type: Array of [TrustedAccessProgramSummary](API_TrustedAccessProgramSummary.md) objects

## Errors
<a name="API_ListTrustedAccessPrograms_Errors"></a>

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
<a name="API_ListTrustedAccessPrograms_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/ListTrustedAccessPrograms)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/ListTrustedAccessPrograms)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/ListTrustedAccessPrograms)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/ListTrustedAccessPrograms)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/ListTrustedAccessPrograms)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/ListTrustedAccessPrograms)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/ListTrustedAccessPrograms)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/ListTrustedAccessPrograms)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/ListTrustedAccessPrograms)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/ListTrustedAccessPrograms)
