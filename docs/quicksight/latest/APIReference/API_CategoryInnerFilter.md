---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CategoryInnerFilter.html
---

# CategoryInnerFilter
<a name="API_CategoryInnerFilter"></a>

A `CategoryInnerFilter` filters text values for the `NestedFilter`.

## Contents
<a name="API_CategoryInnerFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Column **   <a name="QS-Type-CategoryInnerFilter-Column"></a>
A column of a data set.
Type: [ColumnIdentifier](API_ColumnIdentifier.md) object
Required: Yes

 ** Configuration **   <a name="QS-Type-CategoryInnerFilter-Configuration"></a>
The configuration for a `CategoryFilter`.
This is a union type structure. For this structure to be valid, only one of the attributes can be defined.
Type: [CategoryFilterConfiguration](API_CategoryFilterConfiguration.md) object
Required: Yes

 ** DefaultFilterControlConfiguration **   <a name="QS-Type-CategoryInnerFilter-DefaultFilterControlConfiguration"></a>
The default configuration for all dependent controls of the filter.
Type: [DefaultFilterControlConfiguration](API_DefaultFilterControlConfiguration.md) object
Required: No

## See Also
<a name="API_CategoryInnerFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CategoryInnerFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CategoryInnerFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CategoryInnerFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
