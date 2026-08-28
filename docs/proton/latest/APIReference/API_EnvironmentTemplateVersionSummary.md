---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_EnvironmentTemplateVersionSummary.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# EnvironmentTemplateVersionSummary
<a name="API_EnvironmentTemplateVersionSummary"></a>

A summary of the version of an environment template detail data.

## Contents
<a name="API_EnvironmentTemplateVersionSummary_Contents"></a>

 ** arn **   <a name="proton-Type-EnvironmentTemplateVersionSummary-arn"></a>
The Amazon Resource Name (ARN) of the version of an environment template.
Type: String
Required: Yes

 ** createdAt **   <a name="proton-Type-EnvironmentTemplateVersionSummary-createdAt"></a>
The time when the version of an environment template was created.
Type: Timestamp
Required: Yes

 ** lastModifiedAt **   <a name="proton-Type-EnvironmentTemplateVersionSummary-lastModifiedAt"></a>
The time when the version of an environment template was last modified.
Type: Timestamp
Required: Yes

 ** majorVersion **   <a name="proton-Type-EnvironmentTemplateVersionSummary-majorVersion"></a>
The latest major version that's associated with the version of an environment template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `(0|([1-9]{1}\d*))`
Required: Yes

 ** minorVersion **   <a name="proton-Type-EnvironmentTemplateVersionSummary-minorVersion"></a>
The version of an environment template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `(0|([1-9]{1}\d*))`
Required: Yes

 ** status **   <a name="proton-Type-EnvironmentTemplateVersionSummary-status"></a>
The status of the version of an environment template.
Type: String
Valid Values: `REGISTRATION_IN_PROGRESS | REGISTRATION_FAILED | DRAFT | PUBLISHED`
Required: Yes

 ** templateName **   <a name="proton-Type-EnvironmentTemplateVersionSummary-templateName"></a>
The name of the environment template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

 ** description **   <a name="proton-Type-EnvironmentTemplateVersionSummary-description"></a>
A description of the version of an environment template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** recommendedMinorVersion **   <a name="proton-Type-EnvironmentTemplateVersionSummary-recommendedMinorVersion"></a>
The recommended minor version of the environment template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `(0|([1-9]{1}\d*))`
Required: No

 ** statusMessage **   <a name="proton-Type-EnvironmentTemplateVersionSummary-statusMessage"></a>
The status message of the version of an environment template.
Type: String
Required: No

## See Also
<a name="API_EnvironmentTemplateVersionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/EnvironmentTemplateVersionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/EnvironmentTemplateVersionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/EnvironmentTemplateVersionSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Proton. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query proton` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
