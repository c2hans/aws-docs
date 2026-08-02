---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_fault_isolation_single_az_system.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# REL10-BP03 Automate recovery for components constrained to a single location
<a name="rel_fault_isolation_single_az_system"></a>

 If components of the workload can only run in a single Availability Zone or in an on-premises data center, you must implement the capability to do a complete rebuild of the workload within your defined recovery objectives.

 If the best practice to deploy the workload to multiple locations is not possible due to technological constraints, you must implement an alternate path to resiliency. You must automate the ability to recreate necessary infrastructure, redeploy applications, and recreate necessary data for these cases.

 For example, Amazon EMR launches all nodes for a given cluster in the same Availability Zone because running a cluster in the same zone improves performance of the jobs flows as it provides a higher data access rate. If this component is required for workload resilience, then you must have a way to redeploy the cluster and its data. Also for Amazon EMR, you should provision redundancy in ways other than using Multi-AZ. You can provision [multiple nodes](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-ha-launch.html). Using [EMR File System (EMRFS)](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-fs.html), data in EMR can be stored in Amazon S3, which in turn can be replicated across multiple Availability Zones or AWS Regions.

 Similarly, for Amazon Redshift, by default it provisions your cluster in a randomly selected Availability Zone within the AWS Region that you select. All the cluster nodes are provisioned in the same zone.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>
+  Implement self-healing. Deploy your instances or containers using automatic scaling when possible. If you cannot use automatic scaling, use automatic recovery for EC2 instances or implement self-healing automation based on Amazon EC2 or ECS container lifecycle events.
  +  Use Auto Scaling groups for instances and container workloads that have no requirements for a single instance IP address, private IP address, Elastic IP address, and instance metadata.
    +  [What Is EC2 Auto Scaling?](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html)
    +  [Service automatic scaling](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-auto-scaling.html)
      +  The launch template user data can be used to implement automation that can self-heal most workloads.
  +  Use automatic recovery of EC2 instances for workloads that require a single instance ID address, private IP address, Elastic IP address, and instance metadata.
    +  [Recover your instance.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-recover.html)
      +  Automatic Recovery will send recovery status alerts to a SNS topic as the instance failure is detected.
  +  Use EC2 instance lifecycle events or ECS events to automate self-healing where automatic scaling or EC2 recovery cannot be used.
    +  [EC2 Auto Scaling lifecycle hooks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html)
    +  [Amazon ECS events](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_cwe_events.html)
      +  Use the events to invoke automation that will heal your component according to the process logic you require.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Amazon ECS events](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_cwe_events.html)
+  [EC2 Auto Scaling lifecycle hooks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html)
+  [Recover your instance.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-recover.html)
+  [Service automatic scaling](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-auto-scaling.html)
+  [What Is EC2 Auto Scaling?](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html)
