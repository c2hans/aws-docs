---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TopicVisual.html
---

# TopicVisual
<a name="API_TopicVisual"></a>

The definition for a `TopicVisual`.

## Contents
<a name="API_TopicVisual_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Ir **   <a name="QS-Type-TopicVisual-Ir"></a>
The ir for the `TopicVisual`.
Type: [TopicIR](API_TopicIR.md) object
Required: No

 ** Role **   <a name="QS-Type-TopicVisual-Role"></a>
The role for the `TopicVisual`.
Type: String
Valid Values: `PRIMARY | COMPLIMENTARY | MULTI_INTENT | FALLBACK | FRAGMENT`
Required: No

 ** SupportingVisuals **   <a name="QS-Type-TopicVisual-SupportingVisuals"></a>
The supporting visuals for the `TopicVisual`.
Type: Array of [TopicVisual](#API_TopicVisual) objects
Required: No

 ** VisualId **   <a name="QS-Type-TopicVisual-VisualId"></a>
The visual ID for the `TopicVisual`.
Type: String
Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_TopicVisual_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TopicVisual)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TopicVisual)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TopicVisual)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
