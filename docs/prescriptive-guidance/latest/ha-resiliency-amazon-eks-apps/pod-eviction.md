---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/ha-resiliency-amazon-eks-apps/pod-eviction.html
---

# Understand pod eviction during zonal disruptions
<a name="pod-eviction"></a>

When a full Availability Zone disruption occurs—that is, when all nodes in that Availability Zone lose connectivity to the Kubernetes control plane—the [node lifecycle controller ](https://kubernetes.io/docs/concepts/architecture/cloud-controller/)in Kubernetes detects the situation and evicts pods from the impacted zone. Pods on unreachable nodes are marked as `Terminating` and new pods are scheduled on healthy nodes in available Availability Zones. During this period, affected nodes display a `NotReady` status, the scheduler prevents new pods from being placed on those nodes, and the EndpointSlice controller removes endpoints that are associated with the impaired Availability Zone from service routing until connectivity is restored.

For scenarios that involve partial node failures within a zone—where only a subset of nodes becomes unreachable—the node lifecycle controller applies different eviction behavior. If the disruption persists beyond the configured toleration period (by default, five minutes), pods on disconnected nodes are marked as `Terminating` and new pods are scheduled on healthy nodes in available Availability Zones.

## Implementing Amazon EKS zonal shift for improved resilience
<a name="implementing-zonal-shift"></a>

[Amazon EKS zonal shift](https://docs.aws.amazon.com/eks/latest/userguide/zone-shift.html), which integrates with Amazon Application Recovery Controller (ARC), provides a mechanism to proactively manage traffic during Availability Zone impairments. This capability allows temporary redirection of network traffic away from an unhealthy Availability Zone toward healthy zones within the same AWS Region to minimize service disruption.

## Understanding the zonal shift mechanism
<a name="understanding-zonal-shift"></a>

Amazon EKS zonal shift addresses east-west traffic (inter-pod communication within the cluster). When zonal shift is configured with Application Load Balancers or Network Load Balancers, it also supports ingress traffic routing. The mechanism operates by coordinating multiple Kubernetes and AWS control plane components to safely redirect traffic without disrupting running workloads. During an active zonal shift, Amazon EKS automatically performs the following coordinated actions:
+ **Node cordoning**: All nodes in the impaired Availability Zone are cordoned. This prevents the Kubernetes scheduler from placing new pods on the nodes while it maintains existing workloads.
+ **Availability Zone rebalancing suspension**: For managed node groups, Availability Zone rebalancing operations are suspended, and Auto Scaling groups are updated to launch new data plane nodes exclusively in healthy Availability Zones. This ensures that new capacity isn't provisioned in the impaired zone.
+ **Endpoint removal**: The EndpointSlice controller removes pod endpoints in the impaired Availability Zone from all relevant EndpointSlices. This ensures that service discovery and load balancing mechanisms route traffic only to pods that are running in healthy Availability Zones.
+ **Workload preservation**: Amazon EKS refrains from terminating nodes or evicting pods in the affected Availability Zone. It maintains full capacity in the impaired zone so that when the zonal shift expires or is canceled, traffic can safely return without requiring additional scaling operations.

## Zonal shift activation methods
<a name="activating-zonal-shift"></a>

You can choose from two approaches to initiate zonal shifts, depending on your operational model:
+ [Manual zonal shift](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.html) provides operator-driven control when specific Availability Zone issues are detected through monitoring, alerts, or customer reports. This method requires explicit action through the Amazon Application Recovery Controller (ARC) console, AWS Command Line Interface (AWS CLI), or zonal shift APIs, where operators specify the impaired Availability Zone and define an expiration time for the shift. Manual shifts are appropriate when teams have dedicated monitoring and on-call capabilities and prefer to maintain direct control over traffic management decisions.
+ [Zonal autoshift](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.html) authorizes AWS to automatically initiate shifts when the Amazon Application Recovery Controller (ARC) detects potential Availability Zone failures or impairments based on internal telemetry and health signals across multiple AWS services, including network metrics, Amazon Elastic Compute Cloud (Amazon EC2), and Elastic Load Balancing. AWS automatically ends an autoshift when indicators show that the issue has been resolved. If you want the highest availability posture with minimal manual intervention, we recommend this approach, because it enables sub-minute response to detected Availability Zone impairments.

## Prerequisites for effective zonal shift
<a name="effective-zonal-shift"></a>

For zonal shift to successfully protect applications during Availability Zone impairments, you must architect your clusters for Multi-AZ resilience before you enable the zonal shift feature:
+ **Multi-AZ node distribution**: Provision worker nodes across at least three Availability Zones to ensure sufficient redundancy when one zone becomes unavailable.
+ **Capacity planning**: Pre-provision enough compute capacity across healthy Availability Zones to accommodate the full workload when one Availability Zone is removed from service, because scaling operations during an active disruption might encounter insufficient capacity.
+ **Pod distribution and pre-scaling**: Deploy multiple replicas of each application across all Availability Zones and pre-scale critical system components such as [CoreDNS](https://docs.aws.amazon.com/eks/latest/userguide/managing-coredns.html) in every zone. This helps ensure that sufficient capacity remains after a zone is shifted away.

## Recommendations for zonal disruption resilience
<a name="zonal-shift-recommendations"></a>
+ **Enable zonal shift at cluster creation**: For new EKS clusters, enable zonal shift integration with Amazon Application Recovery Controller (ARC) during initial provisioning through the Amazon EKS console, AWS CLI,  or infrastructure as code (IaC) tools such as AWS CloudFormation. [EKS Auto Mode clusters](https://docs.aws.amazon.com/eks/latest/userguide/automode.html) that are created with quick configuration have zonal shift enabled by default.
+ **Select the appropriate activation method**: Choose zonal autoshift for production environments that require maximum availability with automated response, particularly for customer-facing applications where minutes of downtime during an Availability Zone impairment can carry significant business impact. Use manual zonal shift for environments where operations teams prefer to provide explicit approval before traffic shifts, or where application testing and validation are still in progress.
+ **Test resilience before production deployment:** Validate cluster behavior under Single-AZ loss by manually initiating test zonal shifts or enabling zonal autoshift practice runs to verify that applications maintain availability, performance remains acceptable, and capacity is sufficient when operating with reduced Availability Zone count. We strongly recommend this testing so you can identify configuration gaps before actual Availability Zone impairments occur.
+ **Coordinate with load balancer configuration**: For applications that receive external traffic, enable Amazon Application Recovery Controller (ARC) zonal shift on associated Application Load Balancers and Network Load Balancers to ensure that both ingress traffic and in-cluster east-west traffic shift together during Availability Zone impairments. This coordination prevents scenarios where external requests reach healthy pods but those pods cannot communicate with dependencies in the shifted-away zone.
+ **Monitor shift operations**: After you enable zonal shift, configure monitoring and alerting for shift events, including autoshift activations, manual shift initiations, and shift expirations, to maintain operational visibility into traffic management actions and their impact on application behavior.

## Shift completion and recovery
<a name="shift-completion-recovery"></a>

When a zonal shift expires based on its configured duration or is manually canceled after the Availability Zone impairment resolves, the EndpointSlice controller automatically updates all EndpointSlices to reincorporate endpoints in the restored Availability Zone. Traffic gradually returns to the previously impacted zone as clients refresh endpoint information and establish new connections. This enables full cluster capacity utilization without requiring manual intervention or pod rescheduling.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
