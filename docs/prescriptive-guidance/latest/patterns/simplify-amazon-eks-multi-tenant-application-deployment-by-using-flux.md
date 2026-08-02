---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/simplify-amazon-eks-multi-tenant-application-deployment-by-using-flux.html
---

# Simplify Amazon EKS multi-tenant application deployment by using Flux
<a name="simplify-amazon-eks-multi-tenant-application-deployment-by-using-flux"></a>

*Nadeem Rahaman, Aditya Ambati, Aniket Dekate, and Shrikant Patil, Amazon Web Services*

## Summary
<a name="simplify-amazon-eks-multi-tenant-application-deployment-by-using-flux-summary"></a>

Many companies that offer products and services are data-regulated industries that are required to maintain data barriers between their internal business functions. This pattern describes how you can use the multi-tenancy feature in Amazon Elastic Kubernetes Service (Amazon EKS) to build a data platform that achieves logical and physical isolation between tenants or users that share a single Amazon EKS cluster. The pattern provides isolation through the following approaches:
+ Kubernetes namespace isolation
+ Role-based access control (RBAC)
+ Network policies
+ Resource quotas
+ AWS Identity and Access Management (IAM) roles for service accounts (IRSA)

In addition, this solution uses Flux to keep the tenant configuration immutable when you deploy applications. You can deploy your tenant applications by specifying the tenant repository that contains the Flux `kustomization.yaml` file in your configuration.

This pattern implements the following:
+ An AWS CodeCommit repository, AWS CodeBuild projects, and an AWS CodePipeline pipeline, which are created by manually deploying Terraform scripts.
+ Network and compute components required for hosting the tenants. These are created through CodePipeline and CodeBuild by using Terraform.
+ Tenant namespaces, network policies, and resource quotas, which are configured through a Helm chart.
+ Applications that belong to different tenants, deployed by using Flux.

We recommend that you carefully plan and build your own architecture for multi-tenancy based on your unique requirements and security considerations. This pattern provides a starting point for your implementation.

