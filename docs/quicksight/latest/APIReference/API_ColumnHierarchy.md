---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ColumnHierarchy.html
---

# ColumnHierarchy
<a name="API_ColumnHierarchy"></a>

The option that determines the hierarchy of the fields for a visual element.

## Contents
<a name="API_ColumnHierarchy_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DateTimeHierarchy **   <a name="QS-Type-ColumnHierarchy-DateTimeHierarchy"></a>
The option that determines the hierarchy of any `DateTime` fields.
Type: [DateTimeHierarchy](API_DateTimeHierarchy.md) object
Required: No

 ** ExplicitHierarchy **   <a name="QS-Type-ColumnHierarchy-ExplicitHierarchy"></a>
The option that determines the hierarchy of the fields that are built within a visual's field wells. These fields can't be duplicated to other visuals.
Type: [ExplicitHierarchy](API_ExplicitHierarchy.md) object
Required: No

 ** PredefinedHierarchy **   <a name="QS-Type-ColumnHierarchy-PredefinedHierarchy"></a>
The option that determines the hierarchy of the fields that are defined during data preparation. These fields are available to use in any analysis that uses the data source.
Type: [PredefinedHierarchy](API_PredefinedHierarchy.md) object
Required: No

## See Also
<a name="API_ColumnHierarchy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ColumnHierarchy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ColumnHierarchy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ColumnHierarchy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
