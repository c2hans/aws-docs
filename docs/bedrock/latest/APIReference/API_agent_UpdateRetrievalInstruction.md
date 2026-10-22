---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_UpdateRetrievalInstruction.html
---

# UpdateRetrievalInstruction
<a name="API_agent_UpdateRetrievalInstruction"></a>

Updates the content of a retrieval instruction. The update is processed asynchronously; the stored content is a candidate until content review passes, and the served content does not change while the update is in flight. The service rejects the request with ConflictException while lastTransitionStatus is CREATING or UPDATING.

## Request Syntax
<a name="API_agent_UpdateRetrievalInstruction_RequestSyntax"></a>

```
PUT /retrievalinstructions/{{retrievalInstructionId}} HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "instruction": {
      "answerFormat": "{{string}}",
      "answerPolicy": "{{string}}",
      "persona": "{{string}}",
      "retrievalGuidance": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_agent_UpdateRetrievalInstruction_RequestParameters"></a>

The request uses the following URI parameters.

 ** [retrievalInstructionId](#API_agent_UpdateRetrievalInstruction_RequestSyntax) **   <a name="bedrock-agent_UpdateRetrievalInstruction-request-uri-retrievalInstructionId"></a>
The identifier of the retrieval instruction to update.
Length Constraints: Fixed length of 10.
Pattern: `[a-z0-9]{10}`
Required: Yes

## Request Body
<a name="API_agent_UpdateRetrievalInstruction_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_agent_UpdateRetrievalInstruction_RequestSyntax) **   <a name="bedrock-agent_UpdateRetrievalInstruction-request-description"></a>
A replacement description; applied together with the content when the review passes. Omit to clear.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

 ** [instruction](#API_agent_UpdateRetrievalInstruction_RequestSyntax) **   <a name="bedrock-agent_UpdateRetrievalInstruction-request-instruction"></a>
The replacement instruction content. This is a full replacement of all four fields, not a patch. During UPDATING, Get continues to return the previously-served content until the update review passes.
Type: [RetrievalInstructionContent](API_agent_RetrievalInstructionContent.md) object
Required: Yes

## Response Syntax
<a name="API_agent_UpdateRetrievalInstruction_ResponseSyntax"></a>

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
<a name="API_agent_UpdateRetrievalInstruction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_agent_UpdateRetrievalInstruction_ResponseSyntax) **   <a name="bedrock-agent_UpdateRetrievalInstruction-response-createdAt"></a>
When you created the retrieval instruction.
Type: Timestamp

 ** [lastTransitionStatus](#API_agent_UpdateRetrievalInstruction_ResponseSyntax) **   <a name="bedrock-agent_UpdateRetrievalInstruction-response-lastTransitionStatus"></a>
Always UPDATING on this response. Poll GetRetrievalInstruction until this member is neither CREATING nor UPDATING, then read the outcome from it.
Type: String
Valid Values: `CREATING | UPDATING | CREATE_SUCCESSFUL | CREATE_FAILED | UPDATE_SUCCESSFUL | UPDATE_FAILED`

 ** [name](#API_agent_UpdateRetrievalInstruction_ResponseSyntax) **   <a name="bedrock-agent_UpdateRetrievalInstruction-response-name"></a>
The name of the retrieval instruction.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `([0-9a-zA-Z][_-]?){1,100}`

 ** [retrievalInstructionArn](#API_agent_UpdateRetrievalInstruction_ResponseSyntax) **   <a name="bedrock-agent_UpdateRetrievalInstruction-response-retrievalInstructionArn"></a>
The ARN of the retrieval instruction.
Type: String
Pattern: `arn:aws(-cn|-us-gov|-eusc|-iso(-[b-f])?)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:retrieval-instruction/[a-z0-9]{10}`

 ** [retrievalInstructionId](#API_agent_UpdateRetrievalInstruction_ResponseSyntax) **   <a name="bedrock-agent_UpdateRetrievalInstruction-response-retrievalInstructionId"></a>
The identifier of the retrieval instruction.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `[a-z0-9]{10}`

 ** [status](#API_agent_UpdateRetrievalInstruction_ResponseSyntax) **   <a name="bedrock-agent_UpdateRetrievalInstruction-response-status"></a>
Whether the instruction can be used. An update never lowers status. Unchanged from the previous value on this response.
Type: String
Valid Values: `ACTIVE | INACTIVE`

 ** [updatedAt](#API_agent_UpdateRetrievalInstruction_ResponseSyntax) **   <a name="bedrock-agent_UpdateRetrievalInstruction-response-updatedAt"></a>
When the retrieval instruction was last updated.
Type: Timestamp

## Errors
<a name="API_agent_UpdateRetrievalInstruction_Errors"></a>

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

 ** ThrottlingException **
The number of requests exceeds the limit. Resubmit your request later.
HTTP Status Code: 429

 ** ValidationException **
Input validation failed. Check your request parameters and retry the request.
 ** fieldList **
A list of objects containing fields that caused validation errors and their corresponding validation error messages.
HTTP Status Code: 400

## See Also
<a name="API_agent_UpdateRetrievalInstruction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/UpdateRetrievalInstruction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/UpdateRetrievalInstruction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/UpdateRetrievalInstruction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/UpdateRetrievalInstruction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/UpdateRetrievalInstruction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/UpdateRetrievalInstruction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/UpdateRetrievalInstruction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/UpdateRetrievalInstruction)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/UpdateRetrievalInstruction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/UpdateRetrievalInstruction)
