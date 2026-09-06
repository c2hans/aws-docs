---
source_url: https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/api-reference.html
---

# API reference
<a name="api-reference"></a>

This section provides API references for the solution.

## Deployment dashboard
<a name="deployment-dashboard-3"></a>

| REST API | HTTP method | Functionality | Authorized callers |
| --- | --- | --- | --- |
|  `/deployments`  |  `GET`  | Get all deployments. | Amazon Cognito authenticated JWT token |
|  `/deployments`  |  `POST`  | Creates a new use case deployment. | Amazon Cognito authenticated JWT token |
|  `/deployments/{useCaseId}`  |  `GET`  | Gets deployment details for a single deployment. | Amazon Cognito authenticated JWT token |
|  `/deployments/{useCaseId}`  |  `PATCH`  | Updates a given deployment. | Amazon Cognito authenticated JWT token |
|  `/deployments/{useCaseId}`  |  `DELETE`  | Deletes a given deployment. | Amazon Cognito authenticated JWT token |
|  `/model-info/use-case-types`  |  `GET`  | Gets the available use case types for the deployment | Amazon Cognito authenticated JWT token |
|  `/model-info/{useCaseType}/providers`  |  `GET`  | Gets the available model providers for the given use case type | Amazon Cognito authenticated JWT token |
|  `/model-info/{useCaseType}/{providerName}`  |  `GET`  | Gets the IDs of the models available for a given provider and use case type | Amazon Cognito authenticated JWT token |
|  `/model-info/{useCaseType}/{providerName}/{modelId}`  |  `GET`  | Gets the info about the given model, including default parameters. | Amazon Cognito authenticated JWT token |

**Note**
OpenAPI and Swagger files can also be exported from API Gateway for easier integration with the API. See [Export a REST API from API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-export-api.html).

 **POST and PATCH Payloads**

See below for an example of a POST payload to the `/deployments` endpoint, which will create a new use case.

```
{
 "UseCaseName": "usecase1",
 "UseCaseDescription": "Description of the use case to be deployed. For display purposes", // optional
 "DefaultUserEmail": "placeholder@example.com", // optional, if not provided, the Cognito Group and User will not be created
 "DeployUI": true, // optional
 "VpcParams": {
 "VpcEnabled": true,
 "CreateNewVpc": false,
 // provide these if not creating new vpc
 "ExistingVpcId": "vpc-id",
 "ExistingPrivateSubnetIds": ["subnet-1", "subnet-2"],
 "ExistingSecurityGroupIds": ["sg-1", "sg-2"]
 },
 "ConversationMemoryParams": {
 "ConversationMemoryType": "DynamoDB",
 "HumanPrefix": "user", // optional
 "AiPrefix": "ai", // optional
 "ChatHistoryLength": 10 // optional
 },
 "KnowledgeBaseParams": {
 "KnowledgeBaseType": "Bedrock",
 // one of the following based on selected provider
 "BedrockKnowledgeBaseParams": {
 "BedrockKnowledgeBaseId": "my-bedrock-kb",
 "RetrievalFilter": {}, // optional
 "OverrideSearchType": "HYBRID" // optional
 },
 "KendraKnowledgeBaseParams": {
 "AttributeFilter": {}, // optional
 "RoleBasedAccessControlEnabled": true, // optional
 "ExistingKendraIndexId": "12345678-abcd-1234-abcd-1234567890ab",
 // provide the following in place of ExistingKendraIndexId if you want the solution to deploy an index for you
 "KendraIndexName": "index",
 "QueryCapacityUnits": 1, // optional
 "StorageCapacityUnits": 1, // optional
 "KendraIndexEdition": "DEVELOPER" // optional
 },
 "NoDocsFoundResponse": "Sorry, I couldn't find any relevant information for your query.", // optional
 "NumberOfDocs": 3, // optional
 "ScoreThreshold": 0.7, // optional
 "ReturnSourceDocs": true // optional
 },
 "LlmParams": {
 "ModelProvider": "Bedrock | SAGEMAKER",
 // one of the following based on selected provider
 "BedrockLlmParams": {
 "ModelId": "model-id", // use this for on demand models. Can't use with ModelArn
 "ModelArn": "model-arn", // use this for provisioned/custom models. Can't use with ModelId,
 "InferenceProfileId": "profile-id"
 "GuardrailIdentifier": "arn:aws:bedrock:us-east-1:123456789012:guardrail/my-guardrail", // optional
 "GuardrailVersion": "1" // optional. Required if GuardrailIdentifier provided.
 },
 "SageMakerLlmParams": {
 "EndpointName": "some-endpoint",
 "ModelInputPayloadSchema": {},
 "ModelOutputJSONPath": "$."
 },
 // optional. Passes on arbitrary params to the underlying LLM.
 "ModelParams": {
 "param1": {
 "Value": "value1",
 "Type": "string"
 },
 "param2": {
 "Value": 1,
 "Type": "integer"
 }
 },
 // optional
 "PromptParams": {
 "PromptTemplate": "some template",
 "UserPromptEditingEnabled": true,
 "MaxPromptTemplateLength": 1000,
 "MaxInputTextLength": 1000,
 "DisambiguationPromptTemplate": "some disambiguation template",
 "DisambiguationEnabled": true
 },
 "Temperature": 1.0, // optional
 "Streaming": true, // optional
 "RAGEnabled": true, // optional. Must be true if providing KnowledgeBaseParams above.
 "Verbose": false // optional
 },
 "AgentParams": {
 "AgentType": "Bedrock",
 "BedrockAgentParams": {
 "AgentId": "agent-id",
 "AgentAliasId": "alias-id",
 "EnableTrace": true
 }
 },
 // optional
 "AuthenticationParams": {
 "AuthenticationProvider": "Cognito",
 "CognitoParams": {
 "ExistingUserPoolId": "user-pool-id",
 "ExistingUserPoolClientId": "client-id" // optional. If not provided, the solution will create a client for you in the provided pool
 }
 }

}
```

