---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcoops04.html
---

# IP verification
<a name="telcoops04"></a>

|  TELCOOPS04: How do you represent IP addresses to the internet and verify the quality of the address representation?  |
| --- |
|   |

 Telco's own large CIDR blocks of IP addresses and wish to have them represented with their ownership even when advertised by AWS. The IP address CIDR block are assigned to telco resources in the cloud and should be propagated through AWS to the Internet where both the CIDR block and the ASN associated with the prefixes are represented as owned by the telco. This improves the reputation of the address prefix propagated across the Internet for telco subscribers and gives CSPs responsibility and accountability of the address space.

**Topics**
+ [TELCOOPS04-BP01 Implement the Bring Your Own IP (BYOIP) address processes and associate the prefixes with the IPAM solution](telcoops04-bp01.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
