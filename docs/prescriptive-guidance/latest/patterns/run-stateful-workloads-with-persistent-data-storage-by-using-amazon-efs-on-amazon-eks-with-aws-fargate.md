---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/run-stateful-workloads-with-persistent-data-storage-by-using-amazon-efs-on-amazon-eks-with-aws-fargate.html
---

# Run stateful workloads with persistent data storage by using Amazon EFS on Amazon EKS with AWS Fargate
<a name="run-stateful-workloads-with-persistent-data-storage-by-using-amazon-efs-on-amazon-eks-with-aws-fargate"></a>

*Ricardo Morais, Rodrigo Bersa, and Lucio Pereira, Amazon Web Services*

## Summary
<a name="run-stateful-workloads-with-persistent-data-storage-by-using-amazon-efs-on-amazon-eks-with-aws-fargate-summary"></a>

This pattern provides guidance for enabling Amazon Elastic File System (Amazon EFS) as a storage device for containers that are running on Amazon Elastic Kubernetes Service (Amazon EKS) by using AWS Fargate to provision your compute resources.

The setup described in this pattern follows security best practices and provides security at rest and security in transit by default. To encrypt your Amazon EFS file system, it uses an AWS Key Management Service (AWS KMS) key, but you can also specify a key alias that dispatches the process of creating a KMS key.

You can follow the steps in this pattern to create a namespace and Fargate profile for a proof-of-concept (PoC) application, install the Amazon EFS Container Storage Interface (CSI) driver that is used to integrate the Kubernetes cluster with Amazon EFS, configure the storage class, and deploy the PoC application. These steps result in an Amazon EFS file system that is shared among multiple Kubernetes workloads, running over Fargate. The pattern is accompanied by scripts that automate these steps.

You can use this pattern if you want data persistence in your containerized applications and want to avoid data loss during scaling operations. For example:
+ **DevOps tools** – A common scenario is to develop a continuous integration and continuous delivery (CI/CD) strategy. In this case, you can use Amazon EFS as a shared file system to store configurations among different instances of the CI/CD tool or to store a cache (for example, an Apache Maven repository) for pipeline stages among different instances of the CI/CD tool.
+ **Web servers** – A common scenario is to use Apache as an HTTP web server. You can use Amazon EFS as a shared file system to store static files that are shared among different instances of the web server. In this example scenario, modifications are applied directly to the file system instead of static files being baked into a Docker image.

## Prerequisites and limitations
<a name="run-stateful-workloads-with-persistent-data-storage-by-using-amazon-efs-on-amazon-eks-with-aws-fargate-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ An existing Amazon EKS cluster with Kubernetes version 1.17 or later (tested up to version 1.27)
+ An existing Amazon EFS file system to bind a Kubernetes StorageClass and provision file systems dynamically
+ Cluster administration permissions
+ Context configured to point to the desired Amazon EKS cluster

