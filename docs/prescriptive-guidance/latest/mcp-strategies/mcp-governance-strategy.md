---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-strategies/mcp-governance-strategy.html
---

# MCP governance strategy
<a name="mcp-governance-strategy"></a>

The other critical capability that MCP offers organizations is support for centralized governance. Your MCP governance strategy should address authentication and authorization to both the MCP servers as well as the resources they access. It should also address rate limiting to protect downstream resources, operational metrics for monitoring tool usage and performance, and managing deployments and distribution of MCP servers.

## Authentication and authorization
<a name="mcp-governance-strategy-auth"></a>

One of the most important parts of your authentication and authorization strategy is managing downstream resource access from MCP servers. When a user calls an agent, authentication and authorization is performed to ensure the user has permissions to call the agent. Then, the agent orchestrates calling specific tools in MCP servers. You need to decide how to authorize access on a per-tool basis.

One option is *machine-to-machine authorization*, where user consent or interaction is not required. For example, a time-based agent invocation uses an MCP server to collect logs from an application and analyze them. In this scenario, the agent is pre-authorized to access the specified data. The second option is *user-delegated access*, where a user provides their consent to access user-specific data and resources.

The following table shows authentication and authorization patterns.

|
|
| **Factor** | **User-delegated access** | **Machine-to-machine** |
| --- |--- |--- |
| Data ownership | User-specific authorization to data | System or organization-wide data |
| User interaction | User is present and can consent | No user interaction |
| Operation timing | Interactive or real-time | Background, scheduled, or batch |
| Permission scope | Permissions vary by user | Consistent permissions at the agent level |

User-delegated access requires careful implementation and should be developed with your security team. Agents must be able to evaluate which tools an LLM has selected and whether they require additional authorization. MCP tools must include descriptions to indicate their authentication and authorization requirements and where to retrieve access tokens. Client applications must support intermediate authentication requests, and the MCP client must provide the retrieved credentials back to the agent for each tool call.

You should ensure that MCP tools always have their own tokens to access external capabilities and that the access is logged and audited. User credentials should not be propagated through your agentic system. For example, your MCP servers should not use the same token to access data that was used to invoke the agent. Downstream calls should use explicitly scoped, purpose-generated tokens. This helps provide additional guardrails to prevent unintended data access on-behalf of actions. It can also help prevent hallucinations from producing unintended results. Imagine that a user with full admin permissions asks an agent to clone a production database for use in pre-production. To do so, the user only needs `READ` and `CREATE` permissions. Let's say the LLM hallucinates and believes it needs to clean up the old database as part of this request. If it reuses the user's credentials, it would likely succeed because the user's original credentials have `DELETE` permissions. Instead, if the MCP server uses an intentionally scoped-down token for the request with just `READ` and `CREATE` permissions, the attempt to delete the production database would fail.

You can use [Amazon Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/common-use-cases.html) to help implement these patterns. Make sure that you make an intentional choice about whether the permissions to list and invoke tools hosted by an MCP server implies permission to the external capabilities that the MCP server exposes. This identity flow from the MCP server to the resource and back to the user is dependent on the type of authentication and authorization service being used. You must decide how this is handled at scale for your MCP servers.

When designing your authentication and authorization patterns, implement token isolation mechanisms that retrieve different access tokens for each tool being accessed. Do not reuse tokens between tools and servers. AgentCore Identity provides this token isolation capability. It automatically manages both workload tokens (for machine-to-machine authentication) and user tokens (for user-delegated access) to ensure proper separation and prevent permission escalation. This is especially critical when incorporating remote MCP servers or MCP gateways.

### Best practices for MCP authentication and authorization
<a name="best-practices-for-mcp-authentication-and-authorization.d06a1469-7b5c-589d-9d0a-1c3189b3a950"></a>
+ **Token separation** – Do not pass bearer tokens from callers to downstream services. Validate the aud (audience) field matches the server receiving the token. The audience claim specifies which service the token is intended for, preventing unauthorized token reuse across different MCP servers.
+ **Select an access approach** – Choose between machine-to-machine and user-delegated access for each tool your MCP servers provide. Consider grouping tools together in the same MCP server that use the same authentication pattern.

## Controlling load
<a name="controlling-load"></a>

As with any distributed system, you must consider how to control load in your MCP server fleet. First, you consider whether to implement rate limiting in your MCP servers and where to implement the limits. If you choose not to implement rate limiting, you pass on any rate limiting performed by downstream resources. Many systems choose to rate limit based on request attributes, such as a user or account ID. Validate that the requests sent to downstream services carry on those same attributes so that multiple users are not affected by load being driven by another user.

If you do choose to implement rate limiting, the recommended approach is to implement primary rate limiting at the MCP server level, with backend services providing secondary protection and agents adapting their behavior based on rate limit feedback. Consider whether the rate limits are per-MCP server or per-tool. Per-MCP server rate limits help protect your MCP server fleet and services in a multi-tenant environment. However, that can be very coarse-grained. Per-tool rate limits are designed to prevent overwhelming downstream resources that might not sufficiently rate limit themselves. If a tool calls multiple APIs, you should set the rate limit to align to the lowest rate allowed by those APIs.

Passing rate limit information in HTTP headers can also be a useful metric for users and automated systems to help manage their own request rate and retry strategy. For example, you might send these headers back to the agent from your MCP server, as shown in the following example:

```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 45
X-RateLimit-Reset: 1640995200
```

Additionally, consider load shedding to protect the overall service when no single customer is exceeding a rate limit but the load is impacting the system's performance.

### Best practices for controlling load
<a name="best-practices-for-controlling-load.4689455f-6589-5d78-bf8e-cdc33592ef94"></a>
+ **Choose a rate-limiting approach** – Plan to rate limit individual users based on either their use of downstream resources or through their use of your MCP server and tools.
+ **Consider load shedding** – Protect your MCP server fleet from general overload that is not driven by a single or handful of customers.

## Operational metrics
<a name="mcp-governance-strategy-metrics"></a>

Key metrics to capture for MCP implementations should focus on the customer experience they deliver. These metrics commonly include token usage, tool selection accuracy, number of tools registered with the agent, and tool latency. For example, monitoring output tokens returned by each tool enables you to set alarms when tools exceed a threshold for context window usage. When a tool exceeds that threshold, you might want to review the tool's behavior. This ties into the MCP tool design strategy as well. Tool selection accuracy metrics indicate how well agents choose appropriate tools for given tasks, while execution speed and success rates highlight performance bottlenecks and reliability issues.

For example, to evaluate the tool-selection and tool-use accuracy metrics, AWS teams created golden datasets for regression testing. The datasets were generated synthetically by using LLMs from historical API invocation logs upon user queries. Using the pre-defined tool-selection and tool-use metrics (such as tool selection accuracy, tool parameter accuracy, and multi-turn function call accuracy), the AWS teams could objectively evaluate the AI agent's ability to correctly identify the appropriate tools, populate their parameters with accurate values, and maintain coherent tool invocation sequences across conversational turns.

Measuring metrics about the number of tools registered with an agent can help you identify potential context window management challenges as well as changes in the available tools presented by MCP servers. You should regularly review operational metrics that indicate the user experience with your MCP server and tools.
