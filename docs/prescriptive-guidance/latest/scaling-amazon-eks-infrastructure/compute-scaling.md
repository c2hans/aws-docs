---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/scaling-amazon-eks-infrastructure/compute-scaling.html
---

# Compute scaling
<a name="compute-scaling"></a>

Compute scaling is a critical component to application performance in a dynamic Kubernetes environment. Kubernetes reduces waste through the dynamic adjustment of computing resources (such as CPU and memory) in response to real-time demand. This capability helps to avoid over- or under-provisioning, which can also save operating expenses. Kubernetes effectively eliminates the need for manual intervention by enabling the infrastructure to automatically scale up during peak hours and down during off-peak periods.

The overall compute scaling of Kubernetes automates the scaling process, which boosts the application's flexibility and scalability and enhances its fault-tolerant behavior. Ultimately, the capabilities of Kubernetes enhance operational excellence and productivity.

This section discusses the following types of compute scaling:
+ [Cluster Autoscaler](#autoscaler)
+ [Cluster Autoscaler with over-provisioning](#over-provisioning)
+ [Karpenter](#karpenter)

## Cluster AutoScaler
<a name="autoscaler"></a>

Depending on the needs of the pods, the [Cluster Autoscaler](https://docs.aws.amazon.com/eks/latest/best-practices/cas.html) tool automatically modifies the size by adding nodes when necessary or removing nodes when they're not needed and are underutilized.

Consider the Cluster Autoscaler tool as a scaling solution for workloads where demand increases gradually and latency in scaling isn't a major issue.

The Cluster Autoscaler tool provides the following key features:
+ **Scaling** – Scales nodes up and down dynamically in response to actual resource demands.
+ **Pod scheduling** – Helps to make sure that every pod is operating and has the resources it needs to function, preventing the scarcity of resources.
+ **Cost-efficiency** – Eliminates the unnecessary expenses of operating under-utilized nodes by eliminating them.

## Cluster Autoscaler with over-provisioning
<a name="over-provisioning"></a>

Cluster Autoscaler with over-provisioning functions similarly to the Cluster Autoscaler in that it deploys nodes efficiently and saves time by running low-priority pods on the nodes. With this technique, traffic is redirected into these pods in response to sudden spikes in demand, allowing the application to continue operating without interruption.

Cluster Autoscaler with over-provisioning offers the features of dummy pods that can be used to easily deploy and run nodes when the workload is very large, latency isn't needed, and scaling needs to be quick.

Cluster Autoscaler with over-provisioning provides the following key features:
+ **Better responsiveness** – By making excess capacity constantly accessible, it takes less time to scale up the cluster in response to spikes in demand.
+ **Resource reservation** – Managing unexpected spikes in traffic effectively assists correct management with little downtime.
+ **Smooth scaling** – Minimizing resource allocation delays facilitates a more seamless scaling process.

## Karpenter
<a name="karpenter"></a>

[Karpenter](https://docs.aws.amazon.com/eks/latest/best-practices/karpenter.html) for Kubernetes outperforms the traditional Cluster Autoscaler tool in terms of open source, performance, and customizability. With Karpenter, you can automatically launch only the required compute resources to handle your cluster's demands in real time. Karpenter is designed to deliver more efficient and responsive scaling.

Applications with extremely variable or complex workloads, where quick scaling decisions are essential, benefit greatly from the use of Karpenter. It integrates with AWS, offering improved deployment and node selection optimization.

Karpenter includes the following key features:
+ **Dynamic provisioning** – Karpenter provides the right instances and sizes for the purpose and provisions new nodes dynamically based on the particular requirements of pods.
+ **Advanced scheduling** – Using clever pod placement, Karpenter arranges nodes such that resources like GPU, CPU, memory, and storage are used as effectively as possible.
+ **Quick scaling** – Karpenter can scale quickly, frequently reacting in seconds. This responsiveness is helpful for patterns of sudden traffic or when the workload demands immediate scaling
+ **Cost efficiency** – By carefully choosing the most effective instance, you can lower operating costs and take advantage of additional cost-saving alternatives offered by AWS, such as On-Demand Instances, Spot Instances, and Reserved Instances.
