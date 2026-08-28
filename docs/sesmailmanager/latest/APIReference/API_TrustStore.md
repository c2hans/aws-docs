---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_TrustStore.html
---

# TrustStore
<a name="API_TrustStore"></a>

The trust store used for mutual TLS authentication. It contains the certificate authority (CA) certificates and optional certificate revocation list (CRL).

## Contents
<a name="API_TrustStore_Contents"></a>

 ** CAContent **   <a name="sesmailmanager-Type-TrustStore-CAContent"></a>
The PEM-encoded certificate authority (CA) certificates bundle for the trust store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500000.
Pattern: `[\P{C}\s]*`
Required: Yes

 ** CrlContent **   <a name="sesmailmanager-Type-TrustStore-CrlContent"></a>
The PEM-encoded certificate revocation lists (CRLs) for the trust store. There can be one CRL per certificate authority (CA) in the trust store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500000.
Pattern: `[\P{C}\s]*`
Required: No

 ** KmsKeyArn **   <a name="sesmailmanager-Type-TrustStore-KmsKeyArn"></a>
The Amazon Resource Name (ARN) of the KMS key used to encrypt the trust store contents.
Type: String
Pattern: `arn:aws(|-cn|-us-gov|-eusc):kms:[a-z0-9-]{1,20}:[0-9]{12}:(key|alias)/.+`
Required: No

## See Also
<a name="API_TrustStore_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/TrustStore)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/TrustStore)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/TrustStore)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Mail Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sesmailmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
