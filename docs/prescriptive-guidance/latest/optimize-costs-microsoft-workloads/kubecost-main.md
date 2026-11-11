---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/kubecost-main.html
---

# Gain visibility into your Amazon EKS costs
<a name="kubecost-main"></a>

## Overview
<a name="kubecost-overview"></a>

To monitor the cost of a Kubernetes deployment effectively, you need a holistic view. The only fixed and known cost is for the [Amazon Elastic Kubernetes Service (Amazon EKS)](https://docs.aws.amazon.com/eks/latest/userguide/) control plane. Every other component that makes up the deployment, from compute and storage to networking, has a variable cost based on your application needs.

You can use [Kubecost](https://www.kubecost.com/) to analyze the cost of your Kubernetes infrastructure, from [Namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) and [Services](https://kubernetes.io/docs/concepts/services-networking/service/) to individual [Pods](https://kubernetes.io/docs/concepts/workloads/pods/), and then display the data in a dashboard. Kubecost surfaces in-cluster costs like compute and storage and out-of-cluster costs like [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) buckets and [Amazon Relational Database Service (Amazon RDS)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) instances. Kubecost provides right-sizing recommendations based on this data and displays critical alerts that might affect the system. Kubecost can [integrate](https://www.ibm.com/docs/en/kubecost/self-hosted/3.x?topic=integrations-aws-cloud-billing-integration) with [AWS Cost and Usage Report](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html) to show savings from [Compute Savings Plans](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html), [Amazon EC2 Reserved Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-reserved-instances.html), and other discount programs.

## Cost benefits
<a name="kubecost-cost-benefits"></a>

Kubecost provides reports and dashboards that visualize the cost of your Amazon EKS deployments. It enables you to drill down from the cluster into each of the various components such as the controllers, services, nodes, pods, and volumes. This gives you a comprehensive view of your applications running in an Amazon EKS environment. By enabling this visibility, you can act on the Kubecost recommendations or view the costs of each application at a granular level. Rightsizing an Amazon EKS node group offers the same potential savings as rightsizing standard EC2 instances. If you rightsize your containers and nodes, you can reduce the instance size needed to run the container and the number of EC2 instances required in the Amazon EC2 Auto Scaling group.

## Cost optimization recommendations
<a name="kubecost-rec"></a>

To take advantage of Kubecost, we recommend that you do the following:

1. Deploy Kubecost into your environment

1. Get a granular cost breakdown of Windows applications

1. Right size cluster nodes

1. Right size container requests

1. Manage underutilized nodes

1. Remedy abandoned workloads

1. Act on recommendations

1. Update self-managed nodes

### Deploy Kubecost into your environment
<a name="deploy-kubecost-into-your-environment.1924e821-0599-53e2-b00d-e8ac99202b40"></a>

The [Amazon EKS Finhack Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/c4ab40ed-0299-4a4e-8987-35d90ba5085e/en-US) teaches you how to deploy an Amazon EKS environment that's configured to use Kubecost in an AWS owned account. This allows you to get hands-on experience with the technology. If you're interested in running this workshop in your organization, contact your account team.

To deploy Kubecost to your Amazon EKS cluster using [Helm](https://helm.sh/), see the [AWS and Kubecost collaborate to deliver cost monitoring for EKS customers](https://aws.amazon.com/blogs/containers/aws-and-kubecost-collaborate-to-deliver-cost-monitoring-for-eks-customers/) post on the AWS Blog. Alternatively, you can refer to the [official Kubecost documentation](https://www.ibm.com/docs/en/kubecost/self-hosted/3.x?topic=installation) for instructions on installing and configuring Kubecost. For information about Kubecost support for Windows nodes, see [Windows Node Support](https://www.ibm.com/docs/en/kubecost/self-hosted/3.x?topic=configuration-windows-node-support) in the Kubecost documentation.

### Get a granular cost breakdown of Windows applications
<a name="get-a-granular-cost-breakdown-of-windows-applications.2cf18feb-9330-5df8-8793-b03de12e6999"></a>

Although you can achieve significant cost savings by using [Amazon EC2 Spot Instances](https://aws.amazon.com/ec2/spot/), you can also benefit from the fact that Windows workloads tend to be stateful. The use of Spot Instances depends on your application, so verify whether they're applicable for your use case.

To get a granular cost breakdown of your Windows applications, [log in to Kubecost](https://auth.app.kubecost.com/login). In the navigation pane, choose **Savings**.

### Right size cluster nodes
<a name="right-size-cluster-nodes.f35994e1-ce9e-5d3a-a7d0-7f2816bc5700"></a>

In [Kubecost](https://auth.app.kubecost.com/login), choose **Savings** from the navigation bar, and then choose **Right-size your cluster node**.

Consider an example where Kubecost reports that the cluster is over-provisioned both in terms of vCPU and RAM. The following table shows the details and recommendations from Kubecost.

|  |
| --- |
|   | Current | Recommendation: Simple | Recommendation: Complex |
| --- |--- |--- |--- |
| **Total count** | US $3462.57 per month | US $137.24 per month | US $303.68 per month |
| **Node count** | 4 | 5 | 4 |
| **CPU** | 74 vCPUs | 10 vCPUs | 8 vCPUs |
| **RAM** | 152 GB | 20 GB | 18 GB |
| **Instance breakdown** | 2 c5.xlarge \+ 2 more | 5 t3a.medium | 2 c5n.large \+ 1 more |

As described in the Kubecost blog post [Find an optimal set of nodes for a Kubernetes cluster](https://blog.kubecost.com/blog/cluster-right-sizing/), the simple option uses a single node group, whereas the complex option uses multiple node groups. You can use the **Learn how to adopt** button to perform one-click cluster resizing. This requires that you install the [Kubecost Cluster Controller](https://www.ibm.com/docs/en/kubecost/self-hosted/3.x?topic=configuration-cluster-controller).

If you're using [self-managed Windows nodes](https://docs.aws.amazon.com/eks/latest/userguide/launch-windows-workers.html) that aren't created by [eksctl](https://eksctl.io/), see [Updating an existing self-managed node group](https://docs.aws.amazon.com/eks/latest/userguide/update-stack.html). These instructions show you how to change the instance type in the Amazon EC2 launch template used by the [Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-groups.html).

### Right size container requests
<a name="right-size-container-requests.495aaff2-2fdf-5501-b22e-c63a0a4db3b4"></a>

In [Kubecost](https://auth.app.kubecost.com/login), choose **Savings** from the navigation bar, and then go to the **Request right-sizing recommendations **page. This page shows the [efficiency](https://www.ibm.com/docs/en/kubecost/self-hosted/2.x?topic=dashboard-efficiency-idle) of the pods, right-sizing recommendations, and estimated cost savings. You can use the **Customize** button to filter by **Cluster**, **Node**, **Namespace\\Controller**, and more.

As an example, consider that Kubecost has calculated that some of your pods are overprovisioned in terms of CPU and RAM (memory). Then, Kubecost recommends that you adjust to new CPU and RAM values to achieve its estimated monthly savings. To change the CPU and RAM values, you must update your [deployment manifest](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) file.

### Manage underutilized nodes
<a name="manage-underutilized-nodes.82f8ce0c-ebff-5af6-83e4-3bdd9a4b9cb7"></a>

In [Kubecost](https://auth.app.kubecost.com/login), choose **Savings** from the navigation bar, and then choose **Manage underutilized nodes**.

Consider an example where the page shows that one node in the cluster is underutilized in terms of CPU and RAM (memory) and can therefore be drained and either stopped or resized. To see why a node can't be drained, choose the nodes that don't pass the node and pod checks.

### Remedy abandoned workloads
<a name="remedy-abandoned-workloads.bc710540-a74a-5273-b081-4ee97de9b82e"></a>

In [Kubecost](https://auth.app.kubecost.com/login), choose **Savings** from the navigation bar, and then choose the **Abandoned Workloads** page. In this example, you filter by a namespace called **windows**. This page shows the pods that haven't met the traffic threshold and that Kubecost considers abandoned. To avoid being considered abandoned, pods must send or receive a minimum amount of network traffic over the defined period.

If you determine that one or more pods are abandoned, you can reduce costs by scaling down the number of replicas, deleting the deployment, resizing it to consume fewer resources, or notifying the application owner that the deployment appears to be abandoned.

### Act on recommendations
<a name="act-on-recommendations.754aa10b-643d-5617-b9dc-8c0b9306a56c"></a>

In the **Right-size your cluster nodes** section, Kubecost analyzes the usage of the worker nodes in the cluster, and makes recommendations about right sizing the nodes to reduce cost. There are two types of node groups that can be used with Amazon EKS: [self-managed](https://docs.aws.amazon.com/eks/latest/userguide/worker.html) and [managed](https://docs.aws.amazon.com/eks/latest/userguide/managed-node-groups.html).

### Update self-managed nodes
<a name="update-self-managed-nodes.4902c066-feb1-50ce-bb3c-b37d2201c851"></a>

For information about updating self-managed nodes, see [Self-managed node updates](https://docs.aws.amazon.com/eks/latest/userguide/update-workers.html) in the Amazon EKS documentation. It states that node groups created with `eksctl` can't be updated and must be migrated to a new node group with the new configuration.

As an example, assume that you have a Windows node group called `ng-windows-m5-2xlarge`** **(which uses an m5.2xlarge EC2 instance) and you want to migrate the pods to a [new node group](https://docs.aws.amazon.com/eks/latest/userguide/launch-windows-workers.html) called `ng-windows-t3-large`** **(which is backed by a t3.large EC2 instance to save cost).

To migrate to a new node group when you use node groups deployed by `eksctl`, do the following:

1. To find the node that the pod is currently running on, run the `kubectl describe pod <pod_name> -n <namespace>` command.

1. Run the `kubectl describe node <node_name>` command. The output shows that the node is running on an m5.2xlarge instance, which matches the node group name (`ng-windows-m5-2xlarge`).

1. To change the deployment to use node group `ng-windows-t3-large`, delete node group `ng-windows-m5-2xlarge` and run `kubectl describe svc,deploy,pod -n windows`. The deployment immediately starts to redeploy now that its node group has been deleted.

<table>
<tbody>
</tbody>
</table>

1. Run the `kubectl describe svc,deploy,pod -n windows` command again after a few minutes. The output shows that the pods are all in a **Running** state again.

1. To show that the pods are now running on node group `ng-windows-t3-large`, run the `kubectl describe pod <pod_name> -n <namespace>` and `kubectl describe node <node_name>` commands again.

### Alternative resizing methods
<a name="alternative-resizing-methods.87d382be-06f7-5cd4-aadc-d2f138cd8bce"></a>

This method applies to any combination of self-managed or managed node groups. The [Seamlessly migrate workloads from EKS self-managed node group to EKS-managed node groups](https://aws.amazon.com/blogs/containers/seamlessly-migrate-workloads-from-eks-self-managed-node-group-to-eks-managed-node-groups/) blog post provides guidance on how to migrate your workloads from a node group with an oversized instance type to a right-sized node group while minimizing downtime.

## Next steps
<a name="kubecost-next-steps"></a>

Kubecost helps you visualize the cost of your [Amazon Elastic Kubernetes Service (Amazon EKS)](https://docs.aws.amazon.com/eks/latest/userguide/) environments. The deep integration of Kubecost with Kubernetes and the AWS APIs can help you find potential cost savings. You can see these as recommendations in the **Savings** dashboard of Kubecost. Kubecost can also implement some of these recommendations for you through its [cluster controller feature](https://github.com/kubecost/cluster-turndown).

We recommend that you review the step-by-step deployment in the [AWS and Kubecost collaborate to deliver cost monitoring for EKS customers](https://aws.amazon.com/blogs/containers/aws-and-kubecost-collaborate-to-deliver-cost-monitoring-for-eks-customers/) blog post from the AWS Containers blog.

## Additional resources
<a name="kubecost-additional-resources"></a>
+ [Amazon EKS Workshop](https://www.eksworkshop.com/) (Amazon EKS Workshop)
+ [AWS and Kubecost collaborate to deliver cost monitoring for EKS customers](https://aws.amazon.com/blogs/containers/aws-and-kubecost-collaborate-to-deliver-cost-monitoring-for-eks-customers/) (AWS Blog)
+ [Amazon EKS Finhack Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/c4ab40ed-0299-4a4e-8987-35d90ba5085e/en-US) (AWS Workshop Studio)
+ [Windows Containers on AWS](https://catalog.us-east-1.prod.workshops.aws/workshops/1de8014a-d598-4cb5-a119-801576492564/en-US) (AWS Workshop Studio)
