---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/log-sources.html
---

# Log sources
<a name="log-sources"></a>

You must create a log source first before collecting application logs. Centralized Logging with OpenSearch supports the following log sources:
+  [Instance group](#instance-group-1)
+  [Amazon EKS cluster](#amazon-eks-cluster-1)
+  [Amazon S3](#amazon-s3-1)
+  [Syslog](#syslog-1)

For more information, see [concepts](solution-overview.md#concepts).

## Instance Group
<a name="instance-group-1"></a>

An instance group represents a group of EC2 Linux instances, which enables the solution to associate a [Log Config](instance-group.md) with multiple EC2 instances quickly. Centralized Logging with OpenSearch uses [Systems Manager Agent(SSM Agent)](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent.html) to install/configure Fluent Bit agent, and sends log data to [Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/).

 **Prerequisites**

Make sure that the instances meet the following requirements:
+ SSM agent is installed on instances. Refer to [install SSM agent on EC2 instances for Linux](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-manual-agent-install.html) for more details.
+ The AmazonSSMManagedInstanceCore policy is being associated with the instances.
+ The [OpenSSL 1.1](https://www.openssl.org/source/) or later is installed. Refer to [OpenSSL Installation](additional-resources.md#openssl-1.1-installation) for more details.
+ The instances have network access to AWS Systems Manager.
+ The instances have network access to Amazon Kinesis Data Streams, if you use it as the Log Buffer.
+ The instances have network access to Amazon S3, if you use it as the Log Buffer.
+ The operating system of the instances is supported by Fluent Bit. Refer to [Supported Platform](https://docs.fluentbit.io/manual/installation/supported-platforms).

### (Option 1) Select instances to create an Instance Group
<a name="option-1-select-instances-to-create-an-instance-group"></a>

1. Sign in to the Centralized Logging with OpenSearch Console.

1. In the left sidebar, under **Log Source**, choose **Instance Group**.

1. Choose the **Create an instance group** button.

1. In the **Settings** section, specify a group name.

1. In the **Configuration** section, select **Instances**. You can use up to 5 tags to filter the instances.

1. Verify that all the selected instances' "Pending Status" is **Online**.

1. (Optional) If the selected instances' "Pending Status" are empty, choose the **Install log agent** button, and wait for "Pending Status" to become **Online**.

1. (Optional) If you want to ingest logs from another account, select a [linked account](cross-account-ingestion.md) in the **Account Settings** section to create an instance group log source from another account.

1. Choose **Create**.

**Important**
Important Use the Centralized Logging with OpenSearch console to install Fluent Bit agent on Ubuntu instances in **Beijing (cn-north-1) and Ningxia (cn-northwest-1)** Region will cause installation error. The Fluent Bit assets cannot be downloaded successfully. You must install the Fluent Bit agent by yourself.

### (Option 2) Select an Auto Scaling group to create an Instance Group
<a name="option-2-select-an-auto-scaling-group-to-create-an-instance-group"></a>

When creating an Instance Group with Amazon EC2 Auto Scaling group, the solution will generate a shell script that you should include in the [EC2 User Data](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html#user-data-shell-scripts).

1. Sign in to the Centralized Logging with OpenSearch Console.

1. In the left sidebar, under **Log Source**, choose **Instance Group**.

1. Choose the **Create an instance group** button.

1. In the **Settings** section, specify a group name.

1. In the Configuration section, select Auto Scaling Groups.

1. In the **Auto Scaling groups** section, select the Auto Scaling group from which you want to collect logs.

1. (Optional) If you want to ingest logs from another account, select a [linked account](cross-account-ingestion.md) in the **Account Settings** section to create an instance group log source from another account.

1. Choose **Create**. After you created a Log Ingestion using the Instance Group, you can find the generated Shell Script in the details page.

1. Copy the shell script and update the User Data of the Auto Scaling Group’s [launch configurations](https://docs.aws.amazon.com/autoscaling/ec2/userguide/launch-configurations.html) or [launch template](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html). The shell script will automatically install Fluent Bit, SSM agent if needed, and download Fluent Bit configurations.

1. Once you have updated the launch configurations or launch template, you must start an [instance refresh](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-instance-refresh.html) to update the instances within the Auto Scaling group. The newly launched instances will ingest logs to the OpenSearch cluster or the Log Buffer layer.

## Amazon EKS Cluster
<a name="amazon-eks-cluster-1"></a>

The [EKS Cluster](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html) in Centralized Logging with OpenSearch refers to the Amazon Elastic Kubernetes Service (Amazon EKS) from which you want to collect pod logs. Centralized Logging with OpenSearch will guide you to deploy the log agent as a [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/) or [Sidecar](https://kubernetes.io/docs/concepts/workloads/pods/#workload-resources-for-managing-pods) in the EKS Cluster.

**Important**
Centralized Logging with OpenSearch does not support sending logs in one EKS cluster to more than one Amazon OpenSearch Service domain at the same time.
Make sure your EKS cluster’s VPC is connected to the Amazon OpenSearch Service cluster’s VPC so that logs can be ingested. Refer to [VPC Connectivity](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/vpc-to-vpc-connectivity.html) for more details regarding approaches to connect VPCs.

1. Sign in to the Centralized Logging with OpenSearch Console.

1. In the left sidebar, under **Log Source**, choose **EKS Cluster**.

1. Choose the **Import a Cluster** button.

1. Choose the **EKS Cluster** where Centralized Logging with OpenSearch collects logs from. (Optional) If you want to ingest logs from another account, select a [linked account](cross-account-ingestion.md) from the **Account** dropdown to import an EKS log source from another account.

1. Select **DaemonSet** or **Sidecar** as the log agent’s deployment pattern.

1. Choose **Next**.

1. Specify the **Amazon OpenSearch Service** where Centralized Logging with OpenSearch sends the logs to.

1. Follow the guidance to establish a VPC peering connection between EKS’s VPC and OpenSearch’s VPC.
   +  [Create and accept VPC peering connections](https://docs.aws.amazon.com/vpc/latest/peering/create-vpc-peering-connection.html)
   +  [Update your route tables for a VPC peering connection](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-routing.html)
   +  [Update your security groups to reference peer VPC groups](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-security-groups.html)

1. Choose **Next**.

1. Add tags if needed.

1. Choose **Create**.

## Amazon S3
<a name="amazon-s3-1"></a>

The [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) in Centralized Logging with OpenSearch refers to the Amazon S3 from which you want to collect application logs stored in your bucket. You can choose **On-going** or **One-time** to create your ingestion job.

**Important**
On-going means that the ingestion job will run when a new file is delivered to the specified Amazon S3 location.
One-time means that the ingestion job will run at creation and will only run once to load all files in the specified location.

## Syslog
<a name="syslog-1"></a>

**Important**
Important To ingest logs, make sure your Syslog generator/sender’s subnet is connected to Centralized Logging with OpenSearch’s **two** private subnets. Refer to [VPC Connectivity](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/vpc-to-vpc-connectivity.html) for more details about how to connect VPCs.

You can use a UDP or TCP custom port number to collect syslog in Centralized Logging with OpenSearch. Syslog refers to logs generated by Linux instance, routers, or network equipment. For more information, see [Syslog](https://en.wikipedia.org/wiki/Syslog) in Wikipedia.

## Add a new log source
<a name="add-a-new-log-source"></a>

A newly created log analytics pipeline has one log source. You can add more log sources into the log pipeline.

1. Sign in to the Centralized Logging with OpenSearch Console.

1. In the left navigation pane, under Log Analytics Pipelines, choose Application Log.

1. Choose the log pipeline’s ID.

1. Choose Create a source.

1. Follow the instructions in [Instance Group](#instance-group-1), [Amazon EKS cluster](#amazon-eks-cluster-1), [Amazon S3](#amazon-s3-1), or [Syslog](#syslog-1) to create a log source according to your need.
