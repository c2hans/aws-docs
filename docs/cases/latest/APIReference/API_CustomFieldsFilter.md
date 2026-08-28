---
source_url: https://docs.aws.amazon.com/cases/latest/APIReference/API_CustomFieldsFilter.html
---

# CustomFieldsFilter
<a name="API_connect-cases_CustomFieldsFilter"></a>

A filter for fields in `Custom` type related items. Only one value can be provided.

## Contents
<a name="API_connect-cases_CustomFieldsFilter_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** andAll **   <a name="connect-Type-connect-cases_CustomFieldsFilter-andAll"></a>
Provides "and all" filtering.
Type: Array of [CustomFieldsFilter](#API_connect-cases_CustomFieldsFilter) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** field **   <a name="connect-Type-connect-cases_CustomFieldsFilter-field"></a>
A filter for fields. Only one value can be provided.
Type: [FieldFilter](API_connect-cases_FieldFilter.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** not **   <a name="connect-Type-connect-cases_CustomFieldsFilter-not"></a>
Excludes items matching the filter.
Type: [CustomFieldsFilter](#API_connect-cases_CustomFieldsFilter) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** orAll **   <a name="connect-Type-connect-cases_CustomFieldsFilter-orAll"></a>
Provides "or all" filtering.
Type: Array of [CustomFieldsFilter](#API_connect-cases_CustomFieldsFilter) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

## See Also
<a name="API_connect-cases_CustomFieldsFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/CustomFieldsFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/CustomFieldsFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/CustomFieldsFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
