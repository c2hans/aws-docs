---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/amazon-emr-hardware/configuration-best-practices.html
---

# Configuration best practices
<a name="configuration-best-practices"></a>

When configuring your Amazon EMR cluster, use the following best practices for adding instances, working with instance groups, and using Spot Instances.

## Adding instances
<a name="adding-instances"></a>

When you are configuring your Amazon EMR cluster, an important consideration is the right choice of your Amazon EC2 instances that will represent your cluster nodes. Remember that you can't change the type of instances, such as changing Spot Instances to On-Demand Instances, when the cluster is running. To change the primary node, you must shut down the cluster and create a new one. That is why you must choose the correct instance type so that you have the least down-time possible. For more information, see [Cluster configuration guidelines and best practices](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-instances-guidelines.html).

There are several ways to add Amazon EC2 instances to a cluster, depending on whether you use the instance groups configuration or the instance fleets configuration for the cluster:
+ Manually add Amazon EC2 instances
+ Manually add a task on the instance group to automatically add an instance
+ Set up automatic scaling

## Instance groups
<a name="instance-groups"></a>

When you are adding Amazon EC2 instances to your configuration, consider using instance groups. If you are manually adding instances, you can add instances of the same type to existing core and task instance groups. Also, you can add a task instance group, which can use a different instance type.

Finally, set up automatic scaling in Amazon EMR for an instance group. Instances can be added and removed automatically based on the value of an Amazon CloudWatch metric that you specify. Otherwise, if you are using instance fleets, add a single task instance fleet. Then change the target capacity for On-Demand Instances and Spot Instances for existing core and task instance fleets.

## Spot Instances
<a name="spot-instances"></a>

Use Spot Instances on task nodes. The task nodes process data but do not hold persistent data in Hadoop Distributed File System (HDFS). If task nodes shut down because the Spot price has risen above your maximum Spot price, no data is lost, and the effect on your cluster is minimal.

When you launch task instance groups as Spot Instances, Amazon EMR provisions as many task nodes as it can, using your maximum Spot price. For example, you can request a task instance group with six nodes. If only five Spot Instances are available at or below your maximum Spot price, Amazon EMR launches the instance group with five nodes. Amazon EMR adds the sixth node later if possible. For more information, see [Cluster configuration guidelines and best practices](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-instances-guidelines.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
