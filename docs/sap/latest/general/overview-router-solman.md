---
source_url: https://docs.aws.amazon.com/sap/latest/general/overview-router-solman.html
---

# SAProuter and SAP Solution Manager
<a name="overview-router-solman"></a>

The following sections describe options for SAProuter and SAP Solution Manager when running SAP solutions on AWS.

## For SAP All-on-AWS Architecture
<a name="overview-router-all-on-aws"></a>

When setting up an SAP environment on AWS, you will need to set up an SAP Solution Manager system and SAProuter with a connection to the SAP support network, as you would with any infrastructure. See the all-on-AWS architecture diagram ([Figure 3: SAP all-on-AWS architecture](overview-sap-planning.md#figure-3)) for an illustration.

When setting up the SAProuter and SAP support network connection, follow these guidelines:
+ Launch the instance that the SAProuter software is installed on into a public subnet of the VPC and assign it an Elastic IP address.
+ Create a specific security group for the SAProuter instance with the necessary rules to allow the required inbound and outbound access to the SAP support network.
+ Use the Secure Network Communications (SNC) type of internet connection. For more information, see [SAP Remote Support & Connections](https://support.sap.com/en/tools/connectivity-tools/remote-support.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for SAP on AWS Technical Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
