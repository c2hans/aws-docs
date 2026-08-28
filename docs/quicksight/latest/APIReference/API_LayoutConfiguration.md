---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_LayoutConfiguration.html
---

# LayoutConfiguration
<a name="API_LayoutConfiguration"></a>

The configuration that determines what the type of layout will be used on a sheet.

This is a union type structure. For this structure to be valid, only one of the attributes can be defined.

## Contents
<a name="API_LayoutConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** FreeFormLayout **   <a name="QS-Type-LayoutConfiguration-FreeFormLayout"></a>
A free-form is optimized for a fixed width and has more control over the exact placement of layout elements.
Type: [FreeFormLayoutConfiguration](API_FreeFormLayoutConfiguration.md) object
Required: No

 ** GridLayout **   <a name="QS-Type-LayoutConfiguration-GridLayout"></a>
A type of layout that can be used on a sheet. In a grid layout, visuals snap to a grid with standard spacing and alignment. Dashboards are displayed as designed, with options to fit to screen or view at actual size. A grid layout can be configured to behave in one of two ways when the viewport is resized: `FIXED` or `RESPONSIVE`.
Type: [GridLayoutConfiguration](API_GridLayoutConfiguration.md) object
Required: No

 ** SectionBasedLayout **   <a name="QS-Type-LayoutConfiguration-SectionBasedLayout"></a>
A section based layout organizes visuals into multiple sections and has customized header, footer and page break.
Type: [SectionBasedLayoutConfiguration](API_SectionBasedLayoutConfiguration.md) object
Required: No

## See Also
<a name="API_LayoutConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/LayoutConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/LayoutConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/LayoutConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
