---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UIColorPalette.html
---

# UIColorPalette
<a name="API_UIColorPalette"></a>

The theme colors that apply to UI and to charts, excluding data colors. The colors description is a hexadecimal color code that consists of six alphanumerical characters, prefixed with `#`, for example \#37BFF5. For more information, see [Using Themes in Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/themes-in-quicksight.html) in the *Quick Sight User Guide.*

## Contents
<a name="API_UIColorPalette_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Accent **   <a name="QS-Type-UIColorPalette-Accent"></a>
This color is that applies to selected states and buttons.
Type: String
Pattern: `^#[A-F0-9]{6}$`
Required: No

 ** AccentForeground **   <a name="QS-Type-UIColorPalette-AccentForeground"></a>
The foreground color that applies to any text or other elements that appear over the accent color.
Type: String
Pattern: `^#[A-F0-9]{6}$`
Required: No

 ** Danger **   <a name="QS-Type-UIColorPalette-Danger"></a>
The color that applies to error messages.
Type: String
Pattern: `^#[A-F0-9]{6}$`
Required: No

 ** DangerForeground **   <a name="QS-Type-UIColorPalette-DangerForeground"></a>
The foreground color that applies to any text or other elements that appear over the error color.
Type: String
Pattern: `^#[A-F0-9]{6}$`
Required: No

 ** Dimension **   <a name="QS-Type-UIColorPalette-Dimension"></a>
The color that applies to the names of fields that are identified as dimensions.
Type: String
Pattern: `^#[A-F0-9]{6}$`
Required: No

 ** DimensionForeground **   <a name="QS-Type-UIColorPalette-DimensionForeground"></a>
The foreground color that applies to any text or other elements that appear over the dimension color.
Type: String
Pattern: `^#[A-F0-9]{6}$`
Required: No

 ** Measure **   <a name="QS-Type-UIColorPalette-Measure"></a>
The color that applies to the names of fields that are identified as measures.
Type: String
Pattern: `^#[A-F0-9]{6}$`
Required: No

 ** MeasureForeground **   <a name="QS-Type-UIColorPalette-MeasureForeground"></a>
The foreground color that applies to any text or other elements that appear over the measure color.
Type: String
Pattern: `^#[A-F0-9]{6}$`
Required: No

 ** PrimaryBackground **   <a name="QS-Type-UIColorPalette-PrimaryBackground"></a>
The background color that applies to visuals and other high emphasis UI.
Type: String
Pattern: `^#[A-F0-9]{6}$`
Required: No

 ** PrimaryForeground **   <a name="QS-Type-UIColorPalette-PrimaryForeground"></a>
The color of text and other foreground elements that appear over the primary background regions, such as grid lines, borders, table banding, icons, and so on.
Type: String
Pattern: `^#[A-F0-9]{6}$`
Required: No

 ** SecondaryBackground **   <a name="QS-Type-UIColorPalette-SecondaryBackground"></a>
The background color that applies to the sheet background and sheet controls.
Type: String
Pattern: `^#[A-F0-9]{6}$`
Required: No

 ** SecondaryForeground **   <a name="QS-Type-UIColorPalette-SecondaryForeground"></a>
The foreground color that applies to any sheet title, sheet control text, or UI that appears over the secondary background.
Type: String
Pattern: `^#[A-F0-9]{6}$`
Required: No

 ** Success **   <a name="QS-Type-UIColorPalette-Success"></a>
The color that applies to success messages, for example the check mark for a successful download.
Type: String
Pattern: `^#[A-F0-9]{6}$`
Required: No

 ** SuccessForeground **   <a name="QS-Type-UIColorPalette-SuccessForeground"></a>
The foreground color that applies to any text or other elements that appear over the success color.
Type: String
Pattern: `^#[A-F0-9]{6}$`
Required: No

 ** Warning **   <a name="QS-Type-UIColorPalette-Warning"></a>
This color that applies to warning and informational messages.
Type: String
Pattern: `^#[A-F0-9]{6}$`
Required: No

 ** WarningForeground **   <a name="QS-Type-UIColorPalette-WarningForeground"></a>
The foreground color that applies to any text or other elements that appear over the warning color.
Type: String
Pattern: `^#[A-F0-9]{6}$`
Required: No

## See Also
<a name="API_UIColorPalette_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UIColorPalette)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UIColorPalette)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UIColorPalette)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