**Limitations**
+ There are some limitations to consider when you’re using Amazon EKS with Fargate. For example, the use of some Kubernetes constructs, such as DaemonSets and privileged containers, aren’t supported. For more information, about Fargate limitations, see the [AWS Fargate considerations](https://docs.aws.amazon.com/eks/latest/userguide/fargate.html#fargate-considerations) in the Amazon EKS documentation.
+ The code provided with this pattern supports workstations that are running Linux or macOS.

**Product versions**
+ AWS Command Line Interface (AWS CLI) version 2 or later
+ Amazon EFS CSI driver version 1.0 or later (tested up to version 2.4.8)
+ eksctl version 0.24.0 or later (tested up to version 0.158.0)
+ jq version 1.6 or later
+ kubectl version 1.17 or later (tested up to version 1.27)
+ Kubernetes version 1.17 or later (tested up to version 1.27)

## Architecture
<a name="run-stateful-workloads-with-persistent-data-storage-by-using-amazon-efs-on-amazon-eks-with-aws-fargate-architecture"></a>

![Architecture diagram of running stateful workloads with persistent data storage by using Amazon EFS](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/2487e285-269b-415b-a270-877f973e3aaf/images/ec8de63c-3307-4010-9e03-2bd7b9881fff.png)

The target architecture is comprised of the following infrastructure:
+ A virtual private cloud (VPC)
+ Two Availability Zones
+ A public subnet with a NAT gateway that provides internet access
+ A private subnet with an Amazon EKS cluster and Amazon EFS mount targets (also known as *mount points*)
+ Amazon EFS at the VPC level

The following is the environment infrastructure for the Amazon EKS cluster:
+ AWS Fargate profiles that accommodate the Kubernetes constructs at the namespace level
+ A Kubernetes namespace with:
  + Two application pods distributed across Availability Zones
  + One persistent volume claim (PVC) bound to a persistent volume (PV) at the cluster level
+ A cluster-wide PV that is bound to the PVC in the namespace and that points to the Amazon EFS mount targets in the private subnet, outside of the cluster

## Tools
<a name="run-stateful-workloads-with-persistent-data-storage-by-using-amazon-efs-on-amazon-eks-with-aws-fargate-tools"></a>

**AWS services**
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open-source tool that you can use to interact with AWS services from the command line.
+ [Amazon Elastic File System (Amazon EFS)](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html) helps you create and configure shared file systems in the AWS Cloud. In this pattern, it provides a simple, scalable, fully managed, and shared file system for use with Amazon EKS.
+ [Amazon Elastic Kubernetes Service (Amazon EKS)](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html) helps you run Kubernetes on AWS without needing to install or operate your own clusters.
+ [AWS Fargate](https://docs.aws.amazon.com/eks/latest/userguide/fargate.html) is a serverless compute engine for Amazon EKS. It creates and manages compute resources for your Kubernetes applications.
+ [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) helps you create and control cryptographic keys to help protect your data.

**Other tools**
+ [Docker](https://www.docker.com/) is a set of platform as a service (PaaS) products that use virtualization at the operating-system level to deliver software in containers.
+ [eksctl](https://docs.aws.amazon.com/eks/latest/userguide/getting-started-eksctl.html) is a command-line utility for creating and managing Kubernetes clusters on Amazon EKS.
+ [kubectl](https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html) is a command-line interface that helps you run commands against Kubernetes clusters.
+ [jq](https://stedolan.github.io/jq/download/) is a command-line tool for parsing JSON.

**Code**

The code for this pattern is provided in the GitHub [Persistence Configuration with Amazon EFS on Amazon EKS using AWS Fargate](https://github.com/aws-samples/eks-efs-share-within-fargate) repo. The scripts are organized by epic, in the folders `epic01` through `epic06`, corresponding to the order in the [Epics](#run-stateful-workloads-with-persistent-data-storage-by-using-amazon-efs-on-amazon-eks-with-aws-fargate-epics) section in this pattern.

## Best practices
<a name="run-stateful-workloads-with-persistent-data-storage-by-using-amazon-efs-on-amazon-eks-with-aws-fargate-best-practices"></a>

The target architecture includes the following services and components, and it follows [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) best practices:
+ Amazon EFS, which provides a simple, scalable, fully managed elastic NFS file system. This is used as a shared file system among all replications of the PoC application that are running in pods, which are distributed in the private subnets of the chosen Amazon EKS cluster.
+ An Amazon EFS mount target for each private subnet. This provides redundancy per Availability Zone within the virtual private cloud (VPC) of the cluster.
+ Amazon EKS, which runs the Kubernetes workloads. You must provision an Amazon EKS cluster before you use this pattern, as described in the [Prerequisites](#run-stateful-workloads-with-persistent-data-storage-by-using-amazon-efs-on-amazon-eks-with-aws-fargate-prereqs) section.
+ AWS KMS, which provides encryption at rest for the content that’s stored in the Amazon EFS file system.
+ Fargate, which manages the compute resources for the containers so that you can focus on business requirements instead of infrastructure burden. The Fargate profile is created for all private subnets. It provides redundancy per Availability Zone within the virtual private cloud (VPC) of the cluster.
+ Kubernetes Pods, for validating that content can be shared, consumed, and written by different instances of an application.

## Epics
<a name="run-stateful-workloads-with-persistent-data-storage-by-using-amazon-efs-on-amazon-eks-with-aws-fargate-epics"></a>

### Provision an Amazon EKS cluster (optional)
<a name="provision-an-amazon-eks-cluster-optional"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an Amazon EKS cluster. | If you already have a cluster deployed, skip to the next epic. Create an Amazon EKS cluster in your existing AWS account. In the [GitHub directory](https://github.com/aws-samples/eks-efs-share-within-fargate/tree/master/bootstrap), use one of the patterns to deploy an Amazon EKS cluster by using Terraform or eksctl. For more information, see [Creating an Amazon EKS cluster](https://docs.aws.amazon.com/eks/latest/userguide/create-cluster.html) in the Amazon EKS documentation. In the Terraform pattern, there are also examples showing how to: link Fargate profiles to your Amazon EKS cluster, create an Amazon EFS file system, and deploy Amazon EFS CSI driver in your Amazon EKS cluster. | AWS administrator, Terraform or eksctl administrator, Kubernetes administrator |
| Export environment variables. | Run the env.sh script. This provides the information required in the next steps.<pre>source ./scripts/env.sh<br />Inform the AWS Account ID:<br /><13-digit-account-id><br />Inform your AWS Region:<br /><aws-Region-code><br />Inform your Amazon EKS Cluster Name:<br /><amazon-eks-cluster-name><br />Inform the Amazon EFS Creation Token:<br /><self-genereated-uuid></pre><br />If not noted yet, you can get all the information requested above with the following CLI commands.<pre># ACCOUNT ID<br />aws sts get-caller-identity --query "Account" --output text</pre><pre># REGION CODE<br />aws configure get region</pre><pre># CLUSTER EKS NAME<br />aws eks list-clusters --query "clusters" --output text</pre><pre># GENERATE EFS TOKEN<br />uuidgen</pre> | AWS systems administrator |

### Create a Kubernetes namespace and a linked Fargate profile
<a name="create-a-kubernetes-namespace-and-a-linked-fargate-profile"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a Kubernetes namespace and Fargate profile for application workloads. | Create a namespace for receiving the application workloads that interact with Amazon EFS. Run the `create-k8s-ns-and-linked-fargate-profile.sh` script. You can choose to use a custom namespace name or the default provided namespace `poc-efs-eks-fargate`.<br />**With a custom application namespace name:**<pre>export $APP_NAMESPACE=<CUSTOM_NAME><br />./scripts/epic01/create-k8s-ns-and-linked-fargate-profile.sh \<br />-c "$CLUSTER_NAME" -n "$APP_NAMESPACE"</pre><br />**Without a custom application namespace name:**<pre>./scripts/epic01/create-k8s-ns-and-linked-fargate-profile.sh \<br />    -c "$CLUSTER_NAME"</pre><br />where `$CLUSTER_NAME` is the name of your Amazon EKS cluster. The `-n <NAMESPACE>` parameter is optional; if not informed, a default generated namespace name will be provided. | Kubernetes user with granted permissions |

### Create an Amazon EFS file system
<a name="create-an-amazon-efs-file-system"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Generate a unique token. | Amazon EFS requires a creation token to ensure idempotent operation (calling the operation with the same creation token has no effect). To meet this requirement, you must generate a unique token through an available technique. For example, you can generate a universally unique identifier (UUID) to use as a creation token. | AWS systems administrator |
| Create an Amazon EFS file system. | Create the file system for receiving the data files that are read and written by the application workloads. You can create an encrypted or non-encrypted file system. (As a best practice, the code for this pattern creates an encrypted system to enable encryption at rest by default.) You can use a unique, symmetric AWS KMS key to encrypt your file system. If a custom key is not specified, an AWS managed key is used.<br />Use the create-efs.sh script to create an encrypted or non-encrypted Amazon EFS file system, after you generate a unique token for Amazon EFS.<br />**With encryption at rest, without a KMS key:**<pre>./scripts/epic02/create-efs.sh \<br />    -c "$CLUSTER_NAME" \<br />    -t "$EFS_CREATION_TOKEN"</pre><br />where `$CLUSTER_NAME` is the name of your Amazon EKS cluster and `$EFS_CREATION_TOKEN` is a unique creation token for the file system.<br />**With encryption at rest, with a KMS key:**<pre>./scripts/epic02/create-efs.sh \<br />    -c "$CLUSTER_NAME" \<br />    -t "$EFS_CREATION_TOKEN" \<br />    -k "$KMS_KEY_ALIAS"</pre><br />where `$CLUSTER_NAME` is the name of your Amazon EKS cluster, `$EFS_CREATION_TOKEN` is a unique creation token for the file system, and `$KMS_KEY_ALIAS` is the alias for the KMS key.<br />**Without encryption:**<pre>./scripts/epic02/create-efs.sh -d \<br />    -c "$CLUSTER_NAME" \<br />    -t "$EFS_CREATION_TOKEN"</pre><br />where `$CLUSTER_NAME` is the name of your Amazon EKS cluster, `$EFS_CREATION_TOKEN` is a unique creation token for the file system, and `–d` disables encryption at rest. | AWS systems administrator |
| Create a security group. | Create a security group to allow the Amazon EKS cluster to access the Amazon EFS file system. | AWS systems administrator |
| Update the inbound rule for the security group. | Update the inbound rules of the security group to allow incoming traffic for the following settings:+ **TCP protocol** – port 2049<br />+ **Source** – CIDR block ranges for the private subnets in the VPC that contains the Kubernetes cluster | AWS systems administrator |
| Add a mount target for each private subnet. | For each private subnet of the Kubernetes cluster, create a mount target for the file system and the security group. | AWS systems administrator |

### Install Amazon EFS components into the Kubernetes cluster
<a name="install-amazon-efs-components-into-the-kubernetes-cluster"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the Amazon EFS CSI driver. | Deploy the Amazon EFS CSI driver into the cluster. The driver provisions storage according to persistent volume claims created by applications. Run the `create-k8s-efs-csi-sc.sh` script to deploy the Amazon EFS CSI driver and the storage class into the cluster.<pre>./scripts/epic03/create-k8s-efs-csi-sc.sh</pre><br />This script uses the `kubectl` utility, so make sure that the context has been configured and point to the desired Amazon EKS cluster. | Kubernetes user with granted permissions |
| Deploy the storage class. | Deploy the storage class into the cluster for the Amazon EFS provisioner (efs.csi.aws.com). | Kubernetes user with granted permissions |

### Install the PoC application into the Kubernetes cluster
<a name="install-the-poc-application-into-the-kubernetes-cluster"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the persistent volume. | Deploy the persistent volume, and link it to the created storage class and to the ID of the Amazon EFS file system. The application uses the persistent volume to read and write content. You can specify any size for the persistent volume in the storage field. Kubernetes requires this field, but because Amazon EFS is an elastic file system, it does not enforce any file system capacity. You can deploy the persistent volume with or without encryption. (The Amazon EFS CSI driver enables encryption by default, as a best practice.) Run the `deploy-poc-app.sh` script to deploy the persistent volume, the persistent volume claim, and the two workloads.<br />**With encryption in transit:**<pre>./scripts/epic04/deploy-poc-app.sh \<br />    -t "$EFS_CREATION_TOKEN"</pre><br />where `$EFS_CREATION_TOKEN` is the unique creation token for the file system.<br />**Without encryption in transit:**<pre>./scripts/epic04/deploy-poc-app.sh -d \<br />    -t "$EFS_CREATION_TOKEN"</pre><br />where `$EFS_CREATION_TOKEN` is the unique creation token for the file system, and `–d` disables encryption in transit. | Kubernetes user with granted permissions |
| Deploy the persistent volume claim requested by the application. | Deploy the persistent volume claim requested by the application, and link it to the storage class. Use the same access mode as the persistent volume you created previously. You can specify any size for the persistent volume claim in the storage field. Kubernetes requires this field, but because Amazon EFS is an elastic file system, it does not enforce any file system capacity. | Kubernetes user with granted permissions |
| Deploy workload 1. | Deploy the pod that represents workload 1 of the application. This workload writes content to the file `/data/out1.txt`. | Kubernetes user with granted permissions |
| Deploy workload 2. | Deploy the pod that represents workload 2 of the application. This workload writes content to the file `/data/out2.txt`. | Kubernetes user with granted permissions |

### Validate file system persistence, durability, and shareability
<a name="validate-file-system-persistence-durability-and-shareability"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Check the status of the `PersistentVolume`. | Enter the following command to check the status of the `PersistentVolume`.<pre>kubectl get pv</pre><br />For an example output, see the [Additional information](#run-stateful-workloads-with-persistent-data-storage-by-using-amazon-efs-on-amazon-eks-with-aws-fargate-additional) section. | Kubernetes user with granted permissions |
| Check the status of the `PersistentVolumeClaim`. | Enter the following command to check the status of the `PersistentVolumeClaim`.<pre>kubectl -n poc-efs-eks-fargate get pvc</pre><br />For an example output, see the [Additional information](#run-stateful-workloads-with-persistent-data-storage-by-using-amazon-efs-on-amazon-eks-with-aws-fargate-additional) section. | Kubernetes user with granted permissions |
| Validate that workload 1 can write to the file system. | Enter the following command to validate that workload 1 is writing to `/data/out1.txt`.<pre>kubectl exec -ti poc-app1 -n poc-efs-eks-fargate -- tail -f /data/out1.txt</pre><br />The results are similar to the following:<pre>...<br />Thu Sep  3 15:25:07 UTC 2023 - PoC APP 1<br />Thu Sep  3 15:25:12 UTC 2023 - PoC APP 1<br />Thu Sep  3 15:25:17 UTC 2023 - PoC APP 1<br />...</pre> | Kubernetes user with granted permissions |
| Validate that workload 2 can write to the file system. | Enter the following command to validate that workload 2 is writing to `/data/out2.txt`.<pre>kubectl -n $APP_NAMESPACE exec -ti poc-app2 -- tail -f /data/out2.txt</pre><br />The results are similar to the following:<pre>...<br />Thu Sep  3 15:26:48 UTC 2023 - PoC APP 2<br />Thu Sep  3 15:26:53 UTC 2023 - PoC APP 2<br />Thu Sep  3 15:26:58 UTC 2023 - PoC APP 2<br />...</pre> | Kubernetes user with granted permissions |
| Validate that workload 1 can read the file written by workload 2. | Enter the following command to validate that workload 1 can read the `/data/out2.txt` file written by workload 2.<pre>kubectl exec -ti poc-app1 -n poc-efs-eks-fargate -- tail -n 3 /data/out2.txt</pre><br />The results are similar to the following:<pre>...<br />Thu Sep  3 15:26:48 UTC 2023 - PoC APP 2<br />Thu Sep  3 15:26:53 UTC 2023 - PoC APP 2<br />Thu Sep  3 15:26:58 UTC 2023 - PoC APP 2<br />...</pre> | Kubernetes user with granted permissions |
| Validate that workload 2 can read the file written by workload 1. | Enter the following command to validate that workload 2 can read the `/data/out1.txt` file written by workload 1.<pre>kubectl -n $APP_NAMESPACE exec -ti poc-app2 -- tail -n 3 /data/out1.txt</pre><br />The results are similar to the following:<pre>...<br />Thu Sep  3 15:29:22 UTC 2023 - PoC APP 1<br />Thu Sep  3 15:29:27 UTC 2023 - PoC APP 1<br />Thu Sep  3 15:29:32 UTC 2023 - PoC APP 1<br />...</pre> | Kubernetes user with granted permissions |
| Validate that files are retained after you remove application components. | Next, you use a script to remove the application components (persistent volume, persistent volume claim, and pods), and validate that the files `/data/out1.txt` and `/data/out2.txt` are retained in the file system. Run the `validate-efs-content.sh` script by using the following command.<pre>./scripts/epic05/validate-efs-content.sh \<br />    -t "$EFS_CREATION_TOKEN"</pre><br />where `$EFS_CREATION_TOKEN` is the unique creation token for the file system.<br />The results are similar to the following:<pre>pod/poc-app-validation created<br />Waiting for pod get Running state...<br />Waiting for pod get Running state...<br />Waiting for pod get Running state...<br />Results from execution of 'find /data' on validation process pod:<br />/data<br />/data/out2.txt<br />/data/out1.txt</pre> | Kubernetes user with granted permissions, System administrator |

### Monitor operations
<a name="monitor-operations"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Monitor application logs. | As part of a day-two operation, ship the application logs to Amazon CloudWatch for monitoring. | AWS systems administrator, Kubernetes user with granted permissions |
| Monitor Amazon EKS and Kubernetes containers with Container Insights. | As part of a day-two operation, monitor the Amazon EKS and Kubernetes systems by using Amazon CloudWatch Container Insights. This tool collects, aggregates, and summarizes metrics from containerized applications at different levels and dimensions. For more information, see the [Related resources](#run-stateful-workloads-with-persistent-data-storage-by-using-amazon-efs-on-amazon-eks-with-aws-fargate-resources) section. | AWS systems administrator, Kubernetes user with granted permissions |
| Monitor Amazon EFS with CloudWatch. | As part of a day-two operation, monitor the file systems using Amazon CloudWatch, which collects and processes raw data from Amazon EFS into readable, near real-time metrics. For more information, see the [Related resources](#run-stateful-workloads-with-persistent-data-storage-by-using-amazon-efs-on-amazon-eks-with-aws-fargate-resources) section. | AWS systems administrator |

### Clean up resources
<a name="clean-up-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clean up all created resources for the pattern. | After you complete this pattern, clean up all resources, to avoid incurring AWS charges. Run the `clean-up-resources.sh` script to remove all resources after you have finished using the PoC application. Complete one of the following options.<br />**With encryption at rest, with a KMS key:**<pre>./scripts/epic06/clean-up-resources.sh \<br />    -c "$CLUSTER_NAME" \<br />    -t "$EFS_CREATION_TOKEN" \<br />    -k "$KMS_KEY_ALIAS"</pre><br />where `$CLUSTER_NAME` is the name of your Amazon EKS cluster, `$EFS_CREATION_TOKEN` is the creation token for the file system, and `$KMS_KEY_ALIAS` is the alias for the KMS key.<br />**Without encryption at rest:**<pre>./scripts/epic06/clean-up-resources.sh \<br />    -c "$CLUSTER_NAME" \<br />    -t "$EFS_CREATION_TOKEN"</pre><br />where `$CLUSTER_NAME` is the name of your Amazon EKS cluster and `$EFS_CREATION_TOKEN` is the creation token for the file system. | Kubernetes user with granted permissions, System administrator |

## Related resources
<a name="run-stateful-workloads-with-persistent-data-storage-by-using-amazon-efs-on-amazon-eks-with-aws-fargate-resources"></a>

**References**
+ [AWS Fargate for Amazon EKS now supports Amazon EFS](https://aws.amazon.com/blogs/aws/new-aws-fargate-for-amazon-eks-now-supports-amazon-efs/) (announcement)
+ [How to capture application logs when using Amazon EKS on AWS Fargate](https://aws.amazon.com/blogs/containers/how-to-capture-application-logs-when-using-amazon-eks-on-aws-fargate/) (blog post)
+ [Using Container Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights.html) (Amazon CloudWatch documentation)
+ [Setting Up Container Insights on Amazon EKS and Kubernetes](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/deploy-container-insights-EKS.html) (Amazon CloudWatch documentation)
+ [Amazon EKS and Kubernetes Container Insights metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-metrics-EKS.html) (Amazon CloudWatch documentation)
+ [Monitoring Amazon EFS with Amazon CloudWatch](https://docs.aws.amazon.com/efs/latest/ug/monitoring-cloudwatch.html) (Amazon EFS documentation)

**GitHub tutorials and examples**
+ [Static provisioning](https://github.com/kubernetes-sigs/aws-efs-csi-driver/blob/master/examples/kubernetes/static_provisioning/README.md)
+ [Encryption in transit](https://github.com/kubernetes-sigs/aws-efs-csi-driver/blob/master/examples/kubernetes/encryption_in_transit/README.md)
+ [Accessing the file system from multiple pods](https://github.com/kubernetes-sigs/aws-efs-csi-driver/blob/master/examples/kubernetes/multiple_pods/README.md)
+ [Consuming Amazon EFS in StatefulSets](https://github.com/kubernetes-sigs/aws-efs-csi-driver/blob/master/examples/kubernetes/statefulset/README.md)
+ [Mounting subpaths](https://github.com/kubernetes-sigs/aws-efs-csi-driver/blob/master/examples/kubernetes/volume_path/README.md)
+ [Using Amazon EFS access points](https://github.com/kubernetes-sigs/aws-efs-csi-driver/blob/master/examples/kubernetes/access_points/README.md)
+ [Amazon EKS Blueprints for Terraform](https://aws-ia.github.io/terraform-aws-eks-blueprints/)

**Required tools**
+ [Installing the AWS CLI version 2](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
+ [Installing eksctl](https://docs.aws.amazon.com/eks/latest/userguide/getting-started-eksctl.html)
+ [Installing kubectl](https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html)
+ [Installing jq](https://stedolan.github.io/jq/download/)

## Additional information
<a name="run-stateful-workloads-with-persistent-data-storage-by-using-amazon-efs-on-amazon-eks-with-aws-fargate-additional"></a>

The following is an example output of the `kubectl get pv` command.

```
NAME         CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                             STORAGECLASS   REASON   AGE
poc-app-pv   1Mi        RWX            Retain           Bound    poc-efs-eks-fargate/poc-app-pvc   efs-sc                  3m56s
```

The following is an example output of the `kubectl -n poc-efs-eks-fargate get pvc` command.

```
NAME          STATUS   VOLUME       CAPACITY   ACCESS MODES   STORAGECLASS   AGE
poc-app-pvc   Bound    poc-app-pv   1Mi        RWX            efs-sc         4m34s
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
