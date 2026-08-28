---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_IngressPointAuthConfiguration.html
---

# IngressPointAuthConfiguration
<a name="API_IngressPointAuthConfiguration"></a>

The authentication configuration for the ingress endpoint resource.

## Contents
<a name="API_IngressPointAuthConfiguration_Contents"></a>

 ** IngressPointPasswordConfiguration **   <a name="sesmailmanager-Type-IngressPointAuthConfiguration-IngressPointPasswordConfiguration"></a>
The ingress endpoint password configuration for the ingress endpoint resource.
Type: [IngressPointPasswordConfiguration](API_IngressPointPasswordConfiguration.md) object
Required: No

 ** SecretArn **   <a name="sesmailmanager-Type-IngressPointAuthConfiguration-SecretArn"></a>
The ingress endpoint SecretsManager::Secret ARN configuration for the ingress endpoint resource.
Type: String
Pattern: `arn:(aws|aws-cn|aws-us-gov|aws-eusc):secretsmanager:[a-z0-9-]+:\d{12}:secret:[a-zA-Z0-9/_+=,.@-]+`
Required: No

 ** TlsAuthConfiguration **   <a name="sesmailmanager-Type-IngressPointAuthConfiguration-TlsAuthConfiguration"></a>
The mutual TLS authentication configuration for the ingress endpoint resource.
Type: [TlsAuthConfiguration](API_TlsAuthConfiguration.md) object
Required: No

## See Also
<a name="API_IngressPointAuthConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/IngressPointAuthConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/IngressPointAuthConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/IngressPointAuthConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Mail Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sesmailmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
