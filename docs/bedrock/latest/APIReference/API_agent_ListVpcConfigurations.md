---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ListVpcConfigurations.html
---

# ListVpcConfigurations
<a name="API_agent_ListVpcConfigurations"></a>

Returns a paginated list of the VPC configurations for a knowledge base. You can optionally filter by status. Use the `nextToken` parameter to retrieve additional results.

## Request Syntax
<a name="API_agent_ListVpcConfigurations_RequestSyntax"></a>

```
GET /knowledgebases/{{knowledgeBaseId}}/vpcconfigurations/?maxResults={{maxResults}}&nextToken={{nextToken}}&status={{statusFilter}} HTTP/1.1
```

## URI Request Parameters
<a name="API_agent_ListVpcConfigurations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [knowledgeBaseId](#API_agent_ListVpcConfigurations_RequestSyntax) **   <a name="bedrock-agent_ListVpcConfigurations-request-uri-knowledgeBaseId"></a>
The unique identifier of the knowledge base whose VPC configurations you want to list.
Pattern: `[0-9a-zA-Z]{10}`
Required: Yes

 ** [maxResults](#API_agent_ListVpcConfigurations_RequestSyntax) **   <a name="bedrock-agent_ListVpcConfigurations-request-uri-maxResults"></a>
The maximum number of results to return in the response. If more results are available, the response returns a `nextToken`.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_agent_ListVpcConfigurations_RequestSyntax) **   <a name="bedrock-agent_ListVpcConfigurations-request-uri-nextToken"></a>
A pagination token to retrieve the next page of results, returned in a previous response when more results are available.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `\S*`

 ** [statusFilter](#API_agent_ListVpcConfigurations_RequestSyntax) **   <a name="bedrock-agent_ListVpcConfigurations-request-uri-statusFilter"></a>
The status to filter the results by. Only VPC configurations with the specified status are returned.
Valid Values: `CREATING | CREATED | DELETING | CREATE_FAILED | DELETE_FAILED`

## Request Body
<a name="API_agent_ListVpcConfigurations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_agent_ListVpcConfigurations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "createdAt": "string",
         "description": "string",
         "hostHeader": "string",
         "name": "string",
         "port": number,
         "protocol": "string",
         "resolutionMode": "string",
         "resourceTarget": "string",
         "status": "string",
         "statusMessage": "string",
         "tlsServerName": "string",
         "vpcConfigurationId": "string",
         "vpcId": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_agent_ListVpcConfigurations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_agent_ListVpcConfigurations_ResponseSyntax) **   <a name="bedrock-agent_ListVpcConfigurations-response-items"></a>
A list of VPC configuration summaries.
Type: Array of [VpcConfigurationSummary](API_agent_VpcConfigurationSummary.md) objects

 ** [nextToken](#API_agent_ListVpcConfigurations_ResponseSyntax) **   <a name="bedrock-agent_ListVpcConfigurations-response-nextToken"></a>
A pagination token to retrieve the next page of results, present when the total number of results exceeds the maximum number of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `\S*`

## Errors
<a name="API_agent_ListVpcConfigurations_Errors"></a>

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
<a name="API_agent_ListVpcConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/ListVpcConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/ListVpcConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/ListVpcConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/ListVpcConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/ListVpcConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/ListVpcConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/ListVpcConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/ListVpcConfigurations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/ListVpcConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/ListVpcConfigurations)
