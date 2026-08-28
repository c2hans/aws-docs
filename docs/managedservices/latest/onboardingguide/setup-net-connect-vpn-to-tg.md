---
source_url: https://docs.aws.amazon.com/managedservices/latest/onboardingguide/setup-net-connect-vpn-to-tg.html
---

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

# Connecting VPN to Transit Gateway
<a name="setup-net-connect-vpn-to-tg"></a>

To attach a VPN connection to your transit gateway, you must specify the customer gateway. For more information about the requirements for a customer gateway, see Requirements for Your Customer Gateway in the Amazon VPC Network Administrator Guide.

You would need to provide the BGP ASN number, static public IP address and routing Option (Static or Dynamic). Once these details are provided, AMS would create the VPN attachment and associate the attachment with the on-prem Transit Gateway routing table.

For more details on Transit Gateway attachments, see [Transit Gateway VPN Attachments](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-vpn-attachments.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
