---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/logging-for-amazon-eks.html
---

# Logging for Amazon EKS
<a name="logging-for-amazon-eks"></a>

Kubernetes logging can be divided into control plane logging, node logging, and application logging. The [Kubernetes control plane](https://kubernetes.io/docs/concepts/overview/components/#control-plane-components) is a set of components that manage Kubernetes clusters and produce logs used for auditing and diagnostic purposes. With Amazon EKS, you can [turn on logs for different control plane components](https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html) and send them to CloudWatch.

Kubernetes also runs system components such as kubelet and kube-proxy on each Kubernetes node that runs your pods. These components write logs within each node and you can configure CloudWatch and Container Insights to capture these logs for each Amazon EKS node.

Containers are grouped as [pods](https://kubernetes.io/docs/concepts/workloads/pods/) within a Kubernetes cluster and are scheduled to run on your Kubernetes nodes. Most containerized applications write to standard output and standard error, and the container engine redirects the output to a logging driver. In Kubernetes, the container logs are found in the /var/ log/pods directory on a node. You can configure CloudWatch and Container Insights to capture these logs for each of your Amazon EKS pods.

## Amazon EKS control plane logging
<a name="amazon-eks-control-plane-logging"></a>

An Amazon EKS cluster consists of a high availability, single-tenant control plane for your Kubernetes cluster and the Amazon EKS nodes that run your containers. The control plane nodes run in an account managed by AWS. The Amazon EKS cluster control plane nodes are integrated with CloudWatch and you can turn on logging for specific control plane components.

Logs are provided for each Kubernetes control plane component instance. AWS manages the health of your control plane nodes and provides a [service-level agreement (SLA) for the Kubernetes endpoint](https://aws.amazon.com/eks/sla/).

## Amazon EKS node and application logging
<a name="amazon-eks-node-and-application-logging"></a>

We recommend that you use [CloudWatch Container Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-setup-logs.html) to capture logs and metrics for Amazon EKS. Container Insights implements cluster, node, and pod-level metrics with the CloudWatch agent, and Fluent Bit or Fluentd for log capture to CloudWatch. Container Insights also provides automatic dashboards with layered views of your captured CloudWatch metrics. Container Insights is deployed as CloudWatch DaemonSet and Fluent Bit DaemonSet that runs on every Amazon EKS node. Fargate nodes are not supported by Container Insights because the nodes are managed by AWS and don't support DaemonSets. Fargate logging for Amazon EKS is covered separately in this guide.

The following table shows the CloudWatch log groups and logs captured by the [default Fluentd or Fluent Bit log capture configuration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-setup-logs-FluentBit.html) for Amazon EKS.

|  |  |
| --- |--- |
| /aws/containerinsights/Cluster\_Name/<br />application | All log files in /var/log/containers. This directory provides symbolic links to all the Kubernetes container logs in the /var/ log/pods directory structure. This captures your application container logs writing to stdout or stderr. It also includes logs<br />for Kubernetes system containers such as aws-vpc-cni-init, kube-proxy, and coreDNS. |
| /aws/containerinsights/Cluster\_Name/host | Logs from /var/log/dmesg, /var/log/ secure, and /var/log/messages. |
| /aws/containerinsights/Cluster\_Name/<br />dataplane | The logs in /var/log/journal for kubelet.service, kubeproxy.service, and docker.service. |

If you don't want to use Container Insights with Fluent Bit or Fluentd for logging, you can capture node and container logs with the CloudWatch agent installed on Amazon EKS nodes. Amazon EKS nodes are EC2 instances, which means you should include them in your standard system-level logging approach for Amazon EC2. If you install the CloudWatch agent using Distributor and State Manager, then Amazon EKS nodes are also included in the CloudWatch agent installation, configuration, and update.

The following table shows logs that are specific to Kubernetes and that you must capture if you aren't using Container Insights with Fluent Bit or Fluentd for logging.

|  |
| --- |
| /var/log/containers | This directory provides symbolic links to all the Kubernetes container logs under the /var/log/ pods directory structure. This effectively captures your application container logs writing to stdout or stderr. This includes logs for Kubernetes system containers such as aws-vpc-cni-init, kube-proxy, and coreDNS. Important: This is not required if you are using Container Insights. |
| --- |--- |
| var/log/aws-routed-eni/ipamd.log /var/log/aws-routed-eni/plugin.log | The logs for the L-IPAM daemon can be found here |

You must make sure that Amazon EKS nodes install and configure the CloudWatch agent to send appropriate system-level logs and metrics. However, the Amazon EKS optimized AMI doesn't include the Systems Manager agent. By using [launch templates](https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html), you can automate the Systems Manager agent installation and a default CloudWatch configuration that captures important Amazon EKS specific logs with a startup script implemented through the user data section. Amazon EKS nodes are deployed using an Auto Scaling group as either a [managed node group](https://docs.aws.amazon.com/eks/latest/userguide/managed-node-groups.html) or as [self-managed nodes](https://docs.aws.amazon.com/eks/latest/userguide/worker.html).

With managed node groups, you supply a [launch template](https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html) that includes the user data section to automate the Systems Manager agent installation and CloudWatch configuration. You can customize and use the [amazon\_eks\_managed\_node\_group\_launch\_config.yaml](https://github.com/aws-samples/logging-monitoring-apg-guide-examples/blob/main/examples/eks/amazon_eks_managed_node_group_launch_config.yaml) AWS CloudFormation template to create a launch template that installs the Systems Manager agent, CloudWatch agent, and also adds an Amazon EKS specific logging configuration to the CloudWatch configuration directory. This template can be used to update your Amazon EKS managed node groups launch template with an infrastructureas-code (IaC) approach. Each update to the AWS CloudFormation template provisions a new version of the launch template. You can then update the node group to use the new template version and have the [managed lifecycle process](https://docs.aws.amazon.com/eks/latest/userguide/managed-node-update-behavior.html) update your nodes without downtime. Make sure that the IAM role and instance profile applied to your managed node group includes the CloudWatchAgentServerPolicy and AmazonSSMManagedInstanceCore AWS managed policies.

With self-managed nodes, you directly provision and manage the lifecycle and update strategy for your Amazon EKS nodes. Self-managed nodes allow you to run Windows nodes on your Amazon EKS cluster and [Bottlerocket](https://aws.amazon.com/bottlerocket/), along with [other options](https://docs.aws.amazon.com/eks/latest/userguide/eks-compute.html). You can use AWS CloudFormation to deploy self-managed nodes into your Amazon EKS clusters, which means you can use an IaC and managed change approach for your Amazon EKS clusters. AWS provides the [amazon-eks-nodegroup.yaml](https://github.com/aws-samples/logging-monitoring-apg-guide-examples/blob/main/examples/eks/amazon-eks-nodegroup.yaml) AWS CloudFormation template that you can use as-is or customize. The template provisions all required resources for Amazon EKS nodes in a cluster (for example, a separate IAM role, security group, Amazon EC2 Auto Scaling group, and a launch template). The [amazon-eks-nodegroup.yaml](https://github.com/aws-samples/logging-monitoring-apg-guide-examples/blob/main/examples/eks/amazon-eks-nodegroup.yaml) AWS CloudFormation template is an updated version that installs the required Systems Manager agent, CloudWatch agent, and also adds an Amazon EKS specific logging configuration to the CloudWatch configuration directory.

## Logging for Amazon EKS on Fargate
<a name="logging-for-amazon-eks-on-fargate"></a>

With Amazon EKS on Fargate, you can deploy pods without allocating or managing your Kubernetes nodes. This removes the need to capture system-level logs for your Kubernetes nodes. To capture the logs from your Fargate pods, you can use Fluent Bit to forward the logs directly to CloudWatch. This enables you to automatically route logs to CloudWatch without further configuration or a sidecar container for your Amazon EKS pods on Fargate. For more information about this, see [Fargate logging](https://docs.aws.amazon.com/eks/latest/userguide/fargate-logging.html) in the Amazon EKS documentation and [Fluent Bit for Amazon EKS](https://aws.amazon.com/blogs/containers/fluent-bit-for-amazon-eks-on-aws-fargate-is-here/) on the AWS Blog. This solution captures the STDOUT and STDERR input/output (I/O) streams from your container and sends them to CloudWatch through Fluent Bit, based on the Fluent Bit configuration established for the Amazon EKS cluster on Fargate.
