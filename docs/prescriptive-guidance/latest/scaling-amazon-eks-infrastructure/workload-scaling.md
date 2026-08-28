---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/scaling-amazon-eks-infrastructure/workload-scaling.html
---

# Workload scaling
<a name="workload-scaling"></a>

Workload scaling in Kubernetes is essential for maintaining application performance and resource efficiency in dynamic environments. Scaling helps to make sure that applications can handle varying workloads without performance degradation. Kubernetes provides the ability to automatically scale resources up or down based on real-time metrics, allowing organizations to respond quickly to changes in traffic. This elasticity not only improves user experience but also optimizes resource utilization, helping to minimize costs associated with underused or overprovisioned resources.

Additionally, effective workload scaling supports high availability, ensuring that applications remain responsive even during peak demand periods. Workload scaling in Kubernetes enables organizations to make better use of cloud resources by dynamically adjusting capacity to meet current needs.

This section discusses the following types of workload scaling:
+ [Horizontal Pod Autoscaler](#hpa)
+ [Cluster Proportional Autoscaler](#cpa)
+ [Kubernetes-based Event Driven Autoscaler](#keda)

## Horizontal Pod Autoscaler
<a name="hpa"></a>

The [Horizontal Pod Autoscaler](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/) (HPA) is a Kubernetes feature that automatically adjusts the number of pod replicas in a deployment, replication controller, or stateful set, based on observed CPU utilization or other select metrics. The HPA makes sure that applications can manage fluctuating traffic and workload levels without the need for manual intervention. The HPA offers a means of preserving optimal performance while making effective use of available resources.

In contexts where user demand might fluctuate considerably over time, such web apps, microservices, and APIs, the HPA is especially helpful.

The Horizontal Pod Autoscaler provides the following key features:
+ **Automatic scaling** – HPA automatically increases or decreases the number of pod replicas in response to real-time metrics, ensuring that applications can scale to meet user demand.
+ **Metrics-based decisions** – By default, HPA scales based on CPU utilization. However, it can also use custom metrics, such as memory usage or application-specific metrics, allowing for more tailored scaling strategies.
+ **Configurable parameters** – You can choose the minimum and maximum replica counts and the desired utilization percentages, giving you authority over how severe the scaling should be.
+ **Integration with Kubernetes** – To monitor and modify resources, HPA works in tandem with other elements of the Kubernetes ecosystem, including the Metrics Server, Kubernetes API, and custom metrics adapters.
+ **Better resource utilization** – HPA assists in making sure that resources are used effectively, lowering costs and improving performance, by dynamically modifying the number of pods.

## Cluster Proportional Autoscaler
<a name="cpa"></a>

The [Cluster Proportional Autoscaler](https://github.com/kubernetes-sigs/cluster-proportional-autoscaler) (CPA) is a Kubernetes component designed to automatically adjust the number of pod replicas in a cluster based on the number of nodes available. Unlike traditional autoscalers that scale based on resource utilization metrics (like CPU and memory), CPA scales workloads in proportion to the size of the cluster itself.

This approach is particularly useful for applications that need to maintain a certain level of redundancy or availability relative to the cluster size, such as CoreDNS and other infrastructure services. Some of the main use cases for CPA include the following:
+ Over-provisioning
+ Scale out core platform services
+ Scale out workloads because CPA doesn't require a metrics server or Prometheus Adapter

By automating the scaling process, CPA assists businesses in maintaining a balanced workload distribution, increasing resource efficiency, and making sure that applications are suitably provisioned to satisfy user demand.

The Cluster Proportional Autoscaler provides the following key features:
+ **Node-based scaling** – CPA scales replicas according to the number of cluster nodes that can be scheduled, enabling applications to expand or contract in proportion to the size of the cluster.
+ **Proportionate adjustment** – To ensure that the application can scale in accordance with changes in the cluster size, the autoscaler establishes a proportionate relationship between the number of nodes and the number of replicas. This relationship is used to compute the desired number of replicas for a workload.
+ **Integration with Kubernetes components** – CPA works with standard Kubernetes components like the Horizontal Pod Autoscaler (HPA) but focuses specifically on node count rather than resource utilization metrics. This integration allows for a more comprehensive scaling strategy.
+ **Golang API clients** – To monitor the number of nodes and their available cores, CPA uses Golang API clients that run inside of pods and talk to the Kubernetes API server.
+ **Configurable parameters** – Using a `ConfigMap`, users can set thresholds and scaling parameters that CPA uses to modify its behavior and make sure it follows the intended scaling plan.

## Kubernetes-based Event-Driven Autoscaler
<a name="keda"></a>

Kubernetes-based Event Driven Autoscaler ([KEDA](https://keda.sh/)) is an open-source project that enables Kubernetes workloads to scale based on the number of events that need to be processed. KEDA enhances the scalability of applications by allowing them to respond dynamically to varying workloads, particularly those that are event-driven.

By automating the scaling process based on events, KEDA helps organizations optimize resource utilization, improve application performance, and reduce costs associated with over-provisioning. This approach is especially valuable for applications that experience varying traffic patterns, such as microservices, serverless functions, and real-time data processing systems.

KEDA provides the following key features:
+ **Event-driven scaling** – KEDA allows you to define scaling rules based on external event sources, such as message queues, HTTP requests, or custom metrics. This capability helps make sure that applications scale in response to real-time demand.
+ **Lightweight component** – KEDA is a single-purpose, lightweight component that doesn't require a lot of setup or overhead to be readily integrated into existing Kubernetes clusters.
+ **Integration with Kubernetes** – KEDA extends the capabilities of Kubernetes-native components, such as the Horizontal Pod Autoscaler (HPA). KEDA adds event-driven scaling capabilities to these components, enhancing rather than replacing them.
+ **Support for multiple event sources** – KEDA is compatible with a wide range of event sources, including popular messaging platforms like RabbitMQ, Apache Kafka, and others. Because of this adaptability, you can customize scaling to fit your unique event-driven architecture.
+ **Custom scalers** – Using custom scalers, you can designate specific metrics that KEDA can use to initiate scaling actions in response to specific business logic or requirements.
+ **Declarative configuration** – In line with Kubernetes principles, you can use KEDA to describe scaling behavior declaratively by using Kubernetes custom resources to define how scaling should happen.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
