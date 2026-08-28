---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/userguide/generate-card-data.html
---

# Generate card data
<a name="generate-card-data"></a>

 The `Generate Card Data` API is used to generate card data using algorithms such as CVV,CVV2 or Dynamic CVV2. To see what keys can be used for this command, please see [Valid keys for cryptographic operations](crypto-ops-validkeys-ops.md) section.

Many cryptographic values such as CVV, CVV2, iCVV, CAVV V7 use the same cryptographic algorithm but vary the input values. For instance [CardVerificationValue1](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_CardVerificationValue1.html) has inputs of ServiceCode, Card Number and Expiration Date. While [CardVerificationValue2](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_CardVerificationValue2.html) only has two of these inputs, this is because for CVV2/CVC2, the ServiceCode is fixed at 000. Similarly, for iCVV the ServiceCode is fixed at 999. Some algorithms may repurpose the existing fields such as CAVV V8 in which case you will need to consult your provider manual for the correct input values.

**Note**
 Expiration date must be entered in the same format (such as MMYY vs. YYMM) for generation and validation to produce correct results.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Payment Cryptography. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query payment-cryptography` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
