---
source_url: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-configuring-dnssec-proof-of-nonexistence.html
---

# DNSSEC proofs of nonexistence in Route 53
<a name="dns-configuring-dnssec-proof-of-nonexistence"></a>

**Note**
Route 53 uses the following rule which might change. Any future changes will not reduce your zone's or Route 53's security posture.

There are three kinds of proof of nonexistence in DNSSEC:
+ Proof of nonexistence of a record matching the query name.
+ Proof of nonexistence of a type matching the query type.
+ Proof of existence of a wildcard record used to generate the record in response.

Route 53 implements the proof of nonexistence of a record matching the query name using the BL method. For more information, see [BL](https://datatracker.ietf.org/doc/html/draft-valsorda-dnsop-black-lies-00). It's a method that produces a compact representation of the proof and prevents zone walking.

In cases where there is a record matching the query name but not the query type (such as querying for web.example.com/AAAA but there is only web.example.com/A present), we return a minimal NSEC (next secure) record containing all supported resource record types.

When Route 53 synthesizes an answer from a wildcard record, the response will not be accompanied with a next secure record, or NSEC record for the wildcard. Such NSEC record is used in some implementations, typically those performing offline signing, to prevent the resource record signatures (RRSIG) in the response from being re-used to spoof a different response. Route 53 uses online signing for non-DNSKEY records to generate RRSIGs specific to the response which cannot be re-used for a different response.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
