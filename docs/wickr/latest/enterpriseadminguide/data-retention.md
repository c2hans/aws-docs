---
source_url: https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/data-retention.html
---

This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html).

# Compliance bot (Data retention)
<a name="data-retention"></a>

The data retention service uses the Compliance bot, which is an additional service available within Wickr Enterprise.

With data retention, an organization can retain all conversations in network. This includes direct messages and conversations in Groups or Rooms between in-network (internal) members and those with other teams (external) with whom your network is federated.

This is achieved by adding a bot to the network before users are provisioned. Once the bot is running, configuration files will have compliance information that facilitates the message archiving process when users begin to register and use the app.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
