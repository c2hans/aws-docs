---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/set-up-a-grafana-monitoring-dashboard-for-aws-parallelcluster.html
---

# Set up a Grafana monitoring dashboard for AWS ParallelCluster
<a name="set-up-a-grafana-monitoring-dashboard-for-aws-parallelcluster"></a>

*Dario La Porta and William Lu, Amazon Web Services*

## Summary
<a name="set-up-a-grafana-monitoring-dashboard-for-aws-parallelcluster-summary"></a>

AWS ParallelCluster helps you deploy and manage high performance computing (HPC) clusters. It supports AWS Batch and Slurm open source job schedulers. Although AWS ParallelCluster is integrated with Amazon CloudWatch for logging and metrics, it doesn't provide a monitoring dashboard for the workload.

The [Grafana dashboard for AWS ParallelCluster](https://github.com/aws-samples/aws-parallelcluster-monitoring) (GitHub) is a monitoring dashboard for AWS ParallelCluster. It provides job scheduler insights and detailed monitoring metrics at the operating system (OS) level. For more information about the dashboards included in this solution, see [Example Dashboards](https://github.com/aws-samples/aws-parallelcluster-monitoring#example-dashboards) in the GitHub repository. These metrics help you better understand the HPC workload and its performance. However, the dashboard code is not updated for the latest versions of AWS ParallelCluster or the open source packages that are used in solution. This pattern enhances the solution to provide the following benefits:
+ Supports AWS ParallelCluster v3
+ Uses the latest version of open source packages, including Prometheus, Grafana, Prometheus Slurm Exporter, and NVIDIA DCGM-Exporter
+ Increases the number of CPU cores and GPUs that the Slurm jobs use
+ Adds a job monitoring dashboard
+ Enhances the GPU node monitoring dashboard for nodes with 4 or 8 graphics processing units (GPUs)

This version of the enhanced solution has been implemented and verified in an AWS customer's HPC production environment.

## Prerequisites and limitations
<a name="set-up-a-grafana-monitoring-dashboard-for-aws-parallelcluster-prereqs"></a>

**Prerequisites**
+ [AWS ParallelCluster CLI](https://docs.aws.amazon.com/parallelcluster/latest/ug/pcluster-v3.html), installed and configured.
+ A supported [network configuration](https://docs.aws.amazon.com/parallelcluster/latest/ug/iam-roles-in-parallelcluster-v3.html) for AWS ParallelCluster. This pattern uses the [AWS ParallelCluster using two subnets](https://docs.aws.amazon.com/parallelcluster/latest/ug/network-configuration-v3.html#network-configuration-v3-two-subnets) configuration, which requires a public subnet, private subnet, internet gateway, and NAT gateway.
+ All AWS ParallelCluster cluster nodes must have internet access. This is required so that the installation scripts can download the open source software and Docker images.
+ A [key pair](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html) in Amazon Elastic Compute Cloud (Amazon EC2). Resources that have this key pair have Secure Shell (SSH) access to the head node.

**Limitations**
+ This pattern is designed to support Ubuntu 20.04 LTS. If you're using a different version of Ubuntu or if you use Amazon Linux or CentOS, then you need to modify the scripts provided with this solution. These modifications are not included in this pattern.

**Product versions**
+ Ubuntu 20.04 LTS
+ ParallelCluster 3.X

**Billing and cost considerations**
+ The solution deployed in this pattern is not covered by the free tier. Charges apply for Amazon EC2, Amazon FSx for Lustre, the NAT gateway in Amazon VPC, and Amazon Route 53.

## Architecture
<a name="set-up-a-grafana-monitoring-dashboard-for-aws-parallelcluster-architecture"></a>

**Target architecture**

The following diagram shows how a user can access the monitoring dashboard for AWS ParallelCluster on the head node. The head node runs NICE DCV, Prometheus, Grafana, Prometheus Slurm Exporter, Prometheus Node Exporter, and NGINX Open Source. The compute nodes run Prometheus Node Exporter, and they also run NVIDIA DCGM-Exporter if the node contains GPUs. The head node retrieves information from the compute nodes and displays that data in the Grafana dashboard.

![Accessing the monitoring dashboard for AWS ParallelCluster on the head node.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/a2132c94-98e0-4b90-8be0-99ebfa546442/images/d2255792-f66a-4ef2-8f04-cc3d5482db5f.png)

In most cases, the head node is not heavily loaded because the job scheduler doesn't require a significant amount of CPU or memory. Users access the dashboard on the head node by using SSL on port 443.

All authorized viewers can anonymously view the monitoring dashboards. Only the Grafana administrator can modify dashboards. You configure a password for the Grafana administrator in the `aws-parallelcluster-monitoring/docker-compose/docker-compose.head.yml` file.

## Tools
<a name="set-up-a-grafana-monitoring-dashboard-for-aws-parallelcluster-tools"></a>

**AWS services**
+ [NICE DCV](https://docs.aws.amazon.com/dcv/#nice-dcv) is a high-performance remote display protocol that helps you deliver remote desktops and application streaming from any cloud or data center to any device, over varying network conditions.
+ [AWS ParallelCluster](https://docs.aws.amazon.com/parallelcluster/latest/ug/what-is-aws-parallelcluster.html) helps you deploy and manage high performance computing (HPC) clusters. It supports AWS Batch and Slurm open source job schedulers.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.
+ [Amazon Virtual Private Cloud (Amazon VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) helps you launch AWS resources into a virtual network that you’ve defined.

**Other tools**
+ [Docker](https://www.docker.com/) is a set of platform as a service (PaaS) products that use virtualization at the operating-system level to deliver software in containers.
+ [Grafana](https://grafana.com/docs/grafana/latest/introduction/) is an open source software that helps you query, visualize, alert on, and explore metrics, logs, and traces.
+ [NGINX Open Source](https://nginx.org/en/docs/?_ga=2.187509224.1322712425.1699399865-405102969.1699399865) is an open source web server and reverse proxy.
+ [NVIDIA Data Center GPU Manager (DCGM)](https://docs.nvidia.com/data-center-gpu-manager-dcgm/index.html) is a suite of tools for managing and monitoring NVIDIA data center graphics processing units (GPUs) in cluster environments. In this pattern, you use [DCGM-Exporter](https://github.com/NVIDIA/dcgm-exporter), which helps you export GPU metrics from Prometheus.
+ [Prometheus](https://prometheus.io/docs/introduction/overview/) is an open source system-monitoring toolkit that collects and stores its metrics as time-series data with associated key-value pairs, which are called *labels*. In this pattern, you also use [Prometheus Slurm Exporter](https://github.com/vpenso/prometheus-slurm-exporter) to collect and export metrics, and you use [Prometheus Node Exporter](https://github.com/prometheus/node_exporter) to export metrics from the compute nodes.
+ [Ubuntu](https://help.ubuntu.com/) is an open source, Linux-based operating system that is designed for enterprise servers, desktops, cloud environments, and IoT.

**Code repository**

The code for this pattern is available in the GitHub [pcluster-monitoring-dashboard](https://github.com/aws-samples/parallelcluster-monitoring-dashboard) repository.

## Epics
<a name="set-up-a-grafana-monitoring-dashboard-for-aws-parallelcluster-epics"></a>

### Create the required resources
<a name="create-the-required-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an S3 bucket. | Create an Amazon S3 bucket. You use this bucket to store the configuration scripts. For instructions, see [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) in the Amazon S3 documentation. | General AWS |
| Clone the repository. | Clone the GitHub [pcluster-monitoring-dashboard](https://github.com/aws-samples/parallelcluster-monitoring-dashboard/tree/main/aws-parallelcluster-monitoring) repo by running the following command.<pre>git clone https://github.com/aws-samples/parallelcluster-monitoring-dashboard.git</pre> | DevOps engineer |
| Create an admin password. | 1. Choose the `aws-parallelcluster-monitoring` folder, choose the `docker-compose` folder, and then open the **docker-compose.head.yml** file.<br />2. In the `GF_SECURITY_ADMIN_PASSWORD` variable, replace `Grafana4PC!` with a password of your choice. This is the administrative password that you use to manage the Grafana account.<br />3. Save and close the** docker-compose.head.yml** file. | Linux Shell scripting |
| Copy the required files into the S3 bucket. | Copy the [post\_install.sh](https://github.com/aws-samples/parallelcluster-monitoring-dashboard/blob/main/post_install.sh) script and the [aws-parallelcluster-monitoring](https://github.com/aws-samples/parallelcluster-monitoring-dashboard/tree/main/aws-parallelcluster-monitoring) folder into the S3 bucket you created. For instructions, see [Uploading objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html) in the Amazon S3 documentation. | General AWS |
| Configure an additional security group for the head node. | 1. Create a security group for the head node. This security group will allow inbound traffic to the monitoring dashboards on the head node. For instructions, see [Create a security group](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-security-groups.html#creating-security-groups) in the Amazon VPC documentation.<br />2. Add an inbound rule to the security group. For instructions, see [Add rules to a security group](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-security-groups.html#adding-security-group-rules) in the Amazon VPC documentation. Use the following parameters for the rule:**Type** – HTTPS**Protocol** – TCP**Port range** – 443**Source** – Enter your IP address**Description** – Allow users to access the monitoring dashboard | AWS administrator |
| Configure an IAM policy for the head node. | Create an identity-based policy for the head node. This policy allows the node to retrieve metric data from Amazon CloudWatch. The GitHub repo contains an example [policy](https://github.com/aws-samples/parallelcluster-monitoring-dashboard/blob/main/policies/head_node.json). For instructions, see [Creating IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) in the AWS Identity and Access Management (IAM) documentation. | AWS administrator |
| Configure an IAM policy for the compute nodes. | Create an identity-based policy for the compute nodes. This policy allows the node to create the tags that contain the job ID and job owner. The GitHub repo contains an example [policy](https://github.com/aws-samples/parallelcluster-monitoring-dashboard/blob/main/policies/compute_node.json). For instructions, see [Creating IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) in the IAM documentation.<br />If you use the provided example file, replace the following values:+ **<REGION>** – The AWS Region where the cluster is hosted<br />+ **<ACCOUNT\_ID>** – The AWS account ID | AWS administrator |

### Create the cluster
<a name="create-the-cluster"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Modify the provided cluster template file. | Create the AWS ParallelCluster cluster. Use the provided [cluster.yaml](https://github.com/aws-samples/parallelcluster-monitoring-dashboard/blob/main/cluster.yaml) AWS CloudFormation template file as a starting point to create the cluster. Replace the following values in the provided template:+ **<REGION>** – The AWS Region where the cluster is hosted.<br />+ **<HEADNODE\_SUBNET>** – The public subnet of the VPC.<br />+ **<ADDITIONAL\_HEAD\_NODE\_SG>** – The name of the security group that you created for the head node.<br />+ **<KEY\_NAME>** – Enter the name of an existing Amazon EC2 key pair. Resources that have this key pair have Secure Shell (SSH) access to the head node.<br />+ **<ALLOWED\_IPS>** -–Enter the CIDR-formatted IP address range that is allowed to make SSH connections to the head node.<br />+ **<ADDITIONAL\_HEAD\_NODE\_POLICY>** – Enter the name of the IAM policy that you created for the head node.<br />+ **<BUCKET\_NAME>** – Enter the name of the S3 bucket you created.<br />+ **<COMPUTE\_SUBNET>** – Enter the name of the private subnet in the VPC.<br />+ **<ADDITIONAL\_COMPUTE\_NODE\_POLICY>** – Enter the name of the IAM policy that you created for the compute node. | AWS administrator |
| Create the cluster. | In the AWS ParallelCluster CLI, enter the following command. This deploys the CloudFormation template and creates the cluster. For more information about this command, see [pcluster create-cluster](https://docs.aws.amazon.com/parallelcluster/latest/ug/pcluster.create-cluster-v3.html) in the AWS ParallelCluster documentation.<pre>pcluster create-cluster -n <cluster_name> -c cluster.yaml</pre> | AWS administrator |
| Monitor the cluster creation. | Enter the following command to monitor the cluster creation. For more information about this command, see [pcluster describe-cluster](https://docs.aws.amazon.com/parallelcluster/latest/ug/pcluster.describe-cluster-v3.html) in the AWS ParallelCluster documentation.<pre>pcluster describe-cluster -n <cluster_name></pre> | AWS administrator |

### Using the Grafana dashboards
<a name="using-the-grafana-dashboards"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Access to the Grafana portal. | 1. Enter the following command to retrieve the public IP address of the head node.<pre>pcluster describe-cluster -n <cluster_name> --query headNode.publicIpAddress</pre><br />2. In a web browser, navigate to the following URL in order to access the Grafana dashboard.<br />**https://<head\_node\_public\_ip\_address>**<br />3. On the Grafana front page, choose the 4-square **Dashboard** icon on the left menu, and then choose **General**. This shows a list of configured dashboards. The following dashboards are available in Grafana:**Cluster Cost** – Contains information about the cost of the cluster**Cluster Logs** – Contains information about the logs of the cluster**Compute Node Details –** Contains information about usage statistics of the compute nodes**Compute Node List** – Contains the list of the compute nodes of the cluster**GPU Nodes** – Contains information about usage statistics of the GPU nodes**Jobs Details** – Contains information about the jobs resources utilization**Head Node Details** – Contains information about usage statistics of the head node**ParallelCluster Summary** – Contains information about cluster usage | AWS administrator |

### Clean up the solution to stop incurring associated costs
<a name="clean-up-the-solution-to-stop-incurring-associated-costs"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Delete the cluster. | Enter the following command to delete the cluster. For more information about this command, see [pcluster delete-cluster](https://docs.aws.amazon.com/parallelcluster/latest/ug/pcluster.delete-cluster-v3.html) in the AWS ParallelCluster documentation.<pre>pcluster delete-cluster -n <cluster_name></pre> | AWS administrator |
| Delete the IAM policies. | Delete the policies that you created for the head node and compute node. For more information about deleting policies, see [Deleting IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-delete.html) in the IAM documentation. | AWS administrator |
| Delete the security group and rule. | Delete the security group that you created for the head node. For more information, see [Delete security group rules](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-security-groups.html#deleting-security-group-rules) and [Delete a security group](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-security-groups.html#deleting-security-groups) in the Amazon VPC documentation. | AWS administrator |
| Delete the S3 bucket. | Delete the S3 bucket that you created to store the configuration scripts. For more information, see [Deleting a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/delete-bucket.html) in the Amazon S3 documentation. | General AWS |

## Troubleshooting
<a name="set-up-a-grafana-monitoring-dashboard-for-aws-parallelcluster-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| The head node is not accessible in the browser. | Check  the security group and confirm that the inbound port 443 is open. |
| Grafana doesn't open. | On the head node, check the container log for `docker logs Grafana`. |
| Some metrics have no data. | On the head node, check the container logs of all containers. |

## Related resources
<a name="set-up-a-grafana-monitoring-dashboard-for-aws-parallelcluster-resources"></a>

**AWS documentation**
+ [IAM policies for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.html)

**Other AWS resources**
+ [AWS ParallelCluster](https://aws.amazon.com/hpc/parallelcluster/)
+ [Monitoring dashboard for AWS ParallelCluster](https://aws.amazon.com/blogs/compute/monitoring-dashboard-for-aws-parallelcluster/) (AWS blog post)

**Other resources**
+ [Prometheus monitoring system](https://prometheus.io/)
+ [Grafana](https://grafana.com/)
