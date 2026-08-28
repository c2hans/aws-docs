---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/launch-instances-synchronously.html
---

# Launch instances synchronously
<a name="launch-instances-synchronously"></a>

Amazon EC2 Auto Scaling provides two methods for launching instances in your Auto Scaling group: asynchronous scaling behavior and synchronous provisioning using the LaunchInstances API.

With synchronous provisioning, you use the LaunchInstances API to request a specific number of instances in a particular Availability Zone. Synchronous provisioning provides the following benefits:
+ Immediate feedback on capacity availability in specific Availability Zones
+ Precise control over which Availability Zone instances launch in
+ Deterministic instance IDs for immediate use in orchestration systems
+ Real-time scaling decisions based on actual capacity constraints
+ Faster scaling by eliminating wait times for asynchronous Auto Scaling launches

With asynchronous Auto Scaling, when you change the desired capacity or when a scaling policy triggers, Amazon EC2 Auto Scaling processes the scaling request and launches instances in the background. You must monitor scaling activities or describe your Auto Scaling group to determine when instances are successfully launched.

**Note**
The LaunchInstances API only works with Auto Scaling groups that use launch templates. Auto Scaling groups that use launch configurations are not supported. If your Auto Scaling group uses a launch configuration, you must migrate to a launch template before using synchronous provisioning.
The LaunchInstances API supports mixed instances policies with fully On-Demand or fully Spot purchasing options only. Mixed policies combining both On-Demand and Spot Instances are not supported.
For Auto Scaling groups covering multiple Availability Zones, you must specify the target Availability Zone or subnet. For single-AZ groups, this parameter is optional.

## Synchronous provisioning and asynchronous scaling
<a name="synchronous-vs-asynchronous-scaling"></a>

### Synchronous provisioning
<a name="synchronous-provisioning-behavior"></a>

When you use the LaunchInstances API, Amazon EC2 Auto Scaling:
+ Immediately attempts to launch the requested instances using CreateFleet
+ Waits for CreateFleet to return instance IDs before responding
+ Returns instance IDs, instance types, and Availability Zone information on success
+ Returns specific error codes and details on failure
+ Provides immediate feedback, enabling real-time scaling decisions

### Asynchronous scaling
<a name="asynchronous-scaling-behavior"></a>

When you use asynchronous Auto Scaling methods such as changing the desired capacity or using scaling policies, Amazon EC2 Auto Scaling:
+ Updates the desired capacity in the API but won't return instances immediately
+ Plans instance launches across Availability Zones automatically
+ Launches instances through background workflows
+ Automatically distributes capacity across multiple Availability Zones for balance
+ Handles launch failures with built-in retry logic

You must poll scaling activities or describe your Auto Scaling group to check the status of launch operations.

## Limitations and considerations
<a name="limitations-considerations-synchronous"></a>

When working with synchronous provisioning, keep in mind the following notes and limitations:
+ **Instance state after launch** – Instances returned by the API are in pending state. They may still fail during subsequent workflow processes or lifecycle hooks. A successful API response means that EC2 has accepted the launch request and returned the instance IDs. Instances aren't automatically considered fully ready for workloads and must complete standard EC2 and Auto Scaling lifecycle processes.
+ **Warm pool limitation** – Auto Scaling groups with warm pools are currently not supported. If you attempt to call the LaunchInstances API on an Auto Scaling group that has a warm pool configured, the API performs a cold start instead of using warm pool instances and returns an UnsupportedOperation error. For more information about cold starts, see [Limitations of warm pools](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-warm-pools.html#warm-pools-limitations).
+ **API timeout and retries** – If the underlying CreateFleet operation takes longer than expected, the API may timeout and return an idempotency token. You can retry using the same ClientToken to track the original launch operation or use describe-instances with the client token to check launched instances.
+ **Availability Zone constraints** – If your Auto Scaling group spans multiple Availability Zones and has Availability Zone rebalancing enabled, launching instances synchronously can cause operational conflicts:
  + Single AZ limitation per call – Each LaunchInstances API call can only target one Availability Zone, even if your Auto Scaling group spans multiple zones.
  + AZ rebalancing conflicts - If your Auto Scaling group has AZ rebalancing enabled, sequential calls across different AZs may trigger additional asynchronous launches, resulting in more instances than intended. Consider suspending AZ rebalancing for precise capacity control. For more information, see [Suspend and resume Amazon EC2 Auto Scaling processes](as-suspend-resume-processes.md).
+ **Partial success scenarios** – The `LaunchInstances` API may return partial success if only some of the requested capacity is available, which is normal EC2 behavior. The API returns successfully launched instances along with error details for failed launches. For use cases requiring all instances to launch together (such as applications needing all instances in the same AZ for low latency), you'll need to terminate partially launched instances and retry in a different AZ. Consider this behavior when designing retry logic for capacity-sensitive workloads.
+ **Instance weights** – If your Auto Scaling group uses instance weights, the RequestedCapacity parameter represents weighted capacity units, not the number of instances. The actual number of instances launched depends on the instance types selected and their configured weights. EC2 Auto Scaling limits launches to 100 instances per API call, regardless of the weighted capacity requested.
+ **Mixed instance types** – The LaunchInstances API uses your Auto Scaling group's existing mixed instances policy to determine which instance types to launch. The API launches instances according to your group's allocation strategy and instance type priorities.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
