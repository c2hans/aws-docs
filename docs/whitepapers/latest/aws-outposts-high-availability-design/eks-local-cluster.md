---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/eks-local-cluster.html
---

# EKS Local Cluster on Outposts
<a name="eks-local-cluster"></a>

When there are disconnections of Outposts service link from the parent region, there might be challenges with services as EKS Extended Cluster, where the control plane lives in the region. Among the challenges is the loss of communication between the EKS control plane and the worker nodes and PODs. Although both worker nodes and PODs can continue to operate and service applications that resides on Outposts locally, the Kubernetes control plane may consider them unhealthy and schedule their replacement when the connection to the control plane recovers. This may lead to application downtimes when connectivity is restored.

To simplify this, there is an option to host your entire EKS cluster on Outposts. In this configuration, both the Kubernetes control plane and your worker nodes run locally on premises on your Outposts compute capacity. That way, your cluster continues to operate even in the event of a temporary drop in your service link connection and after it is restored.

![Amazon EKS local cluster on Outposts](https://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/images/page-52-eks-local-cluster-outposts.png)

## Amazon EKS Local Cluster on Outposts considerations
<a name="eks-local-cluster-considerations"></a>

Consider the following when you deploy an Amazon EKS local cluster in Outposts:
+ During a disconnection there are not options to execute any change in the cluster itself that requires to add new worker nodes, or auto-scale a node group, as long as it depends on EC2 and ASG API calls toward the AWS parent Region.
+ There are a set of unsupported features on local clusters listed on [eksctl AWS Outposts support.](https://eksctl.io/usage/outposts/).