For updates, the structure is the same as above with some caveats:
+ The use case name cannot be changed
+ A use case can only change security groups and subnets once it has been deployed in a VPC. The VPC itself cannot be changed.
+ If a Kendra index was created for you as a knowledge base, you cannot change the configuration of that index (for example, KendraIndexName, QueryCapacityUnits)

## Shared Use Case APIs
<a name="shared-use-case-apis"></a>

The following REST API endpoints are available for both Text and Bedrock Agent use cases:

| REST API | HTTP method | Functionality | Authorized callers |
| --- | --- | --- | --- |
|  `/details/{useCaseConfigKey}`  |  `GET`  | Gets configuration details for a specific use case. | Amazon Cognito authenticated JWT token |

| WebSocket API | Functionality | Authorized callers |
| --- | --- | --- |
|  `/$connect`  | Initiate WebSocket connection and authenticate user. | Amazon Cognito authenticated JWT token |
|  `/$disconnect`  | Endpoint called when a WebSocket connection has been disconnected. | Amazon Cognito authenticated JWT token |

 **Use Case Details API**

The details API endpoint retrieves information about a specific use case:

```
GET /details/{useCaseConfigKey}
```

This endpoint returns the configuration details for a specific use case, including model parameters, knowledge base settings, and other deployment information. It requires an Amazon Cognito authenticated JWT token for authorization.

## Text use case
<a name="chat-use-case-2"></a>

| WebSocket API | Functionality | Authorized callers |
| --- | --- | --- |
|  `/sendMessage`  | Sends user’s chat message to the WebSocket for processing with the configured LLM experience. | Amazon Cognito authenticated JWT token |

| REST API | HTTP method | Functionality | Authorized callers |
| --- | --- | --- | --- |
|  `/feedback/{useCaseId}`  |  `POST`  | Submits user feedback for a specific use case. | Amazon Cognito authenticated JWT token |

 **sendMessage Payloads**

If you’re directly integrating with the `/sendMessage` API, you must adhere to the following request and response payload formats.

 *Request Payload*

```
{
 "action": "sendMessage",
 "question": "the message to send to the api",
 "conversationId": "", // If not provided, a new conversation will be created, with the conversationId returned in the response. All subsequent messages in that conversation (where history is retained), should provide the conversationId there.
 "promptTemplate": "", // Optional. Overrides the configured prompt
 "authToken": "XXXX" // Optional. accessToken from cognito flow. Required for RAG with RBAC
}
```

