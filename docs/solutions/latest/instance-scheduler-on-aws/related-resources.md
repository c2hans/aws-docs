---
source_url: https://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/related-resources.html
---

# Related resources
<a name="related-resources"></a>

The [Resource Scheduler](https://docs.aws.amazon.com/systems-manager/latest/userguide/quick-setup-scheduler.html) is a similar to Instance Scheduler on AWS, but its implementation differs in the following ways:

Instance Scheduler on AWS uses a Lambda function to frequently evaluate the schedules stored in its configuration and checks if the instances are in the desired state. The Resource scheduler quicksetup uses start and stop times to perform start and stop actions using SSM runbooks. This occurs one time when the current time is equal to the start time or the current time is past the start time.

Instance Scheduler on AWS currently enables scheduling for EC2, RDS, and Aurora Clusters. Resource scheduler only schedules or starts and stops EC2 instances.

Use Resource scheduler to identify EC2 instances and start/stop them at specific times.

Use Instance Scheduler on AWS when the accounts have to regulary scanned to start/stop instances.

The table identifies which solution is better based on scenarios.

| Scenario | Resource Scheduler | Instance Scheduler on AWS |
| --- | --- | --- |
| Schedule Amazon Neptune instances | No | Yes |
| Schedule Amazon DocumentDB instances | No | Yes |
| Schedule Auto Scaling group instances | No | Yes |
| Schedule EC2 instances | Yes | Yes |
| Schedule RDS instances | No | Yes |
| Schedule Aurora Clusters | No | Yes |
| Manage Schedules in a Single Account (hub account) | No | Yes |
| Manage Schedules in individual accounts | Yes | No |
| Change Calendar Integration | Yes | No |
| Start and Stop actions only | Yes | No |
| Monitor instances periodically and start and stop based on instance current state | No | Yes |
