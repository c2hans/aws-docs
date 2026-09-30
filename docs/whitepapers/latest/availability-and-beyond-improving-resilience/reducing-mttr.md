---
source_url: https://docs.aws.amazon.com/whitepapers/latest/availability-and-beyond-improving-resilience/reducing-mttr.html
---

# Reducing MTTR
<a name="reducing-mttr"></a>

 After a failure is discovered, the remainder of the MTTR time is the actual repair or mitigation of impact. To repair or mitigate a failure, you have to know what's wrong. There are two key groups of metrics that provide insight during this phase: 1/*Impact Assessment* metrics and 2/*Operational Health* metrics. The first group tells you the scope of impact during a failure, measuring the number or percentage of the customers, resources, or workloads impacted. The second group helps identify *why* there is impact. After the why is discovered, operators and automation can respond to and resolve the failure. Refer to [Appendix 1 – MTTD and MTTR critical metrics](appendix-1-mttd-and-mttr-critical-metrics.md) for more information about these metrics.

**Rule 9**
Observability and instrumentation are critical for reducing MTTD and MTTR.

## Route around failure
<a name="route-around-failure"></a>

 The fastest approach to mitigating impact is through fail-fast subsystems that route around failure. This approach uses redundancy to reduce MTTR by quickly shifting the work of a failed subsystem to a spare. The redundancy can range from software processes, to Amazon EC2 instances, to multiple AZs, to multiple Regions.

 Spare subsystems can reduce the MTTR down to almost zero. The recovery time is only what it takes to reroute the work to the stand-by spare. This often happens with minimal latency and allows the work to complete within the defined SLA, maintaining the availability of the system. This produces MTTRs that are experienced as slight, perhaps even imperceptible, delays, rather than prolonged periods of unavailability.

 For example, if your service uses Amazon EC2 instances behind an Application Load Balancer (ALB), you can configure health checks at an interval as small as five seconds and require only two failed health checks before a target is marked as unhealthy. This means that within 10 seconds, you can detect a failure and stop sending traffic to the unhealthy host. In this case, the MTTR is effectively the same as the MTTD since as soon as the failure is detected, it is also mitigated.

 This is what *high-availability* or *continuous-availability* workloads are trying to achieve. We want to quickly route around failure in the workload by quickly detecting failed subsystems, marking them as failed, stop sending traffic to them, and instead send traffic to a redundant subsystem.

 Note that using this kind of fail-fast mechanism makes your workload very sensitive to transient errors. In the example provided, ensure that your load balancer health checks are performing *shallow* or [*liveness and local*](https://aws.amazon.com/builders-library/implementing-health-checks/) health checks of just the instance, not testing dependencies or workflows (often referred to as *deep* health checks). This will help prevent unnecessary replacement of instances during transient errors affecting the workload.

 Observability and the ability to detect failure in subsystems is critical for routing around failure to be successful. You have to know the scope of impact so the affected resources can be marked as unhealthy or failed and taken out of service so they can be routed around. For example, if a single AZ experiences a partial service impairment, your instrumentation will need to be able to identify that there is an AZ-localized issue to route around all resources in that AZ until it has recovered.

 Being able to route around failure might also require additional tooling depending on the environment. Using the previous example with Amazon EC2 instances behind an ALB, imagine that instances in one AZ might be passing local health checks, but an isolated AZ impairment is causing them to fail to connect to their database in a different AZ. In this case, the load balancing health checks won't take those instances out of service. A different automated mechanism would be needed to [remove the AZ from the load balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-subnets.html) or force the instances to fail their health checks, which depends on identifying that the scope of impact is an AZ. For workloads that aren't using a load balancer, a similar method would be needed to prevent resources in a specific AZ from accepting units of work or removing capacity from the AZ altogether.

 In some cases, the shift of work to a redundant subsystem can't be automated, like the failover of a primary to secondary database where the technology doesn't provide its own leader election. This is a common scenario for [AWS multi-Region architectures](https://aws.amazon.com/blogs/architecture/disaster-recovery-dr-architecture-on-aws-part-i-strategies-for-recovery-in-the-cloud/). Because these types of failovers require some amount of downtime to accomplish, can't be immediately reversed, and leave the workload without redundancy for a period of time, it's important to have a human in the decision-making process.

 Workloads that can embrace a less strict consistency model can achieve shorter MTTRs by using multi-Region failover automation to route around failure. Features like [Amazon S3 cross-Region replication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html) or [Amazon DynamoDB global tables](https://aws.amazon.com/dynamodb/global-tables/) provide multi-Region capabilities through eventually consistent replication. Furthermore, using a relaxed consistency model is beneficial when we consider the CAP theorem. During network failures that impact connectivity to stateful subsystems, if the workload chooses availability over consistency, it can still provide non-error responses, another way of routing around failure.

 Routing around failure can be implemented with two different strategies. The first strategy is by implementing static stability by pre-provisioning enough resources to handle the complete load of the failed subsystem. This can be a single Amazon EC2 instance or it might be an entire AZ worth of capacity. Attempting to provision new resources during a failure increases the MTTR and adds a dependency to a control plane in your recovery path. However, it comes at additional cost.

 The second strategy is to route some of the traffic from the failed subsystem to others and [load shed the excess traffic](https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload) that cannot be handled by the remaining capacity. During this period of degradation, you can scale up new resources to replace the failed capacity. This approach has a longer MTTR and creates a dependency on a control plane, but costs less in standby, spare capacity.

## Return to a known good state
<a name="return-to-a-known-good-state"></a>

 Another common approach for mitigation during repair is returning the workload to a previous known good state. If a recent change might have caused the failure, rolling back that change is one way to return to the previous state.

 In other cases, transient conditions might have caused the failure, in which case, restarting the workload might mitigate the impact. Let's examine both of these scenarios.

 During a deployment, minimizing the MTTD and MTTR relies on observability and automation. Your deployment process must continually watch the workload for the introduction of increased error rates, increased latency, or anomalies. After these are recognized, it should halt the deployment process.

 There are various [deployment strategies](https://docs.aws.amazon.com/whitepapers/latest/overview-deployment-options/deployment-strategies.html), like in-place deployments, blue/green deployments, and rolling deployments. Each one of these might use a different mechanism to return to a known-good state. It can automatically roll back to the previous state, shift traffic back to the blue environment, or require manual intervention.

 CloudFormation [offers the capability to automatically rollback](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-rollback-triggers.html) as part of its create and update stack operations, as does [AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployments-rollback-and-redeploy.html#deployments-rollback-and-redeploy-automatic-rollbacks). CodeDeploy also supports blue/green and rolling deployments.

 To take advantage of these capabilities and minimize your MTTR, consider automating all of your infrastructure and code deployments through these services. In scenarios where you cannot use these services, consider implementing the [saga pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/implement-the-serverless-saga-pattern-by-using-aws-step-functions.html) with AWS Step Functions to rollback failed deployments.

 When considering *restart*, there are several different approaches. These range from rebooting a server, the longest task, to restarting a thread, the shortest task. Here is a table that outlines some of the restart approaches and approximate times to complete (representative of orders of magnitude difference, these are not exact).

|  Fault recovery mechanism  |  Estimated MTTR  |
| --- | --- |
|  Launch and configure new virtual server  |  15 minutes  |
|  Redeploy the software  |  10 minutes  |
|  Reboot server  |  5 minutes  |
|  Restart or launch container  |  2 seconds  |
|  Invoke new serverless function  |  100 ms  |
|  Restart process  |  10 ms  |
|  Restart thread  |  10 μs  |

 Reviewing the table, there are some clear benefits for MTTR in using containers and serverless functions (like [AWS Lambda](https://aws.amazon.com/lambda/)). Their MTTR is orders of magnitude faster than restarting a virtual machine or launching a new one. However, using fault isolation through software modularity is also beneficial. If you can contain failure to a single process or thread, recovering from that failure is much faster than restarting a container or server.

 As a general approach to recovery, you can move from bottom to top: 1/Restart, 2/Reboot, 3/Re-image/Redeploy, 4/Replace. However, once you get to the reboot step, routing around failure is usually a faster approach (usually taking at most 3–4 minutes). So, to most quickly mitigate impact after an attempted restart, route around the failure, and then, in the background, continue the recovery process to return capacity to your workload.

**Rule 10**
 Focus on impact mitigation, not problem resolution. Take the fastest path back to normal operation.

## Failure diagnosis
<a name="failure-diagnosis"></a>

 Part of the repair process after detection is the diagnosis period. This is the period of time where operators try to determine what is wrong. This process might involve querying logs, reviewing Operational Health metrics, or logging into hosts to troubleshoot. All of these actions require time, so creating tools and runbooks to expedite these actions can help reduce the MTTR as well.

## Runbooks and automation
<a name="runbooks-and-automation"></a>

 Similarly, after you determine what is wrong and what course of action will repair the workload, operators typically need to perform some set of steps to do that. For example, after a failure, the fastest way to repair the workload might be to restart it, which can involve multiple, ordered steps. Using a runbook that either automates these steps or provides specific direction to an operator will expedite the process and help reduce the risk of inadvertent action.
