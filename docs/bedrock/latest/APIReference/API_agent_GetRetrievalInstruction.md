---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetRetrievalInstruction.html
---

# GetRetrievalInstruction
<a name="API_agent_GetRetrievalInstruction"></a>

Gets a retrieval instruction. Also used to poll the terminal reporting of an asynchronous create or update.

## Request Syntax
<a name="API_agent_GetRetrievalInstruction_RequestSyntax"></a>

```
GET /retrievalinstructions/{{retrievalInstructionId}}?retrievalInstructionVersion={{retrievalInstructionVersion}} HTTP/1.1
```

## URI Request Parameters
<a name="API_agent_GetRetrievalInstruction_RequestParameters"></a>

The request uses the following URI parameters.

 ** [retrievalInstructionId](#API_agent_GetRetrievalInstruction_RequestSyntax) **   <a name="bedrock-agent_GetRetrievalInstruction-request-uri-retrievalInstructionId"></a>
The identifier of the retrieval instruction to get.
Length Constraints: Fixed length of 10.
Pattern: `[a-z0-9]{10}`
Required: Yes

 ** [retrievalInstructionVersion](#API_agent_GetRetrievalInstruction_RequestSyntax) **   <a name="bedrock-agent_GetRetrievalInstruction-request-uri-retrievalInstructionVersion"></a>
The version to return: a version number, or DRAFT for the retrieval instruction's current reviewed content. When omitted, DRAFT is used. This default is permanent: omitting retrievalInstructionVersion will never resolve to a numbered version.
Length Constraints: Minimum length of 1. Maximum length of 9.
Pattern: `(DRAFT|[1-9][0-9]{0,8})`

## Request Body
<a name="API_agent_GetRetrievalInstruction_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_agent_GetRetrievalInstruction_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": "string",
   "customerEncryptionKeyArn": "string",
   "description": "string",
   "instruction": {
      "answerFormat": "string",
      "answerPolicy": "string",
      "persona": "string",
      "retrievalGuidance": "string"
   },
   "lastTransitionStatus": "string",
   "lastTransitionStatusReasons": [
      {
         "code": "string",
         "fieldName": "string",
         "message": "string"
      }
   ],
   "latestVersion": "string",
   "name": "string",
   "retrievalInstructionArn": "string",
   "retrievalInstructionId": "string",
   "status": "string",
   "updatedAt": "string",
   "version": "string"
}
```

## Response Elements
<a name="API_agent_GetRetrievalInstruction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_agent_GetRetrievalInstruction_ResponseSyntax) **   <a name="bedrock-agent_GetRetrievalInstruction-response-createdAt"></a>
When the retrieval instruction was created. On a numbered version, when that version was created.
Type: Timestamp

 ** [customerEncryptionKeyArn](#API_agent_GetRetrievalInstruction_ResponseSyntax) **   <a name="bedrock-agent_GetRetrievalInstruction-response-customerEncryptionKeyArn"></a>
The ARN of the customer managed KMS key protecting this content, when one was supplied at create.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`

 ** [description](#API_agent_GetRetrievalInstruction_ResponseSyntax) **   <a name="bedrock-agent_GetRetrievalInstruction-response-description"></a>
A description of the retrieval instruction. On a numbered version, the description of that version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.

 ** [instruction](#API_agent_GetRetrievalInstruction_ResponseSyntax) **   <a name="bedrock-agent_GetRetrievalInstruction-response-instruction"></a>
The reviewed content this instruction serves — what AgenticRetrieveStream resolves while status is ACTIVE. Absent until the first create review passes. Always present on a numbered version.
Type: [RetrievalInstructionContent](API_agent_RetrievalInstructionContent.md) object

 ** [lastTransitionStatus](#API_agent_GetRetrievalInstruction_ResponseSyntax) **   <a name="bedrock-agent_GetRetrievalInstruction-response-lastTransitionStatus"></a>
The outcome or in-progress state of the most recent create or update. CREATING or UPDATING means the operation is still running. Independent of status. Always has a value from the create 202 onward. On a numbered version this is always CREATE\_SUCCESSFUL: a version is created once, from reviewed content, and is immutable.
Type: String
Valid Values: `CREATING | UPDATING | CREATE_SUCCESSFUL | CREATE_FAILED | UPDATE_SUCCESSFUL | UPDATE_FAILED`

 ** [lastTransitionStatusReasons](#API_agent_GetRetrievalInstruction_ResponseSyntax) **   <a name="bedrock-agent_GetRetrievalInstruction-response-lastTransitionStatusReasons"></a>
Why the most recent create or update was rejected. One entry for each rejected field, or a single entry when the review itself failed. Each entry has a machine-readable code and a message, and names the field when it applies to one. The service includes this field only when lastTransitionStatus is CREATE\_FAILED or UPDATE\_FAILED. Never present on a numbered version.
Type: Array of [RetrievalInstructionFailureReason](API_agent_RetrievalInstructionFailureReason.md) objects

 ** [latestVersion](#API_agent_GetRetrievalInstruction_ResponseSyntax) **   <a name="bedrock-agent_GetRetrievalInstruction-response-latestVersion"></a>
The largest version number that currently exists for this retrieval instruction, that is, the newest version you can retrieve. Present only on a DRAFT read, and only when at least one version exists. Because version numbers are never reused, deleting versions can leave gaps: this is the newest existing version, not a count and not the highest number ever created.
Type: String
Pattern: `[1-9][0-9]{0,8}`

 ** [name](#API_agent_GetRetrievalInstruction_ResponseSyntax) **   <a name="bedrock-agent_GetRetrievalInstruction-response-name"></a>
The name of the retrieval instruction.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `([0-9a-zA-Z][_-]?){1,100}`

 ** [retrievalInstructionArn](#API_agent_GetRetrievalInstruction_ResponseSyntax) **   <a name="bedrock-agent_GetRetrievalInstruction-response-retrievalInstructionArn"></a>
The ARN of the retrieval instruction.
Type: String
Pattern: `arn:aws(-cn|-us-gov|-eusc|-iso(-[b-f])?)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:retrieval-instruction/[a-z0-9]{10}`

 ** [retrievalInstructionId](#API_agent_GetRetrievalInstruction_ResponseSyntax) **   <a name="bedrock-agent_GetRetrievalInstruction-response-retrievalInstructionId"></a>
The identifier of the retrieval instruction.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `[a-z0-9]{10}`

 ** [status](#API_agent_GetRetrievalInstruction_ResponseSyntax) **   <a name="bedrock-agent_GetRetrievalInstruction-response-status"></a>
Specifies whether you can use the instruction. You can resolve only an ACTIVE instruction at retrieval time. Monotone: INACTIVE to ACTIVE once, never back. Numbered versions are always ACTIVE.
Type: String
Valid Values: `ACTIVE | INACTIVE`

 ** [updatedAt](#API_agent_GetRetrievalInstruction_ResponseSyntax) **   <a name="bedrock-agent_GetRetrievalInstruction-response-updatedAt"></a>
When the retrieval instruction was last updated. Equal to createdAt on a numbered version, which is immutable.
Type: Timestamp

 ** [version](#API_agent_GetRetrievalInstruction_ResponseSyntax) **   <a name="bedrock-agent_GetRetrievalInstruction-response-version"></a>
The version this response describes: a version number, or DRAFT.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 9.
Pattern: `(DRAFT|[1-9][0-9]{0,8})`

## Errors
<a name="API_agent_GetRetrievalInstruction_Errors"></a>

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
 ** fieldList **
A list of objects containing fields that caused validation errors and their corresponding validation error messages.
HTTP Status Code: 400

## See Also
<a name="API_agent_GetRetrievalInstruction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/GetRetrievalInstruction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/GetRetrievalInstruction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/GetRetrievalInstruction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/GetRetrievalInstruction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/GetRetrievalInstruction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/GetRetrievalInstruction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/GetRetrievalInstruction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/GetRetrievalInstruction)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/GetRetrievalInstruction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/GetRetrievalInstruction)
