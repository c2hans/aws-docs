---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_EnvironmentTemplateSummary.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# EnvironmentTemplateSummary
<a name="API_EnvironmentTemplateSummary"></a>

The environment template data.

## Contents
<a name="API_EnvironmentTemplateSummary_Contents"></a>

 ** arn **   <a name="proton-Type-EnvironmentTemplateSummary-arn"></a>
The Amazon Resource Name (ARN) of the environment template.
Type: String
Required: Yes

 ** createdAt **   <a name="proton-Type-EnvironmentTemplateSummary-createdAt"></a>
The time when the environment template was created.
Type: Timestamp
Required: Yes

 ** lastModifiedAt **   <a name="proton-Type-EnvironmentTemplateSummary-lastModifiedAt"></a>
The time when the environment template was last modified.
Type: Timestamp
Required: Yes

 ** name **   <a name="proton-Type-EnvironmentTemplateSummary-name"></a>
The name of the environment template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

 ** description **   <a name="proton-Type-EnvironmentTemplateSummary-description"></a>
A description of the environment template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** displayName **   <a name="proton-Type-EnvironmentTemplateSummary-displayName"></a>
The name of the environment template as displayed in the developer interface.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** provisioning **   <a name="proton-Type-EnvironmentTemplateSummary-provisioning"></a>
When included, indicates that the environment template is for customer provisioned and managed infrastructure.
Type: String
Valid Values: `CUSTOMER_MANAGED`
Required: No

 ** recommendedVersion **   <a name="proton-Type-EnvironmentTemplateSummary-recommendedVersion"></a>
The recommended version of the environment template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `(0|([1-9]{1}\d*)).(0|([1-9]{1}\d*))`
Required: No

## See Also
<a name="API_EnvironmentTemplateSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/EnvironmentTemplateSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/EnvironmentTemplateSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/EnvironmentTemplateSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Proton. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query proton` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
