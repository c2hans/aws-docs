---
source_url: https://docs.aws.amazon.com/whitepapers/latest/overview-deployment-options/amazon-elastic-kubernetes-service.html
---

# Amazon Elastic Kubernetes Service
<a name="amazon-elastic-kubernetes-service"></a>

 [Amazon Elastic Kubernetes Service](https://aws.amazon.com/eks/) (Amazon EKS) is a fully-managed, certified [Kubernetes](https://kubernetes.io/) conformant service that simplifies the process of building, securing, operating, and maintaining Kubernetes clusters on AWS. Amazon EKS integrates with core AWS services such as CloudWatch, Auto Scaling Groups, and IAM to provide a seamless experience for monitoring, scaling, and load balancing your containerized applications.

 Amazon EKS provides a scalable, highly-available control plane for Kubernetes workloads. When you run applications on Amazon EKS, as with Amazon ECS, you can choose to provide the underlying compute power for your containers with Amazon EC2 instances or with AWS Fargate.

 Amazon VPC Lattice is a fully managed application networking service built directly into the AWS networking infrastructure that you can use to connect, secure, and monitor your services across multiple accounts and virtual private clouds (VPCs). With Amazon EKS, you can leverage VPC Lattice through the use of the AWS Gateway API Controller, an implementation of the Kubernetes Gateway API. Using VPC Lattice, you can set up cross-cluster connectivity with standard Kubernetes semantics in a simple and consistent manner.

 You can use Amazon EKS with any of the following deployment options:
+  [https://aws.amazon.com/eks/eks-distro/](https://aws.amazon.com/eks/eks-distro/) – Amazon EKS Distro is a distribution of the same open-source Kubernetes software and dependencies deployed by Amazon EKS in the cloud. Amazon EKS Distro follows the same Kubernetes version release cycle as Amazon EKS and is provided as an open-source project. To learn more, see [Amazon EKS Distro](https://distro.eks.amazonaws.com/).
+  []() – AWS Outposts enables native AWS services, infrastructure, and operating models in your on-premises facilities. Amazon EKS on AWS Outposts, you can choose to run extended or local clusters. With extended clusters, the Kubernetes control plane runs in an AWS Region and the nodes run on AWS Outposts. With local clusters, the entire Kubernetes cluster runs locally on AWS Outposts, including both the Kubernetes control plane and nodes.
+  [https://aws.amazon.com/eks/eks-anywhere/](https://aws.amazon.com/eks/eks-anywhere/) – Amazon EKS Anywhere is a deployment option for Amazon EKS that enables you to easily create and operate Kubernetes clusters on-premises. Both Amazon EKS and Amazon EKS Anywhere are built on the Amazon EKS Distro. To learn more about Amazon EKS Anywhere, see [Running Hybrid Container workloads with Amazon EKS Anywhere](https://d1.awsstatic.com/kubernetes-pmm/eks-a/getting-started/AWS_Whitepaper_Running_Hybrid_Container_Workloads_with_Amazon_EKS_Anywhere.pdf), [Amazon EKS Anywhere Overview](https://anywhere.eks.amazonaws.com/docs/overview/), and [Comparing Amazon EKS Anywhere to Amazon EKS](https://anywhere.eks.amazonaws.com/docs/concepts/eksafeatures/#comparing-amazon-eks-anywhere-to-amazon-eks).

 When choosing which deployment options to use for your Kubernetes cluster, consider the following:

*Table 5: Kubernetes deployment features*

|  Feature  |  Amazon EKS  |  Amazon EKS on AWS Outposts  |  Amazon EKS Anywhere  |  Amazon EKS Distro  |
| --- | --- | --- | --- | --- |
|  Hardware  |  AWS-supplied  |  AWS-supplied  |  Supplied by you  |  Supplied by you  |
|  Deployment location  |  AWS Cloud  |  Your data center  |  Your data center  |  Your data center  |
|  Kubernetes control plane location  |  AWS Cloud  |  AWS Cloud or your data center  |  Your data center  |  Your data center  |
|  Kubernetes data plane location  |  AWS Cloud  |  Your data center  |  Your data center  |  Your data center  |
|  Support  |  AWS support  |  AWS support  |  AWS support  |  OSS community support  |

* Table 6: Amazon EKS deployment features *

|  Capability  |  Description  |
| --- | --- |
|  Provision  |  Amazon EKS provisions certain resources to support containerized applications: +   Load Balancers, if needed  <br />+   Compute resources, or *workers* (Amazon EKS supports Windows and Linux)  <br />+   Application Container Instances, or *pods*  <br /> Refer to [Getting Started with Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/getting-started-console.html) for more details on Amazon EKS cluster provisioning.  |
|  Configure  |  Amazon EKS supports customization of the compute resources (workers) if you use Amazon EC2 instances to supply compute power. Amazon EKS also supports customization of the runtime conditions of the application containers (pods). <br /> Refer to [Worker Nodes](https://docs.aws.amazon.com/eks/latest/userguide/worker.html) and [Fargate Pod Configuration](https://docs.aws.amazon.com/eks/latest/userguide/fargate-pod-configuration.html) documentation for more details.  |
|  Deploy  |  Amazon EKS supports the same deployment strategies as Kubernetes. See [Writing a Kubernetes Deployment Spec -> Strategy](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#strategy) for more details.  |
|  Scale  |  Amazon EKS scales workers with [Kubernetes Cluster Autoscaler](https://docs.aws.amazon.com/eks/latest/userguide/cluster-autoscaler.html), and pods with Kubernetes Horizontal Pod Autoscaler and Kubernetes Vertical Pod Autoscaler. Amazon EKS also supports [Karpenter](https://karpenter.sh/), an open source, flexible, high-performance Kubernetes cluster autoscaler to help improve your application availability and cluster efficiency by rapidly launching right-sized compute resources in response to changing application load.  |
|  Monitor  |  The Amazon EKS control plane logs provide audit and diagnostic information directly to CloudWatch Logs. The Amazon EKS control plane also integrates with AWS CloudTrail to record actions taken in Amazon EKS. <br /> Refer to [Logging and Monitoring Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/logging-monitoring.html) for more details.  |

 Amazon EKS allows organizations to leverage open source Kubernetes tools and plugins, and can be a good choice for organizations migrating to AWS with existing Kubernetes environments. The following diagram illustrates Amazon EKS being used to manage a general containerized application.

![EKS control plane managing pods across three availability zones using different node group types.](http://docs.aws.amazon.com/whitepapers/latest/overview-deployment-options/images/image6.png)

## Amazon EKS Anywhere
<a name="eks-anywhere"></a>

 [Amazon EKS Anywhere](https://aws.amazon.com/eks/eks-anywhere/) lets you create and operate Kubernetes clusters on your own infrastructure. Amazon EKS Anywhere builds on the strengths of Amazon EKS Distro and provides open-source software that’s up to date and patched so you can have an on-premises Kubernetes environment that’s more reliable than a self-managed Kubernetes offering.

 Amazon EKS Anywhere creates a Kubernetes cluster on-premises to a chosen provider. Supported providers include Bare Metal (via Tinkerbell), CloudStack, and vSphere. To manage that cluster, you can run cluster create and delete commands from an Ubuntu or Mac Administrative machine.
