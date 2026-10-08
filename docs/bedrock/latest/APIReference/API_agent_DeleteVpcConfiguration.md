---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_DeleteVpcConfiguration.html
---

# DeleteVpcConfiguration
<a name="API_agent_DeleteVpcConfiguration"></a>

Deletes a VPC configuration. This operation is asynchronous: it returns status `DELETING`. Poll `GetVpcConfiguration` until it returns a `ResourceNotFoundException`, indicating the configuration is deleted. Delete requests are idempotent and safe to retry.

## Request Syntax
<a name="API_agent_DeleteVpcConfiguration_RequestSyntax"></a>

```
DELETE /knowledgebases/{{knowledgeBaseId}}/vpcconfigurations/{{vpcConfigurationId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_agent_DeleteVpcConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [knowledgeBaseId](#API_agent_DeleteVpcConfiguration_RequestSyntax) **   <a name="bedrock-agent_DeleteVpcConfiguration-request-uri-knowledgeBaseId"></a>
The unique identifier of the knowledge base that owns the VPC configuration.
Pattern: `[0-9a-zA-Z]{10}`
Required: Yes

 ** [vpcConfigurationId](#API_agent_DeleteVpcConfiguration_RequestSyntax) **   <a name="bedrock-agent_DeleteVpcConfiguration-request-uri-vpcConfigurationId"></a>
The unique identifier of the VPC configuration to delete.
Length Constraints: Fixed length of 32.
Pattern: `[a-z0-9](?:[a-z0-9-]{30}[a-z0-9])`
Required: Yes

## Request Body
<a name="API_agent_DeleteVpcConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_agent_DeleteVpcConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "status": "string",
   "vpcConfigurationId": "string"
}
```

## Response Elements
<a name="API_agent_DeleteVpcConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [status](#API_agent_DeleteVpcConfiguration_ResponseSyntax) **   <a name="bedrock-agent_DeleteVpcConfiguration-response-status"></a>
The current status of the VPC configuration. Immediately after a delete request this is `DELETING`.
Type: String
Valid Values: `CREATING | CREATED | DELETING | CREATE_FAILED | DELETE_FAILED`

 ** [vpcConfigurationId](#API_agent_DeleteVpcConfiguration_ResponseSyntax) **   <a name="bedrock-agent_DeleteVpcConfiguration-response-vpcConfigurationId"></a>
The unique identifier of the VPC configuration being deleted.
Type: String
Length Constraints: Fixed length of 32.
Pattern: `[a-z0-9](?:[a-z0-9-]{30}[a-z0-9])`

## Errors
<a name="API_agent_DeleteVpcConfiguration_Errors"></a>

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
<a name="API_agent_DeleteVpcConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/DeleteVpcConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/DeleteVpcConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/DeleteVpcConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/DeleteVpcConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/DeleteVpcConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/DeleteVpcConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/DeleteVpcConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/DeleteVpcConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/DeleteVpcConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/DeleteVpcConfiguration)
