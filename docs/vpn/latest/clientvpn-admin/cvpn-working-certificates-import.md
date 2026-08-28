---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-certificates-import.html
---

# Import an AWS Client VPN client certificate revocation list
<a name="cvpn-working-certificates-import"></a>

You must have a Client VPN client certificate revocation list file to import. For more information about generating a client certificate revocation list, see [Generate an AWS Client VPN client certificate revocation list](cvpn-working-certificates-generate.md).

You can import a client certificate revocation list using the console and the AWS CLI.

**To import a client certificate revocation list (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint for which to import the client certificate revocation list.

1. Choose **Actions**, and choose **Import Client Certificate CRL**.

1. For **Certificate Revocation List**, enter the contents of the client certificate revocation list file, and choose **Import client certificate CRL**.

**To import a client certificate revocation list (AWS CLI)**
Use the [import-client-vpn-client-certificate-revocation-list](https://docs.aws.amazon.com/cli/latest/reference/ec2/import-client-vpn-client-certificate-revocation-list.html) command.

```
$ aws ec2 import-client-vpn-client-certificate-revocation-list --certificate-revocation-list file://{{path_to_CRL_file}} --client-vpn-endpoint-id {{endpoint_id}} --region {{region}}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
