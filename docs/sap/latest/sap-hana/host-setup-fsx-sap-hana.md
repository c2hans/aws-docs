---
source_url: https://docs.aws.amazon.com/sap/latest/sap-hana/host-setup-fsx-sap-hana.html
---

# Set up host
<a name="host-setup-fsx-sap-hana"></a>

This section walks you through an example host setup for deploying SAP HANA scale-up and scale-out systems on AWS using Amazon FSx for NetApp ONTAP as the primary storage solution.

You must configure your Amazon EC2 instance on an operating system level to use FSx for ONTAP with SAP HANA on AWS.

**Note**
The following examples apply to an SAP HANA workload with SAP System ID `HDB`. The operating system user is `hdbadm`.

**Topics**
+ [SAP HANA scale-up](fsx-host-scaleup.md)
+ [SAP HANA scale-out](fsx-host-scaleout.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for SAP on AWS Technical Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
