---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/regional-services.html
---

# Regional services
<a name="regional-services"></a>

 Regional services are built on top of multiple Availability Zones, using their isolation and redundancy to transparently reduce infrastructure failures as a category of availability and durability risk for your workloads. For example, Amazon S3 spreads requests and data across multiple Availability Zones by default and is designed to automatically recover from the failure of a single Availability Zone. Regional services are also isolated from service disruptions in other Regions.

 Many customers meet their resilience objectives within a single AWS Region with zonal and regional fault isolation. However, some applications might require additional redundancy to tolerate the impairment of a regional AWS service. Because of the physical and logical separation between AWS Regions, you can use multiple Regions to create bounded recovery times to a wide range of infrastructure- and application-level failures.

 Multi-Region architectures involve tradeoffs in cost, effort, data consistency, latency, and operational burden. If you choose to build multi-Region applications, you should consider your recovery requirements, data access and consistency requirements, operational processes, and dependencies. For more information on multi-Region architectures, see [AWS Multi-Region Fundamentals](https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-multi-region-fundamentals/introduction.html) and [Disaster Recovery of Workloads on AWS](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html).

 The best practices for multi-Region applications are similar to multi-AZ applications. First, make sure you don’t have cross-Region dependencies, or that your applications are able to gracefully degrade when a dependency is unavailable. Your application should be able to successfully run without network connectivity to resources in the impaired Region.

 Second, consider pre-provisioning capacity in the failover Region to absorb the load from the impaired Region. While you shouldn’t plan for the control plane to be impaired in the failover Region, other customers might also be failing over and competing for similar capacity requirements. The only way to guarantee you can acquire capacity in both multi-AZ and multi-Region applications is to already be running the capacity or using an [On-Demand Capacity Reservation (ODCR)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-reservations.html). If you use a multi-Region approach that doesn’t have all of your required capacity pre-provisioned (such as with pilot light or warm standby approaches), you risk not being able to immediately acquire the required capacity to match what you have provisioned in your primary Region. This might delay your ability to recover, missing your recovery time objective and removing the consistent, bounded recovery you expect. AWS makes no guarantees about the available capacity in any single Availability Zone or Region.

 This approach presents a cost tradeoff that you should weigh against the business impact of not being able to provision the capacity you require. To reduce the cost impact of pre-provisioning capacity, you can run non-production applications or async or batch type applications on the capacity in the failover Region. Then, protect this capacity with ODCRs. During a failover, you would terminate the instances running these lower-tier applications and re-provision that capacity for the more critical applications that are being failed over. The ODCRs make sure you still have access to this capacity during the termination and re-provisioning process.

 If you choose not to pre-provision capacity, you can use approaches like instance type flexibility and Availability Zone flexibility. If you’re able to run your application on a variety of Amazon EC2 instance families and sizes, you will have a better chance of acquiring your desired capacity. [Amazon EC2 Auto Scaling mixed instances groups](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-mixed-instances-groups.html) and [Amazon EC2 Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-ec2-fleet.html) support this capability. AWS manages Amazon EC2 capacity at the Availability Zone level, so being flexible about which Availability Zones you scale capacity in can also help. For the purpose of regional failover, being unbalanced across the Availability Zones in your recovery Region might be acceptable.

 Finally, you can combine some of these approaches with patterns like load shedding and graceful degradation. If immediately acquiring your required capacity isn’t possible, but you can provision some or have a warm standby, you might choose to accept some traffic while load shedding additional traffic to protect your application from overload. Alternatively, you can choose to only offer specific functionality while you operate at reduced capacity. Whichever approach you choose for multi-Region failover, make sure you test the process regularly so that you’re confident it will work when you need it.

**Regional services best practices**
Plan for potential impact to regional AWS service control planes and data planes and build multi-Region applications as required
Build multi-Region applications using an intentional approach for capacity planning
Remove cross-Region dependencies in your applications
Plan to recover your application from regional service impairments, either through graceful degradation or regional failover
Test that plan regularly
