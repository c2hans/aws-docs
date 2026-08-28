---
source_url: https://docs.aws.amazon.com/pcs/latest/userguide/working-with_capacity-reservations.html
---

# Capacity Reservations in AWS PCS
<a name="working-with_capacity-reservations"></a>

 You can reserve Amazon EC2 capacity in a specific Availability Zone and for a specific duration using On-Demand Capacity Reservations or Amazon EC2 Capacity Blocks for ML to make sure that you have the necessary compute capacity available when you need it.

 **On-Demand Capacity Reservations (ODCRs)** let you reserve compute capacity for your Amazon EC2 instances in a specific Availability Zone for any duration. You can create and cancel reservations at any time, with no long-term commitments or upfront payments. ODCRs are ideal when you need flexible capacity reservations that you can modify as your requirements change. For more information, see [On-Demand Capacity Reservations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-reservations.html) in the *Amazon Elastic Compute Cloud User Guide*.

 **Amazon EC2 Capacity Blocks for ML** allow you to reserve GPU-based accelerated computing instances on a future date to support your machine learning (ML) workloads. For more information, see [Capacity Blocks for ML](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-blocks.html) in the *Amazon Elastic Compute Cloud User Guide*.

**Topics**
+ [Using ODCRs with AWS PCS](capacity-reservations-odcr.md)
+ [Using I-ODCRs with AWS PCS](capacity-reservations-iodcr.md)
+ [Using Amazon EC2 Capacity Blocks for ML with AWS PCS](capacity-blocks.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS PCS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pcs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
