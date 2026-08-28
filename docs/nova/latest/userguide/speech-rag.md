---
source_url: https://docs.aws.amazon.com/nova/latest/userguide/speech-rag.html
---

# Implementing RAG
<a name="speech-rag"></a>

**Note**
This documentation is for Amazon Nova Version 1. For the Amazon Nova 2 Sonic guide, visit [Tool configuration](https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-tool-configuration.html).

Retrieval-Augmented Generation (RAG) enhances responses by retrieving and incorporating information from your knowledge bases. With Amazon Nova Sonic, RAG is implemented through tool use.

## Knowledge base implementation outline
<a name="speech-rag-implement"></a>

Implementing a RAG requires the following elements:
+ **Configure the tool** - Define a knowledge base search tool in your `promptStart` event.
+ **Receive Tool Use Request** - When the user asks a question, the model will call the knowledge base tool.
+ **Query Vector Database** - Execute the search query against your vector database.
+ **Return Results** - Send the search results back to the model.
+ **Generate Response** - The model incorporates the retrieved information in its spoken response.

## Knowledge base configuration
<a name="speech-rag-tool"></a>

Here is an example configuration of a basic knowledge base tool:

```
{
     toolSpec: {
         name: "knowledgeBase",
         description: "Search the company knowledge base for information",
         inputSchema: {
             json: JSON.stringify({
                 type: "object",
                 properties: {
                     query: {
                         type: "string",
                         description: "The search query to find relevant information"
                     }
                 },
                 required: ["query"]
             })
         }
     }
 };
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Nova. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query nova` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
