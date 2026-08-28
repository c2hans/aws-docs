---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_IngressPointConfiguration.html
---

# IngressPointConfiguration
<a name="API_IngressPointConfiguration"></a>

The configuration of the ingress endpoint resource.

## Contents
<a name="API_IngressPointConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** SecretArn **   <a name="sesmailmanager-Type-IngressPointConfiguration-SecretArn"></a>
The SecretsManager::Secret ARN of the ingress endpoint resource.
Type: String
Pattern: `arn:(aws|aws-cn|aws-us-gov|aws-eusc):secretsmanager:[a-z0-9-]+:\d{12}:secret:[a-zA-Z0-9/_+=,.@-]+`
Required: No

 ** SmtpPassword **   <a name="sesmailmanager-Type-IngressPointConfiguration-SmtpPassword"></a>
The password of the ingress endpoint resource.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 64.
Pattern: `[A-Za-z0-9!@#$%^&*()_+\-=\[\]{}|.,?]+`
Required: No

 ** TlsAuthConfiguration **   <a name="sesmailmanager-Type-IngressPointConfiguration-TlsAuthConfiguration"></a>
The mutual TLS authentication configuration of the ingress endpoint resource.
Type: [TlsAuthConfiguration](API_TlsAuthConfiguration.md) object
Required: No

## See Also
<a name="API_IngressPointConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/IngressPointConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/IngressPointConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/IngressPointConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Mail Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sesmailmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
