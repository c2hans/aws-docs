---
source_url: https://docs.aws.amazon.com/whitepapers/latest/cicd_for_5g_networks_on_aws/infrastructure-deployment.html
---

# Infrastructure deployment
<a name="infrastructure-deployment"></a>

Infrastructure deployment provisions any infrastructure components. It includes spawning the EKS cluster and the supporting infrastructure, such as EFS, EKS Worker nodes, ELBs, and configuring the cluster according to cloud-native network function requirements. Based on the CNF requirements, AWS also deploys extra network interfaces for the nodes, including [Multus](https://github.com/intel/multus-cni) interfaces. Most of the deployment and configuration steps are a one-time effort for an application, and are updated only when needed as an update for the application.

![A diagram depicting infrastructure deployment with CDK.](http://docs.aws.amazon.com/whitepapers/latest/cicd_for_5g_networks_on_aws/images/cicd_5g8.png)

*Infrastructure deployment with CDK*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
