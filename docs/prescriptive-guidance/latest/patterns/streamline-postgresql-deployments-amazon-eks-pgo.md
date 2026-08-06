---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/streamline-postgresql-deployments-amazon-eks-pgo.html
---

# Streamline PostgreSQL deployments on Amazon EKS by using PGO
<a name="streamline-postgresql-deployments-amazon-eks-pgo"></a>

*Shalaka Dengale, Amazon Web Services*

## Summary
<a name="streamline-postgresql-deployments-amazon-eks-pgo-summary"></a>

This pattern integrates the Postgres Operator from Crunchy Data (PGO) with Amazon Elastic Kubernetes Service (Amazon EKS) to streamline PostgreSQL deployments in cloud-native environments. PGO provides automation and scalability for managing PostgreSQL databases in Kubernetes. When you combine PGO with Amazon EKS, it forms a robust platform for deploying, managing, and scaling PostgreSQL databases efficiently.

This integration provides the following key benefits:
+ Automated deployment: Simplifies PostgreSQL cluster deployment and management.
+ Custom resource definitions (CRDs):** **Uses Kubernetes primitives for PostgreSQL management.
+ High availability: Supports automatic failover and synchronous replication.
+ Automated backups and restores:** **Streamlines backup and restore processes.
+ Horizontal scaling:** **Enables dynamic scaling of PostgreSQL clusters.
+ Version upgrades: Facilitates rolling upgrades with minimal downtime.
+ Security: Enforces encryption, access controls, and authentication mechanisms.

## Prerequisites and limitations
<a name="streamline-postgresql-deployments-amazon-eks-pgo-prereqs"></a>

