---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_EmptyVisual.html
---

# EmptyVisual
<a name="API_EmptyVisual"></a>

An empty visual.

Empty visuals are used in layouts but have not been configured to show any data. A new visual created in the Quick Sight console is considered an `EmptyVisual` until a visual type is selected.

## Contents
<a name="API_EmptyVisual_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** VisualId **   <a name="QS-Type-EmptyVisual-VisualId"></a>
The unique identifier of a visual. This identifier must be unique within the context of a dashboard, template, or analysis. Two dashboards, analyses, or templates can have visuals with the same identifiers.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** Actions **   <a name="QS-Type-EmptyVisual-Actions"></a>
The list of custom actions that are configured for a visual.
Type: Array of [VisualCustomAction](API_VisualCustomAction.md) objects
Array Members: Maximum number of 10 items.
Required: No

 ** DataSetIdentifier **   <a name="QS-Type-EmptyVisual-DataSetIdentifier"></a>
The data set that is used in the empty visual. Every visual requires a dataset or a topic to render.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** TopicIdentifier **   <a name="QS-Type-EmptyVisual-TopicIdentifier"></a>
The topic that is used in the empty visual. Every visual requires a dataset or a topic to render.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_EmptyVisual_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/EmptyVisual)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/EmptyVisual)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/EmptyVisual)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
