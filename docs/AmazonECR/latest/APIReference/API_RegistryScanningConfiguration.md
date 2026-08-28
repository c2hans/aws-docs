---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_RegistryScanningConfiguration.html
---

# RegistryScanningConfiguration
<a name="API_RegistryScanningConfiguration"></a>

The scanning configuration for a private registry.

## Contents
<a name="API_RegistryScanningConfiguration_Contents"></a>

 ** rules **   <a name="ECR-Type-RegistryScanningConfiguration-rules"></a>
The scanning rules associated with the registry.
Type: Array of [RegistryScanningRule](API_RegistryScanningRule.md) objects
Array Members: Minimum number of 0 items. Maximum number of 2 items.
Required: No

 ** scanType **   <a name="ECR-Type-RegistryScanningConfiguration-scanType"></a>
The type of scanning configured for the registry.
Type: String
Valid Values: `BASIC | ENHANCED`
Required: No

## See Also
<a name="API_RegistryScanningConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/RegistryScanningConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/RegistryScanningConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/RegistryScanningConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
