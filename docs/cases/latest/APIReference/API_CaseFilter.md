---
source_url: https://docs.aws.amazon.com/cases/latest/APIReference/API_CaseFilter.html
---

# CaseFilter
<a name="API_connect-cases_CaseFilter"></a>

A filter for cases. Only one value can be provided.

## Contents
<a name="API_connect-cases_CaseFilter_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** andAll **   <a name="connect-Type-connect-cases_CaseFilter-andAll"></a>
Provides "and all" filtering.
Type: Array of [CaseFilter](#API_connect-cases_CaseFilter) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** field **   <a name="connect-Type-connect-cases_CaseFilter-field"></a>
A list of fields to filter on.
Type: [FieldFilter](API_connect-cases_FieldFilter.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** not **   <a name="connect-Type-connect-cases_CaseFilter-not"></a>
A filter for cases. Only one value can be provided.
Type: [CaseFilter](#API_connect-cases_CaseFilter) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** orAll **   <a name="connect-Type-connect-cases_CaseFilter-orAll"></a>
Provides "or all" filtering.
Type: Array of [CaseFilter](#API_connect-cases_CaseFilter) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** tag **   <a name="connect-Type-connect-cases_CaseFilter-tag"></a>
A list of tags to filter on.
Type: [TagFilter](API_connect-cases_TagFilter.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_connect-cases_CaseFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/CaseFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/CaseFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/CaseFilter)
