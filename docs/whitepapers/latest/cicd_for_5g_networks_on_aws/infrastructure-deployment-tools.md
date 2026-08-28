---
source_url: https://docs.aws.amazon.com/whitepapers/latest/cicd_for_5g_networks_on_aws/infrastructure-deployment-tools.html
---

# Infrastructure deployment
<a name="infrastructure-deployment-tools"></a>

Infrastructure deployment includes all the prerequisites for the network function to be successfully deployed and configured.

Some of the components created as part of this phase are:
+  Networking — VPC, public and private subnets, routes, load balancers
+  Compute — Kubernetes ( [ Vmware Tanzu ](https://tanzu.vmware.com/tanzu), Amazon EKS, or AWS Outposts), Amazon EC2 instances primary and worker nodes, auto scaling group
+  Storage — Amazon EFS, Amazon EBS, Amazon S3 bucket
+  Security — [ Security groups ](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)
+  Pipeline — CodePipeline, CodeBuild
+  Observability — CloudWatch, Prometheus, FluentD

Here is the infrastructure sequence orchestrated by Terraform and explained in the following figure:

1. A developer populates a JSON file that is stored in a central repository with the IaC code. The file contains information about the desired infrastructure configuration such as instances size, Kubernetes version, network information, and application repository details.

1. Retrieves secrets from HashiCorp Vault or [ AWS Secrets Manager ](https://aws.amazon.com/secrets-manager/) at runtime.

1. Deploys and configures the infrastructure components (networking, compute, storage, and security).

1. An Amazon EKS cluster with worker nodes that hosts the network function pods is deployed. Amazon EKS can also be deployed on [AWS Outposts](https://aws.amazon.com/outposts/) to support workloads that require proximity to a datacenter.

1. An application pipeline is created and configured to listen for changes in the network function repository. Every time code is pushed to the configured repository branch, the pipeline automatically triggers build, test, and deployment of the network function.

1. Observability tools that collect and centralize logs and metrics are deployed as services in all the nodes, and provide almost real-time data that can be visualized in [ Grafana ](https://grafana.com/) or [ OpenSearch Dashboards ](https://www.elastic.co/kibana)

![A diagram depicting infrastructure deployment with Terraform.](http://docs.aws.amazon.com/whitepapers/latest/cicd_for_5g_networks_on_aws/images/cicd_5g12.png)

*Network function deployment and configuration*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
