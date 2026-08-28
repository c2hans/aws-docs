---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/userguide/p2pe-compliance.html
---

# Using the AWS Payment Cryptography Decryption Component in P2PE solutions
<a name="p2pe-compliance"></a>

PCI P2PE Solutions can use the [AWS Payment Cryptography Decryption Component](https://listings.pcisecuritystandards.org/assessors_and_solutions/point_to_point_encryption_components). This is documented in the PCI Point-to-Point Encryption: Security Requirements and Testing Procedures, Section P2PE Solutions and Use of Third Parties and/or P2PE Component Providers: “A solution provider (or a merchant as a solution provider) can outsource certain P2PE functions to PCI-listed P2PE component providers and report use of the PCI-listed P2PE component(s) in their P2PE Report on Validation (P-ROV)”, which is available on the [PCI website](https://www.pcisecuritystandards.org/).

As with other AWS services and compliance standards, it is your responsibility to use the service securely, configuring access control and using security parameters in alignment with PCI P2PE requirements. The *AWS Payment Cryptography P2PE Decryption Component User’s Guide*, which is available on AWS Artifact, has detailed instructions for integrating AWS Payment Cryptography with your PCI P2PE Solution and the annual decryption component report, which is required for compliance reporting.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Payment Cryptography. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query payment-cryptography` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
