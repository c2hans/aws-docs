---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-endpoint-delete.html
---

# Delete an AWS Client VPN endpoint
<a name="cvpn-working-endpoint-delete"></a>

You will need to disassociate all target networks before you can delete a Client VPN endpoint. When you delete a Client VPN endpoint, its state is changed to `deleting` and clients can no longer connect to it.

You can delete a Client VPN endpoint by using the console or the AWS CLI.

**To delete a Client VPN endpoint (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint to delete. Choose **Actions**, **Delete Client VPN endpoint**.

1. Enter *delete* into the confirmation window and choose** Delete**.

**To delete a Client VPN endpoint (AWS CLI)**
Use the [delete-client-vpn-endpoint](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-client-vpn-endpoint.html) command.
