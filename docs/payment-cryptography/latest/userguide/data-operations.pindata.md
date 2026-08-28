---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/userguide/data-operations.pindata.html
---

# Generate, translate and verify PIN data
<a name="data-operations.pindata"></a>

PIN data functions allow you to generate random pins, pin verification values (PVV) and validate inbound encrypted pins against PVV or PIN Offsets.

Pin translation allows you to translate a pin from one working key to another without exposing the pin in clear text as specified by PCI PIN Requirement 1.

**Note**
 As PIN generation and validation are typically issuer functions and PIN translation is a typical acquirer function, we recommend that you consider least priviledged access and set policies appropriately for your systems use case.

**Topics**
+ [Translate PIN data](translate-pin-data.md)
+ [Generate PIN data](generate-pin-data.md)
+ [Verify PIN data](verify-pin-data.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Payment Cryptography. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query payment-cryptography` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
