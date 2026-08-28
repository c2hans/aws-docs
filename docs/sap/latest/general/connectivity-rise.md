---
source_url: https://docs.aws.amazon.com/sap/latest/general/connectivity-rise.html
---

# Connectivity
<a name="connectivity-rise"></a>

You must establish connectivity between AWS cloud where your RISE with SAP solution is running and on-premises data centers. You also need a connection for direct data transfer (to avoid routing data via your on-premises locations) and communication between SAP systems and your applications running on AWS cloud. The following image provides an example overview of connectivity to RISE with SAP VPC.

![An example RISE with SAP VPC connection between an SAP-managed account and on-premises data centers](http://docs.aws.amazon.com/sap/latest/general/images/rise-connectivity.png)

See the following topics for further details:

**Topics**
+ [Roles and responsibility for establishing connectivity](rise-responsibility.md)
+ [Connecting to RISE from on-premises networks](rise-connection-on-premises.md)
+ [Connecting to RISE from your AWS account](rise-accounts.md)
+ [Connect to nearest Direct Connect POP (including Local Zone)](rise-local-zone.md)
+ [Decision tree on connectivity to RISE](rise-decision-tree.md)
+ [Other considerations](other-considerations.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for SAP on AWS Technical Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
