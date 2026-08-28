---
source_url: https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/push-configuration.html
---

This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html).

# Push configuration
<a name="push-configuration"></a>

The **Push Configuration** section has available options for proxy or intermediary networking devices. This can also be used to obfuscate the infrastructure by forcing users to connect to proxies which then forward traffic to the Messaging/App server.

**Note**
Push configuration entries supersede any connection information in a config file or deeplink.
+ **Messaging Domains:** Domains and IP addresses accepting client connections.
+ **Voice & Video Domains:** Domains and IP addresses accepting client calls.
+ **Certificate Pinning:** Accepts only authorized pinned certificates for authentication of client-server connections.
+ **SSL Certificates:** The SSL certificate used during installation is here automatically.

We recommend using intermediate certificates instead of a leaf.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
