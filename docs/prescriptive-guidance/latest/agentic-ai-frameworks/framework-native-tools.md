---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-frameworks/framework-native-tools.html
---

# Framework-native tools
<a name="framework-native-tools"></a>

Although the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) provides a flexible foundation, framework-native tools offer advantages for specific use cases.

The [Strands Agents SDK](https://strandsagents.com/) offers lightweight, Python-based tools that require minimal overhead for simple operations. You can create tools with just a few lines of code. These tools are also tightly integrated with the Strands Agents framework.

The following example demonstrates how to create a simple weather tool using Strands Agents. You can transform Python functions into agent-accessible tools with minimal code, and Strands Agents automatically generates tool documentation from the function's docstring.

`#Example of a simple Strands native tool`

`@tool`

`def weather(location: str) -> str:`

`"""Get the current weather for a location""" #`

`Implementation here`

`return f"The weather in {location} is sunny."`

For rapid prototyping or simple use cases, framework-native tools can accelerate development. However, for production systems, MCP tools provide greater interoperability across frameworks than framework-native tools.

The following table provides an overview of other framework-specific tools.

|
|
| Framework | Tool type | Advantages | Considerations |
| --- |--- |--- |--- |
| [AutoGen](https://microsoft.github.io/autogen/docs/Use-Cases/agent_chat) | Function definitions | Strong multi-agent support | Best suited to Microsoft tooling |
| [LangChain](https://python.langchain.com/docs/concepts/tools/) | Python classes | Large library of pre-built tools | Tools are specific to the LangChain framework |
| [LlamaIndex](https://docs.llamaindex.ai/en/stable/getting_started/starter_tools/) | Python functions | Optimized for data operations | Limited to LlamaIndex |
