---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/ethereum-dev/ethereum-data-protection.html
---

# Data protection for Amazon Managed Blockchain (AMB) Access Ethereum
<a name="ethereum-data-protection"></a>

Data encryption helps prevent unauthorized users from reading data from a blockchain network and the associated data storage systems. This includes data that might be intercepted as it travels the network, known as *data in transit*.

## Encryption in transit
<a name="managed-blockchain-encryption-in-transit"></a>

By default, AMB Access uses an HTTPS/TLS connection to encrypt all the data that's transmitted from a client computer that runs the AWS CLI to AWS service endpoints.

You don't need to do anything to enable the use of HTTPS/TLS. It's always enabled unless you explicitly disable it for an individual AWS CLI command by using the `--no-verify-ssl` command line option.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Blockchain. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-blockchain` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
