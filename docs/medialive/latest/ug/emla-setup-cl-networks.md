---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/emla-setup-cl-networks.html
---

# Create the networks
<a name="emla-setup-cl-networks"></a>

Create the networks that you identified when you [designed the cluster](emla-deploy-design-cluster.md). Creating the network integrates the [resources that you identified](emla-deploy-identify-network-requirements.md) into AWS Elemental MediaLive Anywhere. You must create the networks before you create other MediaLive Anywhere resources.

1. Open the MediaLive console at [https://console.aws.amazon.com/medialive/](https://console.aws.amazon.com/medialive/).

1. In the navigation bar, choose MediaLive Anywhere, then choose **Networks**. On the **Networks** page, choose **Create network**.

1. Complete the fields with the information that the network engineer provided you with in [Identifying network resources](emla-deploy-identify-network-requirements.md).

1. Choose **Create**. MediaLive Anywhere creates the network and adds it to the list of networks.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
