---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_MpaStatus.html
---

# MpaStatus
<a name="API_MpaStatus"></a>

The status of an MPA session.

## Contents
<a name="API_MpaStatus_Contents"></a>

 ** InitiationDate **   <a name="paymentcryptography-Type-MpaStatus-InitiationDate"></a>
The date and time when the MPA session was initiated.
Type: Timestamp
Required: Yes

 ** MpaSessionArn **   <a name="paymentcryptography-Type-MpaStatus-MpaSessionArn"></a>
The ARN of the MPA session.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:mpa:[a-z0-9-]{1,20}:[0-9]{12}:session/[a-zA-Z0-9._-]+/[a-zA-Z0-9_-]+`
Required: Yes

 ** Status **   <a name="paymentcryptography-Type-MpaStatus-Status"></a>
The current status of the MPA session.
Type: String
Valid Values: `PENDING | APPROVED | FAILED | CANCELLED`
Required: Yes

 ** StatusMessage **   <a name="paymentcryptography-Type-MpaStatus-StatusMessage"></a>
The message providing additional information about the MPA session status.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

## See Also
<a name="API_MpaStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-2021-09-14/MpaStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-2021-09-14/MpaStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-2021-09-14/MpaStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Payment Cryptography Control Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query payment-cryptography` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
