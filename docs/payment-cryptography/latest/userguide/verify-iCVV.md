---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/userguide/verify-iCVV.html
---

# Verify iCVV
<a name="verify-iCVV"></a>

**Example**
In this example, we will verify a [iCVV](terminology.md#terms.icvv) for a given PAN with inputs of [Key to Use for validation (CVK)](create-keys.md#cvvkey-example), `PAN`, a service code of 999, card expiration date and the iCVV provided by the transaction to validate.
iCVV is not a user entered value (like CVV2) but embedded on an EMV card. Consideration should be given to whether it should always validate when provided.
For all available parameters see, [CardVerificationValue1](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_CardVerificationValue1.html) in the API reference guide.

```
$ aws payment-cryptography-data verify-card-validation-data --key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/tqv5yij6wtxx64pi --primary-account-number=171234567890123 --verification-attributes CardVerificationValue1='{CardExpiryDate=1127,ServiceCode=999} --validation-data 801
```

```
{
    "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/tqv5yij6wtxx64pi",
    "KeyCheckValue": "CADDA1",
    "ValidationData": "801"
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Payment Cryptography. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query payment-cryptography` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
