---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_HallucinationReductionConfiguration.html
---

# HallucinationReductionConfiguration
<a name="API_HallucinationReductionConfiguration"></a>

Configuration information required to setup hallucination reduction. For more information, see [ hallucination reduction](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/hallucination-reduction.html).

**Note**
The hallucination reduction feature won't work if chat orchestration controls are enabled for your application.

## Contents
<a name="API_HallucinationReductionConfiguration_Contents"></a>

 ** hallucinationReductionControl **   <a name="qbusiness-Type-HallucinationReductionConfiguration-hallucinationReductionControl"></a>
Controls whether hallucination reduction has been enabled or disabled for your application. The default status is `DISABLED`.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_HallucinationReductionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/HallucinationReductionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/HallucinationReductionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/HallucinationReductionConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
