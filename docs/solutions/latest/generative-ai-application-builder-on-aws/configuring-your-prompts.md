---
source_url: https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/configuring-your-prompts.html
---

# Configuring your prompts
<a name="configuring-your-prompts"></a>

The Deployment dashboard wizard has a prompt configuration step which allows you to customize the prompt experience and template that will guide the interactions between users and the AI model. Properly configuring these settings is crucial for obtaining accurate and relevant responses from the AI assistant.

This section controls the overall experience and behavior of the AI prompt.
+  **Max prompt template length**: This setting determines the maximum length (in characters) of the prompt template. A higher value allows for more context to be provided to the AI model, potentially leading to more accurate responses. However, excessively long prompts may also introduce noise and negatively impact performance. For Amazon Bedrock models, the default values for max prompt template length (in characters) is calculated using the underlying model token limits. If you edit and change a model name within Bedrock, 'Reset to default' button is highlighted and can be used to adopt the newly selected model’s defaults. For Amazon SageMaker AI models, reasonable default values are provided, but it is recommended that you check your underlying model and choose these max prompt template length and input text lengths accordingly. Refer to the Tips on managing model token limits section for more information.
+  **Max input text length**: This setting limits the maximum length (in characters) of the user’s input text. Longer inputs may contain irrelevant information, increasing the risk of obtaining irrelevant or inaccurate responses from the AI model.
+  **User Prompt Editing**: This option allows you to enable or disable the ability for users to modify the prompt template through the Chat UI. Disabling this feature can help maintain consistency and prevent unintended changes to the prompt.

 **Prompt template**

This section allows you to define the actual prompt template that will be used by the AI model. The prompt template typically follows a structure that includes placeholders for various components, such as the user’s input, reference passages, and chat history.
+  **Prompt template**: This is the main text area where you can write or paste the desired prompt template. The template should be crafted to provide the necessary context and instructions to the AI model. It typically includes the following placeholders:
  +  `{input}`: This placeholder is mandatory for Sagemaker AI deployments and will be substituted with the user’s input or query.
  +  `{history}`: This placeholder is mandatory for Sagemaker AI deployments and will be substituted with the chat history of the current conversation.
  +  `{context}`: This placeholder is mandatory for RAG deployments and will be substituted with the document excerpts obtained from the configured knowledge base.
+  **Rephrase Question?**: This option (available for RAG deployments only) determines whether the user’s original input query should be rephrased or disambiguated before being passed to the AI model. Rephrasing the query can sometimes help the model better understand the user’s intent, potentially leading to more accurate responses.

When configuring the prompt template and experience, it’s essential to strike a balance between providing sufficient context and instructions to the AI model while avoiding excessively long or irrelevant information that may introduce noise or performance issues.

 **Advanced prompt settings**

This section allows you to control how the conversation history is presented to the AI model.
+  **Size of trailing history**: This setting determines the number of previous messages that should be included in the final prompt. Setting this value to zero would result in no history being injected into either the prompt template or the disambiguation prompt template. Please note: even when set to zero, a {history} placeholder is still required to exist in the prompt templates. At runtime, it will get replaced with an empty string.
  + Note: It is recommended to provide an even number for this value. Providing an odd number would result in only the AI response of a paired interaction being returned.
+  **Human Prefix**: This is the prefix used to identify messages sent by the user in the conversation history.
+  **AI Prefix**: This is the prefix used to identify messages returned by the AI model in the conversation history.

 *Disambiguation Prompt Configuration*

This section allows you to configure the behavior and template for disambiguating user inputs before sending them to the configured knowledge base.
+  **Enable Disambiguation**: This option determines whether user inputs should be disambiguated before sending to the knowledge base.
+  **Disambiguation Prompt Template**: This is the prompt template used for disambiguating user inputs when connected to a knowledge base. The output generated from this prompt will be used as the query sent to the knowledge base. Disabling disambiguation would result in the user’s raw query being sent to the knowledge base unchanged.

For example, with disambiguation enabled, a follow-up user query of "How much does it cost?" might be disambiguated to "How much does it cost renew my license plate?", leading to a better search query.
