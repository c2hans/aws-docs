---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/security-infrastructure.html
---

# IVS Infrastructure Security
<a name="security-infrastructure"></a>

As a managed service, Amazon IVS is protected by the AWS global network security procedures. These are described in [Best Practices for Security, Identity, & Compliance](https://aws.amazon.com/architecture/security-identity-compliance/).

## API Calls
<a name="infrastructure-api-calls"></a>

You use AWS published API calls to access Amazon IVS through the network. Clients must support Transport Layer Security (TLS) 1.2 or later. We recommend TLS 1.3 or later (due to vulnerabilities in earlier versions). Clients must also support cipher suites with perfect forward secrecy (PFS) such as Ephemeral Diffie-Hellman (DHE) or Elliptic Curve Ephemeral Diffie-Hellman (ECDHE). Most modern systems such as Java 7 and later support these modes.

Also, API requests must be signed by using an access key ID and a secret access key that is associated with an IAM principal. Or you can use the [AWS Security Token Service](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html) to generate temporary security credentials to sign requests.

You can call these API operations from any network location, but Amazon IVS does support resource-based access policies, which can include restrictions based on the source IP address. You can also use Amazon IVS policies to control access from specific Amazon Virtual Private Cloud (Amazon VPC) endpoints or specific VPCs. Effectively, this isolates network access to a given Amazon IVS resource from only the specific VPC within the AWS network.

Also, all API requests are signed sigv4.

For API details, see the [IVS Low-Latency Streaming API Reference](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/Welcome.html), [IVS Real-Time Streaming API Reference](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/Welcome.html), and [IVS Chat API Reference](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/Welcome.html).

## Streaming and Playback
<a name="infrastructure-streaming-playback"></a>

Playback happens over HTTPS from the edge to the viewer, and the “contribution edge” (ingest endpoint) supports RTMPS (RTMP over TLS) or RTMP if the channel is configured to allow insecure ingest. Amazon IVS streaming requires TLS version 1.2 or later. Streams are not end-to-end encrypted; a stream may be transmitted unencrypted internally in the IVS network, for processing.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
