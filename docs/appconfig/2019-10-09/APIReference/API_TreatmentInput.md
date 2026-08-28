---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_TreatmentInput.html
---

# TreatmentInput
<a name="API_TreatmentInput"></a>

Input structure for defining a treatment when creating or updating an experiment definition.

## Contents
<a name="API_TreatmentInput_Contents"></a>

 ** FlagValue **   <a name="appconfig-Type-TreatmentInput-FlagValue"></a>
The feature flag value to serve to users assigned to this treatment.
Type: [FlagValue](API_FlagValue.md) object
Required: Yes

 ** Weight **   <a name="appconfig-Type-TreatmentInput-Weight"></a>
The traffic allocation weight for this treatment.
Type: Float
Valid Range: Minimum value of 0.0.
Required: Yes

 ** Description **   <a name="appconfig-Type-TreatmentInput-Description"></a>
A description of the treatment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_TreatmentInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/TreatmentInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/TreatmentInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/TreatmentInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppConfig. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appconfig` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
