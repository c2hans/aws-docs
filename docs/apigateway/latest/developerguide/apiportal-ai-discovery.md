---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/apiportal-ai-discovery.html
---

# Identify AI-facing endpoints with API Portal

AI endpoint identification is an optional discovery feature. When it's on, discovery also inspects each API's traffic for the protocol signatures of three kinds of AI endpoint and records them as the API's *workloads* in the inventory, so AI-facing endpoints appear alongside your other APIs and can be managed and documented the same way.
+ **MCP**: an endpoint that speaks the Model Context Protocol, such as an MCP server.
+ **A2A**: an endpoint that speaks the Agent2Agent protocol, such as an A2A server (agent).
+ **LLM**: an endpoint that carries traffic to or from a large language model (LLM) inference server or gateway.

Identification works from protocol signals in request and response headers (and, for A2A, a query parameter) and from well-known paths. API Portal records *that* an API carries a given protocol; it doesn't read or store the content. For an MCP server, API Portal reports the method and path that serve MCP traffic, but not the tools the server exposes; for an A2A server, not its agent card; for an LLM endpoint, not the prompts or completions.

## What API Portal looks for
<a name="apiportal-ai-discovery-signals"></a>

An API is labeled with a workload when its traffic carries one of the following signals. Clients that don't send them aren't identified, even if they speak the protocol.

| Workload | Signal |
| --- | --- |
| MCP | The MCP-Protocol-Version request header. MCP clients send it on every request from protocol version 2025-06-18; servers that negotiate an earlier version don't produce it and aren't identified. |
| A2A | The A2A-Version request header or query parameter (A2A protocol 1.0), or a request to the /.well-known/agent-card.json path. |
| LLM | A well-known inference path such as /v1/chat/completions or /v1/embeddings, or an ambiguous path such as /generate together with a known LLM gateway or server header (for example an x-litellm-\*, X-Kong-LLM-\*, or X-Inference-Time response header, or an X-Vllm-\* request header). |

If an endpoint you expect to see labeled isn't, check that its clients send the version header for MCP or A2A. Labels typically appear within a few hours of the first matching request.

## Considerations
<a name="apiportal-ai-discovery-considerations"></a>
+ Workloads are detected from request and response headers (and, for A2A, a query parameter). API Portal doesn't inspect or store request or response bodies, so it doesn't see tool definitions, agent cards, prompts, or completions.
+ An API can report more than one workload. An API with no detected workload shows none.
+ AI discovery is set per discovery configuration, so it applies to every account in an organization-scoped configuration.
+ Workloads appear only after traffic that uses the protocol has been observed. An MCP, A2A, or LLM endpoint that hasn't received traffic isn't labeled, even if it's discovered from configuration.

**To turn on AI discovery**

1. Under **API Portal**, choose **API inventory**, and then **Discovery settings** (or set this when you enable discovery).

1. Select **AI discovery**, and save.

In the inventory, filter on the **Workloads** column to see your AI-facing endpoints.

```
aws apiportal put-discovery-configuration \
    --discovery-sources API_GATEWAY ELB CLOUDFRONT \
    --features AI_DISCOVERY \
    --region us-east-1
```
