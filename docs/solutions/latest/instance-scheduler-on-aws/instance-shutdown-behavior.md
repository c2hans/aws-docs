---
source_url: https://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/instance-shutdown-behavior.html
---

# Instance shutdown behavior
<a name="instance-shutdown-behavior"></a>

## Amazon EC2
<a name="amazon-ec2"></a>

This solution is designed to automatically stop EC2 instances and assumes that instance *shutdown behavior* is set to Stop, not Terminate. Note that you cannot restart an Amazon EC2 instance after it is terminated.

By default, EC2 instances are configured to stop, not terminate, when shut down, but you can [modify this behavior](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingInstanceInitiatedShutdownBehavior). Therefore, make sure that the instances you control using the Instance Scheduler on AWS are configured with a Stop shutdown behavior; otherwise, they will be terminated.

## Amazon RDS, Amazon Neptune, and Amazon DocumentDB
<a name="amazon-rds-amazon-neptune-and-amazon-documentdb"></a>

This solution is designed to automatically stop, not delete, RDS, Neptune, and DocDB instances. You can use the **Create RDS Instance Snapshot** AWS CloudFormation template parameter to create snapshots of RDS DB instances before the solution stops the instances. Snapshots are kept until the next time the instance is stopped and a new snapshot is created.

**Note**
Snapshots are not available for Amazon Aurora clusters. You can use the **Schedule Aurora Clusters** template parameter to start and stop RDS DB instances that are part of an Aurora cluster or that manage Aurora databases. You must tag the cluster (not the individual instances) with the tag key you defined during initial configuration and the schedule name as the tag value to schedule that cluster.

For more information about limitations to starting and stopping an RDS DB instance, refer to [Stopping an Amazon RDS DB instance temporarily](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_StopInstance.html) in the *Amazon RDS User Guide*.

When an RDS DB instance is stopped, the cache is cleared, which might lead to slower performance when the instance is restarted.

## Amazon RDS maintenance window
<a name="amazon-rds-maintenance-window"></a>

Every RDS DB instance has a weekly [maintenance window](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Maintenance.html#Concepts.DBMaintenance) during which any system changes are applied. During the maintenance window, Amazon RDS will automatically start instances that have been stopped for more than seven days to apply maintenance. Amazon RDS will not stop the instance once the maintenance event is complete.

The solution allows you to specify whether to add the preferred maintenance window of an RDS DB instance as a running period to its schedule. The solution will start the instance at the beginning of the maintenance window and stop the instance at the end of the maintenance window if no other running period specifies that the instance should run, and if the maintenance event is completed.

If the maintenance event is not completed by the end of the maintenance window, the instance will run until the scheduling interval after the maintenance event is completed. For more information about the Amazon RDS maintenance window, refer to [Maintaining a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Maintenance.html) in the *Amazon RDS User Guide*.

## Amazon EC2 Auto Scaling groups
<a name="amazon-ec2-auto-scaling-groups"></a>

We designed this solution to automatically stop Amazon EC2 Auto Scaling groups by using scheduled scaling actions. You can use the solution to configure scheduled scaling actions on the Auto Scaling group (ASG). When an ASG is stopped by a scheduled scaling action, its minimum, desired, and maximum capacities will be set to `0` until the ASG is automatically started again. This will return the minimum, desired, and maximum capacities to their original values.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Instance Scheduler on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