**Prerequisites**
+ An active AWS account.
+ [AWS Command Line Interface (AWS CLI) version 2](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html), installed and configured on Linux, macOS, or Windows.
+ [AWS CLI Config](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-quickstart.html), to connect AWS resources from the command line.
+ [eksctl](https://github.com/eksctl-io/eksctl#installation), installed and configured on Linux, macOS, or Windows.
+ `kubectl`, installed and configured to access resources on your Amazon EKS cluster. For more information, see [Set up kubectl and eksctl](https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html) in the Amazon EKS documentation.
+ Your computer terminal configured to access the Amazon EKS cluster. For more information, see [Configure your computer to communicate with your cluster](https://docs.aws.amazon.com/eks/latest/userguide/getting-started-console.html#eks-configure-kubectl) in the Amazon EKS documentation.

**Product versions**
+ Kubernetes versions 1.21–1.24 or later (see the [PGO documentation](https://access.crunchydata.com/documentation/postgres-operator/5.2.5/)).
+ PostgreSQL version 10 or later. This pattern uses PostgreSQL version 16.

**Limitations**
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see the [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) page, and choose the link for the service.

## Architecture
<a name="streamline-postgresql-deployments-amazon-eks-pgo-architecture"></a>

**Target technology stack **
+ Amazon EKS
+ Amazon Virtual Private Cloud (Amazon VPC)
+ Amazon Elastic Compute Cloud (Amazon EC2)

**Target architecture **

![Architecture for using PGO with three Availability Zones and two replicas, PgBouncer, and PGO operator.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/4c164012-7527-4ebe-b6a7-c129600328d6/images/26a5572b-405b-4634-b96a-91254c3ea2c1.png)

This pattern builds an architecture that contains an Amazon EKS cluster with three nodes. Each node runs on a set of EC2 instances in the backend. This PostgreSQL setup follows a primary replica architecture, which is particularly effective for read-heavy use cases. The architecture includes the following components:
+ **Primary database container (pg-primary)** hosts the main PostgreSQL instance where all write operations are directed.
+ **Secondary replica containers (pg-replica)** host the PostgreSQL instances that replicate the data from the primary database and handle read operations.
+ **PgBouncer** is a lightweight connection pooler for PostgreSQL databases that's included with PGO. It sits between the client and the PostgreSQL server, and acts as an intermediary for database connections.
+ **PGO** automates the deployment and management of PostgreSQL clusters in this Kubernetes environment.
+ **Patroni** is an open-source tool that manages and automates high availability configurations for PostgreSQL. It's included with PGO. When you use Patroni with PGO in Kubernetes, it plays a crucial role in ensuring the resilience and fault tolerance of a PostgreSQL cluster. For more information, see the [Patroni documentation](https://patroni.readthedocs.io/en/latest/).

The workflow includes these steps:
+ **Deploy the PGO operator**. You deploy the PGO operator on your Kubernetes cluster that runs on Amazon EKS. This can be done by using Kubernetes manifests or Helm charts. This pattern uses Kubernetes manifests.
+ **Define PostgreSQL instances**. When the operator is running, you create custom resources (CRs) to specify the desired state of PostgreSQL instances. This includes configurations such as storage, replication, and high availability settings.
+ **Operator management**. You interact with the operator through Kubernetes API objects such as CRs to create, update, or delete PostgreSQL instances.
+ **Monitoring and maintenance**. You can monitor the health and performance of the PostgreSQL instances running on Amazon EKS. Operators often provide metrics and logging for monitoring purposes. You can perform routine maintenance tasks such as upgrades and patching as necessary. For more information, see [Monitor your cluster performance and view logs](https://docs.aws.amazon.com/eks/latest/userguide/eks-observe.html) in the Amazon EKS documentation.
+ **Scaling and backup**: You can use the features provided by the operator to scale PostgreSQL instances and manage backups.

This pattern doesn't cover monitoring, maintenance, and backup operations.

**Automation and scale**
+ You can use CloudFormation to automate the infrastructure creation. For more information, see [Create Amazon EKS resources with CloudFormation](https://docs.aws.amazon.com/eks/latest/userguide/creating-resources-with-cloudformation.html) in the Amazon EKS documentation.
+ You can use GitVersion or Jenkins build numbers to automate the deployment of database instances.

## Tools
<a name="streamline-postgresql-deployments-amazon-eks-pgo-tools"></a>

**AWS services**
+ [Amazon Elastic Kubernetes Service (Amazon EKS)](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html) helps you run Kubernetes on AWS without needing to install or maintain your own Kubernetes control plane or nodes.
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open-source tool that helps you interact with AWS services through commands in your command line shell.

**Other tools**
+ [eksctl](https://eksctl.io/) is a simple command line tool for creating clusters on Amazon EKS.
+ [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/) is a command line utility for running commands against Kubernetes clusters.
+ [PGO](https://github.com/CrunchyData/postgres-operator) automates and scales the management of PostgreSQL databases in Kubernetes.

## Best practices
<a name="streamline-postgresql-deployments-amazon-eks-pgo-best-practices"></a>

Follow these best practices to ensure a smooth and efficient deployment:
+ **Secure your EKS cluster**. Implement security best practices for your EKS cluster, such as using AWS Identity and Access Management (IAM) roles for service accounts (IRSA), network policies, and VPC security groups. Limit access to the EKS cluster API server, and encrypt communications between nodes and the API server by using TLS.
+ **Ensure version compatibility** between PGO and Kubernetes running on Amazon EKS. Some PGO features might require specific Kubernetes versions or introduce compatibility limitations. For more information, see [Components and Compatibility](https://access.crunchydata.com/documentation/postgres-operator/5.2.5/references/components/) in the PGO documentation.
+ **Plan resource allocation** for your PGO deployment, including CPU, memory, and storage. Consider the resource requirements of both PGO and the PostgreSQL instances it manages. Monitor resource usage and scale resources as needed.
+ **Design for high availability**. Design your PGO deployment for high availability to minimize downtime and ensure reliability. Deploy multiple replicas of PGO across multiple Availability Zones for fault tolerance.
+ **Implement backup and restore procedures** for your PostgreSQL databases that PGO manages. Use features provided by PGO or third-party backup solutions that are compatible with Kubernetes and Amazon EKS.
+ **Set up monitoring and logging** for your PGO deployment to track performance, health, and events. Use tools such as Prometheus for monitoring metrics and Grafana for visualization. Configure logging to capture PGO logs for troubleshooting and auditing.
+ **Configure networking** properly to allow communications between PGO, PostgreSQL instances, and other services in your Kubernetes cluster. Use Amazon VPC networking features and Kubernetes networking plugins such as Calico or [Amazon VPC CNI](https://github.com/aws/amazon-vpc-cni-k8s) for network policy enforcement and traffic isolation.
+ **Choose appropriate storage options** for your PostgreSQL databases, considering factors such as performance, durability, and scalability. Use Amazon Elastic Block Store (Amazon EBS) volumes or AWS managed storage services for persistent storage. For more information, see [Store Kubernetes volumes with Amazon EBS](https://docs.aws.amazon.com/eks/latest/userguide/ebs-csi.html) in the Amazon EKS documentation.
+ **Use infrastructure as code (IaC) tools** such as CloudFormation to automate the deployment and configuration of PGO on Amazon EKS. Define infrastructure components—including the EKS cluster, networking, and PGO resources—as code for consistency, repeatability, and version control.

## Epics
<a name="streamline-postgresql-deployments-amazon-eks-pgo-epics"></a>

### Create an IAM role
<a name="create-an-iam-role"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an IAM role. | 1. Create an IAM role by using the following command in the AWS CLI:<pre>aws iam create-role \<br />    --role-name {YourRoleName} \<br />    --assume-role-policy-document '{<br />        "Version": "2012-10-17",		 	 	 <br />        "Statement": [<br />            {<br />                "Effect": "Allow",<br />                "Principal": {<br />                    "Service": "eks.amazonaws.com"<br />                },<br />                "Action": "sts:AssumeRole"<br />            }<br />        ]<br />    }' && \<br />aws iam attach-role-policy \<br />    --role-name {YourRoleName}\<br />    --policy-arn arn:aws:iam::aws:policy/AmazonEKSClusterPolicy && \<br />aws iam attach-role-policy \<br />    --role-name {YourRoleName}\<br />    --policy-arn arn:aws:iam::aws:policy/AmazonEKSServicePolicy && \<br />aws iam attach-role-policy \<br />    --role-name {YourRoleName}\<br />	    --policy-arn arn:aws:iam::aws:policy/CloudWatchFullAccess</pre><br />2. Review the role in the AWS Management Console:Open the [IAM console](https://console.aws.amazon.com/iam/).Choose **Roles**, and search for the role name you created.Validate that the following policies are attached:<br />`AmazonEKSClusterPolicy`<br />`AmazonEKSServicePolicy`<br />`CloudWatchFullAccess` | AWS administrator |

### Create an Amazon EKS cluster
<a name="create-an-eks-cluster"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an Amazon EKS cluster. | If you've already deployed a cluster, skip this step. Otherwise, deploy an Amazon EKS cluster in your current AWS account by using `eksctl`, Terraform, or CloudFormation. This pattern uses `eksctl` for cluster deployment.This pattern uses Amazon EC2 as a node group for Amazon EKS. If you want to use AWS Fargate, see the `managedNodeGroups` configuration in the [eksctl documentation](https://eksctl.io/usage/schema/#managedNodeGroups).1. Use the following `eksctl` input file to generate the cluster.<br />`sample-cluster.yaml`:<pre>apiVersion: eksctl.io/v1alpha5<br />kind: ClusterConfig<br />metadata:<br />  name: postgresql<br />  region: us-east-1<br />  version: "1.29"<br />accessConfig:<br />  authenticationMode: API_AND_CONFIG_MAP<br />availabilityZones:<br />- us-east-1a<br />- us-east-1b<br />- us-east-1c<br />nodeGroups:<br />  - name: ng-1<br />    instanceType: m5.16xlarge<br />    desiredCapacity: 2<br />  - name: ng-2<br />    instanceType: m5.16xlarge<br />    desiredCapacity: 2<br />  - name: ng-3<br />    instanceType: m5.16xlarge<br />    desiredCapacity: 2<br />vpc:<br />  cidr: 192.168.0.0/16<br />  clusterEndpoints:<br />    publicAccess: true<br />  nat:<br />    gateway: HighlyAvailable<br />iamIdentityMappings:<br />  - arn: arn:aws:iam::<account-id>:role/<role-name> # update the IAM role ARN created in step 1<br />    username: <user-name> # Enter the user name per your choice<br />    noDuplicateARNs: false</pre><br />2. Run the following command to create the cluster (provide the file path to your `sample-cluster.yaml` file):<pre>eksctl create cluster -f sample-cluster.yaml</pre> | AWS administrator, Terraform or eksctl administrator, Kubernetes administrator |
| Validate the status of the cluster. | Run the following command to see the current status of nodes in the cluster:<pre>kubectl get nodes</pre><br />If you encounter errors, see the [troubleshooting section](https://docs.aws.amazon.com/eks/latest/userguide/troubleshooting.html) of the Amazon EKS documentation. | AWS administrator, Terraform or eksctl administrator, Kubernetes administrator |

### Create an OIDC identity provider
<a name="create-an-oidc-identity-provider"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Enable the IAM OIDC provider. | As a prerequisite for the Amazon EBS Container Storage Interface (CSI) driver, you must have an existing IAM OpenID Connect (OIDC) provider for your cluster.<br />Enable the IAM OIDC provider by using the following command:<pre>eksctl utils associate-iam-oidc-provider --region={region} --cluster={YourClusterNameHere} --approve</pre><br />For more information about this step, see the [Amazon EKS documentation](https://docs.aws.amazon.com/eks/latest/userguide/ebs-csi.html). | AWS administrator |
| Create an IAM role for the Amazon EBS CSI driver. | Use the following `eksctl` command to create the IAM role for the CSI driver:<pre>eksctl create iamserviceaccount \<br />  --region {RegionName} \<br />  --name ebs-csi-controller-sa \<br />  --namespace kube-system \<br />  --cluster {YourClusterNameHere} \<br />  --attach-policy-arn arn:aws:iam::aws:policy/service-role/AmazonEBSCSIDriverPolicy \<br />  --approve \<br />  --role-only \<br />  --role-name AmazonEKS_EBS_CSI_DriverRole</pre><br />If you use encrypted Amazon EBS drives, you have to configure the policy further. For instructions, see the [Amazon EBS SCI driver documentation](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/blob/master/docs/install.md#installation-1). | AWS administrator |
| Add the Amazon EBS CSI driver. | Use the following `eksctl` command to add the Amazon EBS CSI driver:<pre>eksctl create addon \<br />  --name aws-ebs-csi-driver \<br />  --cluster <YourClusterName> service-account-role-arn arn:aws:iam::$(aws sts get-caller-identity \<br />  --query Account \<br />  --output text):role/AmazonEKS_EBS_CSI_DriverRole \<br />  --force</pre> | AWS administrator |

### Install PGO
<a name="install-pgo"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the PGO repository. | Clone the GitHub repository for PGO:<pre>git clone https://github.com/CrunchyData/postgres-operator-examples.git </pre> | AWS DevOps |
| Provide the role details for service account creation. | To grant the Amazon EKS cluster access to the required AWS resources, specify the Amazon Resource Name (ARN) of the OIDC role that you created earlier in the `service_account.yaml` file that is located in [GitHub](https://github.com/CrunchyData/postgres-operator/blob/main/config/rbac/cluster/service_account.yaml).<pre>cd postgres-operator-examples</pre><pre>---<br />metadata:<br />  annotations:<br />    eks.amazonaws.com/role-arn: arn:aws:iam::<accountId>:role/<role_name> # Update the OIDC role ARN created earlier</pre> | AWS administrator, Kubernetes administrator |
| Create the namespace and PGO prerequisites. | 1. Run the following command to create the namespace:<pre>kubectl apply -k kustomize/install/namespace</pre><br />This establishes a dedicated namespace for PGO. If necessary, you can modify the `namespace.yml` file and assign the namespace  a different name.<br />2. Run the following command to apply the default configuration to the cluster:<pre>kubectl apply --server-side -k kustomize/install/default</pre><br />`kustomize/install/default` provides the default configuration for the Kubernetes role-based access control (RBAC), custom resource definition (CRD), and Kubernetes Manager files. | Kubernetes administrator |
| Verify the creation of pods. | Verify that the namespace and default configuration were created:<pre>kubectl get pods -n postgres-operator</pre> | AWS administrator, Kubernetes administrator |
| Verify PVCs. | Use the following command to verify persistent volume claims (PVCs):<pre>kubectl describe pvc -n postgres-operator</pre> | AWS administrator, Kubernetes administrator |

### Create and deploy an operator
<a name="create-and-deploy-an-operator"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an operator. | Revise the contents of the file located at `/kustomize/postgres/postgres.yaml` to match the following:<pre>spec:<br />  instances:<br />    - name: pg-1<br />      replicas: 3<br />  patroni:<br />    dynamicConfiguration:<br />      postgresql:<br />      pg_hba:<br />        - "host all all 0.0.0.0/0 trust" # this line enabled logical replication with programmatic access<br />        - "host all postgres 127.0.0.1/32 md5"<br />      synchronous_mode: true<br />  users:<br />  - name: replicator<br />    databases:<br />      - testdb<br />    options: "REPLICATION"</pre><br />These updates do the following:+ Adjust the PostgreSQL configuration settings to facilitate access to the PostgreSQL instance.<br />+ Include configurations for replication user, database user, and superuser to enable streaming replication, database access, and cluster management. | AWS administrator, DBA, Kubernetes administrator |
| Deploy the operator. | Deploy the PGO operator to enable the streamlined management and operation of PostgreSQL databases in Kubernetes environments:<pre>kubectl apply -k kustomize/postgres</pre> | AWS administrator, DBA, Kubernetes administrator |
| Verify the deployment. | 1. Validate that the operator has been deployed:<pre>kubectl get pods -n postgres-operator --selector=postgres-operator.crunchydata.com/instance-set \   -L postgres-operator.crunchydata.com/role </pre><br />2. Verify that the service resource associated with the operator pod has been created:<pre>kubectl get svc -n postgres-operator</pre>From the command output, note the primary replica (`primary_pod_name`) and read replica (`read_pod_name`). You will uses these in the next steps. | AWS administrator, DBA, Kubernetes administrator |

### Verify streaming replication
<a name="verify-streaming-replication"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Write data to the primary replica. | Use the following commands to connect to the PostgreSQL primary replica and write data to the database:<pre>kubectl exec -it <primary_pod_name> bash -n postgres-operator</pre><pre>psql</pre><pre>CREATE TABLE customers (firstname text, customer_id serial, date_created timestamp);<br />\dt</pre> | AWS administrator, Kubernetes administrator |
| Confirm that the read replica has the same data. | Connect to the PostgreSQL read replica and check whether the streaming replication is working correctly:<pre>kubectl exec -it {read_pod_name} bash -n postgres-operator</pre><pre>psql</pre><pre>\dt</pre><br />The read replica should have the table that you created in the primary replica in the previous step. | AWS administrator, Kubernetes administrator |

## Troubleshooting
<a name="streamline-postgresql-deployments-amazon-eks-pgo-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| The pod doesn’t start. | + Use the following command to inspect pod status:<pre>kubectl get pods -n your-namespace </pre><br />+ Inspect the logs for any errors:<pre>kubectl logs your-pod-name -n your-namespace</pre><br />+ Check pod events for any abnormal events related to your pods:<pre>kubectl describe pod your-pod-name -n your-namespace</pre> |
| Replicas are significantly behind the primary database. | + Check for replication lag:<pre>SELECT * FROM pg_stat_replication;</pre><br />+ Make sure that replicas have enough CPU and memory resources. Check resource limits:<pre>kubectl describe pod your-replica-pod -n your-namespace</pre><br />+ Verify that the storage backend is performing optimally. Slow disk I/O can cause replication lag. |
| You don’t have visibility into the performance and health of the PostgreSQL cluster. | + Enable Amazon CloudWatch Logs and make sure that logs are being sent to Amazon CloudWatch for analysis. For more information, see the [Amazon EKS documentation](https://docs.aws.amazon.com/eks/latest/userguide/eks-observe.html#eks-monitor-tools).<br />+ Check** **`pg_stat_activity`:<pre>SELECT * FROM pg_stat_activity;</pre> |
| Replication doesn’t work. | + Check the primary configuration by viewing the replication settings in `postgresql.conf`:<pre>wal_level = replica</pre><pre>max_wal_senders = 10</pre><pre>wal_keep_size = 64  # or wal_keep_segments in older versions</pre><br />+ Verify that `pg_hba.conf` includes replication permissions:<pre>host replication replica_user all md5</pre><br />+ Check replica configuration. Make sure that `recovery.conf` or equivalent settings (`standby.signal` and `primary_conninfo`) are correctly set up on replicas. |

## Related resources
<a name="streamline-postgresql-deployments-amazon-eks-pgo-resources"></a>
+ [Amazon Elastic Kubernetes Service](https://docs.aws.amazon.com/whitepapers/latest/overview-deployment-options/amazon-elastic-kubernetes-service.html) (*Overview of Deployment Options on AWS* whitepaper)
+  [CloudFormation](https://docs.aws.amazon.com/whitepapers/latest/overview-deployment-options/aws-cloudformation.html) (*Overview of Deployment Options on AWS* whitepaper)
+ [Get started with Amazon EKS – eksctl](https://docs.aws.amazon.com/eks/latest/userguide/getting-started-eksctl.html) (*Amazon EKS User Guide*)
+ [Set up kubectl and eksctl](https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html) (*Amazon EKS User Guide*)
+ [Create a role for OpenID Connect federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp_oidc.html) (*IAM User Guide*)
+ [Configuring settings for the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) (*AWS CLI User Guide*)
+ [Crunchy Postgres for Kubernetes documentation](https://access.crunchydata.com/documentation/postgres-operator/latest)
+ [Crunch & Learn: Crunchy Postgres for Kubernetes 5.0](https://www.youtube-nocookie.com/embed/IIf9WZO3K50) (video)
