---
source_url: https://docs.aws.amazon.com/nova-act/latest/APIReference/API_CompatibilityInformation.html
---

# CompatibilityInformation
<a name="API_CompatibilityInformation"></a>

Information about client compatibility and supported model versions.

## Contents
<a name="API_CompatibilityInformation_Contents"></a>

 ** clientCompatibilityVersion **   <a name="novaact-Type-CompatibilityInformation-clientCompatibilityVersion"></a>
The client compatibility version that was requested.
Type: Integer
Required: Yes

 ** supportedModelIds **   <a name="novaact-Type-CompatibilityInformation-supportedModelIds"></a>
A list of model IDs that are supported for the client compatibility version.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** message **   <a name="novaact-Type-CompatibilityInformation-message"></a>
Additional information about compatibility requirements or recommendations.
Type: String
Pattern: `[\s\S]+`
Required: No

## See Also
<a name="API_CompatibilityInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/nova-act-2025-08-22/CompatibilityInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/nova-act-2025-08-22/CompatibilityInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/nova-act-2025-08-22/CompatibilityInformation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Nova Act. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query nova-act` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
