---
source_url: https://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/using-and-customizing-route-tables.html
---

# Using and customizing route tables
<a name="using-and-customizing-route-tables"></a>

This section provides a user guide for solution transit gateway route tables.

## Default route tables
<a name="default-route-tables"></a>

This solution creates the following default transit gateway route tables: `Flat`, `Isolated`, `Infrastructure`, and `On-premises`. Each route table and suggested propagations include a policy for common use cases.
+  **Flat**\***route table** - VPCs associated with the `Flat` policy can reach other VPCs associated with the `Flat`, `SharedServices`, or `Hybrid` policies. The `Flat` policy enables a VPC to have connectivity to many other VPCs.
+  **Isolated route table** - VPCs associated with the `Isolated policy` can reach VPCs with the `SharedServices` and `Hybrid` policies. VPCs in the `Isolated` policy can’t use Transit Gateway to connect to other VPCs in the `Isolated` policy. This policy is for VPCs that don’t communicate with each other.
+  **Infrastructure route table** - VPCs associated with the `SharedServices` policy can reach other VPCs associated with the `Isolated`, `Flat`, or `Hybrid` policies. The `SharedServices` policy is used for VPCs that many other VPCs may rely on, such as shared authentication, shared tooling, or orchestration tools.
+  **On-premises route table -** This route table is used for connecting to on-premises through either [AWS Virtual Private Network](https://aws.amazon.com/vpn/) (AWS VPN) or [AWS Direct Connect](https://aws.amazon.com/directconnect/). Associate your on-premises connections to the `On-premises` route table.

| Policy types | Associate with (route table name) | Propagate to (list of route table names) |
| --- | --- | --- |
|  ** `Flat` (east-west traffic)**  |  `Flat`  |  `Flat, On-premises, Infrastructure`  |
|  ** `Isolated` (north-south traffic)**  |  `Isolated`  |  `On-premises, Infrastructure`  |
|  ** `SharedServices` **  |  `Infrastructure`  |  `Flat, On-premises, Isolated`  |
|  ** `Hybrid` **  |  `On-premises`  |  `Flat, Infrastructure, Isolated`  |

**Note**
In this implementation guide, a policy is defined by both an association to a single transit gateway route table, and the transit gateway route table propagation. To implement these concepts, you must tag both the association and propagation on each spoke VPC according to the intended design. This is because the policies aren’t centrally managed. Inconsistent tagging can create a drift between the desired policy and what is configured.
You can use the **ApprovalRequired** tag on route tables that need manual control. By default, we set up this solution for automatic approval, but you can change this tag to set up manual approval. See [Transit gateway route table tags](custom-compliance.md#add-tags-to-transit-gateway-route-table) for more information about the **ApprovalRequired** tag.
For more information, refer to [On-premises connectivity](#on-premises-connectivity).

## Custom route tables
<a name="custom-route-tables"></a>

If the default policies don’t meet your requirements, you can create your own transit gateway route table configurations.

**Note**
You don’t need a separate route table for each VPC to achieve segmentation. Segmentation is accomplished by controlling the propagation. For example, an `Isolated` route table doesn’t propagate to itself and, as a result, nothing associated with an `Isolated` route table is able to reach other `Isolated` resources through the transit gateway.

The administrator can create new transit gateway route tables in the Amazon VPC console in the hub account. The combination of route tables and propagation provided with the transit gateway allows for a variety of connection policies.

### Example 1: Create a new custom route table
<a name="example-1-create-a-new-custom-route-table"></a>

The following sample table and steps provide a guide for setting your routing policies. For this example, you implement a `Development` policy and route table. This policy and route table allow developers to create VPCs that don’t have access to sensitive resources in the `Isolated` or `Infrastructure` route tables. You create a new transit gateway route table that propagates to the `Flat`, `On-premises`, and `Development` route tables.

| Policy types | Associate with (route table name) | Propagate to (list of route table names) |
| --- | --- | --- |
|  ** `Flat` (east-west traffic)**  |  `Flat`  |  `Flat, On-premises, Infrastructure, Development`  |
|  ** `Isolated` (north-south traffic)**  |  `Isolated`  |  `On-premises, Infrastructure`  |
|  ** `SharedServices` **  |  `Infrastructure`  |  `Flat, On-premises, Isolated`  |
|  ** `Hybrid` **  |  `On-premises`  |  `Flat, Infrastructure, Isolated, Development`  |
|  ** `Development` **  |  `Development`  |  `Development, Flat, On-premises`  |

#### Create the route table
<a name="create-the-route-table"></a>

1. In the hub account, sign in to the [Amazon VPC console](https://console.aws.amazon.com/vpc/home).

1. In the navigation pane, choose **Transit gateway route tables**.

1. Choose **Create transit gateway route table**.

1. For **Name tag**, enter a name for the route table. For this example, enter `Development`.

1. For **Transit gateway ID**, select the appropriate transit gateway.

1. Choose **Create transit gateway route table**. You will receive a confirmation message.

1. Select **Close**.

1. Optional: If you want changes to this route table to be manually approved:

   1. Select the newly created route table from the list in step 2.

   1. Choose the **Tags** tab.

   1. Choose **Add/Edit** tags and then choose **Create tag**.

   1. In the **Key** field, enter `ApprovalRequired` and in the **Value** field, enter `Yes`.

   1. Choose **Save**.

#### Determine the access model
<a name="determine-the-access-model"></a>

After the new route table is created, determine the access model. For two transit gateway attachments to communicate, each of their associated route tables must have each other’s routes.

1. Determine where your new route table should propagate routes, defined by the other transit gateway route tables. For example, should the `Infrastructure` route table be propagated from your new `Development` route table?

1. Check that the other route tables are reciprocating the propagation for two-way communication. For example, you may want to propagate `Infrastructure`, `Flat`, and `On-premises` route table to your new `Development` route table.
**Note**
If your custom route table requires access to VPCs that have already been attached, you must change the **Propagate-to** tag for each spoke VPC to include your new route table.

#### Associate VPCs
<a name="associate-vpcs"></a>

To associate a new VPC to this route table:

1. Tag the new VPC with the **Associate-with** key and reference the new route table name in the value. See [Step 5: Add tags](step-5-add-tags.md) for detailed tagging instructions. For example:

   ```
   Associate-with: <ExampleRouteTable>
   ```

1. Tag the new VPC with the **Propagate-to** key and reference the route tables you want to propagate to from the previous step. For example:

   ```
   Propagate-to: Infrastructure, Flat, Hybrid
   ```

1. Tag one subnet in each Availability Zone. For example:

   ```
   Attach-to-tgw: <leave blank>
   ```
**Note**
If you configured manual approval, you might need to sign in to the web UI to approve the change. If that is the case, you will receive an email with the request that contains the link to the web UI.

To confirm the attachment, look for attachments on the transit gateway in the VPC management console, in the web UI, or in the state machine history.

For more information about transit gateway route tables, refer to [Transit gateway route tables](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-route-tables.html).

### Example 2: Modify policies
<a name="example-2-modify-policies"></a>

If you don’t need the provided `Flat` policy, you can modify the existing `Flat` policy to meet your custom requirements. Turn off propagation to the `Infrastructure` route table and remove the `Flat` propagation from the `Infrastructure` route table.

## On-premises connectivity
<a name="on-premises-connectivity"></a>

This solution builds a base network, giving you automation to attach VPCs to a transit gateway. You can extend your on-premises network by creating transit gateway route tables using the web UI, creating VPN attachments, or attaching a transit gateway to an AWS Direct Connect gateway.

For instructions on how to manually attach a VPN to the transit gateway for on-premises connectivity, see [Transit gateway VPN attachments](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-vpn-attachments.html).

For instructions on how to manually attach Direct Connect to the transit gateway for on-premises connectivity, refer to [Transit gateway attachments to a Direct Connect gateway](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-dcg-attachments.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Network Orchestration for AWS Transit Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
