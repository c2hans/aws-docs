---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_DeleteRetrievalInstruction.html
---

# DeleteRetrievalInstruction
<a name="API_agent_DeleteRetrievalInstruction"></a>

Deletes a retrieval instruction or a single version of it. Omit retrievalInstructionVersion to delete the retrieval instruction itself; the service rejects that request with ConflictException while the retrieval instruction has versions or while lastTransitionStatus is CREATING or UPDATING. Specify retrievalInstructionVersion to delete only that version; the retrieval instruction and its other versions are unaffected.

## Request Syntax
<a name="API_agent_DeleteRetrievalInstruction_RequestSyntax"></a>

```
DELETE /retrievalinstructions/{{retrievalInstructionId}}?retrievalInstructionVersion={{retrievalInstructionVersion}} HTTP/1.1
```

## URI Request Parameters
<a name="API_agent_DeleteRetrievalInstruction_RequestParameters"></a>

The request uses the following URI parameters.

 ** [retrievalInstructionId](#API_agent_DeleteRetrievalInstruction_RequestSyntax) **   <a name="bedrock-agent_DeleteRetrievalInstruction-request-uri-retrievalInstructionId"></a>
The identifier of the retrieval instruction to delete.
Length Constraints: Fixed length of 10.
Pattern: `[a-z0-9]{10}`
Required: Yes

 ** [retrievalInstructionVersion](#API_agent_DeleteRetrievalInstruction_RequestSyntax) **   <a name="bedrock-agent_DeleteRetrievalInstruction-request-uri-retrievalInstructionVersion"></a>
The version to delete. Omit this field to delete the retrieval instruction itself, which you can do only when it has no versions; while any version exists the service rejects the request with ConflictException. You cannot delete DRAFT on its own; deleting the retrieval instruction removes it.
Pattern: `[1-9][0-9]{0,8}`

## Request Body
<a name="API_agent_DeleteRetrievalInstruction_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_agent_DeleteRetrievalInstruction_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "retrievalInstructionArn": "string",
   "retrievalInstructionId": "string",
   "version": "string"
}
```

## Response Elements
<a name="API_agent_DeleteRetrievalInstruction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [retrievalInstructionArn](#API_agent_DeleteRetrievalInstruction_ResponseSyntax) **   <a name="bedrock-agent_DeleteRetrievalInstruction-response-retrievalInstructionArn"></a>
The ARN of the retrieval instruction.
Type: String
Pattern: `arn:aws(-cn|-us-gov|-eusc|-iso(-[b-f])?)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:retrieval-instruction/[a-z0-9]{10}`

 ** [retrievalInstructionId](#API_agent_DeleteRetrievalInstruction_ResponseSyntax) **   <a name="bedrock-agent_DeleteRetrievalInstruction-response-retrievalInstructionId"></a>
The identifier of the deleted retrieval instruction.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `[a-z0-9]{10}`

 ** [version](#API_agent_DeleteRetrievalInstruction_ResponseSyntax) **   <a name="bedrock-agent_DeleteRetrievalInstruction-response-version"></a>
The version that you deleted. Absent when you deleted the whole retrieval instruction.
Type: String
Pattern: `[1-9][0-9]{0,8}`

## Errors
<a name="API_agent_DeleteRetrievalInstruction_Errors"></a>

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
<a name="API_agent_DeleteRetrievalInstruction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/DeleteRetrievalInstruction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/DeleteRetrievalInstruction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/DeleteRetrievalInstruction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/DeleteRetrievalInstruction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/DeleteRetrievalInstruction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/DeleteRetrievalInstruction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/DeleteRetrievalInstruction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/DeleteRetrievalInstruction)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/DeleteRetrievalInstruction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/DeleteRetrievalInstruction)
