---
source_url: https://docs.aws.amazon.com/tag-editor/latest/userguide/infrastructure-security.html
---

# Infrastructure security in Tag Editor
<a name="infrastructure-security"></a>

Tag Editor doesn't provide additional ways of isolating service or network traffic. If applicable, use AWS specific isolation. You can use the Tag Editor API and console in a virtual private cloud (VPC) to help maximize privacy and infrastructure security.

You use AWS published API calls to access Tag Editor through the network. Clients must support the following:
+ Transport Layer Security (TLS). We require TSL 1.2 and recommend TSL 1.3.
+ Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems such as Java 7 and later support these modes.

Additionally, requests must be signed by using an access key ID and a secret access key that is associated with an AWS Identity and Access Management (IAM) principal. Or, you can use the [AWS Security Token Service](https://docs.aws.amazon.com/STS/latest/APIReference/) (AWS STS) to generate temporary security credentials to sign requests.

Tag Editor does not support resource-based policies.

You can call Tag Editor API operations from any network location, but Tag Editor does support resource-based access policies, which can include restrictions based on the source IP address. You can also use Tag Editor policies to control access from specific Amazon Virtual Private Cloud (Amazon VPC) endpoints or specific VPCs. Effectively, this approach isolates network access to a given resource from only the specific VPC within the AWS network.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Tagging and Tag Editor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query tag-editor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