## Prerequisites and limitations
<a name="simplify-amazon-eks-multi-tenant-application-deployment-by-using-flux-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ AWS Command Line Interface (AWS CLI) version 2.11.4 or later, [installed](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and [configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)
+ [Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli) version 0.12 or later installed on your local machine
+ [Terraform AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest) version 3.0.0 or later
+ [Kubernetes Provider](https://registry.terraform.io/providers/hashicorp/kubernetes/latest/docs) version 2.10 or later
+ [Helm Provider](https://registry.terraform.io/providers/hashicorp/helm/latest/docs) version 2.8.0 or later
+ [Kubectl Provider](https://registry.terraform.io/providers/gavinbunney/kubectl/latest/docs) version 1.14 or later

**Limitations**
+ **Dependency on Terraform manual deployments: **The workflow's initial setup, including creating CodeCommit repositories, CodeBuild projects, and CodePipeline pipelines, relies on manual Terraform deployments. This introduces a potential limitation in terms of automation and scalability, because it requires manual intervention for infrastructure changes.
+ **CodeCommit repository dependency: **The workflow relies on CodeCommit repositories as the source code management solution and is tightly coupled with AWS services.

## Architecture
<a name="simplify-amazon-eks-multi-tenant-application-deployment-by-using-flux-architecture"></a>

**Target architectures **

This pattern deploys three modules to build the pipeline, network, and compute infrastructure for a data platform, as illustrated in the following diagrams.

*Pipeline architecture:*

![Pipeline infrastructure for Amazon EKS multi-tenant architecture](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/97b700a7-74b6-4f9d-b53a-76de42409a8e/images/76a4a23d-4275-427a-ae36-51c9a3803128.png)

*Network architecture:*

![Network infrastructure for Amazon EKS multi-tenant architecture](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/97b700a7-74b6-4f9d-b53a-76de42409a8e/images/e542249a-19a3-4c99-b6f5-fdf80fee4edf.png)

*Compute architecture:*

![Compute infrastructure for Amazon EKS multi-tenant architecture](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/97b700a7-74b6-4f9d-b53a-76de42409a8e/images/91bd1ca8-17f0-433c-8600-4c8e6c474e31.png)

## Tools
<a name="simplify-amazon-eks-multi-tenant-application-deployment-by-using-flux-tools"></a>

**AWS services**
+ [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) is a fully managed build service that helps you compile source code, run unit tests, and produce artifacts that are ready to deploy.
+ [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html) is a version control service that helps you privately store and manage Git repositories, without needing to manage your own source control system.
+ [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) helps you quickly model and configure the different stages of a software release and automate the steps required to release software changes continuously.
+ [Amazon Elastic Kubernetes Service (Amazon EKS) ](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html)helps you run Kubernetes on AWS without needing to install or maintain your own Kubernetes control plane or nodes.
+ [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) is a central hub that connects virtual private clouds (VPCs) and on-premises networks.
+ [Amazon Virtual Private Cloud (Amazon VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) helps you launch AWS resources into a virtual network that you’ve defined. This virtual network resembles a traditional network that you’d operate in your own data center, with the benefits of using the scalable infrastructure of AWS.

**Other tools**
+ [Cilium Network Policies](https://cilium.io/use-cases/network-policy/#:~:text=Cilium%20implements%20Kubernetes%20Network%20Policies,%2C%20Kafka%2C%20gRPC%2C%20etc.) support Kubernetes L3 and L4 networking policies. They can be extended with L7 policies to provide API-level security for HTTP, Kafka, and gRPC, and other similar protocols.
+ [Flux](https://fluxcd.io/) is a Git-based continuous delivery (CD) tool that automates application deployments on Kubernetes.
+ [Helm](https://helm.sh/docs/) is an open source package manager for Kubernetes that helps you install and manage applications on your Kubernetes cluster.
+ [Terraform](https://www.terraform.io/) is an infrastructure as code (IaC) tool from HashiCorp that helps you create and manage cloud and on-premises resources.

**Code repository**

The code for this pattern is available in the GitHub [EKS Multi-Tenancy Terraform Solution](https://github.com/aws-samples/aws-eks-multitenancy-deployment) repository.

## Best practices
<a name="simplify-amazon-eks-multi-tenant-application-deployment-by-using-flux-best-practices"></a>

For guidelines and best practices for using this implementation, see the following:
+ [Amazon EKS multi-tenancy best practices](https://aws.github.io/aws-eks-best-practices/security/docs/multitenancy/)
+ [Flux documentation](https://fluxcd.io/flux/get-started/)

## Epics
<a name="simplify-amazon-eks-multi-tenant-application-deployment-by-using-flux-epics"></a>

### Create pipelines for Terraform build, test, and deploy stages
<a name="create-pipelines-for-terraform-build-test-and-deploy-stages"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the project repository. | Clone the GitHub [EKS Multi-Tenancy Terraform Solution](https://github.com/aws-samples/aws-eks-multitenancy-deployment) repository by running the following command in a terminal window:<pre>git clone https://github.com/aws-samples/aws-eks-multitenancy-deployment.git</pre> | AWS DevOps |
| Bootstrap the Terraform S3 bucket and Amazon DynamoDB. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/simplify-amazon-eks-multi-tenant-application-deployment-by-using-flux.html) | AWS DevOps |
| Update the `run.sh` and `locals.tf` files. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/simplify-amazon-eks-multi-tenant-application-deployment-by-using-flux.html) | AWS DevOps |
| Deploy the pipeline module. | To create pipeline resources, run the following Terraform commands manually. There is no orchestration for running these commands automatically.<pre>./run.sh -m pipeline -e demo -r <AWS_REGION> -t init<br />./run.sh -m pipeline -e demo -r <AWS_REGION> -t plan<br />./run.sh -m pipeline -e demo -r <AWS_REGION> -t apply</pre> | AWS DevOps |

### Create the network infrastructure
<a name="create-the-network-infrastructure"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Start the pipeline. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/simplify-amazon-eks-multi-tenant-application-deployment-by-using-flux.html)After this first run, the pipeline starts automatically whenever you commit a change to the CodeCommit repository main branch.<br />The pipeline includes the following [stages](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts.html#concepts-stages):[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/simplify-amazon-eks-multi-tenant-application-deployment-by-using-flux.html) | AWS DevOps |
| Validate the resources created through the network module. | Confirm that the following AWS resources were created after the pipeline deployed successfully:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/simplify-amazon-eks-multi-tenant-application-deployment-by-using-flux.html) | AWS DevOps |

### Create the compute infrastructure
<a name="create-the-compute-infrastructure"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Update `locals.tf` to enable the CodeBuild project’s access to the VPC. | To deploy the add-ons for the Amazon EKS private cluster, the CodeBuild project must be attached to the Amazon EKS VPC.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/simplify-amazon-eks-multi-tenant-application-deployment-by-using-flux.html) | AWS DevOps |
| Update the `buildspec` files to build the compute module. | In the `templates` folder, in all `buildspec` YAML files, set the value of the `TF_MODULE_TO_BUILD` variable from `network` to `compute`:<pre>TF_MODULE_TO_BUILD: "compute"</pre> | AWS DevOps |
| Update the `values` file for the tenant management Helm chart. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/simplify-amazon-eks-multi-tenant-application-deployment-by-using-flux.html) | AWS DevOps |
| Validate compute resources. | After you update the files in the previous steps, CodePipeline starts automatically. Confirm that it created the following AWS resources for the compute infrastructure:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/simplify-amazon-eks-multi-tenant-application-deployment-by-using-flux.html) | AWS DevOps |

### Check tenant management and other resources
<a name="check-tenant-management-and-other-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Validate the tenant management resources in Kubernetes. | Run the following commands to check that tenant management resources were created successfully with the help of Helm.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/simplify-amazon-eks-multi-tenant-application-deployment-by-using-flux.html) | AWS DevOps |
| Verify tenant application deployments. | Run the following commands to verify that the tenant applications were deployed.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/simplify-amazon-eks-multi-tenant-application-deployment-by-using-flux.html) |  |

## Troubleshooting
<a name="simplify-amazon-eks-multi-tenant-application-deployment-by-using-flux-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| You encounter an error message that’s similar to the following:<br />`Failed to checkout and determine revision: unable to clone unknown error: You have successfully authenticated over SSH. You can use Git to interact with AWS CodeCommit.` | Follow these steps to troubleshoot the issue:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/simplify-amazon-eks-multi-tenant-application-deployment-by-using-flux.html) |

## Related resources
<a name="simplify-amazon-eks-multi-tenant-application-deployment-by-using-flux-resources"></a>
+ [Amazon EKS Blueprints for Terraform](https://github.com/aws-ia/terraform-aws-eks-blueprints)
+ [Amazon EKS Best Practices Guides, Multi-tenancy section](https://aws.github.io/aws-eks-best-practices/security/docs/multitenancy/)
+ [Flux website](https://fluxcd.io/)
+ [Helm website](https://helm.sh/)

## Additional information
<a name="simplify-amazon-eks-multi-tenant-application-deployment-by-using-flux-additional"></a>

Here's an example repository structure for deploying tenant applications:

```
applications
sample_tenant_app
├── README.md
├── base
│   ├── configmap.yaml
│   ├── deployment.yaml
│   ├── ingress.yaml
│   ├── kustomization.yaml
│   └── service.yaml
└── overlays
    ├── tenant-1
    │   ├── configmap.yaml
    │   ├── deployment.yaml
    │   └── kustomization.yaml
    └── tenant-2
        ├── configmap.yaml
        └── kustomization.yaml
```
