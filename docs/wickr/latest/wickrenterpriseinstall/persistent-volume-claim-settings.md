---
source_url: https://docs.aws.amazon.com/wickr/latest/wickrenterpriseinstall/persistent-volume-claim-settings.html
---

This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html) or [AWS Wickr User Guide](https://docs.aws.amazon.com/wickr/latest/userguide/what-is-wickr.html).

# Persistent volume claim settings
<a name="persistent-volume-claim-settings"></a>

Wickr Enterprise requires Persistent Volume Claims to store stateful data. This setting allows you to specify the name of the name of the Storage Class you would like to use. If left blank Wickr will attempt to use the default Storage Class. Changing the Storage Class after Wickr has been deployed is not supported.

A default StorageClass for Persistent Volume Claims is often provided by cloud providers, however in fully onprem installations it may require explicit configuration using a third party service such as [Longhorn](https://longhorn.io/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
