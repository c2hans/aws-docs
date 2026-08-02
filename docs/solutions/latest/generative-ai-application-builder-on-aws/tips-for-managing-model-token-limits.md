---
source_url: https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/tips-for-managing-model-token-limits.html
---

# Tips for managing model token limits
<a name="tips-for-managing-model-token-limits"></a>

Note: The solution does not directly attempt to manage token limits imposed by various LLMs. Test and ensure your prompt remains within the available limits enforced by the model provider.

To help control the size of prompts, try the following:

1. Familiarize yourself with the limits imposed by the model you want to use. These values can differ dramatically across models so it’s important to know what your available budget is before getting started.

1. Craft your initial prompt with that budget in mind and consider how much you want to save for any dynamic elements of the prompt. For example, user input, chat history, document excerpts, and so on.

1. In the prompt configuration page, set a limit for **Size of trailing history** to limit the number of conversation turns included within the prompt.

1. Set document return limits in the Knowledge Base configuration wizard. You need to try and strike the right balance between providing the LLM with enough context to perform the task, but not so much as to exceed token limits or negatively affect latency.

1. Leave some buffer. Don’t budget for the typical case, think about and experiment with the edge cases such as long input queries, large document excerpts, or long conversations.
