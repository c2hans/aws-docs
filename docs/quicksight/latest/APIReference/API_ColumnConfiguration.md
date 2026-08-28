---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ColumnConfiguration.html
---

# ColumnConfiguration
<a name="API_ColumnConfiguration"></a>

The general configuration of a column.

## Contents
<a name="API_ColumnConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Column **   <a name="QS-Type-ColumnConfiguration-Column"></a>
The column.
Type: [ColumnIdentifier](API_ColumnIdentifier.md) object
Required: Yes

 ** ColorsConfiguration **   <a name="QS-Type-ColumnConfiguration-ColorsConfiguration"></a>
The color configurations of the column.
Type: [ColorsConfiguration](API_ColorsConfiguration.md) object
Required: No

 ** DecalSettingsConfiguration **   <a name="QS-Type-ColumnConfiguration-DecalSettingsConfiguration"></a>
Decal configuration of the column.
Type: [DecalSettingsConfiguration](API_DecalSettingsConfiguration.md) object
Required: No

 ** FormatConfiguration **   <a name="QS-Type-ColumnConfiguration-FormatConfiguration"></a>
The format configuration of a column.
Type: [FormatConfiguration](API_FormatConfiguration.md) object
Required: No

 ** Role **   <a name="QS-Type-ColumnConfiguration-Role"></a>
The role of the column.
Type: String
Valid Values: `DIMENSION | MEASURE`
Required: No

## See Also
<a name="API_ColumnConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ColumnConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ColumnConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ColumnConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
