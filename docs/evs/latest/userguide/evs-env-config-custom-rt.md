---
source_url: https://docs.aws.amazon.com/evs/latest/userguide/evs-env-config-custom-rt.html
---

# Configure a custom route table for Amazon EVS subnets
<a name="evs-env-config-custom-rt"></a>

Amazon EVS supports the use of a custom route table only after the Amazon EVS environment is created. To enable successful environment creation, you must configure the main route table to allow traffic to dependent services such as DNS and on-premises systems. This is because Amazon EVS VLAN subnets are implicitly associated to your VPC’s main route table during environment deployment.

After your environment deploys, you must explicitly associate each of the Amazon EVS VLAN subnets with a route table in your VPC. NSX connectivity fails if your VLAN subnets are not explicitly associated with a VPC route table. We strongly recommend that you explicitly associate your subnets with a custom route table. A custom route table provides more granular control over network traffic routing within your VPC, allowing for tailored routing rules for specific subnets or gateways. For more information about creating a custom route table, see [Create a route table for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc-route-table.html) in the *Amazon VPC User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic VMware Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query evs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
