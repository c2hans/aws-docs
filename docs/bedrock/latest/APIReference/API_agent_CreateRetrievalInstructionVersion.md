---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_CreateRetrievalInstructionVersion.html
---

# CreateRetrievalInstructionVersion
<a name="API_agent_CreateRetrievalInstructionVersion"></a>

Creates an immutable numbered version from the retrieval instruction's current reviewed content. The service creates the version synchronously.

The service numbers versions from 1 and assigns them in order, never reusing a number.

## Request Syntax
<a name="API_agent_CreateRetrievalInstructionVersion_RequestSyntax"></a>

```
POST /retrievalinstructions/{{retrievalInstructionId}}/versions HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}"
}
```

## URI Request Parameters
<a name="API_agent_CreateRetrievalInstructionVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [retrievalInstructionId](#API_agent_CreateRetrievalInstructionVersion_RequestSyntax) **   <a name="bedrock-agent_CreateRetrievalInstructionVersion-request-uri-retrievalInstructionId"></a>
The identifier of the retrieval instruction to version.
Length Constraints: Fixed length of 10.
Pattern: `[a-z0-9]{10}`
Required: Yes

## Request Body
<a name="API_agent_CreateRetrievalInstructionVersion_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_agent_CreateRetrievalInstructionVersion_RequestSyntax) **   <a name="bedrock-agent_CreateRetrievalInstructionVersion-request-clientToken"></a>
A caller-supplied token that makes a retried call return the version created by the first call rather than a second version. The window is 8 hours.
Type: String
Length Constraints: Minimum length of 33. Maximum length of 256.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`
Required: No

 ** [description](#API_agent_CreateRetrievalInstructionVersion_RequestSyntax) **   <a name="bedrock-agent_CreateRetrievalInstructionVersion-request-description"></a>
A description of this version. Independent of the retrieval instruction's own description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

## Response Syntax
<a name="API_agent_CreateRetrievalInstructionVersion_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "createdAt": "string",
   "description": "string",
   "retrievalInstructionArn": "string",
   "retrievalInstructionId": "string",
   "version": "string"
}
```

## Response Elements
<a name="API_agent_CreateRetrievalInstructionVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_agent_CreateRetrievalInstructionVersion_ResponseSyntax) **   <a name="bedrock-agent_CreateRetrievalInstructionVersion-response-createdAt"></a>
When this version was created.
Type: Timestamp

 ** [description](#API_agent_CreateRetrievalInstructionVersion_ResponseSyntax) **   <a name="bedrock-agent_CreateRetrievalInstructionVersion-response-description"></a>
The description of this version, when one was supplied.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.

 ** [retrievalInstructionArn](#API_agent_CreateRetrievalInstructionVersion_ResponseSyntax) **   <a name="bedrock-agent_CreateRetrievalInstructionVersion-response-retrievalInstructionArn"></a>
The ARN of the retrieval instruction. Versions do not have their own ARN.
Type: String
Pattern: `arn:aws(-cn|-us-gov|-eusc|-iso(-[b-f])?)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:retrieval-instruction/[a-z0-9]{10}`

 ** [retrievalInstructionId](#API_agent_CreateRetrievalInstructionVersion_ResponseSyntax) **   <a name="bedrock-agent_CreateRetrievalInstructionVersion-response-retrievalInstructionId"></a>
The identifier of the retrieval instruction.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `[a-z0-9]{10}`

 ** [version](#API_agent_CreateRetrievalInstructionVersion_ResponseSyntax) **   <a name="bedrock-agent_CreateRetrievalInstructionVersion-response-version"></a>
The number of the version created. Versions are numbered from 1 and allocated monotonically; a number is never reused, even after the version is deleted.
Type: String
Pattern: `[1-9][0-9]{0,8}`

## Errors
<a name="API_agent_CreateRetrievalInstructionVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request is denied because of missing access permissions.
HTTP Status Code: 403

 ** ConflictException **
There was a conflict performing an operation.
HTTP Status Code: 409

 ** InternalServerException **
An internal server error occurred. Retry your request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The number of requests exceeds the service quota. Resubmit your request later.
HTTP Status Code: 402

 ** ThrottlingException **
The number of requests exceeds the limit. Resubmit your request later.
HTTP Status Code: 429

 ** ValidationException **
Input validation failed. Check your request parameters and retry the request.
 ** fieldList **
A list of objects containing fields that caused validation errors and their corresponding validation error messages.
HTTP Status Code: 400

## See Also
<a name="API_agent_CreateRetrievalInstructionVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/CreateRetrievalInstructionVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/CreateRetrievalInstructionVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/CreateRetrievalInstructionVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/CreateRetrievalInstructionVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/CreateRetrievalInstructionVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/CreateRetrievalInstructionVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/CreateRetrievalInstructionVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/CreateRetrievalInstructionVersion)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/CreateRetrievalInstructionVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/CreateRetrievalInstructionVersion)
