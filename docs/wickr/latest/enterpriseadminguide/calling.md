---
source_url: https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/calling.html
---

This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html).

# Calling
<a name="calling"></a>

The **Calling** section has the following available features for users:
+ **Audio Calling Control:** Disables calling for users. At a minimum users must be able to share audio to start or join a call. Enabled by default.
+ **Video Calling Control:** Is used if disabled users cannot share their camera feed or their screen. Enabled by default.
+ **Force TCP Calling:** Forces users to connect to calls over TCP without trying connections over UDP, saving time when you know UDP is disabled in the network.
+ **Use Hosted Federated Calls:** For Global Federation. Disabled by default. If this setting is enabled, users within the Enterprise deployment will connect to the external, federated infrastructure for calls instead of the local infrastructure. It is useful for isolated environments where outside users can't connect to the Enterprise infrastructure.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
