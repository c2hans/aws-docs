---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_InsightConfiguration.html
---

# InsightConfiguration
<a name="API_InsightConfiguration"></a>

The configuration of an insight visual.

## Contents
<a name="API_InsightConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Computations **   <a name="QS-Type-InsightConfiguration-Computations"></a>
The computations configurations of the insight visual
Type: Array of [Computation](API_Computation.md) objects
Array Members: Maximum number of 100 items.
Required: No

 ** CustomNarrative **   <a name="QS-Type-InsightConfiguration-CustomNarrative"></a>
The custom narrative of the insight visual.
Type: [CustomNarrativeOptions](API_CustomNarrativeOptions.md) object
Required: No

 ** Interactions **   <a name="QS-Type-InsightConfiguration-Interactions"></a>
The general visual interactions setup for a visual.
Type: [VisualInteractionOptions](API_VisualInteractionOptions.md) object
Required: No

## See Also
<a name="API_InsightConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/InsightConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/InsightConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/InsightConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
