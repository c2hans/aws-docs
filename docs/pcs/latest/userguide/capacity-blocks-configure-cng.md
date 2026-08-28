---
source_url: https://docs.aws.amazon.com/pcs/latest/userguide/capacity-blocks-configure-cng.html
---

# Configure an AWS PCS compute node group to use a Capacity Block
<a name="capacity-blocks-configure-cng"></a>

**To associate a Capacity Block with a compute node group**

1. Create an Amazon EC2 launch template for AWS PCS that specifies your Capacity Block. For more information about creating a launch template for AWS PCS, see [Using Amazon EC2 launch templates with AWS PCS](working-with_launch-templates.md).

   Your launch template must include:
   + The value `MarketType` of `InstanceMarketOptions` must be set to `capacity-block`.
   + A `CapacityReservationSpecification` with a valid `CapacityReservationId`
   + A valid `InstanceType` that matches the instance type of the Capacity Block you purchased.

1. Create a compute node group that uses the launch template. For more information, see [Creating a compute node group in AWS PCS](working-with_cng_create.md). You can also update an existing compute node group to use the launch template. For more information, see [Updating an AWS PCS compute node group](working-with_cng_update.md).

   When you create or update the compute node group:
   + The IAM identity you use to create or update the compute node group must have the following permissions:

     ```
     ec2:DescribeCapacityReservations
     ec2:DescribeCapacityBlocks
     ec2:DescribeCapacityBlockStatus
     ```

     For more information, see [Minimum permissions for AWS PCS](security-min-permissions.md).
   + The Capacity Block must be in a `scheduled` or `active` state.
   + Set the `purchaseOption` of the compute node group to `CAPACITY_BLOCK`.
   + The `maxInstanceCount` of the compute node group must not exceed the size of the Capacity Block.
   + The availability zone of the compute node group must match 1 of the compute node group's subnet availability zones.

**Important**
You can't change the instance type of a compute node group when you update it. You can only use a Capacity Block with the same instance type as the compute node group. If you want to use a Capacity Block with a different instance type, you must create a new compute node group.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS PCS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pcs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
