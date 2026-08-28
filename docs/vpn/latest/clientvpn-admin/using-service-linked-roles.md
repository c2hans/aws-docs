---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/using-service-linked-roles.html
---

# Using service-linked roles for AWS Client VPN
<a name="using-service-linked-roles"></a>

AWS Client VPN uses AWS Identity and Access Management (IAM) service-linked roles. A service-linked role is a unique type of IAM role that is linked directly to Client VPN. Service-linked roles are predefined by Client VPN and include all the permissions that the service requires to call other AWS services on your behalf.

**Topics**
+ [Client VPN usage](using-service-linked-roles-cvpn-slr.md)
+ [Connection authorization](using-service-linked-roles-client-connect-handler.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
