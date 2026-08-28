---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-frameworks/framework-native-tools.html
---

# Framework-native tools
<a name="framework-native-tools"></a>

Although the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) provides the most flexible foundation, framework-native tools offer advantages for specific use cases.

The [Strands Agents SDK](https://strandsagents.com/) offers Python-based tools characterized by their lightweight design that requires minimal overhead for simple operations. They enable quick implementation and allow developers to create tools with just a few lines of code. In addition, they're tightly integrated to work seamlessly within the Strands Agents framework.

The following example demonstrates how to create a simple weather tool using Strands Agents. Developers can quickly transform Python functions into agent-accessible tools with minimal code overhead and automatically generate appropriate documentation from the function's docstring.

`#Example of a simple Strands native tool`

`@tool`

`def weather(location: str) -> str:`

`"""Get the current weather for a location""" #`

`Implementation here`

`return f"The weather in {location} is sunny."`

For rapid prototyping or simple use cases, framework-native tools can accelerate development. However, for production systems, MCP tools provide better interoperability and future flexibility than framework-native tools.

The following table provides an overview of other framework-specific tools.

|
|
| Framework | Tool type | Advantages | Considerations |
| --- |--- |--- |--- |
| [AutoGen](https://microsoft.github.io/autogen/docs/Use-Cases/agent_chat) | Function definitions | Strong multi-agent support | Microsoft ecosystem |
| [LangChain](https://python.langchain.com/docs/concepts/tools/) | Python classes | Large ecosystem of pre-built tools | Framework lock-in |
| [LlamaIndex](https://docs.llamaindex.ai/en/stable/getting_started/starter_tools/) | Python functions | Optimized for data operations | Limited to LlamaIndex |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
