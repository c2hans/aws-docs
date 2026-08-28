---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_NumericalDimensionField.html
---

# NumericalDimensionField
<a name="API_NumericalDimensionField"></a>

The dimension type field with numerical type columns.

## Contents
<a name="API_NumericalDimensionField_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Column **   <a name="QS-Type-NumericalDimensionField-Column"></a>
The column that is used in the `NumericalDimensionField`.
Type: [ColumnIdentifier](API_ColumnIdentifier.md) object
Required: Yes

 ** FieldId **   <a name="QS-Type-NumericalDimensionField-FieldId"></a>
The custom field ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

 ** FormatConfiguration **   <a name="QS-Type-NumericalDimensionField-FormatConfiguration"></a>
The format configuration of the field.
Type: [NumberFormatConfiguration](API_NumberFormatConfiguration.md) object
Required: No

 ** HierarchyId **   <a name="QS-Type-NumericalDimensionField-HierarchyId"></a>
The custom hierarchy ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

## See Also
<a name="API_NumericalDimensionField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/NumericalDimensionField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/NumericalDimensionField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/NumericalDimensionField)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
