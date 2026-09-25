---
source_url: https://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/tgw-attachments-to-vpc.html
---

# Transit gateway attachments to a VPC
<a name="tgw-attachments-to-vpc"></a>

This section provides instructions for attaching VPCs to your transit gateway.

## Add tags to VPCs
<a name="add-tags-to-vpcs"></a>

Follow the step-by-step instructions in this section to add tags to your VPCs.

1. Sign in to your spoke account.

1. Navigate to the [Amazon VPC console](https://console.aws.amazon.com/vpc/).

1. Choose **VPCs**.

1. Select **Tags** and choose **Manage tags**.

1. Choose **Add new tag**.

1. Add the key-value pairs listed in [VPC tags](#vpc-tags).
**Note**
If you’re using custom names for your transit gateway route tables, the values of the tags you assign need to match the names of the route tables associated with the transit gateway you’re connecting to.

## Add tags to subnets
<a name="add-tags-to-subnets"></a>

Follow the step-by-step instructions in this section to add tags to your subnets.

1. Sign in to your spoke account.

1. Navigate to [Subnets](https://us-east-1.console.aws.amazon.com/vpc/home?region=us-east-1#subnets:) within the Amazon VPC console.

1. Select the subnet that you want to attach to the transit gateway.

1. Select **Tags** and choose **Manage tags**.

1. Choose **Add new tag**.

1. Add keys (without values) listed in [Subnet tags](#subnet-tags).

## Add transit gateway attachments
<a name="transit-gateway-attachments-to-a-vpc"></a>

Tags identify applicable resources, such as VPCs and subnets, in your spoke accounts. Tags allow create, read, update, and delete (CRUD) operations to run on the transit gateway route table associations and propagation.

**Note**
Verify that you have the appropriate access privileges to tag VPCs in spoke accounts, or identify the appropriate administrator in your organization.

### VPC tags
<a name="vpc-tags"></a>

For this Guidance to manage a VPC, the VPC in the spoke account must be tagged with both the **Associate-with** and **Propagate-to** keys. You must also add or remove both keys at the same time. By default, the tags are configured for automatic approval.

| Key | Value | Description |
| --- | --- | --- |
|  **Associate-with**  |  {{<Requires input>}}  | The default key is `Associate-with`. The value can be one of the default route table names (`Flat`, `Isolated`, `Infrastructure`, or `On-premises`) or a custom key.<br />You can change the name of the key in the template during initial configuration, but you must use the same key name when you tag the VPC.<br /> **Type:** String<br />For sample route table options, refer to [Custom route tables](using-and-customizing-route-tables.md#custom-route-tables). |
|  **Propagate-to**  |  {{<Requires input>}}  | The default key is `Propagate-to`. The value can be one or more default route table names (`Flat`, `Isolated`, `Infrastructure`, or `On-premises`) or a key(s) that you created.<br />You can change the name of the key in the template during initial configuration, but you must use the same key name when you tag the VPC.<br /> **Type:** CommaDelimitedList<br />For sample route table options, refer to [Custom route tables](using-and-customizing-route-tables.md#custom-route-tables). |

### Subnet tags
<a name="subnet-tags"></a>

**Note**
For a transit gateway attachment to a VPC, you can add only one subnet per Availability Zone. You can’t attach a second subnet in the same Availability Zone to the transit gateway.
Starting in version 3.3.0, this Guidance supports a new tag key **Route-to-tgw** that skips adding the subnet in the transit gateway attachment and only updates the associated route table with the default route.

| Key | Value | Description |
| --- | --- | --- |
|  **Attach-to-tgw**  |  *<Leave blank>*  | The default key is `Attach-to-tgw`. Don’t enter a value. <br />You can change the name of the key in the template during initial configuration, but you must use the same key name when you tag the subnet.<br />If there isn’t an explicit route table associated with the subnet, the Guidance updates the main route table with the default route. |
|  **Route-to-tgw**  |  *<Leave blank>*  | The default key is `Route-to-tgw`. Don’t enter a value. <br />You can change the name of the key in the template during initial configuration, but you must use the same key name when you tag the subnet.<br />If there isn’t an explicit route table associated with the subnet, the Guidance updates the main route table with the default route. |
