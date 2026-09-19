---
source_url: https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/integration-guide.html
---

# Integration guide
<a name="integration-guide"></a>

The entire solution is designed to be easily extensible. The orchestration layer of this solution is built using [LangChain](https://www.langchain.com/). You can add any model provider, knowledge base, or conversation memory type supported by LangChain (or a third party that provides LangChain connectors for these components) to this solution.

## Expanding supported LLMs
<a name="expanding-supported-llms"></a>

To add another model provider, such as a custom LLM provider, you must update the following three components of the solution:

1. Create a new `TextUseCase` CDK stack, which deploys the chat application configured with your custom LLM provider:

   1. Clone this solution’s [GitHub repository](https://github.com/aws-solutions/generative-ai-application-builder-on-aws), and set up your build environment by following the instructions provided in the [README.md](https://github.com/aws-solutions/generative-ai-application-builder-on-aws/blob/main/README.md) file.

   1. Copy (or create new) the `source/infrastructure/lib/bedrock-chat-stack.ts` file, paste it to the same directory, and rename it to `custom-chat-stack.ts`.

   1. Rename the class in the file to a suitable one, such as `CustomLLMChat`.

   1. You can choose to add a Secrets Manager secret to this stack, which stores your credentials for your custom LLM. You can retrieve these credentials during model invocation in the chat Lambda layer discussed in the next paragraph.

1. Build and attach a Lambda layer containing the Python library of the model provider to be added. For an Amazon Bedrock use case chat application, the `langchain-aws` Python library contains the custom connectors on top of the LangChain package to connect to the AWS model providers (Amazon Bedrock and SageMaker AI), knowledge bases (Amazon Kendra and Amazon Bedrock Knowledge Bases), and memory types (such as DynamoDB). Similarly, other model providers have their own connectors. This layer helps you attach this model provider’s Python library so that you can use these connectors in the chat Lambda layer, which invokes the LLM (step 3). In this solution, a custom asset bundler is used to build Lambda layers, which are attached using CDK aspects. To create a new layer for the custom model provider library:

   1. Navigate to the `LambdaAspects` class in the `source/infrastructure/lib/utils/lambda-aspects.ts` file.

   1. Follow the instructions on how to extend the functionality of the Lambda aspects class provided in the file (such as adding the `getOrCreateLangchainLayer` method). To use this new method (for example, `getOrCreateCustomLLMLayer`), also update the `LLM_LIBRARY_LAYER_TYPES` enum in the `source/infrastructure/lib/utils/constants.ts` file.

1. Extend the `chat` Lambda function to implement a builder, client, and handler for the new provider.

   The `source/lambda/chat` contains the LangChain connections for different LLMs along with the supporting classes to build these LLMs. These supporting classes follow Builder and Object Oriented design patterns to create the LLM.

   Each handler (for example, `bedrock_handler.py`) first creates a *client*, checks the environment for required environment variables, and then calls a `get_model` method to get the LangChain LLM class. The generate method is then called to invoke the LLM and get its response. LangChain currently supports streaming functionality for Amazon Bedrock, but not SageMaker AI. Based on streaming or non-streaming functionality, appropriate WebSocket handler (`WebsocketStreamingCallbackHandler` or `WebsocketHandler`) is called to send the response back to the WebSocket connection using the `post_to_connection` method.

   The `clients/builder` folder contains the classes which help build an LLM Builder using Builder pattern. First, a `use_case_config` is retrieved from a DynamoDB configurations store, which stores the details on what type of knowledge base, conversation memory, and model to construct. It also contains relevant model details such as model parameters and prompts. The Builder then helps in following the steps for creating a knowledge base, creating a conversation memory to maintain conversation context for LLM, setting the appropriate LangChain callbacks for streaming and non-streaming cases, and creating an LLM model based on the provided model conﬁgurations. The DynamoDB configuration is stored at the time of use case creation when you deploy a use case from the Deployment dashboard (or when it is provided by the users in standalone use case stack deployments without the Deployment dashboard).

   The `clients/factories` subfolder helps set the appropriate conversation memory and knowledge base class, based on the LLM configruation. This enables easy extension to any other knowledge base or memory types that you want your implementation to support.

   The `shared` subfolder contains specific implementations of knowledge base and conversation memory which are instantiated inside the factories by the builder. It also contains Amazon Kendra and Amazon Bedrock Knowledge Base retrievers called within LangChain to retrieve documents for the RAG use cases, along with callbacks, which are used by the LangChain LLM model.

   The LangChain implementations use LangChain Expression Language (LCEL) to compose conversation chains together. `RunnableWithMessageHistory` class is used to maintain conversation history with custom LCEL chains, enabling functionalities such as returning source documents and using the rephrased (or disambiguated) question sent to the knowledge base to also be sent to the LLM.

   To create your own implementation of a custom provider, you can:

   1. Copy the `bedrock_handler.py` file and create your custom handler (for example, `custom_handler.py`), which creates your custom client (for example, `CustomProviderClient`) (specified in the following step.)

   1. Copy `bedrock_client.py` in the clients folder. Rename it to `custom_provider_client.py` (or your specific model provider name, such as `CustomProvider`). Name the class within it appropriately, such as `CustomProviderClient` which inherits `LLMChatClient`.

      You can use the methods provided by `LLMChatClient` or write your own implementations to override these.

      The `get_model` method builds a `CustomProviderBuilder` (see the following step), and calls the `construct_chat_model` method that constructs the chat model using builder steps. This method acts as the *Director* in the builder pattern.

   1. Copy `clients/builders/bedrock_builder.py` and rename it to `custom_provider_builder.py` and the class within it to `CustomProviderBuilder` that inherits LLMBuilder (`llm_builder.py`). You can use the methods provided by LLMBuilder or write your own implementations to override these. The builder steps are called in sequence inside the client’s `construct_chat_model` method, such as `set_model_defaults`, `set_knowledge_base`, and `set_conversation_memory`.

      The `set_llm_model` method would create the actual LLM model using all of the values that are set using the methods called before it. Specifically, you can create a RAG (`CustomProviderRetrievalLLM`) or non-RAG (`CustomProviderLLM`) LLM, based on the `rag_enabled variable` that is retrieved from the LLM configuration in DynamoDB.

      This configuration is fetched in the `retrieve_use_case_config` method in the `LLMChatClient` class.

   1. Implement your `CustomProviderLLM` or `CustomProviderRetrievalLLM` implementation in the `llm_models` subfolder based on whether you require RAG or non-RAG use case. Most functionalities to implement these models are provided in their `BaseLangChainModel` and `RetrievalLLM` classes respectively, for non-RAG and RAG use cases.

      You can copy the `llm_models/bedrock.py` file and make the necessary changes to call the LangChain model that refer to your custom provider. For example, Amazon Bedrock uses a `ChatBedrock` class to create a chat model using LangChain.

      The generate method generates the LLM response using the LangChain LCEL *chains*.

      You can also use the `get_clean_model_params` method to sanitize the model parameters per LangChain or your model requirements.

## Expanding supported Strands tools
<a name="expanding-strands-tools"></a>

The Solution enables you to build and deploy MCP servers, AI agents, and multi-agent workflows. Within the Agent Builder experience, you can attach MCP servers to give your agents additional capabilities. In addition to MCP servers, you can leverage built-in tools provided by [Strands](https://strandsagents.com/latest/documentation/docs/user-guide/concepts/tools/community-tools-package/) (the underlying framework used by the solution).

Out of the box, the solution comes pre-configured with the following Strands tools:
+ Current Time (enabled by default)
+ Calculator (enabled by default)
+ Environment

 **MCP Server and Tools selection in the Agent Builder wizard showing built-in Strands tools**

![builtin strands tools](https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/images/builtin-strands-tools.png)

To extend your agents with additional Strands tools, follow the four-step process outlined in this section.

### Step 1: Find the Strands tool
<a name="find-the-strands-tool"></a>

Browse the [available Strands tools](https://strandsagents.com/latest/documentation/docs/user-guide/concepts/tools/community-tools-package/#available-tools) to identify the tool you want to use. Each tool has specific capabilities and configuration requirements.

For example, to add Amazon Bedrock Knowledge Base retrieval capabilities, you would use the [retrieve](https://github.com/strands-agents/tools/blob/main/src/strands_tools/retrieve.py) tool.

### Step 2: Update the SSM parameter
<a name="update-ssm-parameter"></a>

To make a tool available in the Agent Builder deployment UI, update the AWS Systems Manager Parameter Store parameter that defines which Strands tools are supported.

1. Navigate to the AWS Systems Manager Parameter Store in your AWS account.

1. Locate the parameter: `/gaab/<stack-name>/strands-tools`

1. Add your tool configuration to the end of the existing list using the following JSON structure:

   ```
   {
     "name": "Bedrock KB Retrieve",
     "description": "Retrieve information from Bedrock Knowledge Base",
     "value": "retrieve",
     "category": "AI",
     "isDefault": false
   }
   ```

<table>
<thead>
  <tr><th>Field</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td> <b>name</b> </td><td>Display name shown in the Agent Builder UI</td></tr>
  <tr><td> <b>description</b> </td><td>Brief description of the tool’s functionality</td></tr>
  <tr><td> <b>value</b> </td><td>The exact tool name as defined in the Strands tools package</td></tr>
  <tr><td> <b>category</b> </td><td>Organizational category for grouping tools in the UI</td></tr>
  <tr><td> <b>isDefault</b> </td><td>Whether the tool should be enabled by default for new agents</td></tr>
</tbody>
</table>

### Step 3: Configure environment variables
<a name="configure-environment-variables"></a>

Many Strands tools require environment variables for configuration. You can set these variables in two ways:

 **Option 1: Direct configuration on AgentCore Runtime**

Update the deployed agent directly on Amazon Bedrock AgentCore Runtime with the required environment variables.

 **Option 2: Model Parameters in the deployment wizard**

Add environment variables during the Model selection step in the Agent Builder wizard using the Model Parameters section. Environment variables that follow the naming convention `ENV_<ALL_CAPS_TOOL_NAME>_<env_variable_name>` will automatically be loaded at runtime into the agent’s execution environment as `<env_variable_name>`.

For example:
+  `ENV_RETRIEVE_KNOWLEDGE_BASE_ID` becomes `KNOWLEDGE_BASE_ID`
+  `ENV_RETRIEVE_MIN_SCORE` becomes `MIN_SCORE`

 **Advanced model parameters section showing ENV\_RETRIEVE\_KNOWLEDGE\_BASE\_ID configuration**

![model parameters env vars](https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/images/model-parameters-env-vars.png)

Refer to the specific tool’s documentation or source code to identify required environment variables. For the retrieve tool, you can find configuration options in the [source code](https://github.com/strands-agents/tools/blob/main/src/strands_tools/retrieve.py#L293).

### Step 4: Add IAM permissions
<a name="add-iam-permissions"></a>

Manually add any necessary IAM permissions to your AgentCore Runtime execution role to allow the agent to use the tool.

For example, to use the retrieve tool with Amazon Bedrock Knowledge Bases:

1. Navigate to the IAM console in your AWS account.

1. Locate the AgentCore Runtime execution role for your agent.

1. Add the following permission:

   ```
   {
     "Effect": "Allow",
     "Action": "bedrock:Retrieve",
     "Resource": "arn:aws:bedrock:region:account-id:knowledge-base/knowledge-base-id"
   }
   ```

 **IAM console showing the StrandsRetrieveToolKBAccess policy attached to the AgentCore Runtime execution role**

![agent execution role update IAM](https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/images/agent-execution-role-update-IAM.png)

The specific permissions required will vary based on the tool. Consult the tool’s documentation and AWS service documentation to determine the appropriate IAM permissions.

### Step 5: Test the agent
<a name="test-the-agent"></a>

After completing the configuration steps, test your agent to verify the tool is working correctly. You should see tool invocations in the agent’s execution logs and responses.

 **Agent successfully using the retrieve tool to answer a question about skate parks**

![strands retrieve tool example](https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/images/strands-retrieve-tool-example.png)

**Note**
For a complete list of available Strands tools and their capabilities, refer to the [Strands Community Tools documentation](https://strandsagents.com/latest/documentation/docs/user-guide/concepts/tools/community-tools-package/).

## Expanding supported knowledge bases and conversation memory types
<a name="expanding-supported-kb-and-cm-types"></a>

To add your implementations of conversation memory or knowledge base, add the required implementations in the `shared` folder and then edit the factories and appropriate enumerations to create an instance of these classes.

When you supply the LLM configuration, which is stored inside the parameter store, the appropriate conversation memory and knowledge base will be created for your LLM. For example, when the `ConversationMemoryType` is specified as DynamoDB, an instance of `DynamoDBChatMessageHistory` (available inside `shared_components/memory/ddb_enhanced_message_history.py`) is created. When the `KnowledgeBaseType` is specified as Amazon Kendra, an instance of `KendraKnowledgeBase` (available inside `shared_components/knowledge/kendra_knowledge_base.py`) is created.

## Building and deploying the code changes
<a name="building-and-deploying-code-changes"></a>

Build the program with the `npm run build` command. Once any errors are resolved, run `cdk synth` to generate the template files and all the Lambda assets.

1. You can use the `0/stage-assets.sh` script to manually stage any generated assets to the staging bucket in your account.

1. Use the following command to deploy or update platform:

   ```
   cdk deploy DeploymentPlatformStack --parameters AdminUserEmail='admin-email@amazon.com'
   ```

   Any additional AWS CloudFormation parameters should also be supplied along with the **AdminUserEmail** parameter.
