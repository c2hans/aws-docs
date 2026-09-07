---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-cockroachdb-on-eks-using-terraform.html
---

# Deploy a CockroachDB cluster in Amazon EKS by using Terraform
<a name="deploy-cockroachdb-on-eks-using-terraform"></a>

*Sandip Gangapadhyay and Kalyan Senthilnathan, Amazon Web Services*

## Summary
<a name="deploy-cockroachdb-on-eks-using-terraform-summary"></a>

This pattern provides a HashiCorp Terraform module for deploying a multi-node [CockroachDB](https://www.cockroachlabs.com/docs/stable/) cluster on Amazon Elastic Kubernetes Service (Amazon EKS) by using the [CockroachDB operator](https://www.cockroachlabs.com/docs/v25.4/cockroachdb-operator-overview). CockroachDB is a distributed SQL database that provides automatic horizontal sharding, high availability, and consistent performance across geographically distributed clusters. This pattern uses Amazon EKS as the managed Kubernetes platform and implements [cert-manager](https://cert-manager.io/docs/) for TLS-secured node communication. It also uses a [Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html) for traffic distribution and creates CockroachDB [StatefulSets](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) with pods that automatically replicate data for fault tolerance and performance.

**Intended audience**

To implement this pattern, we recommend that you are familiar with the following:
+ HashiCorp Terraform concepts and infrastructure as code (IaC) practices
+ AWS services, particularly Amazon EKS
+ Kubernetes fundamentals, including StatefulSets, operators, and service configurations
+ Distributed SQL databases
+ Security concepts, such as TLS certificate management.
+ DevOps practices, CI/CD workflows, and infrastructure automation

## Prerequisites and limitations
<a name="deploy-cockroachdb-on-eks-using-terraform-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ Permissions to deploy resources in an Amazon EKS cluster
+ An Amazon EKS cluster version v1.23 or later, with nodes labeled `node=cockroachdb`
+ [Amazon Elastic Block Store Container Storage Interface (CSI) Driver](https://github.com/kubernetes-sigs/aws-ebs-csi-driver) version 1.19.0 or later, installed in the Amazon EKS cluster
+ Terraform CLI version 1.0.0 or later, [installed](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)
+ kubectl, [installed](https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html)
+ Git, [installed](https://git-scm.com/install/)
+ AWS Command Line Interface (AWS CLI) version 2.9.18 or later, [installed](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and [configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)

**Limitations**
+ The CockroachDB Kubernetes operator does not support multiple Kubernetes clusters for multi-Region deployments. For more limitation, see [Orchestrate CockroachDB Across Multiple Kubernetes Clusters](https://www.cockroachlabs.com/docs/stable/orchestrate-cockroachdb-with-kubernetes-multi-cluster.html#eks) (CockroachDB documentation) and [CockroachDB Kubernetes Operator](https://github.com/cockroachdb/cockroach-operator) (GitHub).
+ Automatic pruning of persistent volume claims (PVCs) is currently disabled by default. This means that after decommissioning and removing a node, the operator will not remove the persistent volume that was mounted to its pod. For more information, see [Automatic PVC pruning](https://www.cockroachlabs.com/docs/stable/scale-cockroachdb-kubernetes.html#automatic-pvc-pruning) in the CockroachDB documentation.

**Product versions**
+ CockroachDB version 22.2.2

## Architecture
<a name="deploy-cockroachdb-on-eks-using-terraform-architecture"></a>

**Target architecture**

The following diagram shows a highly available CockroachDB deployment across three AWS Availability Zones within a virtual private cloud (VPC). The CockroachDB pods are managed through Amazon EKS. The architecture illustrates how users access the database through a Network Load Balancer, which distributes traffic to the CockroachDB pods. The pods run on Amazon Elastic Compute Cloud (Amazon EC2) instances in each Availability Zone, which provides resilience and fault tolerance.

![A highly available CockroachDB deployment across three AWS Availability Zones within a VPC.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/e22d81ab-b85c-4709-8579-4c9cdb4afdb6/images/4b163abf-6fdc-4310-840c-bda621ab25dd.png)

**Resources created**

Deploying the Terraform module used in this pattern creates the following resources:

1. **Network Load Balancer** – This resource serves as the entry point for client requests and evenly distributes traffic across the CockroachDB instances.

1. **CockroachDB StatefulSet** – The StatefulSet defines the desired state of the CockroachDB deployment within the Amazon EKS cluster. It manages the ordered deployment, scaling, and updates of CockroachDB pods.

1. **CockroachDB pods** – These pods are instances of CockroachDB running as containers within Kubernetes pods. These pods store and manage the data across the distributed cluster.

1. **CockroachDB database** – This is the distributed database that is managed by CockroachDB, spanning multiple pods. It replicates data for high availability, fault tolerance, and performance.

## Tools
<a name="deploy-cockroachdb-on-eks-using-terraform-tools"></a>

**AWS services**
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open source tool that helps you interact with AWS services through commands in your command-line shell.
+ [Amazon Elastic Kubernetes Service (Amazon EKS)](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html) helps you run Kubernetes on AWS without needing to install or maintain your own Kubernetes control plane or nodes.

**Other tools**
+ [HashiCorp Terraform](https://www.terraform.io/docs) is an infrastructure as code (IaC) tool that helps you use code to provision and manage cloud infrastructure and resources.
+ [kubectl](https://kubernetes.io/docs/tasks/tools/) is a command-line interface that helps you run commands against Kubernetes clusters.

**Code repository**

The code for this pattern is available in the GitHub [Deploy a CockroachDB cluster in Amazon EKS using Terraform](https://github.com/aws-samples/crdb-cluster-eks-terraform) repository. The code repository contains the following files and folders for Terraform:
+ `modules` folder – This folder contains the Terraform module for CockroachDB
+ `main` folder – This folder contains the root module that calls CockroachDB child module to create the CockroachDB database cluster.

## Best practices
<a name="deploy-cockroachdb-on-eks-using-terraform-best-practices"></a>
+ Do not scale down to fewer than three nodes. This is considered an anti-pattern on CockroachDB and can cause errors. For more information, see [Cluster Scaling](https://www.cockroachlabs.com/docs/stable/scale-cockroachdb-kubernetes.html) in the CockroachDB documentation.
+ Implement Amazon EKS autoscaling by using Karpernter or Cluster Autoscaler. This allows the CockroachDB cluster to scale horizontally and new nodes automatically. For more information, see [Scale cluster compute with Karpenter and Cluster Autoscaler](https://docs.aws.amazon.com/eks/latest/userguide/autoscaling.html) in the Amazon EKS documentation.
**Note**
Due to the `podAntiAffinity` Kubernetes scheduling rule, only one CockroachDB pod can be schedule in one Amazon EKS node.
+ For Amazon EKS security best practices, see [Best Practices for Security](https://docs.aws.amazon.com/eks/latest/best-practices/security.html) in the Amazon EKS documentation.
+ For SQL performance best practices for CockroachDB, see [SQL Performance Best Practices](https://www.cockroachlabs.com/docs/stable/performance-best-practices-overview.html) in the CockroachDB documentation.
+ For more information about setting up an Amazon Simple Storage Service (Amazon S3) remote backend for the Terraform state file, see [Amazon S3](https://developer.hashicorp.com/terraform/language/backend/s3) in the Terraform documentation.

## Epics
<a name="deploy-cockroachdb-on-eks-using-terraform-epics"></a>

### Set up your environment
<a name="set-up-your-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the code repository. | Enter the following command to clone the repository:<pre>git clone https://github.com/aws-samples/crdb-cluster-eks-terraform.git</pre> | DevOps engineer, Git |
| Update the Terraform variables. | 1. Enter the following command to navigate into the main folder in the cloned repository:<pre>cd crdb-cluster-eks-terraform/main</pre><br />2. Open the **variable.tf** file.<br />3. Configure the default value for the following variables:`region` – Enter the target AWS Region`eks_cluster_name` – Enter the name for the target Amazon EKS cluster`number_of_nodes` – Enter the number of nodes to deploy<br />4. Save and close the **variable.tf** file. | DevOps engineer, Terraform |

### Deploy the resources
<a name="deploy-the-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the infrastructure. | 1. Enter the following command to initialize the Terraform deployment:<pre>terraform init</pre><br />2. Enter the following command to generate an execution plan:<pre>terraform plan</pre><br />3. Review the plan, and validate the resources and infrastructure components that will be created.<br />4. Enter the following command to deploy the infrastructure:<pre>terraform apply</pre><br />5. When prompted, enter **yes** to confirm the deployment.<br />6. Wait until the deployment is completed. | DevOps engineer, Terraform |

### Verify the deployment
<a name="verify-the-deployment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Verify resource creation. | 1. Enter the following command to set the Amazon EKS context using the AWS CLI:<pre>aws eks update-kubeconfig —name <eks_cluster_name></pre><br />2. Enter the following command to verify the number of pods that are using CockroachDB:<pre>kubectl get pods -n <namespace></pre><br />The following is a sample output.<pre>NAME                                  READY   STATUS    RESTARTS   AGE<br />cockroach-operator-655fbf7847-zn9v8   1/1     Running   0          30m<br />cockroachdb-0                         1/1     Running   0          24m<br />cockroachdb-1                         1/1     Running   0          24m<br />cockroachdb-2                         1/1     Running   0          24m</pre><br />3. Verify that the number of pods matches the value that you defined in the **variable.tf** file. | DevOps engineer |
| (Optional) Scale up or down. | 1. In the **variable.tf** file, increase or decrease the number of nodes and then save the file.<br />2. Repeat the steps to deploy the infrastructure through Terraform. Terraform adds or removes pods.<br />3. Repeat the steps to verify the number of pods that are using Cockroach DB. For example, if you increased the number of nodes from three to four, you should now see four pods running. | DevOps engineer, Terraform |

### Clean up
<a name="clean-up"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Delete the infrastructure. | Scaling nodes to `0` will reduce compute costs. However, you will still incur charges for the persistent Amazon EBS volumes that were created by this module. To eliminate storage costs, follow these steps to delete all volumes:1. Enter the following command to delete the infrastructure:<pre>terraform destroy</pre><br />2. When prompted, enter **yes** to confirm. | Terraform |

## Troubleshooting
<a name="deploy-cockroachdb-on-eks-using-terraform-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Error validating provider credentials | When you run the Terraform `apply` or `destroy` command, you might encounter the following error:<br />`Error: configuring Terraform AWS Provider: error validating provider  credentials: error calling sts:GetCallerIdentity: operation error STS: GetCallerIdentity, https response error StatusCode: 403, RequestID: 123456a9-fbc1-40ed-b8d8-513d0133ba7f, api error InvalidClientTokenId: The security token included in the request is invalid.`<br />This error is caused by the expiration of the security token for the credentials used in your local machine’s configuration. For instructions on how to resolve the error, see [Set and view configuration settings](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html#cli-configure-files-methods) in the AWS CLI documentation. |
| CockroachDB pods in pending state | 1. Due to the `podAntiAffinity` Kubernetes scheduling rule, only one CockroachDB pod can be schedule in one Amazon EKS node. If the number of CockroachDB pods exceeds number of available Amazon EKS nodes, then CockroachDB pods might be in pending state. In that case, you need to implement Cluster Autoscaler or Karpenter so that theAmazon EKS node scales automatically. For more information, see [Scale cluster compute with Karpenter and Cluster Autoscaler](https://docs.aws.amazon.com/eks/latest/userguide/autoscaling.html).<br />2. Check if the Kubernetes worker nodes have `node=cockroachdb` labels by entering the following command:<pre>kubectl get nodes --show-labels</pre><br />If they are not, you need to make sure that all of the worker nodes are correctly labeled. For more information, see [Edit a node group configuration](https://docs.aws.amazon.com/eks/latest/userguide/update-managed-node-group.html#mng-edit) in the Amazon EKS documentation. |

## Related resources
<a name="deploy-cockroachdb-on-eks-using-terraform-resources"></a>
+ [Deploy CockroachDB in a Single Kubernetes Cluster](https://www.cockroachlabs.com/docs/dev/deploy-cockroachdb-with-kubernetes.html) (CockroachDB documentation)
+ [Orchestrate CockroachDB Across Multiple Kubernetes Clusters](https://www.cockroachlabs.com/docs/dev/orchestrate-cockroachdb-with-kubernetes-multi-cluster.html) (CockroachDB documentation)
+ [AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs) (Terraform documentation)

## Attachments
<a name="attachments-e22d81ab-b85c-4709-8579-4c9cdb4afdb6"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/e22d81ab-b85c-4709-8579-4c9cdb4afdb6/attachments/attachment.zip)
