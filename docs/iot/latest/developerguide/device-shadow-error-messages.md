---
source_url: https://docs.aws.amazon.com/iot/latest/developerguide/device-shadow-error-messages.html
---

# Device Shadow error messages
<a name="device-shadow-error-messages"></a>

The Device Shadow service publishes a message on the error topic (over MQTT) when an attempt to change the state document fails. This message is only emitted as a response to a publish request on one of the reserved `$aws` topics. If the client updates the document using the REST API, then it receives the HTTP error code as part of its response, and no MQTT error messages are emitted.

| HTTP error code | Error messages |
| --- | --- |
| 400 (Bad Request) |  +  Invalid JSON <br />+  Missing required node: state <br />+  State node must be an object <br />+  Desired node must be an object <br />+  Reported node must be an object <br />+  Invalid version <br />+  Invalid clientToken  A client token that is longer than 64 bytes will cause this response.  <br />+  JSON contains too many levels of nesting; maximum is 6 <br />+  State contains an invalid node   |
| 401 (Unauthorized) |  +  Unauthorized   |
| 403 (Forbidden) |  +  Forbidden   |
| 404 (Not Found) |  +  Thing not found <br />+  No shadow exists with name: {{shadowName}}   |
| 409 (Conflict) |  +  Version conflict   |
| 413 (Payload Too Large) |  +  The payload exceeds the maximum size allowed   |
| 415 (Unsupported Media Type) |  +  Unsupported documented encoding; supported encoding is UTF-8   |
| 429 (Too Many Requests) |  +  The Device Shadow service will generate this error message when there are more than 10 in-flight requests on a single connection. An in-flight request is an in-progress request that has been started but not yet completed.   |
| 500 (Internal Server Error) |  +  Internal service failure   |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Core. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
