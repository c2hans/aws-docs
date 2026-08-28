---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_FreeFormLayoutElement.html
---

# FreeFormLayoutElement
<a name="API_FreeFormLayoutElement"></a>

An element within a free-form layout.

## Contents
<a name="API_FreeFormLayoutElement_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ElementId **   <a name="QS-Type-FreeFormLayoutElement-ElementId"></a>
A unique identifier for an element within a free-form layout.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** ElementType **   <a name="QS-Type-FreeFormLayoutElement-ElementType"></a>
The type of element.
Type: String
Valid Values: `VISUAL | FILTER_CONTROL | PARAMETER_CONTROL | TEXT_BOX | IMAGE`
Required: Yes

 ** Height **   <a name="QS-Type-FreeFormLayoutElement-Height"></a>
The height of an element within a free-form layout.
Type: String
Required: Yes

 ** Width **   <a name="QS-Type-FreeFormLayoutElement-Width"></a>
The width of an element within a free-form layout.
Type: String
Required: Yes

 ** XAxisLocation **   <a name="QS-Type-FreeFormLayoutElement-XAxisLocation"></a>
The x-axis coordinate of the element.
Type: String
Required: Yes

 ** YAxisLocation **   <a name="QS-Type-FreeFormLayoutElement-YAxisLocation"></a>
The y-axis coordinate of the element.
Type: String
Required: Yes

 ** BackgroundStyle **   <a name="QS-Type-FreeFormLayoutElement-BackgroundStyle"></a>
The background style configuration of a free-form layout element.
Type: [FreeFormLayoutElementBackgroundStyle](API_FreeFormLayoutElementBackgroundStyle.md) object
Required: No

 ** BorderRadius **   <a name="QS-Type-FreeFormLayoutElement-BorderRadius"></a>
The border radius of a free-form layout element.
Type: String
Length Constraints: Maximum length of 50.
Required: No

 ** BorderStyle **   <a name="QS-Type-FreeFormLayoutElement-BorderStyle"></a>
The border style configuration of a free-form layout element.
Type: [FreeFormLayoutElementBorderStyle](API_FreeFormLayoutElementBorderStyle.md) object
Required: No

 ** LoadingAnimation **   <a name="QS-Type-FreeFormLayoutElement-LoadingAnimation"></a>
The loading animation configuration of a free-form layout element.
Type: [LoadingAnimation](API_LoadingAnimation.md) object
Required: No

 ** Padding **   <a name="QS-Type-FreeFormLayoutElement-Padding"></a>
The padding of a free-form layout element.
Type: String
Length Constraints: Maximum length of 200.
Required: No

 ** RenderingRules **   <a name="QS-Type-FreeFormLayoutElement-RenderingRules"></a>
The rendering rules that determine when an element should be displayed within a free-form layout.
Type: Array of [SheetElementRenderingRule](API_SheetElementRenderingRule.md) objects
Array Members: Maximum number of 10000 items.
Required: No

 ** SelectedBorderStyle **   <a name="QS-Type-FreeFormLayoutElement-SelectedBorderStyle"></a>
The border style configuration of a free-form layout element. This border style is used when the element is selected.
Type: [FreeFormLayoutElementBorderStyle](API_FreeFormLayoutElementBorderStyle.md) object
Required: No

 ** Visibility **   <a name="QS-Type-FreeFormLayoutElement-Visibility"></a>
The visibility of an element within a free-form layout.
Type: String
Valid Values: `HIDDEN | VISIBLE`
Required: No

## See Also
<a name="API_FreeFormLayoutElement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/FreeFormLayoutElement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/FreeFormLayoutElement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/FreeFormLayoutElement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
