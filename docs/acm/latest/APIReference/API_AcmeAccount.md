---
source_url: https://docs.aws.amazon.com/acm/latest/APIReference/API_AcmeAccount.html
---

# AcmeAccount
<a name="API_AcmeAccount"></a>

Contains detailed information about an ACME account.

## Contents
<a name="API_AcmeAccount_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AccountUrl **   <a name="ACM-Type-AcmeAccount-AccountUrl"></a>
The URL of the ACME account.
Type: String
Required: No

 ** AcmeExternalAccountBindingArn **   <a name="ACM-Type-AcmeAccount-AcmeExternalAccountBindingArn"></a>
The Amazon Resource Name (ARN) of the external account binding associated with this ACME account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `arn:aws[a-z-]*:acm:[a-z0-9-]+:[0-9]{12}:acme-endpoint/[a-zA-Z0-9-]+/acme-external-account-binding/[a-zA-Z0-9-]+`
Required: No

 ** Contacts **   <a name="ACM-Type-AcmeAccount-Contacts"></a>
The contact information for the ACME account.
Type: Array of strings
Required: No

 ** CreatedAt **   <a name="ACM-Type-AcmeAccount-CreatedAt"></a>
The time at which the ACME account was created.
Type: Timestamp
Required: No

 ** PublicKeyThumbprint **   <a name="ACM-Type-AcmeAccount-PublicKeyThumbprint"></a>
The thumbprint of the public key associated with the ACME account.
Type: String
Required: No

 ** Status **   <a name="ACM-Type-AcmeAccount-Status"></a>
The status of the ACME account.
Type: String
Valid Values: `VALID | DEACTIVATED | REVOKED`
Required: No

## See Also
<a name="API_AcmeAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/AcmeAccount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/AcmeAccount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/AcmeAccount)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ACM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query acm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
