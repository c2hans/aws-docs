---
source_url: https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/custom-tcp-calling-port.html
---

This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html).

# Custom TCP calling port
<a name="custom-tcp-calling-port"></a>

Calling and messaging services in Wickr Enterprise utilize the same TCP port 443. To prevent collision when deploying Wickr Enterprise in Low Resource Mode, a custom calling port must be configured.

The Replicated console provides a configuration field `callingTcpPort`, which you must set before deploying the service. If no value is specified, the default is TCP 443. This extra field is passed into Wickr's calling service as an environment variable. Any firewalls in place must support inbound traffic on that port. Dynamic port changes are not supported. If an administrator changes the `callingTcpPort` value, it is necessary to restart the Orville and TCPProxy pods.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
