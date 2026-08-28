---
source_url: https://docs.aws.amazon.com/sap/latest/sap-netweaver/net-win-network-1.html
---

# Network
<a name="net-win-network-1"></a>

Ensure that you have your network constructs set up to deploy resources related to SAP NetWeaver. If you haven’t already set up network components, such as Amazon VPC, subnets, and route tables, you can use the [AWS Quick Start for Modular and Scalable VPC Architecture](https://aws.amazon.com/quickstart/architecture/vpc/) to easily deploy scalable VPC architecture in minutes. See the deployment guide for more details, then set up your EC2 instances for the NetWeaver application server within this VPC.

You also will need to set up a secured network connection between the corporate data center and the VPC, along with the appropriate route table configuration, if this has not already been configured.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for SAP on AWS Technical Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
