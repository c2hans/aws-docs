---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/wazuh-platform-setup.html
---

# Wazuh Platform integration configuration
<a name="wazuh-platform-setup"></a>

Wazuh is an open-source security platform that provides unified XDR and SIEM capabilities including threat detection, integrity monitoring, incident response, and compliance across on-premises, cloud, and hybrid environments. The Wazuh Platform is the central component built on OpenSearch that stores and indexes security alerts, providing near real-time search and analytics through a RESTful API. Use CloudWatch pipelines with the Wazuh Platform API to retrieve security alerts, vulnerability findings, system inventory, and agent monitoring data.

**Topics**
+ [Source configuration for Wazuh Platform](wazuh-platform-source-config.md)
+ [CloudWatch pipelines configuration for Wazuh Platform](wazuh-platform-pipeline-setup.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
