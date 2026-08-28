---
source_url: https://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/tgw-peering-attachments.html
---

# Transit gateway peering attachments
<a name="tgw-peering-attachments"></a>

This section provides instructions for creating transit gateway peering attachments.

See [Add or edit tags for a transit gateway](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-transit-gateways.html#tgw-tagging) for instructions on adding and editing tags.

## Add tags to transit gateway
<a name="add-tags-to-transit-gateway"></a>

| Key | Value | Description |
| --- | --- | --- |
|  **TgwPeer**  |  {{<tgw-id\_aws\_region>}}  | The default key prefix is `TgwPeer`.<br />The default delimiter in the tag value to list multiple transit gateway per region is `slash(/)`.<br />You must provide a valid Region name where the remote transit gateway exists. The value must be the remote transit gateway ID that exists in the `<aws_region>` that you provided in the key.<br />For example, if you create a peering attachment with a transit gateway (`tgw-2222`) in the U.S. East (Ohio) Region (`us-east-2`), the tag key would be `TgwPeer` and the value would be `tgw-2222_us-east-2`.<br />You can peer with a second transit gateway in the same Region by using the same delimiter to add another suffix the tag key. In this case, the tag key would be `TgwPeer` and the value must be `tgw-2222_us-east-2/tgw-3333_us-east-1`.<br />You can change the Transit Gateway Peering Tag add reference to the CFN parameter used in the key in the template during initial configuration, but you must use the same key name when you tag the transit gateway. Changing the value doesn’t update the attachment. You must delete the tag and recreate it with a new value, then recreate the peering attachment.  |

**Note**
If you created peering attachments using solution versions before v3.0.0 and then upgraded to v3.0.0 or later, those attachments cannot be deleted by updating the tag value on the transit gateway. You will need to delete them manually.

**Important**
To route traffic between peered transit gateways, you must add a static route to the selected transit gateway route table that points to the transit gateway peering attachment. After you create the route, associate the same transit gateway route table with the transit gateway peering attachment. Refer to [Create a static route](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-route-tables.html#tgw-create-static-route) for more information.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Network Orchestration for AWS Transit Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
