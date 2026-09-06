---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-vdi/vdi-capacity-planning.html
---

# Instance capacity planning for large VDI migrations
<a name="vdi-capacity-planning"></a>

VDI solutions tend to require the deployment of hundreds or thousands of EC2 instances. To avoid [insufficient instance capacity errors](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/troubleshooting-launch.html#troubleshooting-launch-capacity), we recommend that you develop a rollout plan and work with AWS Support or your AWS Technical Account Manager to coordinate the capacity requirements with the AWS service team.

Capacity planning is even more important if dedicated instances or dedicated hosts are required. Consider the following when planning instance capacity requirements:
+ Concurrent instances required
+ Instance families and types
+ [On-Demand Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-on-demand-instances.html), [On-Demand Capacity Reservations (ODCR)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-reservations.html), or [Reserved Instances (RI)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-reserved-instances.html) capacity
+ Cost implications

## Capacity reservation considerations
<a name="capacity-reservation-considerations"></a>

When developing a capacity reservation model, consider and answer the following:
+ How much capacity is required for concurrent users?
+ Does the solution have to cater for unavailability of a specific Availability Zone or instance types?
+ Is reserved capacity required to meet business requirements?

To answer these questions, you can use the following matrix. The matrix includes an example of how you might distribute instance types for a total of 5,000 VDI users.

![Decision chart for how plan reservations for EC2 instances for VDI users](http://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-vdi/images/guide-img/4216869b-a3c7-4a1b-8529-279b6b36f090/images/6c283fb5-936a-4e28-a7d0-dab2a44f888d.png)
