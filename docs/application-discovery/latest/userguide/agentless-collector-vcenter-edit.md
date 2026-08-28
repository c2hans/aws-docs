---
source_url: https://docs.aws.amazon.com/application-discovery/latest/userguide/agentless-collector-vcenter-edit.html
---

AWS Application Discovery Service is no longer open to new customers. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).

# Editing VMware vCenter credentials
<a name="agentless-collector-vcenter-edit"></a>

To collect server inventory, profile, and utilization data from your VMware VMs, set up connections to your vCenter servers. For information about setting up VMware vCenter connections, see [Using the VMware vCenter Agentless Collector data collection module](agentless-collector-gs-data-collection-vcenter.md).

This section describes how to edit the vCenter credentials.

**Note**
Before editing vCenter credentials, make sure you can provide vCenter credentials with Read and View permissions set for the System group.

**To edit the VMware vCenter credentials**

On the [Viewing VMware data collection details](agentless-collector-gs-vcenter-details.md) page, choose **Edit vCenter servers**.
+ On the **Edit vCenter** page, perform the following:

  1. Under **vCenter credentials**:

     1. For **vCenter URL/IP**, enter the IP address of your VMware vCenter Server host.

     1. For **vCenter Username**, enter the name of a local or domain user that the connector uses to communicate with vCenter. For domain users, use the form *domain*\\*username* or *username*@*domain*.

     1. For **vCenter Password**, enter the local or domain user password.

  1. Choose **Save**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Application Discovery Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query application-discovery` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
