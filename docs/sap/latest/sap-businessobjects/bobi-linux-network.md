---
source_url: https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobi-linux-network.html
---

# Network
<a name="bobi-linux-network"></a>

Ensure that you have your network constructs set up to deploy resources related to your SAP workload. If you haven’t already set up network components like Amazon Virtual Private Cloud (Amazon VPC), subnets, route tables and so on., you can use the [AWS Quick Start for Modular and Scalable VPC Architecture](https://aws.amazon.com/quickstart/architecture/vpc/) to easily deploy scalable VPC architecture in minutes. Refer to the deployment guide for more details, then set up your EC2 instances for the SAP workload within this VPC.

You will also need to set up a secured network connection between the corporate datacenter and the VPC, along with appropriate route table configuration, if this is not already configured.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for SAP on AWS Technical Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
