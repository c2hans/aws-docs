---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/userguide/pin-compliance-scope-diagram.html
---

# High-Level Network Diagrams
<a name="pin-compliance-scope-diagram"></a>

The PCI PIN Reporting Template requires, “For entities engaged in the processing of PIN based transaction provide a network schematic describing PIN based transaction flows with the associated key type usage. Additionally, KIFs and entities engaged in remote key distribution using asymmetric techniques should provide keying material flows“

AWS Payment Cryptography has reported the internal service structure for our PCI PIN assessment. Your diagrams will illustrate calling the service APIs for PIN processing.

Example high level network diagram for a PIN applications using AWS Payment Cryptography:

![Example high level network diagram for a PIN applications using AWS Payment Cryptography](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/images/high-level-network-example.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Payment Cryptography. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query payment-cryptography` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
