---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_Alias.html
---

# Alias
<a name="API_Alias"></a>

Contains information about an alias.

## Contents
<a name="API_Alias_Contents"></a>

 ** AliasName **   <a name="paymentcryptography-Type-Alias-AliasName"></a>
A friendly name that you can use to refer to a key. The value must begin with `alias/`.
Do not include confidential or sensitive information in this field. This field may be displayed in plaintext in AWS CloudTrail logs and other output.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 256.
Pattern: `alias/[a-zA-Z0-9/_-]+`
Required: Yes

 ** KeyArn **   <a name="paymentcryptography-Type-Alias-KeyArn"></a>
The `KeyARN` of the key associated with the alias.
Type: String
Length Constraints: Minimum length of 70. Maximum length of 150.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:key/[0-9a-zA-Z]{16,64}`
Required: No

## See Also
<a name="API_Alias_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-2021-09-14/Alias)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-2021-09-14/Alias)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-2021-09-14/Alias)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Payment Cryptography Control Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query payment-cryptography` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
