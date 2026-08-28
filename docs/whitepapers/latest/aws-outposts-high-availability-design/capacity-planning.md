---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/capacity-planning.html
---

# Capacity planning
<a name="capacity-planning"></a>

 While Amazon EC2 capacity in AWS Regions is seemingly infinite, capacity on Outposts is finite – constrained by the total volume of compute capacity ordered. You are responsible for planning and managing the compute capacity of your Outposts deployments. You should order sufficient compute capacity to support an N\+M availability model, where N is the required number of servers and M is the number of spare servers provisioned to accommodate server failures. N\+1 and N\+2 are the most common availability levels.

 Each host (`C5`, `M5`, `R5`, etc.) supports a single family of EC2 instances. Before you can launch instances on EC2 compute servers, you must provide slotting layouts that specify the [EC2 instance sizes](https://aws.amazon.com/ec2/instance-types/) you want each server to provide. AWS configures each server with the requested slotting layout.

 Hosts may be homogeneously slotted where all slots are the same instance size (for example, 48 `m5.large` slots) or heterogeneously slotted with a mixture of instances types (for example, 4 `m5.large`, 4 `m5.xlarge`, 3 `m5.2xlarge`, 1 `m5.4xlarge`, and 1 `m5.8xlarge`) – see the next three figures for visualizations of these slotting configurations.

![Diagram showing m5.24xlarge host compute resources](http://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/images/m5-24xlarge-server-resources.png)

![Diagram showing m5.24xlarge host homogenously slotted into 48 m5.large slots](http://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/images/m5-24xlarge-slotted-into-48-m5-large-slots.png)

![Diagram showing m5.24xlarge host heterogeneously slotted into 4 m5.large, 4 m5.xlarge, 3 m5.2xlarge, 1 m5.4xlarge, and 1 m5.8xlarge slots](http://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/images/m5-24xlarge-slotted-into-different-x5-slots.png)

The full host capacity does not have to be slotted. Slots may be added to a host that has available unallocated capacity. You can modify a slotting layout by using the Capacity Management APIs or UIs for AWS Outposts and creating a new capacity task. For more information, see [Capacity management for AWS Outposts](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-capacity.html) in the *AWS Outposts user guide for racks*. You may be required to shut down or restart certain instances to complete a new capacity task if the new slotting layout cannot be applied while certain slots are occupied by running instances. The `CreateCapacityTask` API allows you to express the number of each instance size that should be present on the Outpost ID indicated, and in the event that a task cannot be completed due to running instances, returns instances that must be stopped in order to satisfy the request. At this point, you can optionally indicate that you want to see “N” additional options in the event that you would prefer not to stop one of the instances returned, and you can also indicate an EC2 instance ID, EC2 instance tag, account, or service that should not be suggested as an instance to shut down in order to satisfy the capacity task request. After making your selection of the option you’d like to go with, we recommend using the Dry Run parameter to validate the proposed changes and understand the potential impact before implementing.

 All hosts contribute their provisioned slots to the EC2 capacity pools on the Outpost, and all slots of a given instance type and size are managed as a single EC2 capacity pool. For example, the previous heterogeneously slotted host with `m5.large`, `m5.xlarge`, `m5.2xlarge`, `m5.4xlarge`, and `m5.8xlarge` slots would contribute these slots to five EC2 capacity pools – one pool for each instance type and size. These pools may be spread across multiple hosts, and instance placement should be a consideration to achieve workload high availability.

 It is important to consider host slotting and EC2 capacity pools when planning spare capacity for N\+M host availability. AWS detects when a host fails or is degraded and schedules a site visit to replace the failed host. You should design your EC2 capacity pools to tolerate the failure of at least one server of each instance family (N\+1) in an Outpost. With this minimum level of host availability, when a host fails or needs to be taken out of service, you can restart failed or degraded instances on the spare slots of the remaining hosts of the same family.

 Planning for N\+M availability is simple when you have homogenously slotted hosts or groups of heterogeneously slotted hosts with identical slotting layouts. You simply calculate the number of hosts (N) your need to run all your workloads and then add (M) additional hosts to meet your requirements for server availability during failure and maintenance events.

The following slotting configurations are not usable due to NUMA boundaries:
+ 3 `m5.8xlarge`
+ 1 `m5.16xlarge` and 1 `m5.8xlarge`

Consult your AWS account team to validate your planned AWS Outposts rack slotting configuration.

 In the following figure, four `m5.24xlarge` hosts are heterogeneously slotted with an identical slotting layout. The four hosts create five EC2 capacity pools. Each pool is running at maximum utilization (75%) to maintain N\+1 availability for the instances running on these four hosts. If any host fails, there is sufficient room to restart the failed instances on the remaining hosts.

![Diagram showing Visualization of EC2 host slots, running instances, and slot pools](http://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/images/ec2-server-slots-and-pools.png)

 For more complex slotting layouts, where hosts are not identically slotted, you will need to calculate N\+M availability for each EC2 capacity pool. You can use the following formula to calculate how many hosts (that contribute slots to a given EC2 capacity pool) can fail and still allow the remaining hosts to carry the running instances:

![Equation M = (available pool slots / maximum host slots)](http://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/images/equation.png)

 Where:
+ **poolSlotsavailable** is the number of available slots in the given EC2 capacity pool (total number of slots in the pool minus the number of running instances)
+  **serverSlotsmax** is the maximum number of slots contributed by any host to the given EC2 capacity pool
+  **M** is the number of hosts that can fail and still allow the remaining hosts to carry the running instances

 ***Example:*** An Outpost has three hosts that contribute slots to an `m5.2xlarge` capacity pool. The first contributes 4 slots, the second contributes 3 slots, and the third host contributes 2 slots. The `m5.2xlarge` instance pool on the Outpost has a total capacity of 9 slots (4 \+ 3 \+ 2). The Outpost has 4 running `m5.2xlarge` instances. How many hosts may fail and still allow the remaining hosts to carry the running instances?

![Three equations](http://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/images/equations.png)

 ***Answer:*** You can lose any one of the hosts and still carry the running instances on the remaining hosts.

## Recommended practices for compute capacity planning
<a name="recommended-practices-for-compute-capacity-planning"></a>
+ Size your compute capacity to provide N\+M redundancy for each EC2 capacity pool on an Outpost.
+ Deploy N\+M servers for homogeneously or identical heterogeneously slotted servers.
+ Calculate the N\+M availability for each EC2 capacity pool and ensure that each pool meets your availability requirements.
+ Consider size compute capacity for use cases that require [ALB on AWS Outposts](https://aws.amazon.com/blogs/networking-and-content-delivery/configuring-an-application-load-balancer-on-aws-outposts/) and [Amazon Route 53 local Resolver](https://aws.amazon.com/blogs/aws/amazon-route-53-resolver-now-available-on-aws-outposts-rack/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
