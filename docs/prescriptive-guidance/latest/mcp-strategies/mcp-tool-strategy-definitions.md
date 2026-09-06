---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-strategies/mcp-tool-strategy-definitions.html
---

# Tool definitions
<a name="mcp-tool-strategy-definitions"></a>

When an LLM receives a request that it cannot handle directly, it will review available tools to help it complete the request. The LLM selects tools based on its semantic understanding of the provided tools' names and descriptions and any instructions provided in the prompt. It will then create input based on the defined input schema and expect output based on the output schema. Therefore, creating descriptive tool definitions and validated input and output schemas is critical in helping the LLM to select tools effectively. There are generally two approaches for creating this documentation: the tool specification approach and the docstring approach.

## Tool specification approach
<a name="mcp-tool-strategy-definitions-spec-approach"></a>

The recommended approach is to directly follow the MCP [tool specification](https://modelcontextprotocol.io/specification/2025-06-18/server/tools#tool) when defining the tool. The following example is shown using the [Strands Agent](https://strandsagents.com/docs/user-guide/quickstart/overview/) tool decorator:

```
@tool(
  name = "search_website",
  description = "This tool searches the provided website for semantic matches to the query provided",
  inputSchema = {
    "json": {
      "type": "object",
      "properties": {
        "url": {
          "type": "string",
          "description": "The url of the website to load and search."
        },
        "query": {
          "type": "string",
          "description": "The content you want to try and match in the website."
      }
    },
    "required": ["url", "query"]
  },
  outputSchema = {
    "json": {
      "type": "object",
      "properties": {
      "results": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      }
    }
  }
)
def search_website:
  …
```

Using standard fields, such as `name`, `description`, `inputSchema`, and `outputSchema` makes sure that every tool has consistent documentation that both the LLM and humans can understand. Every tool should define these fields at a minimum and optionally provide a title and annotations, which are optional hints about tool behavior. When possible, use enums for parameter values to make it easy for the LLM to select the correct options. Enums work best for finite sets, such as status or priority values, but are not suitable for free-form text, dynamic values, arbitrary numbers, or resource identifiers. In those cases, provide clear descriptions and examples instead. Also include a default value when possible so the LLM does not have to guess what the correct option is. Keep in mind that tool definitions are included in the LLM prompt on each invocation, consuming context window space alongside system instructions and conversation history.

## Docstring approach
<a name="mcp-tool-strategy-definitions-docstring-approach"></a>

Another approach, if you are writing your tools in Python, is using docstrings to provide the tool's description, usage, and output. The following is an example of this approach:

```
def search_website(url: str, query: str) -> list:

    """
    This tool loads the specified website and then attempts to find content that matches the provided query through semantic search. It provides back a list of strings that are the sentences that match the query.
    Args:
      url: the website url to load
      query: the content you want to semantically match in the website
    """
```

Docstrings do not enforce a schema or standardized format. Using this approach might yield inconsistent results based on how tool developers choose to document each tool. Defining and enforcing an organization-wide standard is essential if you follow this approach.

## Best practices for MCP tool definitions
<a name="mcp-tool-strategy-definitions-best-practices"></a>
+ **Follow MCP tool specification** – Provide `name`, `description`, `inputSchema`, and `outputSchema` fields for every tool. For Python implementations, use [Pydantic models](https://docs.pydantic.dev/latest/concepts/models/) to provide inline documentation through field descriptions, automatic type validation, and constrained values through enums. This makes schemas self-documenting and improves LLM understanding of valid parameter options.
+ **Write descriptions as prompts** – Tool descriptions are instructions that guide LLM decision-making. Include the essential components of the tool's purpose (what the tool does), when to use it (user intent patterns or scenarios), the context of the output (what the output is used for), parameters, and error conditions.
+ **Provide concrete examples** – Including workflow examples with actual values is the most effective way to guide LLMs about correct tool usage.
+ **Document dependencies explicitly** – Include prerequisites, numbered sequences, state changes, and follow-up actions.
