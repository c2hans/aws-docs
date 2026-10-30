---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/zonal-services.html
---

# Zonal services
<a name="zonal-services"></a>

 You can use zonal services, such as Amazon EC2 and Amazon EBS, to provision and operate resources in an Availability Zone that you specify. Zonal services have zonal data planes that operate independently in each Availability Zone within a Region, and more importantly, fail independently in each Availability Zone. We call this pattern [Availability Zone Independence (AZI)](https://aws.amazon.com/builders-library/static-stability-using-availability-zones/). In some cases, such as with Amazon EC2, the service also includes zonal control planes for zonally aligned operations, such as launching an Amazon EC2 instance. Each zonal service also provides a regional control plane endpoint to manage regionally scoped functionality and simplify interacting with the service’s zonal control planes by providing a routing and aggregation layer. This is shown in the following figure.

![This image shows a zonal service with zonally isolated control planes and data planes](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/images/a-zonal-service-with-zonally-isolated-control-planes-and-data-planes.png)

 Zonal data planes don’t take dependencies on components in other Availability Zones or on regional services, which helps prevent simultaneous correlated failures. It also allows them to remain operational if regional services are impacted. As a result, the scope of impact for a zonal service’s data plane resources is typically a single Availability Zone in a Region. By using multiple Availability Zones, you can implement redundant application replicas that provide isolation to single-AZ failures and allow you to recover by partitioning off the impacted AZ from your application.

 AWS Local Zones, Wavelength Zones, and Outposts bring the data plane of select AWS services closer to end users. The control planes for these services reside in the parent Region. Your Local Zone or Outposts instance will have control plane dependencies for zonal services like Amazon EC2 and Amazon EBS in the Availability Zone where you created your Local Zone or Outposts subnet. They will also have dependencies on regional control planes for regional services like Elastic Load Balancing, security groups, and the [Amazon Elastic Kubernetes Service](https://docs.aws.amazon.com/eks/latest/userguide/local-zones.html) (Amazon EKS)-managed Kubernetes control plane (if you use Amazon EKS). For additional information specific to Outposts, see the [Outposts documentation](https://docs.aws.amazon.com/outposts/latest/userguide/disaster-recovery-resiliency.html) and [support and maintenance FAQ](https://aws.amazon.com/outposts/rack/faqs/#support-and-maintenance).

 There are two best practices for using zonal service fault boundaries to improve the resilience of your applications.

 First, design your application to detect single-Availability Zone impairments and successfully shift traffic away from the affected zone. You should use per-AZ health metrics, either custom application metrics or AWS-provided metrics such as the per-AZ [`HTTPCode_Target_5XX_Count`](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-cloudwatch-metrics.html#target-metric-table) metrics from Application Load Balancers, to determine when an Availability Zone is unhealthy. To enable rapid recovery, you can use [zonal shift](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.html) to redirect traffic away from the impaired Availability Zone, or [zonal autoshift](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.html) to automatically initiate a shift based on AWS telemetry of Availability Zone health.

 Traffic shifting must extend to the dependencies used by your application so that requests don’t re-enter the impaired Availability Zone. This requires deploying dependencies redundantly across multiple Availability Zones and ensuring that request routing, service discovery, and data access paths respect Availability Zone isolation during a shift. Recovering from single-Availability Zone impairments should be tested regularly using the AWS Fault Injection Service (FIS) and zonal shift so you’re confident the process will work when you need it.

 You can also take advantage of Availability Zones by following some of the same best practices AWS uses for its own services, such as only deploying changes to a single Availability Zone at a time and shifting work away from an Availability Zone when that change has unexpected results. For more details about Availability Zone recovery, see the [Advanced Multi-AZ Resilience Patterns](https://docs.aws.amazon.com/whitepapers/latest/advanced-multi-az-resilience-patterns/advanced-multi-az-resilience-patterns.html) whitepaper.

 Second, design your application to be statically stable to single-Availability Zone impairments, as described in [Static stability using Availability Zones](https://aws.amazon.com/builders-library/static-stability-using-availability-zones/). For multi-Availability Zone architectures, plan for the simultaneous loss of an Availability Zone’s worth of capacity. Rather than launching new resources in response to a failure, a statically stable approach uses pre-provisioned capacity to make sure that sufficient resources are already available.

 Static stability enables faster recovery by eliminating resource provisioning as a recovery step and reduces the risk that control plane impairments impact your ability to recover successfully. This pattern is also recommended when using Local Zones or Outposts, where control plane impairments or interruptions in connectivity to the parent Region can affect recovery. As with any resilience strategy, you should weigh the trade-offs of static stability, such as increased cost, against the risk of exceeding your application’s recovery time objectives.

**Zonal service best practices**
Remove cross-AZ dependencies, or provide multi-AZ redundancy of dependencies, to prevent cascading failures across AZs
Use per-AZ observability to detect single-AZ impairments
Make your application statically stable to single-AZ impairments
Recover from a single-AZ impairment by partitioning off the affected AZ
