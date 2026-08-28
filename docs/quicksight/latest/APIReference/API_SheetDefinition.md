---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SheetDefinition.html
---

# SheetDefinition
<a name="API_SheetDefinition"></a>

A sheet is an object that contains a set of visuals that are viewed together on one page in a paginated report. Every analysis and dashboard must contain at least one sheet.

## Contents
<a name="API_SheetDefinition_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** SheetId **   <a name="QS-Type-SheetDefinition-SheetId"></a>
The unique identifier of a sheet.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** ContentType **   <a name="QS-Type-SheetDefinition-ContentType"></a>
The layout content type of the sheet. Choose one of the following options:
+  `PAGINATED`: Creates a sheet for a paginated report.
+  `INTERACTIVE`: Creates a sheet for an interactive dashboard.
Type: String
Valid Values: `PAGINATED | INTERACTIVE`
Required: No

 ** CustomActionDefaults **   <a name="QS-Type-SheetDefinition-CustomActionDefaults"></a>
A list of visual custom actions for the sheet.
Type: [VisualCustomActionDefaults](API_VisualCustomActionDefaults.md) object
Required: No

 ** Description **   <a name="QS-Type-SheetDefinition-Description"></a>
A description of the sheet.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** FilterControls **   <a name="QS-Type-SheetDefinition-FilterControls"></a>
The list of filter controls that are on a sheet.
For more information, see [Adding filter controls to analysis sheets](https://docs.aws.amazon.com/quicksight/latest/user/filter-controls.html) in the *Amazon Quick Suite User Guide*.
Type: Array of [FilterControl](API_FilterControl.md) objects
Array Members: Maximum number of 200 items.
Required: No

 ** Images **   <a name="QS-Type-SheetDefinition-Images"></a>
A list of images on a sheet.
Type: Array of [SheetImage](API_SheetImage.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** Layouts **   <a name="QS-Type-SheetDefinition-Layouts"></a>
Layouts define how the components of a sheet are arranged.
For more information, see [Types of layout](https://docs.aws.amazon.com/quicksight/latest/user/types-of-layout.html) in the *Amazon Quick Suite User Guide*.
Type: Array of [Layout](API_Layout.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** Name **   <a name="QS-Type-SheetDefinition-Name"></a>
The name of the sheet. This name is displayed on the sheet's tab in the Quick console.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** ParameterControls **   <a name="QS-Type-SheetDefinition-ParameterControls"></a>
The list of parameter controls that are on a sheet.
For more information, see [Using a Control with a Parameter in Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/parameters-controls.html) in the *Amazon Quick Suite User Guide*.
Type: Array of [ParameterControl](API_ParameterControl.md) objects
Array Members: Maximum number of 200 items.
Required: No

 ** SheetControlLayouts **   <a name="QS-Type-SheetDefinition-SheetControlLayouts"></a>
The control layouts of the sheet.
Type: Array of [SheetControlLayout](API_SheetControlLayout.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

 ** TextBoxes **   <a name="QS-Type-SheetDefinition-TextBoxes"></a>
The text boxes that are on a sheet.
Type: Array of [SheetTextBox](API_SheetTextBox.md) objects
Array Members: Maximum number of 100 items.
Required: No

 ** Title **   <a name="QS-Type-SheetDefinition-Title"></a>
The title of the sheet.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** Visuals **   <a name="QS-Type-SheetDefinition-Visuals"></a>
A list of the visuals that are on a sheet. Visual placement is determined by the layout of the sheet.
Type: Array of [Visual](API_Visual.md) objects
Array Members: Maximum number of 75 items.
Required: No

## See Also
<a name="API_SheetDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/SheetDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/SheetDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/SheetDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