| Parameter Name | Type | Description |
| --- | --- | --- |
|  **action**  |  `String`  | Currently we only support the "sendMessage" action on the WebSocket |
|  **question**  |  `String`  | The user input to send to the LLM |
|  **conversationId**  |  `String`  | A UUID identifying the conversation. If not provided, a new conversation will be created, with the conversationId returned in the response. All subsequent messages in that conversation (where you wish for history/context to be retained), should provide the conversationId there. |
|  **promptTemplate**  |  `String` [Optional] | Overrides the prompt template for this message. If empty or not provided, will default to the prompt set at deployment time. Must have the proper placeholders specified for the given configuration (i.e. {history} and {input} for non-RAG Sagemaker AI deployments, with the addition of {context} if using RAG for all deployments. |
|  **authToken**  |  `String` [Optional] | accessToken as obtained from the cognito auth flow. This is required when invoking a chat websocket endpoint configured for RAG with Role Based Access Control (RBAC). The cognito:groups claim list in this JWT token is used to control access to documents in the Kendra index. This parameter is **not** required for non-RAG use cases. It is also **not** required for RAG use cases that has RBAC disabled. |

 *Response Payloads*

 *Question Response*

The WebSocket API will respond with 1 (if streaming is disabled) or many (if streaming is enabled) JSON objects structured as follows for each query.

```
{
 "data": "some data",
 "conversationId": "id",
}
```

| Parameter Name | Type | Description |
| --- | --- | --- |
|  **data**  |  `String`  | A chunk of the response from the LLM if streaming is enabled, or the entire response. If using streaming, a response of this format with the data content being *END\_CONVERSATION* will be sent to indicate the end of the response to a single question. |
|  **conversationId**  |  `String`  | The ID of the conversation this sourceDocument response belongs to. |

 *Source Document Response*

If you have configured your RAG use case to return source documents, you will also receive the following payload at the end of every response for each source document used to create the response.

```
{
 "sourceDocument": {
 "excerpt": "some excerpt from the",
 "location": "s3://fake-bucket/test.txt",
 "score": 0.500,
 "document_title": null,
 "document_id": null,
 "additional_attributes": null
 },
 "conversationId": "some-id"
}
```

| Parameter Name | Type | Description |
| --- | --- | --- |
|  **excerpt**  |  `String`  | An excerpt from the source document. |
|  **location**  |  `String`  | Location of the source document. This will depend on the data sources used and type of knowledge base, but could be things like s3 URIs or websites. |
|  **score**  |  `Number` \| `String`  | The confidence that the document corresponds to the question asked. This will be a float from 0 to 1 for Bedrock, and a string (e.g. HIGH, LOW, etc.) for Kendra. |
|  **document\_title**  |  `String`  | Title of the returned source document. Only available when using Kendra. |
|  **document\_id**  |  `String`  | ID of the returned source document. Only available when using Kendra. |
|  **additional\_attributes**  |  `String`  | This field will contain all additional attributes on the document as customized on your knowledge base at ingestion. |
|  **conversationId**  |  `String`  | The ID of the conversation this sourceDocument response belongs to. |

 **Feedback API Payload**

Below is an example of a POST payload to the `/feedback/{useCaseId}` endpoint, which will submit user feedback for a specific use case:

```
{
  "useCaseRecordKey": "12345678-12345678",
  "conversationId": "12345678-1234-1234-1234-123456789012",
  "messageId": "12345678-1234-1234-1234-123456789012",
  "feedback": "positive",
  "feedbackReason": ["accurate", "helpful"],
  "comment": "This response was very helpful.",
  "rephrasedQuery": "What are the key features of Amazon Bedrock?",
  "sourceDocuments": [
    "s3://bucket-name/document1.pdf",
    "s3://bucket-name/document2.pdf"
  ]
}
```

## Bedrock Agent use case
<a name="agent-use-case-2"></a>

| WebSocket API | Functionality | Authorized callers |
| --- | --- | --- |
|  `/invokeAgent`  | Sends user’s message to the WebSocket for processing with the configured agent. | Amazon Cognito authenticated JWT token |

### invokeAgent Payloads
<a name="invokeagent-payloads"></a>

If you’re directly integrating with the `/invokeAgent API`, you must adhere to the following request and response payload formats.

 *Request payload*

```
{
"action": "invokeAgent",
"inputText": "User query to the agent",
"conversationId": "", // Optional. Empty conversationId implies a new conversation. When not provided, a new conversationId will be created and returned with the response. All subsequent messages in the same conversation should provide the same conversationId (i.e. chat memory/history is maintained).
"authToken": "XXXX" // Optional. accessToken from cognito flow. If provided, it needs to be a valid JWT token associated with the user
}
```

| Parameter name | Type | Description |
| --- | --- | --- |
|  **action**  |  `String`  | We only support the `invokeAgent` action on the WebSocket. |
|  **inputText**  |  `String`  | The user input to send to the LLM. |
|  **conversationId**  |  `String[Optional]`  | A UUID that uniquely identifies the conversation. If you don’t provide this value, the solution creates a new conversation and returns the **conversationId** in the response. All subsequent messages in that conversation (where you want to retain history and context) provide the **conversationId** there. |
|  **authToken**  |  `String[Optional]`  |  **accessToken** as obtained from the Amazon Cognito auth ﬂow. This parameter is **not** required. If you provide it, the JWT token will be validated. This helps make it easier for this solution to be extended. |

 *Response payloads*

 *Question response*

The WebSocket API will respond with one (if streaming is disabled) or many (if streaming is enabled) JSON objects structured as follows for each query.

```
{
 "data" "some data",
 "conversationId": "id",
 }
```

| Parameter name | Type | Description |
| --- | --- | --- |
|  **data**  |  `String`  | The response from the agent invocation. |
|  **conversationId**  |  `String`  | The ID of the conversation. |
