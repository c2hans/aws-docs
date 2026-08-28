---
source_url: https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_CdnAuthConfiguration.html
---

# CdnAuthConfiguration
<a name="API_CdnAuthConfiguration"></a>

The settings to enable CDN authorization headers in MediaPackage.

## Contents
<a name="API_CdnAuthConfiguration_Contents"></a>

 ** CdnIdentifierSecretArns **   <a name="mediapackage-Type-CdnAuthConfiguration-CdnIdentifierSecretArns"></a>
The ARN for the secret in Secrets Manager that your CDN uses for authorization to access the endpoint.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

 ** SecretsRoleArn **   <a name="mediapackage-Type-CdnAuthConfiguration-SecretsRoleArn"></a>
The ARN for the IAM role that gives MediaPackage read access to Secrets Manager and AWS KMS for CDN authorization.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

## See Also
<a name="API_CdnAuthConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediapackagev2-2022-12-25/CdnAuthConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediapackagev2-2022-12-25/CdnAuthConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediapackagev2-2022-12-25/CdnAuthConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V2 Live API. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
