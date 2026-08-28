---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_DifferentialPrivacyTemplateParametersInput.html
---

# DifferentialPrivacyTemplateParametersInput
<a name="API_DifferentialPrivacyTemplateParametersInput"></a>

The epsilon and noise parameter values that you want to use for the differential privacy template.

## Contents
<a name="API_DifferentialPrivacyTemplateParametersInput_Contents"></a>

 ** epsilon **   <a name="API-Type-DifferentialPrivacyTemplateParametersInput-epsilon"></a>
The epsilon value that you want to use.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 20.
Required: Yes

 ** usersNoisePerQuery **   <a name="API-Type-DifferentialPrivacyTemplateParametersInput-usersNoisePerQuery"></a>
Noise added per query is measured in terms of the number of users whose contributions you want to obscure. This value governs the rate at which the privacy budget is depleted.
Type: Integer
Valid Range: Minimum value of 10. Maximum value of 100.
Required: Yes

## See Also
<a name="API_DifferentialPrivacyTemplateParametersInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/DifferentialPrivacyTemplateParametersInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/DifferentialPrivacyTemplateParametersInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/DifferentialPrivacyTemplateParametersInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
