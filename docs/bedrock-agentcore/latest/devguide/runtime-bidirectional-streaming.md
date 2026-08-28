---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-bidirectional-streaming.html
---

# Bidirectional streaming
<a name="runtime-bidirectional-streaming"></a>

Amazon Bedrock AgentCore Runtime supports bidirectional streaming, enabling real-time, two-way communication between clients and agents. This is essential for interactive applications such as conversational voice agents where both the client and agent need to send and receive data simultaneously.

AgentCore Runtime supports two protocols for bidirectional streaming:

WebSocket
A persistent, full-duplex connection over TCP. WebSocket supports text-based streaming, structured message exchange, and audio streaming with no additional infrastructure required. Clients connect to the AgentCore Runtime WebSocket endpoint using SigV4 or OAuth 2.0 authentication.

WebRTC
A protocol optimized for real-time audio and video with low latency. WebRTC is well-suited for voice agents in browser and mobile applications, using UDP-based transport for real-time media delivery.

**Topics**
+ [Bidirectional streaming with WebSocket](runtime-bidirectional-streaming-websocket.md)
+ [Bidirectional streaming with WebRTC](runtime-webrtc.md)
+ [Code examples](runtime-bidirectional-streaming-examples.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
