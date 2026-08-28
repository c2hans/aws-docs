---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migrating-self-managed-kubernetes-cluster-to-amazon-eks/introduction.html
---

# Migrating large-scale self-managed Kubernetes clusters to Amazon EKS
<a name="introduction"></a>

*Pradip kumar Pandey and Pratap Kumar Nanda, Amazon Web Services*

## Overview
<a name="overview"></a>

Moving from a self-managed Kubernetes setup to[Amazon Elastic Kubernetes Service (Amazon EKS](https://aws.amazon.com/pm/eks/)) represents a significant shift in how organizations handle container orchestration. This transition involves moving your existing workloads, configurations, and operational practices from clusters you manage yourself to a managed Kubernetes service on AWS.

This guide helps you migrate self-managed Kubernetes to Amazon EKS by reducing risks, saving time and cost, and providing clear planning frameworks. It builds team confidence, supports informed decision-making, and enables effective stakeholder communication. The guide serves as a practical reference throughout the migration journey, helping organizations avoid costly mistakes while transitioning from infrastructure maintenance to focusing on application development and business value delivery.

## Intended audience
<a name="intended-audience"></a>

This guide is intended for the following roles:
+ Cloud architects planning the target Amazon EKS environment
+ Platform engineers responsible for Kubernetes cluster operations
+ DevOps engineers managing CI/CD pipelines and deployment workflows
+ Migration leads coordinating the transition from self-managed clusters

Readers should have foundational knowledge of Kubernetes concepts (pods, deployments, services, namespaces), experience with kubectl, and familiarity with AWS core services.

## Objectives
<a name="objectives"></a>

After reading this guide, you will be able to:
+ Assess your current self-managed Kubernetes environment for migration readiness
+ Select the appropriate migration approach (blue-green, phased, or lift-and-shift) based on your requirements
+ Plan infrastructure, networking, storage, and security for the target Amazon EKS environment
+ Define a testing and validation strategy that minimizes risk during cutover
+ Identify post-migration optimization opportunities using AWS native services
+ Communicate migration plans and progress effectively to stakeholders

## Service availability
<a name="service-availability"></a>

Some AWS services aren't available in all AWS Regions. For Region availability, see [AWS services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see the [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) page, and choose the link for the service.

## Prerequisites and limitations
<a name="prerequisites-and-limitations"></a>

### Prerequisites
<a name="prerequisites.f2d8c791-078d-53ef-8ee6-da4e76294465"></a>

|
|
| Requirement | Details |
| --- |--- |
| Python | 3.9 or higher installed on the local machine |
| kubectl | Installed and configured with access to both the source cluster (for extraction) and the target Amazon EKS cluster (for migration) |
| AWS Command Line Interface (AWS CLI) | Version 2.x, configured with AWS Identity and Access Management (IAM) permissions for Amazon EKS, IAM, and Amazon EC2. |
| Helm (optional) | Version 3.x, required only if migrating Helm releases |
| Target Amazon EKS cluster | Must already exist. The migration script does not provision the cluster. For more information, see [Creating an Amazon EKS cluster](https://docs.aws.amazon.com/eks/latest/userguide/create-cluster.html) in the Amazon EKS documentation. |
| Amazon Elastic Block Store (Amazon EBS) CSI driver | Installed on the target Amazon EKS cluster for StorageClass provisioner remapping (`ebs.csi.aws.com`) |
| AWS Load Balancer Controller | Installed on the target Amazon EKS cluster for Service type LoadBalancer and Application Load Balancer Ingress support |
| CRD operators | Any controllers for custom resources used in the source cluster (for example, cert-manager, Prometheus Operator) must be installed on the target cluster before migration |
| IAM roles for service accounts (IRSA) | Configured on the target Amazon EKS cluster if workloads require AWS API access |
| Network connectivity | The local machine must have network access to both the source and target Kubernetes API servers |
| Cluster admin access | Admin-level access to both source and target clusters through kubectl. The extraction script requires read access to all resources; the migration script requires create/update permissions. |

### Limitations
<a name="limitations.ba091003-9006-536a-8faf-e12f29d4b317"></a>
+ Persistent volume data is not migrated. Use AWS DataSync or Velero for persistent volume data migration.
+ Helm releases require the original chart source to reinstall. The script outputs the commands but cannot run them without chart references.
+ Secret values are created as opaque placeholders. You must populate actual values post-migration through AWS Secrets Manager, AWS Systems Manager Parameter Store, or External Secrets Operator.
+ CRD operators and controllers must be pre-installed on the target Amazon EKS cluster before you migrate custom resource instances. For more information, see [AWS Controllers for Kubernetes](https://aws-controllers-k8s.github.io/community/).
+ If the source cluster uses a private container registry, ensure that Amazon EKS nodes have pull access, such as Amazon Elastic Container Registry (Amazon ECR) and image pull secrets.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
