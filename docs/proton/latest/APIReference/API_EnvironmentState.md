---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_EnvironmentState.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# EnvironmentState
<a name="API_EnvironmentState"></a>

The detailed data about the current state of the environment.

## Contents
<a name="API_EnvironmentState_Contents"></a>

 ** templateMajorVersion **   <a name="proton-Type-EnvironmentState-templateMajorVersion"></a>
The major version of the environment template that was used to create the environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `(0|([1-9]{1}\d*))`
Required: Yes

 ** templateMinorVersion **   <a name="proton-Type-EnvironmentState-templateMinorVersion"></a>
The minor version of the environment template that was used to create the environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `(0|([1-9]{1}\d*))`
Required: Yes

 ** templateName **   <a name="proton-Type-EnvironmentState-templateName"></a>
The name of the environment template that was used to create the environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

 ** spec **   <a name="proton-Type-EnvironmentState-spec"></a>
The environment spec that was used to create the environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 51200.
Required: No

## See Also
<a name="API_EnvironmentState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/EnvironmentState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/EnvironmentState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/EnvironmentState)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Proton. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query proton` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
