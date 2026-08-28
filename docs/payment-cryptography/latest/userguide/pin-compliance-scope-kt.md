---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/userguide/pin-compliance-scope-kt.html
---

# Key Table
<a name="pin-compliance-scope-kt"></a>

The report requires that all keys protecting PINs, directly or indirectly, are listed. Any keys that exist in the service can be listed with the [ListKeysAPI ](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ListKeys).

Be sure to provide the key list for all regions and accounts that own keys for your application.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Payment Cryptography. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query payment-cryptography` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
