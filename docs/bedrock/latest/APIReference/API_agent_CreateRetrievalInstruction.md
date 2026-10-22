---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_CreateRetrievalInstruction.html
---

# CreateRetrievalInstruction
<a name="API_agent_CreateRetrievalInstruction"></a>

Creates a new retrieval instruction. The retrieval instruction is usable once its status becomes ACTIVE. Use GetRetrievalInstruction to check whether it is ready.

## Request Syntax
<a name="API_agent_CreateRetrievalInstruction_RequestSyntax"></a>

```
POST /retrievalinstructions/ HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "customerEncryptionKeyArn": "{{string}}",
   "description": "{{string}}",
   "instruction": {
      "answerFormat": "{{string}}",
      "answerPolicy": "{{string}}",
      "persona": "{{string}}",
      "retrievalGuidance": "{{string}}"
   },
   "name": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_agent_CreateRetrievalInstruction_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_agent_CreateRetrievalInstruction_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_agent_CreateRetrievalInstruction_RequestSyntax) **   <a name="bedrock-agent_CreateRetrievalInstruction-request-clientToken"></a>
A caller-supplied token that makes a retried create return the existing resource rather than a second one. The window is 8 hours.
Type: String
Length Constraints: Minimum length of 33. Maximum length of 256.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`
Required: No

 ** [customerEncryptionKeyArn](#API_agent_CreateRetrievalInstruction_RequestSyntax) **   <a name="bedrock-agent_CreateRetrievalInstruction-request-customerEncryptionKeyArn"></a>
The Amazon Resource Name (ARN) of a customer managed AWS Key Management Service (AWS KMS) key used to encrypt the instruction content at rest. If you omit it, the service uses an AWS owned key. You fix the key at create and cannot change it later.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`
Required: No

 ** [description](#API_agent_CreateRetrievalInstruction_RequestSyntax) **   <a name="bedrock-agent_CreateRetrievalInstruction-request-description"></a>
Specifies a description of the retrieval instruction.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

 ** [instruction](#API_agent_CreateRetrievalInstruction_RequestSyntax) **   <a name="bedrock-agent_CreateRetrievalInstruction-request-instruction"></a>
The instruction content, as a set of named fields. Get does not return this field until the create review passes.
Type: [RetrievalInstructionContent](API_agent_RetrievalInstructionContent.md) object
Required: Yes

 ** [name](#API_agent_CreateRetrievalInstruction_RequestSyntax) **   <a name="bedrock-agent_CreateRetrievalInstruction-request-name"></a>
Specifies the name of the retrieval instruction.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `([0-9a-zA-Z][_-]?){1,100}`
Required: Yes

 ** [tags](#API_agent_CreateRetrievalInstruction_RequestSyntax) **   <a name="bedrock-agent_CreateRetrievalInstruction-request-tags"></a>
Tags for the retrieval instruction.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[a-zA-Z0-9\s._:/=+@-]*`
Required: No

## Response Syntax
<a name="API_agent_CreateRetrievalInstruction_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "createdAt": "string",
   "lastTransitionStatus": "string",
   "name": "string",
   "retrievalInstructionArn": "string",
   "retrievalInstructionId": "string",
   "status": "string",
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_agent_CreateRetrievalInstruction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_agent_CreateRetrievalInstruction_ResponseSyntax) **   <a name="bedrock-agent_CreateRetrievalInstruction-response-createdAt"></a>
When you created the retrieval instruction.
Type: Timestamp

 ** [lastTransitionStatus](#API_agent_CreateRetrievalInstruction_ResponseSyntax) **   <a name="bedrock-agent_CreateRetrievalInstruction-response-lastTransitionStatus"></a>
Always CREATING on this response. Poll GetRetrievalInstruction until this member is neither CREATING nor UPDATING, then read the outcome from it.
Type: String
Valid Values: `CREATING | UPDATING | CREATE_SUCCESSFUL | CREATE_FAILED | UPDATE_SUCCESSFUL | UPDATE_FAILED`

 ** [name](#API_agent_CreateRetrievalInstruction_ResponseSyntax) **   <a name="bedrock-agent_CreateRetrievalInstruction-response-name"></a>
The name of the retrieval instruction.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `([0-9a-zA-Z][_-]?){1,100}`

 ** [retrievalInstructionArn](#API_agent_CreateRetrievalInstruction_ResponseSyntax) **   <a name="bedrock-agent_CreateRetrievalInstruction-response-retrievalInstructionArn"></a>
The ARN of the newly created retrieval instruction.
Type: String
Pattern: `arn:aws(-cn|-us-gov|-eusc|-iso(-[b-f])?)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:retrieval-instruction/[a-z0-9]{10}`

 ** [retrievalInstructionId](#API_agent_CreateRetrievalInstruction_ResponseSyntax) **   <a name="bedrock-agent_CreateRetrievalInstruction-response-retrievalInstructionId"></a>
The identifier of the newly created retrieval instruction.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `[a-z0-9]{10}`

 ** [status](#API_agent_CreateRetrievalInstruction_ResponseSyntax) **   <a name="bedrock-agent_CreateRetrievalInstruction-response-status"></a>
Always INACTIVE on this response. The content review has not run when this call returns, so the resource is not yet usable.
Type: String
Valid Values: `ACTIVE | INACTIVE`

 ** [updatedAt](#API_agent_CreateRetrievalInstruction_ResponseSyntax) **   <a name="bedrock-agent_CreateRetrievalInstruction-response-updatedAt"></a>
When the retrieval instruction was last updated.
Type: Timestamp

## Errors
<a name="API_agent_CreateRetrievalInstruction_Errors"></a>

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
<a name="API_agent_CreateRetrievalInstruction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/CreateRetrievalInstruction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/CreateRetrievalInstruction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/CreateRetrievalInstruction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/CreateRetrievalInstruction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/CreateRetrievalInstruction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/CreateRetrievalInstruction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/CreateRetrievalInstruction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/CreateRetrievalInstruction)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/CreateRetrievalInstruction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/CreateRetrievalInstruction)
