---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/automated-infrastructure-provisioning.html
---

# Automated infrastructure provisioning
<a name="automated-infrastructure-provisioning"></a>

 AWS TNB automatically provisions the required compute and network resources, such as VPCs, subnets, Elastic Network Interfaces (ENIs), Amazon EKS clusters, and Amazon EC2 instances, to support the 5G NF deployment.

 **Recommendations:** Verify the network and compute resources are designed to meet the performance, scalability, and resiliency requirements of the 5G network. Use AWS services like VPC, Amazon EKS, and Amazon EC2 to benefit from the built-in security, monitoring, and management capabilities.

 **Practical advice:** Implement robust access controls, network segmentation, and security monitoring to protect the 5G network infrastructure. Establish automated remediation processes to address infrastructure-related issues.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
