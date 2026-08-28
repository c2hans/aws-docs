---
source_url: https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_CredentialsProvider.html
---

# CredentialsProvider
<a name="API_CredentialsProvider"></a>

Contains information about the credential provider for user administration.

## Contents
<a name="API_CredentialsProvider_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** SecretsManagerCredentialsProvider **   <a name="licensemanagerusersubscriptions-Type-CredentialsProvider-SecretsManagerCredentialsProvider"></a>
Identifies the AWS Secrets Manager secret that contains credentials needed for user administration in the Active Directory.
Type: [SecretsManagerCredentialsProvider](API_SecretsManagerCredentialsProvider.md) object
Required: No

## See Also
<a name="API_CredentialsProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-user-subscriptions-2018-05-10/CredentialsProvider)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-user-subscriptions-2018-05-10/CredentialsProvider)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-user-subscriptions-2018-05-10/CredentialsProvider)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for License Manager User Subscriptions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager-user-subscriptions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
