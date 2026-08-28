---
source_url: https://docs.aws.amazon.com/sap/latest/sap-netweaver/hadr-sap-ase.html
---

# High availability disaster recovery deployment
<a name="hadr-sap-ase"></a>

Create an additional Amazon EC2 instance and perform the installation in a secondary Availability Zone. The steps for creating a high availability or disaster recovery instance in a secondary Availability Zone are the same as described in Standalone deployment. You can simplify this step by using the following methods.
+ If you have built any automation using AWS CloudFormation or other tools to create the primary Amazon EC2 instance and install database software, you can use the same automation to build the HA instance.
+ You can create an [Amazon Machine Image](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html) of the primary Amazon EC2 instance and launch another instance in the secondary Availability Zone.

The configuration of high availability or disaster recovery depends on the tools you use. See the next sections for more details.

**Note**
You must configure cross-regional [Amazon VPC peering](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) or [Transit Gateway](https://aws.amazon.com/transit-gateway/) to enable SAP ASE asynchronous replication between two Regions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for SAP on AWS Technical Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
