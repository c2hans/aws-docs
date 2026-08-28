---
source_url: https://docs.aws.amazon.com/sap/latest/sap-hana/sap-ha-overlay-ip.html
---

# SAP on AWS High Availability with Overlay IP Address Routing
<a name="sap-ha-overlay-ip"></a>

This guide provides SAP customers and partners instructions to set up a highly available SAP architecture that uses overlay IP addresses on Amazon Web Services. This guide includes two configuration approaches:
+  AWS Transit Gateway serves as central hub to facilitate network connection to an overlay IP address.
+ Elastic Load Balancing where a Network Load Balancer enables network access to an overlay IP address.

This guide is intended for users who have previous experience installing and operating highly available SAP environments and systems.

**Topics**
+ [SAP on AWS High Availability Setup](sap-oip-sap-on-aws-high-availability-setup.md)
+ [Overlay IP Routing using AWS Transit Gateway](sap-oip-overlay-ip-routing-using-aws-transit-gateway.md)
+ [Overlay IP Routing with Network Load Balancer](sap-oip-overlay-ip-routing-with-network-load-balancer.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for SAP on AWS Technical Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
