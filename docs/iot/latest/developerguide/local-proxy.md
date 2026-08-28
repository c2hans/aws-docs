---
source_url: https://docs.aws.amazon.com/iot/latest/developerguide/local-proxy.html
---

# Local proxy
<a name="local-proxy"></a>

The local proxy transmits data sent by the application running on the source device by using secure tunneling over a WebSocket secure connection. You can download the local proxy source from [GitHub](https://github.com/aws-samples/aws-iot-securetunneling-localproxy).

The local proxy can run in two modes: `source` or `destination`. In source mode, the local proxy runs on the same device or network as the client application that initiates the TCP connection. In destination mode, the local proxy runs on the remote device, along with the destination application. A single tunnel can support up to three data streams at a time by using tunnel multiplexing. For each data stream, secure tunneling uses multiple TCP connections, which reduces the potential for a time out. For more information, see [Multiplex data streams and using simultaneous TCP connections in a secure tunnel](multiplexing.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Core. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
