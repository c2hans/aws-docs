---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/userguide/verify-card-data.html
---

# Verify card data
<a name="verify-card-data"></a>

`Verify Card Data` is used to verify data that has been created using payment algorithms that rely on encryption principals such as `DISCOVER_DYNAMIC_CARD_VERIFICATION_CODE`.

The input values are typically provided as part of an inbound transaction to an issuer or supporting platform partner. To verify an ARQC cryptogram (used for EMV chips cards), please see [Verify ARQC](data-operations.verifyauthrequestcryptogram.md).

For more information, see [VerifyCardValidationData](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_VerifyCardValidationData.html) in the API guide.

If the value is verified, then the api will return http/200. If the value is not verified, it will return http/400.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Payment Cryptography. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query payment-cryptography` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
