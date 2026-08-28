---
source_url: https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/compliance-data-location.html
---

This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html).

# Compliance data location
<a name="compliance-data-location"></a>

The compliance bot will save messages and output by default to the following:

`/opt/WickrIO/clients/(bot_name)/integrations/compliance_bot/receivedMessages.log`

The (bot name) is the username entered during [Creating a compliance bot user](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/initial-network-configuration.html#compliance-bot-user.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
