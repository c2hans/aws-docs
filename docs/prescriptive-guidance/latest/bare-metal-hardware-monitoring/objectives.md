---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/bare-metal-hardware-monitoring/objectives.html
---

# Objectives
<a name="objectives"></a>

Telegraf and the Redfish API can help you address the challenges of hardware health monitoring in multi-vendor environments. By using the plugin-based architecture and robust authentication mechanisms in Telegraf, organizations can achieve the following targeted business outcomes.

**Improved operational efficiency through automation:**
+ The adoption of the Redfish API and Telegraf helps you automate hardware monitoring tasks. This reduces the need for manual intervention and streamlines operational processes.
+ By using the RESTful interface of Redfish API and the plugin-based architecture of Telegraf, you can automate data collection, analysis, and reporting. This can lead to substantial time savings and increase productivity.
+ Automated monitoring helps you detect and resolve hardware issues in a timely manner. This minimizes downtime and improves the overall system reliability.

**Vendor-agnostic monitoring solution:**
+ One of the key advantages is the ability to establish a vendor-agnostic monitoring solution. This mitigates vendor lock-in and helps you integrate hardware components from multiple vendors.
+ By developing vendor-specific Telegraf plugins, you can resolve the differences in Redfish API implementations. This provides a consistent interface for data collection and monitoring across various vendors.
+ This vendor-agnostic approach offers flexibility, reduces dependency on specific vendors, and facilitates easier hardware component upgrades or replacements that don't disrupt the monitoring infrastructure.

**Enhanced security and access control:**
+ Because the Redfish API provides direct access to hardware components, it is crucial to implement robust authentication and authorization mechanisms. Telegraf can help you establish proper access control and security.
+ Telegraf supports various authentication methods that help you secure communication with Redfish API endpoints.
+ Enforcing fine-grained access control, based on defined roles and permissions, can help you mitigate potential security risks and allow access only to authorized personnel.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
